# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFoldsFeatureData_members.html
class IFoldsFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bends(self):
		"""Gets or sets the bend features for this fold feature."""
		return self._instance.Bends

	@bends.setter
	def bends(self, value):
		"""Gets or sets the bend features for this fold feature."""
		self._instance.Bends = value

	@property
	def fixed_face(self):
		"""Gets or sets the fixed face of this fold feature."""
		return self._instance.FixedFace

	@fixed_face.setter
	def fixed_face(self, value):
		"""Gets or sets the fixed face of this fold feature."""
		self._instance.FixedFace = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe this fold feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe this fold feature."""
		self._instance.AccessSelections = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that describe this fold feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that describe this fold feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_bends(self):
		"""Gets the bend features for this fold feature."""
		return self._instance.IGetBends

	@i_get_bends.setter
	def i_get_bends(self, value):
		"""Gets the bend features for this fold feature."""
		self._instance.IGetBends = value

	@property
	def i_get_bends_count(self):
		"""Gets the number of bend features in this fold feature."""
		return self._instance.IGetBendsCount

	@i_get_bends_count.setter
	def i_get_bends_count(self, value):
		"""Gets the number of bend features in this fold feature."""
		self._instance.IGetBendsCount = value

	@property
	def i_set_bends(self):
		"""Sets the bend features for this fold feature."""
		return self._instance.ISetBends

	@i_set_bends.setter
	def i_set_bends(self, value):
		"""Sets the bend features for this fold feature."""
		self._instance.ISetBends = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe this fold feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe this fold feature."""
		self._instance.ReleaseSelectionAccess = value

