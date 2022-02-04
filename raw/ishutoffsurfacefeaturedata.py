# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShutOffSurfaceFeatureData_members.html
class IShutOffSurfaceFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def edges(self):
		"""Gets or sets the edges that form closed loops for the patches."""
		return self._instance.Edges

	@edges.setter
	def edges(self, value):
		"""Gets or sets the edges that form closed loops for the patches."""
		self._instance.Edges = value

	@property
	def knit(self):
		"""Gets or sets whether to knit the patches in this shut-off surface feature."""
		return self._instance.Knit

	@knit.setter
	def knit(self, value):
		"""Gets or sets whether to knit the patches in this shut-off surface feature."""
		self._instance.Knit = value

	@property
	def loop_edges(self):
		"""Gets the edges in the specified loop in this shut-off surface feature."""
		return self._instance.LoopEdges

	@loop_edges.setter
	def loop_edges(self, value):
		"""Gets the edges in the specified loop in this shut-off surface feature."""
		self._instance.LoopEdges = value

	@property
	def loop_patch_type(self):
		"""Gets and sets the type of patch for the specified loop for this shut-off surface feature."""
		return self._instance.LoopPatchType

	@loop_patch_type.setter
	def loop_patch_type(self, value):
		"""Gets and sets the type of patch for the specified loop for this shut-off surface feature."""
		self._instance.LoopPatchType = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this shut-off surface feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this shut-off surface feature."""
		self._instance.AccessSelections = value

	@property
	def flip_face_tangent_to(self):
		"""Indicates to create the patch on the opposite tangent face."""
		return self._instance.FlipFaceTangentTo

	@flip_face_tangent_to.setter
	def flip_face_tangent_to(self, value):
		"""Indicates to create the patch on the opposite tangent face."""
		self._instance.FlipFaceTangentTo = value

	@property
	def get_edge_count(self):
		"""Gets the number of edges that form a closed loop."""
		return self._instance.GetEdgeCount

	@get_edge_count.setter
	def get_edge_count(self, value):
		"""Gets the number of edges that form a closed loop."""
		self._instance.GetEdgeCount = value

	@property
	def get_face_tangent_to(self):
		"""Gets the tangent face for the specified loop where to create the patch."""
		return self._instance.GetFaceTangentTo

	@get_face_tangent_to.setter
	def get_face_tangent_to(self, value):
		"""Gets the tangent face for the specified loop where to create the patch."""
		self._instance.GetFaceTangentTo = value

	@property
	def get_loop_count(self):
		"""Gets the number of closed loops for all of the patches."""
		return self._instance.GetLoopCount

	@get_loop_count.setter
	def get_loop_count(self, value):
		"""Gets the number of closed loops for all of the patches."""
		self._instance.GetLoopCount = value

	@property
	def get_loop_edge_count(self):
		"""Gets the number of edges in the specified loop."""
		return self._instance.GetLoopEdgeCount

	@get_loop_edge_count.setter
	def get_loop_edge_count(self, value):
		"""Gets the number of edges in the specified loop."""
		self._instance.GetLoopEdgeCount = value

	@property
	def i_get_edges(self):
		"""Gets the edges that form closed loops to use for the patches."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Gets the edges that form closed loops to use for the patches."""
		self._instance.IGetEdges = value

	@property
	def i_get_loop_edges(self):
		"""Gets the edges in the specified loop."""
		return self._instance.IGetLoopEdges

	@i_get_loop_edges.setter
	def i_get_loop_edges(self, value):
		"""Gets the edges in the specified loop."""
		self._instance.IGetLoopEdges = value

	@property
	def i_set_edges(self):
		"""Sets the edges to use to form closed loops for patches."""
		return self._instance.ISetEdges

	@i_set_edges.setter
	def i_set_edges(self, value):
		"""Sets the edges to use to form closed loops for patches."""
		self._instance.ISetEdges = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this shut-off surface feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this shut-off surface feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_all_patch_types(self):
		"""Sets the type of patch for all loops for this shut-off surface feature."""
		return self._instance.SetAllPatchTypes

	@set_all_patch_types.setter
	def set_all_patch_types(self, value):
		"""Sets the type of patch for all loops for this shut-off surface feature."""
		self._instance.SetAllPatchTypes = value

	@property
	def status(self):
		"""Gets the status of the shut-off surface feature."""
		return self._instance.Status

	@status.setter
	def status(self, value):
		"""Gets the status of the shut-off surface feature."""
		self._instance.Status = value

