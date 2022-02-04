# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParagraphs_members.html
class IParagraphs:
	def __init__(self, parent=None):
		self._instance = parent

	def count(self):
		"""Gets the number of paragraphs in the annotation."""
		# return self._instance.Count
		raise NotImplemented

	@property
	def current_paragraph(self):
		"""Gets or sets the current paragraph."""
		return self._instance.CurrentParagraph

	@current_paragraph.setter
	def current_paragraph(self, value):
		"""Gets or sets the current paragraph."""
		self._instance.CurrentParagraph = value

	@property
	def get_bullets_and_numbering(self):
		"""Gets the list properties of the current paragraph."""
		return self._instance.GetBulletsAndNumbering

	@get_bullets_and_numbering.setter
	def get_bullets_and_numbering(self, value):
		"""Gets the list properties of the current paragraph."""
		self._instance.GetBulletsAndNumbering = value

	@property
	def get_formatting(self):
		"""Gets the formatting of the current paragraph."""
		return self._instance.GetFormatting

	@get_formatting.setter
	def get_formatting(self, value):
		"""Gets the formatting of the current paragraph."""
		self._instance.GetFormatting = value

	@property
	def get_indentation(self):
		"""Gets the indentation of the current paragraph."""
		return self._instance.GetIndentation

	@get_indentation.setter
	def get_indentation(self, value):
		"""Gets the indentation of the current paragraph."""
		self._instance.GetIndentation = value

	@property
	def get_text(self):
		"""Gets the text of the current paragraph."""
		return self._instance.GetText

	@get_text.setter
	def get_text(self, value):
		"""Gets the text of the current paragraph."""
		self._instance.GetText = value

	@property
	def get_text_segment_count(self):
		"""Gets the number of text segments in the current paragraph."""
		return self._instance.GetTextSegmentCount

	@get_text_segment_count.setter
	def get_text_segment_count(self, value):
		"""Gets the number of text segments in the current paragraph."""
		self._instance.GetTextSegmentCount = value

	@property
	def get_text_segment_format(self):
		"""Gets the text format for the specified text segment in the current paragraph."""
		return self._instance.GetTextSegmentFormat

	@get_text_segment_format.setter
	def get_text_segment_format(self, value):
		"""Gets the text format for the specified text segment in the current paragraph."""
		self._instance.GetTextSegmentFormat = value

	@property
	def get_text_segment_text(self):
		"""Gets the text of the specified text segment in the current paragraph."""
		return self._instance.GetTextSegmentText

	@get_text_segment_text.setter
	def get_text_segment_text(self, value):
		"""Gets the text of the specified text segment in the current paragraph."""
		self._instance.GetTextSegmentText = value

	@property
	def set_bullets_and_numbering(self):
		"""Sets the list properties of the current paragraph."""
		return self._instance.SetBulletsAndNumbering

	@set_bullets_and_numbering.setter
	def set_bullets_and_numbering(self, value):
		"""Sets the list properties of the current paragraph."""
		self._instance.SetBulletsAndNumbering = value

	@property
	def set_formatting(self):
		"""Sets the formatting of the current paragraph."""
		return self._instance.SetFormatting

	@set_formatting.setter
	def set_formatting(self, value):
		"""Sets the formatting of the current paragraph."""
		self._instance.SetFormatting = value

	@property
	def set_indentation(self):
		"""Sets the indentation of the current paragraph."""
		return self._instance.SetIndentation

	@set_indentation.setter
	def set_indentation(self, value):
		"""Sets the indentation of the current paragraph."""
		self._instance.SetIndentation = value

	@property
	def set_text_segment_format(self):
		"""Sets the text format for the specified text segment in the current paragraph."""
		return self._instance.SetTextSegmentFormat

	@set_text_segment_format.setter
	def set_text_segment_format(self, value):
		"""Sets the text format for the specified text segment in the current paragraph."""
		self._instance.SetTextSegmentFormat = value

	@property
	def update_paragraph(self):
		"""Updates the model with the changes made to the current paragraph."""
		return self._instance.UpdateParagraph

	@update_paragraph.setter
	def update_paragraph(self, value):
		"""Updates the model with the changes made to the current paragraph."""
		self._instance.UpdateParagraph = value

