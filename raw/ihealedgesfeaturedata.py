# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHealEdgesFeatureData_members.html
class IHealEdgesFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angular_tolerance(self):
		"""Gets or sets the maximum angle between the edges to merge."""
		return self._instance.AngularTolerance

	@angular_tolerance.setter
	def angular_tolerance(self, value):
		"""Gets or sets the maximum angle between the edges to merge."""
		self._instance.AngularTolerance = value

	@property
	def edge_length_tolerance(self):
		"""Gets or sets the maximum length of the edges to merge."""
		return self._instance.EdgeLengthTolerance

	@edge_length_tolerance.setter
	def edge_length_tolerance(self, value):
		"""Gets or sets the maximum length of the edges to merge."""
		self._instance.EdgeLengthTolerance = value

	@property
	def faces(self):
		"""Gets the faces whose edges were healed or sets the faces whose edges you want healed."""
		return self._instance.Faces

	@faces.setter
	def faces(self, value):
		"""Gets the faces whose edges were healed or sets the faces whose edges you want healed."""
		self._instance.Faces = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe this heal edges feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe this heal edges feature."""
		self._instance.AccessSelections = value

	@property
	def get_edge_information(self):
		"""Gets the number of edges before healing and the number of edges after healing."""
		return self._instance.GetEdgeInformation

	@get_edge_information.setter
	def get_edge_information(self, value):
		"""Gets the number of edges before healing and the number of edges after healing."""
		self._instance.GetEdgeInformation = value

	@property
	def get_faces_count(self):
		"""Gets the number of faces for this heal edges feature."""
		return self._instance.GetFacesCount

	@get_faces_count.setter
	def get_faces_count(self, value):
		"""Gets the number of faces for this heal edges feature."""
		self._instance.GetFacesCount = value

	@property
	def heal_edges(self):
		"""Merges the edges using the specified faces and tolerances."""
		return self._instance.HealEdges

	@heal_edges.setter
	def heal_edges(self, value):
		"""Merges the edges using the specified faces and tolerances."""
		self._instance.HealEdges = value

	@property
	def i_get_faces(self):
		"""Gets the faces whose edges to heal."""
		return self._instance.IGetFaces

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets the faces whose edges to heal."""
		self._instance.IGetFaces = value

	@property
	def i_set_faces(self):
		"""Gets the faces whose edges were healed."""
		return self._instance.ISetFaces

	@i_set_faces.setter
	def i_set_faces(self, value):
		"""Gets the faces whose edges were healed."""
		self._instance.ISetFaces = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that describe this heal edges feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that describe this heal edges feature."""
		self._instance.ReleaseSelectionAccess = value

