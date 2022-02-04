# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.html
class IDisplayData:
	def __init__(self, parent=None):
		self._instance = parent

	def get_arc_at_index(self, index):
		"""
		Gets information for the specified arc.
		:param index: Index of the desired arc where the index begins at zero
		"""
		# return self._instance.GetArcAtIndex2(index)
		raise NotImplemented

	def get_arc_count(self):
		"""Gets the number of arc items."""
		# return self._instance.GetArcCount
		raise NotImplemented

	def get_arrow_head_at_index(self, index):
		"""
		Gets information on the specified arrow head.
		:param index: Index of the desired arrow head where the index begins at zero
		"""
		# return self._instance.GetArrowHeadAtIndex2(index)
		raise NotImplemented

	def get_arrow_head_count(self):
		"""Gets the number of arrow heads."""
		# return self._instance.GetArrowHeadCount
		raise NotImplemented

	def get_ellipse_at_index(self, index):
		"""
		Gets information for the specified ellipse.
		:param index: Index of the desired ellipse where the index begins at zero
		"""
		# return self._instance.GetEllipseAtIndex2(index)
		raise NotImplemented

	def get_ellipse_count(self):
		"""Gets the number of line ellipses."""
		# return self._instance.GetEllipseCount
		raise NotImplemented

	def get_line_at_index(self, index):
		"""
		Gets information for the specified line.
		:param index: Index of the desired line where the index begins at 0
		"""
		# return self._instance.GetLineAtIndex3(index)
		raise NotImplemented

	def get_line_count(self):
		"""Gets the number of lines."""
		# return self._instance.GetLineCount
		raise NotImplemented

	def get_parabola_at_index(self, index):
		"""
		Gets information for the specified parabola.
		:param index: Index of parabola
		"""
		# return self._instance.GetParabolaAtIndex(index)
		raise NotImplemented

	def get_parabola_count(self):
		"""Gets the number of parabolas."""
		# return self._instance.GetParabolaCount
		raise NotImplemented

	def get_point_at_index(self, index):
		"""
		Gets information about the specified point.
		:param index: Index of the point
		"""
		# return self._instance.GetPointAtIndex(index)
		raise NotImplemented

	def get_point_count(self):
		"""Gets the number of points."""
		# return self._instance.GetPointCount
		raise NotImplemented

	def get_polygon_at_index(self, index):
		"""
		Gets information for the specified polygon.
		:param index: Index of the desired polygon where the index begins at zero
		"""
		# return self._instance.GetPolygonAtIndex(index)
		raise NotImplemented

	def get_polygon_count(self):
		"""Gets the number of polygons."""
		# return self._instance.GetPolygonCount
		raise NotImplemented

	def get_polygon_size_at_index(self, index):
		"""
		Gets the number of array elements returned by IDisplayData::GetPolygonAtIndex and IDisplayData::IGetPolygonAtIndex.
		:param index: Index for the polygon
		"""
		# return self._instance.GetPolygonSizeAtIndex(index)
		raise NotImplemented

	def get_polyline_at_index(self, index):
		"""
		Gets information for the specified polyline.
		:param index: Index of the desired polyline where the index begins at zero
		"""
		# return self._instance.GetPolylineAtIndex2(index)
		raise NotImplemented

	def get_poly_line_count(self):
		"""Gets the number of polylines."""
		# return self._instance.GetPolyLineCount
		raise NotImplemented

	def get_polyline_size_at_index(self, index):
		"""
		Gets the number of array elements returned by IDisplayData::GetPolylineAtIndex2 and IDisplayData::IGetPolylineAtIndex2.
		:param index: Index of the desired polyline where the index begins at zero
		"""
		# return self._instance.GetPolylineSizeAtIndex2(index)
		raise NotImplemented

	def get_text_angle_at_index(self, index):
		"""
		Gets the text angle for the specified piece of text.
		:param index: Zero-based index of the desired piece of text
		"""
		# return self._instance.GetTextAngleAtIndex(index)
		raise NotImplemented

	def get_text_at_index(self, index):
		"""
		Gets the specified text string.
		:param index: Zero-based index of the desired piece of text
		"""
		# return self._instance.GetTextAtIndex(index)
		raise NotImplemented

	def get_text_count(self):
		"""Gets the number of text items."""
		# return self._instance.GetTextCount
		raise NotImplemented

	def get_text_font_at_index(self, index):
		"""
		Gets the specified text font.
		:param index: Zero-based index of the desired piece of text
		"""
		# return self._instance.GetTextFontAtIndex(index)
		raise NotImplemented

	def get_text_height_at_index(self, index):
		"""
		Gets the text height for the specified piece of text .
		:param index: Zero-based index of the desired piece of text
		"""
		# return self._instance.GetTextHeightAtIndex(index)
		raise NotImplemented

	def get_text_in_box_height_at_index(self, index):
		"""
		Gets the text-in-box height of the specified text and table cell in a table annotation.
		:param index: Zero-based index of the text and table cell to examine
		"""
		# return self._instance.GetTextInBoxHeightAtIndex(index)
		raise NotImplemented

	def get_text_in_box_style_at_index(self, index):
		"""
		Gets the text-in-box style of the specified text and table cell in a table annotation.
		:param index: Zero-based index of the text and table cell to examine
		"""
		# return self._instance.GetTextInBoxStyleAtIndex(index)
		raise NotImplemented

	def get_text_in_box_width_at_index(self, index):
		"""
		Gets the text-in-box width of the specified text and table cell in the table annotation.
		:param index: Zero-based index of the text and table cell to examine
		"""
		# return self._instance.GetTextInBoxWidthAtIndex(index)
		raise NotImplemented

	def get_text_invert_at_index(self, index):
		"""
		Gets the specified text's invert flag.
		:param index: Zero-based index of the desired piece of text
		"""
		# return self._instance.GetTextInvertAtIndex(index)
		raise NotImplemented

	def get_text_line_spacing_at_index(self, index):
		"""
		Gets the line spacing for this text.
		:param index: Zero-based index of the text
		"""
		# return self._instance.GetTextLineSpacingAtIndex(index)
		raise NotImplemented

	def get_text_plane_at_index(self, index):
		"""
		Gets the rotation matrix of the specified text relative to the X-Y plane of the model.
		:param index: Zero-based index of the text whose plane rotation matrix to retrieve (see Remarks)
		"""
		# return self._instance.GetTextPlaneAtIndex(index)
		raise NotImplemented

	def get_text_position_at_index(self, index):
		"""
		Gets the text item offset relative to the note text point.
		:param index: Zero-based index of the desired piece of text
		"""
		# return self._instance.GetTextPositionAtIndex(index)
		raise NotImplemented

	def get_text_ref_position_at_index(self, index):
		"""
		Gets the specified text item reference position.
		:param index: Zero-based index of the desired piece of text
		"""
		# return self._instance.GetTextRefPositionAtIndex(index)
		raise NotImplemented

	def get_triangle_at_index(self, index):
		"""
		Gets the triangle at the specified index.
		:param index: Zero-based index of the desired triangle
		"""
		# return self._instance.GetTriangleAtIndex(index)
		raise NotImplemented

	def get_triangle_count(self):
		"""Gets the number of triangles."""
		# return self._instance.GetTriangleCount
		raise NotImplemented

	def i_get_arc_at_index(self, index):
		"""
		Gets information for the specified arc.
		:param index: Index of the desired arc where the index begins at zero
		"""
		# return self._instance.IGetArcAtIndex2(index)
		raise NotImplemented

	def i_get_arrow_head_at_index(self, index):
		"""
		Gets information on the specified arrow head.
		:param index: Index of the desired arrow head where the index begins at zero
		"""
		# return self._instance.IGetArrowHeadAtIndex(index)
		raise NotImplemented

	def i_get_ellipse_at_index(self, index):
		"""
		Gets information for the specified ellipse.
		:param index: Index of the desired ellipse where the index begins at zero
		"""
		# return self._instance.IGetEllipseAtIndex2(index)
		raise NotImplemented

	def i_get_line_at_index(self, index):
		"""
		Gets information for the specified line.
		:param index: Index of the desired line where the index begins at 0
		"""
		# return self._instance.IGetLineAtIndex3(index)
		raise NotImplemented

	def i_get_parabola_at_index(self, index):
		"""
		Gets the information for the specified parabola.
		:param index: GetPolygonCount MethodIndex of parabola
		"""
		# return self._instance.IGetParabolaAtIndex(index)
		raise NotImplemented

	def i_get_point_at_index(self, index):
		"""
		Gets information about the specified point.
		:param index: Index of the point
		"""
		# return self._instance.IGetPointAtIndex(index)
		raise NotImplemented

	def i_get_polygon_at_index(self, index):
		"""
		Gets information for the specified polygon.
		:param index: Index of the desired polygon where the index begins at zero
		"""
		# return self._instance.IGetPolygonAtIndex(index)
		raise NotImplemented

	def i_get_polyline_at_index(self, index):
		"""
		Gets information for the specified polyline.
		:param index: Index of the desired polyline where the index begins at zero
		"""
		# return self._instance.IGetPolylineAtIndex2(index)
		raise NotImplemented

	def i_get_text_position_at_index(self, index):
		"""
		Gets the text item offset relative to the note text point.
		:param index: Index of the desired piece of text where the index begins at zero
		"""
		# return self._instance.IGetTextPositionAtIndex(index)
		raise NotImplemented

	def i_get_triangle_at_index(self, index):
		"""
		Gets the triangle at the specified index.
		:param index: Index of the desired triangle where the index begins at zero
		"""
		# return self._instance.IGetTriangleAtIndex(index)
		raise NotImplemented

