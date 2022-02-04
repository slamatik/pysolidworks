# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionTableAnnotation_members.html
class IRevisionTableAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def current_revision(self):
		"""Gets the latest revision of this revision table annotation."""
		# return self._instance.CurrentRevision
		raise NotImplemented

	def revision_table_feature(self):
		"""Gets the revision table for this revision table annotation."""
		# return self._instance.RevisionTableFeature
		raise NotImplemented

	def add_revision(self, revision):
		"""
		Adds a revision to this revision table.
		:param revision: Revision
		"""
		# return self._instance.AddRevision(revision)
		raise NotImplemented

	def delete_revision(self, revision_id, delete_symbols):
		"""
		Deletes a revision from this revision table.
		:param revision_id: Revision ID
		:param delete_symbols: True to delete all associated symbols, false to not
		"""
		# return self._instance.DeleteRevision(revision_id, delete_symbols)
		raise NotImplemented

	def get_all_custom_properties(self):
		"""Gets a list of available custom properties that can be used for a custom properties column in this revision table annotation."""
		# return self._instance.GetAllCustomProperties
		raise NotImplemented

	def get_all_custom_properties_count(self):
		"""Gets the number of items in the list of available custom properties that can be used for a custom properties column in this revision table annotation."""
		# return self._instance.GetAllCustomPropertiesCount
		raise NotImplemented

	def get_column_custom_property(self, index):
		"""
		Gets the custom property used for the values in a specified user-defined column.
		:param index: Column from which to get the custom property
		"""
		# return self._instance.GetColumnCustomProperty(index)
		raise NotImplemented

	def get_id_for_row_number(self, row_index):
		"""
		Gets the revision ID for the specified row number.
		:param row_index: 0-based index for this row number
		"""
		# return self._instance.GetIdForRowNumber(row_index)
		raise NotImplemented

	def get_revision_for_id(self, revision_id):
		"""
		Gets the revision text for the specified revision ID.
		:param revision_id: Revision ID
		"""
		# return self._instance.GetRevisionForId(revision_id)
		raise NotImplemented

	def get_revision_symbol_count(self, revision_id):
		"""
		Gets the number of revision symbols associated with the specified revision ID.
		:param revision_id: Revision ID
		"""
		# return self._instance.GetRevisionSymbolCount(revision_id)
		raise NotImplemented

	def get_revision_symbols(self, revision_id):
		"""
		Gets the revision symbols associated with the specified revision ID.
		:param revision_id: Revision ID
		"""
		# return self._instance.GetRevisionSymbols(revision_id)
		raise NotImplemented

	def get_row_number_for_id(self, revision_id):
		"""
		Gets the row number in the table for the specified revision ID.
		:param revision_id: Revision ID
		"""
		# return self._instance.GetRowNumberForId(revision_id)
		raise NotImplemented

	def get_sheet(self):
		"""Gets the drawing sheet on which this revision ID exists."""
		# return self._instance.GetSheet
		raise NotImplemented

	def i_get_all_custom_properties(self, count):
		"""
		Gets a list of available custom properties that can be used for a custom properties column in this revision table annotation.
		:param count: Number of available custom properties
		"""
		# return self._instance.IGetAllCustomProperties(count)
		raise NotImplemented

	def i_get_revision_symbols(self, revision_id, count):
		"""
		Gets the revision symbols associated with the specified revision ID.
		:param revision_id: Revision ID
		:param count: Number of revision symbols
		"""
		# return self._instance.IGetRevisionSymbols(revision_id, count)
		raise NotImplemented

	def set_column_custom_property(self, index, custom_prop):
		"""
		Sets the custom property used for the values in a specified user-defined column.
		:param index: Column for which to get the custom property
		:param custom_prop: Custom property used for the values in this user-defined column
		"""
		# return self._instance.SetColumnCustomProperty(index, custom_prop)
		raise NotImplemented

