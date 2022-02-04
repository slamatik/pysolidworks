# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutStringVariable_members.html
class ICalloutStringVariable:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def string(self):
		"""Gets or sets the text for this string variable in a hole callout."""
		return self._instance.String

	@string.setter
	def string(self, value):
		"""Gets or sets the text for this string variable in a hole callout."""
		self._instance.String = value

