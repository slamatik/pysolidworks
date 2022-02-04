# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRipFeatureData_members.html
class IRipFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def edges(self):
		"""Gets or sets the edges for this rip feature."""
		return self._instance.Edges

	@edges.setter
	def edges(self, value):
		"""Gets or sets the edges for this rip feature."""
		self._instance.Edges = value

	@property
	def gap(self):
		"""Gets or sets the gap for this rip feature."""
		return self._instance.Gap

	@gap.setter
	def gap(self, value):
		"""Gets or sets the gap for this rip feature."""
		self._instance.Gap = value

	@property
	def access_selections(self):
		"""Gains access to the selections for this rip feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections for this rip feature."""
		self._instance.AccessSelections = value

	@property
	def get_direction(self):
		"""Gets the rip direction for the specified edge."""
		return self._instance.GetDirection

	@get_direction.setter
	def get_direction(self, value):
		"""Gets the rip direction for the specified edge."""
		self._instance.GetDirection = value

	@property
	def get_edges_count(self):
		"""Gets the number of edges for this rip feature."""
		return self._instance.GetEdgesCount

	@get_edges_count.setter
	def get_edges_count(self, value):
		"""Gets the number of edges for this rip feature."""
		self._instance.GetEdgesCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections for this rip feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections for this rip feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_edges(self):
		"""Gets the edges for this rip feature."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Gets the edges for this rip feature."""
		self._instance.IGetEdges = value

	@property
	def i_set_edges(self):
		"""Sets the edges for this rip feature."""
		return self._instance.ISetEdges

	@i_set_edges.setter
	def i_set_edges(self, value):
		"""Sets the edges for this rip feature."""
		self._instance.ISetEdges = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this rip feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this rip feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_direction(self):
		"""Sets the direction for this rip feature."""
		return self._instance.SetDirection

	@set_direction.setter
	def set_direction(self, value):
		"""Sets the direction for this rip feature."""
		self._instance.SetDirection = value

