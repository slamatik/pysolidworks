# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITangentMateFeatureData_members.html
class ITangentMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this tangent mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this tangent mate."""
		self._instance.EntitiesToMate = value

	@property
	def mate_alignment(self):
		"""Gets or sets the mate alignment of this tangent mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the mate alignment of this tangent mate."""
		self._instance.MateAlignment = value

	@property
	def pick_points(self):
		"""Gets or sets the pick points for the entities to mate in this tangent mate."""
		return self._instance.PickPoints

	@pick_points.setter
	def pick_points(self, value):
		"""Gets or sets the pick points for the entities to mate in this tangent mate."""
		self._instance.PickPoints = value

