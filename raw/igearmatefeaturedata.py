# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGearMateFeatureData_members.html
class IGearMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this gear mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this gear mate."""
		self._instance.EntitiesToMate = value

	@property
	def gear_ratio_denominator(self):
		"""Gets or sets the denominator of the gear ratio of this gear mate."""
		return self._instance.GearRatioDenominator

	@gear_ratio_denominator.setter
	def gear_ratio_denominator(self, value):
		"""Gets or sets the denominator of the gear ratio of this gear mate."""
		self._instance.GearRatioDenominator = value

	@property
	def gear_ratio_numerator(self):
		"""Gets or sets the numerator of the gear ratio of this gear mate."""
		return self._instance.GearRatioNumerator

	@gear_ratio_numerator.setter
	def gear_ratio_numerator(self, value):
		"""Gets or sets the numerator of the gear ratio of this gear mate."""
		self._instance.GearRatioNumerator = value

	@property
	def reverse(self):
		"""Gets or sets whether to change the direction of rotation of the gears relative to one another in this gear mate."""
		return self._instance.Reverse

	@reverse.setter
	def reverse(self, value):
		"""Gets or sets whether to change the direction of rotation of the gears relative to one another in this gear mate."""
		self._instance.Reverse = value

