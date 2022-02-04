# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweptFlangeFeatureData_members.html
class ISweptFlangeFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bend_radius(self):
		"""Gets or sets the bend radius of this swept flange feature."""
		return self._instance.BendRadius

	@bend_radius.setter
	def bend_radius(self, value):
		"""Gets or sets the bend radius of this swept flange feature."""
		self._instance.BendRadius = value

	@property
	def cylindrical_or_conical_edge(self):
		"""Gets or sets the linear sketch entity to propagate to the flat pattern of this cylindrical or conical swept flange feature."""
		return self._instance.CylindricalOrConicalEdge

	@cylindrical_or_conical_edge.setter
	def cylindrical_or_conical_edge(self, value):
		"""Gets or sets the linear sketch entity to propagate to the flat pattern of this cylindrical or conical swept flange feature."""
		self._instance.CylindricalOrConicalEdge = value

	@property
	def end_offset(self):
		"""Gets or sets the end offset of this swept flange feature."""
		return self._instance.EndOffset

	@end_offset.setter
	def end_offset(self, value):
		"""Gets or sets the end offset of this swept flange feature."""
		self._instance.EndOffset = value

	@property
	def flange_position(self):
		"""Gets or sets the flange position of this swept flange feature."""
		return self._instance.FlangePosition

	@flange_position.setter
	def flange_position(self, value):
		"""Gets or sets the flange position of this swept flange feature."""
		self._instance.FlangePosition = value

	@property
	def flatten_along_path(self):
		"""Gets or sets whether to flatten the flange profile along the sweep path of this swept flange feature."""
		return self._instance.FlattenAlongPath

	@flatten_along_path.setter
	def flatten_along_path(self, value):
		"""Gets or sets whether to flatten the flange profile along the sweep path of this swept flange feature."""
		self._instance.FlattenAlongPath = value

	@property
	def material_inside(self):
		"""Gets or sets whether to flatten the flange profile with material inside of this swept flange feature."""
		return self._instance.MaterialInside

	@material_inside.setter
	def material_inside(self, value):
		"""Gets or sets whether to flatten the flange profile with material inside of this swept flange feature."""
		self._instance.MaterialInside = value

	@property
	def override_default_sheet_metal_parameters(self):
		"""Gets or sets whether to override the default sheet metal parameters for this swept flange feature."""
		return self._instance.OverrideDefaultSheetMetalParameters

	@override_default_sheet_metal_parameters.setter
	def override_default_sheet_metal_parameters(self, value):
		"""Gets or sets whether to override the default sheet metal parameters for this swept flange feature."""
		self._instance.OverrideDefaultSheetMetalParameters = value

	@property
	def path(self):
		"""Gets or sets the sweep path of this swept flange feature."""
		return self._instance.Path

	@path.setter
	def path(self, value):
		"""Gets or sets the sweep path of this swept flange feature."""
		self._instance.Path = value

	@property
	def profile(self):
		"""Gets or sets the sweep profile of this swept flange feature."""
		return self._instance.Profile

	@profile.setter
	def profile(self, value):
		"""Gets or sets the sweep profile of this swept flange feature."""
		self._instance.Profile = value

	@property
	def relief_depth(self):
		"""Gets or sets the bend relief depth for this swept flange feature."""
		return self._instance.ReliefDepth

	@relief_depth.setter
	def relief_depth(self, value):
		"""Gets or sets the bend relief depth for this swept flange feature."""
		self._instance.ReliefDepth = value

	@property
	def relief_ratio(self):
		"""Gets or sets the bend relief ratio for this swept flange feature."""
		return self._instance.ReliefRatio

	@relief_ratio.setter
	def relief_ratio(self, value):
		"""Gets or sets the bend relief ratio for this swept flange feature."""
		self._instance.ReliefRatio = value

	@property
	def relief_type(self):
		"""Gets or sets the bend relief type for this swept flange feature."""
		return self._instance.ReliefType

	@relief_type.setter
	def relief_type(self, value):
		"""Gets or sets the bend relief type for this swept flange feature."""
		self._instance.ReliefType = value

	@property
	def relief_width(self):
		"""Gets or sets the bend relief width for this swept flange feature."""
		return self._instance.ReliefWidth

	@relief_width.setter
	def relief_width(self, value):
		"""Gets or sets the bend relief width for this swept flange feature."""
		self._instance.ReliefWidth = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of sheet metal thickness of this swept flange feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of sheet metal thickness of this swept flange feature."""
		self._instance.ReverseDirection = value

	@property
	def start_offset(self):
		"""Gets or sets the start offset of this swept flange feature."""
		return self._instance.StartOffset

	@start_offset.setter
	def start_offset(self, value):
		"""Gets or sets the start offset of this swept flange feature."""
		self._instance.StartOffset = value

	@property
	def thickness(self):
		"""Gets or sets the sheet metal thickness of this swept flange feature."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or sets the sheet metal thickness of this swept flange feature."""
		self._instance.Thickness = value

	@property
	def trim_side_bends(self):
		"""Gets or sets whether to remove extra material in neighboring bends of this swept flange feature."""
		return self._instance.TrimSideBends

	@trim_side_bends.setter
	def trim_side_bends(self, value):
		"""Gets or sets whether to remove extra material in neighboring bends of this swept flange feature."""
		self._instance.TrimSideBends = value

	@property
	def use_default_bend_allowance(self):
		"""Gets or sets whether to use the bend allowance from the original sheet metal feature in this swept flange feature."""
		return self._instance.UseDefaultBendAllowance

	@use_default_bend_allowance.setter
	def use_default_bend_allowance(self, value):
		"""Gets or sets whether to use the bend allowance from the original sheet metal feature in this swept flange feature."""
		self._instance.UseDefaultBendAllowance = value

	@property
	def use_default_bend_relief(self):
		"""Gets or sets whether to use the bend relief from the original sheet metal feature in this swept flange feature."""
		return self._instance.UseDefaultBendRelief

	@use_default_bend_relief.setter
	def use_default_bend_relief(self, value):
		"""Gets or sets whether to use the bend relief from the original sheet metal feature in this swept flange feature."""
		self._instance.UseDefaultBendRelief = value

	@property
	def use_default_radius(self):
		"""Gets or sets whether to use the bend radius from the original sheet metal feature in this swept flange feature."""
		return self._instance.UseDefaultRadius

	@use_default_radius.setter
	def use_default_radius(self, value):
		"""Gets or sets whether to use the bend radius from the original sheet metal feature in this swept flange feature."""
		self._instance.UseDefaultRadius = value

	@property
	def use_gauge_table(self):
		"""Gets or sets whether to use an Excel gauge table for this swept flange feature."""
		return self._instance.UseGaugeTable

	@use_gauge_table.setter
	def use_gauge_table(self, value):
		"""Gets or sets whether to use an Excel gauge table for this swept flange feature."""
		self._instance.UseGaugeTable = value

	@property
	def use_material_sheet_metal_parameters(self):
		"""Gets or sets whether to use the material sheet metal parameters in this swept flange feature."""
		return self._instance.UseMaterialSheetMetalParameters

	@use_material_sheet_metal_parameters.setter
	def use_material_sheet_metal_parameters(self, value):
		"""Gets or sets whether to use the material sheet metal parameters in this swept flange feature."""
		self._instance.UseMaterialSheetMetalParameters = value

	@property
	def use_relief_ratio(self):
		"""Gets or sets whether to use the relief ratio in this swept flange feature."""
		return self._instance.UseReliefRatio

	@use_relief_ratio.setter
	def use_relief_ratio(self, value):
		"""Gets or sets whether to use the relief ratio in this swept flange feature."""
		self._instance.UseReliefRatio = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this swept flange feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this swept flange feature."""
		self._instance.AccessSelections = value

	@property
	def get_custom_bend_allowance(self):
		"""Gets the custom bend allowance object."""
		return self._instance.GetCustomBendAllowance

	@get_custom_bend_allowance.setter
	def get_custom_bend_allowance(self, value):
		"""Gets the custom bend allowance object."""
		self._instance.GetCustomBendAllowance = value

	@property
	def get_error_codes(self):
		"""Gets the error conditions that occur during swept flange feature creation or modification."""
		return self._instance.GetErrorCodes

	@get_error_codes.setter
	def get_error_codes(self, value):
		"""Gets the error conditions that occur during swept flange feature creation or modification."""
		self._instance.GetErrorCodes = value

	@property
	def get_gauge_table_parameters(self):
		"""Gets the gauge table parameters object."""
		return self._instance.GetGaugeTableParameters

	@get_gauge_table_parameters.setter
	def get_gauge_table_parameters(self, value):
		"""Gets the gauge table parameters object."""
		self._instance.GetGaugeTableParameters = value

	@property
	def get_path_type(self):
		"""Gets the type of the sweep path in this swept flange feature."""
		return self._instance.GetPathType

	@get_path_type.setter
	def get_path_type(self, value):
		"""Gets the type of the sweep path in this swept flange feature."""
		self._instance.GetPathType = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this swept flange feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this swept flange feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_custom_bend_allowance(self):
		"""Sets the custom bend allowance for this swept flange feature."""
		return self._instance.SetCustomBendAllowance

	@set_custom_bend_allowance.setter
	def set_custom_bend_allowance(self, value):
		"""Sets the custom bend allowance for this swept flange feature."""
		self._instance.SetCustomBendAllowance = value

	@property
	def set_gauge_table_parameters(self):
		"""Sets the gauge table parameters object."""
		return self._instance.SetGaugeTableParameters

	@set_gauge_table_parameters.setter
	def set_gauge_table_parameters(self, value):
		"""Sets the gauge table parameters object."""
		self._instance.SetGaugeTableParameters = value

