# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.html
class ITitleBlock:
	def __init__(self, parent=None):
		self._instance = parent

	def get_extents(self, x_upper_left, y_upper_left, x_lower_right, y_lower_right):
		"""
		Gets the coordinates on the drawing sheet format that define the extents of the title block.
		:param x_upper_left: X upper-left coordinate
		:param y_upper_left: Y upper-left coordinate
		:param x_lower_right: X lower-right coordinate
		:param y_lower_right: Y lower-right coordinate
		"""
		# return self._instance.GetExtents(x_upper_left, y_upper_left, x_lower_right, y_lower_right)
		raise NotImplemented

	def get_feature(self):
		"""Gets the feature for this title block."""
		# return self._instance.GetFeature
		raise NotImplemented

	def get_note_count(self):
		"""Gets the number of notes in this title block."""
		# return self._instance.GetNoteCount
		raise NotImplemented

	def get_notes(self):
		"""Gets the notes in this title block."""
		# return self._instance.GetNotes
		raise NotImplemented

	def i_get_notes(self, count):
		"""
		Gets the notes in this title block.
		:param count: Number of notes in this title block
		"""
		# return self._instance.IGetNotes(count)
		raise NotImplemented

	def set_extents(self, x_upper_left, y_upper_left, x_lower_right, y_lower_right):
		"""
		Sets the coordinates on the drawing sheet format that define the extens of the title blcok.
		:param x_upper_left: X upper-left coordinate
		:param y_upper_left: Y upper-left coordinate
		:param x_lower_right: X lower-right coordinate
		:param y_lower_right: Y lower-right coordinate
		"""
		# return self._instance.SetExtents(x_upper_left, y_upper_left, x_lower_right, y_lower_right)
		raise NotImplemented

