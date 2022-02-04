# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html
class ILoop2:
	def __init__(self, parent=None):
		self._instance = parent

	def enum_co_edges(self):
		"""Enumerates the coedges in a loop."""
		# return self._instance.EnumCoEdges
		raise NotImplemented

	def enum_edges(self):
		"""Enumerates the edges in a face."""
		# return self._instance.EnumEdges
		raise NotImplemented

	def get_co_edge_count(self):
		"""Gets the number of coedges in this loop."""
		# return self._instance.GetCoEdgeCount
		raise NotImplemented

	def get_co_edges(self):
		"""Gets the coedges in this loop."""
		# return self._instance.GetCoEdges
		raise NotImplemented

	def get_edge_count(self):
		"""Gets the number of edges in the loop."""
		# return self._instance.GetEdgeCount
		raise NotImplemented

	def get_edges(self):
		"""Gets all the edges in the loop."""
		# return self._instance.GetEdges
		raise NotImplemented

	def get_face(self):
		"""Gets the face containing this loop."""
		# return self._instance.GetFace
		raise NotImplemented

	def get_first_co_edge(self):
		"""Gets the first coedge of the loop."""
		# return self._instance.GetFirstCoEdge
		raise NotImplemented

	def get_next(self):
		"""Gets the next loop on the face."""
		# return self._instance.GetNext
		raise NotImplemented

	def get_tracking_i_ds(self, tracking_cookie, tracking_i_ds):
		"""
		Gets the tracking IDs assigned to this loop.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		:param tracking_i_ds: Array of tracking IDs on this loop
		"""
		# return self._instance.GetTrackingIDs(tracking_cookie, tracking_i_ds)
		raise NotImplemented

	def get_tracking_i_ds_count(self, tracking_cookie):
		"""
		Gets the number of tracking IDs on this loop.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		"""
		# return self._instance.GetTrackingIDsCount(tracking_cookie)
		raise NotImplemented

	def get_vertex_count(self):
		"""Gets the number of vertices in the loop."""
		# return self._instance.GetVertexCount
		raise NotImplemented

	def get_vertices(self):
		"""Gets the vertices in this loop."""
		# return self._instance.GetVertices
		raise NotImplemented

	def i_get_co_edges(self, num_co_edges):
		"""
		Gets the coedges in this loop.
		:param num_co_edges: Number of coedges in this loop
		"""
		# return self._instance.IGetCoEdges(num_co_edges)
		raise NotImplemented

	def i_get_edges(self):
		"""Gets all the edges in the loop."""
		# return self._instance.IGetEdges
		raise NotImplemented

	def i_get_face(self):
		"""Gets the face containing this loop."""
		# return self._instance.IGetFace
		raise NotImplemented

	def i_get_first_co_edge(self):
		"""Gets the first coedge in the loop."""
		# return self._instance.IGetFirstCoEdge
		raise NotImplemented

	def i_get_next(self):
		"""Gets the next loop in the face."""
		# return self._instance.IGetNext
		raise NotImplemented

	def i_get_tracking_i_ds(self, tracking_cookie, count, tracking_i_ds):
		"""
		Gets the tracking IDs assigned to this loop.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		:param count: Number of tracking IDs on this loop
		:param tracking_i_ds: 
in-process, unmanaged C++: Pointer to an array of tracking IDs on this loop 
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IGetTrackingIDs(tracking_cookie, count, tracking_i_ds)
		raise NotImplemented

	def i_get_vertices(self, num_vertices, vertices):
		"""
		Gets the vertices in this loop.
		:param num_vertices: Number of vertices in this loop
		:param vertices: 
in-process, unmanaged C++: Pointer to an array of vertices for this loop
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IGetVertices(num_vertices, vertices)
		raise NotImplemented

	def i_revolve_planar_loop(self, x, y, z, axisx, axisy, axisz, rev_angle, stop_faces_out):
		"""
		Creates a body by revolving a planar loop around an axis.
		:param x: x coordinate of the axis point
		:param y: y coordinate of the axis point
		:param z: z coordinate of the axis point
		:param axisx: Direction along x
		:param axisy: Direction along y
		:param axisz: Direction along z
		:param rev_angle: Angle of revolution in radians
		:param stop_faces_out: Array of two stop faces
		"""
		# return self._instance.IRevolvePlanarLoop(x, y, z, axisx, axisy, axisz, rev_angle, stop_faces_out)
		raise NotImplemented

	def is_outer(self):
		"""Indicates whether the loop is the outermost loop on the face."""
		# return self._instance.IsOuter
		raise NotImplemented

	def is_singular(self):
		"""Gets whether this loop is singular."""
		# return self._instance.IsSingular
		raise NotImplemented

	def i_sweep_planar_loop(self, x, y, z, draft_angle, stop_faces_out):
		"""
		Creates a temporary body by sweeping a planar loop along a vector.
		:param x: X component of the sweep vector
		:param y: Y component of the sweep vector
		:param z: Z component of the sweep vector
		:param draft_angle: Draft angle for the faces on the side of this swept body
		:param stop_faces_out: Array of two stop faces
		"""
		# return self._instance.ISweepPlanarLoop(x, y, z, draft_angle, stop_faces_out)
		raise NotImplemented

	def remove_tracking_i_d(self, tracking_cookie):
		"""
		Removes a tracking ID assigned to this loop.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		"""
		# return self._instance.RemoveTrackingID(tracking_cookie)
		raise NotImplemented

	def revolve_planar_loop(self, x, y, z, axisx, axisy, axisz, rev_angle):
		"""
		Creates a body by revolving a planar loop around an axis.
		:param x: x coordinate of the axis point
		:param y: y coordinate of the axis point
		:param z: z coordinate of the axis point
		:param axisx: Direction along x
		:param axisy: Direction along y
		:param axisz: Direction along z
		:param rev_angle: Angle of revolution in radians
		"""
		# return self._instance.RevolvePlanarLoop(x, y, z, axisx, axisy, axisz, rev_angle)
		raise NotImplemented

	def select(self, edge, append, selection_data):
		"""
		Selects a loop in the graphics area.
		:param edge: Edge of the loop (see Remarks)
		:param append: True to append this selection to the selection list, false to replace the selection list with this selection
		:param selection_data: ISelectData object
		"""
		# return self._instance.Select(edge, append, selection_data)
		raise NotImplemented

	def set_tracking_i_d(self, tracking_cookie, tracking_i_d):
		"""
		Assigns a tracking ID to this loop.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		:param tracking_i_d: Application-defined value for the tracking ID




Value
Action

>0
Loop is tracked

0
Tracking of loop is stopped
		"""
		# return self._instance.SetTrackingID(tracking_cookie, tracking_i_d)
		raise NotImplemented

	def sweep_planar_loop(self, x, y, z, draft_angle):
		"""
		Creates a temporary body by sweeping a planar loop along a vector.
		:param x: X component of the sweep vector
		:param y: Y component of the sweep vector
		:param z: Z component of the sweep vector
		:param draft_angle: Draft angle for the faces on the side of this swept body
		"""
		# return self._instance.SweepPlanarLoop(x, y, z, draft_angle)
		raise NotImplemented

