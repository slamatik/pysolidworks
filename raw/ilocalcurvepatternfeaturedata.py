# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCurvePatternFeatureData_members.html
class ILocalCurvePatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def d_alignment_method(self):
		"""Gets or sets how to align the instances in this curve-driven component pattern feature."""
		return self._instance.D1AlignmentMethod

	@d_alignment_method.setter
	def d_alignment_method(self, value):
		"""Gets or sets how to align the instances in this curve-driven component pattern feature."""
		self._instance.D1AlignmentMethod = value

	@property
	def d_curve_method(self):
		"""Gets or sets how to use the curve, edge, sketch, or sketch entity selected for the pattern direction."""
		return self._instance.D1CurveMethod

	@d_curve_method.setter
	def d_curve_method(self, value):
		"""Gets or sets how to use the curve, edge, sketch, or sketch entity selected for the pattern direction."""
		self._instance.D1CurveMethod = value

	@property
	def d_direction(self):
		"""Gets or sets Direction 1 using the selected curve, edge, sketch, or sketch entity for this curve-driven component pattern feature."""
		return self._instance.D1Direction

	@d_direction.setter
	def d_direction(self, value):
		"""Gets or sets Direction 1 using the selected curve, edge, sketch, or sketch entity for this curve-driven component pattern feature."""
		self._instance.D1Direction = value

	@property
	def d_face_normal(self):
		"""Gets or sets the face on which the 3D curve lies for this curve-driven component pattern feature."""
		return self._instance.D1FaceNormal

	@d_face_normal.setter
	def d_face_normal(self, value):
		"""Gets or sets the face on which the 3D curve lies for this curve-driven component pattern feature."""
		self._instance.D1FaceNormal = value

	@property
	def d_instance_count(self):
		"""Gets or sets the number of instances of the seed component in Direction 1 in this curve-driven component pattern feature."""
		return self._instance.D1InstanceCount

	@d_instance_count.setter
	def d_instance_count(self, value):
		"""Gets or sets the number of instances of the seed component in Direction 1 in this curve-driven component pattern feature."""
		self._instance.D1InstanceCount = value

	@property
	def d_is_equal_spaced(self):
		"""Gets or sets whether to use equal spacing between instances of the pattern in Direction 1 for this curve-driven component pattern feature."""
		return self._instance.D1IsEqualSpaced

	@d_is_equal_spaced.setter
	def d_is_equal_spaced(self, value):
		"""Gets or sets whether to use equal spacing between instances of the pattern in Direction 1 for this curve-driven component pattern feature."""
		self._instance.D1IsEqualSpaced = value

	@property
	def d_reference_point(self):
		"""Gets or sets the reference point for Direction 1 for this curve-driven component pattern feature."""
		return self._instance.D1ReferencePoint

	@d_reference_point.setter
	def d_reference_point(self, value):
		"""Gets or sets the reference point for Direction 1 for this curve-driven component pattern feature."""
		self._instance.D1ReferencePoint = value

	@property
	def d_reverse_direction(self):
		"""Gets or sets whether to reverse the direction of Direction 1 in this curve-driven component pattern feature."""
		return self._instance.D1ReverseDirection

	@d_reverse_direction.setter
	def d_reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of Direction 1 in this curve-driven component pattern feature."""
		self._instance.D1ReverseDirection = value

	@property
	def d_spacing(self):
		"""Gets or sets the distance between pattern instances in Direction 1 in this curve-driven component pattern feature."""
		return self._instance.D1Spacing

	@d_spacing.setter
	def d_spacing(self, value):
		"""Gets or sets the distance between pattern instances in Direction 1 in this curve-driven component pattern feature."""
		self._instance.D1Spacing = value

	@property
	def d_direction(self):
		"""Gets or sets Direction 2 using the selected curve, edge, sketch, or sketch entity for this bidirectional curve-driven component pattern feature."""
		return self._instance.D2Direction

	@d_direction.setter
	def d_direction(self, value):
		"""Gets or sets Direction 2 using the selected curve, edge, sketch, or sketch entity for this bidirectional curve-driven component pattern feature."""
		self._instance.D2Direction = value

	@property
	def d_instance_count(self):
		"""Gets or sets the number of instances of the seed component in Direction 2 in this bidirectional curve-driven component pattern feature."""
		return self._instance.D2InstanceCount

	@d_instance_count.setter
	def d_instance_count(self, value):
		"""Gets or sets the number of instances of the seed component in Direction 2 in this bidirectional curve-driven component pattern feature."""
		self._instance.D2InstanceCount = value

	@property
	def d_is_equal_spaced(self):
		"""Gets or sets whether to use equal spacing between instances of the pattern in Direction 2 for this bidirectional curve-driven component pattern feature."""
		return self._instance.D2IsEqualSpaced

	@d_is_equal_spaced.setter
	def d_is_equal_spaced(self, value):
		"""Gets or sets whether to use equal spacing between instances of the pattern in Direction 2 for this bidirectional curve-driven component pattern feature."""
		self._instance.D2IsEqualSpaced = value

	@property
	def d_pattern_seed_only(self):
		"""Gets or sets whether to only pattern the seed component in Direction 2 in this bidirectional curve-driven component pattern feature."""
		return self._instance.D2PatternSeedOnly

	@d_pattern_seed_only.setter
	def d_pattern_seed_only(self, value):
		"""Gets or sets whether to only pattern the seed component in Direction 2 in this bidirectional curve-driven component pattern feature."""
		self._instance.D2PatternSeedOnly = value

	@property
	def d_reverse_direction(self):
		"""Gets or sets whether to reverse the direction of Direction 2 in this bidirectional curve-driven component pattern feature."""
		return self._instance.D2ReverseDirection

	@d_reverse_direction.setter
	def d_reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of Direction 2 in this bidirectional curve-driven component pattern feature."""
		self._instance.D2ReverseDirection = value

	@property
	def d_spacing(self):
		"""Gets or sets the distance between pattern instances in Direction 2 in this bidirectional curve-driven component pattern feature."""
		return self._instance.D2Spacing

	@d_spacing.setter
	def d_spacing(self, value):
		"""Gets or sets the distance between pattern instances in Direction 2 in this bidirectional curve-driven component pattern feature."""
		self._instance.D2Spacing = value

	@property
	def dir_specified(self):
		"""Gets or sets whether to create a bidirectional pattern for this curve-driven component pattern feature."""
		return self._instance.Dir2Specified

	@dir_specified.setter
	def dir_specified(self, value):
		"""Gets or sets whether to create a bidirectional pattern for this curve-driven component pattern feature."""
		self._instance.Dir2Specified = value

	@property
	def force_use_seed_configuration(self):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local curve pattern feature."""
		return self._instance.ForceUseSeedConfiguration

	@force_use_seed_configuration.setter
	def force_use_seed_configuration(self, value):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local curve pattern feature."""
		self._instance.ForceUseSeedConfiguration = value

	@property
	def pattern_component_array(self):
		"""Gets or sets the components in this curve-driven component pattern feature."""
		return self._instance.PatternComponentArray

	@pattern_component_array.setter
	def pattern_component_array(self, value):
		"""Gets or sets the components in this curve-driven component pattern feature."""
		self._instance.PatternComponentArray = value

	@property
	def selected_point(self):
		"""Gets or sets the reference point for this curve-driven component pattern feature."""
		return self._instance.SelectedPoint

	@selected_point.setter
	def selected_point(self, value):
		"""Gets or sets the reference point for this curve-driven component pattern feature."""
		self._instance.SelectedPoint = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the array of skipped components in this curve-driven component pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the array of skipped components in this curve-driven component pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this curve-driven component pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this curve-driven component pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_pattern_component_count(self):
		"""Gets the number of components in this curve-driven component pattern feature."""
		return self._instance.GetPatternComponentCount

	@get_pattern_component_count.setter
	def get_pattern_component_count(self, value):
		"""Gets the number of components in this curve-driven component pattern feature."""
		self._instance.GetPatternComponentCount = value

	@property
	def get_skipped_item_count(self):
		"""Gets the number of components skipped in this curve-driven component pattern feature."""
		return self._instance.GetSkippedItemCount

	@get_skipped_item_count.setter
	def get_skipped_item_count(self, value):
		"""Gets the number of components skipped in this curve-driven component pattern feature."""
		self._instance.GetSkippedItemCount = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified instance in this curve-driven component pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified instance in this curve-driven component pattern feature."""
		self._instance.GetTransform = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this curve-driven component pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this curve-driven component pattern feature."""
		self._instance.ReleaseSelectionAccess = value

