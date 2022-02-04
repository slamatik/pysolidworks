# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalCircularPatternFeatureData_members.html
class ILocalCircularPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def axis(self):
		"""Gets or sets the circular axis for this circular component pattern feature."""
		return self._instance.Axis

	@axis.setter
	def axis(self, value):
		"""Gets or sets the circular axis for this circular component pattern feature."""
		self._instance.Axis = value

	@property
	def direction(self):
		"""Gets or sets whether to create a bidirectional circular component pattern feature."""
		return self._instance.Direction2

	@direction.setter
	def direction(self, value):
		"""Gets or sets whether to create a bidirectional circular component pattern feature."""
		self._instance.Direction2 = value

	@property
	def equal_spacing(self):
		"""Gets or sets whether to equally space the pattern instances in Direction 1 in this circular component pattern feature."""
		return self._instance.EqualSpacing

	@equal_spacing.setter
	def equal_spacing(self, value):
		"""Gets or sets whether to equally space the pattern instances in Direction 1 in this circular component pattern feature."""
		self._instance.EqualSpacing = value

	@property
	def equal_spacing(self):
		"""Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular component pattern feature."""
		return self._instance.EqualSpacing2

	@equal_spacing.setter
	def equal_spacing(self, value):
		"""Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular component pattern feature."""
		self._instance.EqualSpacing2 = value

	@property
	def force_use_seed_configuration(self):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local circular pattern feature."""
		return self._instance.ForceUseSeedConfiguration

	@force_use_seed_configuration.setter
	def force_use_seed_configuration(self, value):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local circular pattern feature."""
		self._instance.ForceUseSeedConfiguration = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether the direction axis for this local circular pattern is reversed for this circular component pattern feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether the direction axis for this local circular pattern is reversed for this circular component pattern feature."""
		self._instance.ReverseDirection = value

	@property
	def seed_component_array(self):
		"""Gets or sets an array of seed component features for this circular component pattern feature."""
		return self._instance.SeedComponentArray

	@seed_component_array.setter
	def seed_component_array(self, value):
		"""Gets or sets an array of seed component features for this circular component pattern feature."""
		self._instance.SeedComponentArray = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the skipped components in this circular component pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the skipped components in this circular component pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def spacing(self):
		"""Gets or sets the distance between pattern instances in Direction 1 for this circular component pattern feature."""
		return self._instance.Spacing

	@spacing.setter
	def spacing(self, value):
		"""Gets or sets the distance between pattern instances in Direction 1 for this circular component pattern feature."""
		self._instance.Spacing = value

	@property
	def spacing(self):
		"""Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular component pattern feature."""
		return self._instance.Spacing2

	@spacing.setter
	def spacing(self, value):
		"""Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular component pattern feature."""
		self._instance.Spacing2 = value

	@property
	def symmetric(self):
		"""Gets or sets whether Direction 2 properties are symmetric with those of Direction 1 of this bidirectional circular component pattern feature."""
		return self._instance.Symmetric

	@symmetric.setter
	def symmetric(self, value):
		"""Gets or sets whether Direction 2 properties are symmetric with those of Direction 1 of this bidirectional circular component pattern feature."""
		self._instance.Symmetric = value

	@property
	def synchronize_flexible_components(self):
		"""Gets or sets whether to synchronize the movement of flexible subassembly components in this circular component pattern feature."""
		return self._instance.SynchronizeFlexibleComponents

	@synchronize_flexible_components.setter
	def synchronize_flexible_components(self, value):
		"""Gets or sets whether to synchronize the movement of flexible subassembly components in this circular component pattern feature."""
		self._instance.SynchronizeFlexibleComponents = value

	@property
	def total_instances(self):
		"""Gets or sets the total number of instances in Direction 1 for this circular component pattern feature."""
		return self._instance.TotalInstances

	@total_instances.setter
	def total_instances(self, value):
		"""Gets or sets the total number of instances in Direction 1 for this circular component pattern feature."""
		self._instance.TotalInstances = value

	@property
	def total_instances(self):
		"""Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular component pattern feature."""
		return self._instance.TotalInstances2

	@total_instances.setter
	def total_instances(self, value):
		"""Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular component pattern feature."""
		self._instance.TotalInstances2 = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this circular component pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this circular component pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_axis_type(self):
		"""Gets whether the circular axis is a reference axis, edge, or dimension for this circular component pattern feature."""
		return self._instance.GetAxisType

	@get_axis_type.setter
	def get_axis_type(self, value):
		"""Gets whether the circular axis is a reference axis, edge, or dimension for this circular component pattern feature."""
		self._instance.GetAxisType = value

	@property
	def get_modified_instance(self):
		"""Gets the modified values for the specified pattern instance in this circular component pattern feature."""
		return self._instance.GetModifiedInstance

	@get_modified_instance.setter
	def get_modified_instance(self, value):
		"""Gets the modified values for the specified pattern instance in this circular component pattern feature."""
		self._instance.GetModifiedInstance = value

	@property
	def get_modified_instances(self):
		"""Gets the instance numbers of all modified instances in this circular component pattern."""
		return self._instance.GetModifiedInstances

	@get_modified_instances.setter
	def get_modified_instances(self, value):
		"""Gets the instance numbers of all modified instances in this circular component pattern."""
		self._instance.GetModifiedInstances = value

	@property
	def get_seed_component_count(self):
		"""Gets the number of seed component features for this circular component pattern feature."""
		return self._instance.GetSeedComponentCount

	@get_seed_component_count.setter
	def get_seed_component_count(self, value):
		"""Gets the number of seed component features for this circular component pattern feature."""
		self._instance.GetSeedComponentCount = value

	@property
	def get_skipped_item_count(self):
		"""Gets the number of skipped items for this circular component pattern feature."""
		return self._instance.GetSkippedItemCount

	@get_skipped_item_count.setter
	def get_skipped_item_count(self, value):
		"""Gets the number of skipped items for this circular component pattern feature."""
		self._instance.GetSkippedItemCount = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified instance of this circular component pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified instance of this circular component pattern feature."""
		self._instance.GetTransform = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this circular component pattern feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this circular component pattern feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_seed_component_array(self):
		"""Gets an array of seed component features for this circular component pattern feature."""
		return self._instance.IGetSeedComponentArray

	@i_get_seed_component_array.setter
	def i_get_seed_component_array(self, value):
		"""Gets an array of seed component features for this circular component pattern feature."""
		self._instance.IGetSeedComponentArray = value

	@property
	def i_get_skipped_item_array(self):
		"""Gets the list of skipped items in this circular component pattern feature."""
		return self._instance.IGetSkippedItemArray

	@i_get_skipped_item_array.setter
	def i_get_skipped_item_array(self, value):
		"""Gets the list of skipped items in this circular component pattern feature."""
		self._instance.IGetSkippedItemArray = value

	@property
	def i_set_seed_component_array(self):
		"""Sets an array of seed component features for this circular component pattern feature."""
		return self._instance.ISetSeedComponentArray

	@i_set_seed_component_array.setter
	def i_set_seed_component_array(self, value):
		"""Sets an array of seed component features for this circular component pattern feature."""
		self._instance.ISetSeedComponentArray = value

	@property
	def i_set_skipped_item_array(self):
		"""Sets the list of skipped items for this circular component pattern feature."""
		return self._instance.ISetSkippedItemArray

	@i_set_skipped_item_array.setter
	def i_set_skipped_item_array(self, value):
		"""Sets the list of skipped items for this circular component pattern feature."""
		self._instance.ISetSkippedItemArray = value

	@property
	def modify_instance(self):
		"""Modifies the specified pattern instance with the specified angle in this circular component pattern feature."""
		return self._instance.ModifyInstance

	@modify_instance.setter
	def modify_instance(self, value):
		"""Modifies the specified pattern instance with the specified angle in this circular component pattern feature."""
		self._instance.ModifyInstance = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this circular component pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this circular component pattern feature."""
		self._instance.ReleaseSelectionAccess = value

