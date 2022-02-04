# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html
class ISimpleFilletFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def asymmetric_fillet(self):
		"""Gets or sets whether this simple fillet/chamfer is asymmetric."""
		return self._instance.AsymmetricFillet

	@asymmetric_fillet.setter
	def asymmetric_fillet(self, value):
		"""Gets or sets whether this simple fillet/chamfer is asymmetric."""
		self._instance.AsymmetricFillet = value

	@property
	def conic_type_for_cross_section_profile(self):
		"""Gets or sets the cross-sectional profile for this simple fillet."""
		return self._instance.ConicTypeForCrossSectionProfile

	@conic_type_for_cross_section_profile.setter
	def conic_type_for_cross_section_profile(self, value):
		"""Gets or sets the cross-sectional profile for this simple fillet."""
		self._instance.ConicTypeForCrossSectionProfile = value

	@property
	def constant_width(self):
		"""Gets or sets whether this simple fillet has a constant width."""
		return self._instance.ConstantWidth

	@constant_width.setter
	def constant_width(self, value):
		"""Gets or sets whether this simple fillet has a constant width."""
		self._instance.ConstantWidth = value

	@property
	def curvature_continuous(self):
		"""Gets or sets whether to create a smoother curvature between adjacent surfaces for this simple fillet feature."""
		return self._instance.CurvatureContinuous

	@curvature_continuous.setter
	def curvature_continuous(self, value):
		"""Gets or sets whether to create a smoother curvature between adjacent surfaces for this simple fillet feature."""
		self._instance.CurvatureContinuous = value

	@property
	def default_conic_rho_or_radius(self):
		"""Gets or sets the default conic rho or radius."""
		return self._instance.DefaultConicRhoOrRadius

	@default_conic_rho_or_radius.setter
	def default_conic_rho_or_radius(self, value):
		"""Gets or sets the default conic rho or radius."""
		self._instance.DefaultConicRhoOrRadius = value

	@property
	def default_distance(self):
		"""Gets or sets the default Distance 2 radius of this asymmetric fillet."""
		return self._instance.DefaultDistance

	@default_distance.setter
	def default_distance(self, value):
		"""Gets or sets the default Distance 2 radius of this asymmetric fillet."""
		self._instance.DefaultDistance = value

	@property
	def default_radius(self):
		"""Gets or sets the default radius of this simple fillet."""
		return self._instance.DefaultRadius

	@default_radius.setter
	def default_radius(self, value):
		"""Gets or sets the default radius of this simple fillet."""
		self._instance.DefaultRadius = value

	@property
	def edges(self):
		"""Gets or sets the edges for this simple radius fillet."""
		return self._instance.Edges

	@edges.setter
	def edges(self, value):
		"""Gets or sets the edges for this simple radius fillet."""
		self._instance.Edges = value

	@property
	def enable_partial_edge_parameters(self):
		"""Gets or sets whether to enable partial edge properties for all edges of this fillet."""
		return self._instance.EnablePartialEdgeParameters

	@enable_partial_edge_parameters.setter
	def enable_partial_edge_parameters(self, value):
		"""Gets or sets whether to enable partial edge properties for all edges of this fillet."""
		self._instance.EnablePartialEdgeParameters = value

	@property
	def features(self):
		"""Gets or sets the features for this simple fillet radius."""
		return self._instance.Features

	@features.setter
	def features(self, value):
		"""Gets or sets the features for this simple fillet radius."""
		self._instance.Features = value

	@property
	def fillet_items_count(self):
		"""Gets the number of fillets for this simple fillet feature."""
		return self._instance.FilletItemsCount

	@fillet_items_count.setter
	def fillet_items_count(self, value):
		"""Gets the number of fillets for this simple fillet feature."""
		self._instance.FilletItemsCount = value

	@property
	def help_point(self):
		"""Gets or sets whether to resolve an ambiguous selection by using a help point when creating a face-face chamfer or a face fillet feature."""
		return self._instance.HelpPoint

	@help_point.setter
	def help_point(self, value):
		"""Gets or sets whether to resolve an ambiguous selection by using a help point when creating a face-face chamfer or a face fillet feature."""
		self._instance.HelpPoint = value

	@property
	def hold_lines(self):
		"""Gets or sets the hold lines (boundaries) for a face blend fillet feature."""
		return self._instance.HoldLines

	@hold_lines.setter
	def hold_lines(self, value):
		"""Gets or sets the hold lines (boundaries) for a face blend fillet feature."""
		self._instance.HoldLines = value

	@property
	def is_multiple_radius(self):
		"""Gets or sets whether this symmetric fillet or chamfer feature is a multiple radius fillet."""
		return self._instance.IsMultipleRadius

	@is_multiple_radius.setter
	def is_multiple_radius(self, value):
		"""Gets or sets whether this symmetric fillet or chamfer feature is a multiple radius fillet."""
		self._instance.IsMultipleRadius = value

	@property
	def keep_features(self):
		"""Gets or sets whether to keep existing features on the entities selected for the fillet."""
		return self._instance.KeepFeatures

	@keep_features.setter
	def keep_features(self, value):
		"""Gets or sets whether to keep existing features on the entities selected for the fillet."""
		self._instance.KeepFeatures = value

	@property
	def loops(self):
		"""Gets or sets the loops on which to create a simple radius fillet."""
		return self._instance.Loops

	@loops.setter
	def loops(self, value):
		"""Gets or sets the loops on which to create a simple radius fillet."""
		self._instance.Loops = value

	@property
	def omit_attached_edges(self):
		"""Gets whether the simple fillet feature is not applied to the attachment edges of the feature."""
		return self._instance.OmitAttachedEdges

	@omit_attached_edges.setter
	def omit_attached_edges(self, value):
		"""Gets whether the simple fillet feature is not applied to the attachment edges of the feature."""
		self._instance.OmitAttachedEdges = value

	@property
	def overflow_type(self):
		"""Gets or sets the overflow type of the simple fillet feature."""
		return self._instance.OverflowType

	@overflow_type.setter
	def overflow_type(self, value):
		"""Gets or sets the overflow type of the simple fillet feature."""
		self._instance.OverflowType = value

	@property
	def propagate_feature_to_parts(self):
		"""Gets or sets whether to extend the assembly simple fillet feature to all affected parts."""
		return self._instance.PropagateFeatureToParts

	@propagate_feature_to_parts.setter
	def propagate_feature_to_parts(self, value):
		"""Gets or sets whether to extend the assembly simple fillet feature to all affected parts."""
		self._instance.PropagateFeatureToParts = value

	@property
	def propagate_to_tangent_faces(self):
		"""Gets or sets whether to extend fillet to all faces tangent to the selected face or edge."""
		return self._instance.PropagateToTangentFaces

	@propagate_to_tangent_faces.setter
	def propagate_to_tangent_faces(self, value):
		"""Gets or sets whether to extend fillet to all faces tangent to the selected face or edge."""
		self._instance.PropagateToTangentFaces = value

	@property
	def reverse_face_normal(self):
		"""Gets or sets the Reverse Face Normal option when creating a face fillet between surface bodies."""
		return self._instance.ReverseFaceNormal

	@reverse_face_normal.setter
	def reverse_face_normal(self, value):
		"""Gets or sets the Reverse Face Normal option when creating a face fillet between surface bodies."""
		self._instance.ReverseFaceNormal = value

	@property
	def round_corners(self):
		"""Gets or sets whether to round the corners of this simple fillet feature."""
		return self._instance.RoundCorners

	@round_corners.setter
	def round_corners(self, value):
		"""Gets or sets whether to round the corners of this simple fillet feature."""
		self._instance.RoundCorners = value

	@property
	def trim_and_attach_surfaces(self):
		"""Gets or sets the Trim surfaces option for surface face fillets."""
		return self._instance.TrimAndAttachSurfaces

	@trim_and_attach_surfaces.setter
	def trim_and_attach_surfaces(self, value):
		"""Gets or sets the Trim surfaces option for surface face fillets."""
		self._instance.TrimAndAttachSurfaces = value

	@property
	def type(self):
		"""Gets the type of simple fillet feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the type of simple fillet feature."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define a simple fillet feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define a simple fillet feature."""
		self._instance.AccessSelections = value

	@property
	def get_conic_rho_or_radius(self):
		"""Gets the conic rho or radius of this fillet/chamfer."""
		return self._instance.GetConicRhoOrRadius

	@get_conic_rho_or_radius.setter
	def get_conic_rho_or_radius(self, value):
		"""Gets the conic rho or radius of this fillet/chamfer."""
		self._instance.GetConicRhoOrRadius = value

	@property
	def get_distance(self):
		"""Gets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer."""
		return self._instance.GetDistance

	@get_distance.setter
	def get_distance(self, value):
		"""Gets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer."""
		self._instance.GetDistance = value

	@property
	def get_edge_count(self):
		"""Gets the number of edges on which to create a simple radius fillet."""
		return self._instance.GetEdgeCount

	@get_edge_count.setter
	def get_edge_count(self, value):
		"""Gets the number of edges on which to create a simple radius fillet."""
		self._instance.GetEdgeCount = value

	@property
	def get_face_count(self):
		"""Gets the number of faces on which to create a simple radius fillet."""
		return self._instance.GetFaceCount

	@get_face_count.setter
	def get_face_count(self, value):
		"""Gets the number of faces on which to create a simple radius fillet."""
		self._instance.GetFaceCount = value

	@property
	def get_faces(self):
		"""Gets the faces on which to create a simple fillet."""
		return self._instance.GetFaces

	@get_faces.setter
	def get_faces(self, value):
		"""Gets the faces on which to create a simple fillet."""
		self._instance.GetFaces = value

	@property
	def get_feature_count(self):
		"""Gets the number of features on which to create a simple radius fillet."""
		return self._instance.GetFeatureCount

	@get_feature_count.setter
	def get_feature_count(self, value):
		"""Gets the number of features on which to create a simple radius fillet."""
		self._instance.GetFeatureCount = value

	@property
	def get_fillet_item_at_index(self):
		"""Gets the fillet item at the specified index."""
		return self._instance.GetFilletItemAtIndex

	@get_fillet_item_at_index.setter
	def get_fillet_item_at_index(self, value):
		"""Gets the fillet item at the specified index."""
		self._instance.GetFilletItemAtIndex = value

	@property
	def get_hold_line_count(self):
		"""Gets the number of hold lines (boundaries) for a face blend fillet feature."""
		return self._instance.GetHoldLineCount

	@get_hold_line_count.setter
	def get_hold_line_count(self, value):
		"""Gets the number of hold lines (boundaries) for a face blend fillet feature."""
		self._instance.GetHoldLineCount = value

	@property
	def get_loop_count(self):
		"""Gets the number of loops on which to create a single radius fillet."""
		return self._instance.GetLoopCount

	@get_loop_count.setter
	def get_loop_count(self, value):
		"""Gets the number of loops on which to create a single radius fillet."""
		self._instance.GetLoopCount = value

	@property
	def get_partial_edge_fillet_data(self):
		"""Gets the partial edge fillet data for the specified edge."""
		return self._instance.GetPartialEdgeFilletData

	@get_partial_edge_fillet_data.setter
	def get_partial_edge_fillet_data(self, value):
		"""Gets the partial edge fillet data for the specified edge."""
		self._instance.GetPartialEdgeFilletData = value

	@property
	def get_radius(self):
		"""Gets the radius at the specified fillet/chamfer item."""
		return self._instance.GetRadius

	@get_radius.setter
	def get_radius(self, value):
		"""Gets the radius at the specified fillet/chamfer item."""
		self._instance.GetRadius = value

	@property
	def get_setback_distance_count(self):
		"""Gets the number of setback distances for the specified vertex on this simple fillet feature."""
		return self._instance.GetSetbackDistanceCount

	@get_setback_distance_count.setter
	def get_setback_distance_count(self, value):
		"""Gets the number of setback distances for the specified vertex on this simple fillet feature."""
		self._instance.GetSetbackDistanceCount = value

	@property
	def get_setback_vertex_distance(self):
		"""Gets the setback distance for the specified vertex on this simple fillet feature."""
		return self._instance.GetSetbackVertexDistance

	@get_setback_vertex_distance.setter
	def get_setback_vertex_distance(self, value):
		"""Gets the setback distance for the specified vertex on this simple fillet feature."""
		self._instance.GetSetbackVertexDistance = value

	@property
	def get_setback_vertices(self):
		"""Gets the setback vertices for this simple fillet feature."""
		return self._instance.GetSetbackVertices

	@get_setback_vertices.setter
	def get_setback_vertices(self, value):
		"""Gets the setback vertices for this simple fillet feature."""
		self._instance.GetSetbackVertices = value

	@property
	def get_setback_vertices_count(self):
		"""Gets the number of setback vertices for this simple fillet feature."""
		return self._instance.GetSetbackVerticesCount

	@get_setback_vertices_count.setter
	def get_setback_vertices_count(self, value):
		"""Gets the number of setback vertices for this simple fillet feature."""
		self._instance.GetSetbackVerticesCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections used to define a simple fillet feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections used to define a simple fillet feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_conic_rho_or_radius(self):
		"""Gets the conic rho, conic radius, or circular radius of this fillet."""
		return self._instance.IGetConicRhoOrRadius

	@i_get_conic_rho_or_radius.setter
	def i_get_conic_rho_or_radius(self, value):
		"""Gets the conic rho, conic radius, or circular radius of this fillet."""
		self._instance.IGetConicRhoOrRadius = value

	@property
	def i_get_edges(self):
		"""Gets the edges on which to put a simple radius fillet."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Gets the edges on which to put a simple radius fillet."""
		self._instance.IGetEdges = value

	@property
	def i_get_faces(self):
		"""Gets the faces on which to create a simple radius fillet."""
		return self._instance.IGetFaces

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets the faces on which to create a simple radius fillet."""
		self._instance.IGetFaces = value

	@property
	def i_get_features(self):
		"""Gets the features on which to create a simple radius fillet."""
		return self._instance.IGetFeatures

	@i_get_features.setter
	def i_get_features(self, value):
		"""Gets the features on which to create a simple radius fillet."""
		self._instance.IGetFeatures = value

	@property
	def i_get_fillet_item_at_index(self):
		"""Gets the fillet item at the specified index."""
		return self._instance.IGetFilletItemAtIndex

	@i_get_fillet_item_at_index.setter
	def i_get_fillet_item_at_index(self, value):
		"""Gets the fillet item at the specified index."""
		self._instance.IGetFilletItemAtIndex = value

	@property
	def i_get_hold_lines(self):
		"""Gets the hold lines (boundaries) for a face blend fillet feature."""
		return self._instance.IGetHoldLines

	@i_get_hold_lines.setter
	def i_get_hold_lines(self, value):
		"""Gets the hold lines (boundaries) for a face blend fillet feature."""
		self._instance.IGetHoldLines = value

	@property
	def i_get_loops(self):
		"""Gets the loops on which to create a simple radius fillet."""
		return self._instance.IGetLoops

	@i_get_loops.setter
	def i_get_loops(self, value):
		"""Gets the loops on which to create a simple radius fillet."""
		self._instance.IGetLoops = value

	@property
	def i_get_radius(self):
		"""Gets the radius value for specified fillet item."""
		return self._instance.IGetRadius

	@i_get_radius.setter
	def i_get_radius(self, value):
		"""Gets the radius value for specified fillet item."""
		self._instance.IGetRadius = value

	@property
	def i_get_setback_vertex_distance(self):
		"""Gets the setback distance for the specified vertex on this simple fillet feature."""
		return self._instance.IGetSetbackVertexDistance

	@i_get_setback_vertex_distance.setter
	def i_get_setback_vertex_distance(self, value):
		"""Gets the setback distance for the specified vertex on this simple fillet feature."""
		self._instance.IGetSetbackVertexDistance = value

	@property
	def i_get_setback_vertices(self):
		"""Gets the setback vertices for this simple fillet feature."""
		return self._instance.IGetSetbackVertices

	@i_get_setback_vertices.setter
	def i_get_setback_vertices(self, value):
		"""Gets the setback vertices for this simple fillet feature."""
		self._instance.IGetSetbackVertices = value

	@property
	def initialize(self):
		"""Initializes this simple fillet feature to the specified type."""
		return self._instance.Initialize

	@initialize.setter
	def initialize(self, value):
		"""Initializes this simple fillet feature to the specified type."""
		self._instance.Initialize = value

	@property
	def i_set_conic_rho_or_radius(self):
		"""Sets the conic rho, conic radius, or circular radius of this fillet."""
		return self._instance.ISetConicRhoOrRadius

	@i_set_conic_rho_or_radius.setter
	def i_set_conic_rho_or_radius(self, value):
		"""Sets the conic rho, conic radius, or circular radius of this fillet."""
		self._instance.ISetConicRhoOrRadius = value

	@property
	def i_set_edges(self):
		"""Sets the edges on which to create a simple radius fillet."""
		return self._instance.ISetEdges

	@i_set_edges.setter
	def i_set_edges(self, value):
		"""Sets the edges on which to create a simple radius fillet."""
		self._instance.ISetEdges = value

	@property
	def i_set_faces(self):
		"""Sets the faces on which to create a simple radius fillet."""
		return self._instance.ISetFaces

	@i_set_faces.setter
	def i_set_faces(self, value):
		"""Sets the faces on which to create a simple radius fillet."""
		self._instance.ISetFaces = value

	@property
	def i_set_features(self):
		"""Sets the features on which to create a simple radius fillet."""
		return self._instance.ISetFeatures

	@i_set_features.setter
	def i_set_features(self, value):
		"""Sets the features on which to create a simple radius fillet."""
		self._instance.ISetFeatures = value

	@property
	def i_set_hold_lines(self):
		"""Sets the hold lines (boundaries) for this face blend fillet feature."""
		return self._instance.ISetHoldLines

	@i_set_hold_lines.setter
	def i_set_hold_lines(self, value):
		"""Sets the hold lines (boundaries) for this face blend fillet feature."""
		self._instance.ISetHoldLines = value

	@property
	def i_set_loops(self):
		"""Sets the loops on which to put a simple radius fillet."""
		return self._instance.ISetLoops

	@i_set_loops.setter
	def i_set_loops(self, value):
		"""Sets the loops on which to put a simple radius fillet."""
		self._instance.ISetLoops = value

	@property
	def i_set_radius(self):
		"""Sets the radius value for specified fillet item."""
		return self._instance.ISetRadius

	@i_set_radius.setter
	def i_set_radius(self, value):
		"""Sets the radius value for specified fillet item."""
		self._instance.ISetRadius = value

	@property
	def i_set_setback_vertex_distance(self):
		"""Sets the setback distance for the specified vertex and its edges on this simple fillet feature."""
		return self._instance.ISetSetbackVertexDistance

	@i_set_setback_vertex_distance.setter
	def i_set_setback_vertex_distance(self, value):
		"""Sets the setback distance for the specified vertex and its edges on this simple fillet feature."""
		self._instance.ISetSetbackVertexDistance = value

	@property
	def i_set_setback_vertices(self):
		"""Sets the setback vertices for this simple fillet feature."""
		return self._instance.ISetSetbackVertices

	@i_set_setback_vertices.setter
	def i_set_setback_vertices(self, value):
		"""Sets the setback vertices for this simple fillet feature."""
		self._instance.ISetSetbackVertices = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the simple fillet feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the simple fillet feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def repair_missing_references(self):
		"""Finds missing references in this fillet/chamfer and reassigns them to new edges."""
		return self._instance.RepairMissingReferences

	@repair_missing_references.setter
	def repair_missing_references(self, value):
		"""Finds missing references in this fillet/chamfer and reassigns them to new edges."""
		self._instance.RepairMissingReferences = value

	@property
	def set_conic_rho_or_radius(self):
		"""Sets the conic rho or radius of this fillet/chamfer."""
		return self._instance.SetConicRhoOrRadius

	@set_conic_rho_or_radius.setter
	def set_conic_rho_or_radius(self, value):
		"""Sets the conic rho or radius of this fillet/chamfer."""
		self._instance.SetConicRhoOrRadius = value

	@property
	def set_distance(self):
		"""Sets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer."""
		return self._instance.SetDistance

	@set_distance.setter
	def set_distance(self, value):
		"""Sets the Distance 2 radius at the specified item of this asymmetric fillet/chamfer."""
		self._instance.SetDistance = value

	@property
	def set_faces(self):
		"""Sets the faces on which to create a simple fillet."""
		return self._instance.SetFaces

	@set_faces.setter
	def set_faces(self, value):
		"""Sets the faces on which to create a simple fillet."""
		self._instance.SetFaces = value

	@property
	def set_partial_edge_fillet_data(self):
		"""Sets the partial edge fillet data for the specified edge."""
		return self._instance.SetPartialEdgeFilletData

	@set_partial_edge_fillet_data.setter
	def set_partial_edge_fillet_data(self, value):
		"""Sets the partial edge fillet data for the specified edge."""
		self._instance.SetPartialEdgeFilletData = value

	@property
	def set_radius(self):
		"""Sets the radius at the specified fillet item."""
		return self._instance.SetRadius

	@set_radius.setter
	def set_radius(self, value):
		"""Sets the radius at the specified fillet item."""
		self._instance.SetRadius = value

	@property
	def set_setback_vertex_distance(self):
		"""Sets the setback distances on fillet edges from the specified fillet corner vertex on this simple fillet feature."""
		return self._instance.SetSetbackVertexDistance

	@set_setback_vertex_distance.setter
	def set_setback_vertex_distance(self, value):
		"""Sets the setback distances on fillet edges from the specified fillet corner vertex on this simple fillet feature."""
		self._instance.SetSetbackVertexDistance = value

	@property
	def set_setback_vertices(self):
		"""Sets the setback vertices for this simple fillet feature."""
		return self._instance.SetSetbackVertices

	@set_setback_vertices.setter
	def set_setback_vertices(self, value):
		"""Sets the setback vertices for this simple fillet feature."""
		self._instance.SetSetbackVertices = value

