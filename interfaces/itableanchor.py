from enums import TableAnnotation
from interfaces.ifeature import IFeature


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor_members.html

class ITableAnchor:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def position(self):
        """Gets or sets the location of the table anchor."""
        return self._instance.Position

    @position.setter
    def position(self, value):
        """Gets or sets the location of the table anchor."""
        self._instance.Position = value

    @property
    def type(self):
        """Gets the type of table anchor."""
        return TableAnnotation(self._instance.Type)

    def get_feature(self):
        """Gets the feature for this table anchor."""
        return IFeature(self._instance)
