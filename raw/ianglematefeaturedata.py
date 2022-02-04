# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAngleMateFeatureData_members.html
class IAngleMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the angle of this angle mate."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle of this angle mate."""
		self._instance.Angle = value

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this angle mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this angle mate."""
		self._instance.EntitiesToMate = value

	@property
	def flip_dimension(self):
		"""Gets or sets whether to move entities to opposite sides of the dimension in this angle mate."""
		return self._instance.FlipDimension

	@flip_dimension.setter
	def flip_dimension(self, value):
		"""Gets or sets whether to move entities to opposite sides of the dimension in this angle mate."""
		self._instance.FlipDimension = value

	@property
	def is_advanced_mate(self):
		"""Gets or sets whether this angle mate is a limit angle mate."""
		return self._instance.IsAdvancedMate

	@is_advanced_mate.setter
	def is_advanced_mate(self, value):
		"""Gets or sets whether this angle mate is a limit angle mate."""
		self._instance.IsAdvancedMate = value

	@property
	def mate_alignment(self):
		"""Gets or sets the alignment of this angle mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the alignment of this angle mate."""
		self._instance.MateAlignment = value

	@property
	def maximum_angle(self):
		"""Gets or sets the maximum angle of this limit angle mate."""
		return self._instance.MaximumAngle

	@maximum_angle.setter
	def maximum_angle(self, value):
		"""Gets or sets the maximum angle of this limit angle mate."""
		self._instance.MaximumAngle = value

	@property
	def minimum_angle(self):
		"""Gets or sets the minimum angle of this limit angle mate."""
		return self._instance.MinimumAngle

	@minimum_angle.setter
	def minimum_angle(self, value):
		"""Gets or sets the minimum angle of this limit angle mate."""
		self._instance.MinimumAngle = value

	@property
	def reference_entity(self):
		"""Gets or sets the direction reference entity for this angle mate."""
		return self._instance.ReferenceEntity

	@reference_entity.setter
	def reference_entity(self, value):
		"""Gets or sets the direction reference entity for this angle mate."""
		self._instance.ReferenceEntity = value

