# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html
class ISketchManager:
	def __init__(self, parent=None):
		self._instance = parent

	def active_sketch(self):
		"""Gets the active sketch."""
		# return self._instance.ActiveSketch
		raise NotImplemented

	@property
	def add_to_d_b(self):
		"""Gets or sets whether sketch entities are added directly to the SOLIDWORKS database."""
		return self._instance.AddToDB

	@add_to_d_b.setter
	def add_to_d_b(self, value):
		"""Gets or sets whether sketch entities are added directly to the SOLIDWORKS database."""
		self._instance.AddToDB = value

	@property
	def auto_solve(self):
		"""Gets or sets whether SOLIDWORKS automatically solves the sketch geometry of the part while creating it."""
		return self._instance.AutoSolve

	@auto_solve.setter
	def auto_solve(self, value):
		"""Gets or sets whether SOLIDWORKS automatically solves the sketch geometry of the part while creating it."""
		self._instance.AutoSolve = value

	@property
	def curvature_density(self):
		"""Gets or sets the scaling factor by which to adjust the density of the curvature combs for this spline."""
		return self._instance.CurvatureDensity

	@curvature_density.setter
	def curvature_density(self, value):
		"""Gets or sets the scaling factor by which to adjust the density of the curvature combs for this spline."""
		self._instance.CurvatureDensity = value

	@property
	def curvature_scale(self):
		"""Gets or sets the scaling factor by which to adjust the size of the curvature combs for this spline."""
		return self._instance.CurvatureScale

	@curvature_scale.setter
	def curvature_scale(self, value):
		"""Gets or sets the scaling factor by which to adjust the size of the curvature combs for this spline."""
		self._instance.CurvatureScale = value

	@property
	def display_when_added(self):
		"""Gets or sets whether new sketch entities are immediately displayed when created."""
		return self._instance.DisplayWhenAdded

	@display_when_added.setter
	def display_when_added(self, value):
		"""Gets or sets whether new sketch entities are immediately displayed when created."""
		self._instance.DisplayWhenAdded = value

	@property
	def document(self):
		"""Gets the document for this ISketchManager object."""
		return self._instance.Document

	@document.setter
	def document(self, value):
		"""Gets the document for this ISketchManager object."""
		self._instance.Document = value

	@property
	def add_along_x_dimension(self):
		"""Projects and displays along the x axis a dimension between selected points in a 3D sketch."""
		return self._instance.AddAlongXDimension

	@add_along_x_dimension.setter
	def add_along_x_dimension(self, value):
		"""Projects and displays along the x axis a dimension between selected points in a 3D sketch."""
		self._instance.AddAlongXDimension = value

	@property
	def add_along_y_dimension(self):
		"""Projects and displays along the y axis a dimension between selected points in a 3D sketch."""
		return self._instance.AddAlongYDimension

	@add_along_y_dimension.setter
	def add_along_y_dimension(self, value):
		"""Projects and displays along the y axis a dimension between selected points in a 3D sketch."""
		self._instance.AddAlongYDimension = value

	@property
	def add_along_z_dimension(self):
		"""Projects and displays along the z axis a dimension between selected points in a 3D sketch."""
		return self._instance.AddAlongZDimension

	@add_along_z_dimension.setter
	def add_along_z_dimension(self, value):
		"""Projects and displays along the z axis a dimension between selected points in a 3D sketch."""
		self._instance.AddAlongZDimension = value

	@property
	def convert_entities(self):
		"""Not implemented. Use ISketchManager::SketchUseEdge2."""
		return self._instance.ConvertEntities

	@convert_entities.setter
	def convert_entities(self, value):
		"""Not implemented. Use ISketchManager::SketchUseEdge2."""
		self._instance.ConvertEntities = value

	@property
	def create_point_arc(self):
		"""Creates a 3-point arc."""
		return self._instance.Create3PointArc

	@create_point_arc.setter
	def create_point_arc(self, value):
		"""Creates a 3-point arc."""
		self._instance.Create3PointArc = value

	@property
	def create_point_center_rectangle(self):
		"""Creates a 3-point center rectangle at any angle."""
		return self._instance.Create3PointCenterRectangle

	@create_point_center_rectangle.setter
	def create_point_center_rectangle(self, value):
		"""Creates a 3-point center rectangle at any angle."""
		self._instance.Create3PointCenterRectangle = value

	@property
	def create_point_corner_rectangle(self):
		"""Creates a 3-point corner rectangle at any angle."""
		return self._instance.Create3PointCornerRectangle

	@create_point_corner_rectangle.setter
	def create_point_corner_rectangle(self, value):
		"""Creates a 3-point corner rectangle at any angle."""
		self._instance.Create3PointCornerRectangle = value

	@property
	def create_arc(self):
		"""Creates an arc based on a center point, a start point, an end point, and a direction."""
		return self._instance.CreateArc

	@create_arc.setter
	def create_arc(self, value):
		"""Creates an arc based on a center point, a start point, an end point, and a direction."""
		self._instance.CreateArc = value

	@property
	def create_boundary_hatch(self):
		"""Creates area hatch/fill boundary hatches using closed sketch profiles."""
		return self._instance.CreateBoundaryHatch

	@create_boundary_hatch.setter
	def create_boundary_hatch(self, value):
		"""Creates area hatch/fill boundary hatches using closed sketch profiles."""
		self._instance.CreateBoundaryHatch = value

	@property
	def create_center_line(self):
		"""Creates a center line between the specified points."""
		return self._instance.CreateCenterLine

	@create_center_line.setter
	def create_center_line(self, value):
		"""Creates a center line between the specified points."""
		self._instance.CreateCenterLine = value

	@property
	def create_center_rectangle(self):
		"""Creates a center rectangle."""
		return self._instance.CreateCenterRectangle

	@create_center_rectangle.setter
	def create_center_rectangle(self, value):
		"""Creates a center rectangle."""
		self._instance.CreateCenterRectangle = value

	@property
	def create_chamfer(self):
		"""Creates a chamfer between two selected sketch entities."""
		return self._instance.CreateChamfer

	@create_chamfer.setter
	def create_chamfer(self, value):
		"""Creates a chamfer between two selected sketch entities."""
		self._instance.CreateChamfer = value

	@property
	def create_circle(self):
		"""Creates a circle based on a center point and a point on the circle."""
		return self._instance.CreateCircle

	@create_circle.setter
	def create_circle(self, value):
		"""Creates a circle based on a center point and a point on the circle."""
		self._instance.CreateCircle = value

	@property
	def create_circle_by_radius(self):
		"""Creates a circle based on a center point and a specified radius."""
		return self._instance.CreateCircleByRadius

	@create_circle_by_radius.setter
	def create_circle_by_radius(self, value):
		"""Creates a circle based on a center point and a specified radius."""
		self._instance.CreateCircleByRadius = value

	@property
	def create_circular_sketch_step_and_repeat(self):
		"""Creates circular sketch pattern."""
		return self._instance.CreateCircularSketchStepAndRepeat

	@create_circular_sketch_step_and_repeat.setter
	def create_circular_sketch_step_and_repeat(self, value):
		"""Creates circular sketch pattern."""
		self._instance.CreateCircularSketchStepAndRepeat = value

	@property
	def create_conic(self):
		"""Creates a conic curve in the active sketch."""
		return self._instance.CreateConic

	@create_conic.setter
	def create_conic(self, value):
		"""Creates a conic curve in the active sketch."""
		self._instance.CreateConic = value

	@property
	def create_construction_geometry(self):
		"""Sets selected sketch segments to be construction geometry instead of sketch geometry."""
		return self._instance.CreateConstructionGeometry

	@create_construction_geometry.setter
	def create_construction_geometry(self, value):
		"""Sets selected sketch segments to be construction geometry instead of sketch geometry."""
		self._instance.CreateConstructionGeometry = value

	@property
	def create_corner_rectangle(self):
		"""Creates a corner rectangle."""
		return self._instance.CreateCornerRectangle

	@create_corner_rectangle.setter
	def create_corner_rectangle(self, value):
		"""Creates a corner rectangle."""
		self._instance.CreateCornerRectangle = value

	@property
	def create_ellipse(self):
		"""Creates an ellipse using the specified center, major-axis, and minor-axis points."""
		return self._instance.CreateEllipse

	@create_ellipse.setter
	def create_ellipse(self, value):
		"""Creates an ellipse using the specified center, major-axis, and minor-axis points."""
		self._instance.CreateEllipse = value

	@property
	def create_elliptical_arc(self):
		"""Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points."""
		return self._instance.CreateEllipticalArc

	@create_elliptical_arc.setter
	def create_elliptical_arc(self, value):
		"""Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points."""
		self._instance.CreateEllipticalArc = value

	@property
	def create_equation_spline(self):
		"""Creates an equation-driven 2D explicit or parametric curve or a 3D parametric curve."""
		return self._instance.CreateEquationSpline2

	@create_equation_spline.setter
	def create_equation_spline(self, value):
		"""Creates an equation-driven 2D explicit or parametric curve or a 3D parametric curve."""
		self._instance.CreateEquationSpline2 = value

	@property
	def create_fillet(self):
		"""Creates a sketch fillet using the selected sketch entities."""
		return self._instance.CreateFillet

	@create_fillet.setter
	def create_fillet(self, value):
		"""Creates a sketch fillet using the selected sketch entities."""
		self._instance.CreateFillet = value

	@property
	def create_line(self):
		"""Creates a sketch line in the currently active 2D or 3D sketch."""
		return self._instance.CreateLine

	@create_line.setter
	def create_line(self, value):
		"""Creates a sketch line in the currently active 2D or 3D sketch."""
		self._instance.CreateLine = value

	@property
	def create_linear_sketch_step_and_repeat(self):
		"""Creates a linear sketch pattern."""
		return self._instance.CreateLinearSketchStepAndRepeat

	@create_linear_sketch_step_and_repeat.setter
	def create_linear_sketch_step_and_repeat(self, value):
		"""Creates a linear sketch pattern."""
		self._instance.CreateLinearSketchStepAndRepeat = value

	@property
	def create_parabola(self):
		"""Creates a parabola in the active sketch."""
		return self._instance.CreateParabola

	@create_parabola.setter
	def create_parabola(self, value):
		"""Creates a parabola in the active sketch."""
		self._instance.CreateParabola = value

	@property
	def create_parallelogram(self):
		"""Creates a parallelogram."""
		return self._instance.CreateParallelogram

	@create_parallelogram.setter
	def create_parallelogram(self, value):
		"""Creates a parallelogram."""
		self._instance.CreateParallelogram = value

	@property
	def create_point(self):
		"""Creates a sketch point in the active 2D or 3D sketch."""
		return self._instance.CreatePoint

	@create_point.setter
	def create_point(self, value):
		"""Creates a sketch point in the active 2D or 3D sketch."""
		self._instance.CreatePoint = value

	@property
	def create_polygon(self):
		"""Creates a polygon in the active sketch."""
		return self._instance.CreatePolygon

	@create_polygon.setter
	def create_polygon(self, value):
		"""Creates a polygon in the active sketch."""
		self._instance.CreatePolygon = value

	@property
	def create_region_hatch(self):
		"""Creates an area hatch/fill region hatch using a closed sketch profile."""
		return self._instance.CreateRegionHatch

	@create_region_hatch.setter
	def create_region_hatch(self, value):
		"""Creates an area hatch/fill region hatch using a closed sketch profile."""
		self._instance.CreateRegionHatch = value

	@property
	def create_sketch_belt(self):
		"""Creates a sketch belt feature."""
		return self._instance.CreateSketchBelt

	@create_sketch_belt.setter
	def create_sketch_belt(self, value):
		"""Creates a sketch belt feature."""
		self._instance.CreateSketchBelt = value

	@property
	def create_sketch_plane(self):
		"""Creates a 3D sketch plane."""
		return self._instance.CreateSketchPlane

	@create_sketch_plane.setter
	def create_sketch_plane(self, value):
		"""Creates a 3D sketch plane."""
		self._instance.CreateSketchPlane = value

	@property
	def create_sketch_slot(self):
		"""Creates a sketch slot."""
		return self._instance.CreateSketchSlot

	@create_sketch_slot.setter
	def create_sketch_slot(self, value):
		"""Creates a sketch slot."""
		self._instance.CreateSketchSlot = value

	@property
	def create_spline(self):
		"""Creates either a 2D spline or a spline constrained to a surface."""
		return self._instance.CreateSpline3

	@create_spline.setter
	def create_spline(self, value):
		"""Creates either a 2D spline or a spline constrained to a surface."""
		self._instance.CreateSpline3 = value

	@property
	def create_spline_by_eqn_params(self):
		"""Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector."""
		return self._instance.CreateSplineByEqnParams

	@create_spline_by_eqn_params.setter
	def create_spline_by_eqn_params(self, value):
		"""Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector."""
		self._instance.CreateSplineByEqnParams = value

	@property
	def create_spline_param_data(self):
		"""Creates an empty spline parameter data object."""
		return self._instance.CreateSplineParamData

	@create_spline_param_data.setter
	def create_spline_param_data(self, value):
		"""Creates an empty spline parameter data object."""
		self._instance.CreateSplineParamData = value

	@property
	def create_splines_by_eqn_params(self):
		"""Creates one or more spline segments using the B-curve parameters provided."""
		return self._instance.CreateSplinesByEqnParams2

	@create_splines_by_eqn_params.setter
	def create_splines_by_eqn_params(self, value):
		"""Creates one or more spline segments using the B-curve parameters provided."""
		self._instance.CreateSplinesByEqnParams2 = value

	@property
	def create_tangent_arc(self):
		"""Creates a tangent arc."""
		return self._instance.CreateTangentArc

	@create_tangent_arc.setter
	def create_tangent_arc(self, value):
		"""Creates a tangent arc."""
		self._instance.CreateTangentArc = value

	@property
	def edit_circular_sketch_step_and_repeat(self):
		"""Edits a circular sketch pattern."""
		return self._instance.EditCircularSketchStepAndRepeat

	@edit_circular_sketch_step_and_repeat.setter
	def edit_circular_sketch_step_and_repeat(self, value):
		"""Edits a circular sketch pattern."""
		self._instance.EditCircularSketchStepAndRepeat = value

	@property
	def edit_linear_sketch_step_and_repeat(self):
		"""Edits a linear sketch pattern."""
		return self._instance.EditLinearSketchStepAndRepeat

	@edit_linear_sketch_step_and_repeat.setter
	def edit_linear_sketch_step_and_repeat(self, value):
		"""Edits a linear sketch pattern."""
		self._instance.EditLinearSketchStepAndRepeat = value

	@property
	def edit_sketch_block(self):
		"""Puts the block definition in edit mode."""
		return self._instance.EditSketchBlock

	@edit_sketch_block.setter
	def edit_sketch_block(self, value):
		"""Puts the block definition in edit mode."""
		self._instance.EditSketchBlock = value

	@property
	def end_edit_sketch_block(self):
		"""Saves or discards your edits of the block and then ends the current editing session of this block."""
		return self._instance.EndEditSketchBlock

	@end_edit_sketch_block.setter
	def end_edit_sketch_block(self, value):
		"""Saves or discards your edits of the block and then ends the current editing session of this block."""
		self._instance.EndEditSketchBlock = value

	@property
	def explode_sketch_block_instance(self):
		"""Explodes the specified block instance."""
		return self._instance.ExplodeSketchBlockInstance

	@explode_sketch_block_instance.setter
	def explode_sketch_block_instance(self, value):
		"""Explodes the specified block instance."""
		self._instance.ExplodeSketchBlockInstance = value

	@property
	def fully_define_sketch(self):
		"""Fully defines a sketch."""
		return self._instance.FullyDefineSketch

	@fully_define_sketch.setter
	def fully_define_sketch(self, value):
		"""Fully defines a sketch."""
		self._instance.FullyDefineSketch = value

	@property
	def get_dynamic_mirror(self):
		"""Gets whether dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline, is enabled."""
		return self._instance.GetDynamicMirror

	@get_dynamic_mirror.setter
	def get_dynamic_mirror(self, value):
		"""Gets whether dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline, is enabled."""
		self._instance.GetDynamicMirror = value

	@property
	def get_sketch_block_definition_count(self):
		"""Gets the number of block definitions in the model."""
		return self._instance.GetSketchBlockDefinitionCount

	@get_sketch_block_definition_count.setter
	def get_sketch_block_definition_count(self, value):
		"""Gets the number of block definitions in the model."""
		self._instance.GetSketchBlockDefinitionCount = value

	@property
	def get_sketch_block_definitions(self):
		"""Gets all of the block definitions."""
		return self._instance.GetSketchBlockDefinitions

	@get_sketch_block_definitions.setter
	def get_sketch_block_definitions(self, value):
		"""Gets all of the block definitions."""
		self._instance.GetSketchBlockDefinitions = value

	@property
	def i_create_spline(self):
		"""Creates a spline passing through the given points."""
		return self._instance.ICreateSpline2

	@i_create_spline.setter
	def i_create_spline(self, value):
		"""Creates a spline passing through the given points."""
		self._instance.ICreateSpline2 = value

	@property
	def i_create_spline_by_eqn_params(self):
		"""Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector."""
		return self._instance.ICreateSplineByEqnParams

	@i_create_spline_by_eqn_params.setter
	def i_create_spline_by_eqn_params(self, value):
		"""Creates a B-curve from B-spline data; that is, a set of B-spline vertices (control points) and a knot vector."""
		self._instance.ICreateSplineByEqnParams = value

	@property
	def i_create_splines_by_eqn_params(self):
		"""Creates one or more spline segments using the B-curve parameters provided."""
		return self._instance.ICreateSplinesByEqnParams

	@i_create_splines_by_eqn_params.setter
	def i_create_splines_by_eqn_params(self, value):
		"""Creates one or more spline segments using the B-curve parameters provided."""
		self._instance.ICreateSplinesByEqnParams = value

	@property
	def i_get_sketch_block_definitions(self):
		"""Gets all of the block definitions."""
		return self._instance.IGetSketchBlockDefinitions

	@i_get_sketch_block_definitions.setter
	def i_get_sketch_block_definitions(self, value):
		"""Gets all of the block definitions."""
		self._instance.IGetSketchBlockDefinitions = value

	@property
	def insert_d_sketch(self):
		"""Inserts a new 3D sketch in a model or closes the active sketch."""
		return self._instance.Insert3DSketch

	@insert_d_sketch.setter
	def insert_d_sketch(self, value):
		"""Inserts a new 3D sketch in a model or closes the active sketch."""
		self._instance.Insert3DSketch = value

	@property
	def insert_explode_line_sketch(self):
		"""Inserts or closes an explode line sketch in an exploded view."""
		return self._instance.InsertExplodeLineSketch

	@insert_explode_line_sketch.setter
	def insert_explode_line_sketch(self, value):
		"""Inserts or closes an explode line sketch in an exploded view."""
		self._instance.InsertExplodeLineSketch = value

	@property
	def insert_sketch(self):
		"""Inserts a new sketch in the current part or assembly document."""
		return self._instance.InsertSketch

	@insert_sketch.setter
	def insert_sketch(self, value):
		"""Inserts a new sketch in the current part or assembly document."""
		self._instance.InsertSketch = value

	@property
	def insert_sketch_block_instance(self):
		"""Inserts a block instance at the specified location using the block definition."""
		return self._instance.InsertSketchBlockInstance

	@insert_sketch_block_instance.setter
	def insert_sketch_block_instance(self, value):
		"""Inserts a block instance at the specified location using the block definition."""
		self._instance.InsertSketchBlockInstance = value

	@property
	def insert_sketch_picture(self):
		"""Inserts a picture on the current drawing sketch."""
		return self._instance.InsertSketchPicture2

	@insert_sketch_picture.setter
	def insert_sketch_picture(self, value):
		"""Inserts a picture on the current drawing sketch."""
		self._instance.InsertSketchPicture2 = value

	@property
	def intersect_curves(self):
		"""Creates a sketched intersection curve."""
		return self._instance.IntersectCurves

	@intersect_curves.setter
	def intersect_curves(self, value):
		"""Creates a sketched intersection curve."""
		self._instance.IntersectCurves = value

	@property
	def make_sketch_block_from_file(self):
		"""Creates a block definition using the specified file."""
		return self._instance.MakeSketchBlockFromFile

	@make_sketch_block_from_file.setter
	def make_sketch_block_from_file(self, value):
		"""Creates a block definition using the specified file."""
		self._instance.MakeSketchBlockFromFile = value

	@property
	def make_sketch_block_from_selected(self):
		"""Creates a block definition at the specified location from the selected entities."""
		return self._instance.MakeSketchBlockFromSelected

	@make_sketch_block_from_selected.setter
	def make_sketch_block_from_selected(self, value):
		"""Creates a block definition at the specified location from the selected entities."""
		self._instance.MakeSketchBlockFromSelected = value

	@property
	def make_sketch_block_from_sketch(self):
		"""Creates a block definition at the specified location using all of the sketch entities in the active sketch."""
		return self._instance.MakeSketchBlockFromSketch

	@make_sketch_block_from_sketch.setter
	def make_sketch_block_from_sketch(self, value):
		"""Creates a block definition at the specified location using all of the sketch entities in the active sketch."""
		self._instance.MakeSketchBlockFromSketch = value

	@property
	def make_sketch_chain(self):
		"""Creates a sketch path using the selected entities."""
		return self._instance.MakeSketchChain

	@make_sketch_chain.setter
	def make_sketch_chain(self, value):
		"""Creates a sketch path using the selected entities."""
		self._instance.MakeSketchChain = value

	@property
	def perimeter_circle(self):
		"""Draws a 3-point perimeter arc."""
		return self._instance.PerimeterCircle

	@perimeter_circle.setter
	def perimeter_circle(self, value):
		"""Draws a 3-point perimeter arc."""
		self._instance.PerimeterCircle = value

	@property
	def reverse_end_point_tangent(self):
		"""Reverses the end point tangent direction of splines and arcs."""
		return self._instance.ReverseEndPointTangent

	@reverse_end_point_tangent.setter
	def reverse_end_point_tangent(self, value):
		"""Reverses the end point tangent direction of splines and arcs."""
		self._instance.ReverseEndPointTangent = value

	@property
	def rotate_or_copy_d_about_vector(self):
		"""Rotates, and optionally copies, the selected 3D sketch entities about the specified vector."""
		return self._instance.RotateOrCopy3DAboutVector

	@rotate_or_copy_d_about_vector.setter
	def rotate_or_copy_d_about_vector(self, value):
		"""Rotates, and optionally copies, the selected 3D sketch entities about the specified vector."""
		self._instance.RotateOrCopy3DAboutVector = value

	@property
	def rotate_or_copy_d_about_x_y_z(self):
		"""Rotates, and optionally copies, the selected 3D sketch entities about the specified x, y, and z coordinates."""
		return self._instance.RotateOrCopy3DAboutXYZ

	@rotate_or_copy_d_about_x_y_z.setter
	def rotate_or_copy_d_about_x_y_z(self, value):
		"""Rotates, and optionally copies, the selected 3D sketch entities about the specified x, y, and z coordinates."""
		self._instance.RotateOrCopy3DAboutXYZ = value

	@property
	def set_dynamic_mirror(self):
		"""Enables or disables dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline."""
		return self._instance.SetDynamicMirror

	@set_dynamic_mirror.setter
	def set_dynamic_mirror(self, value):
		"""Enables or disables dynamic sketch mirroring, which is the automatic mirroring of newly created sketch entities about a selected centerline."""
		self._instance.SetDynamicMirror = value

	@property
	def set_grid_options(self):
		"""Sets the options for the grid."""
		return self._instance.SetGridOptions

	@set_grid_options.setter
	def set_grid_options(self, value):
		"""Sets the options for the grid."""
		self._instance.SetGridOptions = value

	@property
	def sketch_extend(self):
		"""Adds to the length of the selected sketch entity (i.e., line, centerline, or arc) to meet the nearest sketch entity."""
		return self._instance.SketchExtend

	@sketch_extend.setter
	def sketch_extend(self, value):
		"""Adds to the length of the selected sketch entity (i.e., line, centerline, or arc) to meet the nearest sketch entity."""
		self._instance.SketchExtend = value

	@property
	def sketch_offset(self):
		"""Offsets the selected sketch entities."""
		return self._instance.SketchOffset2

	@sketch_offset.setter
	def sketch_offset(self, value):
		"""Offsets the selected sketch entities."""
		self._instance.SketchOffset2 = value

	@property
	def sketch_replace(self):
		"""Replaces a sketch entity in a model with another sketch entity, preserving all references."""
		return self._instance.SketchReplace

	@sketch_replace.setter
	def sketch_replace(self, value):
		"""Replaces a sketch entity in a model with another sketch entity, preserving all references."""
		self._instance.SketchReplace = value

	@property
	def sketch_trim(self):
		"""Trims the selected sketch entities."""
		return self._instance.SketchTrim

	@sketch_trim.setter
	def sketch_trim(self, value):
		"""Trims the selected sketch entities."""
		self._instance.SketchTrim = value

	@property
	def sketch_use_edge(self):
		"""Creates sketch entities on a sketch plane by projecting selected edges, loops, faces, curves, and external sketch contours."""
		return self._instance.SketchUseEdge3

	@sketch_use_edge.setter
	def sketch_use_edge(self, value):
		"""Creates sketch entities on a sketch plane by projecting selected edges, loops, faces, curves, and external sketch contours."""
		self._instance.SketchUseEdge3 = value

	@property
	def split_closed_segment(self):
		"""Splits the selected closed sketch segment into two sketch segments."""
		return self._instance.SplitClosedSegment

	@split_closed_segment.setter
	def split_closed_segment(self, value):
		"""Splits the selected closed sketch segment into two sketch segments."""
		self._instance.SplitClosedSegment = value

	@property
	def split_open_segment(self):
		"""Splits the selected open sketch segment into two sketch segments."""
		return self._instance.SplitOpenSegment

	@split_open_segment.setter
	def split_open_segment(self, value):
		"""Splits the selected open sketch segment into two sketch segments."""
		self._instance.SplitOpenSegment = value

