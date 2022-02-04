# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html
class IPropertyManagerPage2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def pinned(self):
		"""Gets or sets the state of the pushpin on a PropertyManager page."""
		return self._instance.Pinned

	@pinned.setter
	def pinned(self, value):
		"""Gets or sets the state of the pushpin on a PropertyManager page."""
		self._instance.Pinned = value

	@property
	def title(self):
		"""Gets or sets the title of the PropertyManager page."""
		return self._instance.Title

	@title.setter
	def title(self, value):
		"""Gets or sets the title of the PropertyManager page."""
		self._instance.Title = value

	@property
	def add_control(self):
		"""Adds a control to this PropertyManager page."""
		return self._instance.AddControl2

	@add_control.setter
	def add_control(self, value):
		"""Adds a control to this PropertyManager page."""
		self._instance.AddControl2 = value

	@property
	def add_group_box(self):
		"""Adds a group box to a PropertyManager page."""
		return self._instance.AddGroupBox

	@add_group_box.setter
	def add_group_box(self, value):
		"""Adds a group box to a PropertyManager page."""
		self._instance.AddGroupBox = value

	@property
	def add_menu_popup_item(self):
		"""Adds a menu item to the pop-up menu for this PropertyManager page."""
		return self._instance.AddMenuPopupItem

	@add_menu_popup_item.setter
	def add_menu_popup_item(self, value):
		"""Adds a menu item to the pop-up menu for this PropertyManager page."""
		self._instance.AddMenuPopupItem = value

	@property
	def add_tab(self):
		"""Adds a tab to a PropertyManager page."""
		return self._instance.AddTab

	@add_tab.setter
	def add_tab(self, value):
		"""Adds a tab to a PropertyManager page."""
		self._instance.AddTab = value

	@property
	def close(self):
		"""Closes the current page in the PropertyManager."""
		return self._instance.Close

	@close.setter
	def close(self, value):
		"""Closes the current page in the PropertyManager."""
		self._instance.Close = value

	@property
	def enable_button(self):
		"""Sets whether to enable the buttons on the PropertyManager."""
		return self._instance.EnableButton

	@enable_button.setter
	def enable_button(self, value):
		"""Sets whether to enable the buttons on the PropertyManager."""
		self._instance.EnableButton = value

	@property
	def get_focus(self):
		"""Gets the ID of the control that has focus on this PropertyManager page."""
		return self._instance.GetFocus

	@get_focus.setter
	def get_focus(self, value):
		"""Gets the ID of the control that has focus on this PropertyManager page."""
		self._instance.GetFocus = value

	@property
	def i_add_group_box(self):
		"""Adds a group box to a PropertyManager page."""
		return self._instance.IAddGroupBox

	@i_add_group_box.setter
	def i_add_group_box(self, value):
		"""Adds a group box to a PropertyManager page."""
		self._instance.IAddGroupBox = value

	@property
	def set_cursor(self):
		"""Sets the cursor after a selection is made in the SOLIDWORKS graphics area."""
		return self._instance.SetCursor

	@set_cursor.setter
	def set_cursor(self, value):
		"""Sets the cursor after a selection is made in the SOLIDWORKS graphics area."""
		self._instance.SetCursor = value

	@property
	def set_focus(self):
		"""Sets focus on the specified control on this PropertyManager page."""
		return self._instance.SetFocus

	@set_focus.setter
	def set_focus(self, value):
		"""Sets focus on the specified control on this PropertyManager page."""
		self._instance.SetFocus = value

	@property
	def set_message(self):
		"""Sets the message in this PropertyManager page."""
		return self._instance.SetMessage3

	@set_message.setter
	def set_message(self, value):
		"""Sets the message in this PropertyManager page."""
		self._instance.SetMessage3 = value

	@property
	def set_title_bitmap(self):
		"""Sets the bitmap to display in the title of this PropertyManager page."""
		return self._instance.SetTitleBitmap2

	@set_title_bitmap.setter
	def set_title_bitmap(self, value):
		"""Sets the bitmap to display in the title of this PropertyManager page."""
		self._instance.SetTitleBitmap2 = value

	@property
	def set_title_bitmapx(self):
		"""Sets the bitmap to display in the title of this PropertyManager page."""
		return self._instance.SetTitleBitmapx64

	@set_title_bitmapx.setter
	def set_title_bitmapx(self, value):
		"""Sets the bitmap to display in the title of this PropertyManager page."""
		self._instance.SetTitleBitmapx64 = value

	@property
	def show(self):
		"""Shows the PropertyManager page."""
		return self._instance.Show2

	@show.setter
	def show(self, value):
		"""Shows the PropertyManager page."""
		self._instance.Show2 = value

