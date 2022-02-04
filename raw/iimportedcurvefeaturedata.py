# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportedCurveFeatureData_members.html
class IImportedCurveFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def curves(self):
		"""Gets or sets the curves for this imported curve feature."""
		return self._instance.Curves

	@curves.setter
	def curves(self, value):
		"""Gets or sets the curves for this imported curve feature."""
		self._instance.Curves = value

	@property
	def get_curve_count(self):
		"""Gets the number of curves for this imported curve feature."""
		return self._instance.GetCurveCount

	@get_curve_count.setter
	def get_curve_count(self, value):
		"""Gets the number of curves for this imported curve feature."""
		self._instance.GetCurveCount = value

	@property
	def i_get_curves(self):
		"""Gets the curves for this imported curve feature."""
		return self._instance.IGetCurves

	@i_get_curves.setter
	def i_get_curves(self, value):
		"""Gets the curves for this imported curve feature."""
		self._instance.IGetCurves = value

	@property
	def i_set_curves(self):
		"""Sets the curves for this imported curve feature."""
		return self._instance.ISetCurves

	@i_set_curves.setter
	def i_set_curves(self, value):
		"""Sets the curves for this imported curve feature."""
		self._instance.ISetCurves = value

	@property
	def set_body(self):
		"""Modifies the wire body for this imported curve feature."""
		return self._instance.SetBody

	@set_body.setter
	def set_body(self, value):
		"""Modifies the wire body for this imported curve feature."""
		self._instance.SetBody = value

