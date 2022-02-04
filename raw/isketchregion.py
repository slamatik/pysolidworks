# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRegion_members.html
class ISketchRegion:
	def __init__(self, parent=None):
		self._instance = parent

	def sketch(self):
		"""Gets the sketch for this sketch region."""
		# return self._instance.Sketch
		raise NotImplemented

	def de_select(self):
		"""Deselects the sketch region."""
		# return self._instance.DeSelect
		raise NotImplemented

	def get_edges(self):
		"""Gets the edges on this sketch region."""
		# return self._instance.GetEdges
		raise NotImplemented

	def get_edges_count(self):
		"""Gets the number of edges for this sketch region."""
		# return self._instance.GetEdgesCount
		raise NotImplemented

	def get_first_loop(self):
		"""Gets the first loop in this sketch region."""
		# return self._instance.GetFirstLoop
		raise NotImplemented

	def i_get_edges(self, count):
		"""
		Gets the edges on this sketch region.
		:param count: Number of edges
		"""
		# return self._instance.IGetEdges(count)
		raise NotImplemented

	def select(self, append, data):
		"""
		Selects the sketch region and marks it.
		:param append: True to append this selection to the selection list, false to replace the selection list with this selection
		:param data: ISelectData object
		"""
		# return self._instance.Select2(append, data)
		raise NotImplemented

