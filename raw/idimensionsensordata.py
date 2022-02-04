# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionSensorData_members.html
class IDimensionSensorData:
	def __init__(self, parent=None):
		self._instance = parent

	def sensor_value(self):
		"""Gets the value of the display dimension for this Measurement (dimension) sensor."""
		# return self._instance.SensorValue
		raise NotImplemented

	def get_display_dimension(self):
		"""Gets the display dimension for this Measurement (dimension) sensor."""
		# return self._instance.GetDisplayDimension
		raise NotImplemented

