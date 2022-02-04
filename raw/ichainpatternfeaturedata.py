# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.html
class IChainPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def align_method(self):
		"""Gets or sets how to align this chain pattern feature."""
		return self._instance.AlignMethod

	@align_method.setter
	def align_method(self, value):
		"""Gets or sets how to align this chain pattern feature."""
		self._instance.AlignMethod = value

	@property
	def fill_path(self):
		"""Gets or sets whether the maximum number of pattern instances to fill the path is calculated by SOLIDWORKS for this chain pattern feature."""
		return self._instance.FillPath

	@fill_path.setter
	def fill_path(self, value):
		"""Gets or sets whether the maximum number of pattern instances to fill the path is calculated by SOLIDWORKS for this chain pattern feature."""
		self._instance.FillPath = value

	@property
	def force_use_seed_configuration(self):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this chain pattern feature."""
		return self._instance.ForceUseSeedConfiguration

	@force_use_seed_configuration.setter
	def force_use_seed_configuration(self, value):
		"""Gets or sets whether to synchronize the configuration of pattern components with the configuration of the seed component in this chain pattern feature."""
		self._instance.ForceUseSeedConfiguration = value

	@property
	def group_flip_plane(self):
		"""Gets or sets whether to flip the position plane for Chain Group 1 in this chain pattern feature."""
		return self._instance.Group1FlipPlane

	@group_flip_plane.setter
	def group_flip_plane(self, value):
		"""Gets or sets whether to flip the position plane for Chain Group 1 in this chain pattern feature."""
		self._instance.Group1FlipPlane = value

	@property
	def group_path_link(self):
		"""Gets or sets Path Link 1 in Chain Group 1 in this chain pattern feature."""
		return self._instance.Group1PathLink1

	@group_path_link.setter
	def group_path_link(self, value):
		"""Gets or sets Path Link 1 in Chain Group 1 in this chain pattern feature."""
		self._instance.Group1PathLink1 = value

	@property
	def group_path_link(self):
		"""Gets or sets Path Link 2 in Chain Group 1 in this chain pattern feature."""
		return self._instance.Group1PathLink2

	@group_path_link.setter
	def group_path_link(self, value):
		"""Gets or sets Path Link 2 in Chain Group 1 in this chain pattern feature."""
		self._instance.Group1PathLink2 = value

	@property
	def group_path_plane(self):
		"""Gets or sets the position of the pattern component relative to the path in Chain Group 1 in this chain pattern feature."""
		return self._instance.Group1PathPlane

	@group_path_plane.setter
	def group_path_plane(self, value):
		"""Gets or sets the position of the pattern component relative to the path in Chain Group 1 in this chain pattern feature."""
		self._instance.Group1PathPlane = value

	@property
	def group_pattern_component(self):
		"""Gets or sets the component to pattern for Chain Group 1 in this chain pattern feature."""
		return self._instance.Group1PatternComponent

	@group_pattern_component.setter
	def group_pattern_component(self, value):
		"""Gets or sets the component to pattern for Chain Group 1 in this chain pattern feature."""
		self._instance.Group1PatternComponent = value

	@property
	def group_flip_plane(self):
		"""Gets or sets whether to flip the position plane for Chain Group 2 in this chain pattern feature."""
		return self._instance.Group2FlipPlane

	@group_flip_plane.setter
	def group_flip_plane(self, value):
		"""Gets or sets whether to flip the position plane for Chain Group 2 in this chain pattern feature."""
		self._instance.Group2FlipPlane = value

	@property
	def group_path_link(self):
		"""Gets or sets Path Link 1 in Chain Group 2 in this chain pattern feature."""
		return self._instance.Group2PathLink1

	@group_path_link.setter
	def group_path_link(self, value):
		"""Gets or sets Path Link 1 in Chain Group 2 in this chain pattern feature."""
		self._instance.Group2PathLink1 = value

	@property
	def group_path_link(self):
		"""Gets or sets Path Link 2 in Chain Group 2 in this chain pattern feature."""
		return self._instance.Group2PathLink2

	@group_path_link.setter
	def group_path_link(self, value):
		"""Gets or sets Path Link 2 in Chain Group 2 in this chain pattern feature."""
		self._instance.Group2PathLink2 = value

	@property
	def group_path_plane(self):
		"""Gets or sets the position of the pattern component relative to the path in Chain Group 2 in this chain pattern feature."""
		return self._instance.Group2PathPlane

	@group_path_plane.setter
	def group_path_plane(self, value):
		"""Gets or sets the position of the pattern component relative to the path in Chain Group 2 in this chain pattern feature."""
		self._instance.Group2PathPlane = value

	@property
	def group_pattern_component(self):
		"""Gets or sets the component to pattern for Chain Group 2 in this chain pattern feature."""
		return self._instance.Group2PatternComponent

	@group_pattern_component.setter
	def group_pattern_component(self, value):
		"""Gets or sets the component to pattern for Chain Group 2 in this chain pattern feature."""
		self._instance.Group2PatternComponent = value

	@property
	def instance_count(self):
		"""Gets or sets the number of pattern instances in this chain pattern feature."""
		return self._instance.InstanceCount

	@instance_count.setter
	def instance_count(self, value):
		"""Gets or sets the number of pattern instances in this chain pattern feature."""
		self._instance.InstanceCount = value

	@property
	def options(self):
		"""Gets or sets whether to calculate the mates between each pattern instance or copy each pattern instance without creating mates in this chain pattern feature."""
		return self._instance.Options

	@options.setter
	def options(self, value):
		"""Gets or sets whether to calculate the mates between each pattern instance or copy each pattern instance without creating mates in this chain pattern feature."""
		self._instance.Options = value

	@property
	def path(self):
		"""Gets or sets the path for this chain pattern feature."""
		return self._instance.Path

	@path.setter
	def path(self, value):
		"""Gets or sets the path for this chain pattern feature."""
		self._instance.Path = value

	@property
	def path_plane_reference(self):
		"""Gets or sets the reference plane for the path selected for this chain pattern feature."""
		return self._instance.PathPlaneReference

	@path_plane_reference.setter
	def path_plane_reference(self, value):
		"""Gets or sets the reference plane for the path selected for this chain pattern feature."""
		self._instance.PathPlaneReference = value

	@property
	def pitch_method(self):
		"""Gets or sets the pitch method for this chain pattern feature."""
		return self._instance.PitchMethod

	@pitch_method.setter
	def pitch_method(self, value):
		"""Gets or sets the pitch method for this chain pattern feature."""
		self._instance.PitchMethod = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of the path in this chain pattern feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of the path in this chain pattern feature."""
		self._instance.ReverseDirection = value

	@property
	def spacing(self):
		"""Gets or sets the distance between the pattern instances in the path in this chain pattern feature."""
		return self._instance.Spacing

	@spacing.setter
	def spacing(self, value):
		"""Gets or sets the distance between the pattern instances in the path in this chain pattern feature."""
		self._instance.Spacing = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this chain pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this chain pattern feature."""
		self._instance.AccessSelections = value

	@property
	def clear_group_selections(self):
		"""Clears Chain Group 2 selections in this connected linkage chain pattern feature."""
		return self._instance.ClearGroup2Selections

	@clear_group_selections.setter
	def clear_group_selections(self, value):
		"""Clears Chain Group 2 selections in this connected linkage chain pattern feature."""
		self._instance.ClearGroup2Selections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this chain pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this chain pattern feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_equal_spacing(self):
		"""Sets equal spacing between each chain pattern instance in this chain pattern feature."""
		return self._instance.SetEqualSpacing

	@set_equal_spacing.setter
	def set_equal_spacing(self, value):
		"""Sets equal spacing between each chain pattern instance in this chain pattern feature."""
		self._instance.SetEqualSpacing = value

