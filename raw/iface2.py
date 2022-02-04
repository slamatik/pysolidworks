# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html
class IFace2:
	def __init__(self, parent=None):
		self._instance = parent

	def check(self):
		"""Checks whether the face is a valid, and, if not, returns the faults."""
		# return self._instance.Check
		raise NotImplemented

	@property
	def i_material_property_values(self):
		"""Gets or sets the material properties for the selected face in the active configuration."""
		return self._instance.IMaterialPropertyValues

	@i_material_property_values.setter
	def i_material_property_values(self, value):
		"""Gets or sets the material properties for the selected face in the active configuration."""
		self._instance.IMaterialPropertyValues = value

	@property
	def i_normal(self):
		"""Gets the unit normal vector for any planar face.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.INormal

	@i_normal.setter
	def i_normal(self, value):
		"""Gets the unit normal vector for any planar face.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.INormal = value

	@property
	def material_id_name(self):
		"""Gets or sets the material name."""
		return self._instance.MaterialIdName

	@material_id_name.setter
	def material_id_name(self, value):
		"""Gets or sets the material name."""
		self._instance.MaterialIdName = value

	@property
	def material_property_values(self):
		"""Gets or sets the material properties for the selected face in the active configuration."""
		return self._instance.MaterialPropertyValues

	@material_property_values.setter
	def material_property_values(self, value):
		"""Gets or sets the material properties for the selected face in the active configuration."""
		self._instance.MaterialPropertyValues = value

	@property
	def material_user_name(self):
		"""Gets or sets the material name, which is visible to the user."""
		return self._instance.MaterialUserName

	@material_user_name.setter
	def material_user_name(self, value):
		"""Gets or sets the material name, which is visible to the user."""
		self._instance.MaterialUserName = value

	@property
	def normal(self):
		"""Gets the unit normal vector for any planar face.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Normal

	@normal.setter
	def normal(self, value):
		"""Gets the unit normal vector for any planar face.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Normal = value

	@property
	def add_property_extension(self):
		"""Adds a property extension to this face."""
		return self._instance.AddPropertyExtension

	@add_property_extension.setter
	def add_property_extension(self, value):
		"""Adds a property extension to this face."""
		self._instance.AddPropertyExtension = value

	@property
	def attach_surface(self):
		"""Attaches a surface to this face."""
		return self._instance.AttachSurface

	@attach_surface.setter
	def attach_surface(self, value):
		"""Attaches a surface to this face."""
		self._instance.AttachSurface = value

	@property
	def create_sheet_body(self):
		"""Creates a sheet body from this face."""
		return self._instance.CreateSheetBody

	@create_sheet_body.setter
	def create_sheet_body(self, value):
		"""Creates a sheet body from this face."""
		self._instance.CreateSheetBody = value

	@property
	def create_sheet_body_by_face_extension(self):
		"""Creates a sheet body by extending the face."""
		return self._instance.CreateSheetBodyByFaceExtension

	@create_sheet_body_by_face_extension.setter
	def create_sheet_body_by_face_extension(self, value):
		"""Creates a sheet body by extending the face."""
		self._instance.CreateSheetBodyByFaceExtension = value

	@property
	def detach_surface(self):
		"""Detaches a surface from this face."""
		return self._instance.DetachSurface

	@detach_surface.setter
	def detach_surface(self, value):
		"""Detaches a surface from this face."""
		self._instance.DetachSurface = value

	@property
	def enum_edges(self):
		"""Enumerates the edges in a face."""
		return self._instance.EnumEdges

	@enum_edges.setter
	def enum_edges(self, value):
		"""Enumerates the edges in a face."""
		self._instance.EnumEdges = value

	@property
	def enum_loops(self):
		"""Enumerates the loops in a face."""
		return self._instance.EnumLoops

	@enum_loops.setter
	def enum_loops(self, value):
		"""Enumerates the loops in a face."""
		self._instance.EnumLoops = value

	@property
	def face_in_surface_sense(self):
		"""Checks whether the face normal has the opposite direction (sense) as the underlying surface."""
		return self._instance.FaceInSurfaceSense

	@face_in_surface_sense.setter
	def face_in_surface_sense(self, value):
		"""Checks whether the face normal has the opposite direction (sense) as the underlying surface."""
		self._instance.FaceInSurfaceSense = value

	@property
	def get_all_decal_properties(self):
		"""Gets the decal properties applied to this face."""
		return self._instance.GetAllDecalProperties

	@get_all_decal_properties.setter
	def get_all_decal_properties(self, value):
		"""Gets the decal properties applied to this face."""
		self._instance.GetAllDecalProperties = value

	@property
	def get_area(self):
		"""Gets the area of this face."""
		return self._instance.GetArea

	@get_area.setter
	def get_area(self, value):
		"""Gets the area of this face."""
		self._instance.GetArea = value

	@property
	def get_body(self):
		"""Gets the body containing this face."""
		return self._instance.GetBody

	@get_body.setter
	def get_body(self, value):
		"""Gets the body containing this face."""
		self._instance.GetBody = value

	@property
	def get_box(self):
		"""Gets the box boundaries for this face."""
		return self._instance.GetBox

	@get_box.setter
	def get_box(self, value):
		"""Gets the box boundaries for this face."""
		self._instance.GetBox = value

	@property
	def get_closest_point_on(self):
		"""Uses the X,Y,Z input point to determine the closest point on the face."""
		return self._instance.GetClosestPointOn

	@get_closest_point_on.setter
	def get_closest_point_on(self, value):
		"""Uses the X,Y,Z input point to determine the closest point on the face."""
		self._instance.GetClosestPointOn = value

	@property
	def get_decals_count(self):
		"""Gets the number of decals applied to this face."""
		return self._instance.GetDecalsCount

	@get_decals_count.setter
	def get_decals_count(self, value):
		"""Gets the number of decals applied to this face."""
		self._instance.GetDecalsCount = value

	@property
	def get_edge_count(self):
		"""Gets the number of the edges that bound this face."""
		return self._instance.GetEdgeCount

	@get_edge_count.setter
	def get_edge_count(self, value):
		"""Gets the number of the edges that bound this face."""
		self._instance.GetEdgeCount = value

	@property
	def get_edges(self):
		"""Get the edges bounding this face."""
		return self._instance.GetEdges

	@get_edges.setter
	def get_edges(self, value):
		"""Get the edges bounding this face."""
		self._instance.GetEdges = value

	@property
	def get_face_id(self):
		"""Gets the face ID of an imported body."""
		return self._instance.GetFaceId

	@get_face_id.setter
	def get_face_id(self, value):
		"""Gets the face ID of an imported body."""
		self._instance.GetFaceId = value

	@property
	def get_feature(self):
		"""Gets the feature that owns this face."""
		return self._instance.GetFeature

	@get_feature.setter
	def get_feature(self, value):
		"""Gets the feature that owns this face."""
		self._instance.GetFeature = value

	@property
	def get_feature_id(self):
		"""Gets the order number for the owning feature of this face."""
		return self._instance.GetFeatureId

	@get_feature_id.setter
	def get_feature_id(self, value):
		"""Gets the order number for the owning feature of this face."""
		self._instance.GetFeatureId = value

	@property
	def get_first_loop(self):
		"""Gets the first loop in this face, which is not necessarily the outer loop."""
		return self._instance.GetFirstLoop

	@get_first_loop.setter
	def get_first_loop(self, value):
		"""Gets the first loop in this face, which is not necessarily the outer loop."""
		self._instance.GetFirstLoop = value

	@property
	def get_loop_count(self):
		"""Gets the number of loops in this face."""
		return self._instance.GetLoopCount

	@get_loop_count.setter
	def get_loop_count(self, value):
		"""Gets the number of loops in this face."""
		self._instance.GetLoopCount = value

	@property
	def get_loops(self):
		"""Gets all of the loops on this face."""
		return self._instance.GetLoops

	@get_loops.setter
	def get_loops(self, value):
		"""Gets all of the loops on this face."""
		self._instance.GetLoops = value

	@property
	def get_material_property_values(self):
		"""Gets the material property values for this face."""
		return self._instance.GetMaterialPropertyValues2

	@get_material_property_values.setter
	def get_material_property_values(self, value):
		"""Gets the material property values for this face."""
		self._instance.GetMaterialPropertyValues2 = value

	@property
	def get_next_face(self):
		"""Gets the next face in a body."""
		return self._instance.GetNextFace

	@get_next_face.setter
	def get_next_face(self, value):
		"""Gets the next face in a body."""
		self._instance.GetNextFace = value

	@property
	def get_pattern_seed_feature(self):
		"""Gets the seed feature of a pattern."""
		return self._instance.GetPatternSeedFeature

	@get_pattern_seed_feature.setter
	def get_pattern_seed_feature(self, value):
		"""Gets the seed feature of a pattern."""
		self._instance.GetPatternSeedFeature = value

	@property
	def get_projected_point_on(self):
		"""Gets the point where the input point is projected on to this face."""
		return self._instance.GetProjectedPointOn

	@get_projected_point_on.setter
	def get_projected_point_on(self, value):
		"""Gets the point where the input point is projected on to this face."""
		self._instance.GetProjectedPointOn = value

	@property
	def get_property_extension(self):
		"""Gets the property extension on this face."""
		return self._instance.GetPropertyExtension

	@get_property_extension.setter
	def get_property_extension(self, value):
		"""Gets the property extension on this face."""
		self._instance.GetPropertyExtension = value

	@property
	def get_seed_feature(self):
		"""Gets the seed feature of a patterned, mirrored, or copied body for this face."""
		return self._instance.GetSeedFeature

	@get_seed_feature.setter
	def get_seed_feature(self, value):
		"""Gets the seed feature of a patterned, mirrored, or copied body for this face."""
		self._instance.GetSeedFeature = value

	@property
	def get_shell_type(self):
		"""Gets the shell type for this face."""
		return self._instance.GetShellType

	@get_shell_type.setter
	def get_shell_type(self, value):
		"""Gets the shell type for this face."""
		self._instance.GetShellType = value

	@property
	def get_silhoutte_edges_v_b(self):
		"""Gets the silhouette edges."""
		return self._instance.GetSilhoutteEdgesVB

	@get_silhoutte_edges_v_b.setter
	def get_silhoutte_edges_v_b(self, value):
		"""Gets the silhouette edges."""
		self._instance.GetSilhoutteEdgesVB = value

	@property
	def get_surface(self):
		"""Gets the surface referenced by this face."""
		return self._instance.GetSurface

	@get_surface.setter
	def get_surface(self, value):
		"""Gets the surface referenced by this face."""
		self._instance.GetSurface = value

	@property
	def get_tess_norms(self):
		"""Gets the normal vector for each of the triangles that make up the shaded picture tessellation."""
		return self._instance.GetTessNorms

	@get_tess_norms.setter
	def get_tess_norms(self, value):
		"""Gets the normal vector for each of the triangles that make up the shaded picture tessellation."""
		self._instance.GetTessNorms = value

	@property
	def get_tess_textures(self):
		"""Gets the texture coordinates for the triangles."""
		return self._instance.GetTessTextures

	@get_tess_textures.setter
	def get_tess_textures(self, value):
		"""Gets the texture coordinates for the triangles."""
		self._instance.GetTessTextures = value

	@property
	def get_tess_triangle_count(self):
		"""Gets the number of triangles that make up the shaded picture tessellation for this face."""
		return self._instance.GetTessTriangleCount

	@get_tess_triangle_count.setter
	def get_tess_triangle_count(self, value):
		"""Gets the number of triangles that make up the shaded picture tessellation for this face."""
		self._instance.GetTessTriangleCount = value

	@property
	def get_tess_triangles(self):
		"""Gets the triangles that make up the shaded picture tessellation for this face."""
		return self._instance.GetTessTriangles

	@get_tess_triangles.setter
	def get_tess_triangles(self, value):
		"""Gets the triangles that make up the shaded picture tessellation for this face."""
		self._instance.GetTessTriangles = value

	@property
	def get_tess_tri_strip_edges(self):
		"""Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face."""
		return self._instance.GetTessTriStripEdges

	@get_tess_tri_strip_edges.setter
	def get_tess_tri_strip_edges(self, value):
		"""Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face."""
		self._instance.GetTessTriStripEdges = value

	@property
	def get_tess_tri_strip_norms(self):
		"""Gets the normal vector for each of the triangles that make up the shaded picture tessellation for this face."""
		return self._instance.GetTessTriStripNorms

	@get_tess_tri_strip_norms.setter
	def get_tess_tri_strip_norms(self, value):
		"""Gets the normal vector for each of the triangles that make up the shaded picture tessellation for this face."""
		self._instance.GetTessTriStripNorms = value

	@property
	def get_tess_tri_strips(self):
		"""Gets the vertices that make up the shaded picture tessellation for this face."""
		return self._instance.GetTessTriStrips

	@get_tess_tri_strips.setter
	def get_tess_tri_strips(self, value):
		"""Gets the vertices that make up the shaded picture tessellation for this face."""
		self._instance.GetTessTriStrips = value

	@property
	def get_tess_tri_strip_size(self):
		"""Gets the array size required for IFace2::GetTessTriStrips and IFace2::IGetTessTriStrips."""
		return self._instance.GetTessTriStripSize

	@get_tess_tri_strip_size.setter
	def get_tess_tri_strip_size(self, value):
		"""Gets the array size required for IFace2::GetTessTriStrips and IFace2::IGetTessTriStrips."""
		self._instance.GetTessTriStripSize = value

	@property
	def get_texture(self):
		"""Gets the texture applied to this face in the specified configuration."""
		return self._instance.GetTexture

	@get_texture.setter
	def get_texture(self, value):
		"""Gets the texture applied to this face in the specified configuration."""
		self._instance.GetTexture = value

	@property
	def get_tracking_i_ds(self):
		"""Gets the tracking IDs assigned to this face."""
		return self._instance.GetTrackingIDs

	@get_tracking_i_ds.setter
	def get_tracking_i_ds(self, value):
		"""Gets the tracking IDs assigned to this face."""
		self._instance.GetTrackingIDs = value

	@property
	def get_tracking_i_ds_count(self):
		"""Gets the number of tracking IDs on this face."""
		return self._instance.GetTrackingIDsCount

	@get_tracking_i_ds_count.setter
	def get_tracking_i_ds_count(self, value):
		"""Gets the number of tracking IDs on this face."""
		self._instance.GetTrackingIDsCount = value

	@property
	def get_trim_curves(self):
		"""Gets the definition of all of the entities that describe a trimmed face."""
		return self._instance.GetTrimCurves2

	@get_trim_curves.setter
	def get_trim_curves(self, value):
		"""Gets the definition of all of the entities that describe a trimmed face."""
		self._instance.GetTrimCurves2 = value

	@property
	def get_trim_curve_topology(self):
		"""Gets the trim curve topology for this face."""
		return self._instance.GetTrimCurveTopology

	@get_trim_curve_topology.setter
	def get_trim_curve_topology(self, value):
		"""Gets the trim curve topology for this face."""
		self._instance.GetTrimCurveTopology = value

	@property
	def get_trim_curve_topology_count(self):
		"""Gets the number of elements in the trim curve topology for this face."""
		return self._instance.GetTrimCurveTopologyCount

	@get_trim_curve_topology_count.setter
	def get_trim_curve_topology_count(self, value):
		"""Gets the number of elements in the trim curve topology for this face."""
		self._instance.GetTrimCurveTopologyCount = value

	@property
	def get_trim_curve_topology_types(self):
		"""Gets the types of elements in the trim curve topology for this face."""
		return self._instance.GetTrimCurveTopologyTypes

	@get_trim_curve_topology_types.setter
	def get_trim_curve_topology_types(self, value):
		"""Gets the types of elements in the trim curve topology for this face."""
		self._instance.GetTrimCurveTopologyTypes = value

	@property
	def get_u_v_bounds(self):
		"""Gets the values that describe the U, V bounds of this face."""
		return self._instance.GetUVBounds

	@get_u_v_bounds.setter
	def get_u_v_bounds(self, value):
		"""Gets the values that describe the U, V bounds of this face."""
		self._instance.GetUVBounds = value

	@property
	def has_material_property_values(self):
		"""Gets whether this face has an appearance."""
		return self._instance.HasMaterialPropertyValues

	@has_material_property_values.setter
	def has_material_property_values(self, value):
		"""Gets whether this face has an appearance."""
		self._instance.HasMaterialPropertyValues = value

	@property
	def highlight(self):
		"""Adds highlighting to or removes highlighting from a face."""
		return self._instance.Highlight

	@highlight.setter
	def highlight(self, value):
		"""Adds highlighting to or removes highlighting from a face."""
		self._instance.Highlight = value

	@property
	def i_create_sheet_body(self):
		"""Creates a sheet body from this face."""
		return self._instance.ICreateSheetBody

	@i_create_sheet_body.setter
	def i_create_sheet_body(self, value):
		"""Creates a sheet body from this face."""
		self._instance.ICreateSheetBody = value

	@property
	def i_create_sheet_body_by_face_extension(self):
		"""Creates a sheet body by extending the face."""
		return self._instance.ICreateSheetBodyByFaceExtension

	@i_create_sheet_body_by_face_extension.setter
	def i_create_sheet_body_by_face_extension(self, value):
		"""Creates a sheet body by extending the face."""
		self._instance.ICreateSheetBodyByFaceExtension = value

	@property
	def i_get_all_decal_properties(self):
		"""Gets the decal properties applied to this face."""
		return self._instance.IGetAllDecalProperties

	@i_get_all_decal_properties.setter
	def i_get_all_decal_properties(self, value):
		"""Gets the decal properties applied to this face."""
		self._instance.IGetAllDecalProperties = value

	@property
	def i_get_body(self):
		"""Gets the body containing this face."""
		return self._instance.IGetBody

	@i_get_body.setter
	def i_get_body(self, value):
		"""Gets the body containing this face."""
		self._instance.IGetBody = value

	@property
	def i_get_box(self):
		"""Gets the box boundaries for this face."""
		return self._instance.IGetBox

	@i_get_box.setter
	def i_get_box(self, value):
		"""Gets the box boundaries for this face."""
		self._instance.IGetBox = value

	@property
	def i_get_closest_point_on(self):
		"""Uses the X,Y,Z input point to determine the closest point on the face."""
		return self._instance.IGetClosestPointOn

	@i_get_closest_point_on.setter
	def i_get_closest_point_on(self, value):
		"""Uses the X,Y,Z input point to determine the closest point on the face."""
		self._instance.IGetClosestPointOn = value

	@property
	def i_get_decal_properties(self):
		"""Gets the properties of the specified decal on this face."""
		return self._instance.IGetDecalProperties

	@i_get_decal_properties.setter
	def i_get_decal_properties(self, value):
		"""Gets the properties of the specified decal on this face."""
		self._instance.IGetDecalProperties = value

	@property
	def i_get_edges(self):
		"""Get the edges bounding this face."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Get the edges bounding this face."""
		self._instance.IGetEdges = value

	@property
	def i_get_feature(self):
		"""Gets the feature that owns this face."""
		return self._instance.IGetFeature

	@i_get_feature.setter
	def i_get_feature(self, value):
		"""Gets the feature that owns this face."""
		self._instance.IGetFeature = value

	@property
	def i_get_first_loop(self):
		"""Gets the first loop in this face, which is not necessarily the outer loop."""
		return self._instance.IGetFirstLoop

	@i_get_first_loop.setter
	def i_get_first_loop(self, value):
		"""Gets the first loop in this face, which is not necessarily the outer loop."""
		self._instance.IGetFirstLoop = value

	@property
	def i_get_loops(self):
		"""Gets all of the loops on this face."""
		return self._instance.IGetLoops

	@i_get_loops.setter
	def i_get_loops(self, value):
		"""Gets all of the loops on this face."""
		self._instance.IGetLoops = value

	@property
	def i_get_material_property_values(self):
		"""Gets the material property values for this face."""
		return self._instance.IGetMaterialPropertyValues2

	@i_get_material_property_values.setter
	def i_get_material_property_values(self, value):
		"""Gets the material property values for this face."""
		self._instance.IGetMaterialPropertyValues2 = value

	@property
	def i_get_next_face(self):
		"""Gets the next face in a body."""
		return self._instance.IGetNextFace

	@i_get_next_face.setter
	def i_get_next_face(self, value):
		"""Gets the next face in a body."""
		self._instance.IGetNextFace = value

	@property
	def i_get_pattern_seed_feature(self):
		"""Gets the seed feature of a pattern."""
		return self._instance.IGetPatternSeedFeature

	@i_get_pattern_seed_feature.setter
	def i_get_pattern_seed_feature(self, value):
		"""Gets the seed feature of a pattern."""
		self._instance.IGetPatternSeedFeature = value

	@property
	def i_get_silhoutte_edge_count(self):
		"""Gets the number of silhouette edges for this face."""
		return self._instance.IGetSilhoutteEdgeCount

	@i_get_silhoutte_edge_count.setter
	def i_get_silhoutte_edge_count(self, value):
		"""Gets the number of silhouette edges for this face."""
		self._instance.IGetSilhoutteEdgeCount = value

	@property
	def i_get_silhoutte_edges(self):
		"""Gets the silhouette edges for this face with the specified root point and in the specified direction."""
		return self._instance.IGetSilhoutteEdges

	@i_get_silhoutte_edges.setter
	def i_get_silhoutte_edges(self, value):
		"""Gets the silhouette edges for this face with the specified root point and in the specified direction."""
		self._instance.IGetSilhoutteEdges = value

	@property
	def i_get_surface(self):
		"""Gets the surface referenced by this face."""
		return self._instance.IGetSurface

	@i_get_surface.setter
	def i_get_surface(self, value):
		"""Gets the surface referenced by this face."""
		self._instance.IGetSurface = value

	@property
	def i_get_tess_norms(self):
		"""Gets the normal vector for each of the triangles that make up the shaded picture tessellation."""
		return self._instance.IGetTessNorms

	@i_get_tess_norms.setter
	def i_get_tess_norms(self, value):
		"""Gets the normal vector for each of the triangles that make up the shaded picture tessellation."""
		self._instance.IGetTessNorms = value

	@property
	def i_get_tess_textures(self):
		"""Gets the texture coordinates for the triangles."""
		return self._instance.IGetTessTextures

	@i_get_tess_textures.setter
	def i_get_tess_textures(self, value):
		"""Gets the texture coordinates for the triangles."""
		self._instance.IGetTessTextures = value

	@property
	def i_get_tess_triangles(self):
		"""Gets the triangles that make up the shaded picture tessellation for this face."""
		return self._instance.IGetTessTriangles

	@i_get_tess_triangles.setter
	def i_get_tess_triangles(self, value):
		"""Gets the triangles that make up the shaded picture tessellation for this face."""
		self._instance.IGetTessTriangles = value

	@property
	def i_get_tess_tri_strip_edges(self):
		"""Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face."""
		return self._instance.IGetTessTriStripEdges

	@i_get_tess_tri_strip_edges.setter
	def i_get_tess_tri_strip_edges(self, value):
		"""Gets the edge ID for each of the edges in the triangles that make up the tessellation for this face."""
		self._instance.IGetTessTriStripEdges = value

	@property
	def i_get_tess_tri_strip_edge_size(self):
		"""Gets the size of the array returned by IFace2::GetTessTriStripEdges and IFace2::IGetTessTriStripEdges."""
		return self._instance.IGetTessTriStripEdgeSize

	@i_get_tess_tri_strip_edge_size.setter
	def i_get_tess_tri_strip_edge_size(self, value):
		"""Gets the size of the array returned by IFace2::GetTessTriStripEdges and IFace2::IGetTessTriStripEdges."""
		self._instance.IGetTessTriStripEdgeSize = value

	@property
	def i_get_tess_tri_strip_norms(self):
		"""Gets the normal vector for each of the triangles that make up the shaded picture tessellation for this face."""
		return self._instance.IGetTessTriStripNorms

	@i_get_tess_tri_strip_norms.setter
	def i_get_tess_tri_strip_norms(self, value):
		"""Gets the normal vector for each of the triangles that make up the shaded picture tessellation for this face."""
		self._instance.IGetTessTriStripNorms = value

	@property
	def i_get_tess_tri_strips(self):
		"""Gets the vertices that make up the shaded picture tessellation for this face."""
		return self._instance.IGetTessTriStrips

	@i_get_tess_tri_strips.setter
	def i_get_tess_tri_strips(self, value):
		"""Gets the vertices that make up the shaded picture tessellation for this face."""
		self._instance.IGetTessTriStrips = value

	@property
	def i_get_tracking_i_ds(self):
		"""Gets the tracking IDs assigned to this face."""
		return self._instance.IGetTrackingIDs

	@i_get_tracking_i_ds.setter
	def i_get_tracking_i_ds(self, value):
		"""Gets the tracking IDs assigned to this face."""
		self._instance.IGetTrackingIDs = value

	@property
	def i_get_trim_curve_size(self):
		"""Gets the size of the array required for IFace2::GetTrimCurves2"""
		return self._instance.IGetTrimCurveSize2

	@i_get_trim_curve_size.setter
	def i_get_trim_curve_size(self, value):
		"""Gets the size of the array required for IFace2::GetTrimCurves2"""
		self._instance.IGetTrimCurveSize2 = value

	@property
	def i_get_trim_curve_topology(self):
		"""Gets the trim curve topology for this face."""
		return self._instance.IGetTrimCurveTopology

	@i_get_trim_curve_topology.setter
	def i_get_trim_curve_topology(self, value):
		"""Gets the trim curve topology for this face."""
		self._instance.IGetTrimCurveTopology = value

	@property
	def i_get_trim_curve_topology_types(self):
		"""Gets the trim curve topology type array for this face."""
		return self._instance.IGetTrimCurveTopologyTypes

	@i_get_trim_curve_topology_types.setter
	def i_get_trim_curve_topology_types(self, value):
		"""Gets the trim curve topology type array for this face."""
		self._instance.IGetTrimCurveTopologyTypes = value

	@property
	def i_get_u_v_bounds(self):
		"""Gets the values that describe the U, V bounds of this face."""
		return self._instance.IGetUVBounds

	@i_get_u_v_bounds.setter
	def i_get_u_v_bounds(self, value):
		"""Gets the values that describe the U, V bounds of this face."""
		self._instance.IGetUVBounds = value

	@property
	def i_highlight(self):
		"""Adds highlighting to or removes highlighting from a face."""
		return self._instance.IHighlight

	@i_highlight.setter
	def i_highlight(self, value):
		"""Adds highlighting to or removes highlighting from a face."""
		self._instance.IHighlight = value

	@property
	def i_imprint_curve(self):
		"""Imprints a curve on the selected face."""
		return self._instance.IImprintCurve

	@i_imprint_curve.setter
	def i_imprint_curve(self, value):
		"""Imprints a curve on the selected face."""
		self._instance.IImprintCurve = value

	@property
	def i_is_coincident(self):
		"""Gets whether this face and the specified face, which is located on a different body, are coincident."""
		return self._instance.IIsCoincident

	@i_is_coincident.setter
	def i_is_coincident(self, value):
		"""Gets whether this face and the specified face, which is located on a different body, are coincident."""
		self._instance.IIsCoincident = value

	@property
	def i_is_same(self):
		"""Gets whether the two faces are the same."""
		return self._instance.IIsSame

	@i_is_same.setter
	def i_is_same(self, value):
		"""Gets whether the two faces are the same."""
		self._instance.IIsSame = value

	@property
	def imprint_curve(self):
		"""Imprints a curve on the selected face."""
		return self._instance.ImprintCurve

	@imprint_curve.setter
	def imprint_curve(self, value):
		"""Imprints a curve on the selected face."""
		self._instance.ImprintCurve = value

	@property
	def imprint_curve_count(self):
		"""Gets the number of new edges and faces to create when imprinting a curve."""
		return self._instance.ImprintCurveCount

	@imprint_curve_count.setter
	def imprint_curve_count(self, value):
		"""Gets the number of new edges and faces to create when imprinting a curve."""
		self._instance.ImprintCurveCount = value

	@property
	def i_remove_inner_loops(self):
		"""Removes the inner loops on this face if the face is from a sheet (surface) body."""
		return self._instance.IRemoveInnerLoops

	@i_remove_inner_loops.setter
	def i_remove_inner_loops(self, value):
		"""Removes the inner loops on this face if the face is from a sheet (surface) body."""
		self._instance.IRemoveInnerLoops = value

	@property
	def i_remove_material_property(self):
		"""Removes the material property values from this face."""
		return self._instance.IRemoveMaterialProperty2

	@i_remove_material_property.setter
	def i_remove_material_property(self, value):
		"""Removes the material property values from this face."""
		self._instance.IRemoveMaterialProperty2 = value

	@property
	def i_reverse_evaluate(self):
		"""Gets the UV parameters for the given XYZ location on this face."""
		return self._instance.IReverseEvaluate

	@i_reverse_evaluate.setter
	def i_reverse_evaluate(self, value):
		"""Gets the UV parameters for the given XYZ location on this face."""
		self._instance.IReverseEvaluate = value

	@property
	def is_coincident(self):
		"""Gets whether this face and the specified face, which is located on a different body, are coincident."""
		return self._instance.IsCoincident

	@is_coincident.setter
	def is_coincident(self, value):
		"""Gets whether this face and the specified face, which is located on a different body, are coincident."""
		self._instance.IsCoincident = value

	@property
	def i_set_material_property_values(self):
		"""Sets the material property values for this face."""
		return self._instance.ISetMaterialPropertyValues2

	@i_set_material_property_values.setter
	def i_set_material_property_values(self, value):
		"""Sets the material property values for this face."""
		self._instance.ISetMaterialPropertyValues2 = value

	@property
	def is_same(self):
		"""Gets whether the two faces are the same."""
		return self._instance.IsSame

	@is_same.setter
	def is_same(self, value):
		"""Gets whether the two faces are the same."""
		self._instance.IsSame = value

	@property
	def remove_face_id(self):
		"""Removes the face ID on an imported body."""
		return self._instance.RemoveFaceId

	@remove_face_id.setter
	def remove_face_id(self, value):
		"""Removes the face ID on an imported body."""
		self._instance.RemoveFaceId = value

	@property
	def remove_inner_loops(self):
		"""Removes the inner loops on this face if the face is from a sheet (surface) body."""
		return self._instance.RemoveInnerLoops

	@remove_inner_loops.setter
	def remove_inner_loops(self, value):
		"""Removes the inner loops on this face if the face is from a sheet (surface) body."""
		self._instance.RemoveInnerLoops = value

	@property
	def remove_material_property(self):
		"""Removes the material property values from this face."""
		return self._instance.RemoveMaterialProperty2

	@remove_material_property.setter
	def remove_material_property(self, value):
		"""Removes the material property values from this face."""
		self._instance.RemoveMaterialProperty2 = value

	@property
	def remove_redundant_topology(self):
		"""Removes redundant topology from the face."""
		return self._instance.RemoveRedundantTopology

	@remove_redundant_topology.setter
	def remove_redundant_topology(self, value):
		"""Removes redundant topology from the face."""
		self._instance.RemoveRedundantTopology = value

	@property
	def remove_texture(self):
		"""Removes the texture applied to this face in the specified configuration."""
		return self._instance.RemoveTexture2

	@remove_texture.setter
	def remove_texture(self, value):
		"""Removes the texture applied to this face in the specified configuration."""
		self._instance.RemoveTexture2 = value

	@property
	def remove_texture_by_display_state(self):
		"""Removes the texture applied to this face in the specified display state."""
		return self._instance.RemoveTextureByDisplayState

	@remove_texture_by_display_state.setter
	def remove_texture_by_display_state(self, value):
		"""Removes the texture applied to this face in the specified display state."""
		self._instance.RemoveTextureByDisplayState = value

	@property
	def remove_tracking_i_d(self):
		"""Removes a tracking ID assigned to this face."""
		return self._instance.RemoveTrackingID

	@remove_tracking_i_d.setter
	def remove_tracking_i_d(self, value):
		"""Removes a tracking ID assigned to this face."""
		self._instance.RemoveTrackingID = value

	@property
	def reset_property_extension(self):
		"""Clears all values stored in the property extension."""
		return self._instance.ResetPropertyExtension

	@reset_property_extension.setter
	def reset_property_extension(self, value):
		"""Clears all values stored in the property extension."""
		self._instance.ResetPropertyExtension = value

	@property
	def reverse_evaluate(self):
		"""Gets the UV parameters for the given XYZ location on this face."""
		return self._instance.ReverseEvaluate

	@reverse_evaluate.setter
	def reverse_evaluate(self, value):
		"""Gets the UV parameters for the given XYZ location on this face."""
		self._instance.ReverseEvaluate = value

	@property
	def set_face_id(self):
		"""Sets the face ID on an imported body."""
		return self._instance.SetFaceId

	@set_face_id.setter
	def set_face_id(self, value):
		"""Sets the face ID on an imported body."""
		self._instance.SetFaceId = value

	@property
	def set_material_property_values(self):
		"""Sets the material property values for this face."""
		return self._instance.SetMaterialPropertyValues2

	@set_material_property_values.setter
	def set_material_property_values(self, value):
		"""Sets the material property values for this face."""
		self._instance.SetMaterialPropertyValues2 = value

	@property
	def set_texture(self):
		"""Applies texture to this face in the specified configuration."""
		return self._instance.SetTexture

	@set_texture.setter
	def set_texture(self, value):
		"""Applies texture to this face in the specified configuration."""
		self._instance.SetTexture = value

	@property
	def set_texture_by_display_state(self):
		"""Applies texture to this face in the specified display state."""
		return self._instance.SetTextureByDisplayState

	@set_texture_by_display_state.setter
	def set_texture_by_display_state(self, value):
		"""Applies texture to this face in the specified display state."""
		self._instance.SetTextureByDisplayState = value

	@property
	def set_tracking_i_d(self):
		"""Assigns a tracking ID to this face."""
		return self._instance.SetTrackingID

	@set_tracking_i_d.setter
	def set_tracking_i_d(self, value):
		"""Assigns a tracking ID to this face."""
		self._instance.SetTrackingID = value

