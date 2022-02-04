# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICavityFeatureData_members.html
class ICavityFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def components(self):
		"""Gets or sets the design components for this cavity."""
		return self._instance.Components

	@components.setter
	def components(self, value):
		"""Gets or sets the design components for this cavity."""
		self._instance.Components = value

	@property
	def scale_type(self):
		"""Gets or sets the point about which scaling occurs in this cavity feature."""
		return self._instance.ScaleType

	@scale_type.setter
	def scale_type(self, value):
		"""Gets or sets the point about which scaling occurs in this cavity feature."""
		self._instance.ScaleType = value

	@property
	def uniform_scale(self):
		"""Gets or sets the value by which to scale this cavity feature in all directions."""
		return self._instance.UniformScale

	@uniform_scale.setter
	def uniform_scale(self, value):
		"""Gets or sets the value by which to scale this cavity feature in all directions."""
		self._instance.UniformScale = value

	@property
	def use_uniform_scale(self):
		"""Gets or sets whether to uniformly scale this cavity feature."""
		return self._instance.UseUniformScale

	@use_uniform_scale.setter
	def use_uniform_scale(self, value):
		"""Gets or sets whether to uniformly scale this cavity feature."""
		self._instance.UseUniformScale = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this cavity feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this cavity feature."""
		self._instance.AccessSelections = value

	@property
	def get_components_count(self):
		"""Gets the number of design components in this cavity feature."""
		return self._instance.GetComponentsCount

	@get_components_count.setter
	def get_components_count(self, value):
		"""Gets the number of design components in this cavity feature."""
		self._instance.GetComponentsCount = value

	@property
	def get_scale(self):
		"""Gets the values used to scale this cavity feature."""
		return self._instance.GetScale

	@get_scale.setter
	def get_scale(self, value):
		"""Gets the values used to scale this cavity feature."""
		self._instance.GetScale = value

	@property
	def i_get_components(self):
		"""Gets the design components for this cavity feature."""
		return self._instance.IGetComponents

	@i_get_components.setter
	def i_get_components(self, value):
		"""Gets the design components for this cavity feature."""
		self._instance.IGetComponents = value

	@property
	def i_set_components(self):
		"""Sets the design components for this cavity feature."""
		return self._instance.ISetComponents

	@i_set_components.setter
	def i_set_components(self, value):
		"""Sets the design components for this cavity feature."""
		self._instance.ISetComponents = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this cavity feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this cavity feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_scale(self):
		"""Sets the values by which to scale this cavity feature."""
		return self._instance.SetScale

	@set_scale.setter
	def set_scale(self, value):
		"""Sets the values by which to scale this cavity feature."""
		self._instance.SetScale = value

