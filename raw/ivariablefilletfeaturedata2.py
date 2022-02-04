# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVariableFilletFeatureData2_members.html
class IVariableFilletFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def asymmetric_fillet(self):
		"""Gets or sets whether this variable radius fillet is asymmetric."""
		return self._instance.AsymmetricFillet

	@asymmetric_fillet.setter
	def asymmetric_fillet(self, value):
		"""Gets or sets whether this variable radius fillet is asymmetric."""
		self._instance.AsymmetricFillet = value

	@property
	def conic_type_for_cross_section_profile(self):
		"""Gets or sets the type of profile for this fillet."""
		return self._instance.ConicTypeForCrossSectionProfile

	@conic_type_for_cross_section_profile.setter
	def conic_type_for_cross_section_profile(self, value):
		"""Gets or sets the type of profile for this fillet."""
		self._instance.ConicTypeForCrossSectionProfile = value

	@property
	def curvature_continuous(self):
		"""Gets or sets whether to create a smoother curvature between adjacent surfaces for this variable radius fillet feature."""
		return self._instance.CurvatureContinuous

	@curvature_continuous.setter
	def curvature_continuous(self, value):
		"""Gets or sets whether to create a smoother curvature between adjacent surfaces for this variable radius fillet feature."""
		self._instance.CurvatureContinuous = value

	@property
	def default_conic_rho_or_radius(self):
		"""Gets or sets the default conic rho or conic radius of this fillet."""
		return self._instance.DefaultConicRhoOrRadius

	@default_conic_rho_or_radius.setter
	def default_conic_rho_or_radius(self, value):
		"""Gets or sets the default conic rho or conic radius of this fillet."""
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
		"""Gets or sets the default radius for this symmetric fillet or the default Distance 1 radius for this asymmetric fillet."""
		return self._instance.DefaultRadius

	@default_radius.setter
	def default_radius(self, value):
		"""Gets or sets the default radius for this symmetric fillet or the default Distance 1 radius for this asymmetric fillet."""
		self._instance.DefaultRadius = value

	@property
	def fillet_edge_count(self):
		"""Gets the number of edges to fillet."""
		return self._instance.FilletEdgeCount

	@fillet_edge_count.setter
	def fillet_edge_count(self, value):
		"""Gets the number of edges to fillet."""
		self._instance.FilletEdgeCount = value

	@property
	def overflow_type(self):
		"""Gets or sets the overflow type for this variable fillet feature."""
		return self._instance.OverflowType

	@overflow_type.setter
	def overflow_type(self, value):
		"""Gets or sets the overflow type for this variable fillet feature."""
		self._instance.OverflowType = value

	@property
	def propagate_feature_to_parts(self):
		"""Gets or sets whether to extend the fillet feature to all affected parts in the assembly."""
		return self._instance.PropagateFeatureToParts

	@propagate_feature_to_parts.setter
	def propagate_feature_to_parts(self, value):
		"""Gets or sets whether to extend the fillet feature to all affected parts in the assembly."""
		self._instance.PropagateFeatureToParts = value

	@property
	def propagate_to_tangent_faces(self):
		"""Gets or sets whether to extend the fillet to all faces tangent to the selected face or edge."""
		return self._instance.PropagateToTangentFaces

	@propagate_to_tangent_faces.setter
	def propagate_to_tangent_faces(self, value):
		"""Gets or sets whether to extend the fillet to all faces tangent to the selected face or edge."""
		self._instance.PropagateToTangentFaces = value

	@property
	def transition_type(self):
		"""Gets or sets the type of transition between this variable fillet and an adjacent fillet."""
		return self._instance.TransitionType

	@transition_type.setter
	def transition_type(self, value):
		"""Gets or sets the type of transition between this variable fillet and an adjacent fillet."""
		self._instance.TransitionType = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define the variable fillet feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define the variable fillet feature."""
		self._instance.AccessSelections = value

	@property
	def get_conic_rho_or_radius(self):
		"""Gets the conic rho, conic radius, or circular radius of this fillet."""
		return self._instance.GetConicRhoOrRadius

	@get_conic_rho_or_radius.setter
	def get_conic_rho_or_radius(self, value):
		"""Gets the conic rho, conic radius, or circular radius of this fillet."""
		self._instance.GetConicRhoOrRadius = value

	@property
	def get_conic_rho_or_radius(self):
		"""Gets the conic rho or radius at the specified vertex."""
		return self._instance.GetConicRhoOrRadius2

	@get_conic_rho_or_radius.setter
	def get_conic_rho_or_radius(self, value):
		"""Gets the conic rho or radius at the specified vertex."""
		self._instance.GetConicRhoOrRadius2 = value

	@property
	def get_control_point_conic_rho_or_radius_at_index(self):
		"""Gets the conic rho or radius at the specified control point."""
		return self._instance.GetControlPointConicRhoOrRadiusAtIndex

	@get_control_point_conic_rho_or_radius_at_index.setter
	def get_control_point_conic_rho_or_radius_at_index(self, value):
		"""Gets the conic rho or radius at the specified control point."""
		self._instance.GetControlPointConicRhoOrRadiusAtIndex = value

	@property
	def get_control_point_distance_at_index(self):
		"""Gets the Distance 2 radius at the specified control point for the asymmetric fillet."""
		return self._instance.GetControlPointDistanceAtIndex

	@get_control_point_distance_at_index.setter
	def get_control_point_distance_at_index(self, value):
		"""Gets the Distance 2 radius at the specified control point for the asymmetric fillet."""
		self._instance.GetControlPointDistanceAtIndex = value

	@property
	def get_control_point_radius_at_index(self):
		"""Gets the radius at the specified control point."""
		return self._instance.GetControlPointRadiusAtIndex

	@get_control_point_radius_at_index.setter
	def get_control_point_radius_at_index(self, value):
		"""Gets the radius at the specified control point."""
		self._instance.GetControlPointRadiusAtIndex = value

	@property
	def get_control_points_count(self):
		"""Gets the number of intermediate control points on this variable fillet feature."""
		return self._instance.GetControlPointsCount

	@get_control_points_count.setter
	def get_control_points_count(self, value):
		"""Gets the number of intermediate control points on this variable fillet feature."""
		self._instance.GetControlPointsCount = value

	@property
	def get_distance(self):
		"""Gets the Distance 2 radius for this asymmetric fillet."""
		return self._instance.GetDistance

	@get_distance.setter
	def get_distance(self, value):
		"""Gets the Distance 2 radius for this asymmetric fillet."""
		self._instance.GetDistance = value

	@property
	def get_fillet_edge_at_index(self):
		"""Gets the fillet edge at the specified index."""
		return self._instance.GetFilletEdgeAtIndex

	@get_fillet_edge_at_index.setter
	def get_fillet_edge_at_index(self, value):
		"""Gets the fillet edge at the specified index."""
		self._instance.GetFilletEdgeAtIndex = value

	@property
	def get_radius(self):
		"""Gets the value of the Distance 1 radius at the specified vertex."""
		return self._instance.GetRadius2

	@get_radius.setter
	def get_radius(self, value):
		"""Gets the value of the Distance 1 radius at the specified vertex."""
		self._instance.GetRadius2 = value

	@property
	def get_setback_distance_count(self):
		"""Gets the number of setback distances for the specified vertex on this variable fillet feature."""
		return self._instance.GetSetbackDistanceCount

	@get_setback_distance_count.setter
	def get_setback_distance_count(self, value):
		"""Gets the number of setback distances for the specified vertex on this variable fillet feature."""
		self._instance.GetSetbackDistanceCount = value

	@property
	def get_setback_vertex_distance(self):
		"""Gets the setback distance for the specified vertex on this variable fillet feature."""
		return self._instance.GetSetbackVertexDistance

	@get_setback_vertex_distance.setter
	def get_setback_vertex_distance(self, value):
		"""Gets the setback distance for the specified vertex on this variable fillet feature."""
		self._instance.GetSetbackVertexDistance = value

	@property
	def get_setback_vertices(self):
		"""Gets the setback vertices for this variable fillet feature."""
		return self._instance.GetSetbackVertices

	@get_setback_vertices.setter
	def get_setback_vertices(self, value):
		"""Gets the setback vertices for this variable fillet feature."""
		self._instance.GetSetbackVertices = value

	@property
	def get_setback_vertices_count(self):
		"""Gets the number of setback vertices for this variable fillet feature."""
		return self._instance.GetSetbackVerticesCount

	@get_setback_vertices_count.setter
	def get_setback_vertices_count(self, value):
		"""Gets the number of setback vertices for this variable fillet feature."""
		self._instance.GetSetbackVerticesCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections used to define the variable fillet feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections used to define the variable fillet feature."""
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
	def i_get_fillet_edge_at_index(self):
		"""Gets the fillet edge at the specified index."""
		return self._instance.IGetFilletEdgeAtIndex

	@i_get_fillet_edge_at_index.setter
	def i_get_fillet_edge_at_index(self, value):
		"""Gets the fillet edge at the specified index."""
		self._instance.IGetFilletEdgeAtIndex = value

	@property
	def i_get_setback_vertex_distance(self):
		"""Gets the setback distance for the specified vertex on this variable fillet feature."""
		return self._instance.IGetSetbackVertexDistance

	@i_get_setback_vertex_distance.setter
	def i_get_setback_vertex_distance(self, value):
		"""Gets the setback distance for the specified vertex on this variable fillet feature."""
		self._instance.IGetSetbackVertexDistance = value

	@property
	def i_get_setback_vertices(self):
		"""Gets the setback vertices for this variable fillet feature."""
		return self._instance.IGetSetbackVertices

	@i_get_setback_vertices.setter
	def i_get_setback_vertices(self, value):
		"""Gets the setback vertices for this variable fillet feature."""
		self._instance.IGetSetbackVertices = value

	@property
	def i_set_conic_rho_or_radius(self):
		"""Sets the conic rho, conic radius, or circular radius of this fillet."""
		return self._instance.ISetConicRhoOrRadius

	@i_set_conic_rho_or_radius.setter
	def i_set_conic_rho_or_radius(self, value):
		"""Sets the conic rho, conic radius, or circular radius of this fillet."""
		self._instance.ISetConicRhoOrRadius = value

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
		"""Sets the setback distance for the specified vertex and its edges on this variable fillet feature."""
		return self._instance.ISetSetbackVertexDistance

	@i_set_setback_vertex_distance.setter
	def i_set_setback_vertex_distance(self, value):
		"""Sets the setback distance for the specified vertex and its edges on this variable fillet feature."""
		self._instance.ISetSetbackVertexDistance = value

	@property
	def i_set_setback_vertices(self):
		"""Sets the setback vertices for this variable fillet feature."""
		return self._instance.ISetSetbackVertices

	@i_set_setback_vertices.setter
	def i_set_setback_vertices(self, value):
		"""Sets the setback vertices for this variable fillet feature."""
		self._instance.ISetSetbackVertices = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the variable fillet feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the variable fillet feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_conic_rho_or_radius(self):
		"""Sets the conic rho or radius for the specified fillet item."""
		return self._instance.SetConicRhoOrRadius

	@set_conic_rho_or_radius.setter
	def set_conic_rho_or_radius(self, value):
		"""Sets the conic rho or radius for the specified fillet item."""
		self._instance.SetConicRhoOrRadius = value

	@property
	def set_control_point_conic_rho_or_radius_at_index(self):
		"""Sets the conic rho or radius at the specified control point."""
		return self._instance.SetControlPointConicRhoOrRadiusAtIndex

	@set_control_point_conic_rho_or_radius_at_index.setter
	def set_control_point_conic_rho_or_radius_at_index(self, value):
		"""Sets the conic rho or radius at the specified control point."""
		self._instance.SetControlPointConicRhoOrRadiusAtIndex = value

	@property
	def set_control_point_distance_at_index(self):
		"""Sets the Distance 2 radius at the specified control point for the asymmetric fillet."""
		return self._instance.SetControlPointDistanceAtIndex

	@set_control_point_distance_at_index.setter
	def set_control_point_distance_at_index(self, value):
		"""Sets the Distance 2 radius at the specified control point for the asymmetric fillet."""
		self._instance.SetControlPointDistanceAtIndex = value

	@property
	def set_control_point_radius_at_index(self):
		"""Sets the radius at the specified control point."""
		return self._instance.SetControlPointRadiusAtIndex

	@set_control_point_radius_at_index.setter
	def set_control_point_radius_at_index(self, value):
		"""Sets the radius at the specified control point."""
		self._instance.SetControlPointRadiusAtIndex = value

	@property
	def set_distance(self):
		"""Sets the Distance 2 radius for this asymmetric fillet."""
		return self._instance.SetDistance

	@set_distance.setter
	def set_distance(self, value):
		"""Sets the Distance 2 radius for this asymmetric fillet."""
		self._instance.SetDistance = value

	@property
	def set_radius(self):
		"""Sets the value of the Distance 1 radius at the specified vertex."""
		return self._instance.SetRadius

	@set_radius.setter
	def set_radius(self, value):
		"""Sets the value of the Distance 1 radius at the specified vertex."""
		self._instance.SetRadius = value

	@property
	def set_setback_vertex_distance(self):
		"""Sets the setback distances on fillet edges from the specified fillet corner vertex on this variable fillet feature."""
		return self._instance.SetSetbackVertexDistance

	@set_setback_vertex_distance.setter
	def set_setback_vertex_distance(self, value):
		"""Sets the setback distances on fillet edges from the specified fillet corner vertex on this variable fillet feature."""
		self._instance.SetSetbackVertexDistance = value

	@property
	def set_setback_vertices(self):
		"""Sets the setback vertices for this variable fillet feature."""
		return self._instance.SetSetbackVertices

	@set_setback_vertices.setter
	def set_setback_vertices(self, value):
		"""Sets the setback vertices for this variable fillet feature."""
		self._instance.SetSetbackVertices = value

