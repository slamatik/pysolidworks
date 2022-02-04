# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTableAnnotation_members.html
class IPunchTableAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def punch_table(self):
		"""Gets the punch table feature for this table annotation."""
		# return self._instance.PunchTable
		raise NotImplemented

