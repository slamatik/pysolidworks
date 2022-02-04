# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJoinFeatureData_members.html
class IJoinFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def force_surface_contact(self):
		"""Gets or sets whether to join any coincident faces and any intruding volumes."""
		return self._instance.ForceSurfaceContact

	@force_surface_contact.setter
	def force_surface_contact(self, value):
		"""Gets or sets whether to join any coincident faces and any intruding volumes."""
		self._instance.ForceSurfaceContact = value

	@property
	def hide_parts(self):
		"""Gets or sets whether the original components are hidden after joined."""
		return self._instance.HideParts

	@hide_parts.setter
	def hide_parts(self, value):
		"""Gets or sets whether the original components are hidden after joined."""
		self._instance.HideParts = value

	@property
	def joined_parts(self):
		"""Gets and sets the parts to join."""
		return self._instance.JoinedParts

	@joined_parts.setter
	def joined_parts(self, value):
		"""Gets and sets the parts to join."""
		self._instance.JoinedParts = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this join feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this join feature."""
		self._instance.AccessSelections = value

	@property
	def get_joined_parts_count(self):
		"""Gets the number of joined parts."""
		return self._instance.GetJoinedPartsCount

	@get_joined_parts_count.setter
	def get_joined_parts_count(self, value):
		"""Gets the number of joined parts."""
		self._instance.GetJoinedPartsCount = value

	@property
	def i_get_joined_parts(self):
		"""Gets the joined parts."""
		return self._instance.IGetJoinedParts

	@i_get_joined_parts.setter
	def i_get_joined_parts(self, value):
		"""Gets the joined parts."""
		self._instance.IGetJoinedParts = value

	@property
	def i_set_joined_parts(self):
		"""Sets the parts to join."""
		return self._instance.ISetJoinedParts

	@i_set_joined_parts.setter
	def i_set_joined_parts(self, value):
		"""Sets the parts to join."""
		self._instance.ISetJoinedParts = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this join feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this join feature."""
		self._instance.ReleaseSelectionAccess = value

