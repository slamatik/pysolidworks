# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageControl_members.html
class IPropertyManagerPageControl:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def background_color(self):
		"""Gets or sets the background color of an edit box or label on the PropertyManager page."""
		return self._instance.BackgroundColor

	@background_color.setter
	def background_color(self, value):
		"""Gets or sets the background color of an edit box or label on the PropertyManager page."""
		self._instance.BackgroundColor = value

	@property
	def enabled(self):
		"""Gets or sets the state of the PropertyManager page."""
		return self._instance.Enabled

	@enabled.setter
	def enabled(self, value):
		"""Gets or sets the state of the PropertyManager page."""
		self._instance.Enabled = value

	@property
	def left(self):
		"""Gets or sets the left edge of the control on a PropertyManager page."""
		return self._instance.Left

	@left.setter
	def left(self, value):
		"""Gets or sets the left edge of the control on a PropertyManager page."""
		self._instance.Left = value

	@property
	def options_for_resize(self):
		"""Gets or sets how to override the SOLIDWORKS default behavior when changing the width of a PropertyManager page."""
		return self._instance.OptionsForResize

	@options_for_resize.setter
	def options_for_resize(self, value):
		"""Gets or sets how to override the SOLIDWORKS default behavior when changing the width of a PropertyManager page."""
		self._instance.OptionsForResize = value

	@property
	def text_color(self):
		"""Gets or sets color of the text of a label on a PropertyManager page."""
		return self._instance.TextColor

	@text_color.setter
	def text_color(self, value):
		"""Gets or sets color of the text of a label on a PropertyManager page."""
		self._instance.TextColor = value

	@property
	def tip(self):
		"""Gets or sets the ToolTip for this control on a PropertyManager page."""
		return self._instance.Tip

	@tip.setter
	def tip(self, value):
		"""Gets or sets the ToolTip for this control on a PropertyManager page."""
		self._instance.Tip = value

	@property
	def top(self):
		"""Gets or sets the top edge of the control on a PropertyManager page."""
		return self._instance.Top

	@top.setter
	def top(self, value):
		"""Gets or sets the top edge of the control on a PropertyManager page."""
		self._instance.Top = value

	@property
	def visible(self):
		"""Gets or sets visibility state of a PropertyManager page."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets visibility state of a PropertyManager page."""
		self._instance.Visible = value

	@property
	def width(self):
		"""Gets or sets the width of the control on a PropertyManager page."""
		return self._instance.Width

	@width.setter
	def width(self, value):
		"""Gets or sets the width of the control on a PropertyManager page."""
		self._instance.Width = value

	@property
	def get_group_box(self):
		"""Gets the PropertyManager group box to which this control belongs."""
		return self._instance.GetGroupBox

	@get_group_box.setter
	def get_group_box(self, value):
		"""Gets the PropertyManager group box to which this control belongs."""
		self._instance.GetGroupBox = value

	@property
	def set_picture_label_by_name(self):
		"""Sets the bitmap label for this control on a PropertyManager page."""
		return self._instance.SetPictureLabelByName

	@set_picture_label_by_name.setter
	def set_picture_label_by_name(self, value):
		"""Sets the bitmap label for this control on a PropertyManager page."""
		self._instance.SetPictureLabelByName = value

	@property
	def set_standard_picture_label(self):
		"""Sets the bitmap's or PNG image's label for this control on a PropertyManager page."""
		return self._instance.SetStandardPictureLabel

	@set_standard_picture_label.setter
	def set_standard_picture_label(self, value):
		"""Sets the bitmap's or PNG image's label for this control on a PropertyManager page."""
		self._instance.SetStandardPictureLabel = value

	@property
	def show_bubble_tooltip(self):
		"""Displays a bubble ToolTip containing the specified title, message, and bitmap."""
		return self._instance.ShowBubbleTooltip

	@show_bubble_tooltip.setter
	def show_bubble_tooltip(self, value):
		"""Displays a bubble ToolTip containing the specified title, message, and bitmap."""
		self._instance.ShowBubbleTooltip = value

