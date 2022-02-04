# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableAnnotation_members.html
class IGeneralTableAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def general_table(self):
		"""Gets the general table feature for this annotation."""
		# return self._instance.GeneralTable
		raise NotImplemented

	def sort(self, column_index, sort_ascending):
		"""
		Sorts this table by the specified column in the specified sorting direction.
		:param column_index: 0-based index of column to sort by
		:param sort_ascending: True to sort ascending, false to sort descending
		"""
		# return self._instance.Sort(column_index, sort_ascending)
		raise NotImplemented

