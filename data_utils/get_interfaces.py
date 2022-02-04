from bs4 import BeautifulSoup
import requests
import os
import codecs

# update year
main_link = 'http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.'


def convert_name(name, method=True):
    new_name = f'{name[0].lower()}'
    for letter in name[1:]:
        if letter.isupper():
            new_name += '_'
        if letter.isnumeric():
            if method:
                continue
        new_name += letter.lower()
    return new_name


def get_interfaces():
    # update year
    link = 'https://help.solidworks.com/2021/english/api/SWHelp_List.html?id=8fa26215b1d9429e81182f4c8a113d10#Pg0'
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all('li')
    results = {}
    interfaces = []
    for i in data:
        interface_name = i.a.text
        if not interface_name.startswith('I'):
            continue
        # interfaces.append(link_members + interface_name + '_members.html')
        results[interface_name] = main_link + interface_name + '_members.html'
    return results


def get_members(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    data = soup.find_all('table', attrs={'class': 'FilteredItemListTable'})
    results = {}
    for i in data:
        tr = i.find_all('tr')
        for row in tr:
            name = row.find('td', class_='MembersLinkCell')
            description = row.find('td', class_='MembersDescriptionCell')
            if name:
                results[name.text] = description.text.strip().replace('\xa0', ' ')
    return results


interfaces = get_interfaces()
n = len(interfaces)
for idx, (interface, link) in enumerate(interfaces.items()):
    # if idx + 1 > 219:
    try:
        gettr_settr = False
        members = get_members(link)
        with codecs.open(interface.lower() + '.py', 'w', "utf-8-sig") as file:
            # with codecs.open(interface.lower() + '.txt', 'w', "utf-8-sig") as file:
            result = f'# {link}\n' \
                     f'class {interface}:\n' \
                     f'\tdef __init__(self, parent=None):\n' \
                     f'\t\tself._instance = parent\n\n'
            for method_name, description in members.items():
                if description.startswith('Obsolete'): continue
                if 'Gets or sets' in description: gettr_settr = True
                # print(description)
                # print(gettr_settr)
                link_to_method = f'{main_link}{interface}~{method_name}.html'
                my_method_name = convert_name(method_name, method=True)
                r = requests.get(link_to_method)
                soup = BeautifulSoup(r.text, "html.parser")
                data = soup.find('dl')
                attributes = True
                try:
                    dt = data.find_all('dt')
                    dd = data.find_all('dd')
                    dt_str = [i.text for i in dt]
                    dt_str = [convert_name(i, False) for i in dt_str]
                    dd_str = [i.text for i in dd]
                    combined_str = zip(dt_str, dd_str)
                    doc_string = ''
                    for i in combined_str:
                        doc_string += '\t\t:param ' + ': '.join(i) + '\n'
                except AttributeError:
                    attributes = False
                    dt_str = ''

                if gettr_settr:
                    result += f'\t@property\n' \
                              f'\tdef {my_method_name}(self):\n' \
                              f'\t\t"""{description}"""\n' \
                              f'\t\treturn self._instance.{method_name}\n' \
                              f'\n' \
                              f'\t@{my_method_name}.setter\n' \
                              f'\tdef {my_method_name}(self, value):\n' \
                              f'\t\t"""{description}"""\n' \
                              f'\t\tself._instance.{method_name} = value\n\n'

                else:
                    if attributes:
                        result += f'\tdef {my_method_name}(self, {", ".join(dt_str)}):\n' \
                                  f'\t\t"""\n' \
                                  f'\t\t{description}\n' \
                                  f'{doc_string}' \
                                  f'\t\t"""\n' \
                                  f'\t\t# return self._instance.{method_name}({", ".join(dt_str)})\n'
                    else:
                        result += f'\tdef {my_method_name}(self):\n' \
                                  f'\t\t"""{description}"""\n' \
                                  f'\t\t# return self._instance.{method_name}\n'
                    result += f'\t\traise NotImplemented\n\n'
                    result = result.replace("&nbsp", " ")
                # uni
                # print(my_method_name)
                # print(description)
                # if attributes:
                #     print(doc_string)
                # print()
            # print(result)
            file.write(result)
        # print(result)
        file.close()
    except Exception as e:
        print(e, interface, sep='\n')
    print(idx + 1, 'completed')
    # print(result)
    # if idx == 3: break

# if idx + 1 == 100: break
# if interface == 'IAdvancedSaveAsOptions': break
# 100 completed
