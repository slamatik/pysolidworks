# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReplaceFaceFeatureData_members.html
class IReplaceFaceFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def faces_for_replacement(self):
		"""Gets or sets the faces to replace for this feature."""
		return self._instance.FacesForReplacement

	@faces_for_replacement.setter
	def faces_for_replacement(self, value):
		"""Gets or sets the faces to replace for this feature."""
		self._instance.FacesForReplacement = value

	@property
	def replacement_surfaces(self):
		"""Gets or sets the replacement surfaces for this feature."""
		return self._instance.ReplacementSurfaces

	@replacement_surfaces.setter
	def replacement_surfaces(self, value):
		"""Gets or sets the replacement surfaces for this feature."""
		self._instance.ReplacementSurfaces = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this Replace Face feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this Replace Face feature."""
		self._instance.AccessSelections = value

	@property
	def get_faces_for_replacement_count(self):
		"""Gets the number of faces to replace in this feature."""
		return self._instance.GetFacesForReplacementCount

	@get_faces_for_replacement_count.setter
	def get_faces_for_replacement_count(self, value):
		"""Gets the number of faces to replace in this feature."""
		self._instance.GetFacesForReplacementCount = value

	@property
	def get_replacement_surfaces_count(self):
		"""Gets the number of replacement surfaces for this feature."""
		return self._instance.GetReplacementSurfacesCount

	@get_replacement_surfaces_count.setter
	def get_replacement_surfaces_count(self, value):
		"""Gets the number of replacement surfaces for this feature."""
		self._instance.GetReplacementSurfacesCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this Replace Face feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this Replace Face feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_faces_for_replacement(self):
		"""Gets the faces to replace in this feature."""
		return self._instance.IGetFacesForReplacement

	@i_get_faces_for_replacement.setter
	def i_get_faces_for_replacement(self, value):
		"""Gets the faces to replace in this feature."""
		self._instance.IGetFacesForReplacement = value

	@property
	def i_get_replacement_surfaces(self):
		"""Gets the replacement surfaces for this feature."""
		return self._instance.IGetReplacementSurfaces

	@i_get_replacement_surfaces.setter
	def i_get_replacement_surfaces(self, value):
		"""Gets the replacement surfaces for this feature."""
		self._instance.IGetReplacementSurfaces = value

	@property
	def i_set_faces_for_replacement(self):
		"""Sets the faces to replace for this feature."""
		return self._instance.ISetFacesForReplacement

	@i_set_faces_for_replacement.setter
	def i_set_faces_for_replacement(self, value):
		"""Sets the faces to replace for this feature."""
		self._instance.ISetFacesForReplacement = value

	@property
	def i_set_replacement_surfaces(self):
		"""Sets the replacement surfaces for this feature."""
		return self._instance.ISetReplacementSurfaces

	@i_set_replacement_surfaces.setter
	def i_set_replacement_surfaces(self, value):
		"""Sets the replacement surfaces for this feature."""
		self._instance.ISetReplacementSurfaces = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections in this feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections in this feature."""
		self._instance.ReleaseSelectionAccess = value

