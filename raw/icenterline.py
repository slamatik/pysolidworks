# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterLine_members.html
class ICenterLine:
	def __init__(self, parent=None):
		self._instance = parent

	def get_annotation(self):
		"""Gets the general annotation for this centerline."""
		# return self._instance.GetAnnotation
		raise NotImplemented

	def get_next(self):
		"""Gets the next centerline in this drawing view."""
		# return self._instance.GetNext
		raise NotImplemented

