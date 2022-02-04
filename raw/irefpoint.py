# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint_members.html
class IRefPoint:
	def __init__(self, parent=None):
		self._instance = parent

	def get_ref_point(self):
		"""Gets the parameters for this reference point."""
		# return self._instance.GetRefPoint
		raise NotImplemented

