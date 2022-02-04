# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData_members.html
class IDerivedPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def driving_feature_skipped_item_array(self):
		"""Gets the skipped instances in the driving feature of this derived pattern feature."""
		# return self._instance.DrivingFeatureSkippedItemArray
		raise NotImplemented

	@property
	def force_use_seed_configuration(self):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this derived pattern feature."""
		return self._instance.ForceUseSeedConfiguration

	@force_use_seed_configuration.setter
	def force_use_seed_configuration(self, value):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this derived pattern feature."""
		self._instance.ForceUseSeedConfiguration = value

	@property
	def pattern_feature(self):
		"""Gets or sets the pattern feature for this derived pattern feature."""
		return self._instance.PatternFeature

	@pattern_feature.setter
	def pattern_feature(self, value):
		"""Gets or sets the pattern feature for this derived pattern feature."""
		self._instance.PatternFeature = value

	@property
	def propagate_visual_property(self):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in this derived pattern feature."""
		return self._instance.PropagateVisualProperty

	@propagate_visual_property.setter
	def propagate_visual_property(self, value):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in this derived pattern feature."""
		self._instance.PropagateVisualProperty = value

	@property
	def seed_component_array(self):
		"""Gets or sets an array of seed component features for this derived pattern feature."""
		return self._instance.SeedComponentArray

	@seed_component_array.setter
	def seed_component_array(self, value):
		"""Gets or sets an array of seed component features for this derived pattern feature."""
		self._instance.SeedComponentArray = value

	@property
	def seed_position(self):
		"""Gets or sets which pattern instance to use as the seed feature for this derived pattern feature."""
		return self._instance.SeedPosition

	@seed_position.setter
	def seed_position(self, value):
		"""Gets or sets which pattern instance to use as the seed feature for this derived pattern feature."""
		self._instance.SeedPosition = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the list of skipped items for this derived pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the list of skipped items for this derived pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe this derived pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe this derived pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_seed_component_count(self):
		"""Gets the number of seed component features for this derived pattern feature."""
		return self._instance.GetSeedComponentCount

	@get_seed_component_count.setter
	def get_seed_component_count(self, value):
		"""Gets the number of seed component features for this derived pattern feature."""
		self._instance.GetSeedComponentCount = value

	@property
	def get_skipped_item_count(self):
		"""Gets the number of skipped items for this derived pattern feature."""
		return self._instance.GetSkippedItemCount

	@get_skipped_item_count.setter
	def get_skipped_item_count(self, value):
		"""Gets the number of skipped items for this derived pattern feature."""
		self._instance.GetSkippedItemCount = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified instance of this derived-pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified instance of this derived-pattern feature."""
		self._instance.GetTransform = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that describe this derived pattern feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that describe this derived pattern feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_seed_component_array(self):
		"""Gets the seed component features for this derived pattern feature."""
		return self._instance.IGetSeedComponentArray

	@i_get_seed_component_array.setter
	def i_get_seed_component_array(self, value):
		"""Gets the seed component features for this derived pattern feature."""
		self._instance.IGetSeedComponentArray = value

	@property
	def i_get_skipped_item_array(self):
		"""Gets the list of skipped items for this derived pattern feature."""
		return self._instance.IGetSkippedItemArray

	@i_get_skipped_item_array.setter
	def i_get_skipped_item_array(self, value):
		"""Gets the list of skipped items for this derived pattern feature."""
		self._instance.IGetSkippedItemArray = value

	@property
	def i_set_seed_component_array(self):
		"""Sets an array of the seed component features for this derived pattern feature."""
		return self._instance.ISetSeedComponentArray

	@i_set_seed_component_array.setter
	def i_set_seed_component_array(self, value):
		"""Sets an array of the seed component features for this derived pattern feature."""
		self._instance.ISetSeedComponentArray = value

	@property
	def i_set_skipped_item_array(self):
		"""Sets the list of items to skip for this derived pattern feature."""
		return self._instance.ISetSkippedItemArray

	@i_set_skipped_item_array.setter
	def i_set_skipped_item_array(self, value):
		"""Sets the list of items to skip for this derived pattern feature."""
		self._instance.ISetSkippedItemArray = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that describe this derived pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that describe this derived pattern feature."""
		self._instance.ReleaseSelectionAccess = value

