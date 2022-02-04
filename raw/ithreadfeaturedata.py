# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.html
class IThreadFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def blind_depth(self):
		"""Gets or sets the distance from the blind end condition reference of this thread feature, taking into account any offset."""
		return self._instance.BlindDepth

	@blind_depth.setter
	def blind_depth(self, value):
		"""Gets or sets the distance from the blind end condition reference of this thread feature, taking into account any offset."""
		self._instance.BlindDepth = value

	@property
	def diameter(self):
		"""Gets or sets the diameter of the cylindrical face or helix of this thread feature."""
		return self._instance.Diameter

	@diameter.setter
	def diameter(self, value):
		"""Gets or sets the diameter of the cylindrical face or helix of this thread feature."""
		self._instance.Diameter = value

	@property
	def diameter_override(self):
		"""Gets or sets whether to override the diameter of the cylindrical face or helix of this thread feature."""
		return self._instance.DiameterOverride

	@diameter_override.setter
	def diameter_override(self, value):
		"""Gets or sets whether to override the diameter of the cylindrical face or helix of this thread feature."""
		self._instance.DiameterOverride = value

	@property
	def edge(self):
		"""Gets or sets the entity where to start the helix of this thread feature."""
		return self._instance.Edge

	@edge.setter
	def edge(self, value):
		"""Gets or sets the entity where to start the helix of this thread feature."""
		self._instance.Edge = value

	@property
	def end_condition(self):
		"""Gets or sets the end condition for this thread feature."""
		return self._instance.EndCondition

	@end_condition.setter
	def end_condition(self, value):
		"""Gets or sets the end condition for this thread feature."""
		self._instance.EndCondition = value

	@property
	def end_condition_offset(self):
		"""Gets or sets whether to offset the end condition of this thread feature."""
		return self._instance.EndConditionOffset

	@end_condition_offset.setter
	def end_condition_offset(self, value):
		"""Gets or sets whether to offset the end condition of this thread feature."""
		self._instance.EndConditionOffset = value

	@property
	def end_condition_offset_distance(self):
		"""Gets or sets the end condition offset distance of this thread feature."""
		return self._instance.EndConditionOffsetDistance

	@end_condition_offset_distance.setter
	def end_condition_offset_distance(self, value):
		"""Gets or sets the end condition offset distance of this thread feature."""
		self._instance.EndConditionOffsetDistance = value

	@property
	def end_condition_offset_reverse(self):
		"""Gets or sets whether to flip the offset of the end condition to the opposite side of the end condition reference in this thread feature."""
		return self._instance.EndConditionOffsetReverse

	@end_condition_offset_reverse.setter
	def end_condition_offset_reverse(self, value):
		"""Gets or sets whether to flip the offset of the end condition to the opposite side of the end condition reference in this thread feature."""
		self._instance.EndConditionOffsetReverse = value

	@property
	def maintain_thread_length(self):
		"""Gets or sets whether to keep the thread a constant length from the starting surface in this thread feature."""
		return self._instance.MaintainThreadLength

	@maintain_thread_length.setter
	def maintain_thread_length(self, value):
		"""Gets or sets whether to keep the thread a constant length from the starting surface in this thread feature."""
		self._instance.MaintainThreadLength = value

	@property
	def mirror_profile(self):
		"""Gets or sets whether to flip the profile of the thread helix about its horizontal or vertical axis in this thread feature."""
		return self._instance.MirrorProfile

	@mirror_profile.setter
	def mirror_profile(self, value):
		"""Gets or sets whether to flip the profile of the thread helix about its horizontal or vertical axis in this thread feature."""
		self._instance.MirrorProfile = value

	@property
	def mirror_type(self):
		"""Gets or sets how to flip the profile of the thread helix of this thread feature."""
		return self._instance.MirrorType

	@mirror_type.setter
	def mirror_type(self, value):
		"""Gets or sets how to flip the profile of the thread helix of this thread feature."""
		self._instance.MirrorType = value

	@property
	def multiple_start(self):
		"""Gets or sets whether the thread has multiple starts in this thread feature."""
		return self._instance.MultipleStart

	@multiple_start.setter
	def multiple_start(self, value):
		"""Gets or sets whether the thread has multiple starts in this thread feature."""
		self._instance.MultipleStart = value

	@property
	def number_of_starts(self):
		"""Gets or sets the number of times the thread is created in an evenly-spaced pattern around the hole or shaft of this thread feature."""
		return self._instance.NumberOfStarts

	@number_of_starts.setter
	def number_of_starts(self, value):
		"""Gets or sets the number of times the thread is created in an evenly-spaced pattern around the hole or shaft of this thread feature."""
		self._instance.NumberOfStarts = value

	@property
	def offset(self):
		"""Gets or sets whether to offset the starting location of the helix of this thread feature."""
		return self._instance.Offset

	@offset.setter
	def offset(self, value):
		"""Gets or sets whether to offset the starting location of the helix of this thread feature."""
		self._instance.Offset = value

	@property
	def offset_distance(self):
		"""Gets or sets the offset of the starting location of the helix of this thread feature."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the offset of the starting location of the helix of this thread feature."""
		self._instance.OffsetDistance = value

	@property
	def pitch(self):
		"""Gets or sets the pitch of the thread helix of this thread feature."""
		return self._instance.Pitch

	@pitch.setter
	def pitch(self, value):
		"""Gets or sets the pitch of the thread helix of this thread feature."""
		self._instance.Pitch = value

	@property
	def pitch_override(self):
		"""Gets or sets whether to override the pitch of the thread helix of this thread feature."""
		return self._instance.PitchOverride

	@pitch_override.setter
	def pitch_override(self, value):
		"""Gets or sets whether to override the pitch of the thread helix of this thread feature."""
		self._instance.PitchOverride = value

	@property
	def profile_location(self):
		"""Gets or sets the point or vertex where to start the helix on the thread profile sketch of this thread feature."""
		return self._instance.ProfileLocation

	@profile_location.setter
	def profile_location(self, value):
		"""Gets or sets the point or vertex where to start the helix on the thread profile sketch of this thread feature."""
		self._instance.ProfileLocation = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of the Blind or Revolutions end condition of this thread feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of the Blind or Revolutions end condition of this thread feature."""
		self._instance.ReverseDirection = value

	@property
	def reverse_offset(self):
		"""Gets or sets whether to flip the offset of the helix to the opposite side of the starting entity in this thread feature."""
		return self._instance.ReverseOffset

	@reverse_offset.setter
	def reverse_offset(self, value):
		"""Gets or sets whether to flip the offset of the helix to the opposite side of the starting entity in this thread feature."""
		self._instance.ReverseOffset = value

	@property
	def revolutions(self):
		"""Gets or sets the number of revolutions in the helix of this thread feature, taking into account any offset."""
		return self._instance.Revolutions

	@revolutions.setter
	def revolutions(self, value):
		"""Gets or sets the number of revolutions in the helix of this thread feature, taking into account any offset."""
		self._instance.Revolutions = value

	@property
	def right_handed(self):
		"""Gets or sets how the thread is wound in this thread feature."""
		return self._instance.RightHanded

	@right_handed.setter
	def right_handed(self, value):
		"""Gets or sets how the thread is wound in this thread feature."""
		self._instance.RightHanded = value

	@property
	def rotation_angle(self):
		"""Gets or sets the angle of rotation of the thread helix of this thread feature."""
		return self._instance.RotationAngle

	@rotation_angle.setter
	def rotation_angle(self, value):
		"""Gets or sets the angle of rotation of the thread helix of this thread feature."""
		self._instance.RotationAngle = value

	@property
	def size(self):
		"""Gets or sets the size of the thread of this thread feature."""
		return self._instance.Size

	@size.setter
	def size(self, value):
		"""Gets or sets the size of the thread of this thread feature."""
		self._instance.Size = value

	@property
	def start_entity(self):
		"""Gets or sets the starting entity for the helix of this thread feature."""
		return self._instance.StartEntity

	@start_entity.setter
	def start_entity(self, value):
		"""Gets or sets the starting entity for the helix of this thread feature."""
		self._instance.StartEntity = value

	@property
	def thread_method(self):
		"""Gets or sets the thread method for this thread feature."""
		return self._instance.ThreadMethod

	@thread_method.setter
	def thread_method(self, value):
		"""Gets or sets the thread method for this thread feature."""
		self._instance.ThreadMethod = value

	@property
	def thread_start_angle(self):
		"""Gets or sets the start angle of the thread of this thread feature"""
		return self._instance.ThreadStartAngle

	@thread_start_angle.setter
	def thread_start_angle(self, value):
		"""Gets or sets the start angle of the thread of this thread feature"""
		self._instance.ThreadStartAngle = value

	@property
	def trim_end_face(self):
		"""Gets or sets whether to align the thread to the end face of this thread feaure."""
		return self._instance.TrimEndFace

	@trim_end_face.setter
	def trim_end_face(self, value):
		"""Gets or sets whether to align the thread to the end face of this thread feaure."""
		self._instance.TrimEndFace = value

	@property
	def trim_start_face(self):
		"""Gets or sets whether to align the thread to the start face of this thread feaure."""
		return self._instance.TrimStartFace

	@trim_start_face.setter
	def trim_start_face(self, value):
		"""Gets or sets whether to align the thread to the start face of this thread feaure."""
		self._instance.TrimStartFace = value

	@property
	def type(self):
		"""Gets or sets the thread profile of this thread feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the thread profile of this thread feature."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this thread feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this thread feature."""
		self._instance.AccessSelections = value

	@property
	def get_end_condition_reference(self):
		"""Gets the Up To Selection end condition reference of this thread feature."""
		return self._instance.GetEndConditionReference

	@get_end_condition_reference.setter
	def get_end_condition_reference(self, value):
		"""Gets the Up To Selection end condition reference of this thread feature."""
		self._instance.GetEndConditionReference = value

	@property
	def initialize_thread_data(self):
		"""Initializes this thread feature's data with default values."""
		return self._instance.InitializeThreadData

	@initialize_thread_data.setter
	def initialize_thread_data(self, value):
		"""Initializes this thread feature's data with default values."""
		self._instance.InitializeThreadData = value

	@property
	def release_selection_access(self):
		"""Releases the selections that created this thread feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases the selections that created this thread feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_end_condition_reference(self):
		"""Sets the Up To Selection end condition reference of this thread feature."""
		return self._instance.SetEndConditionReference

	@set_end_condition_reference.setter
	def set_end_condition_reference(self, value):
		"""Sets the Up To Selection end condition reference of this thread feature."""
		self._instance.SetEndConditionReference = value

