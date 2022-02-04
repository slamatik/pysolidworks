# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.html
class ILinearCouplerMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def coupler_ratio_denominator(self):
		"""Gets or sets the displacement of the second mated component along its direction of motion in this linear/linear coupler mate."""
		return self._instance.CouplerRatioDenominator

	@coupler_ratio_denominator.setter
	def coupler_ratio_denominator(self, value):
		"""Gets or sets the displacement of the second mated component along its direction of motion in this linear/linear coupler mate."""
		self._instance.CouplerRatioDenominator = value

	@property
	def coupler_ratio_numerator(self):
		"""Gets or sets the displacement of the first mated component along its direction of motion in this linear/linear coupler mate."""
		return self._instance.CouplerRatioNumerator

	@coupler_ratio_numerator.setter
	def coupler_ratio_numerator(self, value):
		"""Gets or sets the displacement of the first mated component along its direction of motion in this linear/linear coupler mate."""
		self._instance.CouplerRatioNumerator = value

	@property
	def mate_entity(self):
		"""Gets or sets the entity of the first mated component of this linear/linear coupler mate."""
		return self._instance.MateEntity1

	@mate_entity.setter
	def mate_entity(self, value):
		"""Gets or sets the entity of the first mated component of this linear/linear coupler mate."""
		self._instance.MateEntity1 = value

	@property
	def mate_entity(self):
		"""Gets or sets the entity of the second mated component of this linear/linear coupler mate."""
		return self._instance.MateEntity2

	@mate_entity.setter
	def mate_entity(self, value):
		"""Gets or sets the entity of the second mated component of this linear/linear coupler mate."""
		self._instance.MateEntity2 = value

	@property
	def reference_component(self):
		"""Gets or sets the reference component of the first mate entity of this linear coupler mate."""
		return self._instance.ReferenceComponent1

	@reference_component.setter
	def reference_component(self, value):
		"""Gets or sets the reference component of the first mate entity of this linear coupler mate."""
		self._instance.ReferenceComponent1 = value

	@property
	def reference_component(self):
		"""Gets or sets the reference component of the second mate entity of this linear/linear coupler mate."""
		return self._instance.ReferenceComponent2

	@reference_component.setter
	def reference_component(self, value):
		"""Gets or sets the reference component of the second mate entity of this linear/linear coupler mate."""
		self._instance.ReferenceComponent2 = value

	@property
	def reverse(self):
		"""Gets or sets whether to reverse the direction of motion of the second mated component relative to the direction of motion of the first mated component of this linear/linear coupler mate."""
		return self._instance.Reverse

	@reverse.setter
	def reverse(self, value):
		"""Gets or sets whether to reverse the direction of motion of the second mated component relative to the direction of motion of the first mated component of this linear/linear coupler mate."""
		self._instance.Reverse = value

