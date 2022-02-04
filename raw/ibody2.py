# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html
class IBody2:
	def __init__(self, parent=None):
		self._instance = parent

	def check(self):
		"""Gets whether the body is a valid and returns an IFaultEntity object if any faults exist."""
		# return self._instance.Check3
		raise NotImplemented

	@property
	def disable_display(self):
		"""Gets or sets whether to hide or show this body."""
		return self._instance.DisableDisplay

	@disable_display.setter
	def disable_display(self, value):
		"""Gets or sets whether to hide or show this body."""
		self._instance.DisableDisplay = value

	@property
	def disable_highlight(self):
		"""Disables highlighting of the selected body in the graphics area."""
		return self._instance.DisableHighlight

	@disable_highlight.setter
	def disable_highlight(self, value):
		"""Disables highlighting of the selected body in the graphics area."""
		self._instance.DisableHighlight = value

	@property
	def i_material_property_values(self):
		"""Gets or sets the material properties for a body other than the base body in the active configuration."""
		return self._instance.IMaterialPropertyValues2

	@i_material_property_values.setter
	def i_material_property_values(self, value):
		"""Gets or sets the material properties for a body other than the base body in the active configuration."""
		self._instance.IMaterialPropertyValues2 = value

	@property
	def is_safe(self):
		"""Not implemented."""
		return self._instance.IsSafe

	@is_safe.setter
	def is_safe(self, value):
		"""Not implemented."""
		self._instance.IsSafe = value

	@property
	def material_property_values(self):
		"""Gets or sets the material properties for a body other than the base body in the active configuration."""
		return self._instance.MaterialPropertyValues2

	@material_property_values.setter
	def material_property_values(self, value):
		"""Gets or sets the material properties for a body other than the base body in the active configuration."""
		self._instance.MaterialPropertyValues2 = value

	@property
	def name(self):
		"""Gets or sets the name of the selected body."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the name of the selected body."""
		self._instance.Name = value

	@property
	def visible(self):
		"""Gets whether this body is visible or hidden."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets whether this body is visible or hidden."""
		self._instance.Visible = value

	@property
	def add_constant_fillets(self):
		"""Creates constant radius fillets on the specified edges on this body."""
		return self._instance.AddConstantFillets

	@add_constant_fillets.setter
	def add_constant_fillets(self, value):
		"""Creates constant radius fillets on the specified edges on this body."""
		self._instance.AddConstantFillets = value

	@property
	def add_profile_arc(self):
		"""Creates an arc profile curve and returns a pointer to that curve."""
		return self._instance.AddProfileArc

	@add_profile_arc.setter
	def add_profile_arc(self, value):
		"""Creates an arc profile curve and returns a pointer to that curve."""
		self._instance.AddProfileArc = value

	@property
	def add_profile_bspline(self):
		"""Creates an B-spline profile curve and returns a pointer to that curve."""
		return self._instance.AddProfileBspline

	@add_profile_bspline.setter
	def add_profile_bspline(self, value):
		"""Creates an B-spline profile curve and returns a pointer to that curve."""
		self._instance.AddProfileBspline = value

	@property
	def add_profile_bspline_by_pts(self):
		"""Adds a profile B-spline."""
		return self._instance.AddProfileBsplineByPts

	@add_profile_bspline_by_pts.setter
	def add_profile_bspline_by_pts(self, value):
		"""Adds a profile B-spline."""
		self._instance.AddProfileBsplineByPts = value

	@property
	def add_profile_line(self):
		"""Creates a line profile curve and returns a pointer to that curve."""
		return self._instance.AddProfileLine

	@add_profile_line.setter
	def add_profile_line(self, value):
		"""Creates a line profile curve and returns a pointer to that curve."""
		self._instance.AddProfileLine = value

	@property
	def add_property_extension(self):
		"""Adds a property extension to this body."""
		return self._instance.AddPropertyExtension2

	@add_property_extension.setter
	def add_property_extension(self, value):
		"""Adds a property extension to this body."""
		self._instance.AddPropertyExtension2 = value

	@property
	def add_vertex_point(self):
		"""Adds a vertex."""
		return self._instance.AddVertexPoint

	@add_vertex_point.setter
	def add_vertex_point(self, value):
		"""Adds a vertex."""
		self._instance.AddVertexPoint = value

	@property
	def apply_transform(self):
		"""Applies a transform to this body."""
		return self._instance.ApplyTransform

	@apply_transform.setter
	def apply_transform(self, value):
		"""Applies a transform to this body."""
		self._instance.ApplyTransform = value

	@property
	def copy(self):
		"""Gets a copy of this body."""
		return self._instance.Copy2

	@copy.setter
	def copy(self, value):
		"""Gets a copy of this body."""
		self._instance.Copy2 = value

	@property
	def create_base_feature(self):
		"""Creates a base feature for the imported body."""
		return self._instance.CreateBaseFeature

	@create_base_feature.setter
	def create_base_feature(self, value):
		"""Creates a base feature for the imported body."""
		self._instance.CreateBaseFeature = value

	@property
	def create_blend_surface(self):
		"""Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces."""
		return self._instance.CreateBlendSurface

	@create_blend_surface.setter
	def create_blend_surface(self, value):
		"""Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces."""
		self._instance.CreateBlendSurface = value

	@property
	def create_body_from_faces(self):
		"""Creates a temporary body from the faces."""
		return self._instance.CreateBodyFromFaces

	@create_body_from_faces.setter
	def create_body_from_faces(self, value):
		"""Creates a temporary body from the faces."""
		self._instance.CreateBodyFromFaces = value

	@property
	def create_body_from_surfaces(self):
		"""Creates a body from a list of trimmed surfaces."""
		return self._instance.CreateBodyFromSurfaces

	@create_body_from_surfaces.setter
	def create_body_from_surfaces(self, value):
		"""Creates a body from a list of trimmed surfaces."""
		self._instance.CreateBodyFromSurfaces = value

	@property
	def create_bounded_surface(self):
		"""Creates a bounded surface from an independent base surface."""
		return self._instance.CreateBoundedSurface

	@create_bounded_surface.setter
	def create_bounded_surface(self, value):
		"""Creates a bounded surface from an independent base surface."""
		self._instance.CreateBoundedSurface = value

	@property
	def create_bspline_surface(self):
		"""Creates a new B-spline surface."""
		return self._instance.CreateBsplineSurface

	@create_bspline_surface.setter
	def create_bspline_surface(self, value):
		"""Creates a new B-spline surface."""
		self._instance.CreateBsplineSurface = value

	@property
	def create_extrusion_surface(self):
		"""Creates a new surface of extrusion (infinitely long tabulated cylinder)."""
		return self._instance.CreateExtrusionSurface

	@create_extrusion_surface.setter
	def create_extrusion_surface(self, value):
		"""Creates a new surface of extrusion (infinitely long tabulated cylinder)."""
		self._instance.CreateExtrusionSurface = value

	@property
	def create_new_surface(self):
		"""Creates a handle for a new surface to serve as geometry for a face to be added to the body."""
		return self._instance.CreateNewSurface

	@create_new_surface.setter
	def create_new_surface(self, value):
		"""Creates a handle for a new surface to serve as geometry for a face to be added to the body."""
		self._instance.CreateNewSurface = value

	@property
	def create_offset_surface(self):
		"""Creates a new surface offset from an existing surface."""
		return self._instance.CreateOffsetSurface

	@create_offset_surface.setter
	def create_offset_surface(self, value):
		"""Creates a new surface offset from an existing surface."""
		self._instance.CreateOffsetSurface = value

	@property
	def create_planar_surface(self):
		"""Creates a new infinite planar surface."""
		return self._instance.CreatePlanarSurface

	@create_planar_surface.setter
	def create_planar_surface(self, value):
		"""Creates a new infinite planar surface."""
		self._instance.CreatePlanarSurface = value

	@property
	def create_planar_trim_surface_d_l_l(self):
		"""Creates a planar trim surface for this body."""
		return self._instance.CreatePlanarTrimSurfaceDLL

	@create_planar_trim_surface_d_l_l.setter
	def create_planar_trim_surface_d_l_l(self, value):
		"""Creates a planar trim surface for this body."""
		self._instance.CreatePlanarTrimSurfaceDLL = value

	@property
	def create_revolution_surface(self):
		"""Creates a new surface of revolution."""
		return self._instance.CreateRevolutionSurface

	@create_revolution_surface.setter
	def create_revolution_surface(self, value):
		"""Creates a new surface of revolution."""
		self._instance.CreateRevolutionSurface = value

	@property
	def create_ruled_surface(self):
		"""Creates a ruled surface from the specified curves and apex point."""
		return self._instance.CreateRuledSurface

	@create_ruled_surface.setter
	def create_ruled_surface(self, value):
		"""Creates a ruled surface from the specified curves and apex point."""
		self._instance.CreateRuledSurface = value

	@property
	def create_temp_body_from_surfaces(self):
		"""Creates a temporary body from a list of existing trimmed surfaces."""
		return self._instance.CreateTempBodyFromSurfaces

	@create_temp_body_from_surfaces.setter
	def create_temp_body_from_surfaces(self, value):
		"""Creates a temporary body from a list of existing trimmed surfaces."""
		self._instance.CreateTempBodyFromSurfaces = value

	@property
	def create_trimmed_surface(self):
		"""Creates a trimmed surface from a base surface and a list of existing trimming curves."""
		return self._instance.CreateTrimmedSurface

	@create_trimmed_surface.setter
	def create_trimmed_surface(self, value):
		"""Creates a trimmed surface from a base surface and a list of existing trimming curves."""
		self._instance.CreateTrimmedSurface = value

	@property
	def delete_blends(self):
		"""Removes a set of fillet faces from a temporary body and heals the body."""
		return self._instance.DeleteBlends3

	@delete_blends.setter
	def delete_blends(self, value):
		"""Removes a set of fillet faces from a temporary body and heals the body."""
		self._instance.DeleteBlends3 = value

	@property
	def delete_faces(self):
		"""Deletes a set of faces from a temporary body."""
		return self._instance.DeleteFaces5

	@delete_faces.setter
	def delete_faces(self, value):
		"""Deletes a set of faces from a temporary body."""
		self._instance.DeleteFaces5 = value

	@property
	def delete_faces_make_sheet_bodies(self):
		"""Creates sheet bodies from deleted faces."""
		return self._instance.DeleteFacesMakeSheetBodies

	@delete_faces_make_sheet_bodies.setter
	def delete_faces_make_sheet_bodies(self, value):
		"""Creates sheet bodies from deleted faces."""
		self._instance.DeleteFacesMakeSheetBodies = value

	@property
	def de_select(self):
		"""Deselects this body."""
		return self._instance.DeSelect

	@de_select.setter
	def de_select(self, value):
		"""Deselects this body."""
		self._instance.DeSelect = value

	@property
	def diagnose(self):
		"""Gets the IDiagnoseResult object for this body."""
		return self._instance.Diagnose

	@diagnose.setter
	def diagnose(self, value):
		"""Gets the IDiagnoseResult object for this body."""
		self._instance.Diagnose = value

	@property
	def display(self):
		"""Displays this temporary body in the context of the specified part or component."""
		return self._instance.Display3

	@display.setter
	def display(self, value):
		"""Displays this temporary body in the context of the specified part or component."""
		self._instance.Display3 = value

	@property
	def display_wire_frame_x_o_r(self):
		"""Displays a temporary body in the given part's context in XOR mode."""
		return self._instance.DisplayWireFrameXOR

	@display_wire_frame_x_o_r.setter
	def display_wire_frame_x_o_r(self, value):
		"""Displays a temporary body in the given part's context in XOR mode."""
		self._instance.DisplayWireFrameXOR = value

	@property
	def draft_body(self):
		"""Adds drafts to the specified faces on a temporary body. This method modifies the body."""
		return self._instance.DraftBody2

	@draft_body.setter
	def draft_body(self, value):
		"""Adds drafts to the specified faces on a temporary body. This method modifies the body."""
		self._instance.DraftBody2 = value

	@property
	def enum_faces(self):
		"""Returns an enumerated list of the faces in a body."""
		return self._instance.EnumFaces

	@enum_faces.setter
	def enum_faces(self, value):
		"""Returns an enumerated list of the faces in a body."""
		self._instance.EnumFaces = value

	@property
	def extend_surface(self):
		"""Creates a new temporary body by extending the selected edges."""
		return self._instance.ExtendSurface

	@extend_surface.setter
	def extend_surface(self, value):
		"""Creates a new temporary body by extending the selected edges."""
		self._instance.ExtendSurface = value

	@property
	def find_attribute(self):
		"""Finds an attribute on a body."""
		return self._instance.FindAttribute

	@find_attribute.setter
	def find_attribute(self, value):
		"""Finds an attribute on a body."""
		self._instance.FindAttribute = value

	@property
	def get_body_box(self):
		"""Gets the bounding box for this body."""
		return self._instance.GetBodyBox

	@get_body_box.setter
	def get_body_box(self, value):
		"""Gets the bounding box for this body."""
		self._instance.GetBodyBox = value

	@property
	def get_coincidence_transform(self):
		"""Calculates the transformation matrix, which would make the input body coincident with this body if the transformation matrix is applied."""
		return self._instance.GetCoincidenceTransform2

	@get_coincidence_transform.setter
	def get_coincidence_transform(self, value):
		"""Calculates the transformation matrix, which would make the input body coincident with this body if the transformation matrix is applied."""
		self._instance.GetCoincidenceTransform2 = value

	@property
	def get_edge_count(self):
		"""Gets the number of edges for this body."""
		return self._instance.GetEdgeCount

	@get_edge_count.setter
	def get_edge_count(self, value):
		"""Gets the number of edges for this body."""
		self._instance.GetEdgeCount = value

	@property
	def get_edges(self):
		"""Gets the edges for this body."""
		return self._instance.GetEdges

	@get_edges.setter
	def get_edges(self, value):
		"""Gets the edges for this body."""
		self._instance.GetEdges = value

	@property
	def get_excess_body_array(self):
		"""Gets the excess bodies after sewing."""
		return self._instance.GetExcessBodyArray

	@get_excess_body_array.setter
	def get_excess_body_array(self, value):
		"""Gets the excess bodies after sewing."""
		self._instance.GetExcessBodyArray = value

	@property
	def get_extreme_point(self):
		"""Calculates the extreme point of the model in the specified direction."""
		return self._instance.GetExtremePoint

	@get_extreme_point.setter
	def get_extreme_point(self, value):
		"""Calculates the extreme point of the model in the specified direction."""
		self._instance.GetExtremePoint = value

	@property
	def get_face_count(self):
		"""Gets the number of faces in this body."""
		return self._instance.GetFaceCount

	@get_face_count.setter
	def get_face_count(self, value):
		"""Gets the number of faces in this body."""
		self._instance.GetFaceCount = value

	@property
	def get_faces(self):
		"""Gets all of the faces on the body."""
		return self._instance.GetFaces

	@get_faces.setter
	def get_faces(self, value):
		"""Gets all of the faces on the body."""
		self._instance.GetFaces = value

	@property
	def get_feature_count(self):
		"""Gets the number of features in this body in a multibody sheet metal part."""
		return self._instance.GetFeatureCount

	@get_feature_count.setter
	def get_feature_count(self, value):
		"""Gets the number of features in this body in a multibody sheet metal part."""
		self._instance.GetFeatureCount = value

	@property
	def get_features(self):
		"""Gets the features in this body in a multibody sheet metal part."""
		return self._instance.GetFeatures

	@get_features.setter
	def get_features(self, value):
		"""Gets the features in this body in a multibody sheet metal part."""
		self._instance.GetFeatures = value

	@property
	def get_first_face(self):
		"""Finds the first face in a body and returns the face."""
		return self._instance.GetFirstFace

	@get_first_face.setter
	def get_first_face(self, value):
		"""Finds the first face in a body and returns the face."""
		self._instance.GetFirstFace = value

	@property
	def get_first_selected_face(self):
		"""Gets the first selected face on this body. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		return self._instance.GetFirstSelectedFace

	@get_first_selected_face.setter
	def get_first_selected_face(self, value):
		"""Gets the first selected face on this body. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		self._instance.GetFirstSelectedFace = value

	@property
	def get_iges_error_code(self):
		"""Gets the current IGES error code."""
		return self._instance.GetIgesErrorCode

	@get_iges_error_code.setter
	def get_iges_error_code(self, value):
		"""Gets the current IGES error code."""
		self._instance.GetIgesErrorCode = value

	@property
	def get_iges_error_count(self):
		"""Gets the number of errors encountered while running an IGES routine."""
		return self._instance.GetIgesErrorCount

	@get_iges_error_count.setter
	def get_iges_error_count(self, value):
		"""Gets the number of errors encountered while running an IGES routine."""
		self._instance.GetIgesErrorCount = value

	@property
	def get_intersection_edges(self):
		"""Gets the edges resulting from the intersection of the specified tool body and this body."""
		return self._instance.GetIntersectionEdges2

	@get_intersection_edges.setter
	def get_intersection_edges(self, value):
		"""Gets the edges resulting from the intersection of the specified tool body and this body."""
		self._instance.GetIntersectionEdges2 = value

	@property
	def get_mass_properties(self):
		"""Gets the mass properties of this body."""
		return self._instance.GetMassProperties

	@get_mass_properties.setter
	def get_mass_properties(self, value):
		"""Gets the mass properties of this body."""
		self._instance.GetMassProperties = value

	@property
	def get_material_id_name(self):
		"""Gets the material name for this body."""
		return self._instance.GetMaterialIdName2

	@get_material_id_name.setter
	def get_material_id_name(self, value):
		"""Gets the material name for this body."""
		self._instance.GetMaterialIdName2 = value

	@property
	def get_material_property_name(self):
		"""Gets the names of the material database and the material for the specified configuration."""
		return self._instance.GetMaterialPropertyName

	@get_material_property_name.setter
	def get_material_property_name(self, value):
		"""Gets the names of the material database and the material for the specified configuration."""
		self._instance.GetMaterialPropertyName = value

	@property
	def get_material_user_name(self):
		"""Gets the material name for this body; the material name is visible to the user."""
		return self._instance.GetMaterialUserName2

	@get_material_user_name.setter
	def get_material_user_name(self, value):
		"""Gets the material name for this body; the material name is visible to the user."""
		self._instance.GetMaterialUserName2 = value

	@property
	def get_middle_surface(self):
		"""Inserts a midsurface in a body."""
		return self._instance.GetMiddleSurface

	@get_middle_surface.setter
	def get_middle_surface(self, value):
		"""Inserts a midsurface in a body."""
		self._instance.GetMiddleSurface = value

	@property
	def get_next_selected_face(self):
		"""Gets the next selected face. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		return self._instance.GetNextSelectedFace

	@get_next_selected_face.setter
	def get_next_selected_face(self, value):
		"""Gets the next selected face. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		self._instance.GetNextSelectedFace = value

	@property
	def get_original_patterned_body(self):
		"""Gets the original body from this patterned body. Also gets the transformation of this body with respect to the original body."""
		return self._instance.GetOriginalPatternedBody

	@get_original_patterned_body.setter
	def get_original_patterned_body(self, value):
		"""Gets the original body from this patterned body. Also gets the transformation of this body with respect to the original body."""
		self._instance.GetOriginalPatternedBody = value

	@property
	def get_processed_body(self):
		"""Pre-processes the geometry of the body using the specified parameters."""
		return self._instance.GetProcessedBody2

	@get_processed_body.setter
	def get_processed_body(self, value):
		"""Pre-processes the geometry of the body using the specified parameters."""
		self._instance.GetProcessedBody2 = value

	@property
	def get_processed_body_with_sel_face(self):
		"""Gets a processed body."""
		return self._instance.GetProcessedBodyWithSelFace

	@get_processed_body_with_sel_face.setter
	def get_processed_body_with_sel_face(self, value):
		"""Gets a processed body."""
		self._instance.GetProcessedBodyWithSelFace = value

	@property
	def get_property_extension(self):
		"""Gets the specified property extension on this body."""
		return self._instance.GetPropertyExtension2

	@get_property_extension.setter
	def get_property_extension(self, value):
		"""Gets the specified property extension on this body."""
		self._instance.GetPropertyExtension2 = value

	@property
	def get_safe_body(self):
		"""Not implemented."""
		return self._instance.GetSafeBody

	@get_safe_body.setter
	def get_safe_body(self, value):
		"""Not implemented."""
		self._instance.GetSafeBody = value

	@property
	def get_selected_face_count(self):
		"""Gets the number of selected faces on this body. For use with IBody2::GetProcessedBodyWithSelFace and IBody2::IGetPrcoessedBodyWithSelFace and intended for IGES routines."""
		return self._instance.GetSelectedFaceCount

	@get_selected_face_count.setter
	def get_selected_face_count(self, value):
		"""Gets the number of selected faces on this body. For use with IBody2::GetProcessedBodyWithSelFace and IBody2::IGetPrcoessedBodyWithSelFace and intended for IGES routines."""
		self._instance.GetSelectedFaceCount = value

	@property
	def get_selected_faces(self):
		"""Gets the selected faces. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		return self._instance.GetSelectedFaces

	@get_selected_faces.setter
	def get_selected_faces(self, value):
		"""Gets the selected faces. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		self._instance.GetSelectedFaces = value

	@property
	def get_selection_id(self):
		"""Gets the selection ID of the body, if one exists."""
		return self._instance.GetSelectionId

	@get_selection_id.setter
	def get_selection_id(self, value):
		"""Gets the selection ID of the body, if one exists."""
		self._instance.GetSelectionId = value

	@property
	def get_sheet_body(self):
		"""Gets a sheet (surface) body in this body."""
		return self._instance.GetSheetBody

	@get_sheet_body.setter
	def get_sheet_body(self, value):
		"""Gets a sheet (surface) body in this body."""
		self._instance.GetSheetBody = value

	@property
	def get_tessellation(self):
		"""Gets the ITessellation object."""
		return self._instance.GetTessellation

	@get_tessellation.setter
	def get_tessellation(self, value):
		"""Gets the ITessellation object."""
		self._instance.GetTessellation = value

	@property
	def get_texture(self):
		"""Gets the texture applied to this body in the specified configuration."""
		return self._instance.GetTexture

	@get_texture.setter
	def get_texture(self, value):
		"""Gets the texture applied to this body in the specified configuration."""
		self._instance.GetTexture = value

	@property
	def get_tracking_i_ds(self):
		"""Gets the tracking IDs assigned to this body."""
		return self._instance.GetTrackingIDs

	@get_tracking_i_ds.setter
	def get_tracking_i_ds(self, value):
		"""Gets the tracking IDs assigned to this body."""
		self._instance.GetTrackingIDs = value

	@property
	def get_tracking_i_ds_count(self):
		"""Gets the number of tracking IDs on this body."""
		return self._instance.GetTrackingIDsCount

	@get_tracking_i_ds_count.setter
	def get_tracking_i_ds_count(self, value):
		"""Gets the number of tracking IDs on this body."""
		self._instance.GetTrackingIDsCount = value

	@property
	def get_type(self):
		"""Gets the type of the body."""
		return self._instance.GetType

	@get_type.setter
	def get_type(self, value):
		"""Gets the type of the body."""
		self._instance.GetType = value

	@property
	def get_update_stamp(self):
		"""Gets the update stamp for the body as of the last rebuild."""
		return self._instance.GetUpdateStamp

	@get_update_stamp.setter
	def get_update_stamp(self, value):
		"""Gets the update stamp for the body as of the last rebuild."""
		self._instance.GetUpdateStamp = value

	@property
	def get_vertex_count(self):
		"""Gets the number of vertices in this body."""
		return self._instance.GetVertexCount

	@get_vertex_count.setter
	def get_vertex_count(self, value):
		"""Gets the number of vertices in this body."""
		self._instance.GetVertexCount = value

	@property
	def get_vertices(self):
		"""Gets the vertices in this body."""
		return self._instance.GetVertices

	@get_vertices.setter
	def get_vertices(self, value):
		"""Gets the vertices in this body."""
		self._instance.GetVertices = value

	@property
	def has_material_property_values(self):
		"""Gets whether this body has an appearance."""
		return self._instance.HasMaterialPropertyValues

	@has_material_property_values.setter
	def has_material_property_values(self, value):
		"""Gets whether this body has an appearance."""
		self._instance.HasMaterialPropertyValues = value

	@property
	def hide(self):
		"""Hides this temporary body in the context of the specified part."""
		return self._instance.Hide

	@hide.setter
	def hide(self, value):
		"""Hides this temporary body in the context of the specified part."""
		self._instance.Hide = value

	@property
	def hide_body(self):
		"""Hides or shows this body."""
		return self._instance.HideBody

	@hide_body.setter
	def hide_body(self, value):
		"""Hides or shows this body."""
		self._instance.HideBody = value

	@property
	def i_add_profile_arc(self):
		"""Creates an arc profile curve and returns a pointer to that curve."""
		return self._instance.IAddProfileArc

	@i_add_profile_arc.setter
	def i_add_profile_arc(self, value):
		"""Creates an arc profile curve and returns a pointer to that curve."""
		self._instance.IAddProfileArc = value

	@property
	def i_add_profile_arc_d_l_l(self):
		"""Adds a profile arc."""
		return self._instance.IAddProfileArcDLL

	@i_add_profile_arc_d_l_l.setter
	def i_add_profile_arc_d_l_l(self, value):
		"""Adds a profile arc."""
		self._instance.IAddProfileArcDLL = value

	@property
	def i_add_profile_bspline(self):
		"""Creates an B-spline profile curve and returns a pointer to that curve."""
		return self._instance.IAddProfileBspline

	@i_add_profile_bspline.setter
	def i_add_profile_bspline(self, value):
		"""Creates an B-spline profile curve and returns a pointer to that curve."""
		self._instance.IAddProfileBspline = value

	@property
	def i_add_profile_bspline_by_pts(self):
		"""Adds a profile B-spline."""
		return self._instance.IAddProfileBsplineByPts

	@i_add_profile_bspline_by_pts.setter
	def i_add_profile_bspline_by_pts(self, value):
		"""Adds a profile B-spline."""
		self._instance.IAddProfileBsplineByPts = value

	@property
	def i_add_profile_bspline_d_l_l(self):
		"""Adds a profile B-spline."""
		return self._instance.IAddProfileBsplineDLL

	@i_add_profile_bspline_d_l_l.setter
	def i_add_profile_bspline_d_l_l(self, value):
		"""Adds a profile B-spline."""
		self._instance.IAddProfileBsplineDLL = value

	@property
	def i_add_profile_line(self):
		"""Creates a line profile curve and returns a pointer to that curve."""
		return self._instance.IAddProfileLine

	@i_add_profile_line.setter
	def i_add_profile_line(self, value):
		"""Creates a line profile curve and returns a pointer to that curve."""
		self._instance.IAddProfileLine = value

	@property
	def i_add_profile_line_d_l_l(self):
		"""Adds a profile line."""
		return self._instance.IAddProfileLineDLL

	@i_add_profile_line_d_l_l.setter
	def i_add_profile_line_d_l_l(self, value):
		"""Adds a profile line."""
		self._instance.IAddProfileLineDLL = value

	@property
	def i_add_vertex_point(self):
		"""Adds a vertex."""
		return self._instance.IAddVertexPoint

	@i_add_vertex_point.setter
	def i_add_vertex_point(self, value):
		"""Adds a vertex."""
		self._instance.IAddVertexPoint = value

	@property
	def i_combine_volumes(self):
		"""Combines the volumes of two bodies."""
		return self._instance.ICombineVolumes

	@i_combine_volumes.setter
	def i_combine_volumes(self, value):
		"""Combines the volumes of two bodies."""
		self._instance.ICombineVolumes = value

	@property
	def i_copy(self):
		"""Gets a copy of this body."""
		return self._instance.ICopy

	@i_copy.setter
	def i_copy(self, value):
		"""Gets a copy of this body."""
		self._instance.ICopy = value

	@property
	def i_create_base_feature(self):
		"""Creates a base feature for the imported body."""
		return self._instance.ICreateBaseFeature

	@i_create_base_feature.setter
	def i_create_base_feature(self, value):
		"""Creates a base feature for the imported body."""
		self._instance.ICreateBaseFeature = value

	@property
	def i_create_blend_surface(self):
		"""Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces."""
		return self._instance.ICreateBlendSurface

	@i_create_blend_surface.setter
	def i_create_blend_surface(self, value):
		"""Creates a constant radius rolling-ball blend surface (also known as a pipe surface) between two side surfaces."""
		self._instance.ICreateBlendSurface = value

	@property
	def i_create_body_from_faces(self):
		"""Creates a temporary body from the faces."""
		return self._instance.ICreateBodyFromFaces

	@i_create_body_from_faces.setter
	def i_create_body_from_faces(self, value):
		"""Creates a temporary body from the faces."""
		self._instance.ICreateBodyFromFaces = value

	@property
	def i_create_bounded_surface(self):
		"""Creates a bounded surface from an independent base surface."""
		return self._instance.ICreateBoundedSurface

	@i_create_bounded_surface.setter
	def i_create_bounded_surface(self, value):
		"""Creates a bounded surface from an independent base surface."""
		self._instance.ICreateBoundedSurface = value

	@property
	def i_create_bspline_surface(self):
		"""Creates a new B-spline surface."""
		return self._instance.ICreateBsplineSurface

	@i_create_bspline_surface.setter
	def i_create_bspline_surface(self, value):
		"""Creates a new B-spline surface."""
		self._instance.ICreateBsplineSurface = value

	@property
	def i_create_bspline_surface_d_l_l(self):
		"""Creates a B-spline surface in this body."""
		return self._instance.ICreateBsplineSurfaceDLL

	@i_create_bspline_surface_d_l_l.setter
	def i_create_bspline_surface_d_l_l(self, value):
		"""Creates a B-spline surface in this body."""
		self._instance.ICreateBsplineSurfaceDLL = value

	@property
	def i_create_extrusion_surface(self):
		"""Creates a new surface of extrusion (infinitely long tabulated cylinder)."""
		return self._instance.ICreateExtrusionSurface

	@i_create_extrusion_surface.setter
	def i_create_extrusion_surface(self, value):
		"""Creates a new surface of extrusion (infinitely long tabulated cylinder)."""
		self._instance.ICreateExtrusionSurface = value

	@property
	def i_create_extrusion_surface_d_l_l(self):
		"""Creates an extruded surface."""
		return self._instance.ICreateExtrusionSurfaceDLL

	@i_create_extrusion_surface_d_l_l.setter
	def i_create_extrusion_surface_d_l_l(self, value):
		"""Creates an extruded surface."""
		self._instance.ICreateExtrusionSurfaceDLL = value

	@property
	def i_create_new_surface(self):
		"""Creates a handle for a new surface to serve as geometry for a face to be added to the body."""
		return self._instance.ICreateNewSurface

	@i_create_new_surface.setter
	def i_create_new_surface(self, value):
		"""Creates a handle for a new surface to serve as geometry for a face to be added to the body."""
		self._instance.ICreateNewSurface = value

	@property
	def i_create_offset_surface(self):
		"""Creates a new surface offset from an existing surface."""
		return self._instance.ICreateOffsetSurface

	@i_create_offset_surface.setter
	def i_create_offset_surface(self, value):
		"""Creates a new surface offset from an existing surface."""
		self._instance.ICreateOffsetSurface = value

	@property
	def i_create_planar_surface(self):
		"""Creates a new infinite planar surface."""
		return self._instance.ICreatePlanarSurface

	@i_create_planar_surface.setter
	def i_create_planar_surface(self, value):
		"""Creates a new infinite planar surface."""
		self._instance.ICreatePlanarSurface = value

	@property
	def i_create_planar_surface_d_l_l(self):
		"""Creates a planar surface."""
		return self._instance.ICreatePlanarSurfaceDLL

	@i_create_planar_surface_d_l_l.setter
	def i_create_planar_surface_d_l_l(self, value):
		"""Creates a planar surface."""
		self._instance.ICreatePlanarSurfaceDLL = value

	@property
	def i_create_planar_trim_surface_d_l_l(self):
		"""Creates a planar trim surface for this body."""
		return self._instance.ICreatePlanarTrimSurfaceDLL

	@i_create_planar_trim_surface_d_l_l.setter
	def i_create_planar_trim_surface_d_l_l(self, value):
		"""Creates a planar trim surface for this body."""
		self._instance.ICreatePlanarTrimSurfaceDLL = value

	@property
	def i_create_pspline_surface_d_l_l(self):
		"""Creates a B-surface from a piecewise surface."""
		return self._instance.ICreatePsplineSurfaceDLL

	@i_create_pspline_surface_d_l_l.setter
	def i_create_pspline_surface_d_l_l(self, value):
		"""Creates a B-surface from a piecewise surface."""
		self._instance.ICreatePsplineSurfaceDLL = value

	@property
	def i_create_revolution_surface(self):
		"""Creates a new surface of revolution."""
		return self._instance.ICreateRevolutionSurface

	@i_create_revolution_surface.setter
	def i_create_revolution_surface(self, value):
		"""Creates a new surface of revolution."""
		self._instance.ICreateRevolutionSurface = value

	@property
	def i_create_revolution_surface_d_l_l(self):
		"""Creates a surface of revolution for this body."""
		return self._instance.ICreateRevolutionSurfaceDLL

	@i_create_revolution_surface_d_l_l.setter
	def i_create_revolution_surface_d_l_l(self, value):
		"""Creates a surface of revolution for this body."""
		self._instance.ICreateRevolutionSurfaceDLL = value

	@property
	def i_create_ruled_surface(self):
		"""Creates a ruled surface from the specified curves and apex point."""
		return self._instance.ICreateRuledSurface

	@i_create_ruled_surface.setter
	def i_create_ruled_surface(self, value):
		"""Creates a ruled surface from the specified curves and apex point."""
		self._instance.ICreateRuledSurface = value

	@property
	def i_create_temp_body_from_surfaces(self):
		"""Creates a temporary body from a list of existing trimmed surfaces."""
		return self._instance.ICreateTempBodyFromSurfaces

	@i_create_temp_body_from_surfaces.setter
	def i_create_temp_body_from_surfaces(self, value):
		"""Creates a temporary body from a list of existing trimmed surfaces."""
		self._instance.ICreateTempBodyFromSurfaces = value

	@property
	def i_delete_blends(self):
		"""Removes a set of fillet faces from a temporary body and heals the body."""
		return self._instance.IDeleteBlends3

	@i_delete_blends.setter
	def i_delete_blends(self, value):
		"""Removes a set of fillet faces from a temporary body and heals the body."""
		self._instance.IDeleteBlends3 = value

	@property
	def i_delete_faces_make_sheet_bodies(self):
		"""Creates sheet bodies from deleted faces."""
		return self._instance.IDeleteFacesMakeSheetBodies

	@i_delete_faces_make_sheet_bodies.setter
	def i_delete_faces_make_sheet_bodies(self, value):
		"""Creates sheet bodies from deleted faces."""
		self._instance.IDeleteFacesMakeSheetBodies = value

	@property
	def i_delete_faces_make_sheet_bodies_count(self):
		"""Gets the number of sheet bodies to create from the deleted faces."""
		return self._instance.IDeleteFacesMakeSheetBodiesCount

	@i_delete_faces_make_sheet_bodies_count.setter
	def i_delete_faces_make_sheet_bodies_count(self, value):
		"""Gets the number of sheet bodies to create from the deleted faces."""
		self._instance.IDeleteFacesMakeSheetBodiesCount = value

	@property
	def i_display_wire_frame_x_o_r(self):
		"""Displays a temporary body in the given part's context in XOR mode."""
		return self._instance.IDisplayWireFrameXOR

	@i_display_wire_frame_x_o_r.setter
	def i_display_wire_frame_x_o_r(self, value):
		"""Displays a temporary body in the given part's context in XOR mode."""
		self._instance.IDisplayWireFrameXOR = value

	@property
	def i_draft_body(self):
		"""Adds drafts to the specified faces on a temporary body. This method modifies the body."""
		return self._instance.IDraftBody2

	@i_draft_body.setter
	def i_draft_body(self, value):
		"""Adds drafts to the specified faces on a temporary body. This method modifies the body."""
		self._instance.IDraftBody2 = value

	@property
	def i_extend_surface(self):
		"""Creates a new temporary body by extending the selected edges."""
		return self._instance.IExtendSurface

	@i_extend_surface.setter
	def i_extend_surface(self, value):
		"""Creates a new temporary body by extending the selected edges."""
		self._instance.IExtendSurface = value

	@property
	def i_get_body_box(self):
		"""Gets the bounding box for this body."""
		return self._instance.IGetBodyBox

	@i_get_body_box.setter
	def i_get_body_box(self, value):
		"""Gets the bounding box for this body."""
		self._instance.IGetBodyBox = value

	@property
	def i_get_edges(self):
		"""Gets the edges for this body."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Gets the edges for this body."""
		self._instance.IGetEdges = value

	@property
	def i_get_excess_body_array(self):
		"""Gets the excess bodies after sewing."""
		return self._instance.IGetExcessBodyArray

	@i_get_excess_body_array.setter
	def i_get_excess_body_array(self, value):
		"""Gets the excess bodies after sewing."""
		self._instance.IGetExcessBodyArray = value

	@property
	def i_get_excess_body_count(self):
		"""Gets the number of excess bodies."""
		return self._instance.IGetExcessBodyCount

	@i_get_excess_body_count.setter
	def i_get_excess_body_count(self, value):
		"""Gets the number of excess bodies."""
		self._instance.IGetExcessBodyCount = value

	@property
	def i_get_faces(self):
		"""Gets all of the faces on the body."""
		return self._instance.IGetFaces

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets all of the faces on the body."""
		self._instance.IGetFaces = value

	@property
	def i_get_features(self):
		"""Gets the features in this body in a multibody sheet metal part."""
		return self._instance.IGetFeatures

	@i_get_features.setter
	def i_get_features(self, value):
		"""Gets the features in this body in a multibody sheet metal part."""
		self._instance.IGetFeatures = value

	@property
	def i_get_first_face(self):
		"""Finds the first face in a body and returns the face."""
		return self._instance.IGetFirstFace

	@i_get_first_face.setter
	def i_get_first_face(self, value):
		"""Finds the first face in a body and returns the face."""
		self._instance.IGetFirstFace = value

	@property
	def i_get_first_selected_face(self):
		"""Gets the first selected face on this body. For use with IBody2::IGetProcessedBodyWithSelFace and intended for IGES routines."""
		return self._instance.IGetFirstSelectedFace

	@i_get_first_selected_face.setter
	def i_get_first_selected_face(self, value):
		"""Gets the first selected face on this body. For use with IBody2::IGetProcessedBodyWithSelFace and intended for IGES routines."""
		self._instance.IGetFirstSelectedFace = value

	@property
	def i_get_intersection_edge_count(self):
		"""Gets the number of intersecting edges between this body and the specified tool body."""
		return self._instance.IGetIntersectionEdgeCount

	@i_get_intersection_edge_count.setter
	def i_get_intersection_edge_count(self, value):
		"""Gets the number of intersecting edges between this body and the specified tool body."""
		self._instance.IGetIntersectionEdgeCount = value

	@property
	def i_get_mass_properties(self):
		"""Gets the mass properties of this body."""
		return self._instance.IGetMassProperties

	@i_get_mass_properties.setter
	def i_get_mass_properties(self, value):
		"""Gets the mass properties of this body."""
		self._instance.IGetMassProperties = value

	@property
	def i_get_material_property_values_for_face(self):
		"""Gets the color of the specified face."""
		return self._instance.IGetMaterialPropertyValuesForFace

	@i_get_material_property_values_for_face.setter
	def i_get_material_property_values_for_face(self, value):
		"""Gets the color of the specified face."""
		self._instance.IGetMaterialPropertyValuesForFace = value

	@property
	def i_get_middle_surface(self):
		"""Inserts a midsurface in a body."""
		return self._instance.IGetMiddleSurface

	@i_get_middle_surface.setter
	def i_get_middle_surface(self, value):
		"""Inserts a midsurface in a body."""
		self._instance.IGetMiddleSurface = value

	@property
	def i_get_next_selected_face(self):
		"""Gets the next selected face. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		return self._instance.IGetNextSelectedFace

	@i_get_next_selected_face.setter
	def i_get_next_selected_face(self, value):
		"""Gets the next selected face. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		self._instance.IGetNextSelectedFace = value

	@property
	def i_get_processed_body_with_sel_face(self):
		"""Gets a processed body."""
		return self._instance.IGetProcessedBodyWithSelFace

	@i_get_processed_body_with_sel_face.setter
	def i_get_processed_body_with_sel_face(self, value):
		"""Gets a processed body."""
		self._instance.IGetProcessedBodyWithSelFace = value

	@property
	def i_get_selected_faces(self):
		"""Gets the selected faces. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		return self._instance.IGetSelectedFaces

	@i_get_selected_faces.setter
	def i_get_selected_faces(self, value):
		"""Gets the selected faces. For use with IBody2::GetProcessedBodyWithSelFace and intended for IGES routines."""
		self._instance.IGetSelectedFaces = value

	@property
	def i_get_sheet_body(self):
		"""Gets a sheet (surface) body in this body."""
		return self._instance.IGetSheetBody

	@i_get_sheet_body.setter
	def i_get_sheet_body(self, value):
		"""Gets a sheet (surface) body in this body."""
		self._instance.IGetSheetBody = value

	@property
	def i_get_tessellation(self):
		"""Gets the ITessellation object."""
		return self._instance.IGetTessellation

	@i_get_tessellation.setter
	def i_get_tessellation(self, value):
		"""Gets the ITessellation object."""
		self._instance.IGetTessellation = value

	@property
	def i_get_tracking_i_ds(self):
		"""Gets the tracking IDs assigned to this body."""
		return self._instance.IGetTrackingIDs

	@i_get_tracking_i_ds.setter
	def i_get_tracking_i_ds(self, value):
		"""Gets the tracking IDs assigned to this body."""
		self._instance.IGetTrackingIDs = value

	@property
	def i_get_vertices(self):
		"""Gets the vertices in this body."""
		return self._instance.IGetVertices

	@i_get_vertices.setter
	def i_get_vertices(self, value):
		"""Gets the vertices in this body."""
		self._instance.IGetVertices = value

	@property
	def i_hide(self):
		"""Hides a temporary body using the specified part's context."""
		return self._instance.IHide

	@i_hide.setter
	def i_hide(self, value):
		"""Hides a temporary body using the specified part's context."""
		self._instance.IHide = value

	@property
	def i_matched_boolean(self):
		"""Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly."""
		return self._instance.IMatchedBoolean4

	@i_matched_boolean.setter
	def i_matched_boolean(self, value):
		"""Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly."""
		self._instance.IMatchedBoolean4 = value

	@property
	def i_operations(self):
		"""Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies."""
		return self._instance.IOperations2

	@i_operations.setter
	def i_operations(self, value):
		"""Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies."""
		self._instance.IOperations2 = value

	@property
	def i_remove_faces_from_sheet(self):
		"""Removes the specified faces from a sheet (surface) body."""
		return self._instance.IRemoveFacesFromSheet

	@i_remove_faces_from_sheet.setter
	def i_remove_faces_from_sheet(self, value):
		"""Removes the specified faces from a sheet (surface) body."""
		self._instance.IRemoveFacesFromSheet = value

	@property
	def i_remove_material_property(self):
		"""Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies."""
		return self._instance.IRemoveMaterialProperty

	@i_remove_material_property.setter
	def i_remove_material_property(self, value):
		"""Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies."""
		self._instance.IRemoveMaterialProperty = value

	@property
	def i_save(self):
		"""Saves this body."""
		return self._instance.ISave

	@i_save.setter
	def i_save(self, value):
		"""Saves this body."""
		self._instance.ISave = value

	@property
	def i_section_by_sheet(self):
		"""Sections a body using a sheet (surface) body."""
		return self._instance.ISectionBySheet

	@i_section_by_sheet.setter
	def i_section_by_sheet(self, value):
		"""Sections a body using a sheet (surface) body."""
		self._instance.ISectionBySheet = value

	@property
	def i_set_current_surface(self):
		"""Places an existing surface into a temporary body that is under construction."""
		return self._instance.ISetCurrentSurface

	@i_set_current_surface.setter
	def i_set_current_surface(self, value):
		"""Places an existing surface into a temporary body that is under construction."""
		self._instance.ISetCurrentSurface = value

	@property
	def is_mesh_body(self):
		"""Gets whether this body is a mesh body."""
		return self._instance.IsMeshBody

	@is_mesh_body.setter
	def is_mesh_body(self, value):
		"""Gets whether this body is a mesh body."""
		self._instance.IsMeshBody = value

	@property
	def is_pattern_seed(self):
		"""Gets whether this body is the seed of a patterned body."""
		return self._instance.IsPatternSeed

	@is_pattern_seed.setter
	def is_pattern_seed(self, value):
		"""Gets whether this body is the seed of a patterned body."""
		self._instance.IsPatternSeed = value

	@property
	def is_sheet_metal(self):
		"""Gets whether this body was created by a sheet metal feature."""
		return self._instance.IsSheetMetal

	@is_sheet_metal.setter
	def is_sheet_metal(self, value):
		"""Gets whether this body was created by a sheet metal feature."""
		self._instance.IsSheetMetal = value

	@property
	def is_temporary_body(self):
		"""Gets whether the body is a temporary body."""
		return self._instance.IsTemporaryBody

	@is_temporary_body.setter
	def is_temporary_body(self, value):
		"""Gets whether the body is a temporary body."""
		self._instance.IsTemporaryBody = value

	@property
	def make_offset(self):
		"""Creates a new temporary body by offsetting the selected surface body by the specified distance and in the specified direction."""
		return self._instance.MakeOffset

	@make_offset.setter
	def make_offset(self, value):
		"""Creates a new temporary body by offsetting the selected surface body by the specified distance and in the specified direction."""
		self._instance.MakeOffset = value

	@property
	def matched_boolean(self):
		"""Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly."""
		return self._instance.MatchedBoolean4

	@matched_boolean.setter
	def matched_boolean(self, value):
		"""Performs a matched boolean on the specified bodies and supports an optional list of faces that match exactly."""
		self._instance.MatchedBoolean4 = value

	@property
	def minimum_radius(self):
		"""Gets the minimum radius of this body."""
		return self._instance.MinimumRadius

	@minimum_radius.setter
	def minimum_radius(self, value):
		"""Gets the minimum radius of this body."""
		self._instance.MinimumRadius = value

	@property
	def negate(self):
		"""Reverses the direction (i.e., orientation) of the body."""
		return self._instance.Negate

	@negate.setter
	def negate(self, value):
		"""Reverses the direction (i.e., orientation) of the body."""
		self._instance.Negate = value

	@property
	def offset_planar_wire_body(self):
		"""Offsets a planar wire body in the normal plane by the specified distance."""
		return self._instance.OffsetPlanarWireBody

	@offset_planar_wire_body.setter
	def offset_planar_wire_body(self, value):
		"""Offsets a planar wire body in the normal plane by the specified distance."""
		self._instance.OffsetPlanarWireBody = value

	@property
	def operations(self):
		"""Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies."""
		return self._instance.Operations2

	@operations.setter
	def operations(self, value):
		"""Performs add, cut, and intersect (unite, subtract, and interfere) operations between two temporary bodies."""
		self._instance.Operations2 = value

	@property
	def remove_faces_from_sheet(self):
		"""Removes the specified faces from a sheet (surface) body."""
		return self._instance.RemoveFacesFromSheet

	@remove_faces_from_sheet.setter
	def remove_faces_from_sheet(self, value):
		"""Removes the specified faces from a sheet (surface) body."""
		self._instance.RemoveFacesFromSheet = value

	@property
	def remove_material_property(self):
		"""Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies."""
		return self._instance.RemoveMaterialProperty

	@remove_material_property.setter
	def remove_material_property(self, value):
		"""Removes the material property values (e.g., color) from the body in the specified configurations in parts and assemblies."""
		self._instance.RemoveMaterialProperty = value

	@property
	def remove_redundant_topology(self):
		"""Removes redundant topology from the body."""
		return self._instance.RemoveRedundantTopology

	@remove_redundant_topology.setter
	def remove_redundant_topology(self, value):
		"""Removes redundant topology from the body."""
		self._instance.RemoveRedundantTopology = value

	@property
	def remove_texture(self):
		"""Removes the texture applied to this body in the specified configuration."""
		return self._instance.RemoveTexture

	@remove_texture.setter
	def remove_texture(self, value):
		"""Removes the texture applied to this body in the specified configuration."""
		self._instance.RemoveTexture = value

	@property
	def remove_texture_by_display_state(self):
		"""Removes the texture applied to this body in the specified display state."""
		return self._instance.RemoveTextureByDisplayState

	@remove_texture_by_display_state.setter
	def remove_texture_by_display_state(self, value):
		"""Removes the texture applied to this body in the specified display state."""
		self._instance.RemoveTextureByDisplayState = value

	@property
	def remove_tracking_i_d(self):
		"""Removes a tracking ID assigned to this body."""
		return self._instance.RemoveTrackingID

	@remove_tracking_i_d.setter
	def remove_tracking_i_d(self, value):
		"""Removes a tracking ID assigned to this body."""
		self._instance.RemoveTrackingID = value

	@property
	def reset_edge_tolerances(self):
		"""Resets the tolerance on all edges of this body."""
		return self._instance.ResetEdgeTolerances

	@reset_edge_tolerances.setter
	def reset_edge_tolerances(self, value):
		"""Resets the tolerance on all edges of this body."""
		self._instance.ResetEdgeTolerances = value

	@property
	def reset_property_extension(self):
		"""Clears all values stored in the property extension."""
		return self._instance.ResetPropertyExtension2

	@reset_property_extension.setter
	def reset_property_extension(self, value):
		"""Clears all values stored in the property extension."""
		self._instance.ResetPropertyExtension2 = value

	@property
	def save(self):
		"""Saves this body."""
		return self._instance.Save

	@save.setter
	def save(self, value):
		"""Saves this body."""
		self._instance.Save = value

	@property
	def select(self):
		"""Selects this body and marks it."""
		return self._instance.Select2

	@select.setter
	def select(self, value):
		"""Selects this body and marks it."""
		self._instance.Select2 = value

	@property
	def set_current_surface(self):
		"""Places an existing surface into a temporary body that is under construction."""
		return self._instance.SetCurrentSurface

	@set_current_surface.setter
	def set_current_surface(self, value):
		"""Places an existing surface into a temporary body that is under construction."""
		self._instance.SetCurrentSurface = value

	@property
	def set_iges_info(self):
		"""Sends IGES-specific data to the geometric modeler."""
		return self._instance.SetIgesInfo

	@set_iges_info.setter
	def set_iges_info(self, value):
		"""Sends IGES-specific data to the geometric modeler."""
		self._instance.SetIgesInfo = value

	@property
	def set_material_id_name(self):
		"""Sets the material name for this body."""
		return self._instance.SetMaterialIdName2

	@set_material_id_name.setter
	def set_material_id_name(self, value):
		"""Sets the material name for this body."""
		self._instance.SetMaterialIdName2 = value

	@property
	def set_material_property(self):
		"""Sets the material for this body."""
		return self._instance.SetMaterialProperty

	@set_material_property.setter
	def set_material_property(self, value):
		"""Sets the material for this body."""
		self._instance.SetMaterialProperty = value

	@property
	def set_material_user_name(self):
		"""Sets the material name for this body. This material name is visible to the user."""
		return self._instance.SetMaterialUserName2

	@set_material_user_name.setter
	def set_material_user_name(self, value):
		"""Sets the material name for this body. This material name is visible to the user."""
		self._instance.SetMaterialUserName2 = value

	@property
	def set_texture(self):
		"""Applies texture to this body in the specified configuration."""
		return self._instance.SetTexture

	@set_texture.setter
	def set_texture(self, value):
		"""Applies texture to this body in the specified configuration."""
		self._instance.SetTexture = value

	@property
	def set_texture_by_display_state(self):
		"""Sets the texture applied to this body in the specified display state."""
		return self._instance.SetTextureByDisplayState

	@set_texture_by_display_state.setter
	def set_texture_by_display_state(self, value):
		"""Sets the texture applied to this body in the specified display state."""
		self._instance.SetTextureByDisplayState = value

	@property
	def set_tracking_i_d(self):
		"""Assigns a tracking ID to this body."""
		return self._instance.SetTrackingID

	@set_tracking_i_d.setter
	def set_tracking_i_d(self, value):
		"""Assigns a tracking ID to this body."""
		self._instance.SetTrackingID = value

