# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchContour_members.html
class ISketchContour:
	def __init__(self, parent=None):
		self._instance = parent

	def sketch(self):
		"""Gets the sketch for this sketch contour."""
		# return self._instance.Sketch
		raise NotImplemented

	def de_select(self):
		"""Deselects the sketch contour."""
		# return self._instance.DeSelect
		raise NotImplemented

	def get_edges(self):
		"""Gets the edges in this sketch contour."""
		# return self._instance.GetEdges
		raise NotImplemented

	def get_edges_count(self):
		"""Gets the number of edges in this sketch contour."""
		# return self._instance.GetEdgesCount
		raise NotImplemented

	def get_sketch_segments(self):
		"""Gets the sketch segments for this sketch contour."""
		# return self._instance.GetSketchSegments
		raise NotImplemented

	def get_sketch_segments_count(self):
		"""Gets the number of sketch segments for this sketch contour."""
		# return self._instance.GetSketchSegmentsCount
		raise NotImplemented

	def i_get_edges(self, count):
		"""
		Gets the edges in this sketch contour.
		:param count: Number of edges
		"""
		# return self._instance.IGetEdges(count)
		raise NotImplemented

	def i_get_sketch_segments(self, count):
		"""
		Gets the sketch segments for this sketch contour.
		:param count: Number of sketch segments
		"""
		# return self._instance.IGetSketchSegments(count)
		raise NotImplemented

	def is_closed(self):
		"""Gets whether this sketch contour is open or closed."""
		# return self._instance.IsClosed
		raise NotImplemented

	def select(self, append, data):
		"""
		Selects the sketch contour and marks it.
		:param append: True appends the selection to the selection list, false replaces the selection list with this selection
		:param data: ISelectData object
		"""
		# return self._instance.Select2(append, data)
		raise NotImplemented

