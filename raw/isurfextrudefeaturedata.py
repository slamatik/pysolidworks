# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfExtrudeFeatureData_members.html
class ISurfExtrudeFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def both_directions(self):
		"""Gets or sets whether this surface is extruded in both directions."""
		return self._instance.BothDirections

	@both_directions.setter
	def both_directions(self, value):
		"""Gets or sets whether this surface is extruded in both directions."""
		self._instance.BothDirections = value

	@property
	def d_cap_end(self):
		"""Gets or sets whether to cap the end of the extruded surface in Direction 1."""
		return self._instance.D1CapEnd

	@d_cap_end.setter
	def d_cap_end(self, value):
		"""Gets or sets whether to cap the end of the extruded surface in Direction 1."""
		self._instance.D1CapEnd = value

	@property
	def d_draft_angle(self):
		"""Gets or sets the angle of the draft of this extruded surface in Direction 1."""
		return self._instance.D1DraftAngle

	@d_draft_angle.setter
	def d_draft_angle(self, value):
		"""Gets or sets the angle of the draft of this extruded surface in Direction 1."""
		self._instance.D1DraftAngle = value

	@property
	def d_draft_on(self):
		"""Gets or sets whether to draft the extruded surface in Direction 1."""
		return self._instance.D1DraftOn

	@d_draft_on.setter
	def d_draft_on(self, value):
		"""Gets or sets whether to draft the extruded surface in Direction 1."""
		self._instance.D1DraftOn = value

	@property
	def d_draft_outward(self):
		"""Gets or sets whether to draft the extruded surface outward or inward in Direction 1."""
		return self._instance.D1DraftOutward

	@d_draft_outward.setter
	def d_draft_outward(self, value):
		"""Gets or sets whether to draft the extruded surface outward or inward in Direction 1."""
		self._instance.D1DraftOutward = value

	@property
	def d_cap_end(self):
		"""Gets or sets whether to cap the end of the extruded surface in Direction 2."""
		return self._instance.D2CapEnd

	@d_cap_end.setter
	def d_cap_end(self, value):
		"""Gets or sets whether to cap the end of the extruded surface in Direction 2."""
		self._instance.D2CapEnd = value

	@property
	def d_draft_angle(self):
		"""Gets or sets the angle of the draft of this extruded surface in Direction 2."""
		return self._instance.D2DraftAngle

	@d_draft_angle.setter
	def d_draft_angle(self, value):
		"""Gets or sets the angle of the draft of this extruded surface in Direction 2."""
		self._instance.D2DraftAngle = value

	@property
	def d_draft_on(self):
		"""Gets or sets whether to draft the extruded surface in Direction 2."""
		return self._instance.D2DraftOn

	@d_draft_on.setter
	def d_draft_on(self, value):
		"""Gets or sets whether to draft the extruded surface in Direction 2."""
		self._instance.D2DraftOn = value

	@property
	def d_draft_outward(self):
		"""Gets or sets whether to draft the extruded surface outward or inward in Direction 2."""
		return self._instance.D2DraftOutward

	@d_draft_outward.setter
	def d_draft_outward(self, value):
		"""Gets or sets whether to draft the extruded surface outward or inward in Direction 2."""
		self._instance.D2DraftOutward = value

	@property
	def delete_original_face(self):
		"""Gets or sets whether to delete the original faces of this extruded surface."""
		return self._instance.DeleteOriginalFace

	@delete_original_face.setter
	def delete_original_face(self, value):
		"""Gets or sets whether to delete the original faces of this extruded surface."""
		self._instance.DeleteOriginalFace = value

	@property
	def knit_result(self):
		"""Gets or sets whether to knit the bodies created by deleting original faces in an extruded surface."""
		return self._instance.KnitResult

	@knit_result.setter
	def knit_result(self, value):
		"""Gets or sets whether to knit the bodies created by deleting original faces in an extruded surface."""
		self._instance.KnitResult = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether the direction of this extruded surface is reversed."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether the direction of this extruded surface is reversed."""
		self._instance.ReverseDirection = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this extruded surface."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this extruded surface."""
		self._instance.AccessSelections = value

	@property
	def get_depth(self):
		"""Gets the depth of the feature in the forward or reverse direction."""
		return self._instance.GetDepth

	@get_depth.setter
	def get_depth(self, value):
		"""Gets the depth of the feature in the forward or reverse direction."""
		self._instance.GetDepth = value

	@property
	def get_end_condition(self):
		"""Gets the end condition of this extruded surface for the forward or reverse direction."""
		return self._instance.GetEndCondition

	@get_end_condition.setter
	def get_end_condition(self, value):
		"""Gets the end condition of this extruded surface for the forward or reverse direction."""
		self._instance.GetEndCondition = value

	@property
	def get_face(self):
		"""Gets the end condition face for this extruded surface in the forward or reverse direction."""
		return self._instance.GetFace

	@get_face.setter
	def get_face(self, value):
		"""Gets the end condition face for this extruded surface in the forward or reverse direction."""
		self._instance.GetFace = value

	@property
	def get_reverse_offset(self):
		"""Gets the reverse offset direction setting for the end condition of this extruded surface."""
		return self._instance.GetReverseOffset

	@get_reverse_offset.setter
	def get_reverse_offset(self, value):
		"""Gets the reverse offset direction setting for the end condition of this extruded surface."""
		self._instance.GetReverseOffset = value

	@property
	def get_translate_surface(self):
		"""Gets the translate surface setting for this extruded surface."""
		return self._instance.GetTranslateSurface

	@get_translate_surface.setter
	def get_translate_surface(self, value):
		"""Gets the translate surface setting for this extruded surface."""
		self._instance.GetTranslateSurface = value

	@property
	def get_vertex(self):
		"""Gets the end condition vertex in the forward or reverse direction for this extruded surface."""
		return self._instance.GetVertex

	@get_vertex.setter
	def get_vertex(self, value):
		"""Gets the end condition vertex in the forward or reverse direction for this extruded surface."""
		self._instance.GetVertex = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this extruded surface."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this extruded surface."""
		self._instance.IAccessSelections = value

	@property
	def i_get_face(self):
		"""Gets the end condition face for this extruded surface in the forward or reverse direction."""
		return self._instance.IGetFace

	@i_get_face.setter
	def i_get_face(self, value):
		"""Gets the end condition face for this extruded surface in the forward or reverse direction."""
		self._instance.IGetFace = value

	@property
	def i_get_vertex(self):
		"""Gets the end condition vertex in the forward or reverse direction for this extruded surface."""
		return self._instance.IGetVertex

	@i_get_vertex.setter
	def i_get_vertex(self, value):
		"""Gets the end condition vertex in the forward or reverse direction for this extruded surface."""
		self._instance.IGetVertex = value

	@property
	def i_set_face(self):
		"""Sets the end condition face for this extruded surface in the forward or reverse direction."""
		return self._instance.ISetFace

	@i_set_face.setter
	def i_set_face(self, value):
		"""Sets the end condition face for this extruded surface in the forward or reverse direction."""
		self._instance.ISetFace = value

	@property
	def i_set_vertex(self):
		"""Sets the end condition vertex in the forward or reverse direction for this extruded surface."""
		return self._instance.ISetVertex

	@i_set_vertex.setter
	def i_set_vertex(self, value):
		"""Sets the end condition vertex in the forward or reverse direction for this extruded surface."""
		self._instance.ISetVertex = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this extruded surface."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this extruded surface."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_depth(self):
		"""Sets the depth of this extruded surface in the forward or reverse direction."""
		return self._instance.SetDepth

	@set_depth.setter
	def set_depth(self, value):
		"""Sets the depth of this extruded surface in the forward or reverse direction."""
		self._instance.SetDepth = value

	@property
	def set_end_condition(self):
		"""Sets the end condition of this extruded surface in the forward or reverse direction."""
		return self._instance.SetEndCondition

	@set_end_condition.setter
	def set_end_condition(self, value):
		"""Sets the end condition of this extruded surface in the forward or reverse direction."""
		self._instance.SetEndCondition = value

	@property
	def set_face(self):
		"""Sets the end condition face for this extruded surface in the forward or reverse direction."""
		return self._instance.SetFace

	@set_face.setter
	def set_face(self, value):
		"""Sets the end condition face for this extruded surface in the forward or reverse direction."""
		self._instance.SetFace = value

	@property
	def set_reverse_offset(self):
		"""Sets the reverse offset direction setting for the end condition of this extruded surface."""
		return self._instance.SetReverseOffset

	@set_reverse_offset.setter
	def set_reverse_offset(self, value):
		"""Sets the reverse offset direction setting for the end condition of this extruded surface."""
		self._instance.SetReverseOffset = value

	@property
	def set_translate_surface(self):
		"""Sets the translate surface setting for this extruded surface."""
		return self._instance.SetTranslateSurface

	@set_translate_surface.setter
	def set_translate_surface(self, value):
		"""Sets the translate surface setting for this extruded surface."""
		self._instance.SetTranslateSurface = value

	@property
	def set_vertex(self):
		"""Sets the end condition vertex in the forward or reverse direction for this extruded surface."""
		return self._instance.SetVertex

	@set_vertex.setter
	def set_vertex(self, value):
		"""Sets the end condition vertex in the forward or reverse direction for this extruded surface."""
		self._instance.SetVertex = value

