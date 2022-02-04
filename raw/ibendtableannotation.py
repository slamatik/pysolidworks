# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTableAnnotation_members.html
class IBendTableAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def bend_table(self):
		"""Gets the bend table feature for this bend table annotation."""
		# return self._instance.BendTable
		raise NotImplemented

