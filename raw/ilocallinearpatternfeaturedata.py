# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html
class ILocalLinearPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def align_to_seed(self):
		"""Gets or sets whether to align each instance to match the original alignment of the seed component in this linear component pattern feature."""
		return self._instance.AlignToSeed

	@align_to_seed.setter
	def align_to_seed(self, value):
		"""Gets or sets whether to align each instance to match the original alignment of the seed component in this linear component pattern feature."""
		self._instance.AlignToSeed = value

	@property
	def d_axis(self):
		"""Gets or sets Direction 1 for this linear component pattern feature."""
		return self._instance.D1Axis

	@d_axis.setter
	def d_axis(self, value):
		"""Gets or sets Direction 1 for this linear component pattern feature."""
		self._instance.D1Axis = value

	@property
	def d_end_condition(self):
		"""Gets or sets how to specify the spacing of pattern instances in Direction 1 of this linear component pattern feature."""
		return self._instance.D1EndCondition

	@d_end_condition.setter
	def d_end_condition(self, value):
		"""Gets or sets how to specify the spacing of pattern instances in Direction 1 of this linear component pattern feature."""
		self._instance.D1EndCondition = value

	@property
	def d_end_reference(self):
		"""Gets or sets the up-to reference entity in Direction 1 for this linear component pattern feature."""
		return self._instance.D1EndReference

	@d_end_reference.setter
	def d_end_reference(self, value):
		"""Gets or sets the up-to reference entity in Direction 1 for this linear component pattern feature."""
		self._instance.D1EndReference = value

	@property
	def d_end_reference_type(self):
		"""Gets the type of ILocalLinearPatternFeatureData::D1EndReference."""
		return self._instance.D1EndReferenceType

	@d_end_reference_type.setter
	def d_end_reference_type(self, value):
		"""Gets the type of ILocalLinearPatternFeatureData::D1EndReference."""
		self._instance.D1EndReferenceType = value

	@property
	def d_end_ref_offset(self):
		"""Gets or sets the offset from a reference entity in Direction 1 of this linear component pattern feature."""
		return self._instance.D1EndRefOffset

	@d_end_ref_offset.setter
	def d_end_ref_offset(self, value):
		"""Gets or sets the offset from a reference entity in Direction 1 of this linear component pattern feature."""
		self._instance.D1EndRefOffset = value

	@property
	def d_end_ref_reverse_offset(self):
		"""Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear component pattern feature."""
		return self._instance.D1EndRefReverseOffset

	@d_end_ref_reverse_offset.setter
	def d_end_ref_reverse_offset(self, value):
		"""Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 1 of this linear component pattern feature."""
		self._instance.D1EndRefReverseOffset = value

	@property
	def d_end_seed_reference(self):
		"""Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 1 of this linear componnet pattern feature."""
		return self._instance.D1EndSeedReference

	@d_end_seed_reference.setter
	def d_end_seed_reference(self, value):
		"""Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 1 of this linear componnet pattern feature."""
		self._instance.D1EndSeedReference = value

	@property
	def d_end_seed_reference_type(self):
		"""Gets the type of ILocalLinearPatternFeatureData::D1EndSeedReference."""
		return self._instance.D1EndSeedReferenceType

	@d_end_seed_reference_type.setter
	def d_end_seed_reference_type(self, value):
		"""Gets the type of ILocalLinearPatternFeatureData::D1EndSeedReference."""
		self._instance.D1EndSeedReferenceType = value

	@property
	def d_end_use_seed_reference(self):
		"""Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 1 of this linear component pattern feature."""
		return self._instance.D1EndUseSeedReference

	@d_end_use_seed_reference.setter
	def d_end_use_seed_reference(self, value):
		"""Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 1 of this linear component pattern feature."""
		self._instance.D1EndUseSeedReference = value

	@property
	def d_end_use_spacing(self):
		"""Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 1 for this linear component pattern feature."""
		return self._instance.D1EndUseSpacing

	@d_end_use_spacing.setter
	def d_end_use_spacing(self, value):
		"""Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 1 for this linear component pattern feature."""
		self._instance.D1EndUseSpacing = value

	@property
	def d_reverse_direction(self):
		"""Gets or sets whether to reverse Direction 1 in this linear component pattern feature."""
		return self._instance.D1ReverseDirection

	@d_reverse_direction.setter
	def d_reverse_direction(self, value):
		"""Gets or sets whether to reverse Direction 1 in this linear component pattern feature."""
		self._instance.D1ReverseDirection = value

	@property
	def d_spacing(self):
		"""Gets the distance between pattern instances in Direction 1 of this linear component pattern feature."""
		return self._instance.D1Spacing

	@d_spacing.setter
	def d_spacing(self, value):
		"""Gets the distance between pattern instances in Direction 1 of this linear component pattern feature."""
		self._instance.D1Spacing = value

	@property
	def d_total_instances(self):
		"""Gets or sets the total number of instances in Direction 1, including skipped items, in this linear component pattern feature."""
		return self._instance.D1TotalInstances

	@d_total_instances.setter
	def d_total_instances(self, value):
		"""Gets or sets the total number of instances in Direction 1, including skipped items, in this linear component pattern feature."""
		self._instance.D1TotalInstances = value

	@property
	def d_axis(self):
		"""Gets or sets Direction 2 for this bidirectional linear component pattern feature."""
		return self._instance.D2Axis

	@d_axis.setter
	def d_axis(self, value):
		"""Gets or sets Direction 2 for this bidirectional linear component pattern feature."""
		self._instance.D2Axis = value

	@property
	def d_end_condition(self):
		"""Gets or sets how to specify the spacing of pattern instances in Direction 2 of this bidirectional linear component pattern feature."""
		return self._instance.D2EndCondition

	@d_end_condition.setter
	def d_end_condition(self, value):
		"""Gets or sets how to specify the spacing of pattern instances in Direction 2 of this bidirectional linear component pattern feature."""
		self._instance.D2EndCondition = value

	@property
	def d_end_reference(self):
		"""Gets or sets the up-to reference geometry in Direction 2 for this bidirectional linear component pattern feature."""
		return self._instance.D2EndReference

	@d_end_reference.setter
	def d_end_reference(self, value):
		"""Gets or sets the up-to reference geometry in Direction 2 for this bidirectional linear component pattern feature."""
		self._instance.D2EndReference = value

	@property
	def d_end_reference_type(self):
		"""Gets the type ILocalLinearPatternFeatureData::D2EndReference."""
		return self._instance.D2EndReferenceType

	@d_end_reference_type.setter
	def d_end_reference_type(self, value):
		"""Gets the type ILocalLinearPatternFeatureData::D2EndReference."""
		self._instance.D2EndReferenceType = value

	@property
	def d_end_ref_offset(self):
		"""Gets or sets the distance of the last pattern instance from up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature."""
		return self._instance.D2EndRefOffset

	@d_end_ref_offset.setter
	def d_end_ref_offset(self, value):
		"""Gets or sets the distance of the last pattern instance from up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature."""
		self._instance.D2EndRefOffset = value

	@property
	def d_end_ref_reverse_offset(self):
		"""Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 2 of this bidirectional linear component pattern feature."""
		return self._instance.D2EndRefReverseOffset

	@d_end_ref_reverse_offset.setter
	def d_end_ref_reverse_offset(self, value):
		"""Gets or sets whether to reverse the offset from the up-to-reference geometry in Direction 2 of this bidirectional linear component pattern feature."""
		self._instance.D2EndRefReverseOffset = value

	@property
	def d_end_seed_reference(self):
		"""Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature."""
		return self._instance.D2EndSeedReference

	@d_end_seed_reference.setter
	def d_end_seed_reference(self, value):
		"""Gets or sets the seed feature geometry to offset from the up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature."""
		self._instance.D2EndSeedReference = value

	@property
	def d_end_seed_reference_type(self):
		"""Gets the type of ILocalLinearPatternFeatureData::D2EndSeedReference."""
		return self._instance.D2EndSeedReferenceType

	@d_end_seed_reference_type.setter
	def d_end_seed_reference_type(self, value):
		"""Gets the type of ILocalLinearPatternFeatureData::D2EndSeedReference."""
		self._instance.D2EndSeedReferenceType = value

	@property
	def d_end_use_seed_reference(self):
		"""Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature."""
		return self._instance.D2EndUseSeedReference

	@d_end_use_seed_reference.setter
	def d_end_use_seed_reference(self, value):
		"""Gets or sets whether to offset a pattern seed reference or a centroid from the up-to reference geometry in Direction 2 of this bidirectional linear component pattern feature."""
		self._instance.D2EndUseSeedReference = value

	@property
	def d_end_use_spacing(self):
		"""Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 2 for this bidirectional linear component pattern feature."""
		return self._instance.D2EndUseSpacing

	@d_end_use_spacing.setter
	def d_end_use_spacing(self, value):
		"""Gets or sets whether to use spacing or a number of pattern instances when offsetting up-to reference geometry in Direction 2 for this bidirectional linear component pattern feature."""
		self._instance.D2EndUseSpacing = value

	@property
	def d_pattern_seed_only(self):
		"""Gets or sets whether to create a pattern in Direction 2 using the seed component only, without replicating the pattern instances of Direction 1, in this bidirectional linear component pattern feature."""
		return self._instance.D2PatternSeedOnly

	@d_pattern_seed_only.setter
	def d_pattern_seed_only(self, value):
		"""Gets or sets whether to create a pattern in Direction 2 using the seed component only, without replicating the pattern instances of Direction 1, in this bidirectional linear component pattern feature."""
		self._instance.D2PatternSeedOnly = value

	@property
	def d_reverse_direction(self):
		"""Gets or sets whether to reverse Direction 2 in this bidirectional linear component pattern feature."""
		return self._instance.D2ReverseDirection

	@d_reverse_direction.setter
	def d_reverse_direction(self, value):
		"""Gets or sets whether to reverse Direction 2 in this bidirectional linear component pattern feature."""
		self._instance.D2ReverseDirection = value

	@property
	def d_spacing(self):
		"""Gets the spacing between pattern instances in Direction 2 in this bidirectional linear component pattern feature."""
		return self._instance.D2Spacing

	@d_spacing.setter
	def d_spacing(self, value):
		"""Gets the spacing between pattern instances in Direction 2 in this bidirectional linear component pattern feature."""
		self._instance.D2Spacing = value

	@property
	def d_total_instances(self):
		"""Gets or sets the total number of instances in Direction 2, including skipped items, in this bidirectional linear component pattern feature."""
		return self._instance.D2TotalInstances

	@d_total_instances.setter
	def d_total_instances(self, value):
		"""Gets or sets the total number of instances in Direction 2, including skipped items, in this bidirectional linear component pattern feature."""
		self._instance.D2TotalInstances = value

	@property
	def fixed_axis_of_rotation(self):
		"""Gets or sets whether patterned instances rotate around a common axis."""
		return self._instance.FixedAxisOfRotation

	@fixed_axis_of_rotation.setter
	def fixed_axis_of_rotation(self, value):
		"""Gets or sets whether patterned instances rotate around a common axis."""
		self._instance.FixedAxisOfRotation = value

	@property
	def force_use_seed_configuration(self):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local linear pattern feature."""
		return self._instance.ForceUseSeedConfiguration

	@force_use_seed_configuration.setter
	def force_use_seed_configuration(self, value):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local linear pattern feature."""
		self._instance.ForceUseSeedConfiguration = value

	@property
	def reverse_axis_of_rotation(self):
		"""Gets or sets whether to reverse the direction of rotation."""
		return self._instance.ReverseAxisOfRotation

	@reverse_axis_of_rotation.setter
	def reverse_axis_of_rotation(self, value):
		"""Gets or sets whether to reverse the direction of rotation."""
		self._instance.ReverseAxisOfRotation = value

	@property
	def rotate_instances(self):
		"""Gets or sets whether to rotate components in Direction 1 of this linear component pattern."""
		return self._instance.RotateInstances

	@rotate_instances.setter
	def rotate_instances(self, value):
		"""Gets or sets whether to rotate components in Direction 1 of this linear component pattern."""
		self._instance.RotateInstances = value

	@property
	def rotation_angle(self):
		"""Gets or sets the angle of rotation of instances in this linear component pattern."""
		return self._instance.RotationAngle

	@rotation_angle.setter
	def rotation_angle(self, value):
		"""Gets or sets the angle of rotation of instances in this linear component pattern."""
		self._instance.RotationAngle = value

	@property
	def rotation_axis(self):
		"""Gets or sets the axis of rotation of components in this linear component pattern feature."""
		return self._instance.RotationAxis

	@rotation_axis.setter
	def rotation_axis(self, value):
		"""Gets or sets the axis of rotation of components in this linear component pattern feature."""
		self._instance.RotationAxis = value

	@property
	def seed_alignment_reference_point(self):
		"""Gets or sets the type of reference point with which to align each pattern instance to the seed feature."""
		return self._instance.SeedAlignmentReferencePoint

	@seed_alignment_reference_point.setter
	def seed_alignment_reference_point(self, value):
		"""Gets or sets the type of reference point with which to align each pattern instance to the seed feature."""
		self._instance.SeedAlignmentReferencePoint = value

	@property
	def seed_component_array(self):
		"""Gets or sets the seed components for this linear component pattern feature."""
		return self._instance.SeedComponentArray

	@seed_component_array.setter
	def seed_component_array(self, value):
		"""Gets or sets the seed components for this linear component pattern feature."""
		self._instance.SeedComponentArray = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the skipped components in this linear component pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the skipped components in this linear component pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def synchronize_flexible_components(self):
		"""Gets or sets whether to synchronize the movement of patterned flexible subassembly components with seed flexible subassembly components in this linear component pattern feature."""
		return self._instance.SynchronizeFlexibleComponents

	@synchronize_flexible_components.setter
	def synchronize_flexible_components(self, value):
		"""Gets or sets whether to synchronize the movement of patterned flexible subassembly components with seed flexible subassembly components in this linear component pattern feature."""
		self._instance.SynchronizeFlexibleComponents = value

	@property
	def access_selections(self):
		"""Gains access to selections that define this linear component pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections that define this linear component pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_d_axis_type(self):
		"""Gets the type of axis used for Direction 1 in this linear component pattern feature."""
		return self._instance.GetD1AxisType

	@get_d_axis_type.setter
	def get_d_axis_type(self, value):
		"""Gets the type of axis used for Direction 1 in this linear component pattern feature."""
		self._instance.GetD1AxisType = value

	@property
	def get_d_axis_type(self):
		"""Gets the type of axis used for Direction 2 in this linear component pattern feature."""
		return self._instance.GetD2AxisType

	@get_d_axis_type.setter
	def get_d_axis_type(self, value):
		"""Gets the type of axis used for Direction 2 in this linear component pattern feature."""
		self._instance.GetD2AxisType = value

	@property
	def get_modified_instance(self):
		"""Gets the modified values for the specified pattern instance in this linear component pattern feature."""
		return self._instance.GetModifiedInstance

	@get_modified_instance.setter
	def get_modified_instance(self, value):
		"""Gets the modified values for the specified pattern instance in this linear component pattern feature."""
		self._instance.GetModifiedInstance = value

	@property
	def get_modified_instances(self):
		"""Gets the instance numbers of all modified instances in this linear component pattern."""
		return self._instance.GetModifiedInstances

	@get_modified_instances.setter
	def get_modified_instances(self, value):
		"""Gets the instance numbers of all modified instances in this linear component pattern."""
		self._instance.GetModifiedInstances = value

	@property
	def get_seed_component_count(self):
		"""Gets the number of seed components in this linear component pattern feature."""
		return self._instance.GetSeedComponentCount

	@get_seed_component_count.setter
	def get_seed_component_count(self, value):
		"""Gets the number of seed components in this linear component pattern feature."""
		self._instance.GetSeedComponentCount = value

	@property
	def get_skipped_item_count(self):
		"""Gets the number of items that are skipped in this linear component pattern feature."""
		return self._instance.GetSkippedItemCount

	@get_skipped_item_count.setter
	def get_skipped_item_count(self, value):
		"""Gets the number of items that are skipped in this linear component pattern feature."""
		self._instance.GetSkippedItemCount = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified instance of this linear component pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified instance of this linear component pattern feature."""
		self._instance.GetTransform = value

	@property
	def i_access_selections(self):
		"""Allows you to gain access to the selections that describe this linear component pattern feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Allows you to gain access to the selections that describe this linear component pattern feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_seed_component_array(self):
		"""Gets an array of seed components for this linear component pattern feature."""
		return self._instance.IGetSeedComponentArray

	@i_get_seed_component_array.setter
	def i_get_seed_component_array(self, value):
		"""Gets an array of seed components for this linear component pattern feature."""
		self._instance.IGetSeedComponentArray = value

	@property
	def i_get_skipped_item_array(self):
		"""Gets the skipped components in this linear component pattern feature."""
		return self._instance.IGetSkippedItemArray

	@i_get_skipped_item_array.setter
	def i_get_skipped_item_array(self, value):
		"""Gets the skipped components in this linear component pattern feature."""
		self._instance.IGetSkippedItemArray = value

	@property
	def i_set_seed_component_array(self):
		"""Sets an array of seed component features to pattern for this linear component pattern feature."""
		return self._instance.ISetSeedComponentArray

	@i_set_seed_component_array.setter
	def i_set_seed_component_array(self, value):
		"""Sets an array of seed component features to pattern for this linear component pattern feature."""
		self._instance.ISetSeedComponentArray = value

	@property
	def i_set_skipped_item_array(self):
		"""Sets the skipped components in this linear component pattern feature."""
		return self._instance.ISetSkippedItemArray

	@i_set_skipped_item_array.setter
	def i_set_skipped_item_array(self, value):
		"""Sets the skipped components in this linear component pattern feature."""
		self._instance.ISetSkippedItemArray = value

	@property
	def modify_instance(self):
		"""Modifies the specified pattern instance with the specified distances in Directions 1 and 2 in this linear component pattern feature."""
		return self._instance.ModifyInstance

	@modify_instance.setter
	def modify_instance(self, value):
		"""Modifies the specified pattern instance with the specified distances in Directions 1 and 2 in this linear component pattern feature."""
		self._instance.ModifyInstance = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created this linear component pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created this linear component pattern feature."""
		self._instance.ReleaseSelectionAccess = value

