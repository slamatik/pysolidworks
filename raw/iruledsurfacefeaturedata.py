# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.html
class IRuledSurfaceFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the taper angle of this ruled-surface feature."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the taper angle of this ruled-surface feature."""
		self._instance.Angle = value

	@property
	def connect(self):
		"""Gets or sets whether or not to connect the surfaces of this ruled-surface feature."""
		return self._instance.Connect

	@connect.setter
	def connect(self, value):
		"""Gets or sets whether or not to connect the surfaces of this ruled-surface feature."""
		self._instance.Connect = value

	@property
	def direction_vector(self):
		"""Gets or sets the reference vector for this ruled-surface feature."""
		return self._instance.DirectionVector

	@direction_vector.setter
	def direction_vector(self, value):
		"""Gets or sets the reference vector for this ruled-surface feature."""
		self._instance.DirectionVector = value

	@property
	def distance(self):
		"""Gets or sets the distance, in meters, to extend the ruled-surface feature."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the distance, in meters, to extend the ruled-surface feature."""
		self._instance.Distance = value

	@property
	def trim_and_knit(self):
		"""Gets or sets whether to trim and knit the surfaces of this ruled-surface feature."""
		return self._instance.TrimAndKnit

	@trim_and_knit.setter
	def trim_and_knit(self, value):
		"""Gets or sets whether to trim and knit the surfaces of this ruled-surface feature."""
		self._instance.TrimAndKnit = value

	@property
	def type(self):
		"""Gets or sets the type of ruled-surface feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of ruled-surface feature."""
		self._instance.Type = value

	@property
	def use_vector(self):
		"""Gets or sets whether or not use a reference vector for this ruled-surface feature."""
		return self._instance.UseVector

	@use_vector.setter
	def use_vector(self, value):
		"""Gets or sets whether or not use a reference vector for this ruled-surface feature."""
		self._instance.UseVector = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this ruled-surface feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this ruled-surface feature."""
		self._instance.AccessSelections = value

	@property
	def get_direction_reference(self):
		"""Gets the direction of this ruled-surface feature."""
		return self._instance.GetDirectionReference

	@get_direction_reference.setter
	def get_direction_reference(self, value):
		"""Gets the direction of this ruled-surface feature."""
		self._instance.GetDirectionReference = value

	@property
	def get_edges(self):
		"""Gets the edges to used as the base for this ruled-surface feature."""
		return self._instance.GetEdges

	@get_edges.setter
	def get_edges(self, value):
		"""Gets the edges to used as the base for this ruled-surface feature."""
		self._instance.GetEdges = value

	@property
	def get_edges_count(self):
		"""Gets the number of edges to use as a base for this ruled-surface feature."""
		return self._instance.GetEdgesCount

	@get_edges_count.setter
	def get_edges_count(self, value):
		"""Gets the number of edges to use as a base for this ruled-surface feature."""
		self._instance.GetEdgesCount = value

	@property
	def i_get_edges(self):
		"""Gets the edges to used as the base for this ruled-surface feature."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Gets the edges to used as the base for this ruled-surface feature."""
		self._instance.IGetEdges = value

	@property
	def i_set_edges(self):
		"""Sets the edge to use as the base for this ruled-surface feature."""
		return self._instance.ISetEdges

	@i_set_edges.setter
	def i_set_edges(self, value):
		"""Sets the edge to use as the base for this ruled-surface feature."""
		self._instance.ISetEdges = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this ruled-surface feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this ruled-surface feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_direction_reference(self):
		"""Sets the direction of the extrusion for this ruled-surface feature."""
		return self._instance.SetDirectionReference

	@set_direction_reference.setter
	def set_direction_reference(self, value):
		"""Sets the direction of the extrusion for this ruled-surface feature."""
		self._instance.SetDirectionReference = value

	@property
	def set_edges(self):
		"""Sets the edge to use as the base for this ruled-surface feature."""
		return self._instance.SetEdges

	@set_edges.setter
	def set_edges(self, value):
		"""Sets the edge to use as the base for this ruled-surface feature."""
		self._instance.SetEdges = value

