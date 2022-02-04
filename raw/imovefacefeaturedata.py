# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html
class IMoveFaceFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the angle for the Move Face feature."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle for the Move Face feature."""
		self._instance.Angle = value

	@property
	def distance(self):
		"""Gets or sets the offset distance of this offset or translated Move Face feature."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the offset distance of this offset or translated Move Face feature."""
		self._instance.Distance = value

	@property
	def end_condition(self):
		"""Gets the end condition for this translated Move Face feature."""
		return self._instance.EndCondition

	@end_condition.setter
	def end_condition(self, value):
		"""Gets the end condition for this translated Move Face feature."""
		self._instance.EndCondition = value

	@property
	def faces(self):
		"""Gets or sets the faces for the Move Face feature."""
		return self._instance.Faces

	@faces.setter
	def faces(self, value):
		"""Gets or sets the faces for the Move Face feature."""
		self._instance.Faces = value

	@property
	def move_type(self):
		"""Gets or sets the type of Move Face feature."""
		return self._instance.MoveType

	@move_type.setter
	def move_type(self, value):
		"""Gets or sets the type of Move Face feature."""
		self._instance.MoveType = value

	@property
	def offset_distance(self):
		"""Gets or sets the offset distance of this translated Move Face feature that has an end condition of Offset From Surface."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the offset distance of this translated Move Face feature that has an end condition of Offset From Surface."""
		self._instance.OffsetDistance = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of the Move Face feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of the Move Face feature."""
		self._instance.ReverseDirection = value

	@property
	def triad_rotation_parameters(self):
		"""Gets or sets the rotation parameters for this Move Face feature."""
		return self._instance.TriadRotationParameters

	@triad_rotation_parameters.setter
	def triad_rotation_parameters(self, value):
		"""Gets or sets the rotation parameters for this Move Face feature."""
		self._instance.TriadRotationParameters = value

	@property
	def triad_translation_parameters(self):
		"""Gets or sets the translation parameters for this Move Face feature."""
		return self._instance.TriadTranslationParameters

	@triad_translation_parameters.setter
	def triad_translation_parameters(self, value):
		"""Gets or sets the translation parameters for this Move Face feature."""
		self._instance.TriadTranslationParameters = value

	@property
	def access_selections(self):
		"""Gains access to selections that define this Move Face feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections that define this Move Face feature."""
		self._instance.AccessSelections = value

	@property
	def get_direction_reference(self):
		"""Gets the direction reference for this Move Face feature."""
		return self._instance.GetDirectionReference

	@get_direction_reference.setter
	def get_direction_reference(self, value):
		"""Gets the direction reference for this Move Face feature."""
		self._instance.GetDirectionReference = value

	@property
	def get_end_condition_entity(self):
		"""Gets the entity to which the Move Face feature is translated."""
		return self._instance.GetEndConditionEntity

	@get_end_condition_entity.setter
	def get_end_condition_entity(self, value):
		"""Gets the entity to which the Move Face feature is translated."""
		self._instance.GetEndConditionEntity = value

	@property
	def get_faces_count(self):
		"""Gets the number of faces for this Move Face feature."""
		return self._instance.GetFacesCount

	@get_faces_count.setter
	def get_faces_count(self, value):
		"""Gets the number of faces for this Move Face feature."""
		self._instance.GetFacesCount = value

	@property
	def get_from_entity(self):
		"""Gets the entity from which the face of the Move Face feature is translated."""
		return self._instance.GetFromEntity

	@get_from_entity.setter
	def get_from_entity(self, value):
		"""Gets the entity from which the face of the Move Face feature is translated."""
		self._instance.GetFromEntity = value

	@property
	def i_get_faces(self):
		"""Gets the faces for this Move Face feature."""
		return self._instance.IGetFaces

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets the faces for this Move Face feature."""
		self._instance.IGetFaces = value

	@property
	def i_get_triad_rotation_parameters(self):
		"""Gets the rotation parameters for this Move Face feature."""
		return self._instance.IGetTriadRotationParameters

	@i_get_triad_rotation_parameters.setter
	def i_get_triad_rotation_parameters(self, value):
		"""Gets the rotation parameters for this Move Face feature."""
		self._instance.IGetTriadRotationParameters = value

	@property
	def i_get_triad_translation_parameters(self):
		"""Gets the translation parameters for this Move Face feature."""
		return self._instance.IGetTriadTranslationParameters

	@i_get_triad_translation_parameters.setter
	def i_get_triad_translation_parameters(self, value):
		"""Gets the translation parameters for this Move Face feature."""
		self._instance.IGetTriadTranslationParameters = value

	@property
	def i_set_faces(self):
		"""Sets the faces for this Move Face feature."""
		return self._instance.ISetFaces

	@i_set_faces.setter
	def i_set_faces(self, value):
		"""Sets the faces for this Move Face feature."""
		self._instance.ISetFaces = value

	@property
	def i_set_triad_rotation_parameters(self):
		"""Sets the rotation parameters for this Move Face feature."""
		return self._instance.ISetTriadRotationParameters

	@i_set_triad_rotation_parameters.setter
	def i_set_triad_rotation_parameters(self, value):
		"""Sets the rotation parameters for this Move Face feature."""
		self._instance.ISetTriadRotationParameters = value

	@property
	def i_set_triad_translation_parameters(self):
		"""Sets the translation parameters for this Move Face feature."""
		return self._instance.ISetTriadTranslationParameters

	@i_set_triad_translation_parameters.setter
	def i_set_triad_translation_parameters(self, value):
		"""Sets the translation parameters for this Move Face feature."""
		self._instance.ISetTriadTranslationParameters = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this Move Face feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this Move Face feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_direction_reference(self):
		"""Sets the direction reference for the Move Face feature."""
		return self._instance.SetDirectionReference

	@set_direction_reference.setter
	def set_direction_reference(self, value):
		"""Sets the direction reference for the Move Face feature."""
		self._instance.SetDirectionReference = value

	@property
	def set_end_condition_entity(self):
		"""Sets the entity to which the face of the Move Face feature is translated."""
		return self._instance.SetEndConditionEntity

	@set_end_condition_entity.setter
	def set_end_condition_entity(self, value):
		"""Sets the entity to which the face of the Move Face feature is translated."""
		self._instance.SetEndConditionEntity = value

	@property
	def set_from_entity(self):
		"""Sets the entity from which the face of the Move Face feature is translated."""
		return self._instance.SetFromEntity

	@set_from_entity.setter
	def set_from_entity(self, value):
		"""Sets the entity from which the face of the Move Face feature is translated."""
		self._instance.SetFromEntity = value

