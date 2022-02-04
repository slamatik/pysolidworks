# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData_members.html
class IConcentricMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this concentric mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this concentric mate."""
		self._instance.EntitiesToMate = value

	@property
	def lock_rotation(self):
		"""Gets or sets whether to lock the rotation of the entities in this concentric mate."""
		return self._instance.LockRotation

	@lock_rotation.setter
	def lock_rotation(self, value):
		"""Gets or sets whether to lock the rotation of the entities in this concentric mate."""
		self._instance.LockRotation = value

	@property
	def mate_alignment(self):
		"""Gets or sets the mate alignment of this concentric mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the mate alignment of this concentric mate."""
		self._instance.MateAlignment = value

	@property
	def pick_points(self):
		"""Gets or sets the pick points for the entities to mate in this concentric mate."""
		return self._instance.PickPoints

	@pick_points.setter
	def pick_points(self, value):
		"""Gets or sets the pick points for the entities to mate in this concentric mate."""
		self._instance.PickPoints = value

