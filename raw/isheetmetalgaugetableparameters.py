# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalGaugeTableParameters_members.html
class ISheetMetalGaugeTableParameters:
	def __init__(self, parent=None):
		self._instance = parent

	def override_radius(self):
		"""Gets whether the bend radius of this gauge table is overridden."""
		# return self._instance.OverrideRadius
		raise NotImplemented

	def override_thickness(self):
		"""Gets whether the gauge thickness of this gauge table is overridden."""
		# return self._instance.OverrideThickness
		raise NotImplemented

	def process(self):
		"""Gets the sheet metal process of this gauge table."""
		# return self._instance.Process
		raise NotImplemented

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of gauge thickness in this gauge table."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of gauge thickness in this gauge table."""
		self._instance.ReverseDirection = value

	@property
	def get_available_gauge_numbers(self):
		"""Gets the available gauge numbers in this gauge table."""
		return self._instance.GetAvailableGaugeNumbers

	@get_available_gauge_numbers.setter
	def get_available_gauge_numbers(self, value):
		"""Gets the available gauge numbers in this gauge table."""
		self._instance.GetAvailableGaugeNumbers = value

	@property
	def get_available_radii(self):
		"""Gets the available bend radii for the gauge number currently selected from this gauge table."""
		return self._instance.GetAvailableRadii

	@get_available_radii.setter
	def get_available_radii(self, value):
		"""Gets the available bend radii for the gauge number currently selected from this gauge table."""
		self._instance.GetAvailableRadii = value

	@property
	def get_current_gauge_number(self):
		"""Gets the gauge number currently selected from this gauge table."""
		return self._instance.GetCurrentGaugeNumber

	@get_current_gauge_number.setter
	def get_current_gauge_number(self, value):
		"""Gets the gauge number currently selected from this gauge table."""
		self._instance.GetCurrentGaugeNumber = value

	@property
	def get_current_radius(self):
		"""Gets the current bend radius for the gauge number currently selected from this gauge table."""
		return self._instance.GetCurrentRadius

	@get_current_radius.setter
	def get_current_radius(self, value):
		"""Gets the current bend radius for the gauge number currently selected from this gauge table."""
		self._instance.GetCurrentRadius = value

	@property
	def get_gauge_number_count(self):
		"""Gets the number of gauges in this gauge table."""
		return self._instance.GetGaugeNumberCount

	@get_gauge_number_count.setter
	def get_gauge_number_count(self, value):
		"""Gets the number of gauges in this gauge table."""
		self._instance.GetGaugeNumberCount = value

	@property
	def get_gauge_table_path(self):
		"""Gets the full path name of this gauge table."""
		return self._instance.GetGaugeTablePath

	@get_gauge_table_path.setter
	def get_gauge_table_path(self, value):
		"""Gets the full path name of this gauge table."""
		self._instance.GetGaugeTablePath = value

	@property
	def get_radii_count(self):
		"""Gets the number of bend radii for the gauge number currently selected from this gauge table."""
		return self._instance.GetRadiiCount

	@get_radii_count.setter
	def get_radii_count(self, value):
		"""Gets the number of bend radii for the gauge number currently selected from this gauge table."""
		self._instance.GetRadiiCount = value

	@property
	def get_thickness(self):
		"""Gets the gauge thickness for the gauge number currently selected from this gauge table."""
		return self._instance.GetThickness

	@get_thickness.setter
	def get_thickness(self, value):
		"""Gets the gauge thickness for the gauge number currently selected from this gauge table."""
		self._instance.GetThickness = value

	@property
	def set_current_gauge_number(self):
		"""Sets the current gauge number in this gauge table."""
		return self._instance.SetCurrentGaugeNumber

	@set_current_gauge_number.setter
	def set_current_gauge_number(self, value):
		"""Sets the current gauge number in this gauge table."""
		self._instance.SetCurrentGaugeNumber = value

	@property
	def set_gauge_table_path(self):
		"""Sets the full path name of this gauge table."""
		return self._instance.SetGaugeTablePath

	@set_gauge_table_path.setter
	def set_gauge_table_path(self, value):
		"""Sets the full path name of this gauge table."""
		self._instance.SetGaugeTablePath = value

	@property
	def set_radius(self):
		"""Sets the bend radius in this gauge table."""
		return self._instance.SetRadius

	@set_radius.setter
	def set_radius(self, value):
		"""Sets the bend radius in this gauge table."""
		self._instance.SetRadius = value

	@property
	def set_thickness(self):
		"""Sets the gauge thickness in this gauge table."""
		return self._instance.SetThickness

	@set_thickness.setter
	def set_thickness(self, value):
		"""Sets the gauge thickness in this gauge table."""
		self._instance.SetThickness = value

