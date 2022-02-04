# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageLabel_members.html
class IPropertyManagerPageLabel:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bold(self):
		"""Gets or sets whether the range of specified characters are bolded in this ProperytManager label."""
		return self._instance.Bold

	@bold.setter
	def bold(self, value):
		"""Gets or sets whether the range of specified characters are bolded in this ProperytManager label."""
		self._instance.Bold = value

	@property
	def caption(self):
		"""Gets or sets the caption for this label."""
		return self._instance.Caption

	@caption.setter
	def caption(self, value):
		"""Gets or sets the caption for this label."""
		self._instance.Caption = value

	@property
	def character_background_color(self):
		"""Gets or sets the background color for the specified range of characters in this PropertyManager label."""
		return self._instance.CharacterBackgroundColor

	@character_background_color.setter
	def character_background_color(self, value):
		"""Gets or sets the background color for the specified range of characters in this PropertyManager label."""
		self._instance.CharacterBackgroundColor = value

	@property
	def character_color(self):
		"""Gets or sets the color of the specified characters in this PropertyManager label."""
		return self._instance.CharacterColor

	@character_color.setter
	def character_color(self, value):
		"""Gets or sets the color of the specified characters in this PropertyManager label."""
		self._instance.CharacterColor = value

	@property
	def font(self):
		"""Gets or sets the font for the specified characters in this PropertyManager label."""
		return self._instance.Font

	@font.setter
	def font(self, value):
		"""Gets or sets the font for the specified characters in this PropertyManager label."""
		self._instance.Font = value

	@property
	def height(self):
		"""Gets or sets the height of this label."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of this label."""
		self._instance.Height = value

	@property
	def italic(self):
		"""Gets or sets whether to italicize the specified range of characters in this PropertyManager label."""
		return self._instance.Italic

	@italic.setter
	def italic(self, value):
		"""Gets or sets whether to italicize the specified range of characters in this PropertyManager label."""
		self._instance.Italic = value

	@property
	def line_offset(self):
		"""Gets or sets whether to raise or lower the specified characters above or below their baselines, relative to their heights, in this PropertyManager label."""
		return self._instance.LineOffset

	@line_offset.setter
	def line_offset(self, value):
		"""Gets or sets whether to raise or lower the specified characters above or below their baselines, relative to their heights, in this PropertyManager label."""
		self._instance.LineOffset = value

	@property
	def size_ratio(self):
		"""Gets or sets the size of the specified characters in this PropertyManager label."""
		return self._instance.SizeRatio

	@size_ratio.setter
	def size_ratio(self, value):
		"""Gets or sets the size of the specified characters in this PropertyManager label."""
		self._instance.SizeRatio = value

	@property
	def style(self):
		"""Gets or sets style-related properties of this label."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets style-related properties of this label."""
		self._instance.Style = value

	@property
	def underline(self):
		"""Gets or sets whether to apply the specified underline style to the specified range of characters in this PropertyManager label."""
		return self._instance.Underline

	@underline.setter
	def underline(self, value):
		"""Gets or sets whether to apply the specified underline style to the specified range of characters in this PropertyManager label."""
		self._instance.Underline = value

