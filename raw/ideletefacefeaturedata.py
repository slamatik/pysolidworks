# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData_members.html
class IDeleteFaceFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def options(self):
		"""Gets or sets the option for the DeleteFace feature."""
		return self._instance.Options

	@options.setter
	def options(self, value):
		"""Gets or sets the option for the DeleteFace feature."""
		self._instance.Options = value

	@property
	def access_selections(self):
		"""Allows access to the selections that describe the DeleteFace feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Allows access to the selections that describe the DeleteFace feature."""
		self._instance.AccessSelections = value

	@property
	def get_deleted_faces(self):
		"""Get the faces of the DeleteFace feature."""
		return self._instance.GetDeletedFaces

	@get_deleted_faces.setter
	def get_deleted_faces(self, value):
		"""Get the faces of the DeleteFace feature."""
		self._instance.GetDeletedFaces = value

	@property
	def get_deleted_faces_count(self):
		"""Gets the number of faces in the DeleteFace feature."""
		return self._instance.GetDeletedFacesCount

	@get_deleted_faces_count.setter
	def get_deleted_faces_count(self, value):
		"""Gets the number of faces in the DeleteFace feature."""
		self._instance.GetDeletedFacesCount = value

	@property
	def i_access_selections(self):
		"""Allows access to the selections that describe the DeleteFace feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Allows access to the selections that describe the DeleteFace feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_deleted_faces(self):
		"""Get the faces of the DeleteFace feature."""
		return self._instance.IGetDeletedFaces

	@i_get_deleted_faces.setter
	def i_get_deleted_faces(self, value):
		"""Get the faces of the DeleteFace feature."""
		self._instance.IGetDeletedFaces = value

	@property
	def i_set_deleted_faces(self):
		"""Sets the faces for the DeleteFace feature."""
		return self._instance.ISetDeletedFaces

	@i_set_deleted_faces.setter
	def i_set_deleted_faces(self, value):
		"""Sets the faces for the DeleteFace feature."""
		self._instance.ISetDeletedFaces = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe the DeleteFace feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe the DeleteFace feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_deleted_faces(self):
		"""Sets the faces for the DeleteFace feature."""
		return self._instance.SetDeletedFaces

	@set_deleted_faces.setter
	def set_deleted_faces(self, value):
		"""Sets the faces for the DeleteFace feature."""
		self._instance.SetDeletedFaces = value

