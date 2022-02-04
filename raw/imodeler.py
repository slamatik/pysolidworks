# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html
class IModeler:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def general_topology(self):
		"""Gets or sets the Parasolid option to create general (non-manifold) bodies."""
		return self._instance.GeneralTopology

	@general_topology.setter
	def general_topology(self, value):
		"""Gets or sets the Parasolid option to create general (non-manifold) bodies."""
		self._instance.GeneralTopology = value

	@property
	def check_interference(self):
		"""Checks for interferences among the specified bodies in a part."""
		return self._instance.CheckInterference3

	@check_interference.setter
	def check_interference(self, value):
		"""Checks for interferences among the specified bodies in a part."""
		self._instance.CheckInterference3 = value

	@property
	def check_interference_between_two_bodies(self):
		"""Checks for interference between the specified bodies in an assembly."""
		return self._instance.CheckInterferenceBetweenTwoBodies

	@check_interference_between_two_bodies.setter
	def check_interference_between_two_bodies(self, value):
		"""Checks for interference between the specified bodies in an assembly."""
		self._instance.CheckInterferenceBetweenTwoBodies = value

	@property
	def copy_wizard_hole(self):
		"""Copies hole data from the source hole to the destination hole."""
		return self._instance.CopyWizardHole

	@copy_wizard_hole.setter
	def copy_wizard_hole(self, value):
		"""Copies hole data from the source hole to the destination hole."""
		self._instance.CopyWizardHole = value

	@property
	def create_arc(self):
		"""Creates an arc."""
		return self._instance.CreateArc

	@create_arc.setter
	def create_arc(self, value):
		"""Creates an arc."""
		self._instance.CreateArc = value

	@property
	def create_bodies_from_sheets(self):
		"""Sews sheets to make sheet (surface) or solid bodies."""
		return self._instance.CreateBodiesFromSheets2

	@create_bodies_from_sheets.setter
	def create_bodies_from_sheets(self, value):
		"""Sews sheets to make sheet (surface) or solid bodies."""
		self._instance.CreateBodiesFromSheets2 = value

	@property
	def create_body_from_box(self):
		"""Creates a temporary body from the specified box dimensions."""
		return self._instance.CreateBodyFromBox3

	@create_body_from_box.setter
	def create_body_from_box(self, value):
		"""Creates a temporary body from the specified box dimensions."""
		self._instance.CreateBodyFromBox3 = value

	@property
	def create_body_from_cone(self):
		"""Creates a temporary body from cone dimensions."""
		return self._instance.CreateBodyFromCone

	@create_body_from_cone.setter
	def create_body_from_cone(self, value):
		"""Creates a temporary body from cone dimensions."""
		self._instance.CreateBodyFromCone = value

	@property
	def create_body_from_cyl(self):
		"""Creates a temporary body from cylinder dimensions."""
		return self._instance.CreateBodyFromCyl

	@create_body_from_cyl.setter
	def create_body_from_cyl(self, value):
		"""Creates a temporary body from cylinder dimensions."""
		self._instance.CreateBodyFromCyl = value

	@property
	def create_body_from_faces(self):
		"""Creates a temporary body from a list of faces."""
		return self._instance.CreateBodyFromFaces2

	@create_body_from_faces.setter
	def create_body_from_faces(self, value):
		"""Creates a temporary body from a list of faces."""
		self._instance.CreateBodyFromFaces2 = value

	@property
	def create_brep_body(self):
		"""Creates a temporary body from BREP (boundary representation) data."""
		return self._instance.CreateBrepBody3

	@create_brep_body.setter
	def create_brep_body(self, value):
		"""Creates a temporary body from BREP (boundary representation) data."""
		self._instance.CreateBrepBody3 = value

	@property
	def create_bspline_curve(self):
		"""Creates a b-spline curve."""
		return self._instance.CreateBsplineCurve

	@create_bspline_curve.setter
	def create_bspline_curve(self, value):
		"""Creates a b-spline curve."""
		self._instance.CreateBsplineCurve = value

	@property
	def create_bspline_surface(self):
		"""Creates a b-spline surface."""
		return self._instance.CreateBsplineSurface

	@create_bspline_surface.setter
	def create_bspline_surface(self, value):
		"""Creates a b-spline surface."""
		self._instance.CreateBsplineSurface = value

	@property
	def create_conical_surface(self):
		"""Creates an untrimmed conical surface."""
		return self._instance.CreateConicalSurface2

	@create_conical_surface.setter
	def create_conical_surface(self, value):
		"""Creates an untrimmed conical surface."""
		self._instance.CreateConicalSurface2 = value

	@property
	def create_coons_b_surface(self):
		"""Creates a coons b-surface using the four specified boundary curves."""
		return self._instance.CreateCoonsBSurface

	@create_coons_b_surface.setter
	def create_coons_b_surface(self, value):
		"""Creates a coons b-surface using the four specified boundary curves."""
		self._instance.CreateCoonsBSurface = value

	@property
	def create_cylindrical_surface(self):
		"""Creates an untrimmed cylindrical surface."""
		return self._instance.CreateCylindricalSurface2

	@create_cylindrical_surface.setter
	def create_cylindrical_surface(self, value):
		"""Creates an untrimmed cylindrical surface."""
		self._instance.CreateCylindricalSurface2 = value

	@property
	def create_ellipse(self):
		"""Creates a temporary elliptical curve."""
		return self._instance.CreateEllipse

	@create_ellipse.setter
	def create_ellipse(self, value):
		"""Creates a temporary elliptical curve."""
		self._instance.CreateEllipse = value

	@property
	def create_extruded_body(self):
		"""Creates a temporary extruded body."""
		return self._instance.CreateExtrudedBody

	@create_extruded_body.setter
	def create_extruded_body(self, value):
		"""Creates a temporary extruded body."""
		self._instance.CreateExtrudedBody = value

	@property
	def create_extrusion_surface(self):
		"""Creates an extruded surface."""
		return self._instance.CreateExtrusionSurface

	@create_extrusion_surface.setter
	def create_extrusion_surface(self, value):
		"""Creates an extruded surface."""
		self._instance.CreateExtrusionSurface = value

	@property
	def create_line(self):
		"""Creates a line."""
		return self._instance.CreateLine

	@create_line.setter
	def create_line(self, value):
		"""Creates a line."""
		self._instance.CreateLine = value

	@property
	def create_loft_body(self):
		"""Creates a loft body using the specified profiles, guide curves, and centerline."""
		return self._instance.CreateLoftBody2

	@create_loft_body.setter
	def create_loft_body(self, value):
		"""Creates a loft body using the specified profiles, guide curves, and centerline."""
		self._instance.CreateLoftBody2 = value

	@property
	def create_loft_surface(self):
		"""Creates a loft surface."""
		return self._instance.CreateLoftSurface

	@create_loft_surface.setter
	def create_loft_surface(self, value):
		"""Creates a loft surface."""
		self._instance.CreateLoftSurface = value

	@property
	def create_offset_surface(self):
		"""Creates a surface that is offset from an existing surface."""
		return self._instance.CreateOffsetSurface

	@create_offset_surface.setter
	def create_offset_surface(self, value):
		"""Creates a surface that is offset from an existing surface."""
		self._instance.CreateOffsetSurface = value

	@property
	def create_p_curve(self):
		"""Creates a pcurve."""
		return self._instance.CreatePCurve

	@create_p_curve.setter
	def create_p_curve(self, value):
		"""Creates a pcurve."""
		self._instance.CreatePCurve = value

	@property
	def create_planar_surface(self):
		"""Creates a new infinite planar surface."""
		return self._instance.CreatePlanarSurface2

	@create_planar_surface.setter
	def create_planar_surface(self, value):
		"""Creates a new infinite planar surface."""
		self._instance.CreatePlanarSurface2 = value

	@property
	def create_ruled_surface(self):
		"""Creates a ruled surface from the curves."""
		return self._instance.CreateRuledSurface

	@create_ruled_surface.setter
	def create_ruled_surface(self, value):
		"""Creates a ruled surface from the curves."""
		self._instance.CreateRuledSurface = value

	@property
	def create_ruled_surface_from_edge(self):
		"""Creates a ruled surface using the specified edges and returns a surface body."""
		return self._instance.CreateRuledSurfaceFromEdge

	@create_ruled_surface_from_edge.setter
	def create_ruled_surface_from_edge(self, value):
		"""Creates a ruled surface using the specified edges and returns a surface body."""
		self._instance.CreateRuledSurfaceFromEdge = value

	@property
	def create_sheet_from_faces(self):
		"""Creates a sheet (surface) body from connected faces."""
		return self._instance.CreateSheetFromFaces

	@create_sheet_from_faces.setter
	def create_sheet_from_faces(self, value):
		"""Creates a sheet (surface) body from connected faces."""
		self._instance.CreateSheetFromFaces = value

	@property
	def create_sheet_from_surface(self):
		"""Creates a sheet (surface) body from a surface."""
		return self._instance.CreateSheetFromSurface

	@create_sheet_from_surface.setter
	def create_sheet_from_surface(self, value):
		"""Creates a sheet (surface) body from a surface."""
		self._instance.CreateSheetFromSurface = value

	@property
	def create_spherical_surface(self):
		"""Creates an untrimmed spherical surface."""
		return self._instance.CreateSphericalSurface2

	@create_spherical_surface.setter
	def create_spherical_surface(self, value):
		"""Creates an untrimmed spherical surface."""
		self._instance.CreateSphericalSurface2 = value

	@property
	def create_spring(self):
		"""Creates the geometry for a spring."""
		return self._instance.CreateSpring

	@create_spring.setter
	def create_spring(self, value):
		"""Creates the geometry for a spring."""
		self._instance.CreateSpring = value

	@property
	def create_swept_body(self):
		"""Creates a swept body."""
		return self._instance.CreateSweptBody

	@create_swept_body.setter
	def create_swept_body(self, value):
		"""Creates a swept body."""
		self._instance.CreateSweptBody = value

	@property
	def create_swept_surface(self):
		"""Creates a swept surface from a curve."""
		return self._instance.CreateSweptSurface

	@create_swept_surface.setter
	def create_swept_surface(self, value):
		"""Creates a swept surface from a curve."""
		self._instance.CreateSweptSurface = value

	@property
	def create_toroidal_surface(self):
		"""Creates an untrimmed toroidal surface from the specified arguments."""
		return self._instance.CreateToroidalSurface

	@create_toroidal_surface.setter
	def create_toroidal_surface(self, value):
		"""Creates an untrimmed toroidal surface from the specified arguments."""
		self._instance.CreateToroidalSurface = value

	@property
	def create_wire_body(self):
		"""Creates a wire body from the input entities, which can be edges or curves."""
		return self._instance.CreateWireBody

	@create_wire_body.setter
	def create_wire_body(self, value):
		"""Creates a wire body from the input entities, which can be edges or curves."""
		self._instance.CreateWireBody = value

	@property
	def delete_faces_from_sheet_body(self):
		"""Deletes the unused faces of the sheet body."""
		return self._instance.DeleteFacesFromSheetBody

	@delete_faces_from_sheet_body.setter
	def delete_faces_from_sheet_body(self, value):
		"""Deletes the unused faces of the sheet body."""
		self._instance.DeleteFacesFromSheetBody = value

	@property
	def find_two_edge_max_deviation(self):
		"""Finds the maximum distance between two edges."""
		return self._instance.FindTwoEdgeMaxDeviation

	@find_two_edge_max_deviation.setter
	def find_two_edge_max_deviation(self, value):
		"""Finds the maximum distance between two edges."""
		self._instance.FindTwoEdgeMaxDeviation = value

	@property
	def get_body_outline(self):
		"""Gets the curves that form the outline of a body."""
		return self._instance.GetBodyOutline2

	@get_body_outline.setter
	def get_body_outline(self, value):
		"""Gets the curves that form the outline of a body."""
		self._instance.GetBodyOutline2 = value

	@property
	def get_init_knit_gap_width(self):
		"""Gets the initial gap bound width for knitting a body."""
		return self._instance.GetInitKnitGapWidth

	@get_init_knit_gap_width.setter
	def get_init_knit_gap_width(self, value):
		"""Gets the initial gap bound width for knitting a body."""
		self._instance.GetInitKnitGapWidth = value

	@property
	def get_manifold_bodies_count(self):
		"""Gets the number of manifold bodies created from the specified non-manifold body."""
		return self._instance.GetManifoldBodiesCount

	@get_manifold_bodies_count.setter
	def get_manifold_bodies_count(self, value):
		"""Gets the number of manifold bodies created from the specified non-manifold body."""
		self._instance.GetManifoldBodiesCount = value

	@property
	def get_tolerance_value(self):
		"""Gets the current tolerance value of the given tolerance ID."""
		return self._instance.GetToleranceValue

	@get_tolerance_value.setter
	def get_tolerance_value(self, value):
		"""Gets the current tolerance value of the given tolerance ID."""
		self._instance.GetToleranceValue = value

	@property
	def i_check_interference(self):
		"""Checks the interference among the specified bodies."""
		return self._instance.ICheckInterference3

	@i_check_interference.setter
	def i_check_interference(self, value):
		"""Checks the interference among the specified bodies."""
		self._instance.ICheckInterference3 = value

	@property
	def i_check_interference_count(self):
		"""Checks interference among the specified bodies and returns the number of interferences."""
		return self._instance.ICheckInterferenceCount3

	@i_check_interference_count.setter
	def i_check_interference_count(self, value):
		"""Checks interference among the specified bodies and returns the number of interferences."""
		self._instance.ICheckInterferenceCount3 = value

	@property
	def i_copy_wizard_hole(self):
		"""Copies hole data from the source hole to the destination hole."""
		return self._instance.ICopyWizardHole

	@i_copy_wizard_hole.setter
	def i_copy_wizard_hole(self, value):
		"""Copies hole data from the source hole to the destination hole."""
		self._instance.ICopyWizardHole = value

	@property
	def i_create_arc(self):
		"""Creates an arc."""
		return self._instance.ICreateArc

	@i_create_arc.setter
	def i_create_arc(self, value):
		"""Creates an arc."""
		self._instance.ICreateArc = value

	@property
	def i_create_bodies_from_sheets(self):
		"""Sews sheets to make a sheet (surface) or solid bodies."""
		return self._instance.ICreateBodiesFromSheets2

	@i_create_bodies_from_sheets.setter
	def i_create_bodies_from_sheets(self, value):
		"""Sews sheets to make a sheet (surface) or solid bodies."""
		self._instance.ICreateBodiesFromSheets2 = value

	@property
	def i_create_body_from_cone(self):
		"""Creates a temporary body from cone dimensions."""
		return self._instance.ICreateBodyFromCone2

	@i_create_body_from_cone.setter
	def i_create_body_from_cone(self, value):
		"""Creates a temporary body from cone dimensions."""
		self._instance.ICreateBodyFromCone2 = value

	@property
	def i_create_body_from_cyl(self):
		"""Creates a temporary body from cylinder dimensions."""
		return self._instance.ICreateBodyFromCyl2

	@i_create_body_from_cyl.setter
	def i_create_body_from_cyl(self, value):
		"""Creates a temporary body from cylinder dimensions."""
		self._instance.ICreateBodyFromCyl2 = value

	@property
	def i_create_body_from_faces(self):
		"""Creates a temporary body from a list of faces."""
		return self._instance.ICreateBodyFromFaces3

	@i_create_body_from_faces.setter
	def i_create_body_from_faces(self, value):
		"""Creates a temporary body from a list of faces."""
		self._instance.ICreateBodyFromFaces3 = value

	@property
	def i_create_brep_body(self):
		"""Creates a temporary body from BREP (boundary representation) data."""
		return self._instance.ICreateBrepBody3

	@i_create_brep_body.setter
	def i_create_brep_body(self, value):
		"""Creates a temporary body from BREP (boundary representation) data."""
		self._instance.ICreateBrepBody3 = value

	@property
	def i_create_bspline_curve(self):
		"""Creates a b-spline curve."""
		return self._instance.ICreateBsplineCurve

	@i_create_bspline_curve.setter
	def i_create_bspline_curve(self, value):
		"""Creates a b-spline curve."""
		self._instance.ICreateBsplineCurve = value

	@property
	def i_create_bspline_surface(self):
		"""Creates a b-spline surface."""
		return self._instance.ICreateBsplineSurface

	@i_create_bspline_surface.setter
	def i_create_bspline_surface(self, value):
		"""Creates a b-spline surface."""
		self._instance.ICreateBsplineSurface = value

	@property
	def i_create_conical_surface(self):
		"""Creates an untrimmed conical surface."""
		return self._instance.ICreateConicalSurface2

	@i_create_conical_surface.setter
	def i_create_conical_surface(self, value):
		"""Creates an untrimmed conical surface."""
		self._instance.ICreateConicalSurface2 = value

	@property
	def i_create_cylindrical_surface(self):
		"""Creates an untrimmed cylindrical surface."""
		return self._instance.ICreateCylindricalSurface2

	@i_create_cylindrical_surface.setter
	def i_create_cylindrical_surface(self, value):
		"""Creates an untrimmed cylindrical surface."""
		self._instance.ICreateCylindricalSurface2 = value

	@property
	def i_create_ellipse(self):
		"""Creates a temporary elliptical curve."""
		return self._instance.ICreateEllipse

	@i_create_ellipse.setter
	def i_create_ellipse(self, value):
		"""Creates a temporary elliptical curve."""
		self._instance.ICreateEllipse = value

	@property
	def i_create_extrusion_surface(self):
		"""Creates an extruded surface."""
		return self._instance.ICreateExtrusionSurface

	@i_create_extrusion_surface.setter
	def i_create_extrusion_surface(self, value):
		"""Creates an extruded surface."""
		self._instance.ICreateExtrusionSurface = value

	@property
	def i_create_line(self):
		"""Creates a line."""
		return self._instance.ICreateLine

	@i_create_line.setter
	def i_create_line(self, value):
		"""Creates a line."""
		self._instance.ICreateLine = value

	@property
	def i_create_loft_surface(self):
		"""Creates a loft surface."""
		return self._instance.ICreateLoftSurface

	@i_create_loft_surface.setter
	def i_create_loft_surface(self, value):
		"""Creates a loft surface."""
		self._instance.ICreateLoftSurface = value

	@property
	def i_create_offset_surface(self):
		"""Creates a surface that is offset from an existing surface."""
		return self._instance.ICreateOffsetSurface

	@i_create_offset_surface.setter
	def i_create_offset_surface(self, value):
		"""Creates a surface that is offset from an existing surface."""
		self._instance.ICreateOffsetSurface = value

	@property
	def i_create_p_curve(self):
		"""Creates a pcurve."""
		return self._instance.ICreatePCurve

	@i_create_p_curve.setter
	def i_create_p_curve(self, value):
		"""Creates a pcurve."""
		self._instance.ICreatePCurve = value

	@property
	def i_create_planar_surface(self):
		"""Creates a new infinite planar surface."""
		return self._instance.ICreatePlanarSurface2

	@i_create_planar_surface.setter
	def i_create_planar_surface(self, value):
		"""Creates a new infinite planar surface."""
		self._instance.ICreatePlanarSurface2 = value

	@property
	def i_create_ruled_surface(self):
		"""Creates a ruled surface from the curves."""
		return self._instance.ICreateRuledSurface

	@i_create_ruled_surface.setter
	def i_create_ruled_surface(self, value):
		"""Creates a ruled surface from the curves."""
		self._instance.ICreateRuledSurface = value

	@property
	def i_create_ruled_surface_from_edge(self):
		"""Creates a ruled surface using the specified edges and returns a surface body."""
		return self._instance.ICreateRuledSurfaceFromEdge

	@i_create_ruled_surface_from_edge.setter
	def i_create_ruled_surface_from_edge(self, value):
		"""Creates a ruled surface using the specified edges and returns a surface body."""
		self._instance.ICreateRuledSurfaceFromEdge = value

	@property
	def i_create_sheet_from_faces(self):
		"""Creates a sheet (surface) body from connected faces."""
		return self._instance.ICreateSheetFromFaces

	@i_create_sheet_from_faces.setter
	def i_create_sheet_from_faces(self, value):
		"""Creates a sheet (surface) body from connected faces."""
		self._instance.ICreateSheetFromFaces = value

	@property
	def i_create_sheet_from_surface(self):
		"""Creates a sheet (surface) body from a surface."""
		return self._instance.ICreateSheetFromSurface2

	@i_create_sheet_from_surface.setter
	def i_create_sheet_from_surface(self, value):
		"""Creates a sheet (surface) body from a surface."""
		self._instance.ICreateSheetFromSurface2 = value

	@property
	def i_create_spherical_surface(self):
		"""Creates an untrimmed spherical surface."""
		return self._instance.ICreateSphericalSurface2

	@i_create_spherical_surface.setter
	def i_create_spherical_surface(self, value):
		"""Creates an untrimmed spherical surface."""
		self._instance.ICreateSphericalSurface2 = value

	@property
	def i_create_swept_surface(self):
		"""Creates a swept surface from a curve."""
		return self._instance.ICreateSweptSurface

	@i_create_swept_surface.setter
	def i_create_swept_surface(self, value):
		"""Creates a swept surface from a curve."""
		self._instance.ICreateSweptSurface = value

	@property
	def i_create_toroidal_surface(self):
		"""Creates an untrimmed toroidal surface from the specified arguments."""
		return self._instance.ICreateToroidalSurface

	@i_create_toroidal_surface.setter
	def i_create_toroidal_surface(self, value):
		"""Creates an untrimmed toroidal surface from the specified arguments."""
		self._instance.ICreateToroidalSurface = value

	@property
	def i_create_wire_body(self):
		"""Creates a wire body from the input entities, which can be edges or curves."""
		return self._instance.ICreateWireBody

	@i_create_wire_body.setter
	def i_create_wire_body(self, value):
		"""Creates a wire body from the input entities, which can be edges or curves."""
		self._instance.ICreateWireBody = value

	@property
	def i_delete_faces_from_sheet_body(self):
		"""Deletes the unused faces of the sheet body."""
		return self._instance.IDeleteFacesFromSheetBody

	@i_delete_faces_from_sheet_body.setter
	def i_delete_faces_from_sheet_body(self, value):
		"""Deletes the unused faces of the sheet body."""
		self._instance.IDeleteFacesFromSheetBody = value

	@property
	def i_find_two_edge_max_deviation(self):
		"""Finds the maximum distance between two edges."""
		return self._instance.IFindTwoEdgeMaxDeviation

	@i_find_two_edge_max_deviation.setter
	def i_find_two_edge_max_deviation(self, value):
		"""Finds the maximum distance between two edges."""
		self._instance.IFindTwoEdgeMaxDeviation = value

	@property
	def i_imprinting_faces(self):
		"""Imprints the specified tool faces onto the specified target faces."""
		return self._instance.IImprintingFaces

	@i_imprinting_faces.setter
	def i_imprinting_faces(self, value):
		"""Imprints the specified tool faces onto the specified target faces."""
		self._instance.IImprintingFaces = value

	@property
	def i_imprinting_faces_count(self):
		"""Gets the number of imprinted edges and vertices in the model."""
		return self._instance.IImprintingFacesCount2

	@i_imprinting_faces_count.setter
	def i_imprinting_faces_count(self, value):
		"""Gets the number of imprinted edges and vertices in the model."""
		self._instance.IImprintingFacesCount2 = value

	@property
	def i_make_manifold_bodies(self):
		"""Creates manifold bodies from the specified non-manifold body."""
		return self._instance.IMakeManifoldBodies

	@i_make_manifold_bodies.setter
	def i_make_manifold_bodies(self, value):
		"""Creates manifold bodies from the specified non-manifold body."""
		self._instance.IMakeManifoldBodies = value

	@property
	def i_merge_curves(self):
		"""Merges multiple curves into one curve."""
		return self._instance.IMergeCurves

	@i_merge_curves.setter
	def i_merge_curves(self, value):
		"""Merges multiple curves into one curve."""
		self._instance.IMergeCurves = value

	@property
	def imprinting_faces(self):
		"""Imprints the specified tool faces onto the specified target faces."""
		return self._instance.ImprintingFaces

	@imprinting_faces.setter
	def imprinting_faces(self, value):
		"""Imprints the specified tool faces onto the specified target faces."""
		self._instance.ImprintingFaces = value

	@property
	def i_replace_surfaces(self):
		"""Replaces the surfaces of the given faces."""
		return self._instance.IReplaceSurfaces2

	@i_replace_surfaces.setter
	def i_replace_surfaces(self, value):
		"""Replaces the surfaces of the given faces."""
		self._instance.IReplaceSurfaces2 = value

	@property
	def i_restore(self):
		"""Restores a temporary body object from the specified stream."""
		return self._instance.IRestore2

	@i_restore.setter
	def i_restore(self, value):
		"""Restores a temporary body object from the specified stream."""
		self._instance.IRestore2 = value

	@property
	def i_split_face_on_param(self):
		"""Splits and retrieves the faces on the U or V parameter."""
		return self._instance.ISplitFaceOnParam2

	@i_split_face_on_param.setter
	def i_split_face_on_param(self, value):
		"""Splits and retrieves the faces on the U or V parameter."""
		self._instance.ISplitFaceOnParam2 = value

	@property
	def i_split_face_on_param_count(self):
		"""Sets up and counts the number of new faces split on the U or V parameter."""
		return self._instance.ISplitFaceOnParamCount2

	@i_split_face_on_param_count.setter
	def i_split_face_on_param_count(self, value):
		"""Sets up and counts the number of new faces split on the U or V parameter."""
		self._instance.ISplitFaceOnParamCount2 = value

	@property
	def make_manifold_bodies(self):
		"""Creates manifold bodies from the specified non-manifold body."""
		return self._instance.MakeManifoldBodies

	@make_manifold_bodies.setter
	def make_manifold_bodies(self, value):
		"""Creates manifold bodies from the specified non-manifold body."""
		self._instance.MakeManifoldBodies = value

	@property
	def merge_curves(self):
		"""Merges multiple curves into one curve."""
		return self._instance.MergeCurves

	@merge_curves.setter
	def merge_curves(self, value):
		"""Merges multiple curves into one curve."""
		self._instance.MergeCurves = value

	@property
	def project_curve_on_surface(self):
		"""Projects a curve on a surface."""
		return self._instance.ProjectCurveOnSurface

	@project_curve_on_surface.setter
	def project_curve_on_surface(self, value):
		"""Projects a curve on a surface."""
		self._instance.ProjectCurveOnSurface = value

	@property
	def replace_surfaces(self):
		"""Replaces the surfaces of the given faces."""
		return self._instance.ReplaceSurfaces

	@replace_surfaces.setter
	def replace_surfaces(self, value):
		"""Replaces the surfaces of the given faces."""
		self._instance.ReplaceSurfaces = value

	@property
	def restore(self):
		"""Restores a temporary body object from the specified stream."""
		return self._instance.Restore

	@restore.setter
	def restore(self, value):
		"""Restores a temporary body object from the specified stream."""
		self._instance.Restore = value

	@property
	def set_init_knit_gap_width(self):
		"""Sets the initial gap bound width for sewing a body. Call this method before calling any calls that attempt to knit a body; for example, IBody2::CreateBodyFromSurfaces."""
		return self._instance.SetInitKnitGapWidth

	@set_init_knit_gap_width.setter
	def set_init_knit_gap_width(self, value):
		"""Sets the initial gap bound width for sewing a body. Call this method before calling any calls that attempt to knit a body; for example, IBody2::CreateBodyFromSurfaces."""
		self._instance.SetInitKnitGapWidth = value

	@property
	def set_tolerance_value(self):
		"""Sets tolerances governing geometry output."""
		return self._instance.SetToleranceValue

	@set_tolerance_value.setter
	def set_tolerance_value(self, value):
		"""Sets tolerances governing geometry output."""
		self._instance.SetToleranceValue = value

	@property
	def split_face_on_param(self):
		"""Splits and retrieves the faces on the U or V parameter"""
		return self._instance.SplitFaceOnParam

	@split_face_on_param.setter
	def split_face_on_param(self, value):
		"""Splits and retrieves the faces on the U or V parameter"""
		self._instance.SplitFaceOnParam = value

	@property
	def thicken_sheet(self):
		"""Thickens a sheet body."""
		return self._instance.ThickenSheet

	@thicken_sheet.setter
	def thicken_sheet(self, value):
		"""Thickens a sheet body."""
		self._instance.ThickenSheet = value

	@property
	def unset_tolerances(self):
		"""Sets the tolerances back to system settings."""
		return self._instance.UnsetTolerances

	@unset_tolerances.setter
	def unset_tolerances(self, value):
		"""Sets the tolerances back to system settings."""
		self._instance.UnsetTolerances = value

