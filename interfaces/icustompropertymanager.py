import win32com.client as win32
import pythoncom
from enums import CustomInfoType


class ICustomPropertyManager:
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

    def delete(self, field_name):
        self._instance.Delete2(field_name)

    def get(self, field_name, use_cached=False):
        # todo format returned values
        arg1 = win32.VARIANT(pythoncom.VT_BSTR, field_name)
        arg2 = win32.VARIANT(pythoncom.VT_BOOL, use_cached)
        arg3 = win32.VARIANT(pythoncom.VT_BSTR | pythoncom.VT_BYREF, None)
        arg4 = win32.VARIANT(pythoncom.VT_BSTR | pythoncom.VT_BYREF, None)
        arg5 = win32.VARIANT(pythoncom.VT_BOOL | pythoncom.VT_BYREF, None)
        arg6 = win32.VARIANT(pythoncom.VT_BOOL | pythoncom.VT_BYREF, None)
        self._instance.Get6(arg1, arg2, arg3, arg4, arg5, arg6)
        # return arg1.value, arg2.value, arg3.value, arg4.value, arg5.value, arg6.value
        return arg1, arg2, arg3, arg4, arg5, arg6

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

    def get_type(self, field_name):
        return CustomInfoType(self._instance.GetType2(field_name))

    def set(self, field_name, field_value):
        self._instance.Set2(field_name, field_value)
