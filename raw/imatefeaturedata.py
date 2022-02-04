# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData_members.html
class IMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def error_status(self):
		"""Gets the status of adding or editing this mate."""
		# return self._instance.ErrorStatus
		raise NotImplemented

	@property
	def type_name(self):
		"""Gets or sets the type of this mate."""
		return self._instance.TypeName

	@type_name.setter
	def type_name(self, value):
		"""Gets or sets the type of this mate."""
		self._instance.TypeName = value

