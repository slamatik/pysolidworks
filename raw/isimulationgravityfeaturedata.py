# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimulationGravityFeatureData_members.html
class ISimulationGravityFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def axis(self):
		"""Gets or sets the axis for this Gravity feature."""
		return self._instance.Axis

	@axis.setter
	def axis(self, value):
		"""Gets or sets the axis for this Gravity feature."""
		self._instance.Axis = value

	@property
	def direction_reference(self):
		"""Gets or sets the direction of in which gravity moves."""
		return self._instance.DirectionReference

	@direction_reference.setter
	def direction_reference(self, value):
		"""Gets or sets the direction of in which gravity moves."""
		self._instance.DirectionReference = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of gravity."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of gravity."""
		self._instance.ReverseDirection = value

	@property
	def strength(self):
		"""Gets or sets the gravitational strength."""
		return self._instance.Strength

	@strength.setter
	def strength(self, value):
		"""Gets or sets the gravitational strength."""
		self._instance.Strength = value

