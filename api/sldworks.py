import pandas as pd

from interfaces.isldworks import ISldWorks
from doc import Doc
import win32com.client as win32
from interfaces.imodeldoc import IModelDoc
import os
import pythoncom
import numpy as np


class SldWorks(ISldWorks):
    def __init__(self):
        super().__init__()

    # def close_doc(self, name):
    #     self._instance.CloseDoc(name)
    #
    # def open_doc(self, file_name, options=1, configuration=str()):
    #     extension = os.path.splitext(file_name)[1]
    #     if extension == ".SLDPRT":
    #         doc_type = 1
    #     elif extension == ".SLDASM":
    #         doc_type = 2
    #     elif extension == ".SLDDRW":
    #         doc_type = 3
    #     else:
    #         raise ValueError("Incompatible File Type")
    #
    #     arg1 = win32.VARIANT(pythoncom.VT_BSTR, file_name.replace("\\", "/"))
    #     arg2 = win32.VARIANT(pythoncom.VT_I4, doc_type)
    #     arg3 = win32.VARIANT(pythoncom.VT_I4, options)
    #     arg4 = win32.VARIANT(pythoncom.VT_BSTR, configuration)
    #     arg5 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
    #     arg6 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
    #     pointer = self._instance.OpenDoc6(arg1, arg2, arg3, arg4, arg5, arg6)
    #     return Doc(pointer), arg5.value, arg6.value
    #
    # def get_configuration_names(self, file_path_name):
    #     return self._instance.GetConfigurationNames(file_path_name)
    #
    # def get_model(self):
    #     return IModelDoc()

    """CUSTOM FUNCTIONS"""

    def export_custom_properties(self, folder=None, file_name=None):
        folder = folder if folder else input()
        file_name = file_name if file_name else input()
        df = pd.DataFrame()
        for file in os.listdir(folder):
            if file.endswith('.SLDDRW'):
                path = os.path.join(folder, file)
                part_number = file.split('.')[0]
                # print(path)
                model = self.open_doc(path)[0]
                model_doc_extension = model.extension
                custom_property_manager = model_doc_extension.custom_property_manager('')
                properties = np.array(custom_property_manager.get_all())
                names, values = ['Part Number'] + list(properties[:, 0]), [part_number] + list(properties[:, 2])
                df = df.append({key: value for key, value in zip(names, values)}, ignore_index=True)
                self.quit_doc(path)
        df.to_csv(file_name + '.csv',  index=False)

    def get_from_excel(self):
        pass

        # for file in os.listdir(folder):
        #     if file.endswith('SLDDRW'):
        #         path = os.path.join(folder, file)
        #         part_number = file.split('.')[0]
        #         drawing = sw.open_doc(path)
        #         model = sw.get_model()
        #         model_doc_extension = model.extension
        #         custom_property_manager = model_doc_extension.custom_property_manager('')
        #         description = df[df['Part Number'] == int(part_number)]['Description'].values[0]
        #         custom_property_manager.set('Description', str(description))
        #         model.save()
