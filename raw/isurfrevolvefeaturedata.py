# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfRevolveFeatureData_members.html
class ISurfRevolveFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def reverse_direction(self):
		"""Gets or sets the reverse direction setting for this surface revolve feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets the reverse direction setting for this surface revolve feature."""
		self._instance.ReverseDirection = value

	@property
	def type(self):
		"""Gets or sets the type for this surface revolve feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type for this surface revolve feature."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this surface revolve feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this surface revolve feature."""
		self._instance.AccessSelections = value

	@property
	def get_revolution_angle(self):
		"""Gets the angle for this surface revolve feature in Direction 1 or Direction 2."""
		return self._instance.GetRevolutionAngle

	@get_revolution_angle.setter
	def get_revolution_angle(self, value):
		"""Gets the angle for this surface revolve feature in Direction 1 or Direction 2."""
		self._instance.GetRevolutionAngle = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this surface revolve feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this surface revolve feature."""
		self._instance.IAccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this surface revolve feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this surface revolve feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_revolution_angle(self):
		"""Sets the angle for this surface revolve feature in Direction 1 or Direction 2."""
		return self._instance.SetRevolutionAngle

	@set_revolution_angle.setter
	def set_revolution_angle(self, value):
		"""Sets the angle for this surface revolve feature in Direction 1 or Direction 2."""
		self._instance.SetRevolutionAngle = value

