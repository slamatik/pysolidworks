# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData_members.html
class IStraightElementData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def classification_type(self):
		"""Gets or sets the classification type of this straight hole element."""
		return self._instance.ClassificationType

	@classification_type.setter
	def classification_type(self, value):
		"""Gets or sets the classification type of this straight hole element."""
		self._instance.ClassificationType = value

	@property
	def drill_point_angle(self):
		"""Gets or sets the drill point angle of this straight hole element."""
		return self._instance.DrillPointAngle

	@drill_point_angle.setter
	def drill_point_angle(self, value):
		"""Gets or sets the drill point angle of this straight hole element."""
		self._instance.DrillPointAngle = value

	@property
	def drill_point_angle_override(self):
		"""Gets or sets whether to override the drill point angle of this straight hole element."""
		return self._instance.DrillPointAngleOverride

	@drill_point_angle_override.setter
	def drill_point_angle_override(self, value):
		"""Gets or sets whether to override the drill point angle of this straight hole element."""
		self._instance.DrillPointAngleOverride = value

	@property
	def end_shape(self):
		"""Gets or sets the end shape for this straight hole element."""
		return self._instance.EndShape

	@end_shape.setter
	def end_shape(self, value):
		"""Gets or sets the end shape for this straight hole element."""
		self._instance.EndShape = value

	@property
	def filter(self):
		"""Gets or sets the filter for this straight hole element."""
		return self._instance.Filter

	@filter.setter
	def filter(self, value):
		"""Gets or sets the filter for this straight hole element."""
		self._instance.Filter = value

	@property
	def fit_type(self):
		"""Gets or sets the fit type for this straight hole element."""
		return self._instance.FitType

	@fit_type.setter
	def fit_type(self, value):
		"""Gets or sets the fit type for this straight hole element."""
		self._instance.FitType = value

	@property
	def hole_fit(self):
		"""Gets or sets the hole fit for this straight hole element."""
		return self._instance.HoleFit

	@hole_fit.setter
	def hole_fit(self, value):
		"""Gets or sets the hole fit for this straight hole element."""
		self._instance.HoleFit = value

	@property
	def shaft_fit(self):
		"""Gets or sets the shaft fit for this straight hole element."""
		return self._instance.ShaftFit

	@shaft_fit.setter
	def shaft_fit(self, value):
		"""Gets or sets the shaft fit for this straight hole element."""
		self._instance.ShaftFit = value

