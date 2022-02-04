# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge_members.html
class IEdge:
	def __init__(self, parent=None):
		self._instance = parent

	def check(self):
		"""Gets whether the edge is a valid, and, if not, returns the faults."""
		# return self._instance.Check
		raise NotImplemented

	def create_wire_body(self):
		"""Creates a wire body from this edge."""
		# return self._instance.CreateWireBody
		raise NotImplemented

	def display(self, width, red, green, blue, highlight_state):
		"""
		Highlights this edge with the specified color.
		:param width: Highlight width
		:param red: Red value of RGB value for the color, between 0 and 1
		:param green: Green value of RGB value for the color, between 0 and 1
		:param blue: Blue value if RGB value for the color, between 0 and 1
		:param highlight_state: True if the edge is highlighted, false if not
		"""
		# return self._instance.Display(width, red, green, blue, highlight_state)
		raise NotImplemented

	def edge_in_face_sense(self, facedisp):
		"""
		Checks whether the edge and the loop lying on the specified face have the same direction (sense).
		:param facedisp: Face that the edge is on
		"""
		# return self._instance.EdgeInFaceSense(facedisp)
		raise NotImplemented

	def enum_co_edges(self):
		"""Lists the coedges that reference this edge."""
		# return self._instance.EnumCoEdges
		raise NotImplemented

	def evaluate(self, parameter, number_of_derivatives):
		"""
		Evaluates the edge for the specified U parameter.
		:param parameter: Curve parameter U value (see Remarks)
		:param number_of_derivatives: Number of derivatives (see Remarks)
		"""
		# return self._instance.Evaluate2(parameter, number_of_derivatives)
		raise NotImplemented

	def get_body(self):
		"""Gets the body for this edge."""
		# return self._instance.GetBody
		raise NotImplemented

	def get_closest_point_on(self, x, y, z):
		"""
		Uses the X,Y,Z input point and returns the closest point on the edge.
		:param x: X value of the input point
		:param y: Y value of the input point
		:param z: Z value of the input point
		"""
		# return self._instance.GetClosestPointOn(x, y, z)
		raise NotImplemented

	def get_co_edges(self):
		"""Gets the coedges that reference this edge."""
		# return self._instance.GetCoEdges
		raise NotImplemented

	def get_curve(self):
		"""Gets the underlying curve for this edge."""
		# return self._instance.GetCurve
		raise NotImplemented

	def get_curve_params(self):
		"""Gets a data object containing the curve parameters for this edge."""
		# return self._instance.GetCurveParams3
		raise NotImplemented

	def get_end_vertex(self):
		"""Gets the ending vertex for this edge."""
		# return self._instance.GetEndVertex
		raise NotImplemented

	def get_i_d(self):
		"""Gets the edge ID of this edge in an imported body."""
		# return self._instance.GetID
		raise NotImplemented

	def get_parameter(self, x, y, z):
		"""
		Gets the parameterization of the edge.
		:param x: X value
		:param y: Y value
		:param z: Z value
		"""
		# return self._instance.GetParameter(x, y, z)
		raise NotImplemented

	def get_start_vertex(self):
		"""Gets the starting vertex for this edge."""
		# return self._instance.GetStartVertex
		raise NotImplemented

	def get_tangent_edges(self):
		"""Gets all of the edges tangent to this edge."""
		# return self._instance.GetTangentEdges
		raise NotImplemented

	def get_tangent_edges_count(self):
		"""Gets the number of edges tangent to this edge."""
		# return self._instance.GetTangentEdgesCount
		raise NotImplemented

	def get_tracking_i_ds(self, tracking_cookie, tracking_i_ds):
		"""
		Gets the tracking IDs assigned to this edge.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		:param tracking_i_ds: Array of tracking IDs on this edge
		"""
		# return self._instance.GetTrackingIDs(tracking_cookie, tracking_i_ds)
		raise NotImplemented

	def get_tracking_i_ds_count(self, tracking_cookie):
		"""
		Gets the number of tracking IDs on this edge.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		"""
		# return self._instance.GetTrackingIDsCount(tracking_cookie)
		raise NotImplemented

	def get_two_adjacent_faces(self):
		"""Gets the two faces adjacent to an edge."""
		# return self._instance.GetTwoAdjacentFaces2
		raise NotImplemented

	def highlight(self, state):
		"""
		Add highlights or removes highlights from this edge.
		:param state: True adds highlights to this edge, false removes highlights from this edge
		"""
		# return self._instance.Highlight(state)
		raise NotImplemented

	def i_edge_in_face_sense(self, facedisp):
		"""
		Checks whether the edge and the loop lying on the specified face have the same direction (sense).
		:param facedisp: Pointer to the face that the edge is on
		"""
		# return self._instance.IEdgeInFaceSense2(facedisp)
		raise NotImplemented

	def i_evaluate(self, parameter, number_of_derivatives):
		"""
		Evaluates the edge for the specified U parameter.
		:param parameter: Curve parameter U value (see Remarks)
		:param number_of_derivatives: Number of derivatives (see Remarks)
		"""
		# return self._instance.IEvaluate2(parameter, number_of_derivatives)
		raise NotImplemented

	def i_get_closest_point_on(self, x, y, z):
		"""
		Uses the X,Y,Z input point and returns the closest point on the edge.
		:param x: X value of the input point
		:param y: Y value of the input point
		:param z: Z value of the input point
		"""
		# return self._instance.IGetClosestPointOn(x, y, z)
		raise NotImplemented

	def i_get_curve(self):
		"""Gets the underlying curve for this edge."""
		# return self._instance.IGetCurve
		raise NotImplemented

	def i_get_curve_params(self):
		"""Returns the curve parameters for this edge, including the edge and curve direction (sense)."""
		# return self._instance.IGetCurveParams2
		raise NotImplemented

	def i_get_end_vertex(self):
		"""Gets the ending vertex for this edge."""
		# return self._instance.IGetEndVertex
		raise NotImplemented

	def i_get_parameter(self, x, y, z):
		"""
		Gets the parameterization of the edge.
		:param x: X value
		:param y: Y value
		:param z: Z value
		"""
		# return self._instance.IGetParameter(x, y, z)
		raise NotImplemented

	def i_get_start_vertex(self):
		"""Gets the starting vertex for this edge."""
		# return self._instance.IGetStartVertex
		raise NotImplemented

	def i_get_tangent_edges(self, count):
		"""
		Gets all of the edges tangent to this edge.
		:param count: Number of tangent edges
		"""
		# return self._instance.IGetTangentEdges(count)
		raise NotImplemented

	def i_get_tracking_i_ds(self, tracking_cookie, count, tracking_i_ds):
		"""
		Gets the tracking IDs assigned to this edge.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		:param count: Number of tracking IDs on this edge
		:param tracking_i_ds: 
in-process, unmanaged C++: Pointer to an array of tracking IDs on this edge 
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IGetTrackingIDs(tracking_cookie, count, tracking_i_ds)
		raise NotImplemented

	def i_get_two_adjacent_faces(self, face1, face2):
		"""
		Gets the two faces adjacent to an edge.
		:param face1: Pointer to the first adjacent face
		:param face2: Pointer to the second adjacent face
		"""
		# return self._instance.IGetTwoAdjacentFaces2(face1, face2)
		raise NotImplemented

	def is_param_reversed(self):
		"""Gets whether the edge and its underlying curve have the same parameterization or if the direction is reversed."""
		# return self._instance.IsParamReversed
		raise NotImplemented

	def is_tolerant(self, tolerance):
		"""
		Gets whether an edge is tolerant and its tolerance value.
		:param tolerance: Edge tolerance or gap in meters
		"""
		# return self._instance.IsTolerant(tolerance)
		raise NotImplemented

	def remove_id(self):
		"""Removes the edge ID assigned to this edge of an imported body."""
		# return self._instance.RemoveId
		raise NotImplemented

	def remove_redundant_topology(self):
		"""Removes redundant topology from the edge."""
		# return self._instance.RemoveRedundantTopology
		raise NotImplemented

	def remove_tracking_i_d(self, tracking_cookie):
		"""
		Removes a tracking ID assigned to this edge.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		"""
		# return self._instance.RemoveTrackingID(tracking_cookie)
		raise NotImplemented

	def set_id(self, id_in):
		"""
		Sets the edge ID of this edge of an imported body.
		:param id_in: Edge ID of this edge of an imported body
		"""
		# return self._instance.SetId(id_in)
		raise NotImplemented

	def set_tracking_i_d(self, tracking_cookie, tracking_i_d):
		"""
		Assigns a tracking ID to this edge.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		:param tracking_i_d: 
Application-defined value for the tracking ID




Value
Action

>0
Edge is tracked

0
Tracking of edge is stopped

		"""
		# return self._instance.SetTrackingID(tracking_cookie, tracking_i_d)
		raise NotImplemented

