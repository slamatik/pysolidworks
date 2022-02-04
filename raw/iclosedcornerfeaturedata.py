# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClosedCornerFeatureData_members.html
class IClosedCornerFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def corner_type(self):
		"""Gets or sets the closed corner type."""
		return self._instance.CornerType

	@corner_type.setter
	def corner_type(self, value):
		"""Gets or sets the closed corner type."""
		self._instance.CornerType = value

	@property
	def faces(self):
		"""Gets or sets the faces for this closed corner feature."""
		return self._instance.Faces

	@faces.setter
	def faces(self, value):
		"""Gets or sets the faces for this closed corner feature."""
		self._instance.Faces = value

	@property
	def gap_distance(self):
		"""Gets or sets the distance for the gap in a closed corner in a sheet metal part."""
		return self._instance.GapDistance

	@gap_distance.setter
	def gap_distance(self, value):
		"""Gets or sets the distance for the gap in a closed corner in a sheet metal part."""
		self._instance.GapDistance = value

	@property
	def open_bend_region(self):
		"""Gets or sets whether this closed corner has an open bend region."""
		return self._instance.OpenBendRegion

	@open_bend_region.setter
	def open_bend_region(self, value):
		"""Gets or sets whether this closed corner has an open bend region."""
		self._instance.OpenBendRegion = value

	@property
	def overlap_underlap_ratio(self):
		"""Gets or sets the overlap/underlap ratio for this closed corner."""
		return self._instance.OverlapUnderlapRatio

	@overlap_underlap_ratio.setter
	def overlap_underlap_ratio(self, value):
		"""Gets or sets the overlap/underlap ratio for this closed corner."""
		self._instance.OverlapUnderlapRatio = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this closed corner feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this closed corner feature."""
		self._instance.AccessSelections = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that describe this closed corner feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that describe this closed corner feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_faces(self):
		"""Gets the faces for this closed corner feature."""
		return self._instance.IGetFaces

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets the faces for this closed corner feature."""
		self._instance.IGetFaces = value

	@property
	def i_get_faces_count(self):
		"""Gets the number of faces in this closed corner feature."""
		return self._instance.IGetFacesCount

	@i_get_faces_count.setter
	def i_get_faces_count(self, value):
		"""Gets the number of faces in this closed corner feature."""
		self._instance.IGetFacesCount = value

	@property
	def i_set_faces(self):
		"""Sets the faces for this closed corner feature."""
		return self._instance.ISetFaces

	@i_set_faces.setter
	def i_set_faces(self, value):
		"""Sets the faces for this closed corner feature."""
		self._instance.ISetFaces = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe this closed corner feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe this closed corner feature."""
		self._instance.ReleaseSelectionAccess = value

