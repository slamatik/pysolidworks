# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlyoutGroup_members.html
class IFlyoutGroup:
	def __init__(self, parent=None):
		self._instance = parent

	def button_count(self):
		"""Gets the number of buttons in this flyout."""
		# return self._instance.ButtonCount
		raise NotImplemented

	def cmd_i_d(self):
		"""Gets the command ID of this flyout."""
		# return self._instance.CmdID
		raise NotImplemented

	@property
	def flyout_type(self):
		"""Gets or sets the type of this flyout."""
		return self._instance.FlyoutType

	@flyout_type.setter
	def flyout_type(self, value):
		"""Gets or sets the type of this flyout."""
		self._instance.FlyoutType = value

	@property
	def icon_list(self):
		"""Gets or sets the paths for the icons for the toolbar buttons for this flyout."""
		return self._instance.IconList

	@icon_list.setter
	def icon_list(self, value):
		"""Gets or sets the paths for the icons for the toolbar buttons for this flyout."""
		self._instance.IconList = value

	@property
	def main_icon_list(self):
		"""Gets or sets the paths for the icons for the buttons for this flyout."""
		return self._instance.MainIconList

	@main_icon_list.setter
	def main_icon_list(self, value):
		"""Gets or sets the paths for the icons for the buttons for this flyout."""
		self._instance.MainIconList = value

	@property
	def add_command_item(self):
		"""Adds an item to a flyout menu."""
		return self._instance.AddCommandItem

	@add_command_item.setter
	def add_command_item(self, value):
		"""Adds an item to a flyout menu."""
		self._instance.AddCommandItem = value

	@property
	def add_context_menu_flyout(self):
		"""Adds this flyout to the context menus of the specified documents and selections."""
		return self._instance.AddContextMenuFlyout

	@add_context_menu_flyout.setter
	def add_context_menu_flyout(self, value):
		"""Adds this flyout to the context menus of the specified documents and selections."""
		self._instance.AddContextMenuFlyout = value

	@property
	def remove_all_command_items(self):
		"""Removes all command items from this flyout."""
		return self._instance.RemoveAllCommandItems

	@remove_all_command_items.setter
	def remove_all_command_items(self, value):
		"""Removes all command items from this flyout."""
		self._instance.RemoveAllCommandItems = value

	@property
	def remove_command_item(self):
		"""Removes a command item at the specified position."""
		return self._instance.RemoveCommandItem

	@remove_command_item.setter
	def remove_command_item(self, value):
		"""Removes a command item at the specified position."""
		self._instance.RemoveCommandItem = value

	@property
	def replace_command_item(self):
		"""Replaces a command item at the specified position."""
		return self._instance.ReplaceCommandItem

	@replace_command_item.setter
	def replace_command_item(self, value):
		"""Replaces a command item at the specified position."""
		self._instance.ReplaceCommandItem = value

