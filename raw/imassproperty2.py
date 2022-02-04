# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty2_members.html
class IMassProperty2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def accuracy_level(self):
		"""Gets or sets the accuracy level used to calculate mass properties."""
		return self._instance.AccuracyLevel

	@accuracy_level.setter
	def accuracy_level(self, value):
		"""Gets or sets the accuracy level used to calculate mass properties."""
		self._instance.AccuracyLevel = value

	@property
	def center_of_mass(self):
		"""Gets the center of mass of selected components/bodies."""
		return self._instance.CenterOfMass

	@center_of_mass.setter
	def center_of_mass(self, value):
		"""Gets the center of mass of selected components/bodies."""
		self._instance.CenterOfMass = value

	@property
	def density(self):
		"""Gets the density of selected components/bodies."""
		return self._instance.Density

	@density.setter
	def density(self, value):
		"""Gets the density of selected components/bodies."""
		self._instance.Density = value

	@property
	def include_hidden_bodies_or_components(self):
		"""Gets or sets whether to include the mass properties of hidden bodies/components."""
		return self._instance.IncludeHiddenBodiesOrComponents

	@include_hidden_bodies_or_components.setter
	def include_hidden_bodies_or_components(self, value):
		"""Gets or sets whether to include the mass properties of hidden bodies/components."""
		self._instance.IncludeHiddenBodiesOrComponents = value

	@property
	def mass(self):
		"""Gets the mass of selected components/bodies."""
		return self._instance.Mass

	@mass.setter
	def mass(self, value):
		"""Gets the mass of selected components/bodies."""
		self._instance.Mass = value

	@property
	def principal_axes_of_inertia(self):
		"""Gets the principal axis of inertia for the specified axis."""
		return self._instance.PrincipalAxesOfInertia

	@principal_axes_of_inertia.setter
	def principal_axes_of_inertia(self, value):
		"""Gets the principal axis of inertia for the specified axis."""
		self._instance.PrincipalAxesOfInertia = value

	@property
	def principal_moments_of_inertia(self):
		"""Gets the principal moments of inertia."""
		return self._instance.PrincipalMomentsOfInertia

	@principal_moments_of_inertia.setter
	def principal_moments_of_inertia(self, value):
		"""Gets the principal moments of inertia."""
		self._instance.PrincipalMomentsOfInertia = value

	@property
	def selected_items(self):
		"""Gets or sets the list of bodies/components for which to calculate mass properties."""
		return self._instance.SelectedItems

	@selected_items.setter
	def selected_items(self, value):
		"""Gets or sets the list of bodies/components for which to calculate mass properties."""
		self._instance.SelectedItems = value

	@property
	def show_weld_bead_mass(self):
		"""Gets or sets whether to calculate weld bead mass."""
		return self._instance.ShowWeldBeadMass

	@show_weld_bead_mass.setter
	def show_weld_bead_mass(self, value):
		"""Gets or sets whether to calculate weld bead mass."""
		self._instance.ShowWeldBeadMass = value

	@property
	def surface_area(self):
		"""Gets the surface area of selected components/bodies."""
		return self._instance.SurfaceArea

	@surface_area.setter
	def surface_area(self, value):
		"""Gets the surface area of selected components/bodies."""
		self._instance.SurfaceArea = value

	@property
	def use_system_units(self):
		"""Gets or sets whether to use system units or document units when calculating mass properties."""
		return self._instance.UseSystemUnits

	@use_system_units.setter
	def use_system_units(self, value):
		"""Gets or sets whether to use system units or document units when calculating mass properties."""
		self._instance.UseSystemUnits = value

	@property
	def volume(self):
		"""Gets the volume of selected components/bodies."""
		return self._instance.Volume

	@volume.setter
	def volume(self, value):
		"""Gets the volume of selected components/bodies."""
		self._instance.Volume = value

	@property
	def weld_bead_mass(self):
		"""Gets the weld bead mass."""
		return self._instance.WeldBeadMass

	@weld_bead_mass.setter
	def weld_bead_mass(self, value):
		"""Gets the weld bead mass."""
		self._instance.WeldBeadMass = value

	@property
	def get_moment_of_inertia(self):
		"""Gets the moment of inertia at the specified coordinate system for the selected bodies/components."""
		return self._instance.GetMomentOfInertia

	@get_moment_of_inertia.setter
	def get_moment_of_inertia(self, value):
		"""Gets the moment of inertia at the specified coordinate system for the selected bodies/components."""
		self._instance.GetMomentOfInertia = value

	@property
	def get_override_options(self):
		"""Gets the mass property override options for the selected bodies/components."""
		return self._instance.GetOverrideOptions

	@get_override_options.setter
	def get_override_options(self, value):
		"""Gets the mass property override options for the selected bodies/components."""
		self._instance.GetOverrideOptions = value

	@property
	def recalculate(self):
		"""Recalculates the mass properties of the selectied bodies/components."""
		return self._instance.Recalculate

	@recalculate.setter
	def recalculate(self, value):
		"""Recalculates the mass properties of the selectied bodies/components."""
		self._instance.Recalculate = value

	@property
	def set_coordinate_system(self):
		"""Sets the coordinate system to use when calculating mass properties for this model."""
		return self._instance.SetCoordinateSystem

	@set_coordinate_system.setter
	def set_coordinate_system(self, value):
		"""Sets the coordinate system to use when calculating mass properties for this model."""
		self._instance.SetCoordinateSystem = value

	@property
	def set_override_options(self):
		"""Sets the mass property override options for the selected bodies/components."""
		return self._instance.SetOverrideOptions

	@set_override_options.setter
	def set_override_options(self, value):
		"""Sets the mass property override options for the selected bodies/components."""
		self._instance.SetOverrideOptions = value

