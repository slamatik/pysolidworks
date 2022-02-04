# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalSketchPatternFeatureData_members.html
class ILocalSketchPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def force_use_seed_configuration(self):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local sketch pattern feature."""
		return self._instance.ForceUseSeedConfiguration

	@force_use_seed_configuration.setter
	def force_use_seed_configuration(self, value):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this local sketch pattern feature."""
		self._instance.ForceUseSeedConfiguration = value

	@property
	def pattern_component_array(self):
		"""Gets or sets the components to pattern for this sketch-driven component pattern feature."""
		return self._instance.PatternComponentArray

	@pattern_component_array.setter
	def pattern_component_array(self, value):
		"""Gets or sets the components to pattern for this sketch-driven component pattern feature."""
		self._instance.PatternComponentArray = value

	@property
	def reference_point(self):
		"""Gets or sets the type of reference point for this sketch-driven component pattern feature."""
		return self._instance.ReferencePoint

	@reference_point.setter
	def reference_point(self, value):
		"""Gets or sets the type of reference point for this sketch-driven component pattern feature."""
		self._instance.ReferencePoint = value

	@property
	def selected_point(self):
		"""Gets or sets the selected point for this sketch-driven component pattern feature."""
		return self._instance.SelectedPoint

	@selected_point.setter
	def selected_point(self, value):
		"""Gets or sets the selected point for this sketch-driven component pattern feature."""
		self._instance.SelectedPoint = value

	@property
	def sketch(self):
		"""Gets or sets the sketch for this sketch-driven component pattern feature."""
		return self._instance.Sketch

	@sketch.setter
	def sketch(self, value):
		"""Gets or sets the sketch for this sketch-driven component pattern feature."""
		self._instance.Sketch = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the array of skipped components in this sketch-driven component pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the array of skipped components in this sketch-driven component pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define this sketch-driven component pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define this sketch-driven component pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_base_point(self):
		"""Gets the data for the base point from which this sketch-driven component pattern feature is created."""
		return self._instance.GetBasePoint

	@get_base_point.setter
	def get_base_point(self, value):
		"""Gets the data for the base point from which this sketch-driven component pattern feature is created."""
		self._instance.GetBasePoint = value

	@property
	def get_pattern_component_count(self):
		"""Gets the number of components in this sketch-driven component pattern feature."""
		return self._instance.GetPatternComponentCount

	@get_pattern_component_count.setter
	def get_pattern_component_count(self, value):
		"""Gets the number of components in this sketch-driven component pattern feature."""
		self._instance.GetPatternComponentCount = value

	@property
	def get_reference_point_type(self):
		"""Gets the type of reference point of this sketch-driven component pattern feature."""
		return self._instance.GetReferencePointType

	@get_reference_point_type.setter
	def get_reference_point_type(self, value):
		"""Gets the type of reference point of this sketch-driven component pattern feature."""
		self._instance.GetReferencePointType = value

	@property
	def get_skipped_item_count(self):
		"""Gets the number of components skipped in this sketch-driven component pattern feature."""
		return self._instance.GetSkippedItemCount

	@get_skipped_item_count.setter
	def get_skipped_item_count(self, value):
		"""Gets the number of components skipped in this sketch-driven component pattern feature."""
		self._instance.GetSkippedItemCount = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified instance in this sketch-driven component pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified instance in this sketch-driven component pattern feature."""
		self._instance.GetTransform = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this sketch-driven component pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this sketch-driven component pattern feature."""
		self._instance.ReleaseSelectionAccess = value

