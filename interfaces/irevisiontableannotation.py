# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation.html
from interfaces.irevisiontablefeature import IRevisionTableFeature
import interfaces.itableannotation


class IRevisionTableAnnotation(interfaces.itableannotation.ITableAnnotation):
    def __init__(self, parent):
        super().__init__(parent)

    @property
    def current_revision(self):
        """Gets the latest revision of this revision table annotation."""
        return self._instance.CurrentRevision

    @property
    def revision_table_features(self):
        """Gets the revision table for this revision table annotation."""
        return IRevisionTableFeature(self._instance.RevisionTableFeature)

    def add_revision(self, revision):
        """
        Adds a revision to this revision table.
        :param revision: Revision
        """
        return self._instance.AddRevision(revision)

    def delete_revision(self, revision_id: int, delete_symbols: bool = True):
        """
        Deletes a revision from this revision table.
        :param revision_id: Revision ID
        :param delete_symbols: True to delete all associated symbols, false to not
        """
        return self._instance.DeleteRevision(revision_id, delete_symbols)

    def get_all_custom_properties(self):
        """Gets a list of available custom properties that can be used for a custom properties column in this revision
        table annotation."""
        return self._instance.GetAllCustomProperties

    def get_all_custom_properties_count(self):
        """Gets the number of items in the list of available custom properties that can be used for a custom properties
        column in this revision table annotation."""
        return self._instance.GetAllCustomPropertiesCount

    def get_column_custom_property(self, index):
        """
        Gets the custom property used for the values in a specified user-defined column.
        :param index: Column from which to get the custom property
        """
        # return self._instance.GetColumnCustomProperty(index) todo
        raise NotImplemented

    def get_id_row_number(self, row_index):
        """
        Gets the revision ID for the specified row number.
        :param row_index: 0-based index for this row number
        """
        return self._instance.GetIdForRowNumber(row_index)

    def get_revision_for_id(self, revision_id):
        """
        Gets the revision text for the specified revision ID.
        :param revision_id: Revision ID
        """
        return self._instance.GetRevisionForId(revision_id)

    def get_revision_symbol_count(self, revision_id):
        """
        Gets the number of revision symbols associated with the specified revision ID.
        :param revision_id: Revision ID
        """
        return self._instance.GetRevisionSymbolCount(revision_id)

    def get_revision_symbols(self, revision_id):
        """
        Gets the revision symbols associated with the specified revision ID.
        :param revision_id: Revision ID
        """
        return self._instance.GetRevisionSymbols(revision_id)

    def get_row_number_for_id(self, revision_id):
        """
        Gets the row number in the table for the specified revision ID.
        :param revision_id: Revision ID
        """
        return self._instance.GetRowNumberForId(revision_id)

    def get_sheet(self):
        """Gets the drawing sheet on which this revision ID exists."""
        # return self._instance.GetSheet todo
        raise NotImplemented

    def i_get_all_custom_properties(self, count):
        """
        Gets a list of available custom properties that can be used for a custom properties column in this revision
        table annotation.
        :param count: Number of available custom properties
        """
        # return self._instance.IGetAllCustomProperties(count) todo
        raise NotImplemented

    def i_get_revision_symbols(self, revision_id, count):
        """
        Gets the revision symbols associated with the specified revision ID.
        :param revision_id: Revision ID
        :param count: Number of revision symbols
        """
        # return self._instance.IGetRevisionSymbols(revision_id, count) todo
        raise NotImplemented

    def set_column_custom_property(self, index, custom_prop):
        """
        Sets the custom property used for the values in a specified user-defined column.
        :param index: Column for which to get the custom property
        :param custom_prop: Custom property used for the values in this user-defined column
        """
        return self._instance.SetColumnCustomProperty(index, custom_prop)
