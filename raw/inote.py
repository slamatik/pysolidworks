# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.html
class INote:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def all_upper_case(self):
		"""Gets or sets whether the text of this note is all uppercase."""
		return self._instance.AllUpperCase

	@all_upper_case.setter
	def all_upper_case(self, value):
		"""Gets or sets whether the text of this note is all uppercase."""
		self._instance.AllUpperCase = value

	@property
	def angle(self):
		"""Controls the rotation angle of this note."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Controls the rotation angle of this note."""
		self._instance.Angle = value

	@property
	def behind_sheet(self):
		"""Places this note, located on the sheet format in a drawing, behind the drawing sheet."""
		return self._instance.BehindSheet

	@behind_sheet.setter
	def behind_sheet(self, value):
		"""Places this note, located on the sheet format in a drawing, behind the drawing sheet."""
		self._instance.BehindSheet = value

	@property
	def has_multiple_fonts(self):
		"""Gets whether a note contains multiple fonts."""
		return self._instance.HasMultipleFonts

	@has_multiple_fonts.setter
	def has_multiple_fonts(self, value):
		"""Gets whether a note contains multiple fonts."""
		self._instance.HasMultipleFonts = value

	@property
	def include_dim_prefix_suffix_tolerance(self):
		"""Gets or sets whether to include the dimension prefix, suffix, and tolerance in this dimension note."""
		return self._instance.IncludeDimPrefixSuffixTolerance

	@include_dim_prefix_suffix_tolerance.setter
	def include_dim_prefix_suffix_tolerance(self, value):
		"""Gets or sets whether to include the dimension prefix, suffix, and tolerance in this dimension note."""
		self._instance.IncludeDimPrefixSuffixTolerance = value

	@property
	def is_bend_line_note(self):
		"""Gets whether this note is a bendline note."""
		return self._instance.IsBendLineNote

	@is_bend_line_note.setter
	def is_bend_line_note(self, value):
		"""Gets whether this note is a bendline note."""
		self._instance.IsBendLineNote = value

	@property
	def lock_position(self):
		"""Gets and sets whether to anchor this note."""
		return self._instance.LockPosition

	@lock_position.setter
	def lock_position(self, value):
		"""Gets and sets whether to anchor this note."""
		self._instance.LockPosition = value

	@property
	def prompt_text(self):
		"""Gets and sets the message prompt text."""
		return self._instance.PromptText

	@prompt_text.setter
	def prompt_text(self, value):
		"""Gets and sets the message prompt text."""
		self._instance.PromptText = value

	@property
	def property_linked_text(self):
		"""Gets or sets the text for the note using the values of the properties linked to the note."""
		return self._instance.PropertyLinkedText

	@property_linked_text.setter
	def property_linked_text(self, value):
		"""Gets or sets the text for the note using the values of the properties linked to the note."""
		self._instance.PropertyLinkedText = value

	@property
	def read_only(self):
		"""Gets or sets the read-only state of a note."""
		return self._instance.ReadOnly

	@read_only.setter
	def read_only(self, value):
		"""Gets or sets the read-only state of a note."""
		self._instance.ReadOnly = value

	@property
	def tag_name(self):
		"""Gets or sets the tag name for this note."""
		return self._instance.TagName

	@tag_name.setter
	def tag_name(self, value):
		"""Gets or sets the tag name for this note."""
		self._instance.TagName = value

	@property
	def text_right_to_left(self):
		"""Gets or sets whether notes are displayed right to left."""
		return self._instance.TextRightToLeft

	@text_right_to_left.setter
	def text_right_to_left(self, value):
		"""Gets or sets whether notes are displayed right to left."""
		self._instance.TextRightToLeft = value

	@property
	def to_bounding_box(self):
		"""Gets and sets whether to select the To bounding box option for leaders in this note's PropertyManager page."""
		return self._instance.ToBoundingBox

	@to_bounding_box.setter
	def to_bounding_box(self, value):
		"""Gets and sets whether to select the To bounding box option for leaders in this note's PropertyManager page."""
		self._instance.ToBoundingBox = value

	@property
	def visible(self):
		"""Gets and sets the visibility state of a note during the creation of a block."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets and sets the visibility state of a note during the creation of a block."""
		self._instance.Visible = value

	@property
	def watermark_behind_geometry(self):
		"""Gets or sets whether to place this note, specified to be a watermark, behind the geometry in a part or assembly."""
		return self._instance.WatermarkBehindGeometry

	@watermark_behind_geometry.setter
	def watermark_behind_geometry(self, value):
		"""Gets or sets whether to place this note, specified to be a watermark, behind the geometry in a part or assembly."""
		self._instance.WatermarkBehindGeometry = value

	@property
	def watermark_note(self):
		"""Gets or sets whether the note is a watermark in a part or assembly."""
		return self._instance.WatermarkNote

	@watermark_note.setter
	def watermark_note(self, value):
		"""Gets or sets whether the note is a watermark in a part or assembly."""
		self._instance.WatermarkNote = value

	@property
	def watermark_transparency_level(self):
		"""Gets or sets the transparency level of a note specified to be a watermark."""
		return self._instance.WatermarkTransparencyLevel

	@watermark_transparency_level.setter
	def watermark_transparency_level(self, value):
		"""Gets or sets the transparency level of a note specified to be a watermark."""
		self._instance.WatermarkTransparencyLevel = value

	@property
	def get_annotation(self):
		"""Gets the annotation for this specific note."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the annotation for this specific note."""
		self._instance.GetAnnotation = value

	@property
	def get_arc_at_index(self):
		"""Gets information for the specified arc in this note."""
		return self._instance.GetArcAtIndex

	@get_arc_at_index.setter
	def get_arc_at_index(self, value):
		"""Gets information for the specified arc in this note."""
		self._instance.GetArcAtIndex = value

	@property
	def get_arc_count(self):
		"""Gets the number of arcs in the note."""
		return self._instance.GetArcCount

	@get_arc_count.setter
	def get_arc_count(self, value):
		"""Gets the number of arcs in the note."""
		self._instance.GetArcCount = value

	@property
	def get_arrow_head_at_index(self):
		"""Gets information on the specified arrowhead in this note."""
		return self._instance.GetArrowHeadAtIndex

	@get_arrow_head_at_index.setter
	def get_arrow_head_at_index(self, value):
		"""Gets information on the specified arrowhead in this note."""
		self._instance.GetArrowHeadAtIndex = value

	@property
	def get_arrow_head_count(self):
		"""Gets the number of arrowheads in the note."""
		return self._instance.GetArrowHeadCount

	@get_arrow_head_count.setter
	def get_arrow_head_count(self, value):
		"""Gets the number of arrowheads in the note."""
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
		"""Gets the attachment point of this note."""
		return self._instance.GetAttachPos

	@get_attach_pos.setter
	def get_attach_pos(self, value):
		"""Gets the attachment point of this note."""
		self._instance.GetAttachPos = value

	@property
	def get_balloon_info(self):
		"""Gets information describing the geometry of the balloon, if any, that encloses the note text."""
		return self._instance.GetBalloonInfo

	@get_balloon_info.setter
	def get_balloon_info(self, value):
		"""Gets information describing the geometry of the balloon, if any, that encloses the note text."""
		self._instance.GetBalloonInfo = value

	@property
	def get_balloon_padding(self):
		"""Gets the balloon padding of this note."""
		return self._instance.GetBalloonPadding

	@get_balloon_padding.setter
	def get_balloon_padding(self, value):
		"""Gets the balloon padding of this note."""
		self._instance.GetBalloonPadding = value

	@property
	def get_balloon_size(self):
		"""Gets the balloon size or fit of this note."""
		return self._instance.GetBalloonSize

	@get_balloon_size.setter
	def get_balloon_size(self, value):
		"""Gets the balloon size or fit of this note."""
		self._instance.GetBalloonSize = value

	@property
	def get_balloon_stack(self):
		"""Gets the balloon stack for this balloon note."""
		return self._instance.GetBalloonStack

	@get_balloon_stack.setter
	def get_balloon_stack(self, value):
		"""Gets the balloon stack for this balloon note."""
		self._instance.GetBalloonStack = value

	@property
	def get_balloon_style(self):
		"""Gets the balloon style of this note."""
		return self._instance.GetBalloonStyle

	@get_balloon_style.setter
	def get_balloon_style(self, value):
		"""Gets the balloon style of this note."""
		self._instance.GetBalloonStyle = value

	@property
	def get_bend_line_values(self):
		"""Gets the values of a bend line note."""
		return self._instance.GetBendLineValues2

	@get_bend_line_values.setter
	def get_bend_line_values(self, value):
		"""Gets the values of a bend line note."""
		self._instance.GetBendLineValues2 = value

	@property
	def get_bom_balloon_text(self):
		"""Gets the text for this BOM balloon note."""
		return self._instance.GetBomBalloonText

	@get_bom_balloon_text.setter
	def get_bom_balloon_text(self, value):
		"""Gets the text for this BOM balloon note."""
		self._instance.GetBomBalloonText = value

	@property
	def get_bom_balloon_text_style(self):
		"""Gets the text style of this BOM balloon note."""
		return self._instance.GetBomBalloonTextStyle

	@get_bom_balloon_text_style.setter
	def get_bom_balloon_text_style(self, value):
		"""Gets the text style of this BOM balloon note."""
		self._instance.GetBomBalloonTextStyle = value

	@property
	def get_extent(self):
		"""Gets the extents of a note in sheet space."""
		return self._instance.GetExtent

	@get_extent.setter
	def get_extent(self, value):
		"""Gets the extents of a note in sheet space."""
		self._instance.GetExtent = value

	@property
	def get_font_info(self):
		"""Gets with the note's font information."""
		return self._instance.GetFontInfo

	@get_font_info.setter
	def get_font_info(self, value):
		"""Gets with the note's font information."""
		self._instance.GetFontInfo = value

	@property
	def get_height(self):
		"""Get the note's height."""
		return self._instance.GetHeight

	@get_height.setter
	def get_height(self, value):
		"""Get the note's height."""
		self._instance.GetHeight = value

	@property
	def get_height_in_points(self):
		"""Gets the height of this note in points (for example, 8, 10, 12, and so on)."""
		return self._instance.GetHeightInPoints

	@get_height_in_points.setter
	def get_height_in_points(self, value):
		"""Gets the height of this note in points (for example, 8, 10, 12, and so on)."""
		self._instance.GetHeightInPoints = value

	@property
	def get_hyperlink_text(self):
		"""Gets the hyperlink in a note."""
		return self._instance.GetHyperlinkText

	@get_hyperlink_text.setter
	def get_hyperlink_text(self, value):
		"""Gets the hyperlink in a note."""
		self._instance.GetHyperlinkText = value

	@property
	def get_leader_at_index(self):
		"""Gets information about the specified leader on this note."""
		return self._instance.GetLeaderAtIndex

	@get_leader_at_index.setter
	def get_leader_at_index(self, value):
		"""Gets information about the specified leader on this note."""
		self._instance.GetLeaderAtIndex = value

	@property
	def get_leader_count(self):
		"""Gets the number of leaders on this note."""
		return self._instance.GetLeaderCount

	@get_leader_count.setter
	def get_leader_count(self, value):
		"""Gets the number of leaders on this note."""
		self._instance.GetLeaderCount = value

	@property
	def get_leader_info(self):
		"""Gets information describing the layout of the note leader lines."""
		return self._instance.GetLeaderInfo

	@get_leader_info.setter
	def get_leader_info(self, value):
		"""Gets information describing the layout of the note leader lines."""
		self._instance.GetLeaderInfo = value

	@property
	def get_leader_num_points_at(self):
		"""Gets the number of points in the specified leader of this note."""
		return self._instance.GetLeaderNumPointsAt

	@get_leader_num_points_at.setter
	def get_leader_num_points_at(self, value):
		"""Gets the number of points in the specified leader of this note."""
		self._instance.GetLeaderNumPointsAt = value

	@property
	def get_line_at_index(self):
		"""Gets information for the specified line."""
		return self._instance.GetLineAtIndex

	@get_line_at_index.setter
	def get_line_at_index(self, value):
		"""Gets information for the specified line."""
		self._instance.GetLineAtIndex = value

	@property
	def get_line_count(self):
		"""Gets the number of line segments in this note."""
		return self._instance.GetLineCount

	@get_line_count.setter
	def get_line_count(self, value):
		"""Gets the number of line segments in this note."""
		self._instance.GetLineCount = value

	@property
	def get_name(self):
		"""Gets the name of this note."""
		return self._instance.GetName

	@get_name.setter
	def get_name(self, value):
		"""Gets the name of this note."""
		self._instance.GetName = value

	@property
	def get_next(self):
		"""Gets the next note in drawing view."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next note in drawing view."""
		self._instance.GetNext = value

	@property
	def get_text(self):
		"""Gets this note's text."""
		return self._instance.GetText

	@get_text.setter
	def get_text(self, value):
		"""Gets this note's text."""
		self._instance.GetText = value

	@property
	def get_text_angle_at_index(self):
		"""Gets the text angle for the specified piece of text in this note."""
		return self._instance.GetTextAngleAtIndex

	@get_text_angle_at_index.setter
	def get_text_angle_at_index(self, value):
		"""Gets the text angle for the specified piece of text in this note."""
		self._instance.GetTextAngleAtIndex = value

	@property
	def get_text_at_index(self):
		"""Gets the specified text in this note."""
		return self._instance.GetTextAtIndex

	@get_text_at_index.setter
	def get_text_at_index(self, value):
		"""Gets the specified text in this note."""
		self._instance.GetTextAtIndex = value

	@property
	def get_text_count(self):
		"""Gets the number of text items in this note."""
		return self._instance.GetTextCount

	@get_text_count.setter
	def get_text_count(self, value):
		"""Gets the number of text items in this note."""
		self._instance.GetTextCount = value

	@property
	def get_text_font_at_index(self):
		"""Gets the font used by the specified text item in this note."""
		return self._instance.GetTextFontAtIndex

	@get_text_font_at_index.setter
	def get_text_font_at_index(self, value):
		"""Gets the font used by the specified text item in this note."""
		self._instance.GetTextFontAtIndex = value

	@property
	def get_text_height_at_index(self):
		"""Gets the text height for the specified piece of text in this note."""
		return self._instance.GetTextHeightAtIndex

	@get_text_height_at_index.setter
	def get_text_height_at_index(self, value):
		"""Gets the text height for the specified piece of text in this note."""
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
	def get_text_justification(self):
		"""Gets the text justification of a standard note."""
		return self._instance.GetTextJustification

	@get_text_justification.setter
	def get_text_justification(self, value):
		"""Gets the text justification of a standard note."""
		self._instance.GetTextJustification = value

	@property
	def get_text_line_spacing_at_index(self):
		"""Gets the line spacing for this note."""
		return self._instance.GetTextLineSpacingAtIndex

	@get_text_line_spacing_at_index.setter
	def get_text_line_spacing_at_index(self, value):
		"""Gets the line spacing for this note."""
		self._instance.GetTextLineSpacingAtIndex = value

	@property
	def get_text_point(self):
		"""Gets the note's text reference point (i.e., note origin)."""
		return self._instance.GetTextPoint2

	@get_text_point.setter
	def get_text_point(self, value):
		"""Gets the note's text reference point (i.e., note origin)."""
		self._instance.GetTextPoint2 = value

	@property
	def get_text_position_at_index(self):
		"""Gets the text item's offset relative to the document origin."""
		return self._instance.GetTextPositionAtIndex

	@get_text_position_at_index.setter
	def get_text_position_at_index(self, value):
		"""Gets the text item's offset relative to the document origin."""
		self._instance.GetTextPositionAtIndex = value

	@property
	def get_text_ref_position_at_index(self):
		"""Gets the specified text item's reference position in this note; for example, the upper left, lower left, or center."""
		return self._instance.GetTextRefPositionAtIndex

	@get_text_ref_position_at_index.setter
	def get_text_ref_position_at_index(self, value):
		"""Gets the specified text item's reference position in this note; for example, the upper left, lower left, or center."""
		self._instance.GetTextRefPositionAtIndex = value

	@property
	def get_text_vertical_justification(self):
		"""Gets the vertical justification of a standard note."""
		return self._instance.GetTextVerticalJustification

	@get_text_vertical_justification.setter
	def get_text_vertical_justification(self, value):
		"""Gets the vertical justification of a standard note."""
		self._instance.GetTextVerticalJustification = value

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
		"""Gets the number of triangles in this note."""
		return self._instance.GetTriangleCount

	@get_triangle_count.setter
	def get_triangle_count(self, value):
		"""Gets the number of triangles in this note."""
		self._instance.GetTriangleCount = value

	@property
	def get_upper_right(self):
		"""Gets the note's upper-right text point."""
		return self._instance.GetUpperRight

	@get_upper_right.setter
	def get_upper_right(self, value):
		"""Gets the note's upper-right text point."""
		self._instance.GetUpperRight = value

	@property
	def has_balloon(self):
		"""Gets whether this note has a balloon."""
		return self._instance.HasBalloon

	@has_balloon.setter
	def has_balloon(self, value):
		"""Gets whether this note has a balloon."""
		self._instance.HasBalloon = value

	@property
	def has_extra_leader(self):
		"""Gets whether this note has a bent or straight leaderline."""
		return self._instance.HasExtraLeader

	@has_extra_leader.setter
	def has_extra_leader(self, value):
		"""Gets whether this note has a bent or straight leaderline."""
		self._instance.HasExtraLeader = value

	@property
	def i_get_annotation(self):
		"""Gets the annotation for this specific note."""
		return self._instance.IGetAnnotation

	@i_get_annotation.setter
	def i_get_annotation(self, value):
		"""Gets the annotation for this specific note."""
		self._instance.IGetAnnotation = value

	@property
	def i_get_arc_at_index(self):
		"""Gets information for the specified arc in this note."""
		return self._instance.IGetArcAtIndex

	@i_get_arc_at_index.setter
	def i_get_arc_at_index(self, value):
		"""Gets information for the specified arc in this note."""
		self._instance.IGetArcAtIndex = value

	@property
	def i_get_arrow_head_at_index(self):
		"""Gets information on the specified arrowhead in this note."""
		return self._instance.IGetArrowHeadAtIndex

	@i_get_arrow_head_at_index.setter
	def i_get_arrow_head_at_index(self, value):
		"""Gets information on the specified arrowhead in this note."""
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
		"""Gets the attachment point of this note."""
		return self._instance.IGetAttachPos

	@i_get_attach_pos.setter
	def i_get_attach_pos(self, value):
		"""Gets the attachment point of this note."""
		self._instance.IGetAttachPos = value

	@property
	def i_get_balloon_info(self):
		"""Gets information describing the geometry of the balloon, if any, that encloses the note text."""
		return self._instance.IGetBalloonInfo

	@i_get_balloon_info.setter
	def i_get_balloon_info(self, value):
		"""Gets information describing the geometry of the balloon, if any, that encloses the note text."""
		self._instance.IGetBalloonInfo = value

	@property
	def i_get_extent(self):
		"""Gets the extents of a note in sheet space."""
		return self._instance.IGetExtent

	@i_get_extent.setter
	def i_get_extent(self, value):
		"""Gets the extents of a note in sheet space."""
		self._instance.IGetExtent = value

	@property
	def i_get_font_info(self):
		"""Gets with the note's font information."""
		return self._instance.IGetFontInfo

	@i_get_font_info.setter
	def i_get_font_info(self, value):
		"""Gets with the note's font information."""
		self._instance.IGetFontInfo = value

	@property
	def i_get_leader_at_index(self):
		"""Gets information about the specified leader on this note."""
		return self._instance.IGetLeaderAtIndex

	@i_get_leader_at_index.setter
	def i_get_leader_at_index(self, value):
		"""Gets information about the specified leader on this note."""
		self._instance.IGetLeaderAtIndex = value

	@property
	def i_get_leader_info(self):
		"""Gets information describing the layout of the note leader lines."""
		return self._instance.IGetLeaderInfo

	@i_get_leader_info.setter
	def i_get_leader_info(self, value):
		"""Gets information describing the layout of the note leader lines."""
		self._instance.IGetLeaderInfo = value

	@property
	def i_get_line_at_index(self):
		"""Gets information for the specified line."""
		return self._instance.IGetLineAtIndex

	@i_get_line_at_index.setter
	def i_get_line_at_index(self, value):
		"""Gets information for the specified line."""
		self._instance.IGetLineAtIndex = value

	@property
	def i_get_next(self):
		"""Gets the next note in drawing view."""
		return self._instance.IGetNext

	@i_get_next.setter
	def i_get_next(self, value):
		"""Gets the next note in drawing view."""
		self._instance.IGetNext = value

	@property
	def i_get_text_point(self):
		"""Gets the note's text reference point (i.e., note origin)."""
		return self._instance.IGetTextPoint2

	@i_get_text_point.setter
	def i_get_text_point(self, value):
		"""Gets the note's text reference point (i.e., note origin)."""
		self._instance.IGetTextPoint2 = value

	@property
	def i_get_text_position_at_index(self):
		"""Gets the text item's offset relative to the document origin."""
		return self._instance.IGetTextPositionAtIndex

	@i_get_text_position_at_index.setter
	def i_get_text_position_at_index(self, value):
		"""Gets the text item's offset relative to the document origin."""
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
	def i_get_upper_right(self):
		"""Gets the note's upper-right text point."""
		return self._instance.IGetUpperRight

	@i_get_upper_right.setter
	def i_get_upper_right(self, value):
		"""Gets the note's upper-right text point."""
		self._instance.IGetUpperRight = value

	@property
	def is_attached(self):
		"""Gets whether the note is attached."""
		return self._instance.IsAttached

	@is_attached.setter
	def is_attached(self, value):
		"""Gets whether the note is attached."""
		self._instance.IsAttached = value

	@property
	def is_bom_balloon(self):
		"""Gets whether this note has a BOM balloon."""
		return self._instance.IsBomBalloon

	@is_bom_balloon.setter
	def is_bom_balloon(self, value):
		"""Gets whether this note has a BOM balloon."""
		self._instance.IsBomBalloon = value

	@property
	def is_stacked_balloon(self):
		"""Gets whether this note is part of a stacked balloon."""
		return self._instance.IsStackedBalloon

	@is_stacked_balloon.setter
	def is_stacked_balloon(self, value):
		"""Gets whether this note is part of a stacked balloon."""
		self._instance.IsStackedBalloon = value

	@property
	def is_stacked_balloon_master(self):
		"""Gets whether this note is the master note of a balloon stack."""
		return self._instance.IsStackedBalloonMaster

	@is_stacked_balloon_master.setter
	def is_stacked_balloon_master(self, value):
		"""Gets whether this note is the master note of a balloon stack."""
		self._instance.IsStackedBalloonMaster = value

	@property
	def make_stacked_balloon(self):
		"""Converts this balloon to a stacked balloon."""
		return self._instance.MakeStackedBalloon

	@make_stacked_balloon.setter
	def make_stacked_balloon(self, value):
		"""Converts this balloon to a stacked balloon."""
		self._instance.MakeStackedBalloon = value

	@property
	def set_balloon(self):
		"""Sets the balloon style, size, and fit for this note."""
		return self._instance.SetBalloon

	@set_balloon.setter
	def set_balloon(self, value):
		"""Sets the balloon style, size, and fit for this note."""
		self._instance.SetBalloon = value

	@property
	def set_balloon_padding(self):
		"""Sets the padding for this balloon note."""
		return self._instance.SetBalloonPadding

	@set_balloon_padding.setter
	def set_balloon_padding(self, value):
		"""Sets the padding for this balloon note."""
		self._instance.SetBalloonPadding = value

	@property
	def set_bom_balloon_text(self):
		"""Sets the text for this BOM balloon note."""
		return self._instance.SetBomBalloonText

	@set_bom_balloon_text.setter
	def set_bom_balloon_text(self, value):
		"""Sets the text for this BOM balloon note."""
		self._instance.SetBomBalloonText = value

	@property
	def set_height(self):
		"""Sets the height of this note in meters."""
		return self._instance.SetHeight

	@set_height.setter
	def set_height(self, value):
		"""Sets the height of this note in meters."""
		self._instance.SetHeight = value

	@property
	def set_height_in_points(self):
		"""Sets the height of this note in points (for example, 8, 10, 12, and so on)."""
		return self._instance.SetHeightInPoints

	@set_height_in_points.setter
	def set_height_in_points(self, value):
		"""Sets the height of this note in points (for example, 8, 10, 12, and so on)."""
		self._instance.SetHeightInPoints = value

	@property
	def set_hyperlink_text(self):
		"""Sets the hyperlink in a note."""
		return self._instance.SetHyperlinkText

	@set_hyperlink_text.setter
	def set_hyperlink_text(self, value):
		"""Sets the hyperlink in a note."""
		self._instance.SetHyperlinkText = value

	@property
	def set_name(self):
		"""Sets the name for this note."""
		return self._instance.SetName

	@set_name.setter
	def set_name(self, value):
		"""Sets the name for this note."""
		self._instance.SetName = value

	@property
	def set_text(self):
		"""Sets the text of the note."""
		return self._instance.SetText

	@set_text.setter
	def set_text(self, value):
		"""Sets the text of the note."""
		self._instance.SetText = value

	@property
	def set_text_justification(self):
		"""Sets the text justification of a standard note."""
		return self._instance.SetTextJustification

	@set_text_justification.setter
	def set_text_justification(self, value):
		"""Sets the text justification of a standard note."""
		self._instance.SetTextJustification = value

	@property
	def set_text_point(self):
		"""Relocates the note origin to the specified location."""
		return self._instance.SetTextPoint

	@set_text_point.setter
	def set_text_point(self, value):
		"""Relocates the note origin to the specified location."""
		self._instance.SetTextPoint = value

	@property
	def set_text_vertical_justification(self):
		"""Sets the vertical justification of a standard note."""
		return self._instance.SetTextVerticalJustification

	@set_text_vertical_justification.setter
	def set_text_vertical_justification(self, value):
		"""Sets the vertical justification of a standard note."""
		self._instance.SetTextVerticalJustification = value

