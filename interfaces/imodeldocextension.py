from .icustompropertymanager import ICustomPropertyManager
from .iexportpdfdata import IExportPdfData
import win32com.client as win32
import pythoncom

# https://stackoverflow.com/questions/5453998/python-instance-to-com-object

# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension.html

class IModelDocExtension:
    def __init__(self, parent):
        self._instance = parent.Extension

    def custom_property_manager(self, config_name):
        return ICustomPropertyManager(self._instance, config_name)

    def save_as(self, name: str, version: int = 0, options: int = 1, export_data: object = None):
        arg1 = win32.VARIANT(pythoncom.VT_BSTR, name)
        arg2 = win32.VARIANT(pythoncom.VT_I4, version)
        arg3 = win32.VARIANT(pythoncom.VT_I4, options)
        arg4 = win32.VARIANT(pythoncom.VT_UNKNOWN, export_data)  # todo
        arg5 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        arg6 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        self._instance.SaveAs(arg1, arg2, arg3, arg4, arg5, arg6)
