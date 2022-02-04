# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html
class ITablePatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def coordinate_system(self):
		"""Gets or sets the coordinate system of the table-driven pattern feature."""
		return self._instance.CoordinateSystem

	@coordinate_system.setter
	def coordinate_system(self, value):
		"""Gets or sets the coordinate system of the table-driven pattern feature."""
		self._instance.CoordinateSystem = value

	@property
	def geometry_pattern(self):
		"""Gets or sets whether to create the pattern using only the geometry (faces and edges) of the features for the table-driven pattern feature."""
		return self._instance.GeometryPattern

	@geometry_pattern.setter
	def geometry_pattern(self, value):
		"""Gets or sets whether to create the pattern using only the geometry (faces and edges) of the features for the table-driven pattern feature."""
		self._instance.GeometryPattern = value

	@property
	def pattern_body_array(self):
		"""Gets or sets the seed bodies to pattern for this table-driven pattern feature."""
		return self._instance.PatternBodyArray

	@pattern_body_array.setter
	def pattern_body_array(self, value):
		"""Gets or sets the seed bodies to pattern for this table-driven pattern feature."""
		self._instance.PatternBodyArray = value

	@property
	def pattern_face_array(self):
		"""Gets or sets the patterned faces for this table-driven pattern feature."""
		return self._instance.PatternFaceArray

	@pattern_face_array.setter
	def pattern_face_array(self, value):
		"""Gets or sets the patterned faces for this table-driven pattern feature."""
		self._instance.PatternFaceArray = value

	@property
	def pattern_feature_array(self):
		"""Gets or sets the seed features used to create the table-driven pattern feature."""
		return self._instance.PatternFeatureArray

	@pattern_feature_array.setter
	def pattern_feature_array(self, value):
		"""Gets or sets the seed features used to create the table-driven pattern feature."""
		self._instance.PatternFeatureArray = value

	@property
	def point_array(self):
		"""Gets or sets the array of points that describe the x,y, and z locations of the repeating elements in the table-driven pattern feature."""
		return self._instance.PointArray

	@point_array.setter
	def point_array(self, value):
		"""Gets or sets the array of points that describe the x,y, and z locations of the repeating elements in the table-driven pattern feature."""
		self._instance.PointArray = value

	@property
	def propagate_visual_property(self):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in the table-driven pattern feature."""
		return self._instance.PropagateVisualProperty

	@propagate_visual_property.setter
	def propagate_visual_property(self, value):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) in the table-driven pattern feature."""
		self._instance.PropagateVisualProperty = value

	@property
	def reference_point(self):
		"""Gets or sets the reference point for pattern instances of this table-driven pattern feature."""
		return self._instance.ReferencePoint

	@reference_point.setter
	def reference_point(self, value):
		"""Gets or sets the reference point for pattern instances of this table-driven pattern feature."""
		self._instance.ReferencePoint = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the skipped items for this table-driven pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the skipped items for this table-driven pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def use_centroid(self):
		"""Gets or sets whether to set the reference point to the centroid of the seed feature for this table-driven pattern feature."""
		return self._instance.UseCentroid

	@use_centroid.setter
	def use_centroid(self, value):
		"""Gets or sets whether to set the reference point to the centroid of the seed feature for this table-driven pattern feature."""
		self._instance.UseCentroid = value

	@property
	def access_selections(self):
		"""Gains access to selections used to define the table-driven pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections used to define the table-driven pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_base_point(self):
		"""Gets the base point for this table-driven pattern feature."""
		return self._instance.GetBasePoint

	@get_base_point.setter
	def get_base_point(self, value):
		"""Gets the base point for this table-driven pattern feature."""
		self._instance.GetBasePoint = value

	@property
	def get_pattern_body_count(self):
		"""Gets the number of seed bodies for this table-driven pattern feature."""
		return self._instance.GetPatternBodyCount

	@get_pattern_body_count.setter
	def get_pattern_body_count(self, value):
		"""Gets the number of seed bodies for this table-driven pattern feature."""
		self._instance.GetPatternBodyCount = value

	@property
	def get_pattern_face_count(self):
		"""Gets the number of patterned faces in this table-driven feature."""
		return self._instance.GetPatternFaceCount

	@get_pattern_face_count.setter
	def get_pattern_face_count(self, value):
		"""Gets the number of patterned faces in this table-driven feature."""
		self._instance.GetPatternFaceCount = value

	@property
	def get_pattern_feature_count(self):
		"""Gets the number of distinct seed features used to create this table-driven pattern feature."""
		return self._instance.GetPatternFeatureCount

	@get_pattern_feature_count.setter
	def get_pattern_feature_count(self, value):
		"""Gets the number of distinct seed features used to create this table-driven pattern feature."""
		self._instance.GetPatternFeatureCount = value

	@property
	def get_point_count(self):
		"""Gets the number of x, y, and z locations of the repeating elements in this table-driven pattern."""
		return self._instance.GetPointCount

	@get_point_count.setter
	def get_point_count(self, value):
		"""Gets the number of x, y, and z locations of the repeating elements in this table-driven pattern."""
		self._instance.GetPointCount = value

	@property
	def get_reference_point_type(self):
		"""Gets whether the table-driven pattern's reference point is a closed curve, a sketch point, or a vertex."""
		return self._instance.GetReferencePointType

	@get_reference_point_type.setter
	def get_reference_point_type(self, value):
		"""Gets whether the table-driven pattern's reference point is a closed curve, a sketch point, or a vertex."""
		self._instance.GetReferencePointType = value

	@property
	def get_skipped_item_count(self):
		"""Gets the number of skipped items in this table-driven pattern feature."""
		return self._instance.GetSkippedItemCount

	@get_skipped_item_count.setter
	def get_skipped_item_count(self, value):
		"""Gets the number of skipped items in this table-driven pattern feature."""
		self._instance.GetSkippedItemCount = value

	@property
	def get_transform(self):
		"""Gets the transform for the specified repeating element in this table-driven pattern feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for the specified repeating element in this table-driven pattern feature."""
		self._instance.GetTransform = value

	@property
	def i_access_selections(self):
		"""Gains access to selections used to define the table-driven pattern feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to selections used to define the table-driven pattern feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_base_point(self):
		"""Gets the base point for this table-driven pattern feature."""
		return self._instance.IGetBasePoint

	@i_get_base_point.setter
	def i_get_base_point(self, value):
		"""Gets the base point for this table-driven pattern feature."""
		self._instance.IGetBasePoint = value

	@property
	def i_get_pattern_body_array(self):
		"""Gets the seed bodies for this table-driven pattern feature."""
		return self._instance.IGetPatternBodyArray

	@i_get_pattern_body_array.setter
	def i_get_pattern_body_array(self, value):
		"""Gets the seed bodies for this table-driven pattern feature."""
		self._instance.IGetPatternBodyArray = value

	@property
	def i_get_pattern_face_array(self):
		"""Gets the patterned faces in this table-driven pattern feature."""
		return self._instance.IGetPatternFaceArray

	@i_get_pattern_face_array.setter
	def i_get_pattern_face_array(self, value):
		"""Gets the patterned faces in this table-driven pattern feature."""
		self._instance.IGetPatternFaceArray = value

	@property
	def i_get_pattern_feature_array(self):
		"""Gets the seed features used to create the table-driven pattern."""
		return self._instance.IGetPatternFeatureArray

	@i_get_pattern_feature_array.setter
	def i_get_pattern_feature_array(self, value):
		"""Gets the seed features used to create the table-driven pattern."""
		self._instance.IGetPatternFeatureArray = value

	@property
	def i_get_point_array(self):
		"""Gets an array of doubles that describe the x, y, and z locations of the repeating elements in this table-driven pattern feature."""
		return self._instance.IGetPointArray

	@i_get_point_array.setter
	def i_get_point_array(self, value):
		"""Gets an array of doubles that describe the x, y, and z locations of the repeating elements in this table-driven pattern feature."""
		self._instance.IGetPointArray = value

	@property
	def i_get_skipped_item_array(self):
		"""Gets the skipped items in this table-driven pattern feature."""
		return self._instance.IGetSkippedItemArray

	@i_get_skipped_item_array.setter
	def i_get_skipped_item_array(self, value):
		"""Gets the skipped items in this table-driven pattern feature."""
		self._instance.IGetSkippedItemArray = value

	@property
	def i_set_pattern_body_array(self):
		"""Sets the seed bodies for this table-driven pattern feature."""
		return self._instance.ISetPatternBodyArray

	@i_set_pattern_body_array.setter
	def i_set_pattern_body_array(self, value):
		"""Sets the seed bodies for this table-driven pattern feature."""
		self._instance.ISetPatternBodyArray = value

	@property
	def i_set_pattern_face_array(self):
		"""Sets the patterned faces for this table-driven pattern feature."""
		return self._instance.ISetPatternFaceArray

	@i_set_pattern_face_array.setter
	def i_set_pattern_face_array(self, value):
		"""Sets the patterned faces for this table-driven pattern feature."""
		self._instance.ISetPatternFaceArray = value

	@property
	def i_set_pattern_feature_array(self):
		"""Sets the seed features used to create the table-driven pattern feature."""
		return self._instance.ISetPatternFeatureArray

	@i_set_pattern_feature_array.setter
	def i_set_pattern_feature_array(self, value):
		"""Sets the seed features used to create the table-driven pattern feature."""
		self._instance.ISetPatternFeatureArray = value

	@property
	def i_set_point_array(self):
		"""Sets the points that describe the x, y, and z locations of the repeating elements in the table-driven pattern feature."""
		return self._instance.ISetPointArray

	@i_set_point_array.setter
	def i_set_point_array(self, value):
		"""Sets the points that describe the x, y, and z locations of the repeating elements in the table-driven pattern feature."""
		self._instance.ISetPointArray = value

	@property
	def i_set_skipped_item_array(self):
		"""Sets the skipped items in this table-driven pattern feature."""
		return self._instance.ISetSkippedItemArray

	@i_set_skipped_item_array.setter
	def i_set_skipped_item_array(self, value):
		"""Sets the skipped items in this table-driven pattern feature."""
		self._instance.ISetSkippedItemArray = value

	@property
	def load_points_from_file(self):
		"""Loads the location points of the table-driven pattern from a *.sldptab file."""
		return self._instance.LoadPointsFromFile

	@load_points_from_file.setter
	def load_points_from_file(self, value):
		"""Loads the location points of the table-driven pattern from a *.sldptab file."""
		self._instance.LoadPointsFromFile = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created this table-driven pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created this table-driven pattern feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def save_points_to_file(self):
		"""Saves the location of the table-driven pattern feature's points to a *.sldptab file."""
		return self._instance.SavePointsToFile

	@save_points_to_file.setter
	def save_points_to_file(self, value):
		"""Saves the location of the table-driven pattern feature's points to a *.sldptab file."""
		self._instance.SavePointsToFile = value

