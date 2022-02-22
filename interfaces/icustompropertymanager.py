import win32com.client as win32
import pythoncom
from enums import CustomInfoType, CustomInfoAddResult, CustomInfoGetResult
from datetime import datetime


# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager.html

class ICustomPropertyManager:
    def __init__(self, parent=None):
        self._instance = parent

    def count(self):
        """Gets the number of custom properties."""
        return self._instance.Count

    @property
    def link_all(self):
        """Gets or sets whether to link or unlink all custom properties to or from their parent parts."""
        return self._instance.LinkAll

    @link_all.setter
    def link_all(self, value):
        """Gets or sets whether to link or unlink all custom properties to or from their parent parts."""
        self._instance.LinkAll = value

    def owner(self):
        """Gets the owner of this custom property."""
        return self._instance.Owner

    def add(self, field_name, field_value='test', overwrite_existing=1):
        """
        Adds a custom property to a configuration or model document.
        :param field_name: Name of custom property
        :param field_type: Type of custom property as defined in swCustomInfoType_e
        :param field_value: Value of custom property
        :param overwrite_existing: Overwrite option as defined in swCustomPropertyAddOption_e
        """
        if type(field_value) == float:
            field_type = CustomInfoType.DOUBLE.value
        elif type(field_value) == int:
            field_type = CustomInfoType.NUMBER.value
        elif type(field_value) == bool:
            field_type = CustomInfoType.YES_OR_NO.value
        elif type(field_value) == str:
            try:
                datetime.strptime(field_value, '%d/%m/%Y')
                field_type = CustomInfoType.DATE.value
            except ValueError:
                field_type = CustomInfoType.TEXT.value
        else:
            field_type = CustomInfoType.UNKNOWN.value
        print(field_type)
        return CustomInfoAddResult(self._instance.Add3(field_name, field_type, field_value, overwrite_existing))

    def delete(self, field_name):
        """
        Deletes the specified custom property.
        :param field_name: Name of the custom property to delete
        """
        self._instance.Delete2(field_name)

    def get(self, field_name, use_cached=False):
        """
        Gets the value and the evaluated value of the specified custom property.
        :param field_name: Name of the custom property
        :param use_cached: True if the configuration has been activated, false if not (see Remarks)
        :param val_out: Value of the custom property
        :param resolved_val_out: Evaluated value of the custom property
        :param was_resolved: True if the value was evaluated, false if not (see Remarks)
        :param link_to_property: True to link FieldName to its parent part, false to not
        """
        arg1 = win32.VARIANT(pythoncom.VT_BSTR, field_name)
        arg2 = win32.VARIANT(pythoncom.VT_BOOL, use_cached)
        arg3 = win32.VARIANT(pythoncom.VT_BSTR | pythoncom.VT_BYREF, None)
        arg4 = win32.VARIANT(pythoncom.VT_BSTR | pythoncom.VT_BYREF, None)
        arg5 = win32.VARIANT(pythoncom.VT_BOOL | pythoncom.VT_BYREF, None)
        arg6 = win32.VARIANT(pythoncom.VT_BOOL | pythoncom.VT_BYREF, None)
        self._instance.Get6(arg1, arg2, arg3, arg4, arg5, arg6)
        return arg1.value, arg2.value, arg3.value, arg4.value, arg5.value, arg6.value

    def get_all(self):
        """
        Gets all of the custom properties for this configuration.
        :param prop_names: Array of the names of custom properties retrieved
        :param prop_types: Array of types of PropNames as defined in swCustomInfoType_e
        :param prop_values: Array of evaluated values of PropNames
        :param resolved: Array of evaluation statuses of PropNames as defined in swCustomInfoGetResult_e
        :param prop_link: Array of integers indicating whether PropNames are linked to their parent parts:
        	1 = link
        	0 = no link
        """
        arg1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg2 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg3 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg4 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        arg5 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_VARIANT, None)
        self._instance.GetAll3(arg1, arg2, arg3, arg4, arg5)
        arg2 = [CustomInfoType(i) for i in arg2.value]
        arg4 = [CustomInfoGetResult(i) for i in arg4.value]
        return list(zip(arg1.value, arg2, arg3.value, arg4, arg5.value))

    def get_names(self):
        """Gets the names of the custom properties."""
        return self._instance.GetNames

    def get_type(self, field_name):
        """
        Gets the type of the specified custom property for a configuration or model document.
        :param field_name: Name of the custom property whose type to get
        """
        return CustomInfoType(self._instance.GetType2(field_name))

    def i_get_all(self, count, prop_names, prop_types, prop_values):
        """
        Gets all of the custom properties for this configuration.
        :param count: Number of custom properties
        :param prop_names: Array of the names of custom properties
        :param prop_types: Array of property types as defined in swCustomInfoType_e
        :param prop_values: Array of values of custom properties
        """
        # return self._instance.IGetAll(count, prop_names, prop_types, prop_values)
        raise NotImplemented

    def i_get_names(self, count):
        """
        Gets the names of the custom properties.
        :param count: Number of custom properties
        """
        # return self._instance.IGetNames(count)
        raise NotImplemented

    def is_custom_property_editable(self, property_name, configuration_name):
        """
        Gets whether the specified custom property is editable in the specified configuration.
        :param property_name: Custom property name
        :param configuration_name: Configuration name
        """
        # return self._instance.IsCustomPropertyEditable(property_name, configuration_name)
        raise NotImplemented

    def link_property(self, field_name, field_link):
        """
        Sets whether to link or unlink the specified custom property to or from its parent part.
        :param field_name: Name of the custom property to link or unlink
        :param field_link: True to link the custom property, false to unlink it
        """
        # return self._instance.LinkProperty(field_name, field_link)
        raise NotImplemented

    def set(self, field_name, field_value):
        """
        Sets the value for the specified custom property.
        :param field_name: Name of the existing custom property
        :param field_value: Value for the existing custom property
        """
        self._instance.Set2(field_name, field_value)
