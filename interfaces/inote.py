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

    def angle(self, value):
        """
        Controls the rotation angle of this note."
        :param value: Rotation angle, in radians, of this note
        :return: None
        """
        self._instance.Angle = value

    def behind_sheet(self):
        """Places this note, located on the sheet format in a drawing, behind the drawing sheet."""
        # return self._instance.BehindSheet
        raise NotImplemented

    def has_multiple_fonts(self):
        """Gets whether a note contains multiple fonts."""
        return self._instance.HasMultipleFonts

    @property
    def include_dim_prefix_suffix_tolerance(self):
        """Gets or sets whether to include the dimension prefix, suffix, and tolerance in this dimension note."""
        return self._instance.IncludeDimPrefixSuffixTolerance

    @include_dim_prefix_suffix_tolerance.setter
    def include_dim_prefix_suffix_tolerance(self, value):
        """Gets or sets whether to include the dimension prefix, suffix, and tolerance in this dimension note."""
        self._instance.IncludeDimPrefixSuffixTolerance = value

    def is_bend_line_note(self):
        """Gets whether this note is a bendline note."""
        return self._instance.IsBendLineNote

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
        """Gets and sets whether to select the To bounding box option for leaders in this note's PropertyManager page.
        """
        return self._instance.ToBoundingBox

    @to_bounding_box.setter
    def to_bounding_box(self, value):
        """Gets and sets whether to select the To bounding box option for leaders in this note's PropertyManager page.
        """
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
        """Gets or sets whether to place this note, specified to be a watermark, behind the geometry in a part or
        assembly."""
        return self._instance.WatermarkBehindGeometry

    @watermark_behind_geometry.setter
    def watermark_behind_geometry(self, value):
        """Gets or sets whether to place this note, specified to be a watermark, behind the geometry in a part or
        assembly."""
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

    def get_annotation(self):
        """Gets the annotation for this specific note."""
        # return self._instance.GetAnnotation
        raise NotImplemented

    def get_arc_at_index(self, index):
        """
        Gets information for the specified arc in this note.
        :param index: Index of the desired arc where the index begins at 0
        """
        # return self._instance.GetArcAtIndex(index)
        raise NotImplemented

    def get_arc_count(self):
        """Gets the number of arcs in the note."""
        # return self._instance.GetArcCount
        raise NotImplemented

    def get_arrow_head_at_index(self, index):
        """
        Gets information on the specified arrowhead in this note.
        :param index: Index of the desired arrowhead where the index begins at 0
        """
        # return self._instance.GetArrowHeadAtIndex(index)
        raise NotImplemented

    def get_arrow_head_count(self):
        """Gets the number of arrowheads in the note."""
        # return self._instance.GetArrowHeadCount
        raise NotImplemented

    def get_arrow_head_info(self):
        """Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
        # return self._instance.GetArrowHeadInfo
        raise NotImplemented

    def get_attach_pos(self):
        """Gets the attachment point of this note."""
        # return self._instance.GetAttachPos
        raise NotImplemented

    def get_balloon_info(self):
        """Gets information describing the geometry of the balloon, if any, that encloses the note text."""
        # return self._instance.GetBalloonInfo
        raise NotImplemented

    def get_balloon_padding(self):
        """Gets the balloon padding of this note."""
        # return self._instance.GetBalloonPadding
        raise NotImplemented

    def get_balloon_size(self):
        """Gets the balloon size or fit of this note."""
        # return self._instance.GetBalloonSize
        raise NotImplemented

    def get_balloon_stack(self):
        """Gets the balloon stack for this balloon note."""
        # return self._instance.GetBalloonStack
        raise NotImplemented

    def get_balloon_style(self):
        """Gets the balloon style of this note."""
        # return self._instance.GetBalloonStyle
        raise NotImplemented

    def get_bend_line_values(self, up, angle, radius, points):
        """
        Gets the values of a bend line note.
        :param up: True if the bend is up, false if the bend is down
        :param angle: Angle of the bend
        :param radius: Radius of the bend
        :param points: Array of doubles (see Remarks)
        """
        # return self._instance.GetBendLineValues2(up, angle, radius, points)
        raise NotImplemented

    def get_bom_balloon_text(self, which_one):
        """
        Gets the text for this BOM balloon note.
        :param which_one: True for the upper text, false for the lower text
        """
        # return self._instance.GetBomBalloonText(which_one)
        raise NotImplemented

    def get_bom_balloon_text_style(self, which_one):
        """
        Gets the text style of this BOM balloon note.
        :param which_one: True for the upper text, false for the lower text
        """
        # return self._instance.GetBomBalloonTextStyle(which_one)
        raise NotImplemented

    def get_extent(self):
        """Gets the extents of a note in sheet space."""
        # return self._instance.GetExtent
        raise NotImplemented

    def get_font_info(self):
        """Gets with the note's font information."""
        # return self._instance.GetFontInfo
        raise NotImplemented

    def get_height(self):
        """Get the note's height."""
        # return self._instance.GetHeight
        raise NotImplemented

    def get_height_in_points(self):
        """Gets the height of this note in points (for example, 8, 10, 12, and so on)."""
        # return self._instance.GetHeightInPoints
        raise NotImplemented

    def get_hyperlink_text(self):
        """Gets the hyperlink in a note."""
        # return self._instance.GetHyperlinkText
        raise NotImplemented

    def get_leader_at_index(self, index):
        """
        Gets information about the specified leader on this note.
        :param index: Index of leader
        """
        # return self._instance.GetLeaderAtIndex(index)
        raise NotImplemented

    def get_leader_count(self):
        """Gets the number of leaders on this note."""
        # return self._instance.GetLeaderCount
        raise NotImplemented

    def get_leader_info(self):
        """Gets information describing the layout of the note leader lines."""
        # return self._instance.GetLeaderInfo
        raise NotImplemented

    def get_leader_num_points_at(self, index):
        """
        Gets the number of points in the specified leader of this note.
        :param index: Index of leader on this note
        """
        # return self._instance.GetLeaderNumPointsAt(index)
        raise NotImplemented

    def get_line_at_index(self, index):
        """
        Gets information for the specified line.
        :param index: Zero-based index of the desired line
        """
        # return self._instance.GetLineAtIndex(index)
        raise NotImplemented

    def get_line_count(self):
        """Gets the number of line segments in this note."""
        # return self._instance.GetLineCount
        raise NotImplemented

    def get_name(self):
        """Gets the name of this note."""
        # return self._instance.GetName
        raise NotImplemented

    def get_next(self):
        """Gets the next note in drawing view."""
        # return self._instance.GetNext
        raise NotImplemented

    def get_text(self):
        """Gets this note's text."""
        # return self._instance.GetText
        raise NotImplemented

    def get_text_angle_at_index(self, index):
        """
        Gets the text angle for the specified piece of text in this note.
        :param index: Index of the desired piece of text where the index begins at 1
        """
        # return self._instance.GetTextAngleAtIndex(index)
        raise NotImplemented

    def get_text_at_index(self, index):
        """
        Gets the specified text in this note.
        :param index: Index position of the text; index begins at 1
        """
        # return self._instance.GetTextAtIndex(index)
        raise NotImplemented

    def get_text_count(self):
        """Gets the number of text items in this note."""
        # return self._instance.GetTextCount
        raise NotImplemented

    def get_text_font_at_index(self, index):
        """
        Gets the font used by the specified text item in this note.
        :param index: Index of the desired piece of text where the index begins at 0
        """
        # return self._instance.GetTextFontAtIndex(index)
        raise NotImplemented

    def get_text_height_at_index(self, index):
        """
        Gets the text height for the specified piece of text in this note.
        :param index: Index of the desired piece of text where the index begins at 0
        """
        # return self._instance.GetTextHeightAtIndex(index)
        raise NotImplemented

    def get_text_invert_at_index(self, index):
        """
        Gets the specified text item's invert flag.
        :param index: Index of the desired piece of text where the index begins at 0
        """
        # return self._instance.GetTextInvertAtIndex(index)
        raise NotImplemented

    def get_text_justification(self):
        """Gets the text justification of a standard note."""
        # return self._instance.GetTextJustification
        raise NotImplemented

    def get_text_line_spacing_at_index(self, index):
        """
        Gets the line spacing for this note.
        :param index: 1-based index position of the text
        """
        # return self._instance.GetTextLineSpacingAtIndex(index)
        raise NotImplemented

    def get_text_point(self):
        """Gets the note's text reference point (i.e., note origin)."""
        # return self._instance.GetTextPoint2
        raise NotImplemented

    def get_text_position_at_index(self, index):
        """
        Gets the text item's offset relative to the document origin.
        :param index: Index of the piece of text where the index begins at 1
        """
        # return self._instance.GetTextPositionAtIndex(index)
        raise NotImplemented

    def get_text_ref_position_at_index(self, index):
        """
        Gets the specified text item's reference position in this note; for example, the upper left, lower left, or
        center.
        :param index: Index of the desired piece of text where the index begins at 1
        """
        # return self._instance.GetTextRefPositionAtIndex(index)
        raise NotImplemented

    def get_text_vertical_justification(self):
        """Gets the vertical justification of a standard note."""
        # return self._instance.GetTextVerticalJustification
        raise NotImplemented

    def get_triangle_at_index(self, index):
        """
        Gets the triangle at the specified index.
        :param index: Index of the triangle where the index begins at 0
        """
        # return self._instance.GetTriangleAtIndex(index)
        raise NotImplemented

    def get_triangle_count(self):
        """Gets the number of triangles in this note."""
        # return self._instance.GetTriangleCount
        raise NotImplemented

    def get_upper_right(self):
        """Gets the note's upper-right text point."""
        # return self._instance.GetUpperRight
        raise NotImplemented

    def has_balloon(self):
        """Gets whether this note has a balloon."""
        # return self._instance.HasBalloon
        raise NotImplemented

    def has_extra_leader(self):
        """Gets whether this note has a bent or straight leaderline."""
        # return self._instance.HasExtraLeader
        raise NotImplemented

    def i_get_annotation(self):
        """Gets the annotation for this specific note."""
        # return self._instance.IGetAnnotation
        raise NotImplemented

    def i_get_arc_at_index(self, index):
        """
        Gets information for the specified arc in this note.
        :param index: Index of the desired arc where the index begins at 0
        """
        # return self._instance.IGetArcAtIndex(index)
        raise NotImplemented

    def i_get_arrow_head_at_index(self, index):
        """
        Gets information on the specified arrowhead in this note.
        :param index: Index of the desired arrowhead where the index begins at 0
        """
        # return self._instance.IGetArrowHeadAtIndex(index)
        raise NotImplemented

    def i_get_arrow_head_info(self):
        """Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line."""
        # return self._instance.IGetArrowHeadInfo
        raise NotImplemented

    def i_get_attach_pos(self):
        """Gets the attachment point of this note."""
        # return self._instance.IGetAttachPos
        raise NotImplemented

    def i_get_balloon_info(self):
        """Gets information describing the geometry of the balloon, if any, that encloses the note text."""
        # return self._instance.IGetBalloonInfo
        raise NotImplemented

    def i_get_extent(self):
        """Gets the extents of a note in sheet space."""
        # return self._instance.IGetExtent
        raise NotImplemented

    def i_get_font_info(self):
        """Gets with the note's font information."""
        # return self._instance.IGetFontInfo
        raise NotImplemented

    def i_get_leader_at_index(self, index, point_count):
        """
        Gets information about the specified leader on this note.
        :param index: Index of leader
        :param point_count: Number of (x,y,z) points returned in the array
        """
        # return self._instance.IGetLeaderAtIndex(index, point_count)
        raise NotImplemented

    def i_get_leader_info(self, point_count):
        """
        Gets information describing the layout of the note leader lines.
        :param point_count: Number of points
        """
        # return self._instance.IGetLeaderInfo(point_count)
        raise NotImplemented

    def i_get_line_at_index(self, index):
        """
        Gets information for the specified line.
        :param index: Index of the desired line where the index begins at 0
        """
        # return self._instance.IGetLineAtIndex(index)
        raise NotImplemented

    def i_get_next(self):
        """Gets the next note in drawing view."""
        # return self._instance.IGetNext
        raise NotImplemented

    def i_get_text_point(self):
        """Gets the note's text reference point (i.e., note origin)."""
        # return self._instance.IGetTextPoint2
        raise NotImplemented

    def i_get_text_position_at_index(self, index):
        """
        Gets the text item's offset relative to the document origin.
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

    def i_get_upper_right(self):
        """Gets the note's upper-right text point."""
        # return self._instance.IGetUpperRight
        raise NotImplemented

    def is_attached(self):
        """Gets whether the note is attached."""
        # return self._instance.IsAttached
        raise NotImplemented

    def is_bom_balloon(self):
        """Gets whether this note has a BOM balloon."""
        # return self._instance.IsBomBalloon
        raise NotImplemented

    def is_stacked_balloon(self):
        """Gets whether this note is part of a stacked balloon."""
        # return self._instance.IsStackedBalloon
        raise NotImplemented

    def is_stacked_balloon_master(self):
        """Gets whether this note is the master note of a balloon stack."""
        # return self._instance.IsStackedBalloonMaster
        raise NotImplemented

    def make_stacked_balloon(self, stacked_balloon_options):
        """
        Converts this balloon to a stacked balloon.
        :param stacked_balloon_options: IStackedBalloonOptions
        """
        # return self._instance.MakeStackedBalloon(stacked_balloon_options)
        raise NotImplemented

    def set_balloon(self, style, size):
        """
        Sets the balloon style, size, and fit for this note.
        :param style: Balloon style as defined in swBalloonStyle_e
        :param size: Balloon size or fit as defined in swBalloonFit_e
        """
        # return self._instance.SetBalloon(style, size)
        raise NotImplemented

    def set_balloon_padding(self, padding):
        """
        Sets the padding for this balloon note.
        :param padding: Balloon padding
        """
        # return self._instance.SetBalloonPadding(padding)
        raise NotImplemented

    def set_bom_balloon_text(self, upper_text_style, upper_text, lower_text_style, lower_text):
        """
        Sets the text for this BOM balloon note.
        :param upper_text_style: Style for the upper text as defined in swDetailingNoteTextContent_e
        :param upper_text: Upper text
        :param lower_text_style: Style for the lower text as defined in swDetailingNoteTextContent_e
        :param lower_text: Lower text
        """
        # return self._instance.SetBomBalloonText(upper_text_style, upper_text, lower_text_style, lower_text)
        raise NotImplemented

    def set_height(self, height_in):
        """
        Sets the height of this note in meters.
        :param height_in: Height for this note in meters
        """
        # return self._instance.SetHeight(height_in)
        raise NotImplemented

    def set_height_in_points(self, height_in):
        """
        Sets the height of this note in points (for example, 8, 10, 12, and so on).
        :param height_in: Height for this note in points
        """
        # return self._instance.SetHeightInPoints(height_in)
        raise NotImplemented

    def set_hyperlink_text(self, text):
        """
        Sets the hyperlink in a note.
        :param text: Text for hyperlink
        """
        # return self._instance.SetHyperlinkText(text)
        raise NotImplemented

    def set_name(self, name_in):
        """
        Sets the name for this note.
        :param name_in: Note name
        """
        # return self._instance.SetName(name_in)
        raise NotImplemented

    def set_text(self, txt):
        """
        Sets the text of the note.
        :param txt: Text to replace the current note text
        """
        # return self._instance.SetText(txt)
        raise NotImplemented

    def set_text_justification(self, justification):
        """
        Sets the text justification of a standard note.
        :param justification: Text justification as defined in swTextJustification_e
        """
        # return self._instance.SetTextJustification(justification)
        raise NotImplemented

    def set_text_point(self, x, y, z):
        """
        Relocates the note origin to the specified location.
        :param x: x coordinate of text reference point
        :param y: y coordinate of text reference point
        :param z: z coordinate of text reference point
        """
        # return self._instance.SetTextPoint(x, y, z)
        raise NotImplemented

    def set_text_vertical_justification(self, justification):
        """
        Sets the vertical justification of a standard note.
        :param justification: Vertical justification as defined in swTextAlignmentVertical_e
        """
        # return self._instance.SetTextVerticalJustification(justification)
        raise NotImplemented
