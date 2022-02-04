# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.html
class IWeldmentCutListAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def weldment_cut_list_feature(self):
		"""Gets the weldment cut list feature for this weldment cut list table annotation."""
		# return self._instance.WeldmentCutListFeature
		raise NotImplemented

	def get_all_custom_properties(self):
		"""Gets the list of available custom properties that could be used for a custom properties column in this weldment cut list table annotation."""
		# return self._instance.GetAllCustomProperties
		raise NotImplemented

	def get_all_custom_properties_count(self):
		"""Gets the number of items in the list of available custom properties that could be used for a custom properties column in this weldment cut list table annotation."""
		# return self._instance.GetAllCustomPropertiesCount
		raise NotImplemented

	def get_column_custom_property(self, index):
		"""
		Gets the custom property for the specified user-defined column.
		:param index: Column for which to get the custom property
		"""
		# return self._instance.GetColumnCustomProperty(index)
		raise NotImplemented

	def i_get_all_custom_properties(self, count):
		"""
		Gets the list of available custom properties that could be used for a custom properties column in this weldment cut list table annotation.
		:param count: Number of available custom properties
		"""
		# return self._instance.IGetAllCustomProperties(count)
		raise NotImplemented

	def set_column_custom_property(self, index, custom_prop):
		"""
		Sets the custom property of the specified user-defined column.
		:param index: Column for which to get the custom property
		:param custom_prop: Custom property for this user-defined column
		"""
		# return self._instance.SetColumnCustomProperty(index, custom_prop)
		raise NotImplemented

	def sort(self, column_index, sort_ascending):
		"""
		Sorts this weldment cut list by the specified column in the specified sorting direction.
		:param column_index: 0-based index of column to sort by (see Remarks)
		:param sort_ascending: True to sort ascending, false to sort descending
		"""
		# return self._instance.Sort(column_index, sort_ascending)
		raise NotImplemented

