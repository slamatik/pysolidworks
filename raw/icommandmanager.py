# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager_members.html
class ICommandManager:
	def __init__(self, parent=None):
		self._instance = parent

	def number_of_flyout_groups(self):
		"""Gets the number of flyouts in the CommandManager."""
		# return self._instance.NumberOfFlyoutGroups
		raise NotImplemented

	def number_of_groups(self):
		"""Gets the number of CommandGroups."""
		# return self._instance.NumberOfGroups
		raise NotImplemented

	def add_command_tab(self, document_type, tab_name):
		"""
		Adds a tab to the CommandManager for the specified document type.
		:param document_type: Document type as defined in swDocumentTypes_e
		:param tab_name: Name of CommandManager tab (see Remarks)
		"""
		# return self._instance.AddCommandTab(document_type, tab_name)
		raise NotImplemented

	def add_context_menu(self, user_i_d, title):
		"""
		Adds a new context-sensitive menu to the CommandManager.
		:param user_i_d: User-defined ID for this context-sensitive menu
		:param title: Name of the context-sensitive menu to add to the CommandManager
		"""
		# return self._instance.AddContextMenu(user_i_d, title)
		raise NotImplemented

	def command_tabs(self, document_type):
		"""
		Gets all of the add-in CommandManager tabs for the specified document type.
		:param document_type: Document type as defined in swDocumentTypes_e
		"""
		# return self._instance.CommandTabs(document_type)
		raise NotImplemented

	def create_command_group(self, user_i_d, title, tool_tip, hint, position, ignore_previous_version, errors):
		"""
		Creates a new CommandGroup in the CommandManager.
		:param user_i_d: Unique user-defined ID for the new CommandGroup 
		:param title: Name of the CommandGroup to create (see Remarks)
		:param tool_tip: Tool tip for the CommandGroup 
		:param hint: Text displayed in SOLIDWORKS status bar when a user's mouse pointer is over the CommandGroup 
		:param position: Position of the CommandGroup in the CommandManager for all document templates (see Remarks)
NOTE: Specify 0 to add the CommandGroup to the beginning of the CommandMananger, or specify -1 to add it to the end of the CommandManager.
		:param ignore_previous_version: True to remove all previously saved customization and toolbar information before creating a new CommandGroup, false to not (see Remarks)
		:param errors: Error code as defined in swCreateCommandGroupErrors
		"""
		# return self._instance.CreateCommandGroup2(user_i_d, title, tool_tip, hint, position, ignore_previous_version, errors)
		raise NotImplemented

	def create_flyout_group(self, user_i_d, title, tool_tip, hint, main_icon_list, icon_list, callback_function, update_callback_function):
		"""
		Creates a new flyout in the CommandManager and context-sensitive menus.
		:param user_i_d: Unique user-defined ID for the new flyout
		:param title: Name of the flyout to create
		:param tool_tip: ToolTip for the new flyout
		:param hint: Text displayed in SOLIDWORKS status bar when a user's mouse pointer is over the flyout
		:param main_icon_list: Array of strings for the paths to the image files for this flyout button (see Remarks)
		:param icon_list: Array of strings for the paths to the image files containing all of the flyout toolbar buttons and separators (see Remarks)
		:param callback_function: Function to call when the flyout is selected
		:param update_callback_function: Optional update function that controls the state of the item; if specified, then SOLIDWORKS calls this function before displaying the item (see Remarks)



If the updatefunction returns...
Then SOLIDWORKS...


0
Disables the item

1
Enables the item; this is the default state if no update function is specified
		"""
		# return self._instance.CreateFlyoutGroup2(user_i_d, title, tool_tip, hint, main_icon_list, icon_list, callback_function, update_callback_function)
		raise NotImplemented

	def get_command_group(self, user_i_d):
		"""
		Gets the CommandGroup using the specified ID.
		:param user_i_d: User-defined ID for this CommandGroup
		"""
		# return self._instance.GetCommandGroup(user_i_d)
		raise NotImplemented

	def get_command_i_ds_count(self, user_group_id):
		"""
		Gets the number of command IDs for the given command group.
		:param user_group_id: User-defined ID of a command group
		"""
		# return self._instance.GetCommandIDsCount(user_group_id)
		raise NotImplemented

	def get_command_tab(self, document_type, tab_name):
		"""
		Gets the specified CommandManager tab for the specified document type.
		:param document_type: Document type as defined in swDocumentTypes_e
		:param tab_name: Name of CommandManager tab
		"""
		# return self._instance.GetCommandTab(document_type, tab_name)
		raise NotImplemented

	def get_command_tab_count(self, document_type):
		"""
		Gets the number of tabs on the CommandManager for the specified document type.
		:param document_type: Document type as defined in swDocumentTypes_e
		"""
		# return self._instance.GetCommandTabCount(document_type)
		raise NotImplemented

	def get_flyout_group(self, user_i_d):
		"""
		Gets the flyout with the specified ID.
		:param user_i_d: User-defined ID for the flyout
		"""
		# return self._instance.GetFlyoutGroup(user_i_d)
		raise NotImplemented

	def get_flyout_groups(self):
		"""Gets the flyouts in the CommandManager."""
		# return self._instance.GetFlyoutGroups
		raise NotImplemented

	def get_group_data_from_registry(self, user_group_id, user_i_ds):
		"""
		Gets the command IDs of the given command group from the registry.
		:param user_group_id: User-defined ID of a command group
		:param user_i_ds: Array of command IDs for the given command group
		"""
		# return self._instance.GetGroupDataFromRegistry(user_group_id, user_i_ds)
		raise NotImplemented

	def get_groups(self):
		"""Gets the CommandGroups in the CommandManager."""
		# return self._instance.GetGroups
		raise NotImplemented

	def i_get_command_tabs(self, document_type, command_tab_count):
		"""
		Gets the CommandManager tabs for the specified document type.
		:param document_type: Document type as defined in swDocumentTypes_e
		:param command_tab_count: Number of CommandManager tabs for DocumentType
		"""
		# return self._instance.IGetCommandTabs(document_type, command_tab_count)
		raise NotImplemented

	def i_get_group_data_from_registry(self, user_group_id, count, user_i_ds):
		"""
		Gets the command IDs of the given command group from the registry.
		:param user_group_id: User-defined ID of a command group
		:param count: Number of command IDs in the given command group
		:param user_i_ds: 
in-process, unmanaged C++: Pointer to an array of integer IDs
VBA, VB.NET, C#, and C++/CLI: Not supported 
 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IGetGroupDataFromRegistry(user_group_id, count, user_i_ds)
		raise NotImplemented

	def i_get_groups(self, count):
		"""
		Gets the CommandGroups in the CommandManager.
		:param count: Number of CommandGroups in this CommandManager
		"""
		# return self._instance.IGetGroups(count)
		raise NotImplemented

	def remove_command_group(self, user_i_d, runtime_only):
		"""
		Removes the specified CommandGroup from the CommandManager.
		:param user_i_d: User-defined ID of the CommandGroup to remove
		:param runtime_only: True to remove the CommandGroup , saving its toolbar information in the registry; false to remove both the CommandGroup and its toolbar information in the registry
		"""
		# return self._instance.RemoveCommandGroup2(user_i_d, runtime_only)
		raise NotImplemented

	def remove_command_tab(self, tab_to_remove):
		"""
		Removes the specified CommandManager tab, including its tab boxes and buttons, from the CommandManager.
		:param tab_to_remove: CommandManager tab, including its tab boxes and buttons, to remove
		"""
		# return self._instance.RemoveCommandTab(tab_to_remove)
		raise NotImplemented

	def remove_flyout_group(self, user_i_d):
		"""
		Removes the specified flyout from the CommandManager.
		:param user_i_d: User-defined ID of the flyout to remove
		"""
		# return self._instance.RemoveFlyoutGroup(user_i_d)
		raise NotImplemented

