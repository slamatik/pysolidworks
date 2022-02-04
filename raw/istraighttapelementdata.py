# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.html
class IStraightTapElementData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def custom_sizing(self):
		"""Gets or sets the custom sizing for this straight tap hole element."""
		return self._instance.CustomSizing

	@custom_sizing.setter
	def custom_sizing(self, value):
		"""Gets or sets the custom sizing for this straight tap hole element."""
		self._instance.CustomSizing = value

	@property
	def drill_point_angle(self):
		"""Gets or sets the drill point angle of this straight tap hole element."""
		return self._instance.DrillPointAngle

	@drill_point_angle.setter
	def drill_point_angle(self, value):
		"""Gets or sets the drill point angle of this straight tap hole element."""
		self._instance.DrillPointAngle = value

	@property
	def drill_point_angle_override(self):
		"""Gets or sets whether to override the drill point angle of this straight tap hole element."""
		return self._instance.DrillPointAngleOverride

	@drill_point_angle_override.setter
	def drill_point_angle_override(self, value):
		"""Gets or sets whether to override the drill point angle of this straight tap hole element."""
		self._instance.DrillPointAngleOverride = value

	@property
	def end_shape(self):
		"""Gets or sets the end shape for this straight tap hole element."""
		return self._instance.EndShape

	@end_shape.setter
	def end_shape(self, value):
		"""Gets or sets the end shape for this straight tap hole element."""
		self._instance.EndShape = value

	@property
	def equation(self):
		"""Gets or sets the equation for the blind depth or offset distance of this straight tap hole element."""
		return self._instance.Equation

	@equation.setter
	def equation(self, value):
		"""Gets or sets the equation for the blind depth or offset distance of this straight tap hole element."""
		self._instance.Equation = value

	@property
	def thread_class(self):
		"""Gets or sets the thread class for this straight tap hole element."""
		return self._instance.ThreadClass

	@thread_class.setter
	def thread_class(self, value):
		"""Gets or sets the thread class for this straight tap hole element."""
		self._instance.ThreadClass = value

	@property
	def thread_class_override(self):
		"""Gets or sets whether to override the thread class of this straight tap hole element."""
		return self._instance.ThreadClassOverride

	@thread_class_override.setter
	def thread_class_override(self, value):
		"""Gets or sets whether to override the thread class of this straight tap hole element."""
		self._instance.ThreadClassOverride = value

