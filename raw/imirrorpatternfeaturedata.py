# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData_members.html
class IMirrorPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for the mirror pattern feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for the mirror pattern feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies that the mirror pattern feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies that the mirror pattern feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def geometry_pattern(self):
		"""Gets or sets whether to mirror only the geometry (faces and edges) of the feature for this mirror pattern feature."""
		return self._instance.GeometryPattern

	@geometry_pattern.setter
	def geometry_pattern(self, value):
		"""Gets or sets whether to mirror only the geometry (faces and edges) of the feature for this mirror pattern feature."""
		self._instance.GeometryPattern = value

	@property
	def mirror_face_array(self):
		"""Gets or sets the faces to mirror."""
		return self._instance.MirrorFaceArray

	@mirror_face_array.setter
	def mirror_face_array(self, value):
		"""Gets or sets the faces to mirror."""
		self._instance.MirrorFaceArray = value

	@property
	def pattern_feature_array(self):
		"""Gets or sets the seed features to use to create the mirror pattern."""
		return self._instance.PatternFeatureArray

	@pattern_feature_array.setter
	def pattern_feature_array(self, value):
		"""Gets or sets the seed features to use to create the mirror pattern."""
		self._instance.PatternFeatureArray = value

	@property
	def plane(self):
		"""Gets or sets the plane about which to mirror the part."""
		return self._instance.Plane

	@plane.setter
	def plane(self, value):
		"""Gets or sets the plane about which to mirror the part."""
		self._instance.Plane = value

	@property
	def propagate_visual_property(self):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all pattern instances."""
		return self._instance.PropagateVisualProperty

	@propagate_visual_property.setter
	def propagate_visual_property(self, value):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all pattern instances."""
		self._instance.PropagateVisualProperty = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define the mirror pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define the mirror pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_feature_scope_bodies_count(self):
		"""Gets the number of solid bodies affected by the mirror pattern feature in a multibody part."""
		return self._instance.GetFeatureScopeBodiesCount

	@get_feature_scope_bodies_count.setter
	def get_feature_scope_bodies_count(self, value):
		"""Gets the number of solid bodies affected by the mirror pattern feature in a multibody part."""
		self._instance.GetFeatureScopeBodiesCount = value

	@property
	def get_mirror_face_count(self):
		"""Gets the number of mirrored faces."""
		return self._instance.GetMirrorFaceCount

	@get_mirror_face_count.setter
	def get_mirror_face_count(self, value):
		"""Gets the number of mirrored faces."""
		self._instance.GetMirrorFaceCount = value

	@property
	def get_mirror_plane_type(self):
		"""Gets whether the mirror plane is a face or a reference plane."""
		return self._instance.GetMirrorPlaneType

	@get_mirror_plane_type.setter
	def get_mirror_plane_type(self, value):
		"""Gets whether the mirror plane is a face or a reference plane."""
		self._instance.GetMirrorPlaneType = value

	@property
	def get_pattern_feature_count(self):
		"""Gets the number of seed features used to create this mirror pattern."""
		return self._instance.GetPatternFeatureCount

	@get_pattern_feature_count.setter
	def get_pattern_feature_count(self, value):
		"""Gets the number of seed features used to create this mirror pattern."""
		self._instance.GetPatternFeatureCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define the mirror pattern feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define the mirror pattern feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_feature_scope_bodies(self):
		"""Gets the solid bodies that the mirror pattern feature affects in a multibody part."""
		return self._instance.IGetFeatureScopeBodies

	@i_get_feature_scope_bodies.setter
	def i_get_feature_scope_bodies(self, value):
		"""Gets the solid bodies that the mirror pattern feature affects in a multibody part."""
		self._instance.IGetFeatureScopeBodies = value

	@property
	def i_get_mirror_face_array(self):
		"""Gets the mirrored faces."""
		return self._instance.IGetMirrorFaceArray

	@i_get_mirror_face_array.setter
	def i_get_mirror_face_array(self, value):
		"""Gets the mirrored faces."""
		self._instance.IGetMirrorFaceArray = value

	@property
	def i_get_pattern_feature_array(self):
		"""Gets the seed features used to create the mirror pattern."""
		return self._instance.IGetPatternFeatureArray

	@i_get_pattern_feature_array.setter
	def i_get_pattern_feature_array(self, value):
		"""Gets the seed features used to create the mirror pattern."""
		self._instance.IGetPatternFeatureArray = value

	@property
	def i_set_feature_scope_bodies(self):
		"""Sets the solid bodies that the mirror pattern feature affects in a multibody part."""
		return self._instance.ISetFeatureScopeBodies

	@i_set_feature_scope_bodies.setter
	def i_set_feature_scope_bodies(self, value):
		"""Sets the solid bodies that the mirror pattern feature affects in a multibody part."""
		self._instance.ISetFeatureScopeBodies = value

	@property
	def i_set_mirror_face_array(self):
		"""Sets the faces to mirror."""
		return self._instance.ISetMirrorFaceArray

	@i_set_mirror_face_array.setter
	def i_set_mirror_face_array(self, value):
		"""Sets the faces to mirror."""
		self._instance.ISetMirrorFaceArray = value

	@property
	def i_set_pattern_feature_array(self):
		"""Sets the seed features to use to create this mirror pattern feature."""
		return self._instance.ISetPatternFeatureArray

	@i_set_pattern_feature_array.setter
	def i_set_pattern_feature_array(self, value):
		"""Sets the seed features to use to create this mirror pattern feature."""
		self._instance.ISetPatternFeatureArray = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the mirror pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the mirror pattern feature."""
		self._instance.ReleaseSelectionAccess = value

