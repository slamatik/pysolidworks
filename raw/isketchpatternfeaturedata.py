# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.html
class ISketchPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def auto_select(self):
		"""Gets whether to automatically select all bodies in a multibody part intersected by this sketch-driven pattern feature."""
		# return self._instance.AutoSelect
		raise NotImplemented

	@property
	def body_pattern(self):
		"""Gets or sets whether to base this sketch pattern feature on bodies or features and faces."""
		return self._instance.BodyPattern

	@body_pattern.setter
	def body_pattern(self, value):
		"""Gets or sets whether to base this sketch pattern feature on bodies or features and faces."""
		self._instance.BodyPattern = value

	@property
	def feature_scope(self):
		"""Gets which bodies in this multibody part are affected by this sketch-driven pattern feature."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets which bodies in this multibody part are affected by this sketch-driven pattern feature."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets the bodies in this multibody part to be affected by this sketch-driven pattern feature."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets the bodies in this multibody part to be affected by this sketch-driven pattern feature."""
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
		"""Gets and sets the bodies to pattern for this sketch pattern feature."""
		return self._instance.PatternBodyArray

	@pattern_body_array.setter
	def pattern_body_array(self, value):
		"""Gets and sets the bodies to pattern for this sketch pattern feature."""
		self._instance.PatternBodyArray = value

	@property
	def pattern_element(self):
		"""Gets or sets the type of entities to base this sketch pattern feature."""
		return self._instance.PatternElement

	@pattern_element.setter
	def pattern_element(self, value):
		"""Gets or sets the type of entities to base this sketch pattern feature."""
		self._instance.PatternElement = value

	@property
	def pattern_face_array(self):
		"""Gets or sets the patterned faces for the sketch pattern feature."""
		return self._instance.PatternFaceArray

	@pattern_face_array.setter
	def pattern_face_array(self, value):
		"""Gets or sets the patterned faces for the sketch pattern feature."""
		self._instance.PatternFaceArray = value

	@property
	def pattern_feature_array(self):
		"""Gets or sets the seed features for the sketch pattern feature."""
		return self._instance.PatternFeatureArray

	@pattern_feature_array.setter
	def pattern_feature_array(self, value):
		"""Gets or sets the seed features for the sketch pattern feature."""
		self._instance.PatternFeatureArray = value

	@property
	def propagate_visual_property(self):
		"""Gets or sets whether to propagate visual properties (i.e., colors to all pattern instances)."""
		return self._instance.PropagateVisualProperty

	@propagate_visual_property.setter
	def propagate_visual_property(self, value):
		"""Gets or sets whether to propagate visual properties (i.e., colors to all pattern instances)."""
		self._instance.PropagateVisualProperty = value

	@property
	def reference_point(self):
		"""Gets or sets the reference point for this sketch pattern feature."""
		return self._instance.ReferencePoint

	@reference_point.setter
	def reference_point(self, value):
		"""Gets or sets the reference point for this sketch pattern feature."""
		self._instance.ReferencePoint = value

	@property
	def sketch(self):
		"""Gets or sets the sketch from which that this sketch pattern feature is created."""
		return self._instance.Sketch

	@sketch.setter
	def sketch(self, value):
		"""Gets or sets the sketch from which that this sketch pattern feature is created."""
		self._instance.Sketch = value

	@property
	def use_centroid(self):
		"""Gets or sets whether to use a centroid for this sketch pattern feature."""
		return self._instance.UseCentroid

	@use_centroid.setter
	def use_centroid(self, value):
		"""Gets or sets whether to use a centroid for this sketch pattern feature."""
		self._instance.UseCentroid = value

	@property
	def access_selections(self):
		"""Gains access to selections used to define the sketch pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections used to define the sketch pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_base_point(self):
		"""Gets the base point data from which this sketch pattern is created."""
		return self._instance.GetBasePoint

	@get_base_point.setter
	def get_base_point(self, value):
		"""Gets the base point data from which this sketch pattern is created."""
		self._instance.GetBasePoint = value

	@property
	def get_pattern_body_count(self):
		"""Gets the number of seed bodies in the sketch pattern feature."""
		return self._instance.GetPatternBodyCount

	@get_pattern_body_count.setter
	def get_pattern_body_count(self, value):
		"""Gets the number of seed bodies in the sketch pattern feature."""
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
		"""Gets the number of seed features for this sketch pattern feature."""
		return self._instance.GetPatternFeatureCount

	@get_pattern_feature_count.setter
	def get_pattern_feature_count(self, value):
		"""Gets the number of seed features for this sketch pattern feature."""
		self._instance.GetPatternFeatureCount = value

	@property
	def get_reference_point_type(self):
		"""Gets the type of reference point for this sketch pattern feature."""
		return self._instance.GetReferencePointType

	@get_reference_point_type.setter
	def get_reference_point_type(self, value):
		"""Gets the type of reference point for this sketch pattern feature."""
		self._instance.GetReferencePointType = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified instance of this sketch pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified instance of this sketch pattern feature."""
		self._instance.GetTransform = value

	@property
	def i_access_selections(self):
		"""Gains access to selections used to define the sketch pattern feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to selections used to define the sketch pattern feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_base_point(self):
		"""Gets the base point data from which this sketch pattern is created."""
		return self._instance.IGetBasePoint

	@i_get_base_point.setter
	def i_get_base_point(self, value):
		"""Gets the base point data from which this sketch pattern is created."""
		self._instance.IGetBasePoint = value

	@property
	def i_get_pattern_body_array(self):
		"""Gets the seed bodies for the sketch pattern feature."""
		return self._instance.IGetPatternBodyArray

	@i_get_pattern_body_array.setter
	def i_get_pattern_body_array(self, value):
		"""Gets the seed bodies for the sketch pattern feature."""
		self._instance.IGetPatternBodyArray = value

	@property
	def i_get_pattern_face_array(self):
		"""Gets the patterned faces for the sketch pattern feature."""
		return self._instance.IGetPatternFaceArray

	@i_get_pattern_face_array.setter
	def i_get_pattern_face_array(self, value):
		"""Gets the patterned faces for the sketch pattern feature."""
		self._instance.IGetPatternFaceArray = value

	@property
	def i_get_pattern_feature_array(self):
		"""Gets the seed features for the sketch pattern."""
		return self._instance.IGetPatternFeatureArray

	@i_get_pattern_feature_array.setter
	def i_get_pattern_feature_array(self, value):
		"""Gets the seed features for the sketch pattern."""
		self._instance.IGetPatternFeatureArray = value

	@property
	def i_set_pattern_body_array(self):
		"""Sets the seed bodies for the sketch pattern feature."""
		return self._instance.ISetPatternBodyArray

	@i_set_pattern_body_array.setter
	def i_set_pattern_body_array(self, value):
		"""Sets the seed bodies for the sketch pattern feature."""
		self._instance.ISetPatternBodyArray = value

	@property
	def i_set_pattern_face_array(self):
		"""Sets the patterned faces for the sketch pattern feature."""
		return self._instance.ISetPatternFaceArray

	@i_set_pattern_face_array.setter
	def i_set_pattern_face_array(self, value):
		"""Sets the patterned faces for the sketch pattern feature."""
		self._instance.ISetPatternFaceArray = value

	@property
	def i_set_pattern_feature_array(self):
		"""Sets the seed features for the sketch pattern feature."""
		return self._instance.ISetPatternFeatureArray

	@i_set_pattern_feature_array.setter
	def i_set_pattern_feature_array(self, value):
		"""Sets the seed features for the sketch pattern feature."""
		self._instance.ISetPatternFeatureArray = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created this sketch pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created this sketch pattern feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_feature_scope(self):
		"""Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this sketch pattern feature."""
		return self._instance.SetFeatureScope

	@set_feature_scope.setter
	def set_feature_scope(self, value):
		"""Sets the feature scope, whether to autoselect the affected bodies, and the affected bodies in this sketch pattern feature."""
		self._instance.SetFeatureScope = value

