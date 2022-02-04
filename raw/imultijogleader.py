# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader_members.html
class IMultiJogLeader:
	def __init__(self, parent=None):
		self._instance = parent

	def get_annotation(self):
		"""Gets the annotation for this multi-jog leader."""
		# return self._instance.GetAnnotation
		raise NotImplemented

	def get_arrow_head_at_index(self, index):
		"""
		Gets information for the specified arrow head.
		:param index: Index of the arrow head
		"""
		# return self._instance.GetArrowHeadAtIndex(index)
		raise NotImplemented

	def get_arrow_head_count(self):
		"""Gets the number of arrowheads in the multi-jog leader."""
		# return self._instance.GetArrowHeadCount
		raise NotImplemented

	def get_display_data(self):
		"""Gets the display data for this multi-jog leader."""
		# return self._instance.GetDisplayData
		raise NotImplemented

	def get_line_at_index(self, index):
		"""
		Gets the symbol information for the specified line.
		:param index: Index of the line 
		"""
		# return self._instance.GetLineAtIndex(index)
		raise NotImplemented

	def get_line_count(self):
		"""Gets the number of line items in this multi-jog leader."""
		# return self._instance.GetLineCount
		raise NotImplemented

	def get_next(self):
		"""Gets the next leader in the view."""
		# return self._instance.GetNext
		raise NotImplemented

	def i_get_annotation(self):
		"""Gets the annotation for this multi-jog leader."""
		# return self._instance.IGetAnnotation
		raise NotImplemented

	def i_get_arrow_head_at_index(self, index):
		"""
		Gets the information for the specified arrow head.
		:param index: Index of the arrow head where the index begins at 0
		"""
		# return self._instance.IGetArrowHeadAtIndex(index)
		raise NotImplemented

	def i_get_display_data(self):
		"""Gets the display data for this multi-jog leader."""
		# return self._instance.IGetDisplayData
		raise NotImplemented

	def i_get_line_at_index(self, index):
		"""
		Gets the symbol information for the specified line.
		:param index: Index of the line where the index begins at 0
		"""
		# return self._instance.IGetLineAtIndex(index)
		raise NotImplemented

	def i_get_next(self):
		"""Gets the next leader in the view."""
		# return self._instance.IGetNext
		raise NotImplemented

