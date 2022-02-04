# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationMotorFeatureData_members.html
class ISimulationMotorFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def direction_reference(self):
		"""Gets or sets the direction in which the motor moves."""
		return self._instance.DirectionReference

	@direction_reference.setter
	def direction_reference(self, value):
		"""Gets or sets the direction in which the motor moves."""
		self._instance.DirectionReference = value

	@property
	def drive_type(self):
		"""Sets the drive type of this motor feature."""
		return self._instance.DriveType

	@drive_type.setter
	def drive_type(self, value):
		"""Sets the drive type of this motor feature."""
		self._instance.DriveType = value

	@property
	def expression(self):
		"""Gets or sets the motor motion expression for this motor feature."""
		return self._instance.Expression

	@expression.setter
	def expression(self, value):
		"""Gets or sets the motor motion expression for this motor feature."""
		self._instance.Expression = value

	@property
	def external_state(self):
		"""Gets or sets whether your application can listen to motor-related motion study event."""
		return self._instance.ExternalState

	@external_state.setter
	def external_state(self, value):
		"""Gets or sets whether your application can listen to motor-related motion study event."""
		self._instance.ExternalState = value

	@property
	def interpolation_scheme(self):
		"""Gets or set the interpolation scheme for this motor feature."""
		return self._instance.InterpolationScheme

	@interpolation_scheme.setter
	def interpolation_scheme(self, value):
		"""Gets or set the interpolation scheme for this motor feature."""
		self._instance.InterpolationScheme = value

	@property
	def load_references(self):
		"""Gets or sets the load references for this motor feature."""
		return self._instance.LoadReferences

	@load_references.setter
	def load_references(self, value):
		"""Gets or sets the load references for this motor feature."""
		self._instance.LoadReferences = value

	@property
	def location(self):
		"""Select a face, vertex, or edge on the assembly for the reference origin when setting motion relative to another part."""
		return self._instance.Location

	@location.setter
	def location(self, value):
		"""Select a face, vertex, or edge on the assembly for the reference origin when setting motion relative to another part."""
		self._instance.Location = value

	@property
	def magnitude(self):
		"""Get or set the magnitude for this motor feature."""
		return self._instance.Magnitude

	@magnitude.setter
	def magnitude(self, value):
		"""Get or set the magnitude for this motor feature."""
		self._instance.Magnitude = value

	@property
	def motion_type(self):
		"""Gets or sets the type of motion of this motor feature."""
		return self._instance.MotionType

	@motion_type.setter
	def motion_type(self, value):
		"""Gets or sets the type of motion of this motor feature."""
		self._instance.MotionType = value

	@property
	def motor_type(self):
		"""Gets the type of motor for this motor feature."""
		return self._instance.MotorType

	@motor_type.setter
	def motor_type(self, value):
		"""Gets the type of motor for this motor feature."""
		self._instance.MotorType = value

	@property
	def relative_component(self):
		"""Gets or sets a part in the assembly to which to reference motion when setting motion relative to another part in this motor feature."""
		return self._instance.RelativeComponent

	@relative_component.setter
	def relative_component(self, value):
		"""Gets or sets a part in the assembly to which to reference motion when setting motion relative to another part in this motor feature."""
		self._instance.RelativeComponent = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether or not to reverse the direction of the motor."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether or not to reverse the direction of the motor."""
		self._instance.ReverseDirection = value

	@property
	def spline_data(self):
		"""Gets or sets the spline data points for this motor feature."""
		return self._instance.SplineData

	@spline_data.setter
	def spline_data(self, value):
		"""Gets or sets the spline data points for this motor feature."""
		self._instance.SplineData = value

	@property
	def velocity(self):
		"""Gets or sets the speed of the motor if no other force acts on it."""
		return self._instance.Velocity

	@velocity.setter
	def velocity(self, value):
		"""Gets or sets the speed of the motor if no other force acts on it."""
		self._instance.Velocity = value

	@property
	def constant_speed_motor(self):
		"""Sets the constant speed for this motor feature."""
		return self._instance.ConstantSpeedMotor

	@constant_speed_motor.setter
	def constant_speed_motor(self, value):
		"""Sets the constant speed for this motor feature."""
		self._instance.ConstantSpeedMotor = value

	@property
	def distance_motor(self):
		"""Sets the distance and time for which to operate this motor feature."""
		return self._instance.DistanceMotor

	@distance_motor.setter
	def distance_motor(self, value):
		"""Sets the distance and time for which to operate this motor feature."""
		self._instance.DistanceMotor = value

	@property
	def get_interpolated_value(self):
		"""Gets the interopolated value at the specified time for this motor feature."""
		return self._instance.GetInterpolatedValue

	@get_interpolated_value.setter
	def get_interpolated_value(self, value):
		"""Gets the interopolated value at the specified time for this motor feature."""
		self._instance.GetInterpolatedValue = value

	@property
	def interpolated_motor(self):
		"""Sets the drive type and interpolation scheme for this motor feature."""
		return self._instance.InterpolatedMotor

	@interpolated_motor.setter
	def interpolated_motor(self, value):
		"""Sets the drive type and interpolation scheme for this motor feature."""
		self._instance.InterpolatedMotor = value

	@property
	def load_spline_data(self):
		"""Loads the spline data from the specified file for this motor feature."""
		return self._instance.LoadSplineData

	@load_spline_data.setter
	def load_spline_data(self, value):
		"""Loads the spline data from the specified file for this motor feature."""
		self._instance.LoadSplineData = value

	@property
	def oscillating_motor(self):
		"""Sets the displacement and frequency for oscillating motion for this motor feature."""
		return self._instance.OscillatingMotor

	@oscillating_motor.setter
	def oscillating_motor(self, value):
		"""Sets the displacement and frequency for oscillating motion for this motor feature."""
		self._instance.OscillatingMotor = value

