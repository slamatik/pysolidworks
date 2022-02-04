# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData_members.html
class IAdvancedHoleFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def customize_callout(self):
		"""Gets or sets whether to customize the hole callouts of the elements of this Advanced Hole."""
		return self._instance.CustomizeCallout

	@customize_callout.setter
	def customize_callout(self, value):
		"""Gets or sets whether to customize the hole callouts of the elements of this Advanced Hole."""
		self._instance.CustomizeCallout = value

	@property
	def far_side_elements_count(self):
		"""Gets the number of far side hole elements in this Advanced Hole."""
		return self._instance.FarSideElementsCount

	@far_side_elements_count.setter
	def far_side_elements_count(self, value):
		"""Gets the number of far side hole elements in this Advanced Hole."""
		self._instance.FarSideElementsCount = value

	@property
	def near_side_elements_count(self):
		"""Gets the number of near side hole elements in this Advanced Hole."""
		return self._instance.NearSideElementsCount

	@near_side_elements_count.setter
	def near_side_elements_count(self, value):
		"""Gets the number of near side hole elements in this Advanced Hole."""
		self._instance.NearSideElementsCount = value

	@property
	def use_baseline_dimensions(self):
		"""Gets or sets whether to use baseline dimensions in this Advanced Hole."""
		return self._instance.UseBaselineDimensions

	@use_baseline_dimensions.setter
	def use_baseline_dimensions(self, value):
		"""Gets or sets whether to use baseline dimensions in this Advanced Hole."""
		self._instance.UseBaselineDimensions = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define the Advanced Hole feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define the Advanced Hole feature."""
		self._instance.AccessSelections = value

	@property
	def get_far_side_elements(self):
		"""Gets the far side hole elements in this Advanced Hole."""
		return self._instance.GetFarSideElements

	@get_far_side_elements.setter
	def get_far_side_elements(self, value):
		"""Gets the far side hole elements in this Advanced Hole."""
		self._instance.GetFarSideElements = value

	@property
	def get_near_side_elements(self):
		"""Gets the near side hole elements in this Advanced Hole."""
		return self._instance.GetNearSideElements

	@get_near_side_elements.setter
	def get_near_side_elements(self, value):
		"""Gets the near side hole elements in this Advanced Hole."""
		self._instance.GetNearSideElements = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the Hole Wizard feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the Hole Wizard feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_far_side_elements(self):
		"""Sets the far side hole elements in this Advanced Hole."""
		return self._instance.SetFarSideElements

	@set_far_side_elements.setter
	def set_far_side_elements(self, value):
		"""Sets the far side hole elements in this Advanced Hole."""
		self._instance.SetFarSideElements = value

	@property
	def set_near_side_elements(self):
		"""Sets the near side hole elements in this Advanced Hole."""
		return self._instance.SetNearSideElements

	@set_near_side_elements.setter
	def set_near_side_elements(self, value):
		"""Sets the near side hole elements in this Advanced Hole."""
		self._instance.SetNearSideElements = value

