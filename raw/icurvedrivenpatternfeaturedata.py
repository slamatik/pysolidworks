# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.html
class ICurveDrivenPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def auto_select(self):
		"""Gets whether to automatically select all bodies in a multibody part intersected by this curve-driven pattern feature."""
		# return self._instance.AutoSelect
		raise NotImplemented

	@property
	def body_pattern(self):
		"""Gets or sets whether to base this curve-driven pattern feature on bodies or features and faces."""
		return self._instance.BodyPattern

	@body_pattern.setter
	def body_pattern(self, value):
		"""Gets or sets whether to base this curve-driven pattern feature on bodies or features and faces."""
		self._instance.BodyPattern = value

	@property
	def d_alignment_method(self):
		"""Gets or sets the alignment method for this curve-driven pattern feature in Direction 1."""
		return self._instance.D1AlignmentMethod

	@d_alignment_method.setter
	def d_alignment_method(self, value):
		"""Gets or sets the alignment method for this curve-driven pattern feature in Direction 1."""
		self._instance.D1AlignmentMethod = value

	@property
	def d_curve_method(self):
		"""Gets or sets the curve method for this curve-driven pattern feature in Direction 1."""
		return self._instance.D1CurveMethod

	@d_curve_method.setter
	def d_curve_method(self, value):
		"""Gets or sets the curve method for this curve-driven pattern feature in Direction 1."""
		self._instance.D1CurveMethod = value

	@property
	def d_direction(self):
		"""Gets or sets Direction 1 of this curve-driven pattern feature."""
		return self._instance.D1Direction

	@d_direction.setter
	def d_direction(self, value):
		"""Gets or sets Direction 1 of this curve-driven pattern feature."""
		self._instance.D1Direction = value

	@property
	def d_face_normal(self):
		"""Gets or sets the face on which the 3D curve lies in Direction 1 of this curve driven pattern."""
		return self._instance.D1FaceNormal

	@d_face_normal.setter
	def d_face_normal(self, value):
		"""Gets or sets the face on which the 3D curve lies in Direction 1 of this curve driven pattern."""
		self._instance.D1FaceNormal = value

	@property
	def d_instance_count(self):
		"""Gets or sets the number of instances in this curve-driven pattern in Direction 1."""
		return self._instance.D1InstanceCount

	@d_instance_count.setter
	def d_instance_count(self, value):
		"""Gets or sets the number of instances in this curve-driven pattern in Direction 1."""
		self._instance.D1InstanceCount = value

	@property
	def d_is_equal_spaced(self):
		"""Gets or sets whether the pattern items are equally spaced in Direction 1."""
		return self._instance.D1IsEqualSpaced

	@d_is_equal_spaced.setter
	def d_is_equal_spaced(self, value):
		"""Gets or sets whether the pattern items are equally spaced in Direction 1."""
		self._instance.D1IsEqualSpaced = value

	@property
	def d_reverse_direction(self):
		"""Gets or sets whether the pattern direction is reversed in Direction 1."""
		return self._instance.D1ReverseDirection

	@d_reverse_direction.setter
	def d_reverse_direction(self, value):
		"""Gets or sets whether the pattern direction is reversed in Direction 1."""
		self._instance.D1ReverseDirection = value

	@property
	def d_spacing(self):
		"""Gets or sets the spacing for this curve-driven pattern in Direction 1."""
		return self._instance.D1Spacing

	@d_spacing.setter
	def d_spacing(self, value):
		"""Gets or sets the spacing for this curve-driven pattern in Direction 1."""
		self._instance.D1Spacing = value

	@property
	def d_direction(self):
		"""Gets or sets Direction 2 of this bidirectional curve-driven pattern feature."""
		return self._instance.D2Direction

	@d_direction.setter
	def d_direction(self, value):
		"""Gets or sets Direction 2 of this bidirectional curve-driven pattern feature."""
		self._instance.D2Direction = value

	@property
	def d_instance_count(self):
		"""Gets or sets the number of instances in Direction 2 of this bidirectional curve-driven pattern feature."""
		return self._instance.D2InstanceCount

	@d_instance_count.setter
	def d_instance_count(self, value):
		"""Gets or sets the number of instances in Direction 2 of this bidirectional curve-driven pattern feature."""
		self._instance.D2InstanceCount = value

	@property
	def d_is_equal_spaced(self):
		"""Gets or sets whether the pattern items are equally spaced in Direction 2 of this bidirectional curve-driven pattern feature."""
		return self._instance.D2IsEqualSpaced

	@d_is_equal_spaced.setter
	def d_is_equal_spaced(self, value):
		"""Gets or sets whether the pattern items are equally spaced in Direction 2 of this bidirectional curve-driven pattern feature."""
		self._instance.D2IsEqualSpaced = value

	@property
	def d_pattern_seed_only(self):
		"""Gets or sets whether to replicate the seed pattern only in Direction 2, without replicating the curve pattern created under Direction 1."""
		return self._instance.D2PatternSeedOnly

	@d_pattern_seed_only.setter
	def d_pattern_seed_only(self, value):
		"""Gets or sets whether to replicate the seed pattern only in Direction 2, without replicating the curve pattern created under Direction 1."""
		self._instance.D2PatternSeedOnly = value

	@property
	def d_reverse_direction(self):
		"""Gets or sets whether to reverse Direction 2 for this bidirectional curve-driven pattern feature."""
		return self._instance.D2ReverseDirection

	@d_reverse_direction.setter
	def d_reverse_direction(self, value):
		"""Gets or sets whether to reverse Direction 2 for this bidirectional curve-driven pattern feature."""
		self._instance.D2ReverseDirection = value

	@property
	def d_spacing(self):
		"""Gets or sets the spacing of pattern instances in Direction 2 for this bidirectional curve-driven pattern feature."""
		return self._instance.D2Spacing

	@d_spacing.setter
	def d_spacing(self, value):
		"""Gets or sets the spacing of pattern instances in Direction 2 for this bidirectional curve-driven pattern feature."""
		self._instance.D2Spacing = value

	@property
	def dir_specified(self):
		"""Gets or sets whether Direction 2 is specified for this curve-driven pattern feature."""
		return self._instance.Dir2Specified

	@dir_specified.setter
	def dir_specified(self, value):
		"""Gets or sets whether Direction 2 is specified for this curve-driven pattern feature."""
		self._instance.Dir2Specified = value

	@property
	def feature_scope(self):
		"""Gets which bodies in this multibody part are affected by this curve-driven pattern feature."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets which bodies in this multibody part are affected by this curve-driven pattern feature."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets the bodies in this multibody part that are affected by this curve-driven pattern feature."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets the bodies in this multibody part that are affected by this curve-driven pattern feature."""
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
	def pattern_body_array(self):
		"""Gets or sets a list of the bodies to pattern for this curve-driven pattern."""
		return self._instance.PatternBodyArray

	@pattern_body_array.setter
	def pattern_body_array(self, value):
		"""Gets or sets a list of the bodies to pattern for this curve-driven pattern."""
		self._instance.PatternBodyArray = value

	@property
	def pattern_element(self):
		"""Gets or sets the type of entities to base this curve-driven pattern feature."""
		return self._instance.PatternElement

	@pattern_element.setter
	def pattern_element(self, value):
		"""Gets or sets the type of entities to base this curve-driven pattern feature."""
		self._instance.PatternElement = value

	@property
	def pattern_face_array(self):
		"""Gets or sets the list of faces to include in this curve-driven pattern feature."""
		return self._instance.PatternFaceArray

	@pattern_face_array.setter
	def pattern_face_array(self, value):
		"""Gets or sets the list of faces to include in this curve-driven pattern feature."""
		self._instance.PatternFaceArray = value

	@property
	def pattern_feature_array(self):
		"""Gets or sets the list of features to include in this curve-driven feature pattern."""
		return self._instance.PatternFeatureArray

	@pattern_feature_array.setter
	def pattern_feature_array(self, value):
		"""Gets or sets the list of features to include in this curve-driven feature pattern."""
		self._instance.PatternFeatureArray = value

	@property
	def propagate_visual_property(self):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all curve-driven pattern instances."""
		return self._instance.PropagateVisualProperty

	@propagate_visual_property.setter
	def propagate_visual_property(self, value):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all curve-driven pattern instances."""
		self._instance.PropagateVisualProperty = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the skipped items for this curve-driven pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the skipped items for this curve-driven pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def vary_sketch(self):
		"""Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to enclosing geometry in this curve-driven pattern feature."""
		return self._instance.VarySketch

	@vary_sketch.setter
	def vary_sketch(self, value):
		"""Gets or sets whether to allow pattern instances of a seed sketch to vary in relation to enclosing geometry in this curve-driven pattern feature."""
		self._instance.VarySketch = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this curve-driven pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this curve-driven pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_pattern_body_count(self):
		"""Gets the number of seed bodies in this curve-driven pattern feature."""
		return self._instance.GetPatternBodyCount

	@get_pattern_body_count.setter
	def get_pattern_body_count(self, value):
		"""Gets the number of seed bodies in this curve-driven pattern feature."""
		self._instance.GetPatternBodyCount = value

	@property
	def get_pattern_face_count(self):
		"""Gets a list of pattern faces for this curve-driven pattern feature."""
		return self._instance.GetPatternFaceCount

	@get_pattern_face_count.setter
	def get_pattern_face_count(self, value):
		"""Gets a list of pattern faces for this curve-driven pattern feature."""
		self._instance.GetPatternFaceCount = value

	@property
	def get_pattern_feature_count(self):
		"""Gets the number of seed features for this curve-driven pattern feature."""
		return self._instance.GetPatternFeatureCount

	@get_pattern_feature_count.setter
	def get_pattern_feature_count(self, value):
		"""Gets the number of seed features for this curve-driven pattern feature."""
		self._instance.GetPatternFeatureCount = value

	@property
	def get_skipped_item_count(self):
		"""Gets the number of skipped items for this curve-driven pattern feature."""
		return self._instance.GetSkippedItemCount

	@get_skipped_item_count.setter
	def get_skipped_item_count(self, value):
		"""Gets the number of skipped items for this curve-driven pattern feature."""
		self._instance.GetSkippedItemCount = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified instance of this curve-driven pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified instance of this curve-driven pattern feature."""
		self._instance.GetTransform = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this curve-driven pattern feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this curve-driven pattern feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_pattern_body_array(self):
		"""Gets a list of the seed bodies for this curve-driven pattern feature."""
		return self._instance.IGetPatternBodyArray

	@i_get_pattern_body_array.setter
	def i_get_pattern_body_array(self, value):
		"""Gets a list of the seed bodies for this curve-driven pattern feature."""
		self._instance.IGetPatternBodyArray = value

	@property
	def i_get_pattern_face_array(self):
		"""Gets a list of pattern faces for this curve-driven pattern feature."""
		return self._instance.IGetPatternFaceArray

	@i_get_pattern_face_array.setter
	def i_get_pattern_face_array(self, value):
		"""Gets a list of pattern faces for this curve-driven pattern feature."""
		self._instance.IGetPatternFaceArray = value

	@property
	def i_get_pattern_feature_array(self):
		"""Gets a list of pattern features in this curve-driven pattern feature."""
		return self._instance.IGetPatternFeatureArray

	@i_get_pattern_feature_array.setter
	def i_get_pattern_feature_array(self, value):
		"""Gets a list of pattern features in this curve-driven pattern feature."""
		self._instance.IGetPatternFeatureArray = value

	@property
	def i_get_skipped_item_array(self):
		"""Gets the array of integers representing the skipped items for this curve-driven pattern feature."""
		return self._instance.IGetSkippedItemArray

	@i_get_skipped_item_array.setter
	def i_get_skipped_item_array(self, value):
		"""Gets the array of integers representing the skipped items for this curve-driven pattern feature."""
		self._instance.IGetSkippedItemArray = value

	@property
	def i_set_pattern_body_array(self):
		"""Sets the list of seed bodies for this curve-driven pattern feature."""
		return self._instance.ISetPatternBodyArray

	@i_set_pattern_body_array.setter
	def i_set_pattern_body_array(self, value):
		"""Sets the list of seed bodies for this curve-driven pattern feature."""
		self._instance.ISetPatternBodyArray = value

	@property
	def i_set_pattern_face_array(self):
		"""Sets a list of pattern faces for this curve-driven pattern feature."""
		return self._instance.ISetPatternFaceArray

	@i_set_pattern_face_array.setter
	def i_set_pattern_face_array(self, value):
		"""Sets a list of pattern faces for this curve-driven pattern feature."""
		self._instance.ISetPatternFaceArray = value

	@property
	def i_set_pattern_feature_array(self):
		"""Sets the list of pattern features for this curve-driven pattern feature."""
		return self._instance.ISetPatternFeatureArray

	@i_set_pattern_feature_array.setter
	def i_set_pattern_feature_array(self, value):
		"""Sets the list of pattern features for this curve-driven pattern feature."""
		self._instance.ISetPatternFeatureArray = value

	@property
	def i_set_skipped_item_array(self):
		"""Sets the list of skipped items for this curve-driven pattern feature."""
		return self._instance.ISetSkippedItemArray

	@i_set_skipped_item_array.setter
	def i_set_skipped_item_array(self, value):
		"""Sets the list of skipped items for this curve-driven pattern feature."""
		self._instance.ISetSkippedItemArray = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this curve-driven pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this curve-driven pattern feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_feature_scope(self):
		"""Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this curve-driven pattern feature."""
		return self._instance.SetFeatureScope

	@set_feature_scope.setter
	def set_feature_scope(self, value):
		"""Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this curve-driven pattern feature."""
		self._instance.SetFeatureScope = value

