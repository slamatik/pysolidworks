# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxisFeatureData_members.html
class IRefAxisFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def type(self):
		"""Gets or sets the type of reference axis feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of reference axis feature."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this reference axis feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this reference axis feature."""
		self._instance.AccessSelections = value

	@property
	def get_selections(self):
		"""Gets the selected entities for this reference axis feature."""
		return self._instance.GetSelections

	@get_selections.setter
	def get_selections(self, value):
		"""Gets the selected entities for this reference axis feature."""
		self._instance.GetSelections = value

	@property
	def get_selections_count(self):
		"""Gets the number of selections that define this reference axis feature."""
		return self._instance.GetSelectionsCount

	@get_selections_count.setter
	def get_selections_count(self, value):
		"""Gets the number of selections that define this reference axis feature."""
		self._instance.GetSelectionsCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this reference axis feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this reference axis feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_selections(self):
		"""Gets the selected entities for this reference axis feature."""
		return self._instance.IGetSelections

	@i_get_selections.setter
	def i_get_selections(self, value):
		"""Gets the selected entities for this reference axis feature."""
		self._instance.IGetSelections = value

	@property
	def i_set_selections(self):
		"""Sets the entities for this reference axis feature."""
		return self._instance.ISetSelections

	@i_set_selections.setter
	def i_set_selections(self, value):
		"""Sets the entities for this reference axis feature."""
		self._instance.ISetSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this reference axis feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this reference axis feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_selections(self):
		"""Sets the entities for this reference axis feature."""
		return self._instance.SetSelections

	@set_selections.setter
	def set_selections(self, value):
		"""Sets the entities for this reference axis feature."""
		self._instance.SetSelections = value

