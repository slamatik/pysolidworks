# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotFeatureData_members.html
class IMotionPlotFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def visibility(self):
		"""Gets or sets whether a plot's feature data is visible."""
		return self._instance.Visibility

	@visibility.setter
	def visibility(self, value):
		"""Gets or sets whether a plot's feature data is visible."""
		self._instance.Visibility = value

	@property
	def add_y_axis(self):
		"""Adds y-axis feature to a plot."""
		return self._instance.AddYAxis

	@add_y_axis.setter
	def add_y_axis(self, value):
		"""Adds y-axis feature to a plot."""
		self._instance.AddYAxis = value

	@property
	def get_x_axis(self):
		"""Gets x-axis feature of a plot."""
		return self._instance.GetXAxis

	@get_x_axis.setter
	def get_x_axis(self, value):
		"""Gets x-axis feature of a plot."""
		self._instance.GetXAxis = value

	@property
	def get_y_axis(self):
		"""Gets y-axis features of a plot."""
		return self._instance.GetYAxis

	@get_y_axis.setter
	def get_y_axis(self, value):
		"""Gets y-axis features of a plot."""
		self._instance.GetYAxis = value

	@property
	def i_get_y_axis(self):
		"""Gets y-axis features of a plot."""
		return self._instance.IGetYAxis

	@i_get_y_axis.setter
	def i_get_y_axis(self, value):
		"""Gets y-axis features of a plot."""
		self._instance.IGetYAxis = value

