# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTableAnnotation_members.html
class IHoleTableAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def hole_table(self):
		"""Gets the hole table feature for this table annotation."""
		# return self._instance.HoleTable
		raise NotImplemented

	def sort(self, column_index, sort_ascending):
		"""
		Sorts this hole table by the specified column in the specified sorting direction.
		:param column_index: 0-based index of column to sort by (see Remarks)
		:param sort_ascending: True to sort ascending, false to sort descending
		"""
		# return self._instance.Sort(column_index, sort_ascending)
		raise NotImplemented

