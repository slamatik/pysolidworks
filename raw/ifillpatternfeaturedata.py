# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.html
class IFillPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all or only specific bodies in a multibody part to be affected by this fill pattern feature."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all or only specific bodies in a multibody part to be affected by this fill pattern feature."""
		self._instance.AutoSelect = value

	@property
	def create_seed_cut_polygon_sides(self):
		"""Gets or sets the number of sides in a polygon-cut seed instance of this fill pattern feature."""
		return self._instance.CreateSeedCutPolygonSides

	@create_seed_cut_polygon_sides.setter
	def create_seed_cut_polygon_sides(self, value):
		"""Gets or sets the number of sides in a polygon-cut seed instance of this fill pattern feature."""
		self._instance.CreateSeedCutPolygonSides = value

	@property
	def create_seed_cut_type(self):
		"""Gets or sets the type of cut for this fill pattern's seed instance."""
		return self._instance.CreateSeedCutType

	@create_seed_cut_type.setter
	def create_seed_cut_type(self, value):
		"""Gets or sets the type of cut for this fill pattern's seed instance."""
		self._instance.CreateSeedCutType = value

	@property
	def diagonal(self):
		"""Gets or sets the length of the diagonal of a diamond-cut seed instance of this fill pattern feature."""
		return self._instance.Diagonal

	@diagonal.setter
	def diagonal(self, value):
		"""Gets or sets the length of the diagonal of a diamond-cut seed instance of this fill pattern feature."""
		self._instance.Diagonal = value

	@property
	def diameter(self):
		"""Gets or sets the diameter of a circle-cut seed instance of this fill pattern feature."""
		return self._instance.Diameter

	@diameter.setter
	def diameter(self, value):
		"""Gets or sets the diameter of a circle-cut seed instance of this fill pattern feature."""
		self._instance.Diameter = value

	@property
	def dimension(self):
		"""Gets or sets the length of a side of a diamond-cut or square-cut seed instance of this fill pattern feature."""
		return self._instance.Dimension

	@dimension.setter
	def dimension(self, value):
		"""Gets or sets the length of a side of a diamond-cut or square-cut seed instance of this fill pattern feature."""
		self._instance.Dimension = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for this fill pattern feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for this fill pattern feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies that the fill pattern feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies that the fill pattern feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def features_to_pattern_type(self):
		"""Gets or sets the type of object to pattern in this fill pattern feature."""
		return self._instance.FeaturesToPatternType

	@features_to_pattern_type.setter
	def features_to_pattern_type(self, value):
		"""Gets or sets the type of object to pattern in this fill pattern feature."""
		self._instance.FeaturesToPatternType = value

	@property
	def geometry_pattern(self):
		"""Gets or sets whether to create this fill pattern using an exact copy of the seed feature."""
		return self._instance.GeometryPattern

	@geometry_pattern.setter
	def geometry_pattern(self, value):
		"""Gets or sets whether to create this fill pattern using an exact copy of the seed feature."""
		self._instance.GeometryPattern = value

	@property
	def inner_radius(self):
		"""Gets or sets the radius of the circle that inscribes the polygon-cut seed instance of this fill pattern feature."""
		return self._instance.InnerRadius

	@inner_radius.setter
	def inner_radius(self, value):
		"""Gets or sets the radius of the circle that inscribes the polygon-cut seed instance of this fill pattern feature."""
		self._instance.InnerRadius = value

	@property
	def instance_spacing(self):
		"""Gets or sets the distance between the pattern instance centers of this fill pattern feature."""
		return self._instance.InstanceSpacing

	@instance_spacing.setter
	def instance_spacing(self, value):
		"""Gets or sets the distance between the pattern instance centers of this fill pattern feature."""
		self._instance.InstanceSpacing = value

	@property
	def layout_spacing_type(self):
		"""Gets or sets the type of spacing between the instances in the layout of this fill pattern feature."""
		return self._instance.LayoutSpacingType

	@layout_spacing_type.setter
	def layout_spacing_type(self, value):
		"""Gets or sets the type of spacing between the instances in the layout of this fill pattern feature."""
		self._instance.LayoutSpacingType = value

	@property
	def loop_spacing(self):
		"""Gets or sets the distance between loops of pattern instances in this fill pattern feature."""
		return self._instance.LoopSpacing

	@loop_spacing.setter
	def loop_spacing(self, value):
		"""Gets or sets the distance between loops of pattern instances in this fill pattern feature."""
		self._instance.LoopSpacing = value

	@property
	def margins(self):
		"""Gets or sets the distance between the fill boundary and the outermost pattern instance in the layout of this fill pattern feature."""
		return self._instance.Margins

	@margins.setter
	def margins(self, value):
		"""Gets or sets the distance between the fill boundary and the outermost pattern instance in the layout of this fill pattern feature."""
		self._instance.Margins = value

	@property
	def no_of_instances(self):
		"""Gets or sets the number of instances per loop or side of the layout of this fill pattern feature."""
		return self._instance.NoOfInstances

	@no_of_instances.setter
	def no_of_instances(self, value):
		"""Gets or sets the number of instances per loop or side of the layout of this fill pattern feature."""
		self._instance.NoOfInstances = value

	@property
	def outer_radius(self):
		"""Gets or sets the radius of the circle that circumscribes the polygon-cut seed instance of this fill pattern feature."""
		return self._instance.OuterRadius

	@outer_radius.setter
	def outer_radius(self, value):
		"""Gets or sets the radius of the circle that circumscribes the polygon-cut seed instance of this fill pattern feature."""
		self._instance.OuterRadius = value

	@property
	def pattern_body_array(self):
		"""Gets or sets the array of bodies to pattern in this fill pattern feature."""
		return self._instance.PatternBodyArray

	@pattern_body_array.setter
	def pattern_body_array(self, value):
		"""Gets or sets the array of bodies to pattern in this fill pattern feature."""
		self._instance.PatternBodyArray = value

	@property
	def pattern_direction(self):
		"""Gets or sets the direction reference for the layout of this fill pattern feature."""
		return self._instance.PatternDirection

	@pattern_direction.setter
	def pattern_direction(self, value):
		"""Gets or sets the direction reference for the layout of this fill pattern feature."""
		self._instance.PatternDirection = value

	@property
	def pattern_direction_type(self):
		"""Gets the type of pattern direction reference returned by IFillPatternFeatureData::PatternDirection for this fill pattern feature."""
		return self._instance.PatternDirectionType

	@pattern_direction_type.setter
	def pattern_direction_type(self, value):
		"""Gets the type of pattern direction reference returned by IFillPatternFeatureData::PatternDirection for this fill pattern feature."""
		self._instance.PatternDirectionType = value

	@property
	def pattern_element(self):
		"""Gets or sets the pattern element selection of this fill pattern feature."""
		return self._instance.PatternElement

	@pattern_element.setter
	def pattern_element(self, value):
		"""Gets or sets the pattern element selection of this fill pattern feature."""
		self._instance.PatternElement = value

	@property
	def pattern_face_array(self):
		"""Gets or sets the array of faces to pattern in this fill pattern feature."""
		return self._instance.PatternFaceArray

	@pattern_face_array.setter
	def pattern_face_array(self, value):
		"""Gets or sets the array of faces to pattern in this fill pattern feature."""
		self._instance.PatternFaceArray = value

	@property
	def pattern_feature_array(self):
		"""Gets or sets the array of features to pattern in this fill pattern feature."""
		return self._instance.PatternFeatureArray

	@pattern_feature_array.setter
	def pattern_feature_array(self, value):
		"""Gets or sets the array of features to pattern in this fill pattern feature."""
		self._instance.PatternFeatureArray = value

	@property
	def pattern_fill_boundary_array(self):
		"""Gets or sets the array of objects representing the boundary of this fill pattern feature."""
		return self._instance.PatternFillBoundaryArray

	@pattern_fill_boundary_array.setter
	def pattern_fill_boundary_array(self, value):
		"""Gets or sets the array of objects representing the boundary of this fill pattern feature."""
		self._instance.PatternFillBoundaryArray = value

	@property
	def pattern_layout_polygon_sides(self):
		"""Gets or sets the number of sides in the polygonal layout of this fill pattern feature."""
		return self._instance.PatternLayoutPolygonSides

	@pattern_layout_polygon_sides.setter
	def pattern_layout_polygon_sides(self, value):
		"""Gets or sets the number of sides in the polygonal layout of this fill pattern feature."""
		self._instance.PatternLayoutPolygonSides = value

	@property
	def pattern_layout_type(self):
		"""Gets or sets the layout of the pattern instances within the fill boundary of this fill pattern feature."""
		return self._instance.PatternLayoutType

	@pattern_layout_type.setter
	def pattern_layout_type(self, value):
		"""Gets or sets the layout of the pattern instances within the fill boundary of this fill pattern feature."""
		self._instance.PatternLayoutType = value

	@property
	def propagate_visual_property(self):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, cosmetic thread data, etc.) to all fill pattern instances in this fill pattern feature."""
		return self._instance.PropagateVisualProperty

	@propagate_visual_property.setter
	def propagate_visual_property(self, value):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, cosmetic thread data, etc.) to all fill pattern instances in this fill pattern feature."""
		self._instance.PropagateVisualProperty = value

	@property
	def rotation(self):
		"""Gets or sets the counterclockwise rotation of the seed instance of this fill pattern feature."""
		return self._instance.Rotation

	@rotation.setter
	def rotation(self, value):
		"""Gets or sets the counterclockwise rotation of the seed instance of this fill pattern feature."""
		self._instance.Rotation = value

	@property
	def seed_cut_flip_shape_direction(self):
		"""Gets or sets whether to reverse the direction of the seed instance cut of this fill pattern feature."""
		return self._instance.SeedCutFlipShapeDirection

	@seed_cut_flip_shape_direction.setter
	def seed_cut_flip_shape_direction(self, value):
		"""Gets or sets whether to reverse the direction of the seed instance cut of this fill pattern feature."""
		self._instance.SeedCutFlipShapeDirection = value

	@property
	def seed_feature_center(self):
		"""Gets or sets the vertex or sketch point where to place the center of the seed cut feature of this fill pattern feature."""
		return self._instance.SeedFeatureCenter

	@seed_feature_center.setter
	def seed_feature_center(self, value):
		"""Gets or sets the vertex or sketch point where to place the center of the seed cut feature of this fill pattern feature."""
		self._instance.SeedFeatureCenter = value

	@property
	def seed_feature_center_type(self):
		"""Gets or sets the type of entity where to place the center of the seed cut feature for this fill pattern feature."""
		return self._instance.SeedFeatureCenterType

	@seed_feature_center_type.setter
	def seed_feature_center_type(self, value):
		"""Gets or sets the type of entity where to place the center of the seed cut feature for this fill pattern feature."""
		self._instance.SeedFeatureCenterType = value

	@property
	def skipped_item_array(self):
		"""Gets or sets the pattern instances to skip in this fill pattern feature."""
		return self._instance.SkippedItemArray

	@skipped_item_array.setter
	def skipped_item_array(self, value):
		"""Gets or sets the pattern instances to skip in this fill pattern feature."""
		self._instance.SkippedItemArray = value

	@property
	def stagger_angle(self):
		"""Gets or sets the angle by which to stagger the rows of pattern instances in the perforation layout of this fill pattern feature."""
		return self._instance.StaggerAngle

	@stagger_angle.setter
	def stagger_angle(self, value):
		"""Gets or sets the angle by which to stagger the rows of pattern instances in the perforation layout of this fill pattern feature."""
		self._instance.StaggerAngle = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define this fill pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define this fill pattern feature."""
		self._instance.AccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that define this fill pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that define this fill pattern feature."""
		self._instance.ReleaseSelectionAccess = value

