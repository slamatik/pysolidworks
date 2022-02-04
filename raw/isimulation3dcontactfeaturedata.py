# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulation3DContactFeatureData_members.html
class ISimulation3DContactFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def contact_components(self):
		"""Gets or sets the components to check for contact in a 3D Contact feature."""
		return self._instance.ContactComponents

	@contact_components.setter
	def contact_components(self, value):
		"""Gets or sets the components to check for contact in a 3D Contact feature."""
		self._instance.ContactComponents = value

	@property
	def dynamic_friction_coefficient(self):
		"""Gets or sets the dynamic friction coefficient in a 3D Contact feature."""
		return self._instance.DynamicFrictionCoefficient

	@dynamic_friction_coefficient.setter
	def dynamic_friction_coefficient(self, value):
		"""Gets or sets the dynamic friction coefficient in a 3D Contact feature."""
		self._instance.DynamicFrictionCoefficient = value

	@property
	def dynamic_friction_velocity(self):
		"""Gets or sets the dynamic friction velocity in a 3D Contact feature."""
		return self._instance.DynamicFrictionVelocity

	@dynamic_friction_velocity.setter
	def dynamic_friction_velocity(self, value):
		"""Gets or sets the dynamic friction velocity in a 3D Contact feature."""
		self._instance.DynamicFrictionVelocity = value

	@property
	def exponent(self):
		"""Gets or sets the exponent used to calculate the exponential force in a 3D Contact feature."""
		return self._instance.Exponent

	@exponent.setter
	def exponent(self, value):
		"""Gets or sets the exponent used to calculate the exponential force in a 3D Contact feature."""
		self._instance.Exponent = value

	@property
	def friction_option(self):
		"""Gets or sets whether contact friction is off, full (static), or dynamic in a 3D Contact feature."""
		return self._instance.FrictionOption

	@friction_option.setter
	def friction_option(self, value):
		"""Gets or sets whether contact friction is off, full (static), or dynamic in a 3D Contact feature."""
		self._instance.FrictionOption = value

	@property
	def material_i_d(self):
		"""Gets or sets the type of material the specified component in this 3D Contact feature."""
		return self._instance.MaterialID

	@material_i_d.setter
	def material_i_d(self, value):
		"""Gets or sets the type of material the specified component in this 3D Contact feature."""
		self._instance.MaterialID = value

	@property
	def max_damping(self):
		"""Gets or sets the maximum damping coefficient of the boundary of interaction in a 3D Contact feature."""
		return self._instance.MaxDamping

	@max_damping.setter
	def max_damping(self, value):
		"""Gets or sets the maximum damping coefficient of the boundary of interaction in a 3D Contact feature."""
		self._instance.MaxDamping = value

	@property
	def penetration(self):
		"""Gets or sets the interaction boundary penetration at which the maximum damping value is applied when calculating the impact force in a 3D Contact feature."""
		return self._instance.Penetration

	@penetration.setter
	def penetration(self, value):
		"""Gets or sets the interaction boundary penetration at which the maximum damping value is applied when calculating the impact force in a 3D Contact feature."""
		self._instance.Penetration = value

	@property
	def restitution_coefficient(self):
		"""Gets or sets the coefficient of restitution in a 3D Contact feature."""
		return self._instance.RestitutionCoefficient

	@restitution_coefficient.setter
	def restitution_coefficient(self, value):
		"""Gets or sets the coefficient of restitution in a 3D Contact feature."""
		self._instance.RestitutionCoefficient = value

	@property
	def specify_material(self):
		"""Gets or sets whether to use materials in a 3D Contact feature."""
		return self._instance.SpecifyMaterial

	@specify_material.setter
	def specify_material(self, value):
		"""Gets or sets whether to use materials in a 3D Contact feature."""
		self._instance.SpecifyMaterial = value

	@property
	def static_friction_coefficient(self):
		"""Gets or sets the static friction coefficent in a 3D Contact feature."""
		return self._instance.StaticFrictionCoefficient

	@static_friction_coefficient.setter
	def static_friction_coefficient(self, value):
		"""Gets or sets the static friction coefficent in a 3D Contact feature."""
		self._instance.StaticFrictionCoefficient = value

	@property
	def static_friction_velocity(self):
		"""Gets or sets the static friction velocity in a 3D Contact feature."""
		return self._instance.StaticFrictionVelocity

	@static_friction_velocity.setter
	def static_friction_velocity(self, value):
		"""Gets or sets the static friction velocity in a 3D Contact feature."""
		self._instance.StaticFrictionVelocity = value

	@property
	def stiffness(self):
		"""Gets or sets the stiffness at the boundary of interaction between the two parts in a 3D Contact feature."""
		return self._instance.Stiffness

	@stiffness.setter
	def stiffness(self, value):
		"""Gets or sets the stiffness at the boundary of interaction between the two parts in a 3D Contact feature."""
		self._instance.Stiffness = value

	@property
	def use_restitution_coefficient(self):
		"""Gets or sets whether to use the restitution coefficient instead of impact force in a 3D Contact feature."""
		return self._instance.UseRestitutionCoefficient

	@use_restitution_coefficient.setter
	def use_restitution_coefficient(self, value):
		"""Gets or sets whether to use the restitution coefficient instead of impact force in a 3D Contact feature."""
		self._instance.UseRestitutionCoefficient = value

