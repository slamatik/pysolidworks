# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.html
class IJogFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bend_radius(self):
		"""Gets or sets the bend radius for this jog feature."""
		return self._instance.BendRadius

	@bend_radius.setter
	def bend_radius(self, value):
		"""Gets or sets the bend radius for this jog feature."""
		self._instance.BendRadius = value

	@property
	def dimension_position_type(self):
		"""Gets or sets the dimension position type for this jog feature."""
		return self._instance.DimensionPositionType

	@dimension_position_type.setter
	def dimension_position_type(self, value):
		"""Gets or sets the dimension position type for this jog feature."""
		self._instance.DimensionPositionType = value

	@property
	def fixed_face(self):
		"""Gets or sets the fixed face for this jog feature."""
		return self._instance.FixedFace

	@fixed_face.setter
	def fixed_face(self, value):
		"""Gets or sets the fixed face for this jog feature."""
		self._instance.FixedFace = value

	@property
	def fixed_point(self):
		"""Gets or sets the fixed point x, y, z coordinates for this jog feature."""
		return self._instance.FixedPoint

	@fixed_point.setter
	def fixed_point(self, value):
		"""Gets or sets the fixed point x, y, z coordinates for this jog feature."""
		self._instance.FixedPoint = value

	@property
	def fix_projected_length(self):
		"""Gets or sets whether to fix the projected length for this jog feature."""
		return self._instance.FixProjectedLength

	@fix_projected_length.setter
	def fix_projected_length(self, value):
		"""Gets or sets whether to fix the projected length for this jog feature."""
		self._instance.FixProjectedLength = value

	@property
	def jog_angle(self):
		"""Gets or sets the jog angle for this jog feature."""
		return self._instance.JogAngle

	@jog_angle.setter
	def jog_angle(self, value):
		"""Gets or sets the jog angle for this jog feature."""
		self._instance.JogAngle = value

	@property
	def jog_position_type(self):
		"""Gets or sets the jog position type for this jog feature."""
		return self._instance.JogPositionType

	@jog_position_type.setter
	def jog_position_type(self, value):
		"""Gets or sets the jog position type for this jog feature."""
		self._instance.JogPositionType = value

	@property
	def offset_distance(self):
		"""Gets or sets the offset distance for this jog feature."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the offset distance for this jog feature."""
		self._instance.OffsetDistance = value

	@property
	def offset_reference(self):
		"""Gets or sets the offset reference for this jog feature."""
		return self._instance.OffsetReference

	@offset_reference.setter
	def offset_reference(self, value):
		"""Gets or sets the offset reference for this jog feature."""
		self._instance.OffsetReference = value

	@property
	def offset_type(self):
		"""Gets or sets the offset type for this jog feature."""
		return self._instance.OffsetType

	@offset_type.setter
	def offset_type(self, value):
		"""Gets or sets the offset type for this jog feature."""
		self._instance.OffsetType = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of this jog feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of this jog feature."""
		self._instance.ReverseDirection = value

	@property
	def reverse_offset(self):
		"""Gets or sets whether to reverse the offset of this jog feature."""
		return self._instance.ReverseOffset

	@reverse_offset.setter
	def reverse_offset(self, value):
		"""Gets or sets whether to reverse the offset of this jog feature."""
		self._instance.ReverseOffset = value

	@property
	def use_default_bend_allowance(self):
		"""Gets or sets whether to use the default bend allowance for this jog feature."""
		return self._instance.UseDefaultBendAllowance

	@use_default_bend_allowance.setter
	def use_default_bend_allowance(self, value):
		"""Gets or sets whether to use the default bend allowance for this jog feature."""
		self._instance.UseDefaultBendAllowance = value

	@property
	def use_default_bend_radius(self):
		"""Gets or sets whether to use the default bend radius for this jog feature."""
		return self._instance.UseDefaultBendRadius

	@use_default_bend_radius.setter
	def use_default_bend_radius(self, value):
		"""Gets or sets whether to use the default bend radius for this jog feature."""
		self._instance.UseDefaultBendRadius = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this jog feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this jog feature."""
		self._instance.AccessSelections = value

	@property
	def get_custom_bend_allowance(self):
		"""Gets the custom bend allowance for this jog feature."""
		return self._instance.GetCustomBendAllowance

	@get_custom_bend_allowance.setter
	def get_custom_bend_allowance(self, value):
		"""Gets the custom bend allowance for this jog feature."""
		self._instance.GetCustomBendAllowance = value

	@property
	def get_offset_reference_type(self):
		"""Gets the offset reference geometry type for this jog feature."""
		return self._instance.GetOffsetReferenceType

	@get_offset_reference_type.setter
	def get_offset_reference_type(self, value):
		"""Gets the offset reference geometry type for this jog feature."""
		self._instance.GetOffsetReferenceType = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this jog feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this jog feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_fixed_point(self):
		"""Gets the fixed-point x, y, z coordinates for this jog feature."""
		return self._instance.IGetFixedPoint

	@i_get_fixed_point.setter
	def i_get_fixed_point(self, value):
		"""Gets the fixed-point x, y, z coordinates for this jog feature."""
		self._instance.IGetFixedPoint = value

	@property
	def i_set_fixed_point(self):
		"""Sets the fixed-point x, y, z coordinates for this jog feature."""
		return self._instance.ISetFixedPoint

	@i_set_fixed_point.setter
	def i_set_fixed_point(self, value):
		"""Sets the fixed-point x, y, z coordinates for this jog feature."""
		self._instance.ISetFixedPoint = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this jog feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this jog feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_custom_bend_allowance(self):
		"""Sets the custom bend allowance for this jog feature."""
		return self._instance.SetCustomBendAllowance

	@set_custom_bend_allowance.setter
	def set_custom_bend_allowance(self, value):
		"""Sets the custom bend allowance for this jog feature."""
		self._instance.SetCustomBendAllowance = value

