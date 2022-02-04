# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRibFeatureData2_members.html
class IRibFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def body(self):
		"""Gets or sets the body where the rib is created."""
		return self._instance.Body

	@body.setter
	def body(self, value):
		"""Gets or sets the body where the rib is created."""
		self._instance.Body = value

	@property
	def draft_angle(self):
		"""Gets or sets the draft angle for the rib."""
		return self._instance.DraftAngle

	@draft_angle.setter
	def draft_angle(self, value):
		"""Gets or sets the draft angle for the rib."""
		self._instance.DraftAngle = value

	@property
	def draft_from_wall(self):
		"""Gets or sets whether to draft the rib from the wall interface or the sketch plane."""
		return self._instance.DraftFromWall

	@draft_from_wall.setter
	def draft_from_wall(self, value):
		"""Gets or sets whether to draft the rib from the wall interface or the sketch plane."""
		self._instance.DraftFromWall = value

	@property
	def draft_outward(self):
		"""Gets or sets whether the rib has an outward draft."""
		return self._instance.DraftOutward

	@draft_outward.setter
	def draft_outward(self, value):
		"""Gets or sets whether the rib has an outward draft."""
		self._instance.DraftOutward = value

	@property
	def enable_draft(self):
		"""Gets or sets whether the rib has an associated draft."""
		return self._instance.EnableDraft

	@enable_draft.setter
	def enable_draft(self, value):
		"""Gets or sets whether the rib has an associated draft."""
		self._instance.EnableDraft = value

	@property
	def extrusion_direction(self):
		"""Gets or sets the direction in which to extrude the rib."""
		return self._instance.ExtrusionDirection

	@extrusion_direction.setter
	def extrusion_direction(self, value):
		"""Gets or sets the direction in which to extrude the rib."""
		self._instance.ExtrusionDirection = value

	@property
	def flip_side(self):
		"""Gets or sets whether material is added to the reverse side of the rib."""
		return self._instance.FlipSide

	@flip_side.setter
	def flip_side(self, value):
		"""Gets or sets whether material is added to the reverse side of the rib."""
		self._instance.FlipSide = value

	@property
	def is_two_sided(self):
		"""Gets or sets whether the rib is created on two sides of the midplane or in a single direction (see IRibFeatureData2::ReverseThicknessDir)."""
		return self._instance.IsTwoSided

	@is_two_sided.setter
	def is_two_sided(self, value):
		"""Gets or sets whether the rib is created on two sides of the midplane or in a single direction (see IRibFeatureData2::ReverseThicknessDir)."""
		self._instance.IsTwoSided = value

	@property
	def ref_sketch_index(self):
		"""Gets or sets which sketch segment defines the draft direction of the rib feature."""
		return self._instance.RefSketchIndex

	@ref_sketch_index.setter
	def ref_sketch_index(self, value):
		"""Gets or sets which sketch segment defines the draft direction of the rib feature."""
		self._instance.RefSketchIndex = value

	@property
	def reverse_thickness_dir(self):
		"""Gets or sets whether the extrusion is on the reverse side of this single-sided rib."""
		return self._instance.ReverseThicknessDir

	@reverse_thickness_dir.setter
	def reverse_thickness_dir(self, value):
		"""Gets or sets whether the extrusion is on the reverse side of this single-sided rib."""
		self._instance.ReverseThicknessDir = value

	@property
	def thickness(self):
		"""Gets or set the overall thickness of the rib."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or set the overall thickness of the rib."""
		self._instance.Thickness = value

	@property
	def type(self):
		"""Gets or sets the type of rib."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of rib."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Gains access to the the selections for this rib feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the the selections for this rib feature."""
		self._instance.AccessSelections = value

	@property
	def i_access_selections(self):
		"""Gains access to the the selections for this rib feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the the selections for this rib feature."""
		self._instance.IAccessSelections = value

	@property
	def next_reference(self):
		"""Cycles through the possible sketch entities that can be used to define the draft, if it is used, for ribs with multiple contours."""
		return self._instance.NextReference

	@next_reference.setter
	def next_reference(self, value):
		"""Cycles through the possible sketch entities that can be used to define the draft, if it is used, for ribs with multiple contours."""
		self._instance.NextReference = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this rib feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this rib feature."""
		self._instance.ReleaseSelectionAccess = value

