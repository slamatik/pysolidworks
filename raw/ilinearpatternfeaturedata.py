# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData_members.html
class ILinearPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def auto_select(self):
		"""Gets whether to automatically select all bodies in a multibody part intersected by this linear pattern feature."""
		# return self._instance.AutoSelect
		raise NotImplemented

	@property
	def body_pattern(self):
		"""Gets or sets whether to base this linear pattern feature on bodies or features and faces."""
		return self._instance.BodyPattern

	@body_pattern.setter
	def body_pattern(self, value):
		"""Gets or sets whether to base this linear pattern feature on bodies or features and faces."""
		self._instance.BodyPattern = value

	@property
	def d_axis(self):
		"""Gets or sets Direction 1 for this linear pattern feature."""
		return self._instance.D1Axis

	@d_axis.setter
	def d_axis(self, value):
		"""Gets or sets Direction 1 for this linear pattern feature."""
		self._instance.D1Axis = value

	@property
	def d_end_condition(self):
		"""Gets or sets how to specify the spacing of pattern instances in Direction 1 of this linear pattern feature."""
		return self._instance.D1EndCondition

	@d_end_condition.setter
	def d_end_condition(self, value):
		"""Gets or sets how to specify the spacing of pattern instances in Direction 1 of this linear pattern feature."""
		self._instance.D1EndCondition = value

	@property
	def d_end_reference(self):
		"""Gets or sets the up-to reference geometry in Direction 1 for this linear pattern feature."""
		return self._instance.D1EndReference

	@d_end_reference.setter
	def d_end_reference(self, value):
		"""Gets or sets the up-to reference geometry in Direction 1 for this linear pattern feature."""
		self._instance.D1EndReference = value

	@property
	def d_end_ref_offset(self):
		"""Gets or sets the distance of the last pattern instance from the up-to reference geometry in Direction 1 of this linear pattern feature."""
		return self._instance.D1EndRefOffset

	@d_end_ref_offset.setter
	def d_end_ref_offset(self, value):
		"""Gets or sets the distance of the last pattern instance from the up-to reference geometry in Direction 1 of this linear pattern feature."""
		self._instance.D1EndRefOffset = value

	@property
	def d_end_ref_reverse_offset(self):
		"""Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear pattern feature."""
		return self._instance.D1EndRefReverseOffset

	@d_end_ref_reverse_offset.setter
	def d_end_ref_reverse_offset(self, value):
		"""Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear pattern feature."""
		self._instance.D1EndRefReverseOffset = value

	@property
	def d_end_seed_reference(self):
		"""Gets or sets the pattern seed geometry to offset from the up-to-reference geometry in Direction 1 of this linear pattern feature."""
		return self._instance.D1EndSeedReference

	@d_end_seed_reference.setter
	def d_end_seed_reference(self, value):
		"""Gets or sets the pattern seed geometry to offset from the up-to-reference geometry in Direction 1 of this linear pattern feature."""
		self._instance.D1EndSeedReference = value

	@property
	def d_end_use_seed_reference(self):
		"""Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 1 of this linear pattern feature."""
		return self._instance.D1EndUseSeedReference

	@d_end_use_seed_reference.setter
	def d_end_use_seed_reference(self, value):
		"""Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 1 of this linear pattern feature."""
		self._instance.D1EndUseSeedReference = value

	@property
	def d_end_use_spacing(self):
		"""Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 1 for this linear pattern feature."""
		return self._instance.D1EndUseSpacing

	@d_end_use_spacing.setter
	def d_end_use_spacing(self, value):
		"""Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 1 for this linear pattern feature."""
		self._instance.D1EndUseSpacing = value

	@property
	def d_reverse_direction(self):
		"""Gets whether to reverse Direction 1 in this linear pattern feature."""
		return self._instance.D1ReverseDirection

	@d_reverse_direction.setter
	def d_reverse_direction(self, value):
		"""Gets whether to reverse Direction 1 in this linear pattern feature."""
		self._instance.D1ReverseDirection = value

	@property
	def d_spacing(self):
		"""Gets or sets the spacing between pattern instances in Direction 1 of this linear pattern feature."""
		return self._instance.D1Spacing

	@d_spacing.setter
	def d_spacing(self, value):
		"""Gets or sets the spacing between pattern instances in Direction 1 of this linear pattern feature."""
		self._instance.D1Spacing = value

	@property
	def d_total_instances(self):
		"""Gets or sets the total number of pattern instances in Direction 1 for this linear pattern feature."""
		return self._instance.D1TotalInstances

	@d_total_instances.setter
	def d_total_instances(self, value):
		"""Gets or sets the total number of pattern instances in Direction 1 for this linear pattern feature."""
		self._instance.D1TotalInstances = value

	@property
	def d_axis(self):
		"""Gets or sets Direction 2 for this bidirectional linear pattern feature."""
		return self._instance.D2Axis

	@d_axis.setter
	def d_axis(self, value):
		"""Gets or sets Direction 2 for this bidirectional linear pattern feature."""
		self._instance.D2Axis = value

	@property
	def d_end_condition(self):
		"""Gets or sets how to specify the spacing of pattern instances in Direction 2 of this bidirectional linear pattern feature."""
		return self._instance.D2EndCondition

	@d_end_condition.setter
	def d_end_condition(self, value):
		"""Gets or sets how to specify the spacing of pattern instances in Direction 2 of this bidirectional linear pattern feature."""
		self._instance.D2EndCondition = value

	@property
	def d_end_reference(self):
		"""Gets or sets the up-to reference geometry in Direction 2 for this bidirectional linear pattern feature."""
		return self._instance.D2EndReference

	@d_end_reference.setter
	def d_end_reference(self, value):
		"""Gets or sets the up-to reference geometry in Direction 2 for this bidirectional linear pattern feature."""
		self._instance.D2EndReference = value

	@property
	def d_end_ref_offset(self):
		"""Gets or sets the distance of the last pattern instance from up-to reference geometry in Direction 2 of this bidirectional linear pattern feature."""
		return self._instance.D2EndRefOffset

	@d_end_ref_offset.setter
	def d_end_ref_offset(self, value):
		"""Gets or sets the distance of the last pattern instance from up-to reference geometry in Direction 2 of this bidirectional linear pattern feature."""
		self._instance.D2EndRefOffset = value

	@property
	def d_end_ref_reverse_offset(self):
		"""Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 2 of this bidirectional linear pattern feature."""
		return self._instance.D2EndRefReverseOffset

	@d_end_ref_reverse_offset.setter
	def d_end_ref_reverse_offset(self, value):
		"""Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 2 of this bidirectional linear pattern feature."""
		self._instance.D2EndRefReverseOffset = value

	@property
	def d_end_seed_reference(self):
		"""Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 2 of this bidirectional linear pattern feature."""
		return self._instance.D2EndSeedReference

	@d_end_seed_reference.setter
	def d_end_seed_reference(self, value):
		"""Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 2 of this bidirectional linear pattern feature."""
		self._instance.D2EndSeedReference = value

	@property
	def d_end_use_seed_reference(self):
		"""Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 2 of this bidirectional linear pattern feature."""
		return self._instance.D2EndUseSeedReference

	@d_end_use_seed_reference.setter
	def d_end_use_seed_reference(self, value):
		"""Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 2 of this bidirectional linear pattern feature."""
		self._instance.D2EndUseSeedReference = value

	@property
	def d_end_use_spacing(self):
		"""Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 2 for this bidirectional linear pattern feature."""
		return self._instance.D2EndUseSpacing

	@d_end_use_spacing.setter
	def d_end_use_spacing(self, value):
		"""Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 2 for this bidirectional linear pattern feature."""
		self._instance.D2EndUseSpacing = value

	@property
	def d_pattern_seed_only(self):
		"""Gets or sets whether to create a pattern in Direction 2 using the seed feature only, without replicating the pattern instances of Direction 1, in this bidirectional linear pattern feature."""
		return self._instance.D2PatternSeedOnly

	@d_pattern_seed_only.setter
	def d_pattern_seed_only(self, value):
		"""Gets or sets whether to create a pattern in Direction 2 using the seed feature only, without replicating the pattern instances of Direction 1, in this bidirectional linear pattern feature."""
		self._instance.D2PatternSeedOnly = value

	@property
	def d_reverse_direction(self):
		"""Gets whether to reverse Direction 2 in this bidirectional linear pattern feature."""
		return self._instance.D2ReverseDirection

	@d_reverse_direction.setter
	def d_reverse_direction(self, value):
		"""Gets whether to reverse Direction 2 in this bidirectional linear pattern feature."""
		self._instance.D2ReverseDirection = value

	@property
	def d_spacing(self):
		"""Gets or sets the distance between pattern instances in Direction 2 in this bidirectional linear pattern feature."""
		return self._instance.D2Spacing

	@d_spacing.setter
	def d_spacing(self, value):
		"""Gets or sets the distance between pattern instances in Direction 2 in this bidirectional linear pattern feature."""
		self._instance.D2Spacing = value

	@property
	def d_total_instances(self):
		"""Gets or sets the total number of pattern instances in Direction 2 in this bidirectional linear pattern feature."""
		return self._instance.D2TotalInstances

	@d_total_instances.setter
	def d_total_instances(self, value):
		"""Gets or sets the total number of pattern instances in Direction 2 in this bidirectional linear pattern feature."""
		self._instance.D2TotalInstances = value

	@property
	def feature_scope(self):
		"""Gets which bodies in this multibody part are affected by this linear pattern feature."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets which bodies in this multibody part are affected by this linear pattern feature."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets the bodies in this multibody part to be affected by this linear pattern feature."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets the bodies in this multibody part to be affected by this linear pattern feature."""
		self._instance.FeatureScopeBodies = value

	@property
	def geometry_pattern(self):
		"""Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature."""
		return self._instance.GeometryPattern

	@geometry_pattern.setter
	def geometry_pattern(self, value):
		"""Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature."""
		self._instance.GeometryPattern = value

	@property
	def instances_to_vary(self):
		"""Gets or sets whether to vary the spacing of pattern instances in this linear pattern feature."""
		return self._instance.InstancesToVary

	@instances_to_vary.setter
	def instances_to_vary(self, value):
		"""Gets or sets whether to vary the spacing of pattern instances in this linear pattern feature."""
		self._instance.InstancesToVary = value

	@property
	def pattern_body_array(self):
		"""Gets or sets the seed bodies in this linear pattern feature."""
		return self._instance.PatternBodyArray

	@pattern_body_array.setter
	def pattern_body_array(self, value):
		"""Gets or sets the seed bodies in this linear pattern feature."""
		self._instance.PatternBodyArray = value

	@property
	def pattern_element(self):
		"""Gets or sets the type of entities on which to base this linear pattern feature."""
		return self._instance.PatternElement

	@pattern_element.setter
	def pattern_element(self, value):
		"""Gets or sets the type of entities on which to base this linear pattern feature."""
		self._instance.PatternElement = value

	@property
	def pattern_face_array(self):
		"""Gets or sets the seed faces for this linear pattern feature."""
		return self._instance.PatternFaceArray

	@pattern_face_array.setter
	def pattern_face_array(self, value):
		"""Gets or sets the seed faces for this linear pattern feature."""
		self._instance.PatternFaceArray = value

	@property
	def pattern_feature_array(self):
		"""Gets or sets the seed features in this linear pattern feature."""
		return self._instance.PatternFeatureArray

	@pattern_feature_array.setter
	def pattern_feature_array(self, value):
		"""Gets or sets the seed features in this linear pattern feature."""
		self._instance.PatternFeatureArray = value

	@property
	def propagate_visual_property(self):
		"""Gets or sets whether pattern instances inherit the visual properties (e.g., colors, textures, etc.) of the original seed feature in this linear pattern feature."""
		return self._instance.PropagateVisualProperty

	@propagate_visual_property.setter
	def propagate_visual_property(self, value):
		"""Gets or sets whether pattern instances inherit the visual properties (e.g., colors, textures, etc.) of the original seed feature in this linear pattern feature."""
		self._instance.PropagateVisualProperty = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the items skipped in this linear pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the items skipped in this linear pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def vary_sketch(self):
		"""Gets or sets whether to allow the pattern instances of a seed sketch to vary in relation to enclosing geometry in this linear pattern feature."""
		return self._instance.VarySketch

	@vary_sketch.setter
	def vary_sketch(self, value):
		"""Gets or sets whether to allow the pattern instances of a seed sketch to vary in relation to enclosing geometry in this linear pattern feature."""
		self._instance.VarySketch = value

	@property
	def access_selections(self):
		"""Gains access to selections used to define the linear pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections used to define the linear pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_d_axis_type(self):
		"""Gets the type of geometry used to determine Direction 1 of this linear pattern feature."""
		return self._instance.GetD1AxisType

	@get_d_axis_type.setter
	def get_d_axis_type(self, value):
		"""Gets the type of geometry used to determine Direction 1 of this linear pattern feature."""
		self._instance.GetD1AxisType = value

	@property
	def get_d_axis_type(self):
		"""Gets the type of geometry used to determine Direction 2 of this linear pattern feature."""
		return self._instance.GetD2AxisType

	@get_d_axis_type.setter
	def get_d_axis_type(self, value):
		"""Gets the type of geometry used to determine Direction 2 of this linear pattern feature."""
		self._instance.GetD2AxisType = value

	@property
	def get_instance_to_vary_options(self):
		"""Gets the options for varying the spacing of pattern instances in this linear pattern feature."""
		return self._instance.GetInstanceToVaryOptions

	@get_instance_to_vary_options.setter
	def get_instance_to_vary_options(self, value):
		"""Gets the options for varying the spacing of pattern instances in this linear pattern feature."""
		self._instance.GetInstanceToVaryOptions = value

	@property
	def get_pattern_body_count(self):
		"""Gets the number of seed bodies in this linear pattern feature."""
		return self._instance.GetPatternBodyCount

	@get_pattern_body_count.setter
	def get_pattern_body_count(self, value):
		"""Gets the number of seed bodies in this linear pattern feature."""
		self._instance.GetPatternBodyCount = value

	@property
	def get_pattern_face_count(self):
		"""Gets the number of seed faces in this linear pattern feature."""
		return self._instance.GetPatternFaceCount

	@get_pattern_face_count.setter
	def get_pattern_face_count(self, value):
		"""Gets the number of seed faces in this linear pattern feature."""
		self._instance.GetPatternFaceCount = value

	@property
	def get_pattern_feature_count(self):
		"""Gets the number of seed features in this linear pattern feature."""
		return self._instance.GetPatternFeatureCount

	@get_pattern_feature_count.setter
	def get_pattern_feature_count(self, value):
		"""Gets the number of seed features in this linear pattern feature."""
		self._instance.GetPatternFeatureCount = value

	@property
	def get_skipped_item_count(self):
		"""Gets the number of instances skipped in this linear pattern feature."""
		return self._instance.GetSkippedItemCount

	@get_skipped_item_count.setter
	def get_skipped_item_count(self, value):
		"""Gets the number of instances skipped in this linear pattern feature."""
		self._instance.GetSkippedItemCount = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified instance of this linear pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified instance of this linear pattern feature."""
		self._instance.GetTransform = value

	@property
	def i_access_selections(self):
		"""Gains access to selections used to define the linear pattern feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to selections used to define the linear pattern feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_pattern_body_array(self):
		"""Gets the seed bodies for this linear pattern feature."""
		return self._instance.IGetPatternBodyArray

	@i_get_pattern_body_array.setter
	def i_get_pattern_body_array(self, value):
		"""Gets the seed bodies for this linear pattern feature."""
		self._instance.IGetPatternBodyArray = value

	@property
	def i_get_pattern_face_array(self):
		"""Gets the seed faces in this linear pattern feature."""
		return self._instance.IGetPatternFaceArray

	@i_get_pattern_face_array.setter
	def i_get_pattern_face_array(self, value):
		"""Gets the seed faces in this linear pattern feature."""
		self._instance.IGetPatternFaceArray = value

	@property
	def i_get_pattern_feature_array(self):
		"""Gets the seed features used to create this linear pattern feature."""
		return self._instance.IGetPatternFeatureArray

	@i_get_pattern_feature_array.setter
	def i_get_pattern_feature_array(self, value):
		"""Gets the seed features used to create this linear pattern feature."""
		self._instance.IGetPatternFeatureArray = value

	@property
	def i_get_skipped_item_array(self):
		"""Gets the items skipped in this linear pattern feature."""
		return self._instance.IGetSkippedItemArray

	@i_get_skipped_item_array.setter
	def i_get_skipped_item_array(self, value):
		"""Gets the items skipped in this linear pattern feature."""
		self._instance.IGetSkippedItemArray = value

	@property
	def is_direction_specified(self):
		"""Gets whether direction 2 is specified for this linear pattern feature."""
		return self._instance.IsDirection2Specified

	@is_direction_specified.setter
	def is_direction_specified(self, value):
		"""Gets whether direction 2 is specified for this linear pattern feature."""
		self._instance.IsDirection2Specified = value

	@property
	def i_set_pattern_body_array(self):
		"""Sets the seed bodies for this linear pattern feature."""
		return self._instance.ISetPatternBodyArray

	@i_set_pattern_body_array.setter
	def i_set_pattern_body_array(self, value):
		"""Sets the seed bodies for this linear pattern feature."""
		self._instance.ISetPatternBodyArray = value

	@property
	def i_set_pattern_face_array(self):
		"""Sets the list of patterned faces for this linear pattern feature."""
		return self._instance.ISetPatternFaceArray

	@i_set_pattern_face_array.setter
	def i_set_pattern_face_array(self, value):
		"""Sets the list of patterned faces for this linear pattern feature."""
		self._instance.ISetPatternFaceArray = value

	@property
	def i_set_pattern_feature_array(self):
		"""Sets a list of pattern features for this linear pattern feature."""
		return self._instance.ISetPatternFeatureArray

	@i_set_pattern_feature_array.setter
	def i_set_pattern_feature_array(self, value):
		"""Sets a list of pattern features for this linear pattern feature."""
		self._instance.ISetPatternFeatureArray = value

	@property
	def i_set_skipped_item_array(self):
		"""Sets the list of items skipped for this linear pattern feature."""
		return self._instance.ISetSkippedItemArray

	@i_set_skipped_item_array.setter
	def i_set_skipped_item_array(self, value):
		"""Sets the list of items skipped for this linear pattern feature."""
		self._instance.ISetSkippedItemArray = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created this linear pattern."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created this linear pattern."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_feature_scope(self):
		"""Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this linear pattern feature."""
		return self._instance.SetFeatureScope

	@set_feature_scope.setter
	def set_feature_scope(self, value):
		"""Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this linear pattern feature."""
		self._instance.SetFeatureScope = value

	@property
	def set_instance_to_vary_options(self):
		"""Sets the options for varying the spacing of pattern instances in this circular pattern feature."""
		return self._instance.SetInstanceToVaryOptions

	@set_instance_to_vary_options.setter
	def set_instance_to_vary_options(self, value):
		"""Sets the options for varying the spacing of pattern instances in this circular pattern feature."""
		self._instance.SetInstanceToVaryOptions = value

