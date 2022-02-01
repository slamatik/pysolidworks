import requests
from bs4 import BeautifulSoup

# initial_link = 'http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html'
link = 'http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~'
# # link = 'http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActiveDrawingView.html'

# https://saralgyaan.com/posts/f-string-in-python-usage-guide/
# https://www.google.com/search?q=python+string+comprehension&oq=python+string+com&aqs=chrome.2.0i512l3j69i57j0i512j69i60l3.4677j0j7&sourceid=chrome&ie=UTF-8


name, description = 'CreateText2', 'Creates a note containing the specified text at a given location.'

new_name = f'{name[0].lower()}'
for letter in name[1:]:
    if letter.isupper():
        new_name += '_'
    if letter.isnumeric():
        continue
    new_name += letter.lower()

r = requests.get(link + name + '.html')
soup = BeautifulSoup(r.text, "html.parser")
data = soup.find('dl')
dt = data.find_all('dt')
dd = data.find_all('dd')

dt_str = [i.text for i in dt]
dd_str = [i.text for i in dd]

combined_str = zip(dt_str, dd_str)
method_description = ''
for i in combined_str:
    method_description += '\t:param ' + ': '.join(i) + '\n'

result = f'def {new_name}(self, {", ".join(dt_str)}):\n' \
         f'\t"""\n' \
         f'\t{description}\n' \
         f'{method_description}' \
         f'\t"""\n' \
         f'\t# return self._instance.{name}({", ".join(dt_str)})\n' \
         f'\traise NotImplemented'

print(result)


# Case 1: No input.
# Case 2: multiple input lines.
# Case 3: 1 input line.

def create_text(self, TextString, TextX, TextY, TextZ, TextHeight, TextAngle):
    """
    Creates a note containing the specified text at a given location.
    :param TextString: User input text
    :param TextX: X text location in meters (see Remarks)
    :param TextY: Y text location in meters (see Remarks)
    :param TextZ: Z text location in meters (see Remarks)
    :param TextHeight: Text height in meters
    :param TextAngle: Text angle for rotated text in radians
    """
    # return self._instance.CreateText2(TextString, TextX, TextY, TextZ, TextHeight, TextAngle)
    raise NotImplemented
