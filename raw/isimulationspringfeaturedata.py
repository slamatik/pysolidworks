# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationSpringFeatureData_members.html
class ISimulationSpringFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def base_component(self):
		"""Gets or sets the base component for this simulation spring feature."""
		return self._instance.BaseComponent

	@base_component.setter
	def base_component(self, value):
		"""Gets or sets the base component for this simulation spring feature."""
		self._instance.BaseComponent = value

	@property
	def coil_diameter(self):
		"""Gets or sets the diameter of the coil for this simulation spring feature."""
		return self._instance.CoilDiameter

	@coil_diameter.setter
	def coil_diameter(self, value):
		"""Gets or sets the diameter of the coil for this simulation spring feature."""
		self._instance.CoilDiameter = value

	@property
	def damping_constant(self):
		"""Gets or sets the damping constant for this simulation spring feature."""
		return self._instance.DampingConstant

	@damping_constant.setter
	def damping_constant(self, value):
		"""Gets or sets the damping constant for this simulation spring feature."""
		self._instance.DampingConstant = value

	@property
	def exponent_of_damper_force_expression(self):
		"""Gets or sets the exponent of the damper force expression for this simulation spring feature."""
		return self._instance.ExponentOfDamperForceExpression

	@exponent_of_damper_force_expression.setter
	def exponent_of_damper_force_expression(self, value):
		"""Gets or sets the exponent of the damper force expression for this simulation spring feature."""
		self._instance.ExponentOfDamperForceExpression = value

	@property
	def exponent_of_spring_force_expression(self):
		"""Gets or sets the exponent of the spring force expression for this simulation spring feature."""
		return self._instance.ExponentOfSpringForceExpression

	@exponent_of_spring_force_expression.setter
	def exponent_of_spring_force_expression(self, value):
		"""Gets or sets the exponent of the spring force expression for this simulation spring feature."""
		self._instance.ExponentOfSpringForceExpression = value

	@property
	def free_angle(self):
		"""Gets or sets the free angle for the functional expression for this simulation spring feature."""
		return self._instance.FreeAngle

	@free_angle.setter
	def free_angle(self, value):
		"""Gets or sets the free angle for the functional expression for this simulation spring feature."""
		self._instance.FreeAngle = value

	@property
	def free_length(self):
		"""Gets or sets the free length (i.e., length to stretch or compress the spring) for the functional expression for this simulation spring feature."""
		return self._instance.FreeLength

	@free_length.setter
	def free_length(self, value):
		"""Gets or sets the free length (i.e., length to stretch or compress the spring) for the functional expression for this simulation spring feature."""
		self._instance.FreeLength = value

	@property
	def has_damper(self):
		"""Gets or sets whether this simulation spring feature has damper."""
		return self._instance.HasDamper

	@has_damper.setter
	def has_damper(self, value):
		"""Gets or sets whether this simulation spring feature has damper."""
		self._instance.HasDamper = value

	@property
	def load_references(self):
		"""Gets or sets the load references for this simulation spring feature."""
		return self._instance.LoadReferences

	@load_references.setter
	def load_references(self, value):
		"""Gets or sets the load references for this simulation spring feature."""
		self._instance.LoadReferences = value

	@property
	def number_of_coils(self):
		"""Gets or sets the number of coils in this simulation spring feature."""
		return self._instance.NumberOfCoils

	@number_of_coils.setter
	def number_of_coils(self, value):
		"""Gets or sets the number of coils in this simulation spring feature."""
		self._instance.NumberOfCoils = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of this simulation spring feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of this simulation spring feature."""
		self._instance.ReverseDirection = value

	@property
	def spring_constant(self):
		"""Gets or sets the strength of this simulation spring feature."""
		return self._instance.SpringConstant

	@spring_constant.setter
	def spring_constant(self, value):
		"""Gets or sets the strength of this simulation spring feature."""
		self._instance.SpringConstant = value

	@property
	def type(self):
		"""Gets or sets the type of simulation spring feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of simulation spring feature."""
		self._instance.Type = value

	@property
	def update_to_model_changes(self):
		"""Gets or sets whether to have the free length dynamically update model changes while the PropertyManager page is open."""
		return self._instance.UpdateToModelChanges

	@update_to_model_changes.setter
	def update_to_model_changes(self, value):
		"""Gets or sets whether to have the free length dynamically update model changes while the PropertyManager page is open."""
		self._instance.UpdateToModelChanges = value

	@property
	def wire_diameter(self):
		"""Gets or sets the diameter of the wire for this simulation spring feature."""
		return self._instance.WireDiameter

	@wire_diameter.setter
	def wire_diameter(self, value):
		"""Gets or sets the diameter of the wire for this simulation spring feature."""
		self._instance.WireDiameter = value

	@property
	def get_end_points(self):
		"""Gets the end points for this simulation spring feature."""
		return self._instance.GetEndPoints

	@get_end_points.setter
	def get_end_points(self, value):
		"""Gets the end points for this simulation spring feature."""
		self._instance.GetEndPoints = value

	@property
	def set_end_points(self):
		"""Sets the end points for this simulation spring feature."""
		return self._instance.SetEndPoints

	@set_end_points.setter
	def set_end_points(self, value):
		"""Sets the end points for this simulation spring feature."""
		self._instance.SetEndPoints = value

