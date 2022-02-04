# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData_members.html
class ICounterboreElementData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def end_condition_override(self):
		"""Gets or sets whether to override the end condition of this counterbore hole element."""
		return self._instance.EndConditionOverride

	@end_condition_override.setter
	def end_condition_override(self, value):
		"""Gets or sets whether to override the end condition of this counterbore hole element."""
		self._instance.EndConditionOverride = value

	@property
	def use_standard_depth(self):
		"""Gets or sets whether to use the standard offset distance for the end condition of this counterbore hole element."""
		return self._instance.UseStandardDepth

	@use_standard_depth.setter
	def use_standard_depth(self, value):
		"""Gets or sets whether to use the standard offset distance for the end condition of this counterbore hole element."""
		self._instance.UseStandardDepth = value

