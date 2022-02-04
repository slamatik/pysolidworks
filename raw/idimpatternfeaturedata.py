# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimPatternFeatureData_members.html
class IDimPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def propagate_visual_properties(self):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all variable pattern instances."""
		return self._instance.PropagateVisualProperties

	@propagate_visual_properties.setter
	def propagate_visual_properties(self, value):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all variable pattern instances."""
		self._instance.PropagateVisualProperties = value

	@property
	def access_selections(self):
		"""Allows access to the selections that describe this variable pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Allows access to the selections that describe this variable pattern feature."""
		self._instance.AccessSelections = value

	@property
	def add_dimension(self):
		"""Adds the selected dimension as a column to the pattern table for this variable pattern feature."""
		return self._instance.AddDimension

	@add_dimension.setter
	def add_dimension(self, value):
		"""Adds the selected dimension as a column to the pattern table for this variable pattern feature."""
		self._instance.AddDimension = value

	@property
	def add_instance_at(self):
		"""Adds a pattern instance to this variable pattern feature."""
		return self._instance.AddInstanceAt

	@add_instance_at.setter
	def add_instance_at(self, value):
		"""Adds a pattern instance to this variable pattern feature."""
		self._instance.AddInstanceAt = value

	@property
	def delete_dimension(self):
		"""Deletes the specified column of dimensions in the pattern table in this variable pattern feature."""
		return self._instance.DeleteDimension

	@delete_dimension.setter
	def delete_dimension(self, value):
		"""Deletes the specified column of dimensions in the pattern table in this variable pattern feature."""
		self._instance.DeleteDimension = value

	@property
	def delete_instance_at(self):
		"""Deletes the specified pattern instance in this variable pattern feature."""
		return self._instance.DeleteInstanceAt

	@delete_instance_at.setter
	def delete_instance_at(self, value):
		"""Deletes the specified pattern instance in this variable pattern feature."""
		self._instance.DeleteInstanceAt = value

	@property
	def export_to_excel(self):
		"""Exports the pattern table to the specified Microsoft Excel file for this variable pattern feature."""
		return self._instance.ExportToExcel

	@export_to_excel.setter
	def export_to_excel(self, value):
		"""Exports the pattern table to the specified Microsoft Excel file for this variable pattern feature."""
		self._instance.ExportToExcel = value

	@property
	def get_controlling_dimension_count(self):
		"""Gets the number of controlling dimensions in this variable pattern feature."""
		return self._instance.GetControllingDimensionCount

	@get_controlling_dimension_count.setter
	def get_controlling_dimension_count(self, value):
		"""Gets the number of controlling dimensions in this variable pattern feature."""
		self._instance.GetControllingDimensionCount = value

	@property
	def get_controlling_dimension_name(self):
		"""Gets the name of the controlling dimension for the pattern instance at the specified index in this variable pattern feature."""
		return self._instance.GetControllingDimensionName

	@get_controlling_dimension_name.setter
	def get_controlling_dimension_name(self, value):
		"""Gets the name of the controlling dimension for the pattern instance at the specified index in this variable pattern feature."""
		self._instance.GetControllingDimensionName = value

	@property
	def get_instance_count(self):
		"""Gets the number of pattern instances in this variable pattern feature."""
		return self._instance.GetInstanceCount

	@get_instance_count.setter
	def get_instance_count(self, value):
		"""Gets the number of pattern instances in this variable pattern feature."""
		self._instance.GetInstanceCount = value

	@property
	def get_instance_dimension_name(self):
		"""Gets the name of the pattern dimension for the pattern instance in this variable pattern feature."""
		return self._instance.GetInstanceDimensionName

	@get_instance_dimension_name.setter
	def get_instance_dimension_name(self, value):
		"""Gets the name of the pattern dimension for the pattern instance in this variable pattern feature."""
		self._instance.GetInstanceDimensionName = value

	@property
	def get_instance_index(self):
		"""Gets the index of the pattern instance in the FeatureManager design tree in the variable pattern feature."""
		return self._instance.GetInstanceIndex

	@get_instance_index.setter
	def get_instance_index(self, value):
		"""Gets the index of the pattern instance in the FeatureManager design tree in the variable pattern feature."""
		self._instance.GetInstanceIndex = value

	@property
	def get_instance_name_by_index(self):
		"""Gets the name of the pattern instance at the specified index in the pattern table in this variable pattern feature."""
		return self._instance.GetInstanceNameByIndex

	@get_instance_name_by_index.setter
	def get_instance_name_by_index(self, value):
		"""Gets the name of the pattern instance at the specified index in the pattern table in this variable pattern feature."""
		self._instance.GetInstanceNameByIndex = value

	@property
	def get_instance_suppress_state_by_index(self):
		"""Gets whether the pattern instance at the specified index in the pattern table is suppressed in this variable pattern feature."""
		return self._instance.GetInstanceSuppressStateByIndex

	@get_instance_suppress_state_by_index.setter
	def get_instance_suppress_state_by_index(self, value):
		"""Gets whether the pattern instance at the specified index in the pattern table is suppressed in this variable pattern feature."""
		self._instance.GetInstanceSuppressStateByIndex = value

	@property
	def get_instance_suppress_state_by_name(self):
		"""Gets whether the pattern instance with the specified name is suppressed in this variable pattern feature."""
		return self._instance.GetInstanceSuppressStateByName

	@get_instance_suppress_state_by_name.setter
	def get_instance_suppress_state_by_name(self, value):
		"""Gets whether the pattern instance with the specified name is suppressed in this variable pattern feature."""
		self._instance.GetInstanceSuppressStateByName = value

	@property
	def get_table_row_index(self):
		"""Gets the index of the specified pattern instance in the pattern table in this variable pattern feature."""
		return self._instance.GetTableRowIndex

	@get_table_row_index.setter
	def get_table_row_index(self, value):
		"""Gets the index of the specified pattern instance in the pattern table in this variable pattern feature."""
		self._instance.GetTableRowIndex = value

	@property
	def import_from_excel(self):
		"""Imports a table from the specified Microsoft Excel file for this variable pattern feature."""
		return self._instance.ImportFromExcel

	@import_from_excel.setter
	def import_from_excel(self, value):
		"""Imports a table from the specified Microsoft Excel file for this variable pattern feature."""
		self._instance.ImportFromExcel = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define this variable pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define this variable pattern feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_instance_dimension_value(self):
		"""Sets a new value for the pattern dimension of the specified pattern instance in this variable pattern feature."""
		return self._instance.SetInstanceDimensionValue

	@set_instance_dimension_value.setter
	def set_instance_dimension_value(self, value):
		"""Sets a new value for the pattern dimension of the specified pattern instance in this variable pattern feature."""
		self._instance.SetInstanceDimensionValue = value

	@property
	def set_instance_suppress_state_by_index(self):
		"""Sets whether the pattern instance with the specified index in the pattern table is suppressed in this variable pattern feature."""
		return self._instance.SetInstanceSuppressStateByIndex

	@set_instance_suppress_state_by_index.setter
	def set_instance_suppress_state_by_index(self, value):
		"""Sets whether the pattern instance with the specified index in the pattern table is suppressed in this variable pattern feature."""
		self._instance.SetInstanceSuppressStateByIndex = value

	@property
	def set_instance_suppress_state_by_name(self):
		"""Sets whether a pattern instance with the specified name is suppressed in this variable pattern feature."""
		return self._instance.SetInstanceSuppressStateByName

	@set_instance_suppress_state_by_name.setter
	def set_instance_suppress_state_by_name(self, value):
		"""Sets whether a pattern instance with the specified name is suppressed in this variable pattern feature."""
		self._instance.SetInstanceSuppressStateByName = value

