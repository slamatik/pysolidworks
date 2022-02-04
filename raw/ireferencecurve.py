# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve_members.html
class IReferenceCurve:
	def __init__(self, parent=None):
		self._instance = parent

	def get_first_segment(self):
		"""Gets the first curve segment in a reference curve feature."""
		# return self._instance.GetFirstSegment
		raise NotImplemented

	def get_next_segment(self):
		"""Gets the next curve segment in the reference curve feature."""
		# return self._instance.GetNextSegment
		raise NotImplemented

	def get_segment_count(self):
		"""Gets the number of curve segments in a reference curve feature."""
		# return self._instance.GetSegmentCount
		raise NotImplemented

	def get_segments(self):
		"""Gets the segments in this reference curve."""
		# return self._instance.GetSegments
		raise NotImplemented

	def i_get_first_segment(self):
		"""Gets the first curve segment in a reference curve feature."""
		# return self._instance.IGetFirstSegment
		raise NotImplemented

	def i_get_next_segment(self):
		"""Gets the next curve segment in the reference curve feature."""
		# return self._instance.IGetNextSegment
		raise NotImplemented

	def i_get_segments(self, num_segments):
		"""
		Gets the segments in this reference curve.
		:param num_segments: Number of segments in the reference curve
		"""
		# return self._instance.IGetSegments(num_segments)
		raise NotImplemented

	def set_color(self, color_in):
		"""
		Sets the color of the reference curve feature.
		:param color_in: COLORREF value of the color 
		"""
		# return self._instance.SetColor(color_in)
		raise NotImplemented

	def set_visible(self, visible):
		"""
		Hides or shows the reference curve feature.
		:param visible: True for visible, false for hidden
		"""
		# return self._instance.SetVisible(visible)
		raise NotImplemented

