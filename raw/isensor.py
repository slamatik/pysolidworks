# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISensor_members.html
class ISensor:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def sensor_alert_enabled(self):
		"""Gets or sets whether an alert is triggered when the limits of the sensor deviate from its specified values."""
		return self._instance.SensorAlertEnabled

	@sensor_alert_enabled.setter
	def sensor_alert_enabled(self, value):
		"""Gets or sets whether an alert is triggered when the limits of the sensor deviate from its specified values."""
		self._instance.SensorAlertEnabled = value

	@property
	def sensor_alert_state(self):
		"""Gets whether an alert is currently triggered for this sensor."""
		return self._instance.SensorAlertState

	@sensor_alert_state.setter
	def sensor_alert_state(self, value):
		"""Gets whether an alert is currently triggered for this sensor."""
		self._instance.SensorAlertState = value

	@property
	def sensor_alert_type(self):
		"""Gets or sets the type of alert for this sensor."""
		return self._instance.SensorAlertType

	@sensor_alert_type.setter
	def sensor_alert_type(self, value):
		"""Gets or sets the type of alert for this sensor."""
		self._instance.SensorAlertType = value

	@property
	def sensor_alert_value(self):
		"""Gets or sets the alert value for this sensor."""
		return self._instance.SensorAlertValue1

	@sensor_alert_value.setter
	def sensor_alert_value(self, value):
		"""Gets or sets the alert value for this sensor."""
		self._instance.SensorAlertValue1 = value

	@property
	def sensor_alert_value(self):
		"""Gets or sets alert value for this sensor; only in effect when sensor alert type set to swSensorAlert_Between."""
		return self._instance.SensorAlertValue2

	@sensor_alert_value.setter
	def sensor_alert_value(self, value):
		"""Gets or sets alert value for this sensor; only in effect when sensor alert type set to swSensorAlert_Between."""
		self._instance.SensorAlertValue2 = value

	@property
	def sensor_type(self):
		"""Gets the type of this sensor."""
		return self._instance.SensorType

	@sensor_type.setter
	def sensor_type(self, value):
		"""Gets the type of this sensor."""
		self._instance.SensorType = value

	@property
	def get_sensor_feature_data(self):
		"""Gets a sensor feature data."""
		return self._instance.GetSensorFeatureData

	@get_sensor_feature_data.setter
	def get_sensor_feature_data(self, value):
		"""Gets a sensor feature data."""
		self._instance.GetSensorFeatureData = value

	@property
	def get_sensor_value(self):
		"""Gets the value and units of this sensor."""
		return self._instance.GetSensorValue

	@get_sensor_value.setter
	def get_sensor_value(self, value):
		"""Gets the value and units of this sensor."""
		self._instance.GetSensorValue = value

	@property
	def update_sensor(self):
		"""Updates the sensor."""
		return self._instance.UpdateSensor

	@update_sensor.setter
	def update_sensor(self, value):
		"""Updates the sensor."""
		self._instance.UpdateSensor = value

