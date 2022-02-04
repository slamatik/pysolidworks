# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationForceFeatureData_members.html
class ISimulationForceFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def action_direction(self):
		"""Gets or sets the direction of the force."""
		return self._instance.ActionDirection

	@action_direction.setter
	def action_direction(self, value):
		"""Gets or sets the direction of the force."""
		self._instance.ActionDirection = value

	@property
	def action_location(self):
		"""Gets or sets the location at which to apply the force for an action-only force."""
		return self._instance.ActionLocation

	@action_location.setter
	def action_location(self, value):
		"""Gets or sets the location at which to apply the force for an action-only force."""
		self._instance.ActionLocation = value

	@property
	def action_type(self):
		"""Gets or sets the type of action for this Force feature."""
		return self._instance.ActionType

	@action_type.setter
	def action_type(self, value):
		"""Gets or sets the type of action for this Force feature."""
		self._instance.ActionType = value

	@property
	def external_state(self):
		"""Gets or sets whether your application can listen to force-related motion study events."""
		return self._instance.ExternalState

	@external_state.setter
	def external_state(self, value):
		"""Gets or sets whether your application can listen to force-related motion study events."""
		self._instance.ExternalState = value

	@property
	def force_function_type(self):
		"""Gets or sets the type of function for this Force feature."""
		return self._instance.ForceFunctionType

	@force_function_type.setter
	def force_function_type(self, value):
		"""Gets or sets the type of function for this Force feature."""
		self._instance.ForceFunctionType = value

	@property
	def force_type(self):
		"""Gets the type of force.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.ForceType

	@force_type.setter
	def force_type(self, value):
		"""Gets the type of force.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.ForceType = value

	@property
	def function_constant_value(self):
		"""Gets or sets the function constant value for this Force feature."""
		return self._instance.FunctionConstantValue

	@function_constant_value.setter
	def function_constant_value(self, value):
		"""Gets or sets the function constant value for this Force feature."""
		self._instance.FunctionConstantValue = value

	@property
	def function_expression(self):
		"""Gets or sets the expression function for this Force feature."""
		return self._instance.FunctionExpression

	@function_expression.setter
	def function_expression(self, value):
		"""Gets or sets the expression function for this Force feature."""
		self._instance.FunctionExpression = value

	@property
	def function_interpolated_values(self):
		"""Gets or sets the interpolated values for this Force feature."""
		return self._instance.FunctionInterpolatedValues

	@function_interpolated_values.setter
	def function_interpolated_values(self, value):
		"""Gets or sets the interpolated values for this Force feature."""
		self._instance.FunctionInterpolatedValues = value

	@property
	def interpolation_scheme(self):
		"""Gets the interopolation scheme for this Force feature."""
		return self._instance.InterpolationScheme

	@interpolation_scheme.setter
	def interpolation_scheme(self, value):
		"""Gets the interopolation scheme for this Force feature."""
		self._instance.InterpolationScheme = value

	@property
	def load_references(self):
		"""Gets or sets the load references for this Force feature."""
		return self._instance.LoadReferences

	@load_references.setter
	def load_references(self, value):
		"""Gets or sets the load references for this Force feature."""
		self._instance.LoadReferences = value

	@property
	def reaction_location(self):
		"""Gets or sets the location at which to apply the force for an action/reaction force."""
		return self._instance.ReactionLocation

	@reaction_location.setter
	def reaction_location(self, value):
		"""Gets or sets the location at which to apply the force for an action/reaction force."""
		self._instance.ReactionLocation = value

	@property
	def reference_component(self):
		"""Gets or sets the component to serve as a reference frame for the force."""
		return self._instance.ReferenceComponent

	@reference_component.setter
	def reference_component(self, value):
		"""Gets or sets the component to serve as a reference frame for the force."""
		self._instance.ReferenceComponent = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of the force."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of the force."""
		self._instance.ReverseDirection = value

	@property
	def get_end_points(self):
		"""Gets the end points of this Force feature."""
		return self._instance.GetEndPoints

	@get_end_points.setter
	def get_end_points(self, value):
		"""Gets the end points of this Force feature."""
		self._instance.GetEndPoints = value

	@property
	def get_function_harmonic_values(self):
		"""Gets the harmonic function values for this Force feature."""
		return self._instance.GetFunctionHarmonicValues

	@get_function_harmonic_values.setter
	def get_function_harmonic_values(self, value):
		"""Gets the harmonic function values for this Force feature."""
		self._instance.GetFunctionHarmonicValues = value

	@property
	def get_function_step_values(self):
		"""Gets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature."""
		return self._instance.GetFunctionStepValues

	@get_function_step_values.setter
	def get_function_step_values(self, value):
		"""Gets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature."""
		self._instance.GetFunctionStepValues = value

	@property
	def get_interpolated_value(self):
		"""Gets the interpolated value at the specified time for this Force feature."""
		return self._instance.GetInterpolatedValue

	@get_interpolated_value.setter
	def get_interpolated_value(self, value):
		"""Gets the interpolated value at the specified time for this Force feature."""
		self._instance.GetInterpolatedValue = value

	@property
	def load_spline_data(self):
		"""Loads the spline data from the specified file for this Force feature."""
		return self._instance.LoadSplineData

	@load_spline_data.setter
	def load_spline_data(self, value):
		"""Loads the spline data from the specified file for this Force feature."""
		self._instance.LoadSplineData = value

	@property
	def set_end_points(self):
		"""Sets the end points for this Force feature."""
		return self._instance.SetEndPoints

	@set_end_points.setter
	def set_end_points(self, value):
		"""Sets the end points for this Force feature."""
		self._instance.SetEndPoints = value

	@property
	def set_function_harmonic_values(self):
		"""Sets the harmonic function values for this Force feature."""
		return self._instance.SetFunctionHarmonicValues

	@set_function_harmonic_values.setter
	def set_function_harmonic_values(self, value):
		"""Sets the harmonic function values for this Force feature."""
		self._instance.SetFunctionHarmonicValues = value

	@property
	def set_function_step_values(self):
		"""Sets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature."""
		return self._instance.SetFunctionStepValues

	@set_function_step_values.setter
	def set_function_step_values(self, value):
		"""Sets the step function, whose magnitude transitions smoothly from one value to another value, for this Force feature."""
		self._instance.SetFunctionStepValues = value

