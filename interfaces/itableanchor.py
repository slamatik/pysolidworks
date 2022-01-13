class ITableAnchor:
    def __init__(self, parent, table_type):
        self._instance = parent.TableAnchor(table_type)

    @property
    def position(self):
        return self._instance.Position

    @property
    def type(self):
        # todo type
        return self._instance.Type

    def get_feature(self):
        # todo IFeature
        return self._instance.GetFeature
