# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.html
class IWeldSymbol:
	def __init__(self, parent=None):
		self._instance = parent

	def get_annotation(self):
		"""Gets the annotation for this weld symbol."""
		# return self._instance.GetAnnotation
		raise NotImplemented

	def get_arc_at_index(self, index):
		"""
		Gets information for the specified arc.
		:param index: Index of the arc where the index begins at 0
		"""
		# return self._instance.GetArcAtIndex(index)
		raise NotImplemented

	def get_arc_count(self):
		"""Gets the number of arcs in this weld symbol."""
		# return self._instance.GetArcCount
		raise NotImplemented

	def get_arrow_head_at_index(self, index):
		"""
		Gets information on the specified arrowhead in this weld symbol.
		:param index: Index of the arrow head where the index begins at 0
		"""
		# return self._instance.GetArrowHeadAtIndex(index)
		raise NotImplemented

	def get_arrow_head_count(self):
		"""Gets the number of arrow heads in the weld symbol."""
		# return self._instance.GetArrowHeadCount
		raise NotImplemented

	def get_arrow_head_info(self):
		"""Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
		# return self._instance.GetArrowHeadInfo
		raise NotImplemented

	def get_contour(self, top):
		"""
		Gets the contour settings for this weld symbol.
		:param top: If true, then get the contour setting for the portion of the symbol above the horizontal line; if false, then get the contour setting for the portion of the symbol below the horizontal line
		"""
		# return self._instance.GetContour(top)
		raise NotImplemented

	def get_field_weld(self):
		"""Gets the field or site weld property of this weld symbol."""
		# return self._instance.GetFieldWeld
		raise NotImplemented

	def get_leader_at_index(self, index):
		"""
		Gets information about the specified leader on this symbol.
		:param index: Index of leader
		"""
		# return self._instance.GetLeaderAtIndex(index)
		raise NotImplemented

	def get_leader_count(self):
		"""Gets the number of leaders on this symbol."""
		# return self._instance.GetLeaderCount
		raise NotImplemented

	def get_line_at_index(self, index):
		"""
		Gets information for the specified line.
		:param index: Index of the line where the index begins at 0
		"""
		# return self._instance.GetLineAtIndex(index)
		raise NotImplemented

	def get_line_count(self):
		"""Gets the number of line segments in this weld symbol."""
		# return self._instance.GetLineCount
		raise NotImplemented

	def get_next(self):
		"""Gets the next weld symbol in the drawing view."""
		# return self._instance.GetNext
		raise NotImplemented

	def get_peripheral(self):
		"""Gets whether this is a peripheral weld."""
		# return self._instance.GetPeripheral
		raise NotImplemented

	def get_process(self):
		"""Gets whether the indication of welding process flag is set on this weld symbol."""
		# return self._instance.GetProcess
		raise NotImplemented

	def get_process_reference(self):
		"""Gets whether there is a reference box around the indication of welding process text."""
		# return self._instance.GetProcessReference
		raise NotImplemented

	def get_stagger(self):
		"""Gets whether this weld symbol is a stagger weld."""
		# return self._instance.GetStagger
		raise NotImplemented

	def get_symmetric(self):
		"""Gets whether this weld symbol is a symmetric weld."""
		# return self._instance.GetSymmetric
		raise NotImplemented

	def get_text(self, which_text):
		"""
		Gets individual pieces of text from the weld symbol.
		:param which_text: Text to retrieve as defined in swWeldSymbolTextTypes_e 
		"""
		# return self._instance.GetText(which_text)
		raise NotImplemented

	def get_text_angle_at_index(self, index):
		"""
		Gets the text angle for the specified piece of text in this weld symbol.
		:param index: Index of the piece of text where the index begins at 0
		"""
		# return self._instance.GetTextAngleAtIndex(index)
		raise NotImplemented

	def get_text_at_index(self, index):
		"""
		Gets the specified text from this weld symbol.
		:param index: Index of the piece of text where the index begins at 0
		"""
		# return self._instance.GetTextAtIndex(index)
		raise NotImplemented

	def get_text_count(self):
		"""Gets the number of text items in the weld symbol."""
		# return self._instance.GetTextCount
		raise NotImplemented

	def get_text_height_at_index(self, index):
		"""
		Gets the text height for the specified piece of text in this weld symbol.
		:param index: Index of the desired piece of text where the index begins at 0
		"""
		# return self._instance.GetTextHeightAtIndex(index)
		raise NotImplemented

	def get_text_invert_at_index(self, index):
		"""
		Gets whether the text has been mirrored (reflected) about the X axis; any reflection is applied after text rotation.
		:param index: Index of the piece of text where the index begins at 0
		"""
		# return self._instance.GetTextInvertAtIndex(index)
		raise NotImplemented

	def get_text_position_at_index(self, index):
		"""
		Gets the text's offset relative to the note's text point.
		:param index: Index of the text where the index begins at 0
		"""
		# return self._instance.GetTextPositionAtIndex(index)
		raise NotImplemented

	def get_text_ref_position_at_index(self, index):
		"""
		Gets the specified text's reference position in this weld symbol (that is, upper left, lower left, center).
		:param index: Index of the piece of text where the index begins at 0
		"""
		# return self._instance.GetTextRefPositionAtIndex(index)
		raise NotImplemented

	def get_triangle_at_index(self, index):
		"""
		Gets the triangle at the specified index.
		:param index: Index of the triangle where the index begins at 0
		"""
		# return self._instance.GetTriangleAtIndex(index)
		raise NotImplemented

	def get_triangle_count(self):
		"""Gets the number of triangles in this weld symbol."""
		# return self._instance.GetTriangleCount
		raise NotImplemented

	def has_extra_leader(self):
		"""Gets whether this symbol has an extra leader."""
		# return self._instance.HasExtraLeader
		raise NotImplemented

	def i_get_annotation(self):
		"""Gets the annotation for this weld symbol."""
		# return self._instance.IGetAnnotation
		raise NotImplemented

	def i_get_arc_at_index(self, index):
		"""
		Gets information for the specified arc.
		:param index: Index of the arc where the index begins at 0
		"""
		# return self._instance.IGetArcAtIndex(index)
		raise NotImplemented

	def i_get_arrow_head_at_index(self, index):
		"""
		Gets information on the specified arrowhead in this weld symbol.
		:param index: Index of the arrow head where the index begins at
		"""
		# return self._instance.IGetArrowHeadAtIndex(index)
		raise NotImplemented

	def i_get_arrow_head_info(self):
		"""Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
		# return self._instance.IGetArrowHeadInfo
		raise NotImplemented

	def i_get_leader_at_index(self, index, point_count):
		"""
		Gets information about the specified leader on this symbol.
		:param index: Index of leader
		:param point_count: Number of (x,y,z) points returned in the array
		"""
		# return self._instance.IGetLeaderAtIndex(index, point_count)
		raise NotImplemented

	def i_get_line_at_index(self, index):
		"""
		Gets information for the specified line.
		:param index: Index of the line where the index begins at 0
		"""
		# return self._instance.IGetLineAtIndex(index)
		raise NotImplemented

	def i_get_next(self):
		"""Gets the next weld symbol in the view."""
		# return self._instance.IGetNext
		raise NotImplemented

	def i_get_text_position_at_index(self, index):
		"""
		Gets the text item's offset relative to note's text point.
		:param index: Index of the piece of text where the index begins at 0
		"""
		# return self._instance.IGetTextPositionAtIndex(index)
		raise NotImplemented

	def i_get_triangle_at_index(self, index):
		"""
		Gets the triangle at the specified index.
		:param index: Index of the triangle where the index begins at 0
		"""
		# return self._instance.IGetTriangleAtIndex(index)
		raise NotImplemented

	def is_attached(self):
		"""Gets whether this symbol is attached."""
		# return self._instance.IsAttached
		raise NotImplemented

	def set_field_weld(self, field_weld):
		"""
		Sets the field or site weld property of this weld symbol.
		:param field_weld: Value indicating whether this is to be a field or site weld, and, if so, whether the flag points up or down as defined in swWeldSymbolField_e 
		"""
		# return self._instance.SetFieldWeld(field_weld)
		raise NotImplemented

	def set_peripheral(self, peripheral):
		"""
		Sets the peripheral property of this weld symbol.
		:param peripheral: True if a peripheral weld, false if not
		"""
		# return self._instance.SetPeripheral(peripheral)
		raise NotImplemented

	def set_process(self, process, text, reference):
		"""
		Sets the values related to the indication of welding process for this weld symbol.
		:param process: True to set the indication of welding process flag, false to not
		:param text: Text related to the indication of welding process
		:param reference: True to place a reference box around the process text, false to not
		"""
		# return self._instance.SetProcess(process, text, reference)
		raise NotImplemented

	def set_stagger(self, stagger):
		"""
		Sets the stagger property of this weld symbol.
		:param stagger: True if this is a stagger weld, false if not
		"""
		# return self._instance.SetStagger(stagger)
		raise NotImplemented

	def set_symmetric(self, symmetric):
		"""
		Sets whether this weld symbol is a symmetric weld.
		:param symmetric: Value indicating whether this should be a symmetric weld, and if not, whether the dashed line is above or below the horizontal line as defined in swWeldSymbolSymmetric_e 
		"""
		# return self._instance.SetSymmetric(symmetric)
		raise NotImplemented

	def set_text(self, top, left, symbol, right, stagger, contour):
		"""
		Sets the text and symbols in the upper or lower portion of the weld symbol.
		:param top: True to set the text in the portion of the symbol above the horizontal line, false to set the text in the portion of the symbol below the horizontal line
		:param left: Text to the left of the weld symbol
		:param symbol: Text representing the weld symbol (see Remarks)
		:param right: Text to the right of the weld symbol
		:param stagger: Text to the right of the stagger symbol (see Remarks)
		:param contour: Contour setting as defined in swWeldSymbolContourTypes_e (see Remarks)
		"""
		# return self._instance.SetText(top, left, symbol, right, stagger, contour)
		raise NotImplemented

