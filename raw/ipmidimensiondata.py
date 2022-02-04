# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData_members.html
class IPMIDimensionData:
	def __init__(self, parent=None):
		self._instance = parent

	def dimension_text(self):
		"""Gets the text of this PMI dimension.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DimensionText
		raise NotImplemented

	def get_dimension_item_at_index(self, index):
		"""
		Gets the PMI dimension item at the specified index.
		:param index: Zero-based index of the dimension item to get
		"""
		# return self._instance.GetDimensionItemAtIndex(index)
		raise NotImplemented

	def get_dimension_item_count(self):
		"""Gets the number of dimension items in this PMI dimension annotation."""
		# return self._instance.GetDimensionItemCount
		raise NotImplemented

