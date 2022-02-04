# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutLengthVariable_members.html
class ICalloutLengthVariable:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def length(self):
		"""Gets or sets the length for this length variable in a hole callout."""
		return self._instance.Length

	@length.setter
	def length(self, value):
		"""Gets or sets the length for this length variable in a hole callout."""
		self._instance.Length = value

	@property
	def precision(self):
		"""Gets or sets number of digits after the decimal point to display the primary precision value for a length variable in a hole callout."""
		return self._instance.Precision

	@precision.setter
	def precision(self, value):
		"""Gets or sets number of digits after the decimal point to display the primary precision value for a length variable in a hole callout."""
		self._instance.Precision = value

	@property
	def tolerance_precision(self):
		"""Gets or sets number of digits after the decimal point to display the primary tolerance value for the length variable in a hole callout."""
		return self._instance.TolerancePrecision

	@tolerance_precision.setter
	def tolerance_precision(self, value):
		"""Gets or sets number of digits after the decimal point to display the primary tolerance value for the length variable in a hole callout."""
		self._instance.TolerancePrecision = value

