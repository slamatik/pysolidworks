# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDistanceMateFeatureData_members.html
class IDistanceMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def distance(self):
		"""Gets or sets the distance of this distance mate."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the distance of this distance mate."""
		self._instance.Distance = value

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this distance mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this distance mate."""
		self._instance.EntitiesToMate = value

	@property
	def flip_dimension(self):
		"""Gets or sets whether to move entities to opposite sides of the dimension of this distance mate."""
		return self._instance.FlipDimension

	@flip_dimension.setter
	def flip_dimension(self, value):
		"""Gets or sets whether to move entities to opposite sides of the dimension of this distance mate."""
		self._instance.FlipDimension = value

	@property
	def is_advanced_mate(self):
		"""Gets or sets whether this distance mate is a limit distance mate."""
		return self._instance.IsAdvancedMate

	@is_advanced_mate.setter
	def is_advanced_mate(self, value):
		"""Gets or sets whether this distance mate is a limit distance mate."""
		self._instance.IsAdvancedMate = value

	@property
	def mate_alignment(self):
		"""Gets or sets the alignment of this distance mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the alignment of this distance mate."""
		self._instance.MateAlignment = value

	@property
	def maximum_distance(self):
		"""Gets or sets the maximum distance of this limit distance mate."""
		return self._instance.MaximumDistance

	@maximum_distance.setter
	def maximum_distance(self, value):
		"""Gets or sets the maximum distance of this limit distance mate."""
		self._instance.MaximumDistance = value

	@property
	def minimum_distance(self):
		"""Gets or sets the minimum distance of this limit distance mate."""
		return self._instance.MinimumDistance

	@minimum_distance.setter
	def minimum_distance(self, value):
		"""Gets or sets the minimum distance of this limit distance mate."""
		self._instance.MinimumDistance = value

