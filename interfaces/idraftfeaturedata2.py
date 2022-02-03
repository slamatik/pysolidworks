# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDraftFeatureData2_members.html
class IDraftFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	def allow_reduced_angle(self):
		"""Gets or sets the Allow reduced angle option for this draft feature."""
		# return self._instance.AllowReducedAngle
		raise NotImplemented

	def angle(self):
		"""Gets or sets the angle for this draft feature."""
		# return self._instance.Angle
		raise NotImplemented

	def direction_pull(self):
		"""Gets or sets the direction in which to pull this draft feature."""
		# return self._instance.DirectionPull
		raise NotImplemented

	def face_propagation(self):
		"""Gets or sets the face propagation for this draft feature."""
		# return self._instance.FacePropagation
		raise NotImplemented

	def faces_to_draft(self):
		"""Gets or sets the faces that define this draft feature."""
		# return self._instance.FacesToDraft
		raise NotImplemented

	def neutral_plane(self):
		"""Gets or sets the neutral plane for this draft feature."""
		# return self._instance.NeutralPlane
		raise NotImplemented

	def parting_lines(self):
		"""Gets or sets the parting lines for this draft feature."""
		# return self._instance.PartingLines
		raise NotImplemented

	def reverse_direction(self):
		"""Gets or sets whether the direction of the draft feature is reversed."""
		# return self._instance.ReverseDirection
		raise NotImplemented

	def step_type(self):
		"""Gets or sets the step type for this draft feature."""
		# return self._instance.StepType
		raise NotImplemented

	def type(self):
		"""Gets the type of draft feature."""
		# return self._instance.Type
		raise NotImplemented

	def access_selections(self, top_doc, component):
		"""
		Accesses the selections that define this draft feature.
		:param top_doc: Top-level document
		:param component: Component in which the feature is to be modified
		"""
		# return self._instance.AccessSelections(top_doc, component)
		raise NotImplemented

	def get_drafted_entities(self):
		"""Gets the drafted entities (faces or edges) for this draft feature."""
		# return self._instance.GetDraftedEntities
		raise NotImplemented

	def get_drafted_entity_count(self):
		"""Gets the number of drafted entities for this draft feature."""
		# return self._instance.GetDraftedEntityCount
		raise NotImplemented

	def get_faces_to_draft_count(self):
		"""Gets the number of faces that define the draft feature."""
		# return self._instance.GetFacesToDraftCount
		raise NotImplemented

	def get_other_faces_flag_at_index(self, index):
		"""
		Gets the value of the Other Face option at the specified index.
		:param index: Number indicating a segment of the parting line
		"""
		# return self._instance.GetOtherFacesFlagAtIndex(index)
		raise NotImplemented

	def get_parting_lines_count(self):
		"""Gets the number of parting lines for this draft feature."""
		# return self._instance.GetPartingLinesCount
		raise NotImplemented

	def i_access_selections(self, top_doc, component):
		"""
		Accesses the selections that define this draft feature.
		:param top_doc: Top-level document
		:param component: Component in which the feature is to be modified
		"""
		# return self._instance.IAccessSelections(top_doc, component)
		raise NotImplemented

	def i_get_drafted_entities(self, count):
		"""
		Gets the drafted entities (faces or edges) for this draft feature.
		:param count: Number of entities
		"""
		# return self._instance.IGetDraftedEntities(count)
		raise NotImplemented

	def i_get_faces_to_draft(self, count):
		"""
		Gets the faces that define this draft feature.
		:param count: Number of faces
		"""
		# return self._instance.IGetFacesToDraft(count)
		raise NotImplemented

	def i_get_parting_lines(self, count):
		"""
		Gets the parting lines that define this draft feature.
		:param count: Number of parting lines
		"""
		# return self._instance.IGetPartingLines(count)
		raise NotImplemented

	def i_set_faces_to_draft(self, count, face_array):
		"""
		Sets the faces to which to apply the draft feature.
		:param count: Number of faces
		:param face_array: 

in-process, unmanaged C++: Pointer to an array of faces of size Count
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.ISetFacesToDraft(count, face_array)
		raise NotImplemented

	def i_set_parting_lines(self, count, line_array):
		"""
		Sets the parting lines for this draft feature.
		:param count: Number of parting lines
		:param line_array: 
in-process, unmanaged C++: Pointer to an array of parting lines of size Count
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.ISetPartingLines(count, line_array)
		raise NotImplemented

	def release_selection_access(self):
		"""Releases access to the selections for this draft feature."""
		# return self._instance.ReleaseSelectionAccess
		raise NotImplemented

	def set_other_faces_flag_at_index(self, index, flag):
		"""
		Sets the Other Face option.
		:param index: Number indicating a segment of the parting line
		:param flag: True to specify a different draft direction for each segment of the parting line,false to not
		"""
		# return self._instance.SetOtherFacesFlagAtIndex(index, flag)
		raise NotImplemented

