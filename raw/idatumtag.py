# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTag_members.html
class IDatumTag:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def filled_triangle(self):
		"""Gets or sets whether a filled triangle or empty triangle attaches to the model on the leader for this datum feature symbol."""
		return self._instance.FilledTriangle

	@filled_triangle.setter
	def filled_triangle(self, value):
		"""Gets or sets whether a filled triangle or empty triangle attaches to the model on the leader for this datum feature symbol."""
		self._instance.FilledTriangle = value

	@property
	def forced_shoulder(self):
		"""Gets whether this datum tag has a forced shoulder on its leader."""
		return self._instance.ForcedShoulder

	@forced_shoulder.setter
	def forced_shoulder(self, value):
		"""Gets whether this datum tag has a forced shoulder on its leader."""
		self._instance.ForcedShoulder = value

	@property
	def leader_orientation(self):
		"""Gets or sets the orientation of the leader for a round datum tag."""
		return self._instance.LeaderOrientation

	@leader_orientation.setter
	def leader_orientation(self, value):
		"""Gets or sets the orientation of the leader for a round datum tag."""
		self._instance.LeaderOrientation = value

	@property
	def shoulder(self):
		"""Gets whether there is a shoulder (or bend) in the leader for this datum tag."""
		return self._instance.Shoulder

	@shoulder.setter
	def shoulder(self, value):
		"""Gets whether there is a shoulder (or bend) in the leader for this datum tag."""
		self._instance.Shoulder = value

	@property
	def get_annotation(self):
		"""Gets the IAnnotation object for this datum tag."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the IAnnotation object for this datum tag."""
		self._instance.GetAnnotation = value

	@property
	def get_arc_at_index(self):
		"""Gets information for the specified arc for this datum tag."""
		return self._instance.GetArcAtIndex

	@get_arc_at_index.setter
	def get_arc_at_index(self, value):
		"""Gets information for the specified arc for this datum tag."""
		self._instance.GetArcAtIndex = value

	@property
	def get_arc_count(self):
		"""Gets the number of arc items in this datum tag."""
		return self._instance.GetArcCount

	@get_arc_count.setter
	def get_arc_count(self, value):
		"""Gets the number of arc items in this datum tag."""
		self._instance.GetArcCount = value

	@property
	def get_arrow_head_at_index(self):
		"""Gets information on the specified arrow head in this datum tag."""
		return self._instance.GetArrowHeadAtIndex

	@get_arrow_head_at_index.setter
	def get_arrow_head_at_index(self, value):
		"""Gets information on the specified arrow head in this datum tag."""
		self._instance.GetArrowHeadAtIndex = value

	@property
	def get_arrow_head_count(self):
		"""Gets the number of arrow heads in the datum tag."""
		return self._instance.GetArrowHeadCount

	@get_arrow_head_count.setter
	def get_arrow_head_count(self, value):
		"""Gets the number of arrow heads in the datum tag."""
		self._instance.GetArrowHeadCount = value

	@property
	def get_display_style(self):
		"""Gets the display style of this datum tag."""
		return self._instance.GetDisplayStyle

	@get_display_style.setter
	def get_display_style(self, value):
		"""Gets the display style of this datum tag."""
		self._instance.GetDisplayStyle = value

	@property
	def get_label(self):
		"""Gets the label for this datum tag."""
		return self._instance.GetLabel

	@get_label.setter
	def get_label(self, value):
		"""Gets the label for this datum tag."""
		self._instance.GetLabel = value

	@property
	def get_line_at_index(self):
		"""Gets information for the specified line in this datum tag."""
		return self._instance.GetLineAtIndex

	@get_line_at_index.setter
	def get_line_at_index(self, value):
		"""Gets information for the specified line in this datum tag."""
		self._instance.GetLineAtIndex = value

	@property
	def get_line_count(self):
		"""Gets the number of lines in this datum tag."""
		return self._instance.GetLineCount

	@get_line_count.setter
	def get_line_count(self, value):
		"""Gets the number of lines in this datum tag."""
		self._instance.GetLineCount = value

	@property
	def get_next(self):
		"""Gets the next datum tag in the view."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next datum tag in the view."""
		self._instance.GetNext = value

	@property
	def get_text_angle_at_index(self):
		"""Gets the text angle for the specified text in this datum tag."""
		return self._instance.GetTextAngleAtIndex

	@get_text_angle_at_index.setter
	def get_text_angle_at_index(self, value):
		"""Gets the text angle for the specified text in this datum tag."""
		self._instance.GetTextAngleAtIndex = value

	@property
	def get_text_at_index(self):
		"""Gets the specified text from this datum tag."""
		return self._instance.GetTextAtIndex

	@get_text_at_index.setter
	def get_text_at_index(self, value):
		"""Gets the specified text from this datum tag."""
		self._instance.GetTextAtIndex = value

	@property
	def get_text_count(self):
		"""Gets the number of text items in the datum tag."""
		return self._instance.GetTextCount

	@get_text_count.setter
	def get_text_count(self, value):
		"""Gets the number of text items in the datum tag."""
		self._instance.GetTextCount = value

	@property
	def get_text_height_at_index(self):
		"""Gets the height of the specified text in this datum tag."""
		return self._instance.GetTextHeightAtIndex

	@get_text_height_at_index.setter
	def get_text_height_at_index(self, value):
		"""Gets the height of the specified text in this datum tag."""
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
	def get_text_position_at_index(self):
		"""Gets the text item's offset relative to note's text point."""
		return self._instance.GetTextPositionAtIndex

	@get_text_position_at_index.setter
	def get_text_position_at_index(self, value):
		"""Gets the text item's offset relative to note's text point."""
		self._instance.GetTextPositionAtIndex = value

	@property
	def get_text_ref_position_at_index(self):
		"""Gets the reference position of the specified text item in this datum tag."""
		return self._instance.GetTextRefPositionAtIndex

	@get_text_ref_position_at_index.setter
	def get_text_ref_position_at_index(self, value):
		"""Gets the reference position of the specified text item in this datum tag."""
		self._instance.GetTextRefPositionAtIndex = value

	@property
	def get_triangle_at_index(self):
		"""Gets the triangle at the specified index of this datum tag."""
		return self._instance.GetTriangleAtIndex

	@get_triangle_at_index.setter
	def get_triangle_at_index(self, value):
		"""Gets the triangle at the specified index of this datum tag."""
		self._instance.GetTriangleAtIndex = value

	@property
	def get_triangle_count(self):
		"""Gets the number of triangles in this datum tag."""
		return self._instance.GetTriangleCount

	@get_triangle_count.setter
	def get_triangle_count(self, value):
		"""Gets the number of triangles in this datum tag."""
		self._instance.GetTriangleCount = value

	@property
	def get_use_doc_display_style(self):
		"""Gets whether this datum tag uses the document setting for its display style."""
		return self._instance.GetUseDocDisplayStyle

	@get_use_doc_display_style.setter
	def get_use_doc_display_style(self, value):
		"""Gets whether this datum tag uses the document setting for its display style."""
		self._instance.GetUseDocDisplayStyle = value

	@property
	def i_get_annotation(self):
		"""Gets the IAnnotation object for this datum feature symbol annotation."""
		return self._instance.IGetAnnotation

	@i_get_annotation.setter
	def i_get_annotation(self, value):
		"""Gets the IAnnotation object for this datum feature symbol annotation."""
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
		"""Gets information for the specified arrow head in this datum tag."""
		return self._instance.IGetArrowHeadAtIndex

	@i_get_arrow_head_at_index.setter
	def i_get_arrow_head_at_index(self, value):
		"""Gets information for the specified arrow head in this datum tag."""
		self._instance.IGetArrowHeadAtIndex = value

	@property
	def i_get_line_at_index(self):
		"""Gets information for the specified line in this datum tag."""
		return self._instance.IGetLineAtIndex

	@i_get_line_at_index.setter
	def i_get_line_at_index(self, value):
		"""Gets information for the specified line in this datum tag."""
		self._instance.IGetLineAtIndex = value

	@property
	def i_get_next(self):
		"""Gets the next datum tag in the view."""
		return self._instance.IGetNext

	@i_get_next.setter
	def i_get_next(self, value):
		"""Gets the next datum tag in the view."""
		self._instance.IGetNext = value

	@property
	def i_get_text_position_at_index(self):
		"""Gets the text item's offset relative to note's text point."""
		return self._instance.IGetTextPositionAtIndex

	@i_get_text_position_at_index.setter
	def i_get_text_position_at_index(self, value):
		"""Gets the text item's offset relative to note's text point."""
		self._instance.IGetTextPositionAtIndex = value

	@property
	def i_get_triangle_at_index(self):
		"""Gets the triangle at the specified index of this datum tag."""
		return self._instance.IGetTriangleAtIndex

	@i_get_triangle_at_index.setter
	def i_get_triangle_at_index(self, value):
		"""Gets the triangle at the specified index of this datum tag."""
		self._instance.IGetTriangleAtIndex = value

	@property
	def set_display_style(self):
		"""Sets the display style of this datum tag."""
		return self._instance.SetDisplayStyle

	@set_display_style.setter
	def set_display_style(self, value):
		"""Sets the display style of this datum tag."""
		self._instance.SetDisplayStyle = value

	@property
	def set_label(self):
		"""Sets the label for this datum tag."""
		return self._instance.SetLabel

	@set_label.setter
	def set_label(self, value):
		"""Sets the label for this datum tag."""
		self._instance.SetLabel = value

	@property
	def set_text(self):
		"""Sets the text of this datum tag."""
		return self._instance.SetText

	@set_text.setter
	def set_text(self, value):
		"""Sets the text of this datum tag."""
		self._instance.SetText = value

