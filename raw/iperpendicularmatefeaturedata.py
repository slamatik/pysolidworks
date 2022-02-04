# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData_members.html
class IPerpendicularMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this perpendicular mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this perpendicular mate."""
		self._instance.EntitiesToMate = value

	@property
	def pick_points(self):
		"""Gets or sets the pick points for the entities to mate in this perpendicular mate."""
		return self._instance.PickPoints

	@pick_points.setter
	def pick_points(self, value):
		"""Gets or sets the pick points for the entities to mate in this perpendicular mate."""
		self._instance.PickPoints = value

