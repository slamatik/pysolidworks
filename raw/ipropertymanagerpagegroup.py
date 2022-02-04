# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageGroup_members.html
class IPropertyManagerPageGroup:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def background_color(self):
		"""Gets or sets the background color of this PropertyManager group box."""
		return self._instance.BackgroundColor

	@background_color.setter
	def background_color(self, value):
		"""Gets or sets the background color of this PropertyManager group box."""
		self._instance.BackgroundColor = value

	@property
	def caption(self):
		"""Gets or sets the title for this group box."""
		return self._instance.Caption

	@caption.setter
	def caption(self, value):
		"""Gets or sets the title for this group box."""
		self._instance.Caption = value

	@property
	def checked(self):
		"""Gets or sets the setting of a check box in the title of a group box on a PropertyManager page."""
		return self._instance.Checked

	@checked.setter
	def checked(self, value):
		"""Gets or sets the setting of a check box in the title of a group box on a PropertyManager page."""
		self._instance.Checked = value

	@property
	def expanded(self):
		"""Gets or sets the group box expansion state."""
		return self._instance.Expanded

	@expanded.setter
	def expanded(self, value):
		"""Gets or sets the group box expansion state."""
		self._instance.Expanded = value

	@property
	def visible(self):
		"""Gets or sets the group box visibility state."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets the group box visibility state."""
		self._instance.Visible = value

	@property
	def add_control(self):
		"""Adds a control to this PropertyManager page group box."""
		return self._instance.AddControl2

	@add_control.setter
	def add_control(self, value):
		"""Adds a control to this PropertyManager page group box."""
		self._instance.AddControl2 = value

