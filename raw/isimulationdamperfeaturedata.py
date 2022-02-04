# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationDamperFeatureData_members.html
class ISimulationDamperFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def base_component(self):
		"""Gets or sets the base component for this damper feature."""
		return self._instance.BaseComponent

	@base_component.setter
	def base_component(self, value):
		"""Gets or sets the base component for this damper feature."""
		self._instance.BaseComponent = value

	@property
	def damping_constant(self):
		"""Gets or sets the damping constant value for this damper feature."""
		return self._instance.DampingConstant

	@damping_constant.setter
	def damping_constant(self, value):
		"""Gets or sets the damping constant value for this damper feature."""
		self._instance.DampingConstant = value

	@property
	def exponent_of_damper_force_expression(self):
		"""Gets or sets the exponent for the functional expression for this damper feature."""
		return self._instance.ExponentOfDamperForceExpression

	@exponent_of_damper_force_expression.setter
	def exponent_of_damper_force_expression(self, value):
		"""Gets or sets the exponent for the functional expression for this damper feature."""
		self._instance.ExponentOfDamperForceExpression = value

	@property
	def load_references(self):
		"""Gets or sets the load references for this damper feature."""
		return self._instance.LoadReferences

	@load_references.setter
	def load_references(self, value):
		"""Gets or sets the load references for this damper feature."""
		self._instance.LoadReferences = value

	@property
	def type(self):
		"""Gets the type of damper.NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the type of damper.NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Type = value

	@property
	def get_end_points(self):
		"""Gets the end points for this damper feature."""
		return self._instance.GetEndPoints

	@get_end_points.setter
	def get_end_points(self, value):
		"""Gets the end points for this damper feature."""
		self._instance.GetEndPoints = value

	@property
	def set_end_points(self):
		"""Sets the end points for this damper feature."""
		return self._instance.SetEndPoints

	@set_end_points.setter
	def set_end_points(self, value):
		"""Sets the end points for this damper feature."""
		self._instance.SetEndPoints = value

