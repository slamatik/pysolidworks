from interfaces.isldworks import ISldWorks
from doc import Doc
import win32com.client as win32
from interfaces.imodeldoc import IModelDoc
import os
import pythoncom


class SldWorks(ISldWorks):
    def __init__(self):
        super().__init__()

    def close_doc(self, name):
        self._isldworks.CloseDoc(name)

    def open_doc(self, file_name, options=1, configuration=str()):
        extension = os.path.splitext(file_name)[1]
        if extension == ".SLDPRT":
            doc_type = 1
        elif extension == ".SLDASM":
            doc_type = 2
        elif extension == ".SLDDRW":
            doc_type = 3
        else:
            raise ValueError("Incompatible File Type")

        arg1 = win32.VARIANT(pythoncom.VT_BSTR, file_name.replace("\\", "/"))
        arg2 = win32.VARIANT(pythoncom.VT_I4, doc_type)
        arg3 = win32.VARIANT(pythoncom.VT_I4, options)
        arg4 = win32.VARIANT(pythoncom.VT_BSTR, configuration)
        arg5 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        arg6 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        pointer = self._isldworks.OpenDoc6(arg1, arg2, arg3, arg4, arg5, arg6)
        return Doc(pointer), arg5.value, arg6.value

    def get_configuration_names(self, file_path_name):
        return self._isldworks.GetConfigurationNames(file_path_name)

    def get_model(self):
        return IModelDoc()
