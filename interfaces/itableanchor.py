from enums import TableAnnotation
from interfaces.ifeature import IFeature


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor.html

class ITableAnchor:
    def __init__(self, parent, table_type):
        self._instance = parent.TableAnchor(table_type)

    @property
    def position(self):
        return self._instance.Position

    @property
    def type(self):
        return TableAnnotation(self._instance.Type)

    def get_feature(self):
        return IFeature(self._instance)
