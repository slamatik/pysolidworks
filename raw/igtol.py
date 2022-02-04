# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.html
class IGtol:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the rotation angle of this symbol."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the rotation angle of this symbol."""
		self._instance.Angle = value

	@property
	def delete_below_frame_text_at(self):
		"""Deletes the specified text line in the below frame of this GTol."""
		return self._instance.DeleteBelowFrameTextAt

	@delete_below_frame_text_at.setter
	def delete_below_frame_text_at(self, value):
		"""Deletes the specified text line in the below frame of this GTol."""
		self._instance.DeleteBelowFrameTextAt = value

	@property
	def get_all_around(self):
		"""Gets whether this GTol uses an All Around leader."""
		return self._instance.GetAllAround

	@get_all_around.setter
	def get_all_around(self, value):
		"""Gets whether this GTol uses an All Around leader."""
		self._instance.GetAllAround = value

	@property
	def get_all_around_this_side(self):
		"""Gets whether this GTol uses an All Around This Side leader."""
		return self._instance.GetAllAroundThisSide

	@get_all_around_this_side.setter
	def get_all_around_this_side(self, value):
		"""Gets whether this GTol uses an All Around This Side leader."""
		self._instance.GetAllAroundThisSide = value

	@property
	def get_all_over_this_side(self):
		"""Gets whether this GTol uses an All Over This Side leader."""
		return self._instance.GetAllOverThisSide

	@get_all_over_this_side.setter
	def get_all_over_this_side(self, value):
		"""Gets whether this GTol uses an All Over This Side leader."""
		self._instance.GetAllOverThisSide = value

	@property
	def get_annotation(self):
		"""Gets the annotation for this specific Gtol."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the annotation for this specific Gtol."""
		self._instance.GetAnnotation = value

	@property
	def get_arc_at_index(self):
		"""Gets information about the specified arc."""
		return self._instance.GetArcAtIndex

	@get_arc_at_index.setter
	def get_arc_at_index(self, value):
		"""Gets information about the specified arc."""
		self._instance.GetArcAtIndex = value

	@property
	def get_arc_count(self):
		"""Gets the number of arcs in this GTol."""
		return self._instance.GetArcCount

	@get_arc_count.setter
	def get_arc_count(self, value):
		"""Gets the number of arcs in this GTol."""
		self._instance.GetArcCount = value

	@property
	def get_arrow_head_at_index(self):
		"""Gets information on the specified arrow head in this GTol."""
		return self._instance.GetArrowHeadAtIndex

	@get_arrow_head_at_index.setter
	def get_arrow_head_at_index(self, value):
		"""Gets information on the specified arrow head in this GTol."""
		self._instance.GetArrowHeadAtIndex = value

	@property
	def get_arrow_head_count(self):
		"""Gets the number of arrow heads in the GTol."""
		return self._instance.GetArrowHeadCount

	@get_arrow_head_count.setter
	def get_arrow_head_count(self, value):
		"""Gets the number of arrow heads in the GTol."""
		self._instance.GetArrowHeadCount = value

	@property
	def get_arrow_head_info(self):
		"""Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
		return self._instance.GetArrowHeadInfo

	@get_arrow_head_info.setter
	def get_arrow_head_info(self, value):
		"""Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
		self._instance.GetArrowHeadInfo = value

	@property
	def get_attach_pos(self):
		"""Gets the attachment point of the GTol."""
		return self._instance.GetAttachPos

	@get_attach_pos.setter
	def get_attach_pos(self, value):
		"""Gets the attachment point of the GTol."""
		self._instance.GetAttachPos = value

	@property
	def get_below_frame_text_at(self):
		"""Gets the specified line of text in this GTol."""
		return self._instance.GetBelowFrameTextAt

	@get_below_frame_text_at.setter
	def get_below_frame_text_at(self, value):
		"""Gets the specified line of text in this GTol."""
		self._instance.GetBelowFrameTextAt = value

	@property
	def get_below_frame_text_line_count(self):
		"""Gets the number of text lines in the below frame of this GTol."""
		return self._instance.GetBelowFrameTextLineCount

	@get_below_frame_text_line_count.setter
	def get_below_frame_text_line_count(self, value):
		"""Gets the number of text lines in the below frame of this GTol."""
		self._instance.GetBelowFrameTextLineCount = value

	@property
	def get_between_two_points(self):
		"""Gets whether the between two points symbol is being used."""
		return self._instance.GetBetweenTwoPoints

	@get_between_two_points.setter
	def get_between_two_points(self, value):
		"""Gets whether the between two points symbol is being used."""
		self._instance.GetBetweenTwoPoints = value

	@property
	def get_between_two_points_text(self):
		"""Gets the text used in the between two points symbol."""
		return self._instance.GetBetweenTwoPointsText

	@get_between_two_points_text.setter
	def get_between_two_points_text(self, value):
		"""Gets the text used in the between two points symbol."""
		self._instance.GetBetweenTwoPointsText = value

	@property
	def get_composite_frame(self):
		"""Gets whether the GTol frame with the specified index is part of a composite frame."""
		return self._instance.GetCompositeFrame2

	@get_composite_frame.setter
	def get_composite_frame(self, value):
		"""Gets whether the GTol frame with the specified index is part of a composite frame."""
		self._instance.GetCompositeFrame2 = value

	@property
	def get_datum_identifier(self):
		"""Gets the datum identifier."""
		return self._instance.GetDatumIdentifier

	@get_datum_identifier.setter
	def get_datum_identifier(self, value):
		"""Gets the datum identifier."""
		self._instance.GetDatumIdentifier = value

	@property
	def get_font_info(self):
		"""Gets with the font information for this GTol."""
		return self._instance.GetFontInfo

	@get_font_info.setter
	def get_font_info(self, value):
		"""Gets with the font information for this GTol."""
		self._instance.GetFontInfo = value

	@property
	def get_frame_count(self):
		"""Gets the number of frames in this GTol symbol."""
		return self._instance.GetFrameCount

	@get_frame_count.setter
	def get_frame_count(self, value):
		"""Gets the number of frames in this GTol symbol."""
		self._instance.GetFrameCount = value

	@property
	def get_frame_diameter_symbols(self):
		"""Gets whether diameter symbols are displayed for the specified frame."""
		return self._instance.GetFrameDiameterSymbols

	@get_frame_diameter_symbols.setter
	def get_frame_diameter_symbols(self, value):
		"""Gets whether diameter symbols are displayed for the specified frame."""
		self._instance.GetFrameDiameterSymbols = value

	@property
	def get_frame_symbols(self):
		"""Gets the symbols for the specified frame."""
		return self._instance.GetFrameSymbols3

	@get_frame_symbols.setter
	def get_frame_symbols(self, value):
		"""Gets the symbols for the specified frame."""
		self._instance.GetFrameSymbols3 = value

	@property
	def get_frame_values(self):
		"""Gets an array that describes the text that appears in each of the fields of the specified GTol frame."""
		return self._instance.GetFrameValues

	@get_frame_values.setter
	def get_frame_values(self, value):
		"""Gets an array that describes the text that appears in each of the fields of the specified GTol frame."""
		self._instance.GetFrameValues = value

	@property
	def get_height(self):
		"""Gets the GTol height."""
		return self._instance.GetHeight

	@get_height.setter
	def get_height(self, value):
		"""Gets the GTol height."""
		self._instance.GetHeight = value

	@property
	def get_leader_at_index(self):
		"""Gets information about the specified leader on this GTol."""
		return self._instance.GetLeaderAtIndex2

	@get_leader_at_index.setter
	def get_leader_at_index(self, value):
		"""Gets information about the specified leader on this GTol."""
		self._instance.GetLeaderAtIndex2 = value

	@property
	def get_leader_count(self):
		"""Gets the number of leaders on this GTol."""
		return self._instance.GetLeaderCount

	@get_leader_count.setter
	def get_leader_count(self, value):
		"""Gets the number of leaders on this GTol."""
		self._instance.GetLeaderCount = value

	@property
	def get_leader_info(self):
		"""Gets information describing the layout of the GTol leader lines."""
		return self._instance.GetLeaderInfo

	@get_leader_info.setter
	def get_leader_info(self, value):
		"""Gets information describing the layout of the GTol leader lines."""
		self._instance.GetLeaderInfo = value

	@property
	def get_leader_side(self):
		"""Gets where the leader attaches to the symbol."""
		return self._instance.GetLeaderSide

	@get_leader_side.setter
	def get_leader_side(self, value):
		"""Gets where the leader attaches to the symbol."""
		self._instance.GetLeaderSide = value

	@property
	def get_line_at_index(self):
		"""Gets the start and end information for the specified line."""
		return self._instance.GetLineAtIndex

	@get_line_at_index.setter
	def get_line_at_index(self, value):
		"""Gets the start and end information for the specified line."""
		self._instance.GetLineAtIndex = value

	@property
	def get_line_count(self):
		"""Gets the number of linea in this GTol."""
		return self._instance.GetLineCount

	@get_line_count.setter
	def get_line_count(self, value):
		"""Gets the number of linea in this GTol."""
		self._instance.GetLineCount = value

	@property
	def get_next_g_t_o_l(self):
		"""Gets the next GTol."""
		return self._instance.GetNextGTOL

	@get_next_g_t_o_l.setter
	def get_next_g_t_o_l(self, value):
		"""Gets the next GTol."""
		self._instance.GetNextGTOL = value

	@property
	def get_p_t_z_height(self):
		"""Gets the projected tolerance zone for the specified frame and tolerance in this GTol."""
		return self._instance.GetPTZHeight2

	@get_p_t_z_height.setter
	def get_p_t_z_height(self, value):
		"""Gets the projected tolerance zone for the specified frame and tolerance in this GTol."""
		self._instance.GetPTZHeight2 = value

	@property
	def get_sym_arcs(self):
		"""Gets an array that defines all arcs in the symbol."""
		return self._instance.GetSymArcs

	@get_sym_arcs.setter
	def get_sym_arcs(self, value):
		"""Gets an array that defines all arcs in the symbol."""
		self._instance.GetSymArcs = value

	@property
	def get_sym_circles(self):
		"""Gets an array that defines all circles in the symbol."""
		return self._instance.GetSymCircles

	@get_sym_circles.setter
	def get_sym_circles(self, value):
		"""Gets an array that defines all circles in the symbol."""
		self._instance.GetSymCircles = value

	@property
	def get_sym_desc(self):
		"""Gets the specified symbol description."""
		return self._instance.GetSymDesc

	@get_sym_desc.setter
	def get_sym_desc(self, value):
		"""Gets the specified symbol description."""
		self._instance.GetSymDesc = value

	@property
	def get_sym_edge_counts(self):
		"""Gets an array of the number of lines, arcs and circles in the specified symbol."""
		return self._instance.GetSymEdgeCounts

	@get_sym_edge_counts.setter
	def get_sym_edge_counts(self, value):
		"""Gets an array of the number of lines, arcs and circles in the specified symbol."""
		self._instance.GetSymEdgeCounts = value

	@property
	def get_sym_lines(self):
		"""Gets an array that defines all lines in the symbol."""
		return self._instance.GetSymLines

	@get_sym_lines.setter
	def get_sym_lines(self, value):
		"""Gets an array that defines all lines in the symbol."""
		self._instance.GetSymLines = value

	@property
	def get_sym_name(self):
		"""Gets the symbol name based on the specified index number that SOLIDWORKS uses to identify the symbol."""
		return self._instance.GetSymName

	@get_sym_name.setter
	def get_sym_name(self, value):
		"""Gets the symbol name based on the specified index number that SOLIDWORKS uses to identify the symbol."""
		self._instance.GetSymName = value

	@property
	def get_sym_text(self):
		"""Gets the symbol text."""
		return self._instance.GetSymText

	@get_sym_text.setter
	def get_sym_text(self, value):
		"""Gets the symbol text."""
		self._instance.GetSymText = value

	@property
	def get_sym_text_points(self):
		"""Gets the text points for the specified symbol."""
		return self._instance.GetSymTextPoints

	@get_sym_text_points.setter
	def get_sym_text_points(self, value):
		"""Gets the text points for the specified symbol."""
		self._instance.GetSymTextPoints = value

	@property
	def get_text(self):
		"""Gets the specified text part of this GTol."""
		return self._instance.GetText

	@get_text.setter
	def get_text(self, value):
		"""Gets the specified text part of this GTol."""
		self._instance.GetText = value

	@property
	def get_text_angle_at_index(self):
		"""Gets the text angle for the specified piece of text in this GTol."""
		return self._instance.GetTextAngleAtIndex

	@get_text_angle_at_index.setter
	def get_text_angle_at_index(self, value):
		"""Gets the text angle for the specified piece of text in this GTol."""
		self._instance.GetTextAngleAtIndex = value

	@property
	def get_text_at_index(self):
		"""Gets the specified text from this GTol."""
		return self._instance.GetTextAtIndex

	@get_text_at_index.setter
	def get_text_at_index(self, value):
		"""Gets the specified text from this GTol."""
		self._instance.GetTextAtIndex = value

	@property
	def get_text_count(self):
		"""Gets the number of text items in the GTol."""
		return self._instance.GetTextCount

	@get_text_count.setter
	def get_text_count(self, value):
		"""Gets the number of text items in the GTol."""
		self._instance.GetTextCount = value

	@property
	def get_text_font(self):
		"""Gets the font for this GTol."""
		return self._instance.GetTextFont

	@get_text_font.setter
	def get_text_font(self, value):
		"""Gets the font for this GTol."""
		self._instance.GetTextFont = value

	@property
	def get_text_height_at_index(self):
		"""Gets the text height for the specified piece of text in this GTol."""
		return self._instance.GetTextHeightAtIndex

	@get_text_height_at_index.setter
	def get_text_height_at_index(self, value):
		"""Gets the text height for the specified piece of text in this GTol."""
		self._instance.GetTextHeightAtIndex = value

	@property
	def get_text_invert_at_index(self):
		"""Gets the specified text item's invert flag."""
		return self._instance.GetTextInvertAtIndex

	@get_text_invert_at_index.setter
	def get_text_invert_at_index(self, value):
		"""Gets the specified text item's invert flag."""
		self._instance.GetTextInvertAtIndex = value

	@property
	def get_text_point(self):
		"""Gets the GTol text reference point, which is the upper-left corner of the bounding rectangle."""
		return self._instance.GetTextPoint

	@get_text_point.setter
	def get_text_point(self, value):
		"""Gets the GTol text reference point, which is the upper-left corner of the bounding rectangle."""
		self._instance.GetTextPoint = value

	@property
	def get_text_position_at_index(self):
		"""Gets the text item's offset relative to note's text point."""
		return self._instance.GetTextPositionAtIndex

	@get_text_position_at_index.setter
	def get_text_position_at_index(self, value):
		"""Gets the text item's offset relative to note's text point."""
		self._instance.GetTextPositionAtIndex = value

	@property
	def get_text_ref_position_at_index(self):
		"""Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center)."""
		return self._instance.GetTextRefPositionAtIndex

	@get_text_ref_position_at_index.setter
	def get_text_ref_position_at_index(self, value):
		"""Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center)."""
		self._instance.GetTextRefPositionAtIndex = value

	@property
	def get_triangle_at_index(self):
		"""Gets the triangle at the specified index."""
		return self._instance.GetTriangleAtIndex

	@get_triangle_at_index.setter
	def get_triangle_at_index(self, value):
		"""Gets the triangle at the specified index."""
		self._instance.GetTriangleAtIndex = value

	@property
	def get_triangle_count(self):
		"""Gets the number of triangles in this GTol."""
		return self._instance.GetTriangleCount

	@get_triangle_count.setter
	def get_triangle_count(self, value):
		"""Gets the number of triangles in this GTol."""
		self._instance.GetTriangleCount = value

	@property
	def get_witness_line(self):
		"""Gets the extension line that connects the leader of this geometric tolerance with the entity being dimensioned."""
		return self._instance.GetWitnessLine

	@get_witness_line.setter
	def get_witness_line(self, value):
		"""Gets the extension line that connects the leader of this geometric tolerance with the entity being dimensioned."""
		self._instance.GetWitnessLine = value

	@property
	def has_extra_leader(self):
		"""Gets whether the GTol has a bent leaderline or a straight leaderline."""
		return self._instance.HasExtraLeader

	@has_extra_leader.setter
	def has_extra_leader(self, value):
		"""Gets whether the GTol has a bent leaderline or a straight leaderline."""
		self._instance.HasExtraLeader = value

	@property
	def i_get_annotation(self):
		"""Gets the annotation for this specific GTol."""
		return self._instance.IGetAnnotation

	@i_get_annotation.setter
	def i_get_annotation(self, value):
		"""Gets the annotation for this specific GTol."""
		self._instance.IGetAnnotation = value

	@property
	def i_get_arc_at_index(self):
		"""Gets information for the specified arc."""
		return self._instance.IGetArcAtIndex

	@i_get_arc_at_index.setter
	def i_get_arc_at_index(self, value):
		"""Gets information for the specified arc."""
		self._instance.IGetArcAtIndex = value

	@property
	def i_get_arrow_head_at_index(self):
		"""Gets information on the specified arrow head in this GTol."""
		return self._instance.IGetArrowHeadAtIndex

	@i_get_arrow_head_at_index.setter
	def i_get_arrow_head_at_index(self, value):
		"""Gets information on the specified arrow head in this GTol."""
		self._instance.IGetArrowHeadAtIndex = value

	@property
	def i_get_arrow_head_info(self):
		"""Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
		return self._instance.IGetArrowHeadInfo

	@i_get_arrow_head_info.setter
	def i_get_arrow_head_info(self, value):
		"""Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
		self._instance.IGetArrowHeadInfo = value

	@property
	def i_get_attach_pos(self):
		"""Gets the attachment point of the GTol."""
		return self._instance.IGetAttachPos

	@i_get_attach_pos.setter
	def i_get_attach_pos(self, value):
		"""Gets the attachment point of the GTol."""
		self._instance.IGetAttachPos = value

	@property
	def i_get_font_info(self):
		"""Gets with the font information for this GTol."""
		return self._instance.IGetFontInfo

	@i_get_font_info.setter
	def i_get_font_info(self, value):
		"""Gets with the font information for this GTol."""
		self._instance.IGetFontInfo = value

	@property
	def i_get_frame_diameter_symbols(self):
		"""Gets whether diameter symbols are displayed for the specified frame."""
		return self._instance.IGetFrameDiameterSymbols

	@i_get_frame_diameter_symbols.setter
	def i_get_frame_diameter_symbols(self, value):
		"""Gets whether diameter symbols are displayed for the specified frame."""
		self._instance.IGetFrameDiameterSymbols = value

	@property
	def i_get_frame_values(self):
		"""Gets an array that describes the text that appears in each of the fields of the specified GTol frame."""
		return self._instance.IGetFrameValues

	@i_get_frame_values.setter
	def i_get_frame_values(self, value):
		"""Gets an array that describes the text that appears in each of the fields of the specified GTol frame."""
		self._instance.IGetFrameValues = value

	@property
	def i_get_leader_at_index(self):
		"""Gets information about the specified leader on this GTol."""
		return self._instance.IGetLeaderAtIndex2

	@i_get_leader_at_index.setter
	def i_get_leader_at_index(self, value):
		"""Gets information about the specified leader on this GTol."""
		self._instance.IGetLeaderAtIndex2 = value

	@property
	def i_get_leader_info(self):
		"""Gets information describing the layout of the GTol leader lines."""
		return self._instance.IGetLeaderInfo

	@i_get_leader_info.setter
	def i_get_leader_info(self, value):
		"""Gets information describing the layout of the GTol leader lines."""
		self._instance.IGetLeaderInfo = value

	@property
	def i_get_line_at_index(self):
		"""Gets the start and end information for the specified line."""
		return self._instance.IGetLineAtIndex

	@i_get_line_at_index.setter
	def i_get_line_at_index(self, value):
		"""Gets the start and end information for the specified line."""
		self._instance.IGetLineAtIndex = value

	@property
	def i_get_next_g_t_o_l(self):
		"""Gets the next GTol."""
		return self._instance.IGetNextGTOL

	@i_get_next_g_t_o_l.setter
	def i_get_next_g_t_o_l(self, value):
		"""Gets the next GTol."""
		self._instance.IGetNextGTOL = value

	@property
	def i_get_sym_arcs(self):
		"""Gets an array that defines all arcs in the symbol."""
		return self._instance.IGetSymArcs

	@i_get_sym_arcs.setter
	def i_get_sym_arcs(self, value):
		"""Gets an array that defines all arcs in the symbol."""
		self._instance.IGetSymArcs = value

	@property
	def i_get_sym_circles(self):
		"""Gets an array that defines all circles in the symbol."""
		return self._instance.IGetSymCircles

	@i_get_sym_circles.setter
	def i_get_sym_circles(self, value):
		"""Gets an array that defines all circles in the symbol."""
		self._instance.IGetSymCircles = value

	@property
	def i_get_sym_edge_counts(self):
		"""Gets an array of the number of lines, arcs and circles in the specified symbol."""
		return self._instance.IGetSymEdgeCounts

	@i_get_sym_edge_counts.setter
	def i_get_sym_edge_counts(self, value):
		"""Gets an array of the number of lines, arcs and circles in the specified symbol."""
		self._instance.IGetSymEdgeCounts = value

	@property
	def i_get_sym_lines(self):
		"""Gets an array that defines all lines in the symbol."""
		return self._instance.IGetSymLines

	@i_get_sym_lines.setter
	def i_get_sym_lines(self, value):
		"""Gets an array that defines all lines in the symbol."""
		self._instance.IGetSymLines = value

	@property
	def i_get_sym_text(self):
		"""Gets the symbol text."""
		return self._instance.IGetSymText

	@i_get_sym_text.setter
	def i_get_sym_text(self, value):
		"""Gets the symbol text."""
		self._instance.IGetSymText = value

	@property
	def i_get_sym_text_points(self):
		"""Gets the text points for the specified symbol."""
		return self._instance.IGetSymTextPoints

	@i_get_sym_text_points.setter
	def i_get_sym_text_points(self, value):
		"""Gets the text points for the specified symbol."""
		self._instance.IGetSymTextPoints = value

	@property
	def i_get_text_point(self):
		"""Gets the GTol text reference point, which is the upper-left corner of the bounding rectangle."""
		return self._instance.IGetTextPoint

	@i_get_text_point.setter
	def i_get_text_point(self, value):
		"""Gets the GTol text reference point, which is the upper-left corner of the bounding rectangle."""
		self._instance.IGetTextPoint = value

	@property
	def i_get_text_position_at_index(self):
		"""Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center)."""
		return self._instance.IGetTextPositionAtIndex

	@i_get_text_position_at_index.setter
	def i_get_text_position_at_index(self, value):
		"""Gets the reference position for the specified text item in this GTol (for example, upper-left, lower-left, center)."""
		self._instance.IGetTextPositionAtIndex = value

	@property
	def i_get_triangle_at_index(self):
		"""Gets the triangle at the specified index."""
		return self._instance.IGetTriangleAtIndex

	@i_get_triangle_at_index.setter
	def i_get_triangle_at_index(self, value):
		"""Gets the triangle at the specified index."""
		self._instance.IGetTriangleAtIndex = value

	@property
	def i_get_witness_line(self):
		"""Gets the extension line that connects the leader of this geometric tolerance with the entity that is being dimensioned."""
		return self._instance.IGetWitnessLine

	@i_get_witness_line.setter
	def i_get_witness_line(self, value):
		"""Gets the extension line that connects the leader of this geometric tolerance with the entity that is being dimensioned."""
		self._instance.IGetWitnessLine = value

	@property
	def insert_below_frame_text_at(self):
		"""Inserts the specified text at the specified line index in the below frame of this GTol."""
		return self._instance.InsertBelowFrameTextAt

	@insert_below_frame_text_at.setter
	def insert_below_frame_text_at(self, value):
		"""Inserts the specified text at the specified line index in the below frame of this GTol."""
		self._instance.InsertBelowFrameTextAt = value

	@property
	def is_attached(self):
		"""Gets whether this GTol is attached."""
		return self._instance.IsAttached

	@is_attached.setter
	def is_attached(self, value):
		"""Gets whether this GTol is attached."""
		self._instance.IsAttached = value

	@property
	def set_all_around_this_side(self):
		"""Sets whether this GTol uses an All Around This Side leader."""
		return self._instance.SetAllAroundThisSide

	@set_all_around_this_side.setter
	def set_all_around_this_side(self, value):
		"""Sets whether this GTol uses an All Around This Side leader."""
		self._instance.SetAllAroundThisSide = value

	@property
	def set_all_over_this_side(self):
		"""Sets whether this Gtol uses an All Over This Side leader."""
		return self._instance.SetAllOverThisSide

	@set_all_over_this_side.setter
	def set_all_over_this_side(self, value):
		"""Sets whether this Gtol uses an All Over This Side leader."""
		self._instance.SetAllOverThisSide = value

	@property
	def set_below_frame_text_at(self):
		"""Edits or inserts a text line at the specified below frame line index of this GTol."""
		return self._instance.SetBelowFrameTextAt

	@set_below_frame_text_at.setter
	def set_below_frame_text_at(self, value):
		"""Edits or inserts a text line at the specified below frame line index of this GTol."""
		self._instance.SetBelowFrameTextAt = value

	@property
	def set_between_two_points(self):
		"""Enables or disables the between two points symbol and its texts."""
		return self._instance.SetBetweenTwoPoints

	@set_between_two_points.setter
	def set_between_two_points(self, value):
		"""Enables or disables the between two points symbol and its texts."""
		self._instance.SetBetweenTwoPoints = value

	@property
	def set_composite_frame(self):
		"""Sets whether to create a composite frame containing the specified GTol frame."""
		return self._instance.SetCompositeFrame2

	@set_composite_frame.setter
	def set_composite_frame(self, value):
		"""Sets whether to create a composite frame containing the specified GTol frame."""
		self._instance.SetCompositeFrame2 = value

	@property
	def set_datum_identifier(self):
		"""Sets the name of the datum being defined."""
		return self._instance.SetDatumIdentifier

	@set_datum_identifier.setter
	def set_datum_identifier(self, value):
		"""Sets the name of the datum being defined."""
		self._instance.SetDatumIdentifier = value

	@property
	def set_frame_symbols(self):
		"""Sets the symbols for the specified frame."""
		return self._instance.SetFrameSymbols2

	@set_frame_symbols.setter
	def set_frame_symbols(self, value):
		"""Sets the symbols for the specified frame."""
		self._instance.SetFrameSymbols2 = value

	@property
	def set_frame_values(self):
		"""Sets the geometric tolerance values and datum references in the specified frame of this GTol symbol."""
		return self._instance.SetFrameValues2

	@set_frame_values.setter
	def set_frame_values(self, value):
		"""Sets the geometric tolerance values and datum references in the specified frame of this GTol symbol."""
		self._instance.SetFrameValues2 = value

	@property
	def set_leader(self):
		"""Sets the characteristics of the leader for this symbol."""
		return self._instance.SetLeader

	@set_leader.setter
	def set_leader(self, value):
		"""Sets the characteristics of the leader for this symbol."""
		self._instance.SetLeader = value

	@property
	def set_position(self):
		"""Sets the position of this GTol."""
		return self._instance.SetPosition

	@set_position.setter
	def set_position(self, value):
		"""Sets the position of this GTol."""
		self._instance.SetPosition = value

	@property
	def set_p_t_z_height(self):
		"""Sets the projected tolerance zone for the specified frame and tolerance in this GTol."""
		return self._instance.SetPTZHeight2

	@set_p_t_z_height.setter
	def set_p_t_z_height(self, value):
		"""Sets the projected tolerance zone for the specified frame and tolerance in this GTol."""
		self._instance.SetPTZHeight2 = value

	@property
	def set_text(self):
		"""Sets the specified text part of this GTol."""
		return self._instance.SetText

	@set_text.setter
	def set_text(self, value):
		"""Sets the specified text part of this GTol."""
		self._instance.SetText = value

