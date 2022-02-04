# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportStepData_members.html
class IImportStepData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def map_configuration_data(self):
		"""Gets or sets whether to import the STEP file configuration data plus geometric data or geometric data only."""
		return self._instance.MapConfigurationData

	@map_configuration_data.setter
	def map_configuration_data(self, value):
		"""Gets or sets whether to import the STEP file configuration data plus geometric data or geometric data only."""
		self._instance.MapConfigurationData = value

