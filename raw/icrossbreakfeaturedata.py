# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICrossBreakFeatureData_members.html
class ICrossBreakFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def break_angle(self):
		"""Gets or sets the angle for this cross break feature."""
		return self._instance.BreakAngle

	@break_angle.setter
	def break_angle(self, value):
		"""Gets or sets the angle for this cross break feature."""
		self._instance.BreakAngle = value

	@property
	def break_radius(self):
		"""Gets or sets the radius for this cross break feature."""
		return self._instance.BreakRadius

	@break_radius.setter
	def break_radius(self, value):
		"""Gets or sets the radius for this cross break feature."""
		self._instance.BreakRadius = value

	@property
	def face(self):
		"""Gets or sets the face to which to apply this cross break feature."""
		return self._instance.Face

	@face.setter
	def face(self, value):
		"""Gets or sets the face to which to apply this cross break feature."""
		self._instance.Face = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of this cross break feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of this cross break feature."""
		self._instance.ReverseDirection = value

	@property
	def access_selections(self):
		"""Allows access to the selections that define this cross break feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Allows access to the selections that define this cross break feature."""
		self._instance.AccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this cross break feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this cross break feature."""
		self._instance.ReleaseSelectionAccess = value

