# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html
class IBaseFlangeFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bend_radius(self):
		"""Gets or sets the bend radius of the bend flange feature."""
		return self._instance.BendRadius

	@bend_radius.setter
	def bend_radius(self, value):
		"""Gets or sets the bend radius of the bend flange feature."""
		self._instance.BendRadius = value

	@property
	def d_offset_distance(self):
		"""Gets or sets the offset distance for Direction 1 for this base flange feature."""
		return self._instance.D1OffsetDistance

	@d_offset_distance.setter
	def d_offset_distance(self, value):
		"""Gets or sets the offset distance for Direction 1 for this base flange feature."""
		self._instance.D1OffsetDistance = value

	@property
	def d_offset_reference(self):
		"""Gets or sets the offset reference for Direction 1 for this base flange feature."""
		return self._instance.D1OffsetReference

	@d_offset_reference.setter
	def d_offset_reference(self, value):
		"""Gets or sets the offset reference for Direction 1 for this base flange feature."""
		self._instance.D1OffsetReference = value

	@property
	def d_offset_type(self):
		"""Gets or sets the offset type for Direction 1 for this base flange feature."""
		return self._instance.D1OffsetType

	@d_offset_type.setter
	def d_offset_type(self, value):
		"""Gets or sets the offset type for Direction 1 for this base flange feature."""
		self._instance.D1OffsetType = value

	@property
	def d_reverse_offset(self):
		"""Gets or sets whether the offset for Direction 1 is reversed for this base flange feature."""
		return self._instance.D1ReverseOffset

	@d_reverse_offset.setter
	def d_reverse_offset(self, value):
		"""Gets or sets whether the offset for Direction 1 is reversed for this base flange feature."""
		self._instance.D1ReverseOffset = value

	@property
	def d_offset_distance(self):
		"""Gets or sets the offset distance for Direction 2 for this base flange feature."""
		return self._instance.D2OffsetDistance

	@d_offset_distance.setter
	def d_offset_distance(self, value):
		"""Gets or sets the offset distance for Direction 2 for this base flange feature."""
		self._instance.D2OffsetDistance = value

	@property
	def d_offset_reference(self):
		"""Gets or sets the offset reference for Direction 2 for this base flange feature."""
		return self._instance.D2OffsetReference

	@d_offset_reference.setter
	def d_offset_reference(self, value):
		"""Gets or sets the offset reference for Direction 2 for this base flange feature."""
		self._instance.D2OffsetReference = value

	@property
	def d_offset_type(self):
		"""Gets or sets the offset type for Direction 2 for this base flange feature."""
		return self._instance.D2OffsetType

	@d_offset_type.setter
	def d_offset_type(self, value):
		"""Gets or sets the offset type for Direction 2 for this base flange feature."""
		self._instance.D2OffsetType = value

	@property
	def d_reverse_offset(self):
		"""Gets or sets whether the offset for Direction 2 is reversed for this base flange feature."""
		return self._instance.D2ReverseOffset

	@d_reverse_offset.setter
	def d_reverse_offset(self, value):
		"""Gets or sets whether the offset for Direction 2 is reversed for this base flange feature."""
		self._instance.D2ReverseOffset = value

	@property
	def gauge_table_path(self):
		"""Gets or sets the path to a gauge table file for this base flange feature"""
		return self._instance.GaugeTablePath

	@gauge_table_path.setter
	def gauge_table_path(self, value):
		"""Gets or sets the path to a gauge table file for this base flange feature"""
		self._instance.GaugeTablePath = value

	@property
	def k_factor(self):
		"""Gets or sets the K-factor for this base-flange feature."""
		return self._instance.KFactor

	@k_factor.setter
	def k_factor(self, value):
		"""Gets or sets the K-factor for this base-flange feature."""
		self._instance.KFactor = value

	@property
	def offset_directions(self):
		"""Gets or sets the number of offset directions for this base flange feature."""
		return self._instance.OffsetDirections

	@offset_directions.setter
	def offset_directions(self, value):
		"""Gets or sets the number of offset directions for this base flange feature."""
		self._instance.OffsetDirections = value

	@property
	def override_k_factor(self):
		"""gets or sets whether to override the K-factor value specified in the gauge table for this base flange feature."""
		return self._instance.OverrideKFactor

	@override_k_factor.setter
	def override_k_factor(self, value):
		"""gets or sets whether to override the K-factor value specified in the gauge table for this base flange feature."""
		self._instance.OverrideKFactor = value

	@property
	def override_radius(self):
		"""Gets or sets whether to override the bend radius value specified in the gauge table for this base flange feature."""
		return self._instance.OverrideRadius

	@override_radius.setter
	def override_radius(self, value):
		"""Gets or sets whether to override the bend radius value specified in the gauge table for this base flange feature."""
		self._instance.OverrideRadius = value

	@property
	def override_thickness(self):
		"""Gets or sets whether to override the thickness value specified in the gauge table for this base flange feature."""
		return self._instance.OverrideThickness

	@override_thickness.setter
	def override_thickness(self, value):
		"""Gets or sets whether to override the thickness value specified in the gauge table for this base flange feature."""
		self._instance.OverrideThickness = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of the base flange feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of the base flange feature."""
		self._instance.ReverseDirection = value

	@property
	def reverse_thickness(self):
		"""Gets or sets the direction in which to thicken the sketch for the base flange feature."""
		return self._instance.ReverseThickness

	@reverse_thickness.setter
	def reverse_thickness(self, value):
		"""Gets or sets the direction in which to thicken the sketch for the base flange feature."""
		self._instance.ReverseThickness = value

	@property
	def table_k_factor(self):
		"""Gets the K-factor to use, if it is not overridden, from the gauge table for this base flange feature."""
		return self._instance.TableKFactor

	@table_k_factor.setter
	def table_k_factor(self, value):
		"""Gets the K-factor to use, if it is not overridden, from the gauge table for this base flange feature."""
		self._instance.TableKFactor = value

	@property
	def table_radius(self):
		"""Gets or sets the bend radius, if is not overridden, in the gauge table for this base flange feature."""
		return self._instance.TableRadius

	@table_radius.setter
	def table_radius(self, value):
		"""Gets or sets the bend radius, if is not overridden, in the gauge table for this base flange feature."""
		self._instance.TableRadius = value

	@property
	def table_thickness(self):
		"""Gets or sets the thickness, if it is not overridden, in the gauge table for this base flange feature."""
		return self._instance.TableThickness

	@table_thickness.setter
	def table_thickness(self, value):
		"""Gets or sets the thickness, if it is not overridden, in the gauge table for this base flange feature."""
		self._instance.TableThickness = value

	@property
	def thickness(self):
		"""Gets or sets the thickness for this base flange feature."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or sets the thickness for this base flange feature."""
		self._instance.Thickness = value

	@property
	def thickness_table_name(self):
		"""Gets or sets the name of the thickness from the gauge table, if thickness not overridden, for this base flange feature."""
		return self._instance.ThicknessTableName

	@thickness_table_name.setter
	def thickness_table_name(self, value):
		"""Gets or sets the name of the thickness from the gauge table, if thickness not overridden, for this base flange feature."""
		self._instance.ThicknessTableName = value

	@property
	def use_gauge_table(self):
		"""Gets or sets whether to use a gauge table for this base flange feature."""
		return self._instance.UseGaugeTable

	@use_gauge_table.setter
	def use_gauge_table(self, value):
		"""Gets or sets whether to use a gauge table for this base flange feature."""
		self._instance.UseGaugeTable = value

	@property
	def access_selections(self):
		"""Allows access to the selections that describe this base flange feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Allows access to the selections that describe this base flange feature."""
		self._instance.AccessSelections = value

	@property
	def get_d_offset_reference_type(self):
		"""Gets the type of reference geometry for Direction 1 for this base flange feature."""
		return self._instance.GetD1OffsetReferenceType

	@get_d_offset_reference_type.setter
	def get_d_offset_reference_type(self, value):
		"""Gets the type of reference geometry for Direction 1 for this base flange feature."""
		self._instance.GetD1OffsetReferenceType = value

	@property
	def get_d_offset_reference_type(self):
		"""Gets the type of reference geometry for Direction 2 for this base flange feature."""
		return self._instance.GetD2OffsetReferenceType

	@get_d_offset_reference_type.setter
	def get_d_offset_reference_type(self, value):
		"""Gets the type of reference geometry for Direction 2 for this base flange feature."""
		self._instance.GetD2OffsetReferenceType = value

	@property
	def get_table_radii(self):
		"""Gets the bend radii from the gauge table for this base flange feature."""
		return self._instance.GetTableRadii

	@get_table_radii.setter
	def get_table_radii(self, value):
		"""Gets the bend radii from the gauge table for this base flange feature."""
		self._instance.GetTableRadii = value

	@property
	def get_table_radii_count(self):
		"""Gets the number of bend radii for the thickness names from the gauge table for this base flange feature."""
		return self._instance.GetTableRadiiCount

	@get_table_radii_count.setter
	def get_table_radii_count(self, value):
		"""Gets the number of bend radii for the thickness names from the gauge table for this base flange feature."""
		self._instance.GetTableRadiiCount = value

	@property
	def get_table_thicknesses(self):
		"""Gets the names of the thicknesses from the gauge table for this base flange feature."""
		return self._instance.GetTableThicknesses

	@get_table_thicknesses.setter
	def get_table_thicknesses(self, value):
		"""Gets the names of the thicknesses from the gauge table for this base flange feature."""
		self._instance.GetTableThicknesses = value

	@property
	def get_table_thicknesses_count(self):
		"""Gets the number of names of the thicknesses in the gauge table for this base flange feature."""
		return self._instance.GetTableThicknessesCount

	@get_table_thicknesses_count.setter
	def get_table_thicknesses_count(self, value):
		"""Gets the number of names of the thicknesses in the gauge table for this base flange feature."""
		self._instance.GetTableThicknessesCount = value

	@property
	def i_access_selections(self):
		"""Allows access to the selections that describe this base flange feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Allows access to the selections that describe this base flange feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_table_radii(self):
		"""Gets the bend radii from the gauge table for this base flange feature."""
		return self._instance.IGetTableRadii

	@i_get_table_radii.setter
	def i_get_table_radii(self, value):
		"""Gets the bend radii from the gauge table for this base flange feature."""
		self._instance.IGetTableRadii = value

	@property
	def i_get_table_thicknesses(self):
		"""Gets the names of the thicknesses from the gauge table for this base flange feature."""
		return self._instance.IGetTableThicknesses

	@i_get_table_thicknesses.setter
	def i_get_table_thicknesses(self, value):
		"""Gets the names of the thicknesses from the gauge table for this base flange feature."""
		self._instance.IGetTableThicknesses = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe this base flange feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe this base flange feature."""
		self._instance.ReleaseSelectionAccess = value

