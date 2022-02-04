# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlotMateFeatureData_members.html
class ISlotMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def constraint(self):
		"""Gets or sets how to constrain the component in the slot of this slot mate."""
		return self._instance.Constraint

	@constraint.setter
	def constraint(self, value):
		"""Gets or sets how to constrain the component in the slot of this slot mate."""
		self._instance.Constraint = value

	@property
	def distance(self):
		"""Gets or sets the distance from the end of the slot where to place the component axis in this slot mate."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the distance from the end of the slot where to place the component axis in this slot mate."""
		self._instance.Distance = value

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this slot mate feature."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this slot mate feature."""
		self._instance.EntitiesToMate = value

	@property
	def flip_direction(self):
		"""Gets or sets whether to change the endpoint from where to measure distance."""
		return self._instance.FlipDirection

	@flip_direction.setter
	def flip_direction(self, value):
		"""Gets or sets whether to change the endpoint from where to measure distance."""
		self._instance.FlipDirection = value

	@property
	def mate_alignment(self):
		"""Gets or sets the mate alignment of this slot mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the mate alignment of this slot mate."""
		self._instance.MateAlignment = value

	@property
	def percent(self):
		"""Gets or sets the percent of slot length where to place the component axis in this slot mate."""
		return self._instance.Percent

	@percent.setter
	def percent(self, value):
		"""Gets or sets the percent of slot length where to place the component axis in this slot mate."""
		self._instance.Percent = value

