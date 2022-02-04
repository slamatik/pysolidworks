# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html
class ICoreFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bounding_sketch(self):
		"""Gets or sets the bounding sketch for this core feature."""
		return self._instance.BoundingSketch

	@bounding_sketch.setter
	def bounding_sketch(self, value):
		"""Gets or sets the bounding sketch for this core feature."""
		self._instance.BoundingSketch = value

	@property
	def cap_ends(self):
		"""Gets or sets whether the endd are capped on this core feature."""
		return self._instance.CapEnds

	@cap_ends.setter
	def cap_ends(self, value):
		"""Gets or sets whether the endd are capped on this core feature."""
		self._instance.CapEnds = value

	@property
	def depth(self):
		"""Gets or sets the depth in the specified direction of this core feature."""
		return self._instance.Depth

	@depth.setter
	def depth(self, value):
		"""Gets or sets the depth in the specified direction of this core feature."""
		self._instance.Depth = value

	@property
	def draft_angle(self):
		"""Gets or sets the angle of the draft for this core feature."""
		return self._instance.DraftAngle

	@draft_angle.setter
	def draft_angle(self, value):
		"""Gets or sets the angle of the draft for this core feature."""
		self._instance.DraftAngle = value

	@property
	def draft_outward(self):
		"""Gets or sets whether draft is applied outward on this core feature."""
		return self._instance.DraftOutward

	@draft_outward.setter
	def draft_outward(self, value):
		"""Gets or sets whether draft is applied outward on this core feature."""
		self._instance.DraftOutward = value

	@property
	def end_condition(self):
		"""Gets or sets the end condition in the specified direction for this core feature."""
		return self._instance.EndCondition

	@end_condition.setter
	def end_condition(self, value):
		"""Gets or sets the end condition in the specified direction for this core feature."""
		self._instance.EndCondition = value

	@property
	def reverse_direction(self):
		"""Gets or sets the direction of the extraction for this core feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets the direction of the extraction for this core feature."""
		self._instance.ReverseDirection = value

	@property
	def target_body(self):
		"""Gets or sets the target body for this core feature."""
		return self._instance.TargetBody

	@target_body.setter
	def target_body(self, value):
		"""Gets or sets the target body for this core feature."""
		self._instance.TargetBody = value

	@property
	def use_draft(self):
		"""Gets or sets whether draft is applied to this core feature."""
		return self._instance.UseDraft

	@use_draft.setter
	def use_draft(self, value):
		"""Gets or sets whether draft is applied to this core feature."""
		self._instance.UseDraft = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe this core feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe this core feature."""
		self._instance.AccessSelections = value

	@property
	def get_extraction_direction(self):
		"""Gets the entities that define the extraction direction of this core feature."""
		return self._instance.GetExtractionDirection

	@get_extraction_direction.setter
	def get_extraction_direction(self, value):
		"""Gets the entities that define the extraction direction of this core feature."""
		self._instance.GetExtractionDirection = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that describe this core feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that describe this core feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_extraction_direction(self):
		"""Sets the entities that define the extraction direction of this core feature."""
		return self._instance.SetExtractionDirection

	@set_extraction_direction.setter
	def set_extraction_direction(self, value):
		"""Sets the entities that define the extraction direction of this core feature."""
		self._instance.SetExtractionDirection = value

