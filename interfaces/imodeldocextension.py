from .icustompropertymanager import ICustomPropertyManager


# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension.html

class IModelDocExtension:
    def __init__(self, parent):
        self._instance = parent.Extension

    def custom_property_manager(self, config_name):
        return ICustomPropertyManager(self._instance, config_name)
