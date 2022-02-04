# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollision_members.html
class ICollision:
	def __init__(self, parent=None):
		self._instance = parent

	def get_components(self):
		"""Gets the components involved in this collision."""
		# return self._instance.GetComponents
		raise NotImplemented

	def get_transforms(self):
		"""Gets the current transforms of the components involved in this collision."""
		# return self._instance.GetTransforms
		raise NotImplemented

	def is_penetrating(self):
		"""Gets whether the components involved in this collision penetrate one another."""
		# return self._instance.IsPenetrating
		raise NotImplemented

