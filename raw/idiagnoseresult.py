# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDiagnoseResult_members.html
class IDiagnoseResult:
	def __init__(self, parent=None):
		self._instance = parent

	def get_co_edges_at_gap(self, index):
		"""
		Gets the coedges at the specified gap.
		:param index: Index number of the gap to get
		"""
		# return self._instance.GetCoEdgesAtGap(index)
		raise NotImplemented

	def get_co_edges_count_at_gap(self, index):
		"""
		Gets the number of coedges at the specified gap.
		:param index: Index number of the gap to get
		"""
		# return self._instance.GetCoEdgesCountAtGap(index)
		raise NotImplemented

	def get_gaps_count(self):
		"""Gets the number of gaps on the body."""
		# return self._instance.GetGapsCount
		raise NotImplemented

	def i_get_co_edges_at_gap(self, index, co_edge_count):
		"""
		Gets the coedges at the specified gap.
		:param index: Index number of the gap to get
		:param co_edge_count: Number of coedges at that gap
		"""
		# return self._instance.IGetCoEdgesAtGap(index, co_edge_count)
		raise NotImplemented

