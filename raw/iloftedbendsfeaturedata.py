# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftedBendsFeatureData_members.html
class ILoftedBendsFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bend_line_control_option(self):
		"""Gets or sets the lofted bend line control options."""
		return self._instance.BendLineControlOption

	@bend_line_control_option.setter
	def bend_line_control_option(self, value):
		"""Gets or sets the lofted bend line control options."""
		self._instance.BendLineControlOption = value

	@property
	def direction(self):
		"""Gets or sets the thickness direction of this lofted bends feature."""
		return self._instance.Direction

	@direction.setter
	def direction(self, value):
		"""Gets or sets the thickness direction of this lofted bends feature."""
		self._instance.Direction = value

	@property
	def faceting_option(self):
		"""Gets or sets how facets are created in this lofted bend feature."""
		return self._instance.FacetingOption

	@faceting_option.setter
	def faceting_option(self, value):
		"""Gets or sets how facets are created in this lofted bend feature."""
		self._instance.FacetingOption = value

	@property
	def facet_value(self):
		"""Gets or sets the value corresponding to ILoftedBendsFeatureData::FacetingOption."""
		return self._instance.FacetValue

	@facet_value.setter
	def facet_value(self, value):
		"""Gets or sets the value corresponding to ILoftedBendsFeatureData::FacetingOption."""
		self._instance.FacetValue = value

	@property
	def formed_method(self):
		"""Gets or sets whether this lofted bend feature is formed."""
		return self._instance.FormedMethod

	@formed_method.setter
	def formed_method(self, value):
		"""Gets or sets whether this lofted bend feature is formed."""
		self._instance.FormedMethod = value

	@property
	def maximum_deviation(self):
		"""Gets or sets the maximum deviation for the bend lines in a lofted bend feature."""
		return self._instance.MaximumDeviation

	@maximum_deviation.setter
	def maximum_deviation(self, value):
		"""Gets or sets the maximum deviation for the bend lines in a lofted bend feature."""
		self._instance.MaximumDeviation = value

	@property
	def number_of_bend_lines(self):
		"""Gets or sets the number of bend lines in this lofted bend feature."""
		return self._instance.NumberOfBendLines

	@number_of_bend_lines.setter
	def number_of_bend_lines(self, value):
		"""Gets or sets the number of bend lines in this lofted bend feature."""
		self._instance.NumberOfBendLines = value

	@property
	def profiles(self):
		"""Gets or sets the profiles for this lofted bends feature."""
		return self._instance.Profiles

	@profiles.setter
	def profiles(self, value):
		"""Gets or sets the profiles for this lofted bends feature."""
		self._instance.Profiles = value

	@property
	def refer_to_end_point(self):
		"""Gets or sets whether to calculate facet transitions using theoretical vertexes."""
		return self._instance.ReferToEndPoint

	@refer_to_end_point.setter
	def refer_to_end_point(self, value):
		"""Gets or sets whether to calculate facet transitions using theoretical vertexes."""
		self._instance.ReferToEndPoint = value

	@property
	def thickness(self):
		"""Gets or sets the thickness for this lofted bends feature."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or sets the thickness for this lofted bends feature."""
		self._instance.Thickness = value

	@property
	def access_selections(self):
		"""Accesses the selections used to define the lofted bends feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections used to define the lofted bends feature."""
		self._instance.AccessSelections = value

	@property
	def can_create_bend_lines(self):
		"""Gets whether the bend lines parameters affect this lofted bend feature."""
		return self._instance.CanCreateBendLines

	@can_create_bend_lines.setter
	def can_create_bend_lines(self, value):
		"""Gets whether the bend lines parameters affect this lofted bend feature."""
		self._instance.CanCreateBendLines = value

	@property
	def get_profile_count(self):
		"""Gets the number of profiles in this lofted bends feature."""
		return self._instance.GetProfileCount

	@get_profile_count.setter
	def get_profile_count(self, value):
		"""Gets the number of profiles in this lofted bends feature."""
		self._instance.GetProfileCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections used to define the lofted bends feature"""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections used to define the lofted bends feature"""
		self._instance.IAccessSelections = value

	@property
	def i_get_profiles(self):
		"""Gets the profiles for this lofted bends feature."""
		return self._instance.IGetProfiles

	@i_get_profiles.setter
	def i_get_profiles(self, value):
		"""Gets the profiles for this lofted bends feature."""
		self._instance.IGetProfiles = value

	@property
	def i_set_profiles(self):
		"""Sets the profiles for this lofted bends feature."""
		return self._instance.ISetProfiles

	@i_set_profiles.setter
	def i_set_profiles(self, value):
		"""Sets the profiles for this lofted bends feature."""
		self._instance.ISetProfiles = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this lofted bends feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this lofted bends feature."""
		self._instance.ReleaseSelectionAccess = value

