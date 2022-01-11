from com import Com
from enums import *
import os
import pythoncom
import win32com.client as win32


class SldWorks:
    def __init__(self):
        self._isldworks = Com('SldWorks.Application')

    @property
    def active_doc(self):
        return self._isldworks.ActiveDoc

    @property
    def visible(self):
        return self._isldworks.Visible

    @visible.setter
    def visible(self, state):
        self._isldworks.Visible = state

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
        self._isldworks.OpenDoc6(arg1, arg2, arg3, arg4, arg5, arg6)
        return arg5.value, arg6.value

    def get_configuration_names(self, file_path_name):
        return self._isldworks.GetConfigurationNames(file_path_name)

    def get_model(self):
        return ModelDoc()


class ModelDoc:
    def __init__(self, parent=None):
        self.parent = parent

    def _instance(self):
        if self.parent is not None:
            return self.parent
        else:
            return Com('SldWorks.Application').ActiveDoc

    # @property
    # def configuration_manager(self):
    #     # return self._instance.ConfigurationManager
    #     return ConfigurationManager(self._instance())

    @property
    def extension(self):
        return ModelDocExtension(self._instance())

    @property
    def feature_manager(self):
        # return FeatureManager(self._instance())
        pass


class ModelDocExtension:
    def __init__(self, parent):
        self._instance = parent.Extension

    def custom_property_manager(self, config_name):
        return CustomPropertyManager(self._instance, config_name)


class ConfigurationManager:
    def __init__(self, parent):
        self._instance = parent.ConfigurationManager

    @property
    def active_configuration(self):
        # return self._instance.ActiveConfiguration todo neew interface IConiguration
        pass

    def add_configuration(self):
        pass


class CustomPropertyManager:
    def __init__(self, parent, config_name=str()):
        self._instance = parent.CustomPropertyManager(config_name)

    @property
    def count(self):
        return self._instance.Count

    @property
    def owner(self):
        return self._instance.Owner

    def add(self, field_name, field_type=30, field_value='test', overwrite_existing=1):
        # todo get field type from field value entered
        self._instance.Add3(field_name, field_type, field_value, overwrite_existing)

    def delete(self):
        pass  # todo

    def get(self, field_name, use_cached=False):
        arg1 = win32.VARIANT(pythoncom.VT_BSTR, field_name)
        arg2 = win32.VARIANT(pythoncom.VT_BOOL, use_cached)
        arg3 = win32.VARIANT(pythoncom.VT_BSTR | pythoncom.VT_BYREF, None)
        arg4 = win32.VARIANT(pythoncom.VT_BSTR | pythoncom.VT_BYREF, None)
        arg5 = win32.VARIANT(pythoncom.VT_BOOL | pythoncom.VT_BYREF, None)
        arg6 = win32.VARIANT(pythoncom.VT_BOOL | pythoncom.VT_BYREF, None)
        self._instance.Get6(arg1, arg2, arg3, arg4, arg5, arg6)
        return arg1.value, arg2.value, arg3.value, arg4.value, arg5.value, arg6.value

    def get_all(self):
        arg1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg2 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg3 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg4 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg5 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        self._instance.GetAll3(arg1, arg2, arg3, arg4, arg5)
        # prop names, prop types, prop values, resolved, proplink
        return arg1, arg2, arg3, arg4, arg5

    def get_names(self):
        return self._instance.GetNames
