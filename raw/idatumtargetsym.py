# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym_members.html
class IDatumTargetSym:
	def __init__(self, parent=None):
		self._instance = parent

	def get_annotation(self):
		"""Gets the IAnnotation object for this specific datum target symbol."""
		# return self._instance.GetAnnotation
		raise NotImplemented

	def get_arc_at_index(self, index):
		"""
		Gets information for the specified arc for this datum target symbol.
		:param index: Index of the arc; index begins at 0
		"""
		# return self._instance.GetArcAtIndex(index)
		raise NotImplemented

	def get_arc_count(self):
		"""Gets the number of arc items in this datum target symbol."""
		# return self._instance.GetArcCount
		raise NotImplemented

	def get_arrow_head_at_index(self, index):
		"""
		Gets information on the specified arrow head in this datum target symbol.
		:param index: Index of the arrow head; index begins at 0
		"""
		# return self._instance.GetArrowHeadAtIndex(index)
		raise NotImplemented

	def get_arrow_head_count(self):
		"""Gets the number of arrow heads in the datum target symbol."""
		# return self._instance.GetArrowHeadCount
		raise NotImplemented

	def get_datum_reference_label(self, which_one):
		"""
		Gets the specified datum target reference label.
		:param which_one: 0-based index indicating the datum reference label to get
		"""
		# return self._instance.GetDatumReferenceLabel(which_one)
		raise NotImplemented

	def get_display_size_outside(self):
		"""Gets whether the datum target area size is displayed inside or outside of the symbol."""
		# return self._instance.GetDisplaySizeOutside
		raise NotImplemented

	def get_display_symbol(self):
		"""Gets whether the datum target symbol is displayed."""
		# return self._instance.GetDisplaySymbol
		raise NotImplemented

	def get_display_target_area(self):
		"""Gets whether the datum target area is displayed."""
		# return self._instance.GetDisplayTargetArea
		raise NotImplemented

	def get_line_at_index(self, index):
		"""
		Gets information for the specified line.
		:param index: Index of the line; index begins at 0
		"""
		# return self._instance.GetLineAtIndex(index)
		raise NotImplemented

	def get_line_count(self):
		"""Gets the number of line items in this datum target symbol."""
		# return self._instance.GetLineCount
		raise NotImplemented

	def get_next(self):
		"""Gets the next datum target symbol in the view."""
		# return self._instance.GetNext
		raise NotImplemented

	def get_target_area_size(self, which_one):
		"""
		Gets the size of the datum target symbol area.
		:param which_one: 0-based index indicating which size value to get (see Remarks)
		"""
		# return self._instance.GetTargetAreaSize(which_one)
		raise NotImplemented

	def get_target_shape(self):
		"""Gets the shape or style of the datum target area."""
		# return self._instance.GetTargetShape
		raise NotImplemented

	def get_text_angle_at_index(self, index):
		"""
		Gets the text angle for the specified text in this datum target symbol.
		:param index: Index of the text; index begins at 0
		"""
		# return self._instance.GetTextAngleAtIndex(index)
		raise NotImplemented

	def get_text_at_index(self, index):
		"""
		Gets the specified text string from this datum target symbol.
		:param index: Index of the text; index begins at 0
		"""
		# return self._instance.GetTextAtIndex(index)
		raise NotImplemented

	def get_text_count(self):
		"""Gets the number of text items in the datum target symbol."""
		# return self._instance.GetTextCount
		raise NotImplemented

	def get_text_height_at_index(self, index):
		"""
		Gets the height of the text for the specified text in this datum target symbol.
		:param index: Index of the text; index begins at 0
		"""
		# return self._instance.GetTextHeightAtIndex(index)
		raise NotImplemented

	def get_text_invert_at_index(self, index):
		"""
		Gets the invert flag for the specified text item.
		:param index: Index of the text; index begins at 0
		"""
		# return self._instance.GetTextInvertAtIndex(index)
		raise NotImplemented

	def get_text_position_at_index(self, index):
		"""
		Gets the offset for the text item relative to the text point of the note.
		:param index: Index of the text index begins at 0
		"""
		# return self._instance.GetTextPositionAtIndex(index)
		raise NotImplemented

	def get_text_ref_position_at_index(self, index):
		"""
		Gets the reference position of the specified text item in this datum target symbol.
		:param index: Index of the text; index begins at 0
		"""
		# return self._instance.GetTextRefPositionAtIndex(index)
		raise NotImplemented

	def get_triangle_at_index(self, index):
		"""
		Gets the triangle at the specified index.
		:param index: Index of the triangle; index begins at 0
		"""
		# return self._instance.GetTriangleAtIndex(index)
		raise NotImplemented

	def get_triangle_count(self):
		"""Gets the number of triangles in this datum target symbol."""
		# return self._instance.GetTriangleCount
		raise NotImplemented

	def i_get_annotation(self):
		"""Gets the IAnnotation object for this specific datum target symbol."""
		# return self._instance.IGetAnnotation
		raise NotImplemented

	def i_get_arc_at_index(self, index):
		"""
		Gets information for the specified arc for this datum target symbol.
		:param index: Index of the arc; index begins at 0
		"""
		# return self._instance.IGetArcAtIndex(index)
		raise NotImplemented

	def i_get_arrow_head_at_index(self, index):
		"""
		Gets information on the specified arrow head in this datum target symbol.
		:param index: Index of the arrow head; index begins at 0
		"""
		# return self._instance.IGetArrowHeadAtIndex(index)
		raise NotImplemented

	def i_get_line_at_index(self, index):
		"""
		Gets information for the specified line.
		:param index: Index of the line; index begins at 0
		"""
		# return self._instance.IGetLineAtIndex(index)
		raise NotImplemented

	def i_get_next(self):
		"""Gets the next datum target symbol in the view."""
		# return self._instance.IGetNext
		raise NotImplemented

	def i_get_text_position_at_index(self, index):
		"""
		Gets the offset for the text item relative to the text point of the note.
		:param index: Index of the text; index begins at 0
		"""
		# return self._instance.IGetTextPositionAtIndex(index)
		raise NotImplemented

	def i_get_triangle_at_index(self, index):
		"""
		Gets the triangle at the specified index.
		:param index: Index of the triangle; index begins at 0
		"""
		# return self._instance.IGetTriangleAtIndex(index)
		raise NotImplemented

	def set_datum_reference_label(self, which_one, text):
		"""
		Sets the specified datum target reference label.
		:param which_one: 0-based index indicating the datum reference label to set
		:param text: Datum reference label
		"""
		# return self._instance.SetDatumReferenceLabel(which_one, text)
		raise NotImplemented

	def set_datum_target_horizontal(self, moveable_datum_direction, lock_leader, lock_leader_angle):
		"""
		Sets this datum target to moveable horizontal.
		:param moveable_datum_direction: Moveable datum direction as defined in swMoveableDatumDirection_e
		:param lock_leader: True to lock the leader, false to not
		:param lock_leader_angle: Angle of locked leader; valid only if LockLeader is set to true
		"""
		# return self._instance.SetDatumTargetHorizontal(moveable_datum_direction, lock_leader, lock_leader_angle)
		raise NotImplemented

	def set_datum_target_not_moveable(self):
		"""Sets this datum target to not moveable."""
		# return self._instance.SetDatumTargetNotMoveable
		raise NotImplemented

	def set_datum_target_rotational(self, moveable_datum_direction, lock_leader, lock_leader_angle, geometry_ref, ref_geometry_error):
		"""
		Sets this datum target to moveable rotational.
		:param moveable_datum_direction: Moveable datum direction as defined in swMoveableDatumDirection_e
		:param lock_leader: True to lock the leader, false to not
		:param lock_leader_angle: Angle of locked leader; valid only if LockLeader is set to true
		:param geometry_ref: True to use a geometry reference, false to not; true is valid only if MoveableDatumDirection is set to swMoveableDatumDirection_e.swMoveableDatumDirectionBySelection
		:param ref_geometry_error: Reference geometry error as defined in swRefGeometryError_e
		"""
		# return self._instance.SetDatumTargetRotational(moveable_datum_direction, lock_leader, lock_leader_angle, geometry_ref, ref_geometry_error)
		raise NotImplemented

	def set_display(self, symbol, target_area, size_outside):
		"""
		Sets the display characteristics of the datum target symbol.
		:param symbol: True displays the datum target symbol part of the annotation, false hides it
		:param target_area: True displays the datum target area part of the annotation, false hides it
		:param size_outside: True displays the datum target area size outside of the symbol, false displays itinside
		"""
		# return self._instance.SetDisplay(symbol, target_area, size_outside)
		raise NotImplemented

	def set_target_area(self, shape, size1, size2):
		"""
		Sets the datum target area style and size.
		:param shape: Target area shape or style as defined in swDatumTargetAreaShape_e
		:param size1: Target area diameter or width (see Remarks)
		:param size2: Target area height (see Remarks)
		"""
		# return self._instance.SetTargetArea(shape, size1, size2)
		raise NotImplemented

