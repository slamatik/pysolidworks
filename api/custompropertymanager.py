from interfaces.icustompropertymanager import ICustomPropertyManager

class CustomPropertyManager(ICustomPropertyManager):
    def __init__(self, parent, config_name):
        super().__init__(parent, config_name)