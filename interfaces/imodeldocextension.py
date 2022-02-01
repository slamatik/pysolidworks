from .icustompropertymanager import ICustomPropertyManager
import win32com.client as win32
import pythoncom
from com import Com


# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension.html

class IModelDocExtension:
    def __init__(self, parent):
        self._instance = parent.Extension

    def custom_property_manager(self, config_name):
        return ICustomPropertyManager(self._instance, config_name)

    def save_as(self, name, version=0, options=1, export_data=None):
        """
        Saves the active document to the specified name with advanced options.
        :param name: Full pathname of the document to save; the file extension indicates any conversion that should be performed
        :param version: Format in which to save this document
        :param options: Option indicating how to save the documen
        :param export_data: IExportPdfData object for exporting drawing sheets to PDF
        :return: True if the save is successful, false if not
        """
        arg1 = win32.VARIANT(pythoncom.VT_BSTR, name)
        arg2 = win32.VARIANT(pythoncom.VT_I4, version)
        arg3 = win32.VARIANT(pythoncom.VT_I4, options)
        arg5 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        arg6 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        # self._instance.SaveAs(arg1, arg2, arg3, arg4, arg5, arg6)
        result = self._instance.SaveAs(arg1, arg2, arg3, Com(export_data), arg5, arg6)
        print(arg5.value, arg6.value)
        return result
