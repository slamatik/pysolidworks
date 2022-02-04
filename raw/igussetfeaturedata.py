# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData_members.html
class IGussetFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def flip_offset_direction(self):
		"""Gets or sets whether the offset direction is flipped for this gusset feature."""
		return self._instance.FlipOffsetDirection

	@flip_offset_direction.setter
	def flip_offset_direction(self, value):
		"""Gets or sets whether the offset direction is flipped for this gusset feature."""
		self._instance.FlipOffsetDirection = value

	@property
	def flip_profile_distance_parameters(self):
		"""Gets or sets whether the Profile Distance 1 and Profile Distance 2 parameters are flipped for this gusset feature."""
		return self._instance.FlipProfileDistanceParameters

	@flip_profile_distance_parameters.setter
	def flip_profile_distance_parameters(self, value):
		"""Gets or sets whether the Profile Distance 1 and Profile Distance 2 parameters are flipped for this gusset feature."""
		self._instance.FlipProfileDistanceParameters = value

	@property
	def offset_used(self):
		"""Gets or sets whether offset is used to locate the profile for this gusset feature."""
		return self._instance.OffsetUsed

	@offset_used.setter
	def offset_used(self, value):
		"""Gets or sets whether offset is used to locate the profile for this gusset feature."""
		self._instance.OffsetUsed = value

	@property
	def profile_angle(self):
		"""Gets or sets the profile angle for this gusset feature."""
		return self._instance.ProfileAngle

	@profile_angle.setter
	def profile_angle(self, value):
		"""Gets or sets the profile angle for this gusset feature."""
		self._instance.ProfileAngle = value

	@property
	def profile_distance(self):
		"""Gets or sets the distance for the Profile Distance 1 parameter for this gusset feature."""
		return self._instance.ProfileDistance1

	@profile_distance.setter
	def profile_distance(self, value):
		"""Gets or sets the distance for the Profile Distance 1 parameter for this gusset feature."""
		self._instance.ProfileDistance1 = value

	@property
	def profile_distance(self):
		"""Gets or sets the distance for the Profile Distance 2 parameter for this gusset feature."""
		return self._instance.ProfileDistance2

	@profile_distance.setter
	def profile_distance(self, value):
		"""Gets or sets the distance for the Profile Distance 2 parameter for this gusset feature."""
		self._instance.ProfileDistance2 = value

	@property
	def profile_distance(self):
		"""Gets or sets the distance for the Profile Distance 3 parameter for this gusset feature."""
		return self._instance.ProfileDistance3

	@profile_distance.setter
	def profile_distance(self, value):
		"""Gets or sets the distance for the Profile Distance 3 parameter for this gusset feature."""
		self._instance.ProfileDistance3 = value

	@property
	def profile_distance(self):
		"""Gets or sets the distance for the Profile Distance 4 parameter for this gusset feature."""
		return self._instance.ProfileDistance4

	@profile_distance.setter
	def profile_distance(self, value):
		"""Gets or sets the distance for the Profile Distance 4 parameter for this gusset feature."""
		self._instance.ProfileDistance4 = value

	@property
	def profile_location(self):
		"""Gets or sets where to locate the profile for this gusset feature."""
		return self._instance.ProfileLocation

	@profile_location.setter
	def profile_location(self, value):
		"""Gets or sets where to locate the profile for this gusset feature."""
		self._instance.ProfileLocation = value

	@property
	def profile_offset_distance(self):
		"""Gets or sets the offset distance of the profile for this gusset feature."""
		return self._instance.ProfileOffsetDistance

	@profile_offset_distance.setter
	def profile_offset_distance(self, value):
		"""Gets or sets the offset distance of the profile for this gusset feature."""
		self._instance.ProfileOffsetDistance = value

	@property
	def profile_type(self):
		"""Gets or sets the type of profile for this gusset feature."""
		return self._instance.ProfileType

	@profile_type.setter
	def profile_type(self, value):
		"""Gets or sets the type of profile for this gusset feature."""
		self._instance.ProfileType = value

	@property
	def thickness(self):
		"""Gets or sets the thickness for this gusset feature."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or sets the thickness for this gusset feature."""
		self._instance.Thickness = value

	@property
	def thickness_type(self):
		"""Gets or sets the type of thickness for this gusset feature."""
		return self._instance.ThicknessType

	@thickness_type.setter
	def thickness_type(self, value):
		"""Gets or sets the type of thickness for this gusset feature."""
		self._instance.ThicknessType = value

	@property
	def use_angle(self):
		"""Gets or sets whether an angle is used for specifying the dimensions of the polygonal profile for this gusset feature."""
		return self._instance.UseAngle

	@use_angle.setter
	def use_angle(self, value):
		"""Gets or sets whether an angle is used for specifying the dimensions of the polygonal profile for this gusset feature."""
		self._instance.UseAngle = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this gusset feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this gusset feature."""
		self._instance.AccessSelections = value

	@property
	def get_supporting_faces(self):
		"""Gets the two, adjacent, supporting faces for this gusset feature."""
		return self._instance.GetSupportingFaces

	@get_supporting_faces.setter
	def get_supporting_faces(self, value):
		"""Gets the two, adjacent, supporting faces for this gusset feature."""
		self._instance.GetSupportingFaces = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this gusset feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this gusset feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_supporting_faces(self):
		"""Sets the two, adjacent, supporting faces for this gusset feature."""
		return self._instance.SetSupportingFaces

	@set_supporting_faces.setter
	def set_supporting_faces(self, value):
		"""Sets the two, adjacent, supporting faces for this gusset feature."""
		self._instance.SetSupportingFaces = value

