# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.html
class ISheetMetalFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_relief_type(self):
		"""Gets or sets the sheet metal auto relief type."""
		return self._instance.AutoReliefType

	@auto_relief_type.setter
	def auto_relief_type(self, value):
		"""Gets or sets the sheet metal auto relief type."""
		self._instance.AutoReliefType = value

	@property
	def bend_radius(self):
		"""Gets or sets the sheet metal bend radius."""
		return self._instance.BendRadius

	@bend_radius.setter
	def bend_radius(self, value):
		"""Gets or sets the sheet metal bend radius."""
		self._instance.BendRadius = value

	@property
	def fixed_reference(self):
		"""Gets or sets the fixed face or edge for this sheet metal feature."""
		return self._instance.FixedReference

	@fixed_reference.setter
	def fixed_reference(self, value):
		"""Gets or sets the fixed face or edge for this sheet metal feature."""
		self._instance.FixedReference = value

	@property
	def relief_ratio(self):
		"""Gets or sets the sheet metal relief ratio."""
		return self._instance.ReliefRatio

	@relief_ratio.setter
	def relief_ratio(self, value):
		"""Gets or sets the sheet metal relief ratio."""
		self._instance.ReliefRatio = value

	@property
	def thickness(self):
		"""Gets or sets the sheet metal thickness."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or sets the sheet metal thickness."""
		self._instance.Thickness = value

	@property
	def use_auto_relief(self):
		"""Gets or sets whether this sheet metal feature uses auto relief."""
		return self._instance.UseAutoRelief

	@use_auto_relief.setter
	def use_auto_relief(self, value):
		"""Gets or sets whether this sheet metal feature uses auto relief."""
		self._instance.UseAutoRelief = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this sheet metal feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this sheet metal feature."""
		self._instance.AccessSelections = value

	@property
	def get_custom_bend_allowance(self):
		"""Gets custom bend allowance for this sheet metal feature."""
		return self._instance.GetCustomBendAllowance

	@get_custom_bend_allowance.setter
	def get_custom_bend_allowance(self, value):
		"""Gets custom bend allowance for this sheet metal feature."""
		self._instance.GetCustomBendAllowance = value

	@property
	def get_override_default_parameter(self):
		"""Gets whether the specified default parameter is overridden in this sheet metal feature in a multibody sheet metal part."""
		return self._instance.GetOverrideDefaultParameter2

	@get_override_default_parameter.setter
	def get_override_default_parameter(self, value):
		"""Gets whether the specified default parameter is overridden in this sheet metal feature in a multibody sheet metal part."""
		self._instance.GetOverrideDefaultParameter2 = value

	@property
	def get_use_gauge_table(self):
		"""Gets whether to use a sheet metal feature gauge table."""
		return self._instance.GetUseGaugeTable

	@get_use_gauge_table.setter
	def get_use_gauge_table(self, value):
		"""Gets whether to use a sheet metal feature gauge table."""
		self._instance.GetUseGaugeTable = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this sheet metal feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this sheet metal feature."""
		self._instance.IAccessSelections2 = value

	@property
	def release_selection_access(self):
		"""Releases access to selections used to define the sheet metal feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections used to define the sheet metal feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_custom_bend_allowance(self):
		"""Sets the custom bend allowance for this sheet metal feature."""
		return self._instance.SetCustomBendAllowance

	@set_custom_bend_allowance.setter
	def set_custom_bend_allowance(self, value):
		"""Sets the custom bend allowance for this sheet metal feature."""
		self._instance.SetCustomBendAllowance = value

	@property
	def set_override_default_parameter(self):
		"""Sets whether to override the specified default parameter in this sheet metal feature in a multibody sheet metal part."""
		return self._instance.SetOverrideDefaultParameter2

	@set_override_default_parameter.setter
	def set_override_default_parameter(self, value):
		"""Sets whether to override the specified default parameter in this sheet metal feature in a multibody sheet metal part."""
		self._instance.SetOverrideDefaultParameter2 = value

	@property
	def set_use_gauge_table(self):
		"""Sets whether to use a sheet metal feature gauge table."""
		return self._instance.SetUseGaugeTable

	@set_use_gauge_table.setter
	def set_use_gauge_table(self, value):
		"""Sets whether to use a sheet metal feature gauge table."""
		self._instance.SetUseGaugeTable = value

