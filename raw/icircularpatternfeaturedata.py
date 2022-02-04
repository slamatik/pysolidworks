# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData_members.html
class ICircularPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def auto_select(self):
		"""Gets whether to automatically select all bodies in a multibody part intersected by this circular pattern feature."""
		# return self._instance.AutoSelect
		raise NotImplemented

	@property
	def axis(self):
		"""Gets or sets the entity used to determine the direction of this circular pattern feature."""
		return self._instance.Axis

	@axis.setter
	def axis(self, value):
		"""Gets or sets the entity used to determine the direction of this circular pattern feature."""
		self._instance.Axis = value

	@property
	def body_pattern(self):
		"""Gets or sets whether to base this circular pattern feature on bodies or features and faces."""
		return self._instance.BodyPattern

	@body_pattern.setter
	def body_pattern(self, value):
		"""Gets or sets whether to base this circular pattern feature on bodies or features and faces."""
		self._instance.BodyPattern = value

	@property
	def direction(self):
		"""Gets or sets whether to create a bidirectional circular pattern feature."""
		return self._instance.Direction2

	@direction.setter
	def direction(self, value):
		"""Gets or sets whether to create a bidirectional circular pattern feature."""
		self._instance.Direction2 = value

	@property
	def equal_spacing(self):
		"""Gets or sets whether the pattern instances in Direction 1 are equally spaced in this circular pattern feature."""
		return self._instance.EqualSpacing

	@equal_spacing.setter
	def equal_spacing(self, value):
		"""Gets or sets whether the pattern instances in Direction 1 are equally spaced in this circular pattern feature."""
		self._instance.EqualSpacing = value

	@property
	def equal_spacing(self):
		"""Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular pattern feature."""
		return self._instance.EqualSpacing2

	@equal_spacing.setter
	def equal_spacing(self, value):
		"""Gets or sets whether the pattern instances in Direction 2 are equally spaced in this bidirectional circular pattern feature."""
		self._instance.EqualSpacing2 = value

	@property
	def feature_scope(self):
		"""Gets which bodies in this multibody part are affected by this circular pattern feature."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets which bodies in this multibody part are affected by this circular pattern feature."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets the bodies in this multibody part that are affected by this circular pattern feature."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets the bodies in this multibody part that are affected by this circular pattern feature."""
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
		"""Gets or sets whether to vary the spacing of pattern instances in this circular pattern feature."""
		return self._instance.InstancesToVary

	@instances_to_vary.setter
	def instances_to_vary(self, value):
		"""Gets or sets whether to vary the spacing of pattern instances in this circular pattern feature."""
		self._instance.InstancesToVary = value

	@property
	def pattern_body_array(self):
		"""Gets or sets a list of bodies to pattern in a multibody part for this circular pattern feature."""
		return self._instance.PatternBodyArray

	@pattern_body_array.setter
	def pattern_body_array(self, value):
		"""Gets or sets a list of bodies to pattern in a multibody part for this circular pattern feature."""
		self._instance.PatternBodyArray = value

	@property
	def pattern_element(self):
		"""Gets or sets the type of entities on which to base this circular pattern feature."""
		return self._instance.PatternElement

	@pattern_element.setter
	def pattern_element(self, value):
		"""Gets or sets the type of entities on which to base this circular pattern feature."""
		self._instance.PatternElement = value

	@property
	def pattern_face_array(self):
		"""Gets or sets the list of faces to pattern for this circular pattern feature."""
		return self._instance.PatternFaceArray

	@pattern_face_array.setter
	def pattern_face_array(self, value):
		"""Gets or sets the list of faces to pattern for this circular pattern feature."""
		self._instance.PatternFaceArray = value

	@property
	def pattern_feature_array(self):
		"""Gets or sets the seed features for the circular pattern feature."""
		return self._instance.PatternFeatureArray

	@pattern_feature_array.setter
	def pattern_feature_array(self, value):
		"""Gets or sets the seed features for the circular pattern feature."""
		self._instance.PatternFeatureArray = value

	@property
	def propagate_visual_property(self):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, cosmetic thread data, etc.) to all pattern instances in this circular pattern feature."""
		return self._instance.PropagateVisualProperty

	@propagate_visual_property.setter
	def propagate_visual_property(self, value):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, cosmetic thread data, etc.) to all pattern instances in this circular pattern feature."""
		self._instance.PropagateVisualProperty = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether the direction of the axis should be reversed in this circular pattern feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether the direction of the axis should be reversed in this circular pattern feature."""
		self._instance.ReverseDirection = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the list of items to skip in this circular pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the list of items to skip in this circular pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def spacing(self):
		"""Gets or sets the spacing between pattern instances in Direction 1 of the circular pattern feature."""
		return self._instance.Spacing

	@spacing.setter
	def spacing(self, value):
		"""Gets or sets the spacing between pattern instances in Direction 1 of the circular pattern feature."""
		self._instance.Spacing = value

	@property
	def spacing(self):
		"""Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular pattern feature."""
		return self._instance.Spacing2

	@spacing.setter
	def spacing(self, value):
		"""Gets or sets the spacing between pattern instances in Direction 2 of this bidirectional circular pattern feature."""
		self._instance.Spacing2 = value

	@property
	def symmetric(self):
		"""Gets or sets whether to create a symmetric or asymmetric circular pattern feature in Direction 2."""
		return self._instance.Symmetric

	@symmetric.setter
	def symmetric(self, value):
		"""Gets or sets whether to create a symmetric or asymmetric circular pattern feature in Direction 2."""
		self._instance.Symmetric = value

	@property
	def total_instances(self):
		"""Gets or sets the total number of pattern instances in Direction 1 of this circular pattern feature."""
		return self._instance.TotalInstances

	@total_instances.setter
	def total_instances(self, value):
		"""Gets or sets the total number of pattern instances in Direction 1 of this circular pattern feature."""
		self._instance.TotalInstances = value

	@property
	def total_instances(self):
		"""Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular pattern feature."""
		return self._instance.TotalInstances2

	@total_instances.setter
	def total_instances(self, value):
		"""Gets or sets the total number of pattern instances in Direction 2 of this bidirectional circular pattern feature."""
		self._instance.TotalInstances2 = value

	@property
	def vary_sketch(self):
		"""Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to the base part in this circular pattern."""
		return self._instance.VarySketch

	@vary_sketch.setter
	def vary_sketch(self, value):
		"""Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to the base part in this circular pattern."""
		self._instance.VarySketch = value

	@property
	def access_selections(self):
		"""Gains access to selections used to define a circular pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections used to define a circular pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_axis_type(self):
		"""Gets the type of geometry used to determine the direction of this circular pattern."""
		return self._instance.GetAxisType

	@get_axis_type.setter
	def get_axis_type(self, value):
		"""Gets the type of geometry used to determine the direction of this circular pattern."""
		self._instance.GetAxisType = value

	@property
	def get_instance_to_vary_options(self):
		"""Gets the options for varying the spacing of pattern instances in this circular pattern feature."""
		return self._instance.GetInstanceToVaryOptions

	@get_instance_to_vary_options.setter
	def get_instance_to_vary_options(self, value):
		"""Gets the options for varying the spacing of pattern instances in this circular pattern feature."""
		self._instance.GetInstanceToVaryOptions = value

	@property
	def get_pattern_body_count(self):
		"""Gets the number of seed bodies in this circular pattern feature."""
		return self._instance.GetPatternBodyCount

	@get_pattern_body_count.setter
	def get_pattern_body_count(self, value):
		"""Gets the number of seed bodies in this circular pattern feature."""
		self._instance.GetPatternBodyCount = value

	@property
	def get_pattern_face_count(self):
		"""Gets the number of patterned faces."""
		return self._instance.GetPatternFaceCount

	@get_pattern_face_count.setter
	def get_pattern_face_count(self, value):
		"""Gets the number of patterned faces."""
		self._instance.GetPatternFaceCount = value

	@property
	def get_pattern_feature_count(self):
		"""Gets the number of seed features used to create this circular pattern."""
		return self._instance.GetPatternFeatureCount

	@get_pattern_feature_count.setter
	def get_pattern_feature_count(self, value):
		"""Gets the number of seed features used to create this circular pattern."""
		self._instance.GetPatternFeatureCount = value

	@property
	def get_skipped_item_count(self):
		"""Gets the number of items skipped in this circular pattern."""
		return self._instance.GetSkippedItemCount

	@get_skipped_item_count.setter
	def get_skipped_item_count(self, value):
		"""Gets the number of items skipped in this circular pattern."""
		self._instance.GetSkippedItemCount = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified instance of this circular-pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified instance of this circular-pattern feature."""
		self._instance.GetTransform = value

	@property
	def i_access_selections(self):
		"""Gains access to selections used to define a circular pattern feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to selections used to define a circular pattern feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_pattern_body_array(self):
		"""Gets a list of the seed bodies for this circular pattern."""
		return self._instance.IGetPatternBodyArray

	@i_get_pattern_body_array.setter
	def i_get_pattern_body_array(self, value):
		"""Gets a list of the seed bodies for this circular pattern."""
		self._instance.IGetPatternBodyArray = value

	@property
	def i_get_pattern_face_array(self):
		"""Gets a list of patterned faces for this circular pattern."""
		return self._instance.IGetPatternFaceArray

	@i_get_pattern_face_array.setter
	def i_get_pattern_face_array(self, value):
		"""Gets a list of patterned faces for this circular pattern."""
		self._instance.IGetPatternFaceArray = value

	@property
	def i_get_pattern_feature_array(self):
		"""Gets the seed features for this circular pattern."""
		return self._instance.IGetPatternFeatureArray

	@i_get_pattern_feature_array.setter
	def i_get_pattern_feature_array(self, value):
		"""Gets the seed features for this circular pattern."""
		self._instance.IGetPatternFeatureArray = value

	@property
	def i_get_skipped_item_array(self):
		"""Gets an array of integers that represent the skipped items in this circular feature."""
		return self._instance.IGetSkippedItemArray

	@i_get_skipped_item_array.setter
	def i_get_skipped_item_array(self, value):
		"""Gets an array of integers that represent the skipped items in this circular feature."""
		self._instance.IGetSkippedItemArray = value

	@property
	def i_set_pattern_body_array(self):
		"""Sets a list of seed bodies for the circular pattern."""
		return self._instance.ISetPatternBodyArray

	@i_set_pattern_body_array.setter
	def i_set_pattern_body_array(self, value):
		"""Sets a list of seed bodies for the circular pattern."""
		self._instance.ISetPatternBodyArray = value

	@property
	def i_set_pattern_face_array(self):
		"""Sets a list of patterned faces for this circular pattern."""
		return self._instance.ISetPatternFaceArray

	@i_set_pattern_face_array.setter
	def i_set_pattern_face_array(self, value):
		"""Sets a list of patterned faces for this circular pattern."""
		self._instance.ISetPatternFaceArray = value

	@property
	def i_set_pattern_feature_array(self):
		"""Sets the seed features to use to create the circular pattern."""
		return self._instance.ISetPatternFeatureArray

	@i_set_pattern_feature_array.setter
	def i_set_pattern_feature_array(self, value):
		"""Sets the seed features to use to create the circular pattern."""
		self._instance.ISetPatternFeatureArray = value

	@property
	def i_set_skipped_item_array(self):
		"""Sets the list of skipped items in this circular pattern."""
		return self._instance.ISetSkippedItemArray

	@i_set_skipped_item_array.setter
	def i_set_skipped_item_array(self, value):
		"""Sets the list of skipped items in this circular pattern."""
		self._instance.ISetSkippedItemArray = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this circular pattern."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this circular pattern."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_feature_scope(self):
		"""Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this circular pattern feature."""
		return self._instance.SetFeatureScope

	@set_feature_scope.setter
	def set_feature_scope(self, value):
		"""Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this circular pattern feature."""
		self._instance.SetFeatureScope = value

	@property
	def set_instance_to_vary_options(self):
		"""Sets the options for varying the spacing of pattern instances in this circular pattern feature."""
		return self._instance.SetInstanceToVaryOptions

	@set_instance_to_vary_options.setter
	def set_instance_to_vary_options(self, value):
		"""Sets the options for varying the spacing of pattern instances in this circular pattern feature."""
		self._instance.SetInstanceToVaryOptions = value

