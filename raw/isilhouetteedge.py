# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.html
class ISilhouetteEdge:
	def __init__(self, parent=None):
		self._instance = parent

	def get_curve(self):
		"""Gets the curve for this silhouette edge."""
		# return self._instance.GetCurve
		raise NotImplemented

	def get_end_point(self):
		"""Gets the end point of this silhouette edge."""
		# return self._instance.GetEndPoint
		raise NotImplemented

	def get_face(self):
		"""Gets the face for this silhouette edge."""
		# return self._instance.GetFace
		raise NotImplemented

	def get_start_point(self):
		"""Gets the start point of this silhouette edge."""
		# return self._instance.GetStartPoint
		raise NotImplemented

	def get_view(self):
		"""Gets the drawing view for this silhouette edge."""
		# return self._instance.GetView
		raise NotImplemented

	def select(self, append, data):
		"""
		Selects the silhouette edge in the active drawing view.
		:param append: True appends this selection to the selection list, false replaces the selection list with this selection
		:param data: SelectData object
		"""
		# return self._instance.Select2(append, data)
		raise NotImplemented

