# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex_members.html
class IVertex:
	def __init__(self, parent=None):
		self._instance = parent

	def display(self, top_doc, color, scale, highlight_state):
		"""
		Highlights the vertex in the specified color.
		:param top_doc: Model in which to display the vertex
		:param color: COLORREF value for highlighting
		:param scale: Radius of the circle used to display the vertex
NOTE: Vertex is displayed as a circle. By default, the radius is 4 pixels. Therefore, a scale of 1 is equal to 4 pixels.
		:param highlight_state: True to highlight the vertex, false to not
		"""
		# return self._instance.Display(top_doc, color, scale, highlight_state)
		raise NotImplemented

	def enum_edges(self):
		"""Gets a list of enumerated edges corresponding to this vertex."""
		# return self._instance.EnumEdges
		raise NotImplemented

	def enum_edges_oriented(self):
		"""Gets the enumerated edges and orients them per coedge in the direction corresponding to this vertex."""
		# return self._instance.EnumEdgesOriented
		raise NotImplemented

	def get_adjacent_faces(self):
		"""Gets the faces adjacent to this vertex."""
		# return self._instance.GetAdjacentFaces
		raise NotImplemented

	def get_closest_point_on(self, x, y, z):
		"""
		Gets the closest point on the vertex using the X, Y, Z input point.
		:param x: X value of the input point
		:param y: Y value of the input point
		:param z: Z value of the input point
		"""
		# return self._instance.GetClosestPointOn(x, y, z)
		raise NotImplemented

	def get_edges(self):
		"""Gets a list of enumerated edges corresponding to this vertex."""
		# return self._instance.GetEdges
		raise NotImplemented

	def get_edges_oriented(self):
		"""Gets the enumerated edges and orients them per coedge in the direction corresponding to this vertex."""
		# return self._instance.GetEdgesOriented
		raise NotImplemented

	def get_point(self):
		"""Gets the point corresponding to this vertex."""
		# return self._instance.GetPoint
		raise NotImplemented

	def get_tracking_i_ds(self, tracking_cookie, tracking_i_ds):
		"""
		Gets the tracking IDs assigned to this vertex.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		:param tracking_i_ds: Array of tracking IDs on this vertex
		"""
		# return self._instance.GetTrackingIDs(tracking_cookie, tracking_i_ds)
		raise NotImplemented

	def get_tracking_i_ds_count(self, tracking_cookie):
		"""
		Gets the number of tracking IDs assigned to this vertex.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		"""
		# return self._instance.GetTrackingIDsCount(tracking_cookie)
		raise NotImplemented

	def i_get_adjacent_faces(self, n_face_count):
		"""
		Gets the faces adjacent to this vertex.
		:param n_face_count: Number of adjacent faces
		"""
		# return self._instance.IGetAdjacentFaces(n_face_count)
		raise NotImplemented

	def i_get_adjacent_faces_count(self):
		"""Gets the number of faces adjacent to this vertex."""
		# return self._instance.IGetAdjacentFacesCount
		raise NotImplemented

	def i_get_closest_point_on(self, x, y, z):
		"""
		Gets the closest point on the vertex using the X, Y, Z input point.
		:param x: X value of the input point
		:param y: Y value of the input point
		:param z: Z value of the input point
		"""
		# return self._instance.IGetClosestPointOn(x, y, z)
		raise NotImplemented

	def i_get_point(self):
		"""Gets the point corresponding to this vertex."""
		# return self._instance.IGetPoint
		raise NotImplemented

	def i_get_tracking_i_ds(self, tracking_cookie, count, tracking_i_ds):
		"""
		Gets the tracking IDs assigned to this vertex.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		:param count: Number of tracking IDs on this vertex
		:param tracking_i_ds: 
in-process, unmanaged C++: Pointer to an array of tracking IDs on this vertex 
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IGetTrackingIDs(tracking_cookie, count, tracking_i_ds)
		raise NotImplemented

	def is_tolerant(self, tolerance):
		"""
		Gets whether a vertex is tolerant and its tolerance value.
		:param tolerance: Vertex tolerance or gap in meters
		"""
		# return self._instance.IsTolerant(tolerance)
		raise NotImplemented

	def remove_tracking_i_d(self, tracking_cookie):
		"""
		Removes a tracking ID assigned to this vertex.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
		"""
		# return self._instance.RemoveTrackingID(tracking_cookie)
		raise NotImplemented

	def set_tracking_i_d(self, tracking_cookie, tracking_i_d):
		"""
		Assigns a tracking ID to this vertex.
		:param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition

		:param tracking_i_d: Cookie obtained from ISldWorks::RegisterTrackingDefinition

		"""
		# return self._instance.SetTrackingID(tracking_cookie, tracking_i_d)
		raise NotImplemented

