# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData_members.html
class IStructuralMemberFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def allow_protrusion(self):
		"""Gets or sets whether to allow protrusion."""
		return self._instance.AllowProtrusion

	@allow_protrusion.setter
	def allow_protrusion(self, value):
		"""Gets or sets whether to allow protrusion."""
		self._instance.AllowProtrusion = value

	@property
	def apply_corner_treatment(self):
		"""Gets or sets whether or not to apply a corner treatment to this structural member."""
		return self._instance.ApplyCornerTreatment

	@apply_corner_treatment.setter
	def apply_corner_treatment(self, value):
		"""Gets or sets whether or not to apply a corner treatment to this structural member."""
		self._instance.ApplyCornerTreatment = value

	@property
	def configuration_name(self):
		"""Gets or sets the name of the configuration in the custom weldment profile for this structural member."""
		return self._instance.ConfigurationName

	@configuration_name.setter
	def configuration_name(self, value):
		"""Gets or sets the name of the configuration in the custom weldment profile for this structural member."""
		self._instance.ConfigurationName = value

	@property
	def connected_segments_option(self):
		"""Gets or sets the connected segments option."""
		return self._instance.ConnectedSegmentsOption

	@connected_segments_option.setter
	def connected_segments_option(self, value):
		"""Gets or sets the connected segments option."""
		self._instance.ConnectedSegmentsOption = value

	@property
	def connection_type(self):
		"""Gets or sets the type of corner treatment at the specified connection point of this structural member."""
		return self._instance.ConnectionType

	@connection_type.setter
	def connection_type(self, value):
		"""Gets or sets the type of corner treatment at the specified connection point of this structural member."""
		self._instance.ConnectionType = value

	@property
	def corner_treatment_type(self):
		"""Gets or sets the type of corner treatment for this structural member."""
		return self._instance.CornerTreatmentType

	@corner_treatment_type.setter
	def corner_treatment_type(self, value):
		"""Gets or sets the type of corner treatment for this structural member."""
		self._instance.CornerTreatmentType = value

	@property
	def groups(self):
		"""Gets or sets the groups to use in this structural member."""
		return self._instance.Groups

	@groups.setter
	def groups(self, value):
		"""Gets or sets the groups to use in this structural member."""
		self._instance.Groups = value

	@property
	def library_profile_material(self):
		"""Gets the name of the material for the library profile for this structural member."""
		return self._instance.LibraryProfileMaterial

	@library_profile_material.setter
	def library_profile_material(self, value):
		"""Gets the name of the material for the library profile for this structural member."""
		self._instance.LibraryProfileMaterial = value

	@property
	def locate_profile_point(self):
		"""Gets or sets the point to use to locate the profile for this structural member."""
		return self._instance.LocateProfilePoint

	@locate_profile_point.setter
	def locate_profile_point(self, value):
		"""Gets or sets the point to use to locate the profile for this structural member."""
		self._instance.LocateProfilePoint = value

	@property
	def path_segments(self):
		"""Gets the path segments used or sets the path segments to use to create this structural member."""
		return self._instance.PathSegments

	@path_segments.setter
	def path_segments(self, value):
		"""Gets the path segments used or sets the path segments to use to create this structural member."""
		self._instance.PathSegments = value

	@property
	def rotation_angle(self):
		"""Gets or sets the angle by which the structural member turns relative to the adjacent structural member."""
		return self._instance.RotationAngle

	@rotation_angle.setter
	def rotation_angle(self, value):
		"""Gets or sets the angle by which the structural member turns relative to the adjacent structural member."""
		self._instance.RotationAngle = value

	@property
	def transfer_material(self):
		"""Gets or sets whether to transfer the material properties of a library profile for this structural member."""
		return self._instance.TransferMaterial

	@transfer_material.setter
	def transfer_material(self, value):
		"""Gets or sets whether to transfer the material properties of a library profile for this structural member."""
		self._instance.TransferMaterial = value

	@property
	def weldment_profile_path(self):
		"""Gets or sets the path for the profile for this structural member."""
		return self._instance.WeldmentProfilePath

	@weldment_profile_path.setter
	def weldment_profile_path(self, value):
		"""Gets or sets the path for the profile for this structural member."""
		self._instance.WeldmentProfilePath = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this structural member."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this structural member."""
		self._instance.AccessSelections = value

	@property
	def get_connection_points(self):
		"""Gets the connection points for this structural member."""
		return self._instance.GetConnectionPoints

	@get_connection_points.setter
	def get_connection_points(self, value):
		"""Gets the connection points for this structural member."""
		self._instance.GetConnectionPoints = value

	@property
	def get_connection_points_count(self):
		"""Gets the number of sketch points for this structural member."""
		return self._instance.GetConnectionPointsCount

	@get_connection_points_count.setter
	def get_connection_points_count(self, value):
		"""Gets the number of sketch points for this structural member."""
		self._instance.GetConnectionPointsCount = value

	@property
	def get_groups_count(self):
		"""Gets the number of structural-member groups for this structural member."""
		return self._instance.GetGroupsCount

	@get_groups_count.setter
	def get_groups_count(self, value):
		"""Gets the number of structural-member groups for this structural member."""
		self._instance.GetGroupsCount = value

	@property
	def get_path_segment_at(self):
		"""Gets the sketch segment associated with the body of this structural member."""
		return self._instance.GetPathSegmentAt

	@get_path_segment_at.setter
	def get_path_segment_at(self, value):
		"""Gets the sketch segment associated with the body of this structural member."""
		self._instance.GetPathSegmentAt = value

	@property
	def get_path_segments_count(self):
		"""Gets the number of path segments for this structural member."""
		return self._instance.GetPathSegmentsCount

	@get_path_segments_count.setter
	def get_path_segments_count(self, value):
		"""Gets the number of path segments for this structural member."""
		self._instance.GetPathSegmentsCount = value

	@property
	def get_sketch_segments(self):
		"""Gets the sketch segments that define the path of the specified structural member body."""
		return self._instance.GetSketchSegments

	@get_sketch_segments.setter
	def get_sketch_segments(self, value):
		"""Gets the sketch segments that define the path of the specified structural member body."""
		self._instance.GetSketchSegments = value

	@property
	def i_get_connection_points(self):
		"""Gets the connection points for this structural member."""
		return self._instance.IGetConnectionPoints

	@i_get_connection_points.setter
	def i_get_connection_points(self, value):
		"""Gets the connection points for this structural member."""
		self._instance.IGetConnectionPoints = value

	@property
	def i_get_groups(self):
		"""Gets the structural-member groups in this structural member."""
		return self._instance.IGetGroups

	@i_get_groups.setter
	def i_get_groups(self, value):
		"""Gets the structural-member groups in this structural member."""
		self._instance.IGetGroups = value

	@property
	def i_get_path_segments(self):
		"""Gets the path segments used to create this structural member."""
		return self._instance.IGetPathSegments

	@i_get_path_segments.setter
	def i_get_path_segments(self, value):
		"""Gets the path segments used to create this structural member."""
		self._instance.IGetPathSegments = value

	@property
	def i_set_groups(self):
		"""Sets the structural-member groups to use in this structural member."""
		return self._instance.ISetGroups

	@i_set_groups.setter
	def i_set_groups(self, value):
		"""Sets the structural-member groups to use in this structural member."""
		self._instance.ISetGroups = value

	@property
	def i_set_path_segments(self):
		"""Sets the path segments to use to create this structural member."""
		return self._instance.ISetPathSegments

	@i_set_path_segments.setter
	def i_set_path_segments(self, value):
		"""Sets the path segments to use to create this structural member."""
		self._instance.ISetPathSegments = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this structural member."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this structural member."""
		self._instance.ReleaseSelectionAccess = value

