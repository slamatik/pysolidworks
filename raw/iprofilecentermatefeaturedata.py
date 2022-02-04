# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData_members.html
class IProfileCenterMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this profile center mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this profile center mate."""
		self._instance.EntitiesToMate = value

	@property
	def flip_dimension(self):
		"""Gets or sets whether to move entities to opposite sides of the dimension of this profile center mate."""
		return self._instance.FlipDimension

	@flip_dimension.setter
	def flip_dimension(self, value):
		"""Gets or sets whether to move entities to opposite sides of the dimension of this profile center mate."""
		self._instance.FlipDimension = value

	@property
	def lock_rotation(self):
		"""Gets or sets whether to lock the rotation of this profile center mate."""
		return self._instance.LockRotation

	@lock_rotation.setter
	def lock_rotation(self, value):
		"""Gets or sets whether to lock the rotation of this profile center mate."""
		self._instance.LockRotation = value

	@property
	def mate_alignment(self):
		"""Gets or sets the alignment of this profile center mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the alignment of this profile center mate."""
		self._instance.MateAlignment = value

	@property
	def offset_distance(self):
		"""Gets or sets the offset distance for this profile center mate."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the offset distance for this profile center mate."""
		self._instance.OffsetDistance = value

