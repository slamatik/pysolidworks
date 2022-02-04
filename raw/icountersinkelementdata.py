# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData_members.html
class ICountersinkElementData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the angle of this countersink hole element."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle of this countersink hole element."""
		self._instance.Angle = value

	@property
	def angle_override(self):
		"""Gets or sets whether to override the angle of this countersink hole element."""
		return self._instance.AngleOverride

	@angle_override.setter
	def angle_override(self, value):
		"""Gets or sets whether to override the angle of this countersink hole element."""
		self._instance.AngleOverride = value

	@property
	def end_condition_override(self):
		"""Gets or sets whether to override the end condition of this countersink hole element."""
		return self._instance.EndConditionOverride

	@end_condition_override.setter
	def end_condition_override(self, value):
		"""Gets or sets whether to override the end condition of this countersink hole element."""
		self._instance.EndConditionOverride = value

	@property
	def use_standard_depth(self):
		"""Gets or sets whether to use the standard offset distance for the end condition of this countersink hole element."""
		return self._instance.UseStandardDepth

	@use_standard_depth.setter
	def use_standard_depth(self, value):
		"""Gets or sets whether to use the standard offset distance for the end condition of this countersink hole element."""
		self._instance.UseStandardDepth = value

