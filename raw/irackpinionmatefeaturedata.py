# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRackPinionMateFeatureData_members.html
class IRackPinionMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def diameter_type(self):
		"""Gets or sets the type of diameter to set."""
		return self._instance.DiameterType

	@diameter_type.setter
	def diameter_type(self, value):
		"""Gets or sets the type of diameter to set."""
		self._instance.DiameterType = value

	@property
	def diameter_val(self):
		"""Gets or sets either the pinion pitch diameter or the rack translation distance per pinion revolution."""
		return self._instance.DiameterVal

	@diameter_val.setter
	def diameter_val(self, value):
		"""Gets or sets either the pinion pitch diameter or the rack translation distance per pinion revolution."""
		self._instance.DiameterVal = value

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this rack and pinion mate feature."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this rack and pinion mate feature."""
		self._instance.EntitiesToMate = value

	@property
	def reverse(self):
		"""Gets or sets whether to change the direction of movement of the rack and pinion relative to one another."""
		return self._instance.Reverse

	@reverse.setter
	def reverse(self, value):
		"""Gets or sets whether to change the direction of movement of the rack and pinion relative to one another."""
		self._instance.Reverse = value

