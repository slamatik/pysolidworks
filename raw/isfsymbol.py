# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.html
class ISFSymbol:
	def __init__(self, parent=None):
		self._instance = parent

	def g_o_s_t_default_symbol(self):
		"""Gets whether the GOST Add default symbol option is set."""
		# return self._instance.GOSTDefaultSymbol
		raise NotImplemented

	def g_o_s_t_notation(self):
		"""Gets whether the GOST Use for notation option is set."""
		# return self._instance.GOSTNotation
		raise NotImplemented

	def orientation(self):
		"""Gets whether the orientation of this surface finish symbol is relative to the model or entity to which it is attached."""
		# return self._instance.Orientation
		raise NotImplemented

	def get_angle(self):
		"""Gets the angle of this surface finish symbol."""
		# return self._instance.GetAngle
		raise NotImplemented

	def get_annotation(self):
		"""Gets the annotation for this surface finish symbol."""
		# return self._instance.GetAnnotation
		raise NotImplemented

	def get_arc_at_index(self, index):
		"""
		Gets information for the specified arc.
		:param index: Index of the arc where the index begins at 0
		"""
		# return self._instance.GetArcAtIndex(index)
		raise NotImplemented

	def get_arc_count(self):
		"""Gets the number of arcs in this surface finish symbol."""
		# return self._instance.GetArcCount
		raise NotImplemented

	def get_arrow_head_at_index(self, index):
		"""
		Gets information on the specified arrow head in this surface finish symbol.
		:param index: Index of the arrow head where the index begins at 0
		"""
		# return self._instance.GetArrowHeadAtIndex(index)
		raise NotImplemented

	def get_arrow_head_count(self):
		"""Gets the number of arrow heads in the surface finish symbol."""
		# return self._instance.GetArrowHeadCount
		raise NotImplemented

	def get_arrow_head_info(self):
		"""Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
		# return self._instance.GetArrowHeadInfo
		raise NotImplemented

	def get_direction_of_lay(self):
		"""Gets the direction of lay value for this surface finish symbol."""
		# return self._instance.GetDirectionOfLay
		raise NotImplemented

	def get_leader_at_index(self, index):
		"""
		Gets information about the specified leader on this surface finish symbol.
		:param index: Index of leader
		"""
		# return self._instance.GetLeaderAtIndex(index)
		raise NotImplemented

	def get_leader_count(self):
		"""Gets the number of leaders on this surface finish symbol."""
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
		"""Gets number of line items in this surface finish symbol."""
		# return self._instance.GetLineCount
		raise NotImplemented

	def get_next(self):
		"""Gets the next surface finish symbol in the view."""
		# return self._instance.GetNext
		raise NotImplemented

	def get_symbol(self):
		"""Gets the type of symbol for this surface finish symbol."""
		# return self._instance.GetSymbol
		raise NotImplemented

	def get_symbol_all_around(self):
		"""Gets whether this symbol is All Around or Local for this surface finish symbol."""
		# return self._instance.GetSymbolAllAround
		raise NotImplemented

	def get_symbol_surface_texture(self):
		"""Gets the symbol surface texture type for this surface finish symbol."""
		# return self._instance.GetSymbolSurfaceTexture
		raise NotImplemented

	def get_text(self, which_one):
		"""
		Gets the specified text string in this surface finish symbol.
		:param which_one: Text item to get as defined in  swSurfaceFinishSymbolText_e
		"""
		# return self._instance.GetText(which_one)
		raise NotImplemented

	def get_text_angle_at_index(self, index):
		"""
		Gets the text angle for the specified text in this surface finish symbol.
		:param index: Index of the text where the index begins at 0
		"""
		# return self._instance.GetTextAngleAtIndex(index)
		raise NotImplemented

	def get_text_at_index(self, index):
		"""
		Gets the specified text string from this surface finish symbol.
		:param index: Index of the text where the index begins at 0
		"""
		# return self._instance.GetTextAtIndex(index)
		raise NotImplemented

	def get_text_count(self):
		"""Gets the number of text items in the surface finish symbol."""
		# return self._instance.GetTextCount
		raise NotImplemented

	def get_text_font_at_index(self, index):
		"""
		Gets the font used by the specified text item in this surface finish symbol.
		:param index: Index of the text where the index begins at 0
		"""
		# return self._instance.GetTextFontAtIndex(index)
		raise NotImplemented

	def get_text_height_at_index(self, index):
		"""
		Gets the text height for the specified piece of text in this surface finish symbol.
		:param index: Index of the text where the index begins at 0
		"""
		# return self._instance.GetTextHeightAtIndex(index)
		raise NotImplemented

	def get_text_invert_at_index(self, index):
		"""
		Gets the specified text item's invert flag.
		:param index: Index of the text where the index begins at 0
		"""
		# return self._instance.GetTextInvertAtIndex(index)
		raise NotImplemented

	def get_text_position_at_index(self, index):
		"""
		Gets the text item's offset relative to note's text point.
		:param index: Index of the text where the index begins at 0
		"""
		# return self._instance.GetTextPositionAtIndex(index)
		raise NotImplemented

	def get_text_ref_position_at_index(self, index):
		"""
		Gets the specified text item's reference position in this note, for example, upper left, lower left, center, and so on.
		:param index: Index of the text where the index begins at 0
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
		"""Gets the number of triangles in this surface finish symbol."""
		# return self._instance.GetTriangleCount
		raise NotImplemented

	def has_extra_leader(self):
		"""Gets whether this surface finish symbol has an extra leader line."""
		# return self._instance.HasExtraLeader
		raise NotImplemented

	def i_get_annotation(self):
		"""Gets the annotation for this surface finish symbol."""
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
		Gets information on the specified arrow head in this surface finish symbol.
		:param index: Index of the arrow head where the index begins at 0
		"""
		# return self._instance.IGetArrowHeadAtIndex(index)
		raise NotImplemented

	def i_get_arrow_head_info(self):
		"""Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
		# return self._instance.IGetArrowHeadInfo
		raise NotImplemented

	def i_get_leader_at_index(self, index, point_count):
		"""
		Gets information about the specified leader on this surface finish symbol.
		:param index: Index of the line where the index begins at 0
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
		"""Gets the next surface finish symbol in the view."""
		# return self._instance.IGetNext
		raise NotImplemented

	def i_get_text_position_at_index(self, index):
		"""
		Gets the text item's offset relative to note's text point.
		:param index: Index of the text where the index begins at 0
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
		"""Gets whether the leader line for this surface finish symbol is attached."""
		# return self._instance.IsAttached
		raise NotImplemented

	def set_angle(self, angle):
		"""
		Sets the angle for this surface finish symbol.
		:param angle: Angle in radians
		"""
		# return self._instance.SetAngle(angle)
		raise NotImplemented

	def set_direction_of_lay(self, direction):
		"""
		Sets the direction of lay value for this surface finish symbol.
		:param direction: Direction of lay value as defined in swSFLaySym_e 
		"""
		# return self._instance.SetDirectionOfLay(direction)
		raise NotImplemented

	def set_symbol(self, symbol, surface_texture, all_around):
		"""
		Sets the type of symbol for this surface finish symbol.
		:param symbol: Type of symbol as defined in swSFSymType_e
		:param surface_texture: Symbol surface text type as defined in swSFSymType_e
		:param all_around: True if symbol is All Around, false if symbol is Local
		"""
		# return self._instance.SetSymbol(symbol, surface_texture, all_around)
		raise NotImplemented

	def set_text(self, which_one, text):
		"""
		Sets a text string in this surface finish symbol.
		:param which_one: Text item to set as defined in swSurfaceFinishSymbolText_e 
		:param text: Text string
		"""
		# return self._instance.SetText(which_one, text)
		raise NotImplemented

