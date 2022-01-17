# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation.html

class IRevisionTableAnnotation:
    def __init__(self, parent=None):
        self._instance = parent.RevisionTable

    @property
    def current_revision(self):
        return self._instance.CurrentRevision

    # @property
    # def revision_table_features(self):
    #     return self._instance.RevisionTableFeature

    def add_revision(self, revision):
        return self._instance.AddRevision(revision)

    def delete_revision(self, revision_id: int, delete_symbols: bool = True):
        return self._instance.DeleteRevision(revision_id, delete_symbols)

    def get_all_custom_properties(self):
        return self._instance.GetAllCustomProperties

    def get_all_custom_properties_count(self):
        return self._instance.GetAllCustomPropertiesCount

    def get_id_row_number(self, row_index):
        return self._instance.GetIdForRowNumber(row_index)

    def get_revision_for_id(self, revision_id):
        return self._instance.GetRevisionForId(revision_id)

    def get_revision_symbol_count(self, revision_id):
        return self._instance.GetRevisionSymbolCount(revision_id)

    def get_revision_symbols(self, revision_id):
        return self._instance.GetRevisionSymbols(revision_id)

    def get_row_number_for_id(self, revision_id):
        return self._instance.GetRowNumberForId(revision_id)

    def set_column_custom_property(self, index, custom_prop):
        return self._instance.SetColumnCustomProperty(index, custom_prop)
