# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChamferFeatureData2_members.html
class IChamferFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def edge_chamfer_angle(self):
		"""Gets or sets the angle on the edge of the chamfer feature."""
		return self._instance.EdgeChamferAngle

	@edge_chamfer_angle.setter
	def edge_chamfer_angle(self, value):
		"""Gets or sets the angle on the edge of the chamfer feature."""
		self._instance.EdgeChamferAngle = value

	@property
	def edges(self):
		"""Gets or sets a list of the edges to which a chamfer is applied."""
		return self._instance.Edges

	@edges.setter
	def edges(self, value):
		"""Gets or sets a list of the edges to which a chamfer is applied."""
		self._instance.Edges = value

	@property
	def equal_distance(self):
		"""Gets or sets whether to specify a single value for distance or vertex."""
		return self._instance.EqualDistance

	@equal_distance.setter
	def equal_distance(self, value):
		"""Gets or sets whether to specify a single value for distance or vertex."""
		self._instance.EqualDistance = value

	@property
	def faces(self):
		"""Gets and sets a list of the faces to which a chamfer is applied."""
		return self._instance.Faces

	@faces.setter
	def faces(self, value):
		"""Gets and sets a list of the faces to which a chamfer is applied."""
		self._instance.Faces = value

	@property
	def i_vertex(self):
		"""Gets or sets the vertex to which a chamfer is applied."""
		return self._instance.IVertex

	@i_vertex.setter
	def i_vertex(self, value):
		"""Gets or sets the vertex to which a chamfer is applied."""
		self._instance.IVertex = value

	@property
	def keep_features(self):
		"""Gets or sets whether to keep existing features on the entities selected for the chamfer."""
		return self._instance.KeepFeatures

	@keep_features.setter
	def keep_features(self, value):
		"""Gets or sets whether to keep existing features on the entities selected for the chamfer."""
		self._instance.KeepFeatures = value

	@property
	def loop_count(self):
		"""Gets the number of loops to which a chamfer is applied."""
		return self._instance.LoopCount

	@loop_count.setter
	def loop_count(self, value):
		"""Gets the number of loops to which a chamfer is applied."""
		self._instance.LoopCount = value

	@property
	def loops(self):
		"""Gets and sets the loops to which a chamfer is applied."""
		return self._instance.Loops

	@loops.setter
	def loops(self, value):
		"""Gets and sets the loops to which a chamfer is applied."""
		self._instance.Loops = value

	@property
	def propagate_feature_to_parts(self):
		"""Gets or sets whether to extend the chamfer feature to all affected parts in the assembly."""
		return self._instance.PropagateFeatureToParts

	@propagate_feature_to_parts.setter
	def propagate_feature_to_parts(self, value):
		"""Gets or sets whether to extend the chamfer feature to all affected parts in the assembly."""
		self._instance.PropagateFeatureToParts = value

	@property
	def tangent_propagation(self):
		"""Gets or sets whether to extend the chamfer to all faces that are tangent to the selected faces or edges."""
		return self._instance.TangentPropagation

	@tangent_propagation.setter
	def tangent_propagation(self, value):
		"""Gets or sets whether to extend the chamfer to all faces that are tangent to the selected faces or edges."""
		self._instance.TangentPropagation = value

	@property
	def type(self):
		"""Gets or sets the type of chamfer feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of chamfer feature."""
		self._instance.Type = value

	@property
	def vertex(self):
		"""Gets or sets the vertex to which a chamfer is applied."""
		return self._instance.Vertex

	@vertex.setter
	def vertex(self, value):
		"""Gets or sets the vertex to which a chamfer is applied."""
		self._instance.Vertex = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this chamfer feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this chamfer feature."""
		self._instance.AccessSelections = value

	@property
	def get_edge_chamfer_distance(self):
		"""Gets the edge chamfer distance on either side of the edge."""
		return self._instance.GetEdgeChamferDistance

	@get_edge_chamfer_distance.setter
	def get_edge_chamfer_distance(self, value):
		"""Gets the edge chamfer distance on either side of the edge."""
		self._instance.GetEdgeChamferDistance = value

	@property
	def get_edge_count(self):
		"""Gets the number of edges that are chamfered."""
		return self._instance.GetEdgeCount

	@get_edge_count.setter
	def get_edge_count(self, value):
		"""Gets the number of edges that are chamfered."""
		self._instance.GetEdgeCount = value

	@property
	def get_face_count(self):
		"""Gets the number of faces that are chamfered."""
		return self._instance.GetFaceCount

	@get_face_count.setter
	def get_face_count(self, value):
		"""Gets the number of faces that are chamfered."""
		self._instance.GetFaceCount = value

	@property
	def get_is_flipped(self):
		"""Gets whether the chamfer feature is flipped."""
		return self._instance.GetIsFlipped

	@get_is_flipped.setter
	def get_is_flipped(self, value):
		"""Gets whether the chamfer feature is flipped."""
		self._instance.GetIsFlipped = value

	@property
	def get_vertex_chamfer_distance(self):
		"""Gets the vertex chamfer distance."""
		return self._instance.GetVertexChamferDistance

	@get_vertex_chamfer_distance.setter
	def get_vertex_chamfer_distance(self, value):
		"""Gets the vertex chamfer distance."""
		self._instance.GetVertexChamferDistance = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this chamfer feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this chamfer feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_edges(self):
		"""Gets the edges to which a chamfer is applied."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Gets the edges to which a chamfer is applied."""
		self._instance.IGetEdges = value

	@property
	def i_get_faces(self):
		"""Gets the faces to which a chamfer is applied."""
		return self._instance.IGetFaces

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets the faces to which a chamfer is applied."""
		self._instance.IGetFaces = value

	@property
	def i_get_loops(self):
		"""Gets the loops to which a chamfer is applied."""
		return self._instance.IGetLoops

	@i_get_loops.setter
	def i_get_loops(self, value):
		"""Gets the loops to which a chamfer is applied."""
		self._instance.IGetLoops = value

	@property
	def i_set_edges(self):
		"""Sets the edges to which a chamfer is applied."""
		return self._instance.ISetEdges

	@i_set_edges.setter
	def i_set_edges(self, value):
		"""Sets the edges to which a chamfer is applied."""
		self._instance.ISetEdges = value

	@property
	def i_set_faces(self):
		"""Gets the faces to which a chamfer is applied."""
		return self._instance.ISetFaces

	@i_set_faces.setter
	def i_set_faces(self, value):
		"""Gets the faces to which a chamfer is applied."""
		self._instance.ISetFaces = value

	@property
	def i_set_loops(self):
		"""Sets the loops to which a chamfer is applied."""
		return self._instance.ISetLoops

	@i_set_loops.setter
	def i_set_loops(self, value):
		"""Sets the loops to which a chamfer is applied."""
		self._instance.ISetLoops = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created this chamfer feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created this chamfer feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_edge_chamfer_distance(self):
		"""Sets the edge chamfer distance on either side of the edge."""
		return self._instance.SetEdgeChamferDistance

	@set_edge_chamfer_distance.setter
	def set_edge_chamfer_distance(self, value):
		"""Sets the edge chamfer distance on either side of the edge."""
		self._instance.SetEdgeChamferDistance = value

	@property
	def set_is_flipped(self):
		"""Gets whether the chamfer feature is flipped."""
		return self._instance.SetIsFlipped

	@set_is_flipped.setter
	def set_is_flipped(self, value):
		"""Gets whether the chamfer feature is flipped."""
		self._instance.SetIsFlipped = value

	@property
	def set_vertex_chamfer_distance(self):
		"""Sets the vertex chamfer distance."""
		return self._instance.SetVertexChamferDistance

	@set_vertex_chamfer_distance.setter
	def set_vertex_chamfer_distance(self, value):
		"""Sets the vertex chamfer distance."""
		self._instance.SetVertexChamferDistance = value

