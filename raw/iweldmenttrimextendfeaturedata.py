# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentTrimExtendFeatureData_members.html
class IWeldmentTrimExtendFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bodies_to_be_trimmed(self):
		"""Gets or sets the bodies to trim."""
		return self._instance.BodiesToBeTrimmed

	@bodies_to_be_trimmed.setter
	def bodies_to_be_trimmed(self, value):
		"""Gets or sets the bodies to trim."""
		self._instance.BodiesToBeTrimmed = value

	@property
	def corner_type(self):
		"""Gets or sets the corner type."""
		return self._instance.CornerType

	@corner_type.setter
	def corner_type(self, value):
		"""Gets or sets the corner type."""
		self._instance.CornerType = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this weldment trim extend feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this weldment trim extend feature."""
		self._instance.AccessSelections = value

	@property
	def get_bodies_to_be_trimmed_count(self):
		"""Gets the number of bodies to trim."""
		return self._instance.GetBodiesToBeTrimmedCount

	@get_bodies_to_be_trimmed_count.setter
	def get_bodies_to_be_trimmed_count(self, value):
		"""Gets the number of bodies to trim."""
		self._instance.GetBodiesToBeTrimmedCount = value

	@property
	def get_trimming_boundary(self):
		"""Gets the entities used to define the trimming boundaries."""
		return self._instance.GetTrimmingBoundary

	@get_trimming_boundary.setter
	def get_trimming_boundary(self, value):
		"""Gets the entities used to define the trimming boundaries."""
		self._instance.GetTrimmingBoundary = value

	@property
	def get_trimming_boundary_count(self):
		"""Gets the number of trimming boundaries."""
		return self._instance.GetTrimmingBoundaryCount

	@get_trimming_boundary_count.setter
	def get_trimming_boundary_count(self, value):
		"""Gets the number of trimming boundaries."""
		self._instance.GetTrimmingBoundaryCount = value

	@property
	def i_get_bodies_to_be_trimmed(self):
		"""Gets the bodies to trim."""
		return self._instance.IGetBodiesToBeTrimmed

	@i_get_bodies_to_be_trimmed.setter
	def i_get_bodies_to_be_trimmed(self, value):
		"""Gets the bodies to trim."""
		self._instance.IGetBodiesToBeTrimmed = value

	@property
	def i_get_trimming_boundary(self):
		"""Gets the entities used to define the trimming boundaries."""
		return self._instance.IGetTrimmingBoundary

	@i_get_trimming_boundary.setter
	def i_get_trimming_boundary(self, value):
		"""Gets the entities used to define the trimming boundaries."""
		self._instance.IGetTrimmingBoundary = value

	@property
	def i_set_bodies_to_be_trimmed(self):
		"""Sets the bodies to trim."""
		return self._instance.ISetBodiesToBeTrimmed

	@i_set_bodies_to_be_trimmed.setter
	def i_set_bodies_to_be_trimmed(self, value):
		"""Sets the bodies to trim."""
		self._instance.ISetBodiesToBeTrimmed = value

	@property
	def i_set_trimming_boundary(self):
		"""Gets the entities used to define the trimming boundaries."""
		return self._instance.ISetTrimmingBoundary

	@i_set_trimming_boundary.setter
	def i_set_trimming_boundary(self, value):
		"""Gets the entities used to define the trimming boundaries."""
		self._instance.ISetTrimmingBoundary = value

	@property
	def release_selection_access(self):
		"""Releases the selections that define this weldment trim extend feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases the selections that define this weldment trim extend feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_trimming_boundary(self):
		"""Sets the trimming boundaries for this weldment trim extend feature."""
		return self._instance.SetTrimmingBoundary

	@set_trimming_boundary.setter
	def set_trimming_boundary(self, value):
		"""Sets the trimming boundaries for this weldment trim extend feature."""
		self._instance.SetTrimmingBoundary = value

