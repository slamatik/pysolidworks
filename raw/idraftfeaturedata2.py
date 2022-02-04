# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html
class IDraftFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def allow_reduced_angle(self):
		"""Gets or sets the Allow reduced angle option for this draft feature."""
		return self._instance.AllowReducedAngle

	@allow_reduced_angle.setter
	def allow_reduced_angle(self, value):
		"""Gets or sets the Allow reduced angle option for this draft feature."""
		self._instance.AllowReducedAngle = value

	@property
	def angle(self):
		"""Gets or sets the angle for this draft feature."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle for this draft feature."""
		self._instance.Angle = value

	@property
	def direction_pull(self):
		"""Gets or sets the direction in which to pull this draft feature."""
		return self._instance.DirectionPull

	@direction_pull.setter
	def direction_pull(self, value):
		"""Gets or sets the direction in which to pull this draft feature."""
		self._instance.DirectionPull = value

	@property
	def face_propagation(self):
		"""Gets or sets the face propagation for this draft feature."""
		return self._instance.FacePropagation

	@face_propagation.setter
	def face_propagation(self, value):
		"""Gets or sets the face propagation for this draft feature."""
		self._instance.FacePropagation = value

	@property
	def faces_to_draft(self):
		"""Gets or sets the faces that define this draft feature."""
		return self._instance.FacesToDraft

	@faces_to_draft.setter
	def faces_to_draft(self, value):
		"""Gets or sets the faces that define this draft feature."""
		self._instance.FacesToDraft = value

	@property
	def neutral_plane(self):
		"""Gets or sets the neutral plane for this draft feature."""
		return self._instance.NeutralPlane

	@neutral_plane.setter
	def neutral_plane(self, value):
		"""Gets or sets the neutral plane for this draft feature."""
		self._instance.NeutralPlane = value

	@property
	def parting_lines(self):
		"""Gets or sets the parting lines for this draft feature."""
		return self._instance.PartingLines

	@parting_lines.setter
	def parting_lines(self, value):
		"""Gets or sets the parting lines for this draft feature."""
		self._instance.PartingLines = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether the direction of the draft feature is reversed."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether the direction of the draft feature is reversed."""
		self._instance.ReverseDirection = value

	@property
	def step_type(self):
		"""Gets or sets the step type for this draft feature."""
		return self._instance.StepType

	@step_type.setter
	def step_type(self, value):
		"""Gets or sets the step type for this draft feature."""
		self._instance.StepType = value

	@property
	def type(self):
		"""Gets the type of draft feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the type of draft feature."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this draft feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this draft feature."""
		self._instance.AccessSelections = value

	@property
	def get_drafted_entities(self):
		"""Gets the drafted entities (faces or edges) for this draft feature."""
		return self._instance.GetDraftedEntities

	@get_drafted_entities.setter
	def get_drafted_entities(self, value):
		"""Gets the drafted entities (faces or edges) for this draft feature."""
		self._instance.GetDraftedEntities = value

	@property
	def get_drafted_entity_count(self):
		"""Gets the number of drafted entities for this draft feature."""
		return self._instance.GetDraftedEntityCount

	@get_drafted_entity_count.setter
	def get_drafted_entity_count(self, value):
		"""Gets the number of drafted entities for this draft feature."""
		self._instance.GetDraftedEntityCount = value

	@property
	def get_faces_to_draft_count(self):
		"""Gets the number of faces that define the draft feature."""
		return self._instance.GetFacesToDraftCount

	@get_faces_to_draft_count.setter
	def get_faces_to_draft_count(self, value):
		"""Gets the number of faces that define the draft feature."""
		self._instance.GetFacesToDraftCount = value

	@property
	def get_other_faces_flag_at_index(self):
		"""Gets the value of the Other Face option at the specified index."""
		return self._instance.GetOtherFacesFlagAtIndex

	@get_other_faces_flag_at_index.setter
	def get_other_faces_flag_at_index(self, value):
		"""Gets the value of the Other Face option at the specified index."""
		self._instance.GetOtherFacesFlagAtIndex = value

	@property
	def get_parting_lines_count(self):
		"""Gets the number of parting lines for this draft feature."""
		return self._instance.GetPartingLinesCount

	@get_parting_lines_count.setter
	def get_parting_lines_count(self, value):
		"""Gets the number of parting lines for this draft feature."""
		self._instance.GetPartingLinesCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this draft feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this draft feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_drafted_entities(self):
		"""Gets the drafted entities (faces or edges) for this draft feature."""
		return self._instance.IGetDraftedEntities

	@i_get_drafted_entities.setter
	def i_get_drafted_entities(self, value):
		"""Gets the drafted entities (faces or edges) for this draft feature."""
		self._instance.IGetDraftedEntities = value

	@property
	def i_get_faces_to_draft(self):
		"""Gets the faces that define this draft feature."""
		return self._instance.IGetFacesToDraft

	@i_get_faces_to_draft.setter
	def i_get_faces_to_draft(self, value):
		"""Gets the faces that define this draft feature."""
		self._instance.IGetFacesToDraft = value

	@property
	def i_get_parting_lines(self):
		"""Gets the parting lines that define this draft feature."""
		return self._instance.IGetPartingLines

	@i_get_parting_lines.setter
	def i_get_parting_lines(self, value):
		"""Gets the parting lines that define this draft feature."""
		self._instance.IGetPartingLines = value

	@property
	def i_set_faces_to_draft(self):
		"""Sets the faces to which to apply the draft feature."""
		return self._instance.ISetFacesToDraft

	@i_set_faces_to_draft.setter
	def i_set_faces_to_draft(self, value):
		"""Sets the faces to which to apply the draft feature."""
		self._instance.ISetFacesToDraft = value

	@property
	def i_set_parting_lines(self):
		"""Sets the parting lines for this draft feature."""
		return self._instance.ISetPartingLines

	@i_set_parting_lines.setter
	def i_set_parting_lines(self, value):
		"""Sets the parting lines for this draft feature."""
		self._instance.ISetPartingLines = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this draft feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this draft feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_other_faces_flag_at_index(self):
		"""Sets the Other Face option."""
		return self._instance.SetOtherFacesFlagAtIndex

	@set_other_faces_flag_at_index.setter
	def set_other_faces_flag_at_index(self, value):
		"""Sets the Other Face option."""
		self._instance.SetOtherFacesFlagAtIndex = value

