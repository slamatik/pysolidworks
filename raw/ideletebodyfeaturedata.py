# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData_members.html
class IDeleteBodyFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bodies(self):
		"""Gets or sets the bodies to delete or keep."""
		return self._instance.Bodies

	@bodies.setter
	def bodies(self, value):
		"""Gets or sets the bodies to delete or keep."""
		self._instance.Bodies = value

	@property
	def keep_bodies(self):
		"""Gets or sets whether to keep bodies."""
		return self._instance.KeepBodies

	@keep_bodies.setter
	def keep_bodies(self, value):
		"""Gets or sets whether to keep bodies."""
		self._instance.KeepBodies = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe this Body-Delete/Keep feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe this Body-Delete/Keep feature."""
		self._instance.AccessSelections = value

	@property
	def get_bodies_count(self):
		"""Gets the number of bodies to delete or keep."""
		return self._instance.GetBodiesCount

	@get_bodies_count.setter
	def get_bodies_count(self, value):
		"""Gets the number of bodies to delete or keep."""
		self._instance.GetBodiesCount = value

	@property
	def i_get_bodies(self):
		"""Gets the bodies to delete."""
		return self._instance.IGetBodies

	@i_get_bodies.setter
	def i_get_bodies(self, value):
		"""Gets the bodies to delete."""
		self._instance.IGetBodies = value

	@property
	def i_set_bodies(self):
		"""Sets the bodies to delete."""
		return self._instance.ISetBodies

	@i_set_bodies.setter
	def i_set_bodies(self, value):
		"""Sets the bodies to delete."""
		self._instance.ISetBodies = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe this Body-Delete/Keep feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe this Body-Delete/Keep feature."""
		self._instance.ReleaseSelectionAccess = value

