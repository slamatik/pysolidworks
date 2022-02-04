# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFolder_members.html
class ICosmeticWeldBeadFolder:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def cost_per_unit_mass(self):
		"""Gets or sets the welding cost per unit mass."""
		return self._instance.CostPerUnitMass

	@cost_per_unit_mass.setter
	def cost_per_unit_mass(self, value):
		"""Gets or sets the welding cost per unit mass."""
		self._instance.CostPerUnitMass = value

	@property
	def mass_per_unit_length(self):
		"""Gets or sets the weld mass per unit length."""
		return self._instance.MassPerUnitLength

	@mass_per_unit_length.setter
	def mass_per_unit_length(self, value):
		"""Gets or sets the weld mass per unit length."""
		self._instance.MassPerUnitLength = value

	@property
	def material(self):
		"""Gets or sets the material of the weld bead."""
		return self._instance.Material

	@material.setter
	def material(self, value):
		"""Gets or sets the material of the weld bead."""
		self._instance.Material = value

	@property
	def number_of_weld_passes(self):
		"""Gets or sets the number of weld passes required to deposit the correct amount of welding material."""
		return self._instance.NumberOfWeldPasses

	@number_of_weld_passes.setter
	def number_of_weld_passes(self, value):
		"""Gets or sets the number of weld passes required to deposit the correct amount of welding material."""
		self._instance.NumberOfWeldPasses = value

	@property
	def process(self):
		"""Gets or sets the weld process."""
		return self._instance.Process

	@process.setter
	def process(self, value):
		"""Gets or sets the weld process."""
		self._instance.Process = value

	@property
	def time_per_unit_length(self):
		"""Gets or sets the welding time per unit length."""
		return self._instance.TimePerUnitLength

	@time_per_unit_length.setter
	def time_per_unit_length(self, value):
		"""Gets or sets the welding time per unit length."""
		self._instance.TimePerUnitLength = value

	@property
	def total_cost(self):
		"""Gets the total welding cost."""
		return self._instance.TotalCost

	@total_cost.setter
	def total_cost(self, value):
		"""Gets the total welding cost."""
		self._instance.TotalCost = value

	@property
	def total_length(self):
		"""Gets the total weld length."""
		return self._instance.TotalLength

	@total_length.setter
	def total_length(self, value):
		"""Gets the total weld length."""
		self._instance.TotalLength = value

	@property
	def total_mass(self):
		"""Gets the total weld mass."""
		return self._instance.TotalMass

	@total_mass.setter
	def total_mass(self, value):
		"""Gets the total weld mass."""
		self._instance.TotalMass = value

	@property
	def total_number(self):
		"""Gets the total number of welds."""
		return self._instance.TotalNumber

	@total_number.setter
	def total_number(self, value):
		"""Gets the total number of welds."""
		self._instance.TotalNumber = value

	@property
	def total_time(self):
		"""Gets the total welding time."""
		return self._instance.TotalTime

	@total_time.setter
	def total_time(self, value):
		"""Gets the total welding time."""
		self._instance.TotalTime = value

