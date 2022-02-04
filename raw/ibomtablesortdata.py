# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableSortData_members.html
class IBomTableSortData:
	def __init__(self, parent=None):
		self._instance = parent

	def ascending(self, sort_order_index):
		"""
		Gets and sets whether this is an ascending sort for the specified sort order index.
		:param sort_order_index: 0 for primary sort, 1 for secondary sort, 2 for tertiary sort (see Remarks)
		"""
		# return self._instance.Ascending(sort_order_index)
		raise NotImplemented

	def column_index(self, sort_order_index):
		"""
		Gets and sets the column index for the specified sort order index.
		:param sort_order_index: 0 for primary sort, 1 for secondary sort, 2 for tertiary sort (see Remarks)
		"""
		# return self._instance.ColumnIndex(sort_order_index)
		raise NotImplemented

	def do_not_change_item_number(self):
		"""Gets and sets whether to change BOM item numbers after sorting."""
		# return self._instance.DoNotChangeItemNumber
		raise NotImplemented

	def item_groups(self):
		"""Gets and sets the categories into which the BOM table rows are grouped."""
		# return self._instance.ItemGroups
		raise NotImplemented

	def save_current_sort_parameters(self):
		"""Gets and sets whether to save the current sort settings in the BOM table in the drawing."""
		# return self._instance.SaveCurrentSortParameters
		raise NotImplemented

	def sort_method(self):
		"""Gets and sets the method for sorting the BOM table."""
		# return self._instance.SortMethod
		raise NotImplemented

