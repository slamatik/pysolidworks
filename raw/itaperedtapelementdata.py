# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData_members.html
class ITaperedTapElementData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def custom_sizing(self):
		"""Gets or sets the custom sizing for this tapered tap hole element."""
		return self._instance.CustomSizing

	@custom_sizing.setter
	def custom_sizing(self, value):
		"""Gets or sets the custom sizing for this tapered tap hole element."""
		self._instance.CustomSizing = value

	@property
	def end_condition_override(self):
		"""Gets or sets whether to override the end condition of this tapered tap hole element."""
		return self._instance.EndConditionOverride

	@end_condition_override.setter
	def end_condition_override(self, value):
		"""Gets or sets whether to override the end condition of this tapered tap hole element."""
		self._instance.EndConditionOverride = value

	@property
	def thread_class(self):
		"""Gets or sets the thread class for this tapered tap hole element."""
		return self._instance.ThreadClass

	@thread_class.setter
	def thread_class(self, value):
		"""Gets or sets the thread class for this tapered tap hole element."""
		self._instance.ThreadClass = value

	@property
	def thread_class_override(self):
		"""Gets or sets whether to override the thread class of this tapered tap hole element."""
		return self._instance.ThreadClassOverride

	@thread_class_override.setter
	def thread_class_override(self, value):
		"""Gets or sets whether to override the thread class of this tapered tap hole element."""
		self._instance.ThreadClassOverride = value

	@property
	def use_standard_depth(self):
		"""Gets or sets whether to use the standard offset distance for the end condition of this tapered tap hole element."""
		return self._instance.UseStandardDepth

	@use_standard_depth.setter
	def use_standard_depth(self, value):
		"""Gets or sets whether to use the standard offset distance for the end condition of this tapered tap hole element."""
		self._instance.UseStandardDepth = value

