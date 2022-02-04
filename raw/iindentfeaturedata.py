# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html
class IIndentFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def clearance(self):
		"""Gets or sets the clearance between the target and tool bodies in this indent feature."""
		return self._instance.Clearance

	@clearance.setter
	def clearance(self, value):
		"""Gets or sets the clearance between the target and tool bodies in this indent feature."""
		self._instance.Clearance = value

	@property
	def clearance_direction(self):
		"""Gets or sets the direction of the clearance for this indent feature."""
		return self._instance.ClearanceDirection

	@clearance_direction.setter
	def clearance_direction(self, value):
		"""Gets or sets the direction of the clearance for this indent feature."""
		self._instance.ClearanceDirection = value

	@property
	def cut_direction(self):
		"""Gets or sets whether to flip the side of the cut for this indent feature."""
		return self._instance.CutDirection

	@cut_direction.setter
	def cut_direction(self, value):
		"""Gets or sets whether to flip the side of the cut for this indent feature."""
		self._instance.CutDirection = value

	@property
	def is_cut(self):
		"""Gets or sets whether to remove the intersection area of the target body."""
		return self._instance.IsCut

	@is_cut.setter
	def is_cut(self, value):
		"""Gets or sets whether to remove the intersection area of the target body."""
		self._instance.IsCut = value

	@property
	def selection_state(self):
		"""Gets or sets the side of the model to keep or remove."""
		return self._instance.SelectionState

	@selection_state.setter
	def selection_state(self, value):
		"""Gets or sets the side of the model to keep or remove."""
		self._instance.SelectionState = value

	@property
	def target_body(self):
		"""Gets or sets the solid or surface body to indent."""
		return self._instance.TargetBody

	@target_body.setter
	def target_body(self, value):
		"""Gets or sets the solid or surface body to indent."""
		self._instance.TargetBody = value

	@property
	def thickness(self):
		"""Gets or sets the thickness of the indent feature."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or sets the thickness of the indent feature."""
		self._instance.Thickness = value

	@property
	def tool_body_region(self):
		"""Gets or sets the tool body region for the indent feature."""
		return self._instance.ToolBodyRegion

	@tool_body_region.setter
	def tool_body_region(self, value):
		"""Gets or sets the tool body region for the indent feature."""
		self._instance.ToolBodyRegion = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this indent feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this indent feature."""
		self._instance.AccessSelections = value

	@property
	def get_bodies_count(self):
		"""Gets the number of solid or surface bodies for the tool body region."""
		return self._instance.GetBodiesCount

	@get_bodies_count.setter
	def get_bodies_count(self, value):
		"""Gets the number of solid or surface bodies for the tool body region."""
		self._instance.GetBodiesCount = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this indent feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this indent feature."""
		self._instance.ReleaseSelectionAccess = value

