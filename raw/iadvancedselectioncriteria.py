# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSelectionCriteria_members.html
class IAdvancedSelectionCriteria:
	def __init__(self, parent=None):
		self._instance = parent

	def add_item(self, category1, category2, condition, value, is_and):
		"""
		Adds the specified advanced component selection criterion to the list.
		:param category1: Name of Category1 (see Remarks)
		:param category2: Name of Category2 (see Remarks)
		:param condition: Condition as defined in swAdvSelectType_e (see Remarks)
		:param value: Text value satisfying Condition (see Remarks)
		:param is_and: True if all of the criteria in the advanced component selection list must be met, false if only this criteria in the advanced component selection list must be met
		"""
		# return self._instance.AddItem2(category1, category2, condition, value, is_and)
		raise NotImplemented

	def delete_item(self, index):
		"""
		Deletes a criteria from the advanced component selection list.
		:param index: Index number of the criteria to delete
		"""
		# return self._instance.DeleteItem(index)
		raise NotImplemented

	def get_item(self, index, category1, category2, condition, value, is_and):
		"""
		Gets the specified advanced component selection criterion.
		:param index: Index number of the criterion to retrieve
		:param category1: Name of Category1 (see Remarks)
		:param category2: Name of Category2 (see Remarks)
		:param condition: Condition as defined in swAdvSelectType_e (see Remarks)
		:param value: Text value satisfying Condition (see Remarks)
		:param is_and: True if all of the criteria in the advanced component selection criteria list must be met, false if only this criterion must be met
		"""
		# return self._instance.GetItem2(index, category1, category2, condition, value, is_and)
		raise NotImplemented

	def get_item_count(self):
		"""Gets the number of criteria in the advanced component selection criteria list."""
		# return self._instance.GetItemCount
		raise NotImplemented

	def load_criteria(self, criteria_file_name):
		"""
		Loads the specified query file and makes it the current advanced component selection criteria list.
		:param criteria_file_name: Path and filename of query file (see Remarks)
		"""
		# return self._instance.LoadCriteria(criteria_file_name)
		raise NotImplemented

	def save_criteria(self, criteria_file_name):
		"""
		Saves the current query to the specified XML file.
		:param criteria_file_name: Path and filename (*.xml) to which to save the current query
		"""
		# return self._instance.SaveCriteria(criteria_file_name)
		raise NotImplemented

	def select(self):
		"""Selects the assembly components that satisfy the current advanced selection criteria."""
		# return self._instance.Select
		raise NotImplemented

