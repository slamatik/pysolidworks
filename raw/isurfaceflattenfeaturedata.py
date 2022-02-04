# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData_members.html
class ISurfaceFlattenFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def accuracy_factor(self):
		"""Gets or sets the accuracy of the flattened triangle mesh."""
		return self._instance.AccuracyFactor

	@accuracy_factor.setter
	def accuracy_factor(self, value):
		"""Gets or sets the accuracy of the flattened triangle mesh."""
		self._instance.AccuracyFactor = value

	@property
	def faces(self):
		"""Gets or sets the faces or surfaces to flatten."""
		return self._instance.Faces

	@faces.setter
	def faces(self, value):
		"""Gets or sets the faces or surfaces to flatten."""
		self._instance.Faces = value

	@property
	def fix_point_vertex(self):
		"""Gets or sets the anchor point for flattening the selected faces or surfaces."""
		return self._instance.FixPointVertex

	@fix_point_vertex.setter
	def fix_point_vertex(self, value):
		"""Gets or sets the anchor point for flattening the selected faces or surfaces."""
		self._instance.FixPointVertex = value

	@property
	def guide_edges(self):
		"""Gets or sets the edges to guide the shape and length of the flattened surface."""
		return self._instance.GuideEdges

	@guide_edges.setter
	def guide_edges(self, value):
		"""Gets or sets the edges to guide the shape and length of the flattened surface."""
		self._instance.GuideEdges = value

	@property
	def keep_internal_control_curves(self):
		"""Gets or sets whether to keep internal control curves for this surface-flatten feature."""
		return self._instance.KeepInternalControlCurves

	@keep_internal_control_curves.setter
	def keep_internal_control_curves(self, value):
		"""Gets or sets whether to keep internal control curves for this surface-flatten feature."""
		self._instance.KeepInternalControlCurves = value

	@property
	def map_edges(self):
		"""Gets or sets the map edges for this surface-flatten feature."""
		return self._instance.MapEdges

	@map_edges.setter
	def map_edges(self, value):
		"""Gets or sets the map edges for this surface-flatten feature."""
		self._instance.MapEdges = value

	@property
	def should_make_tears(self):
		"""Gets or sets whether to enable relief cuts for this surface-flatten feature."""
		return self._instance.ShouldMakeTears

	@should_make_tears.setter
	def should_make_tears(self, value):
		"""Gets or sets whether to enable relief cuts for this surface-flatten feature."""
		self._instance.ShouldMakeTears = value

	@property
	def tear_edges(self):
		"""Gets or sets the tear edges for the relief cuts for this surface-flatten feature."""
		return self._instance.TearEdges

	@tear_edges.setter
	def tear_edges(self, value):
		"""Gets or sets the tear edges for the relief cuts for this surface-flatten feature."""
		self._instance.TearEdges = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this surface-flatten feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this surface-flatten feature."""
		self._instance.AccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this surface-flatten feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this surface-flatten feature."""
		self._instance.ReleaseSelectionAccess = value

