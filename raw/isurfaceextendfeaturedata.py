# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.html
class ISurfaceExtendFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def distance(self):
		"""Gets or sets the extended distance for this surface-extend feature."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the extended distance for this surface-extend feature."""
		self._instance.Distance = value

	@property
	def end_condition(self):
		"""Gets or sets the end condition for this surface-extend feature."""
		return self._instance.EndCondition

	@end_condition.setter
	def end_condition(self, value):
		"""Gets or sets the end condition for this surface-extend feature."""
		self._instance.EndCondition = value

	@property
	def face(self):
		"""Gets or sets the end-condition face for this surface-extend feature."""
		return self._instance.Face

	@face.setter
	def face(self, value):
		"""Gets or sets the end-condition face for this surface-extend feature."""
		self._instance.Face = value

	@property
	def i_face(self):
		"""Gets or sets the end-condition face for this surface-extend feature."""
		return self._instance.IFace

	@i_face.setter
	def i_face(self, value):
		"""Gets or sets the end-condition face for this surface-extend feature."""
		self._instance.IFace = value

	@property
	def items(self):
		"""Gets or sets the extended faces and edges for this surface-extend feature."""
		return self._instance.Items

	@items.setter
	def items(self, value):
		"""Gets or sets the extended faces and edges for this surface-extend feature."""
		self._instance.Items = value

	@property
	def i_vertex(self):
		"""Gets and sets the vertex for the end condition of this surface-extend feature."""
		return self._instance.IVertex

	@i_vertex.setter
	def i_vertex(self, value):
		"""Gets and sets the vertex for the end condition of this surface-extend feature."""
		self._instance.IVertex = value

	@property
	def propagating_edges(self):
		"""Gets or sets the propagating edges for this surface-extend feature."""
		return self._instance.PropagatingEdges

	@propagating_edges.setter
	def propagating_edges(self, value):
		"""Gets or sets the propagating edges for this surface-extend feature."""
		self._instance.PropagatingEdges = value

	@property
	def type(self):
		"""Gets or sets the extension type for this surface-extend feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the extension type for this surface-extend feature."""
		self._instance.Type = value

	@property
	def vertex(self):
		"""Gets and sets the vertex for the end condition of this surface-extend feature."""
		return self._instance.Vertex

	@vertex.setter
	def vertex(self, value):
		"""Gets and sets the vertex for the end condition of this surface-extend feature."""
		self._instance.Vertex = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this surface-extend feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this surface-extend feature."""
		self._instance.AccessSelections = value

	@property
	def get_items_count(self):
		"""Gets the number of extended faces and edges for this surface-extend feature."""
		return self._instance.GetItemsCount

	@get_items_count.setter
	def get_items_count(self, value):
		"""Gets the number of extended faces and edges for this surface-extend feature."""
		self._instance.GetItemsCount = value

	@property
	def get_propagating_edges_count(self):
		"""Gets the propagating edges for this surface-extend feature."""
		return self._instance.GetPropagatingEdgesCount

	@get_propagating_edges_count.setter
	def get_propagating_edges_count(self, value):
		"""Gets the propagating edges for this surface-extend feature."""
		self._instance.GetPropagatingEdgesCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this surface-extend feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this surface-extend feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_items(self):
		"""Gets the extended faces and edges for this surface-extend feature."""
		return self._instance.IGetItems

	@i_get_items.setter
	def i_get_items(self, value):
		"""Gets the extended faces and edges for this surface-extend feature."""
		self._instance.IGetItems = value

	@property
	def i_get_propagating_edges(self):
		"""Gets the propagating edges for this surface-extend feature."""
		return self._instance.IGetPropagatingEdges

	@i_get_propagating_edges.setter
	def i_get_propagating_edges(self, value):
		"""Gets the propagating edges for this surface-extend feature."""
		self._instance.IGetPropagatingEdges = value

	@property
	def i_set_items(self):
		"""Sets the extended faces and edges for this surface-extend feature."""
		return self._instance.ISetItems

	@i_set_items.setter
	def i_set_items(self, value):
		"""Sets the extended faces and edges for this surface-extend feature."""
		self._instance.ISetItems = value

	@property
	def i_set_propagating_edges(self):
		"""Sets the propagating edges for this surface-extend feature."""
		return self._instance.ISetPropagatingEdges

	@i_set_propagating_edges.setter
	def i_set_propagating_edges(self, value):
		"""Sets the propagating edges for this surface-extend feature."""
		self._instance.ISetPropagatingEdges = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this surface-extend feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this surface-extend feature."""
		self._instance.ReleaseSelectionAccess = value

