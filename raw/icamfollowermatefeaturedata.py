# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamFollowerMateFeatureData_members.html
class ICamFollowerMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this cam-follower mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this cam-follower mate."""
		self._instance.EntitiesToMate = value

	@property
	def mate_alignment(self):
		"""Gets or sets the mate alignment of this cam-follower mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the mate alignment of this cam-follower mate."""
		self._instance.MateAlignment = value

