# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassPropertyOverrideOptions_members.html
class IMassPropertyOverrideOptions:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def override_center_of_mass(self):
		"""Gets or sets whether to override the calculated center of mass for the model currently being edited."""
		return self._instance.OverrideCenterOfMass

	@override_center_of_mass.setter
	def override_center_of_mass(self, value):
		"""Gets or sets whether to override the calculated center of mass for the model currently being edited."""
		self._instance.OverrideCenterOfMass = value

	@property
	def override_mass(self):
		"""Gets or sets whether to override the calculated mass value for the model currently being edited."""
		return self._instance.OverrideMass

	@override_mass.setter
	def override_mass(self, value):
		"""Gets or sets whether to override the calculated mass value for the model currently being edited."""
		self._instance.OverrideMass = value

	@property
	def override_moments_of_inertia(self):
		"""Gets or sets whether to override the calculated moments of inertia for the model currently being edited."""
		return self._instance.OverrideMomentsOfInertia

	@override_moments_of_inertia.setter
	def override_moments_of_inertia(self, value):
		"""Gets or sets whether to override the calculated moments of inertia for the model currently being edited."""
		self._instance.OverrideMomentsOfInertia = value

	@property
	def get_override_center_of_mass_value(self):
		"""Gets the override center of mass."""
		return self._instance.GetOverrideCenterOfMassValue

	@get_override_center_of_mass_value.setter
	def get_override_center_of_mass_value(self, value):
		"""Gets the override center of mass."""
		self._instance.GetOverrideCenterOfMassValue = value

	@property
	def get_override_mass_value(self):
		"""Gets the override mass."""
		return self._instance.GetOverrideMassValue

	@get_override_mass_value.setter
	def get_override_mass_value(self, value):
		"""Gets the override mass."""
		self._instance.GetOverrideMassValue = value

	@property
	def get_override_moments_of_inertia_value(self):
		"""Gets the override moments of inertia."""
		return self._instance.GetOverrideMomentsOfInertiaValue

	@get_override_moments_of_inertia_value.setter
	def get_override_moments_of_inertia_value(self, value):
		"""Gets the override moments of inertia."""
		self._instance.GetOverrideMomentsOfInertiaValue = value

	@property
	def get_override_principal_axes_orientation(self):
		"""Gets the override principal axis of inertia."""
		return self._instance.GetOverridePrincipalAxesOrientation

	@get_override_principal_axes_orientation.setter
	def get_override_principal_axes_orientation(self, value):
		"""Gets the override principal axis of inertia."""
		self._instance.GetOverridePrincipalAxesOrientation = value

	@property
	def get_override_principal_moments_of_inertia(self):
		"""Gets the override principal moments of inertia."""
		return self._instance.GetOverridePrincipalMomentsOfInertia

	@get_override_principal_moments_of_inertia.setter
	def get_override_principal_moments_of_inertia(self, value):
		"""Gets the override principal moments of inertia."""
		self._instance.GetOverridePrincipalMomentsOfInertia = value

	@property
	def set_override_center_of_mass_value(self):
		"""Overrides the calculated center of mass of the model currently being edited."""
		return self._instance.SetOverrideCenterOfMassValue

	@set_override_center_of_mass_value.setter
	def set_override_center_of_mass_value(self, value):
		"""Overrides the calculated center of mass of the model currently being edited."""
		self._instance.SetOverrideCenterOfMassValue = value

	@property
	def set_override_mass_value(self):
		"""Overrides the calculated mass of the model currently being edited."""
		return self._instance.SetOverrideMassValue

	@set_override_mass_value.setter
	def set_override_mass_value(self, value):
		"""Overrides the calculated mass of the model currently being edited."""
		self._instance.SetOverrideMassValue = value

	@property
	def set_override_moments_of_inertia_value(self):
		"""Overrides the calculated moments of inertia of the model currently being edited."""
		return self._instance.SetOverrideMomentsOfInertiaValue

	@set_override_moments_of_inertia_value.setter
	def set_override_moments_of_inertia_value(self, value):
		"""Overrides the calculated moments of inertia of the model currently being edited."""
		self._instance.SetOverrideMomentsOfInertiaValue = value

	@property
	def set_override_principal_axes_orientation(self):
		"""Overrides the orientation of the specified principal axis of inertia of the model currently being edited."""
		return self._instance.SetOverridePrincipalAxesOrientation

	@set_override_principal_axes_orientation.setter
	def set_override_principal_axes_orientation(self, value):
		"""Overrides the orientation of the specified principal axis of inertia of the model currently being edited."""
		self._instance.SetOverridePrincipalAxesOrientation = value

	@property
	def set_override_principal_moments_of_inertia(self):
		"""Overrides the calculated principal moments of inertia of the model currently being edited."""
		return self._instance.SetOverridePrincipalMomentsOfInertia

	@set_override_principal_moments_of_inertia.setter
	def set_override_principal_moments_of_inertia(self, value):
		"""Overrides the calculated principal moments of inertia of the model currently being edited."""
		self._instance.SetOverridePrincipalMomentsOfInertia = value

