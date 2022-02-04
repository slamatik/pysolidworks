# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.html
class ICommandGroup:
	def __init__(self, parent=None):
		self._instance = parent

	def command_i_d(self, command_index):
		"""
		Gets the command ID for the specified item in the CommandGroup.
		:param command_index: Index of the item in the CommandGroup
		"""
		# return self._instance.CommandID(command_index)
		raise NotImplemented

	@property
	def custom_names(self):
		"""Gets or sets the custom names in the CommandGroup."""
		return self._instance.CustomNames

	@custom_names.setter
	def custom_names(self, value):
		"""Gets or sets the custom names in the CommandGroup."""
		self._instance.CustomNames = value

	@property
	def docking_state(self):
		"""Gets or sets the docking state of the toolbar in the CommandGroup."""
		return self._instance.DockingState

	@docking_state.setter
	def docking_state(self, value):
		"""Gets or sets the docking state of the toolbar in the CommandGroup."""
		self._instance.DockingState = value

	@property
	def has_enabled_button(self):
		"""Gets whether any buttons in this CommandGroup are enabled."""
		return self._instance.HasEnabledButton

	@has_enabled_button.setter
	def has_enabled_button(self, value):
		"""Gets whether any buttons in this CommandGroup are enabled."""
		self._instance.HasEnabledButton = value

	@property
	def has_menu(self):
		"""Gets or sets whether this CommandGroup has a menu."""
		return self._instance.HasMenu

	@has_menu.setter
	def has_menu(self, value):
		"""Gets or sets whether this CommandGroup has a menu."""
		self._instance.HasMenu = value

	@property
	def has_toolbar(self):
		"""Gets or sets whether this CommandGroup has a toolbar."""
		return self._instance.HasToolbar

	@has_toolbar.setter
	def has_toolbar(self, value):
		"""Gets or sets whether this CommandGroup has a toolbar."""
		self._instance.HasToolbar = value

	@property
	def icon_list(self):
		"""Gets or sets the paths for the icons for the toolbar buttons and separators for this CommandGroup."""
		return self._instance.IconList

	@icon_list.setter
	def icon_list(self, value):
		"""Gets or sets the paths for the icons for the toolbar buttons and separators for this CommandGroup."""
		self._instance.IconList = value

	@property
	def main_icon_list(self):
		"""Gets or sets the paths for the icons for the buttons for this CommandGroup."""
		return self._instance.MainIconList

	@main_icon_list.setter
	def main_icon_list(self, value):
		"""Gets or sets the paths for the icons for the buttons for this CommandGroup."""
		self._instance.MainIconList = value

	@property
	def menu_position(self):
		"""Gets or sets the position of the CommandGroup for the specified document templates."""
		return self._instance.MenuPosition

	@menu_position.setter
	def menu_position(self, value):
		"""Gets or sets the position of the CommandGroup for the specified document templates."""
		self._instance.MenuPosition = value

	@property
	def name(self):
		"""Gets the name of the CommandGroup."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets the name of the CommandGroup."""
		self._instance.Name = value

	@property
	def number_of_group_items(self):
		"""Gets the number of items in the CommandGroup."""
		return self._instance.NumberOfGroupItems

	@number_of_group_items.setter
	def number_of_group_items(self, value):
		"""Gets the number of items in the CommandGroup."""
		self._instance.NumberOfGroupItems = value

	@property
	def select_type(self):
		"""This property:

gets the type of object selected on the context sensitive, pop-up menu. 
sets the type of object that the user must select to show the context sensitive, pop-up menu."""
		return self._instance.SelectType

	@select_type.setter
	def select_type(self, value):
		"""This property:

gets the type of object selected on the context sensitive, pop-up menu. 
sets the type of object that the user must select to show the context sensitive, pop-up menu."""
		self._instance.SelectType = value

	@property
	def show_in_document_type(self):
		"""Gets or sets the types of documents to show this CommandGroup."""
		return self._instance.ShowInDocumentType

	@show_in_document_type.setter
	def show_in_document_type(self, value):
		"""Gets or sets the types of documents to show this CommandGroup."""
		self._instance.ShowInDocumentType = value

	@property
	def toolbar_id(self):
		"""Gets the toolbar ID of this CommandGroup."""
		return self._instance.ToolbarId

	@toolbar_id.setter
	def toolbar_id(self, value):
		"""Gets the toolbar ID of this CommandGroup."""
		self._instance.ToolbarId = value

	@property
	def activate(self):
		"""Activates the CommandGroup."""
		return self._instance.Activate

	@activate.setter
	def activate(self, value):
		"""Activates the CommandGroup."""
		self._instance.Activate = value

	@property
	def add_command_item(self):
		"""Adds a combination menu item and toolbar item to a CommandGroup."""
		return self._instance.AddCommandItem2

	@add_command_item.setter
	def add_command_item(self, value):
		"""Adds a combination menu item and toolbar item to a CommandGroup."""
		self._instance.AddCommandItem2 = value

	@property
	def add_spacer(self):
		"""Adds a spacer between items in a CommandGroup."""
		return self._instance.AddSpacer2

	@add_spacer.setter
	def add_spacer(self, value):
		"""Adds a spacer between items in a CommandGroup."""
		self._instance.AddSpacer2 = value

	@property
	def get_toolbar_visibility(self):
		"""Gets whether this toolbar is visible."""
		return self._instance.GetToolbarVisibility

	@get_toolbar_visibility.setter
	def get_toolbar_visibility(self, value):
		"""Gets whether this toolbar is visible."""
		self._instance.GetToolbarVisibility = value

	@property
	def set_toolbar_visibility(self):
		"""Sets the visibility of the toolbar in the CommandGroup."""
		return self._instance.SetToolbarVisibility

	@set_toolbar_visibility.setter
	def set_toolbar_visibility(self, value):
		"""Sets the visibility of the toolbar in the CommandGroup."""
		self._instance.SetToolbarVisibility = value

