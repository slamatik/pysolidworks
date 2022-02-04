# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html
class ISldWorks:
	def __init__(self, parent=None):
		self._instance = parent

	def active_doc(self):
		"""Gets the currently active document."""
		# return self._instance.ActiveDoc
		raise NotImplemented

	def application_type(self):
		"""Gets the type of this SOLIDWORKS application."""
		# return self._instance.ApplicationType
		raise NotImplemented

	def command_in_progress(self):
		"""Improves performance of out-of-process applications by informing SOLIDWORKS that a sequence of API calls will be made by the out-of-process application."""
		# return self._instance.CommandInProgress
		raise NotImplemented

	@property
	def enable_background_processing(self):
		"""Gets or sets whether to enable background processing."""
		return self._instance.EnableBackgroundProcessing

	@enable_background_processing.setter
	def enable_background_processing(self, value):
		"""Gets or sets whether to enable background processing."""
		self._instance.EnableBackgroundProcessing = value

	@property
	def enable_file_menu(self):
		"""Gets or sets whether to enable file-related menus and toolbars."""
		return self._instance.EnableFileMenu

	@enable_file_menu.setter
	def enable_file_menu(self, value):
		"""Gets or sets whether to enable file-related menus and toolbars."""
		self._instance.EnableFileMenu = value

	@property
	def frame_height(self):
		"""Get or sets the height of the SOLIDWORKS window."""
		return self._instance.FrameHeight

	@frame_height.setter
	def frame_height(self, value):
		"""Get or sets the height of the SOLIDWORKS window."""
		self._instance.FrameHeight = value

	@property
	def frame_left(self):
		"""Gets or sets the left position of the SOLIDWORKS window."""
		return self._instance.FrameLeft

	@frame_left.setter
	def frame_left(self, value):
		"""Gets or sets the left position of the SOLIDWORKS window."""
		self._instance.FrameLeft = value

	@property
	def frame_state(self):
		"""Gets or sets the window state (minimum, maximum, or normal) for the SOLIDWORKS window."""
		return self._instance.FrameState

	@frame_state.setter
	def frame_state(self, value):
		"""Gets or sets the window state (minimum, maximum, or normal) for the SOLIDWORKS window."""
		self._instance.FrameState = value

	@property
	def frame_top(self):
		"""Gets or sets the top position of the SOLIDWORKS window."""
		return self._instance.FrameTop

	@frame_top.setter
	def frame_top(self, value):
		"""Gets or sets the top position of the SOLIDWORKS window."""
		self._instance.FrameTop = value

	@property
	def frame_width(self):
		"""Gets or sets the width of the frame of the SOLIDWORKS window."""
		return self._instance.FrameWidth

	@frame_width.setter
	def frame_width(self, value):
		"""Gets or sets the width of the frame of the SOLIDWORKS window."""
		self._instance.FrameWidth = value

	@property
	def i_active_doc(self):
		"""Gets the currently active document."""
		return self._instance.IActiveDoc2

	@i_active_doc.setter
	def i_active_doc(self, value):
		"""Gets the currently active document."""
		self._instance.IActiveDoc2 = value

	@property
	def startup_process_completed(self):
		"""Gets whether the SOLIDWORKS startup process, including loading all startup add-ins, has completed."""
		return self._instance.StartupProcessCompleted

	@startup_process_completed.setter
	def startup_process_completed(self, value):
		"""Gets whether the SOLIDWORKS startup process, including loading all startup add-ins, has completed."""
		self._instance.StartupProcessCompleted = value

	@property
	def task_pane_is_pinned(self):
		"""Gets or sets whether the SOLIDWORKS Task Pane is pinned."""
		return self._instance.TaskPaneIsPinned

	@task_pane_is_pinned.setter
	def task_pane_is_pinned(self, value):
		"""Gets or sets whether the SOLIDWORKS Task Pane is pinned."""
		self._instance.TaskPaneIsPinned = value

	@property
	def user_control(self):
		"""Gets and sets whether the user has control over the application."""
		return self._instance.UserControl

	@user_control.setter
	def user_control(self, value):
		"""Gets and sets whether the user has control over the application."""
		self._instance.UserControl = value

	@property
	def user_control_background(self):
		"""Gets and sets whether the user has control over the application."""
		return self._instance.UserControlBackground

	@user_control_background.setter
	def user_control_background(self, value):
		"""Gets and sets whether the user has control over the application."""
		self._instance.UserControlBackground = value

	@property
	def user_type_lib_references(self):
		"""Gets and sets the user-specified type library references."""
		return self._instance.UserTypeLibReferences

	@user_type_lib_references.setter
	def user_type_lib_references(self, value):
		"""Gets and sets the user-specified type library references."""
		self._instance.UserTypeLibReferences = value

	@property
	def visible(self):
		"""Gets and sets the visibility property of the SOLIDWORKS application."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets and sets the visibility property of the SOLIDWORKS application."""
		self._instance.Visible = value

	@property
	def activate_doc(self):
		"""Activates a loaded document and rebuilds it as specified."""
		return self._instance.ActivateDoc3

	@activate_doc.setter
	def activate_doc(self, value):
		"""Activates a loaded document and rebuilds it as specified."""
		self._instance.ActivateDoc3 = value

	@property
	def activate_task_pane(self):
		"""Activates the specified task pane."""
		return self._instance.ActivateTaskPane

	@activate_task_pane.setter
	def activate_task_pane(self, value):
		"""Activates the specified task pane."""
		self._instance.ActivateTaskPane = value

	@property
	def add_callback(self):
		"""Registers a general purpose callback handler."""
		return self._instance.AddCallback

	@add_callback.setter
	def add_callback(self, value):
		"""Registers a general purpose callback handler."""
		self._instance.AddCallback = value

	@property
	def add_file_open_item(self):
		"""Adds file types to the File > Open dialog box."""
		return self._instance.AddFileOpenItem3

	@add_file_open_item.setter
	def add_file_open_item(self, value):
		"""Adds file types to the File > Open dialog box."""
		self._instance.AddFileOpenItem3 = value

	@property
	def add_file_save_as_item(self):
		"""Adds a file type to the SOLIDWORKS File > Save As dialog box."""
		return self._instance.AddFileSaveAsItem2

	@add_file_save_as_item.setter
	def add_file_save_as_item(self, value):
		"""Adds a file type to the SOLIDWORKS File > Save As dialog box."""
		self._instance.AddFileSaveAsItem2 = value

	@property
	def add_item_to_third_party_popup_menu(self):
		"""Adds menu items to a pop-up (shortcut) menu in a C++ SOLIDWORKS add-in."""
		return self._instance.AddItemToThirdPartyPopupMenu

	@add_item_to_third_party_popup_menu.setter
	def add_item_to_third_party_popup_menu(self, value):
		"""Adds menu items to a pop-up (shortcut) menu in a C++ SOLIDWORKS add-in."""
		self._instance.AddItemToThirdPartyPopupMenu = value

	@property
	def add_item_to_third_party_popup_menu(self):
		"""Adds menu items to a pop-up (shortcut) menu in a SOLIDWORKS add-in."""
		return self._instance.AddItemToThirdPartyPopupMenu2

	@add_item_to_third_party_popup_menu.setter
	def add_item_to_third_party_popup_menu(self, value):
		"""Adds menu items to a pop-up (shortcut) menu in a SOLIDWORKS add-in."""
		self._instance.AddItemToThirdPartyPopupMenu2 = value

	@property
	def add_menu(self):
		"""Adds a menu item to a SOLIDWORKS menu for DLL applications."""
		return self._instance.AddMenu

	@add_menu.setter
	def add_menu(self, value):
		"""Adds a menu item to a SOLIDWORKS menu for DLL applications."""
		self._instance.AddMenu = value

	@property
	def add_menu_item(self):
		"""Adds a menu item and image to the SOLIDWORKS user interface."""
		return self._instance.AddMenuItem5

	@add_menu_item.setter
	def add_menu_item(self, value):
		"""Adds a menu item and image to the SOLIDWORKS user interface."""
		self._instance.AddMenuItem5 = value

	@property
	def add_menu_popup_item(self):
		"""Adds a menu item and zero or more submenus to shortcut menus of entities of the specified type in documents of the specified type."""
		return self._instance.AddMenuPopupItem3

	@add_menu_popup_item.setter
	def add_menu_popup_item(self, value):
		"""Adds a menu item and zero or more submenus to shortcut menus of entities of the specified type in documents of the specified type."""
		self._instance.AddMenuPopupItem3 = value

	@property
	def add_menu_popup_item(self):
		"""Adds a menu item and zero or more submenus to shortcut menus of features of the specified type in documents of the specified type."""
		return self._instance.AddMenuPopupItem4

	@add_menu_popup_item.setter
	def add_menu_popup_item(self, value):
		"""Adds a menu item and zero or more submenus to shortcut menus of features of the specified type in documents of the specified type."""
		self._instance.AddMenuPopupItem4 = value

	@property
	def add_toolbar(self):
		"""Creates a Windows-style dockable toolbar."""
		return self._instance.AddToolbar5

	@add_toolbar.setter
	def add_toolbar(self, value):
		"""Creates a Windows-style dockable toolbar."""
		self._instance.AddToolbar5 = value

	@property
	def add_toolbar_command(self):
		"""Specifies the application functions to call when a toolbar button is clicked or sets a separator."""
		return self._instance.AddToolbarCommand2

	@add_toolbar_command.setter
	def add_toolbar_command(self, value):
		"""Specifies the application functions to call when a toolbar button is clicked or sets a separator."""
		self._instance.AddToolbarCommand2 = value

	@property
	def allow_failed_feature_creation(self):
		"""Sets whether to allow the creation of a feature that has rebuild errors."""
		return self._instance.AllowFailedFeatureCreation

	@allow_failed_feature_creation.setter
	def allow_failed_feature_creation(self, value):
		"""Sets whether to allow the creation of a feature that has rebuild errors."""
		self._instance.AllowFailedFeatureCreation = value

	@property
	def arrange_icons(self):
		"""Arranges the icons in SOLIDWORKS."""
		return self._instance.ArrangeIcons

	@arrange_icons.setter
	def arrange_icons(self, value):
		"""Arranges the icons in SOLIDWORKS."""
		self._instance.ArrangeIcons = value

	@property
	def arrange_windows(self):
		"""Arranges the open windows in SOLIDWORKS."""
		return self._instance.ArrangeWindows

	@arrange_windows.setter
	def arrange_windows(self, value):
		"""Arranges the open windows in SOLIDWORKS."""
		self._instance.ArrangeWindows = value

	@property
	def block_skinning(self):
		"""Blocks skinning a window, which prevents a window from looking like a SOLIDWORKS window."""
		return self._instance.BlockSkinning

	@block_skinning.setter
	def block_skinning(self, value):
		"""Blocks skinning a window, which prevents a window from looking like a SOLIDWORKS window."""
		self._instance.BlockSkinning = value

	@property
	def call_back(self):
		"""Allows an out-of-process executable or a SOLIDWORKS macro to call back a function in a SOLIDWORKS add-in DLL."""
		return self._instance.CallBack

	@call_back.setter
	def call_back(self, value):
		"""Allows an out-of-process executable or a SOLIDWORKS macro to call back a function in a SOLIDWORKS add-in DLL."""
		self._instance.CallBack = value

	@property
	def checkpoint_converted_document(self):
		"""Saves the specified open document if its version is older than the version of the SOLIDWORKS product being used."""
		return self._instance.CheckpointConvertedDocument

	@checkpoint_converted_document.setter
	def checkpoint_converted_document(self, value):
		"""Saves the specified open document if its version is older than the version of the SOLIDWORKS product being used."""
		self._instance.CheckpointConvertedDocument = value

	@property
	def close_all_documents(self):
		"""Closes all open documents in the SOLIDWORKS session."""
		return self._instance.CloseAllDocuments

	@close_all_documents.setter
	def close_all_documents(self, value):
		"""Closes all open documents in the SOLIDWORKS session."""
		self._instance.CloseAllDocuments = value

	@property
	def close_and_reopen(self):
		"""Closes and reopens the specified drawing document without unloading its references from memory."""
		return self._instance.CloseAndReopen

	@close_and_reopen.setter
	def close_and_reopen(self, value):
		"""Closes and reopens the specified drawing document without unloading its references from memory."""
		self._instance.CloseAndReopen = value

	@property
	def close_doc(self):
		"""Closes the specified document."""
		return self._instance.CloseDoc

	@close_doc.setter
	def close_doc(self, value):
		"""Closes the specified document."""
		self._instance.CloseDoc = value

	@property
	def command(self):
		"""Opens the specified dialog or file."""
		return self._instance.Command

	@command.setter
	def command(self, value):
		"""Opens the specified dialog or file."""
		self._instance.Command = value

	@property
	def copy_appearance(self):
		"""Copies the appearance of the specified entity to the clipboard."""
		return self._instance.CopyAppearance

	@copy_appearance.setter
	def copy_appearance(self, value):
		"""Copies the appearance of the specified entity to the clipboard."""
		self._instance.CopyAppearance = value

	@property
	def copy_document(self):
		"""Copies a document and optionally updates references to it."""
		return self._instance.CopyDocument

	@copy_document.setter
	def copy_document(self, value):
		"""Copies a document and optionally updates references to it."""
		self._instance.CopyDocument = value

	@property
	def create_new_window(self):
		"""Creates a client window containing the active document."""
		return self._instance.CreateNewWindow

	@create_new_window.setter
	def create_new_window(self, value):
		"""Creates a client window containing the active document."""
		self._instance.CreateNewWindow = value

	@property
	def create_property_manager_page(self):
		"""Creates a PropertyManager page."""
		return self._instance.CreatePropertyManagerPage

	@create_property_manager_page.setter
	def create_property_manager_page(self, value):
		"""Creates a PropertyManager page."""
		self._instance.CreatePropertyManagerPage = value

	@property
	def create_taskpane_view(self):
		"""Creates an application-level Task Pane view."""
		return self._instance.CreateTaskpaneView3

	@create_taskpane_view.setter
	def create_taskpane_view(self, value):
		"""Creates an application-level Task Pane view."""
		self._instance.CreateTaskpaneView3 = value

	@property
	def define_attribute(self):
		"""Creates an attribute definition, which is the first step in generating attributes."""
		return self._instance.DefineAttribute

	@define_attribute.setter
	def define_attribute(self, value):
		"""Creates an attribute definition, which is the first step in generating attributes."""
		self._instance.DefineAttribute = value

	@property
	def display_status_bar(self):
		"""Sets whether to display the status bar."""
		return self._instance.DisplayStatusBar

	@display_status_bar.setter
	def display_status_bar(self, value):
		"""Sets whether to display the status bar."""
		self._instance.DisplayStatusBar = value

	@property
	def document_visible(self):
		"""Allows the application to control the display of a document in a window upon creation or retrieval."""
		return self._instance.DocumentVisible

	@document_visible.setter
	def document_visible(self, value):
		"""Allows the application to control the display of a document in a window upon creation or retrieval."""
		self._instance.DocumentVisible = value

	@property
	def download_from_my_solid_works_settings(self):
		"""Downloads the specified SOLIDWORKS Connected settings to SOLIDWORKS Desktop."""
		return self._instance.DownloadFromMySolidWorksSettings

	@download_from_my_solid_works_settings.setter
	def download_from_my_solid_works_settings(self, value):
		"""Downloads the specified SOLIDWORKS Connected settings to SOLIDWORKS Desktop."""
		self._instance.DownloadFromMySolidWorksSettings = value

	@property
	def drag_toolbar_button(self):
		"""Copies the specified toolbar button from the specified native SOLIDWORKS toolbar or ICommandGroup toolbar to the specified native SOLIDWORKS toolbar or ICommandGroup toolbar."""
		return self._instance.DragToolbarButton

	@drag_toolbar_button.setter
	def drag_toolbar_button(self, value):
		"""Copies the specified toolbar button from the specified native SOLIDWORKS toolbar or ICommandGroup toolbar to the specified native SOLIDWORKS toolbar or ICommandGroup toolbar."""
		self._instance.DragToolbarButton = value

	@property
	def drag_toolbar_button_from_command_i_d(self):
		"""Copies a button to a toolbar using a command ID."""
		return self._instance.DragToolbarButtonFromCommandID

	@drag_toolbar_button_from_command_i_d.setter
	def drag_toolbar_button_from_command_i_d(self, value):
		"""Copies a button to a toolbar using a command ID."""
		self._instance.DragToolbarButtonFromCommandID = value

	@property
	def enum_documents(self):
		"""Gets a list of documents currently open in the application."""
		return self._instance.EnumDocuments2

	@enum_documents.setter
	def enum_documents(self, value):
		"""Gets a list of documents currently open in the application."""
		self._instance.EnumDocuments2 = value

	@property
	def exit_app(self):
		"""Shuts down SOLIDWORKS."""
		return self._instance.ExitApp

	@exit_app.setter
	def exit_app(self, value):
		"""Shuts down SOLIDWORKS."""
		self._instance.ExitApp = value

	@property
	def export_hole_wizard_item(self):
		"""Exports data for the specified Hole Wizard standard."""
		return self._instance.ExportHoleWizardItem

	@export_hole_wizard_item.setter
	def export_hole_wizard_item(self, value):
		"""Exports data for the specified Hole Wizard standard."""
		self._instance.ExportHoleWizardItem = value

	@property
	def export_toolbox_item(self):
		"""Exports data for the specified Toolbox standard."""
		return self._instance.ExportToolboxItem

	@export_toolbox_item.setter
	def export_toolbox_item(self, value):
		"""Exports data for the specified Toolbox standard."""
		self._instance.ExportToolboxItem = value

	@property
	def frame(self):
		"""Gets the SOLIDWORKS main frame."""
		return self._instance.Frame

	@frame.setter
	def frame(self, value):
		"""Gets the SOLIDWORKS main frame."""
		self._instance.Frame = value

	@property
	def get_active_configuration_name(self):
		"""Gets the name of the active configuration in the specified SOLIDWORKS document."""
		return self._instance.GetActiveConfigurationName

	@get_active_configuration_name.setter
	def get_active_configuration_name(self, value):
		"""Gets the name of the active configuration in the specified SOLIDWORKS document."""
		self._instance.GetActiveConfigurationName = value

	@property
	def get_add_in_object(self):
		"""Gets an add-in object for the specified SOLIDWORKS add-in."""
		return self._instance.GetAddInObject

	@get_add_in_object.setter
	def get_add_in_object(self, value):
		"""Gets an add-in object for the specified SOLIDWORKS add-in."""
		self._instance.GetAddInObject = value

	@property
	def get_apply_selection_filter(self):
		"""Gets the current state of the selection filter."""
		return self._instance.GetApplySelectionFilter

	@get_apply_selection_filter.setter
	def get_apply_selection_filter(self, value):
		"""Gets the current state of the selection filter."""
		self._instance.GetApplySelectionFilter = value

	@property
	def get_build_numbers(self):
		"""Gets the build, major revision, and hot fix numbers of the SOLIDWORKS application."""
		return self._instance.GetBuildNumbers2

	@get_build_numbers.setter
	def get_build_numbers(self, value):
		"""Gets the build, major revision, and hot fix numbers of the SOLIDWORKS application."""
		self._instance.GetBuildNumbers2 = value

	@property
	def get_button_position(self):
		"""Gets the center coordinates of the specified SOLIDWORKS toolbar button."""
		return self._instance.GetButtonPosition

	@get_button_position.setter
	def get_button_position(self, value):
		"""Gets the center coordinates of the specified SOLIDWORKS toolbar button."""
		self._instance.GetButtonPosition = value

	@property
	def get_collision_detection_manager(self):
		"""Gets the collision detection manager."""
		return self._instance.GetCollisionDetectionManager

	@get_collision_detection_manager.setter
	def get_collision_detection_manager(self, value):
		"""Gets the collision detection manager."""
		self._instance.GetCollisionDetectionManager = value

	@property
	def get_color_table(self):
		"""Gets a color table from the SOLIDWORKS application."""
		return self._instance.GetColorTable

	@get_color_table.setter
	def get_color_table(self, value):
		"""Gets a color table from the SOLIDWORKS application."""
		self._instance.GetColorTable = value

	@property
	def get_command_i_d(self):
		"""Gets the SOLIDWORKS command ID for an instance of an add-in's control (e.g., an add-in's toolbar button)."""
		return self._instance.GetCommandID

	@get_command_i_d.setter
	def get_command_i_d(self, value):
		"""Gets the SOLIDWORKS command ID for an instance of an add-in's control (e.g., an add-in's toolbar button)."""
		self._instance.GetCommandID = value

	@property
	def get_command_manager(self):
		"""Gets the CommandManager for the specified add-in."""
		return self._instance.GetCommandManager

	@get_command_manager.setter
	def get_command_manager(self, value):
		"""Gets the CommandManager for the specified add-in."""
		self._instance.GetCommandManager = value

	@property
	def get_configuration_count(self):
		"""Gets the number of configurations in the SOLIDWORKS document, whether the document is opened or closed."""
		return self._instance.GetConfigurationCount

	@get_configuration_count.setter
	def get_configuration_count(self, value):
		"""Gets the number of configurations in the SOLIDWORKS document, whether the document is opened or closed."""
		self._instance.GetConfigurationCount = value

	@property
	def get_configuration_names(self):
		"""Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed."""
		return self._instance.GetConfigurationNames

	@get_configuration_names.setter
	def get_configuration_names(self, value):
		"""Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed."""
		self._instance.GetConfigurationNames = value

	@property
	def get_current_file_user(self):
		"""Gets the name of the user who has the the specified document open."""
		return self._instance.GetCurrentFileUser

	@get_current_file_user.setter
	def get_current_file_user(self, value):
		"""Gets the name of the user who has the the specified document open."""
		self._instance.GetCurrentFileUser = value

	@property
	def get_current_language(self):
		"""Gets the current language used by SOLIDWORKS."""
		return self._instance.GetCurrentLanguage

	@get_current_language.setter
	def get_current_language(self, value):
		"""Gets the current language used by SOLIDWORKS."""
		self._instance.GetCurrentLanguage = value

	@property
	def get_current_license_type(self):
		"""Gets the type of license for the current SOLIDWORKS session."""
		return self._instance.GetCurrentLicenseType

	@get_current_license_type.setter
	def get_current_license_type(self, value):
		"""Gets the type of license for the current SOLIDWORKS session."""
		self._instance.GetCurrentLicenseType = value

	@property
	def get_current_macro_path_folder(self):
		"""Gets the name of the folder where the macro resides."""
		return self._instance.GetCurrentMacroPathFolder

	@get_current_macro_path_folder.setter
	def get_current_macro_path_folder(self, value):
		"""Gets the name of the folder where the macro resides."""
		self._instance.GetCurrentMacroPathFolder = value

	@property
	def get_current_macro_path_name(self):
		"""Gets the path name for the macro currently running."""
		return self._instance.GetCurrentMacroPathName

	@get_current_macro_path_name.setter
	def get_current_macro_path_name(self, value):
		"""Gets the path name for the macro currently running."""
		self._instance.GetCurrentMacroPathName = value

	@property
	def get_current_working_directory(self):
		"""Gets the current working directory being used by the SOLIDWORKS application."""
		return self._instance.GetCurrentWorkingDirectory

	@get_current_working_directory.setter
	def get_current_working_directory(self, value):
		"""Gets the current working directory being used by the SOLIDWORKS application."""
		self._instance.GetCurrentWorkingDirectory = value

	@property
	def get_data_folder(self):
		"""Gets the data directory name currently used by SOLIDWORKS."""
		return self._instance.GetDataFolder

	@get_data_folder.setter
	def get_data_folder(self, value):
		"""Gets the data directory name currently used by SOLIDWORKS."""
		self._instance.GetDataFolder = value

	@property
	def get_document_count(self):
		"""Gets the number of open documents in the current SOLIDWORKS session."""
		return self._instance.GetDocumentCount

	@get_document_count.setter
	def get_document_count(self, value):
		"""Gets the number of open documents in the current SOLIDWORKS session."""
		self._instance.GetDocumentCount = value

	@property
	def get_document_dependencies(self):
		"""Gets all of the model dependencies for a document."""
		return self._instance.GetDocumentDependencies2

	@get_document_dependencies.setter
	def get_document_dependencies(self, value):
		"""Gets all of the model dependencies for a document."""
		self._instance.GetDocumentDependencies2 = value

	@property
	def get_documents(self):
		"""Gets the open documents in this SOLIDWORKS session."""
		return self._instance.GetDocuments

	@get_documents.setter
	def get_documents(self, value):
		"""Gets the open documents in this SOLIDWORKS session."""
		self._instance.GetDocuments = value

	@property
	def get_document_template(self):
		"""Gets the name of document template that can be used in ISldWorks::NewDocument or ISldWorks::INewDocument2."""
		return self._instance.GetDocumentTemplate

	@get_document_template.setter
	def get_document_template(self, value):
		"""Gets the name of document template that can be used in ISldWorks::NewDocument or ISldWorks::INewDocument2."""
		self._instance.GetDocumentTemplate = value

	@property
	def get_document_visible(self):
		"""Gets the visibility of the document to open."""
		return self._instance.GetDocumentVisible

	@get_document_visible.setter
	def get_document_visible(self, value):
		"""Gets the visibility of the document to open."""
		self._instance.GetDocumentVisible = value

	@property
	def get_environment(self):
		"""Gets the IEnvironment object."""
		return self._instance.GetEnvironment

	@get_environment.setter
	def get_environment(self, value):
		"""Gets the IEnvironment object."""
		self._instance.GetEnvironment = value

	@property
	def get_error_messages(self):
		"""Gets the last 20 messages issued by SOLIDWORKS in the current SOLIDWORKS session."""
		return self._instance.GetErrorMessages

	@get_error_messages.setter
	def get_error_messages(self, value):
		"""Gets the last 20 messages issued by SOLIDWORKS in the current SOLIDWORKS session."""
		self._instance.GetErrorMessages = value

	@property
	def get_executable_path(self):
		"""Gets the path to the SOLIDWORKS executable, sldworks.exe."""
		return self._instance.GetExecutablePath

	@get_executable_path.setter
	def get_executable_path(self, value):
		"""Gets the path to the SOLIDWORKS executable, sldworks.exe."""
		self._instance.GetExecutablePath = value

	@property
	def get_export_file_data(self):
		"""Gets the data interface for the specified file type to which to export one or more drawing sheets."""
		return self._instance.GetExportFileData

	@get_export_file_data.setter
	def get_export_file_data(self, value):
		"""Gets the data interface for the specified file type to which to export one or more drawing sheets."""
		self._instance.GetExportFileData = value

	@property
	def get_first_document(self):
		"""Gets the document opened first in this SOLIDWORKS session."""
		return self._instance.GetFirstDocument

	@get_first_document.setter
	def get_first_document(self, value):
		"""Gets the document opened first in this SOLIDWORKS session."""
		self._instance.GetFirstDocument = value

	@property
	def get_hole_standards_data(self):
		"""Gets the hole standards for the specified hole type."""
		return self._instance.GetHoleStandardsData

	@get_hole_standards_data.setter
	def get_hole_standards_data(self, value):
		"""Gets the hole standards for the specified hole type."""
		self._instance.GetHoleStandardsData = value

	@property
	def get_image_size(self):
		"""Gets:

small, medium, and large image sizes suitable for the current DPI setting of the display device. 
default image size for the current DPI setting of the display device for images that are not based on the SOLIDWORKS icon size setting."""
		return self._instance.GetImageSize

	@get_image_size.setter
	def get_image_size(self, value):
		"""Gets:

small, medium, and large image sizes suitable for the current DPI setting of the display device. 
default image size for the current DPI setting of the display device for images that are not based on the SOLIDWORKS icon size setting."""
		self._instance.GetImageSize = value

	@property
	def get_import_file_data(self):
		"""Gets the IGES or DXF/DWG import data for the specified file."""
		return self._instance.GetImportFileData

	@get_import_file_data.setter
	def get_import_file_data(self, value):
		"""Gets the IGES or DXF/DWG import data for the specified file."""
		self._instance.GetImportFileData = value

	@property
	def get_interface_brightness_theme_colors(self):
		"""Gets the theme and colors of the SOLIDWORKS background."""
		return self._instance.GetInterfaceBrightnessThemeColors

	@get_interface_brightness_theme_colors.setter
	def get_interface_brightness_theme_colors(self, value):
		"""Gets the theme and colors of the SOLIDWORKS background."""
		self._instance.GetInterfaceBrightnessThemeColors = value

	@property
	def get_last_save_error(self):
		"""Gets the last save error issued by Microsoft in the current session."""
		return self._instance.GetLastSaveError

	@get_last_save_error.setter
	def get_last_save_error(self, value):
		"""Gets the last save error issued by Microsoft in the current session."""
		self._instance.GetLastSaveError = value

	@property
	def get_last_toolbar_i_d(self):
		"""Gets the ID of the last toolbar added to the CommandManager."""
		return self._instance.GetLastToolbarID

	@get_last_toolbar_i_d.setter
	def get_last_toolbar_i_d(self, value):
		"""Gets the ID of the last toolbar added to the CommandManager."""
		self._instance.GetLastToolbarID = value

	@property
	def get_latest_supported_file_version(self):
		"""Gets the version number that this instance of SOLIDWORKS reads and writes."""
		return self._instance.GetLatestSupportedFileVersion

	@get_latest_supported_file_version.setter
	def get_latest_supported_file_version(self, value):
		"""Gets the version number that this instance of SOLIDWORKS reads and writes."""
		self._instance.GetLatestSupportedFileVersion = value

	@property
	def get_line_styles(self):
		"""Gets all of the line styles in the specified file."""
		return self._instance.GetLineStyles

	@get_line_styles.setter
	def get_line_styles(self, value):
		"""Gets all of the line styles in the specified file."""
		self._instance.GetLineStyles = value

	@property
	def get_localized_menu_name(self):
		"""Gets a localized menu name for the specified menu ID."""
		return self._instance.GetLocalizedMenuName

	@get_localized_menu_name.setter
	def get_localized_menu_name(self, value):
		"""Gets a localized menu name for the specified menu ID."""
		self._instance.GetLocalizedMenuName = value

	@property
	def get_macro_methods(self):
		"""Gets the names of the modules in the specified macro."""
		return self._instance.GetMacroMethods

	@get_macro_methods.setter
	def get_macro_methods(self, value):
		"""Gets the names of the modules in the specified macro."""
		self._instance.GetMacroMethods = value

	@property
	def get_mass_properties(self):
		"""Gets the mass properties from the specified document for the specified configuration."""
		return self._instance.GetMassProperties2

	@get_mass_properties.setter
	def get_mass_properties(self, value):
		"""Gets the mass properties from the specified document for the specified configuration."""
		self._instance.GetMassProperties2 = value

	@property
	def get_material_database_count(self):
		"""Gets the number of material databases."""
		return self._instance.GetMaterialDatabaseCount

	@get_material_database_count.setter
	def get_material_database_count(self, value):
		"""Gets the number of material databases."""
		self._instance.GetMaterialDatabaseCount = value

	@property
	def get_material_databases(self):
		"""Gets the names of the material databases."""
		return self._instance.GetMaterialDatabases

	@get_material_databases.setter
	def get_material_databases(self, value):
		"""Gets the names of the material databases."""
		self._instance.GetMaterialDatabases = value

	@property
	def get_material_schema_path_name(self):
		"""Gets the path for the XML material schema file."""
		return self._instance.GetMaterialSchemaPathName

	@get_material_schema_path_name.setter
	def get_material_schema_path_name(self, value):
		"""Gets the path for the XML material schema file."""
		self._instance.GetMaterialSchemaPathName = value

	@property
	def get_math_utility(self):
		"""Gets IMathUtility."""
		return self._instance.GetMathUtility

	@get_math_utility.setter
	def get_math_utility(self, value):
		"""Gets IMathUtility."""
		self._instance.GetMathUtility = value

	@property
	def get_menu_strings(self):
		"""Gets the name of the parent menu of the specified menu command."""
		return self._instance.GetMenuStrings

	@get_menu_strings.setter
	def get_menu_strings(self, value):
		"""Gets the name of the parent menu of the specified menu command."""
		self._instance.GetMenuStrings = value

	@property
	def get_modeler(self):
		"""Gets the IModeler interface."""
		return self._instance.GetModeler

	@get_modeler.setter
	def get_modeler(self, value):
		"""Gets the IModeler interface."""
		self._instance.GetModeler = value

	@property
	def get_mouse_drag_mode(self):
		"""Gets whether the specified command-mouse mode is in effect."""
		return self._instance.GetMouseDragMode

	@get_mouse_drag_mode.setter
	def get_mouse_drag_mode(self, value):
		"""Gets whether the specified command-mouse mode is in effect."""
		self._instance.GetMouseDragMode = value

	@property
	def get_open_doc_spec(self):
		"""Gets the specifications to use when opening a model document."""
		return self._instance.GetOpenDocSpec

	@get_open_doc_spec.setter
	def get_open_doc_spec(self, value):
		"""Gets the specifications to use when opening a model document."""
		self._instance.GetOpenDocSpec = value

	@property
	def get_open_document(self):
		"""Gets the open document with the specified name."""
		return self._instance.GetOpenDocument

	@get_open_document.setter
	def get_open_document(self, value):
		"""Gets the open document with the specified name."""
		self._instance.GetOpenDocument = value

	@property
	def get_open_document_by_name(self):
		"""Gets the open document with the specified name."""
		return self._instance.GetOpenDocumentByName

	@get_open_document_by_name.setter
	def get_open_document_by_name(self, value):
		"""Gets the open document with the specified name."""
		self._instance.GetOpenDocumentByName = value

	@property
	def get_opened_file_info(self):
		"""Gets the name of the last model successfully opened by SOLIDWORKS and the options that were in effect when it opened."""
		return self._instance.GetOpenedFileInfo

	@get_opened_file_info.setter
	def get_opened_file_info(self, value):
		"""Gets the name of the last model successfully opened by SOLIDWORKS and the options that were in effect when it opened."""
		self._instance.GetOpenedFileInfo = value

	@property
	def get_open_file_name(self):
		"""Prompts the user for the name of the file to open."""
		return self._instance.GetOpenFileName

	@get_open_file_name.setter
	def get_open_file_name(self, value):
		"""Prompts the user for the name of the file to open."""
		self._instance.GetOpenFileName = value

	@property
	def get_preview_bitmap(self):
		"""Gets the preview bitmap (.bmp) for the specified configuration, regardless if the SOLIDWORKS document is open or closed."""
		return self._instance.GetPreviewBitmap

	@get_preview_bitmap.setter
	def get_preview_bitmap(self, value):
		"""Gets the preview bitmap (.bmp) for the specified configuration, regardless if the SOLIDWORKS document is open or closed."""
		self._instance.GetPreviewBitmap = value

	@property
	def get_preview_bitmap_file(self):
		"""Gets the specified preview bitmap of a document and saves it as a Windows bitmap file (.bmp) using the specified filename."""
		return self._instance.GetPreviewBitmapFile

	@get_preview_bitmap_file.setter
	def get_preview_bitmap_file(self, value):
		"""Gets the specified preview bitmap of a document and saves it as a Windows bitmap file (.bmp) using the specified filename."""
		self._instance.GetPreviewBitmapFile = value

	@property
	def get_process_i_d(self):
		"""Gets the process ID for the current SOLIDWORKS session."""
		return self._instance.GetProcessID

	@get_process_i_d.setter
	def get_process_i_d(self, value):
		"""Gets the process ID for the current SOLIDWORKS session."""
		self._instance.GetProcessID = value

	@property
	def get_ray_trace_renderer(self):
		"""Get a ray-trace rendering engine, such as PhotoView 360."""
		return self._instance.GetRayTraceRenderer

	@get_ray_trace_renderer.setter
	def get_ray_trace_renderer(self, value):
		"""Get a ray-trace rendering engine, such as PhotoView 360."""
		self._instance.GetRayTraceRenderer = value

	@property
	def get_recent_files(self):
		"""Gets a list of the most recently used files."""
		return self._instance.GetRecentFiles

	@get_recent_files.setter
	def get_recent_files(self, value):
		"""Gets a list of the most recently used files."""
		self._instance.GetRecentFiles = value

	@property
	def get_routing_settings(self):
		"""Gets routing settings."""
		return self._instance.GetRoutingSettings

	@get_routing_settings.setter
	def get_routing_settings(self, value):
		"""Gets routing settings."""
		self._instance.GetRoutingSettings = value

	@property
	def get_running_command_info(self):
		"""Get a command's ID or PropertyManager page's command ID, title, and whether it is active in the user-interface."""
		return self._instance.GetRunningCommandInfo

	@get_running_command_info.setter
	def get_running_command_info(self, value):
		"""Get a command's ID or PropertyManager page's command ID, title, and whether it is active in the user-interface."""
		self._instance.GetRunningCommandInfo = value

	@property
	def get_safe_array_utility(self):
		"""Gets the ISafeArrayUtility object."""
		return self._instance.GetSafeArrayUtility

	@get_safe_array_utility.setter
	def get_safe_array_utility(self, value):
		"""Gets the ISafeArrayUtility object."""
		self._instance.GetSafeArrayUtility = value

	@property
	def get_save_to_d_experience_options(self):
		"""Initializes save options for a SOLIDWORKS Connected document."""
		return self._instance.GetSaveTo3DExperienceOptions

	@get_save_to_d_experience_options.setter
	def get_save_to_d_experience_options(self, value):
		"""Initializes save options for a SOLIDWORKS Connected document."""
		self._instance.GetSaveTo3DExperienceOptions = value

	@property
	def get_search_folders(self):
		"""Gets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for > Referenced Documents."""
		return self._instance.GetSearchFolders

	@get_search_folders.setter
	def get_search_folders(self, value):
		"""Gets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for > Referenced Documents."""
		self._instance.GetSearchFolders = value

	@property
	def get_selection_filter(self):
		"""Gets the current selection filter settings for the specified item type."""
		return self._instance.GetSelectionFilter

	@get_selection_filter.setter
	def get_selection_filter(self, value):
		"""Gets the current selection filter settings for the specified item type."""
		self._instance.GetSelectionFilter = value

	@property
	def get_selection_filters(self):
		"""Gets all active selection filters."""
		return self._instance.GetSelectionFilters

	@get_selection_filters.setter
	def get_selection_filters(self, value):
		"""Gets all active selection filters."""
		self._instance.GetSelectionFilters = value

	@property
	def get_s_s_o_formatted_u_r_l(self):
		"""Formats the specified URL for single sign-on."""
		return self._instance.GetSSOFormattedURL

	@get_s_s_o_formatted_u_r_l.setter
	def get_s_s_o_formatted_u_r_l(self, value):
		"""Formats the specified URL for single sign-on."""
		self._instance.GetSSOFormattedURL = value

	@property
	def get_template_sizes(self):
		"""Gets the sheet properties from a template document."""
		return self._instance.GetTemplateSizes

	@get_template_sizes.setter
	def get_template_sizes(self, value):
		"""Gets the sheet properties from a template document."""
		self._instance.GetTemplateSizes = value

	@property
	def get_toolbar_dock(self):
		"""Gets the docking state of the toolbar."""
		return self._instance.GetToolbarDock2

	@get_toolbar_dock.setter
	def get_toolbar_dock(self, value):
		"""Gets the docking state of the toolbar."""
		self._instance.GetToolbarDock2 = value

	@property
	def get_toolbar_state(self):
		"""Gets the state of the toolbar."""
		return self._instance.GetToolbarState2

	@get_toolbar_state.setter
	def get_toolbar_state(self, value):
		"""Gets the state of the toolbar."""
		self._instance.GetToolbarState2 = value

	@property
	def get_toolbar_visibility(self):
		"""Gets whether this toolbar is visible."""
		return self._instance.GetToolbarVisibility

	@get_toolbar_visibility.setter
	def get_toolbar_visibility(self, value):
		"""Gets whether this toolbar is visible."""
		self._instance.GetToolbarVisibility = value

	@property
	def get_user_preference_double_value(self):
		"""Gets system default user preference values."""
		return self._instance.GetUserPreferenceDoubleValue

	@get_user_preference_double_value.setter
	def get_user_preference_double_value(self, value):
		"""Gets system default user preference values."""
		self._instance.GetUserPreferenceDoubleValue = value

	@property
	def get_user_preference_integer_value(self):
		"""Gets system default user preference values."""
		return self._instance.GetUserPreferenceIntegerValue

	@get_user_preference_integer_value.setter
	def get_user_preference_integer_value(self, value):
		"""Gets system default user preference values."""
		self._instance.GetUserPreferenceIntegerValue = value

	@property
	def get_user_preference_string_list_value(self):
		"""Gets the name of the DXF mapping file."""
		return self._instance.GetUserPreferenceStringListValue

	@get_user_preference_string_list_value.setter
	def get_user_preference_string_list_value(self, value):
		"""Gets the name of the DXF mapping file."""
		self._instance.GetUserPreferenceStringListValue = value

	@property
	def get_user_preference_string_value(self):
		"""Gets system default user preference values."""
		return self._instance.GetUserPreferenceStringValue

	@get_user_preference_string_value.setter
	def get_user_preference_string_value(self, value):
		"""Gets system default user preference values."""
		self._instance.GetUserPreferenceStringValue = value

	@property
	def get_user_preference_toggle(self):
		"""Gets document default user preference values."""
		return self._instance.GetUserPreferenceToggle

	@get_user_preference_toggle.setter
	def get_user_preference_toggle(self, value):
		"""Gets document default user preference values."""
		self._instance.GetUserPreferenceToggle = value

	@property
	def get_user_progress_bar(self):
		"""Gets a progress indicator."""
		return self._instance.GetUserProgressBar

	@get_user_progress_bar.setter
	def get_user_progress_bar(self, value):
		"""Gets a progress indicator."""
		self._instance.GetUserProgressBar = value

	@property
	def get_user_type_lib_reference_count(self):
		"""Gets the number of user-specified type library references."""
		return self._instance.GetUserTypeLibReferenceCount

	@get_user_type_lib_reference_count.setter
	def get_user_type_lib_reference_count(self, value):
		"""Gets the number of user-specified type library references."""
		self._instance.GetUserTypeLibReferenceCount = value

	@property
	def get_user_unit(self):
		"""Gets an empty IUserUnit object of the specified type."""
		return self._instance.GetUserUnit

	@get_user_unit.setter
	def get_user_unit(self, value):
		"""Gets an empty IUserUnit object of the specified type."""
		self._instance.GetUserUnit = value

	@property
	def hide_bubble_tooltip(self):
		"""Hides the bubble ToolTip displayed by ISldWorks::ShowBubbleTooltipAt2."""
		return self._instance.HideBubbleTooltip

	@hide_bubble_tooltip.setter
	def hide_bubble_tooltip(self, value):
		"""Hides the bubble ToolTip displayed by ISldWorks::ShowBubbleTooltipAt2."""
		self._instance.HideBubbleTooltip = value

	@property
	def hide_toolbar(self):
		"""Hides a toolbar created with ISldWorks::AddToolbar5."""
		return self._instance.HideToolbar2

	@hide_toolbar.setter
	def hide_toolbar(self, value):
		"""Hides a toolbar created with ISldWorks::AddToolbar5."""
		self._instance.HideToolbar2 = value

	@property
	def i_activate_doc(self):
		"""Activates a document that has already been loaded. This file becomes the active document, and this method returns a pointer to that document object."""
		return self._instance.IActivateDoc3

	@i_activate_doc.setter
	def i_activate_doc(self, value):
		"""Activates a document that has already been loaded. This file becomes the active document, and this method returns a pointer to that document object."""
		self._instance.IActivateDoc3 = value

	@property
	def i_copy_document(self):
		"""Copies a document and optionally updates references to it."""
		return self._instance.ICopyDocument

	@i_copy_document.setter
	def i_copy_document(self, value):
		"""Copies a document and optionally updates references to it."""
		self._instance.ICopyDocument = value

	@property
	def i_create_property_manager_page(self):
		"""Creates a PropertyManager page."""
		return self._instance.ICreatePropertyManagerPage

	@i_create_property_manager_page.setter
	def i_create_property_manager_page(self, value):
		"""Creates a PropertyManager page."""
		self._instance.ICreatePropertyManagerPage = value

	@property
	def i_define_attribute(self):
		"""Creates an attribute definition, which is the first step in generating attributes."""
		return self._instance.IDefineAttribute

	@i_define_attribute.setter
	def i_define_attribute(self, value):
		"""Creates an attribute definition, which is the first step in generating attributes."""
		self._instance.IDefineAttribute = value

	@property
	def i_get_color_table(self):
		"""Gets a color table from the SOLIDWORKS application."""
		return self._instance.IGetColorTable

	@i_get_color_table.setter
	def i_get_color_table(self, value):
		"""Gets a color table from the SOLIDWORKS application."""
		self._instance.IGetColorTable = value

	@property
	def i_get_configuration_names(self):
		"""Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed."""
		return self._instance.IGetConfigurationNames

	@i_get_configuration_names.setter
	def i_get_configuration_names(self, value):
		"""Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed."""
		self._instance.IGetConfigurationNames = value

	@property
	def i_get_document_dependencies(self):
		"""Gets all of the model dependencies for a document."""
		return self._instance.IGetDocumentDependencies2

	@i_get_document_dependencies.setter
	def i_get_document_dependencies(self, value):
		"""Gets all of the model dependencies for a document."""
		self._instance.IGetDocumentDependencies2 = value

	@property
	def i_get_document_dependencies_count(self):
		"""Gets the size of the array needed for a call to ISldWorks::IGetDocumetnDependencies2."""
		return self._instance.IGetDocumentDependenciesCount2

	@i_get_document_dependencies_count.setter
	def i_get_document_dependencies_count(self, value):
		"""Gets the size of the array needed for a call to ISldWorks::IGetDocumetnDependencies2."""
		self._instance.IGetDocumentDependenciesCount2 = value

	@property
	def i_get_documents(self):
		"""Gets the open documents is this SOLIDWORKS session."""
		return self._instance.IGetDocuments

	@i_get_documents.setter
	def i_get_documents(self, value):
		"""Gets the open documents is this SOLIDWORKS session."""
		self._instance.IGetDocuments = value

	@property
	def i_get_environment(self):
		"""Gets the IEnvironment object."""
		return self._instance.IGetEnvironment

	@i_get_environment.setter
	def i_get_environment(self, value):
		"""Gets the IEnvironment object."""
		self._instance.IGetEnvironment = value

	@property
	def i_get_first_document(self):
		"""Gets the document opened first in this SOLIDWORKS session."""
		return self._instance.IGetFirstDocument2

	@i_get_first_document.setter
	def i_get_first_document(self, value):
		"""Gets the document opened first in this SOLIDWORKS session."""
		self._instance.IGetFirstDocument2 = value

	@property
	def i_get_mass_properties(self):
		"""Gets the mass properties from the specified document for the specified configuration."""
		return self._instance.IGetMassProperties2

	@i_get_mass_properties.setter
	def i_get_mass_properties(self, value):
		"""Gets the mass properties from the specified document for the specified configuration."""
		self._instance.IGetMassProperties2 = value

	@property
	def i_get_material_databases(self):
		"""Gets the names of the material databases."""
		return self._instance.IGetMaterialDatabases

	@i_get_material_databases.setter
	def i_get_material_databases(self, value):
		"""Gets the names of the material databases."""
		self._instance.IGetMaterialDatabases = value

	@property
	def i_get_math_utility(self):
		"""Gets the IMathUtility interface."""
		return self._instance.IGetMathUtility

	@i_get_math_utility.setter
	def i_get_math_utility(self, value):
		"""Gets the IMathUtility interface."""
		self._instance.IGetMathUtility = value

	@property
	def i_get_modeler(self):
		"""Gets the IModeler interface."""
		return self._instance.IGetModeler

	@i_get_modeler.setter
	def i_get_modeler(self, value):
		"""Gets the IModeler interface."""
		self._instance.IGetModeler = value

	@property
	def i_get_open_document_by_name(self):
		"""Gets the open document with the specified name."""
		return self._instance.IGetOpenDocumentByName2

	@i_get_open_document_by_name.setter
	def i_get_open_document_by_name(self, value):
		"""Gets the open document with the specified name."""
		self._instance.IGetOpenDocumentByName2 = value

	@property
	def i_get_ray_trace_renderer(self):
		"""Get a ray-trace rendering engine."""
		return self._instance.IGetRayTraceRenderer

	@i_get_ray_trace_renderer.setter
	def i_get_ray_trace_renderer(self, value):
		"""Get a ray-trace rendering engine."""
		self._instance.IGetRayTraceRenderer = value

	@property
	def i_get_selection_filters(self):
		"""Gets all active selection filters."""
		return self._instance.IGetSelectionFilters

	@i_get_selection_filters.setter
	def i_get_selection_filters(self, value):
		"""Gets all active selection filters."""
		self._instance.IGetSelectionFilters = value

	@property
	def i_get_selection_filters_count(self):
		"""Gets the number of active selection filters."""
		return self._instance.IGetSelectionFiltersCount

	@i_get_selection_filters_count.setter
	def i_get_selection_filters_count(self, value):
		"""Gets the number of active selection filters."""
		self._instance.IGetSelectionFiltersCount = value

	@property
	def i_get_template_sizes(self):
		"""Gets the sheet properties from a template document."""
		return self._instance.IGetTemplateSizes

	@i_get_template_sizes.setter
	def i_get_template_sizes(self, value):
		"""Gets the sheet properties from a template document."""
		self._instance.IGetTemplateSizes = value

	@property
	def i_get_user_type_lib_references(self):
		"""Gets the specified user-specified type library references."""
		return self._instance.IGetUserTypeLibReferences

	@i_get_user_type_lib_references.setter
	def i_get_user_type_lib_references(self, value):
		"""Gets the specified user-specified type library references."""
		self._instance.IGetUserTypeLibReferences = value

	@property
	def i_get_user_unit(self):
		"""Gets an empty IUserUnit object of the specified type."""
		return self._instance.IGetUserUnit

	@i_get_user_unit.setter
	def i_get_user_unit(self, value):
		"""Gets an empty IUserUnit object of the specified type."""
		self._instance.IGetUserUnit = value

	@property
	def i_get_version_history_count(self):
		"""Gets the size of the array required to hold data returned by ISldWorks::IVersionHistory."""
		return self._instance.IGetVersionHistoryCount

	@i_get_version_history_count.setter
	def i_get_version_history_count(self, value):
		"""Gets the size of the array required to hold data returned by ISldWorks::IVersionHistory."""
		self._instance.IGetVersionHistoryCount = value

	@property
	def i_move_document(self):
		"""Moves a document and optionally updates references to it."""
		return self._instance.IMoveDocument

	@i_move_document.setter
	def i_move_document(self, value):
		"""Moves a document and optionally updates references to it."""
		self._instance.IMoveDocument = value

	@property
	def import_hole_wizard_item(self):
		"""Imports data for the specified Hole Wizard standard."""
		return self._instance.ImportHoleWizardItem

	@import_hole_wizard_item.setter
	def import_hole_wizard_item(self, value):
		"""Imports data for the specified Hole Wizard standard."""
		self._instance.ImportHoleWizardItem = value

	@property
	def import_toolbox_item(self):
		"""Imports data for the specified Toolbox standard."""
		return self._instance.ImportToolboxItem

	@import_toolbox_item.setter
	def import_toolbox_item(self, value):
		"""Imports data for the specified Toolbox standard."""
		self._instance.ImportToolboxItem = value

	@property
	def i_new_document(self):
		"""Creates a new document based on the specified template."""
		return self._instance.INewDocument2

	@i_new_document.setter
	def i_new_document(self, value):
		"""Creates a new document based on the specified template."""
		self._instance.INewDocument2 = value

	@property
	def install_quick_tip_guide(self):
		"""Implements your add-in's copy of the Quick Tips."""
		return self._instance.InstallQuickTipGuide

	@install_quick_tip_guide.setter
	def install_quick_tip_guide(self, value):
		"""Implements your add-in's copy of the Quick Tips."""
		self._instance.InstallQuickTipGuide = value

	@property
	def i_remove_user_type_lib_references(self):
		"""Removes the user-specified type library references."""
		return self._instance.IRemoveUserTypeLibReferences

	@i_remove_user_type_lib_references.setter
	def i_remove_user_type_lib_references(self, value):
		"""Removes the user-specified type library references."""
		self._instance.IRemoveUserTypeLibReferences = value

	@property
	def is_background_processing_completed(self):
		"""Gets whether SOLIDWORKS has finished background processing a drawing document that requires a lot of CPU time to open."""
		return self._instance.IsBackgroundProcessingCompleted

	@is_background_processing_completed.setter
	def is_background_processing_completed(self, value):
		"""Gets whether SOLIDWORKS has finished background processing a drawing document that requires a lot of CPU time to open."""
		self._instance.IsBackgroundProcessingCompleted = value

	@property
	def is_command_enabled(self):
		"""Gets whether the specified command is enabled."""
		return self._instance.IsCommandEnabled

	@is_command_enabled.setter
	def is_command_enabled(self, value):
		"""Gets whether the specified command is enabled."""
		self._instance.IsCommandEnabled = value

	@property
	def i_set_selection_filters(self):
		"""Sets the status for multiple selection filters."""
		return self._instance.ISetSelectionFilters

	@i_set_selection_filters.setter
	def i_set_selection_filters(self, value):
		"""Sets the status for multiple selection filters."""
		self._instance.ISetSelectionFilters = value

	@property
	def i_set_user_type_lib_references(self):
		"""Sets the user-specified type library references."""
		return self._instance.ISetUserTypeLibReferences

	@i_set_user_type_lib_references.setter
	def i_set_user_type_lib_references(self, value):
		"""Sets the user-specified type library references."""
		self._instance.ISetUserTypeLibReferences = value

	@property
	def is_rapid_draft(self):
		"""Gets whether the specified drawing file is in SOLIDWORKS Detached format."""
		return self._instance.IsRapidDraft

	@is_rapid_draft.setter
	def is_rapid_draft(self, value):
		"""Gets whether the specified drawing file is in SOLIDWORKS Detached format."""
		self._instance.IsRapidDraft = value

	@property
	def is_same(self):
		"""Gets whether the two specified objects are the same object."""
		return self._instance.IsSame

	@is_same.setter
	def is_same(self, value):
		"""Gets whether the two specified objects are the same object."""
		self._instance.IsSame = value

	@property
	def i_version_history(self):
		"""Gets a list of strings indicating the versions in which a model was saved."""
		return self._instance.IVersionHistory

	@i_version_history.setter
	def i_version_history(self, value):
		"""Gets a list of strings indicating the versions in which a model was saved."""
		self._instance.IVersionHistory = value

	@property
	def load_add_in(self):
		"""Loads the specified add-in in SOLIDWORKS."""
		return self._instance.LoadAddIn

	@load_add_in.setter
	def load_add_in(self, value):
		"""Loads the specified add-in in SOLIDWORKS."""
		self._instance.LoadAddIn = value

	@property
	def load_file(self):
		"""Loads a third-party native CAD file into a new SOLIDWORKS document using 3D Interconnect."""
		return self._instance.LoadFile4

	@load_file.setter
	def load_file(self, value):
		"""Loads a third-party native CAD file into a new SOLIDWORKS document using 3D Interconnect."""
		self._instance.LoadFile4 = value

	@property
	def move_document(self):
		"""Moves a document and optionally updates references to it."""
		return self._instance.MoveDocument

	@move_document.setter
	def move_document(self, value):
		"""Moves a document and optionally updates references to it."""
		self._instance.MoveDocument = value

	@property
	def new_document(self):
		"""Creates a new document based on the specified template."""
		return self._instance.NewDocument

	@new_document.setter
	def new_document(self, value):
		"""Creates a new document based on the specified template."""
		self._instance.NewDocument = value

	@property
	def open_doc(self):
		"""Opens an existing document and returns a pointer to the document object."""
		return self._instance.OpenDoc6

	@open_doc.setter
	def open_doc(self, value):
		"""Opens an existing document and returns a pointer to the document object."""
		self._instance.OpenDoc6 = value

	@property
	def open_doc(self):
		"""Opens an existing document and returns a pointer to the document object."""
		return self._instance.OpenDoc7

	@open_doc.setter
	def open_doc(self, value):
		"""Opens an existing document and returns a pointer to the document object."""
		self._instance.OpenDoc7 = value

	@property
	def paste_appearance(self):
		"""Applies to the specified entity an appearance that has been copied to the clipboard."""
		return self._instance.PasteAppearance

	@paste_appearance.setter
	def paste_appearance(self, value):
		"""Applies to the specified entity an appearance that has been copied to the clipboard."""
		self._instance.PasteAppearance = value

	@property
	def post_message_to_application(self):
		"""Posts a message to the application that invoked this method."""
		return self._instance.PostMessageToApplication

	@post_message_to_application.setter
	def post_message_to_application(self, value):
		"""Posts a message to the application that invoked this method."""
		self._instance.PostMessageToApplication = value

	@property
	def post_message_to_applicationx(self):
		"""Posts a message to the application that invoked this method in 64-bit applications."""
		return self._instance.PostMessageToApplicationx64

	@post_message_to_applicationx.setter
	def post_message_to_applicationx(self, value):
		"""Posts a message to the application that invoked this method in 64-bit applications."""
		self._instance.PostMessageToApplicationx64 = value

	@property
	def pre_select_dwg_template_size(self):
		"""Establishes which template to use when creating a drawing."""
		return self._instance.PreSelectDwgTemplateSize

	@pre_select_dwg_template_size.setter
	def pre_select_dwg_template_size(self, value):
		"""Establishes which template to use when creating a drawing."""
		self._instance.PreSelectDwgTemplateSize = value

	@property
	def preset_new_drawing_parameters(self):
		"""Presets the drawing template and sheet size parameters to avoid showing the Sheet Format/Size dialog when creating a new drawing document in the user-interface."""
		return self._instance.PresetNewDrawingParameters

	@preset_new_drawing_parameters.setter
	def preset_new_drawing_parameters(self, value):
		"""Presets the drawing template and sheet size parameters to avoid showing the Sheet Format/Size dialog when creating a new drawing document in the user-interface."""
		self._instance.PresetNewDrawingParameters = value

	@property
	def preview_doc(self):
		"""Displays a preview of a document to the specified window."""
		return self._instance.PreviewDoc

	@preview_doc.setter
	def preview_doc(self, value):
		"""Displays a preview of a document to the specified window."""
		self._instance.PreviewDoc = value

	@property
	def preview_docx(self):
		"""Displays a preview of a document to the specified window in 64-bit applications."""
		return self._instance.PreviewDocx64

	@preview_docx.setter
	def preview_docx(self, value):
		"""Displays a preview of a document to the specified window in 64-bit applications."""
		self._instance.PreviewDocx64 = value

	@property
	def quit_doc(self):
		"""Closes the specified document without saving changes."""
		return self._instance.QuitDoc

	@quit_doc.setter
	def quit_doc(self, value):
		"""Closes the specified document without saving changes."""
		self._instance.QuitDoc = value

	@property
	def record_line(self):
		"""Adds a line of code to a VBA macro and the SOLIDWORKS journal file."""
		return self._instance.RecordLine

	@record_line.setter
	def record_line(self, value):
		"""Adds a line of code to a VBA macro and the SOLIDWORKS journal file."""
		self._instance.RecordLine = value

	@property
	def record_line_c_sharp(self):
		"""Adds a line of code to a C# macro and the SOLIDWORKS journal file."""
		return self._instance.RecordLineCSharp

	@record_line_c_sharp.setter
	def record_line_c_sharp(self, value):
		"""Adds a line of code to a C# macro and the SOLIDWORKS journal file."""
		self._instance.RecordLineCSharp = value

	@property
	def record_line_v_bnet(self):
		"""Adds a line of code to a VB.NET macro and the SOLIDWORKS journal file."""
		return self._instance.RecordLineVBnet

	@record_line_v_bnet.setter
	def record_line_v_bnet(self, value):
		"""Adds a line of code to a VB.NET macro and the SOLIDWORKS journal file."""
		self._instance.RecordLineVBnet = value

	@property
	def refresh_quick_tip_window(self):
		"""Tells the SOLIDWORKS application that your add-in's state has changed and triggers a query for the current URL page."""
		return self._instance.RefreshQuickTipWindow

	@refresh_quick_tip_window.setter
	def refresh_quick_tip_window(self, value):
		"""Tells the SOLIDWORKS application that your add-in's state has changed and triggers a query for the current URL page."""
		self._instance.RefreshQuickTipWindow = value

	@property
	def refresh_taskpane_content(self):
		"""Refreshes the view of the Design Library tab in the Task Pane."""
		return self._instance.RefreshTaskpaneContent

	@refresh_taskpane_content.setter
	def refresh_taskpane_content(self, value):
		"""Refreshes the view of the Design Library tab in the Task Pane."""
		self._instance.RefreshTaskpaneContent = value

	@property
	def register_third_party_popup_menu(self):
		"""Registers a third-party pop-up (shortcut) menu."""
		return self._instance.RegisterThirdPartyPopupMenu

	@register_third_party_popup_menu.setter
	def register_third_party_popup_menu(self, value):
		"""Registers a third-party pop-up (shortcut) menu."""
		self._instance.RegisterThirdPartyPopupMenu = value

	@property
	def register_tracking_definition(self):
		"""Registers a tracking definition."""
		return self._instance.RegisterTrackingDefinition

	@register_tracking_definition.setter
	def register_tracking_definition(self, value):
		"""Registers a tracking definition."""
		self._instance.RegisterTrackingDefinition = value

	@property
	def remove_callback(self):
		"""Unregisters a general purpose callback handler."""
		return self._instance.RemoveCallback

	@remove_callback.setter
	def remove_callback(self, value):
		"""Unregisters a general purpose callback handler."""
		self._instance.RemoveCallback = value

	@property
	def remove_file_open_item(self):
		"""Removes a file type from the File > Open dialog box that was added using ISldWorks::AddFileOpenItem3."""
		return self._instance.RemoveFileOpenItem2

	@remove_file_open_item.setter
	def remove_file_open_item(self, value):
		"""Removes a file type from the File > Open dialog box that was added using ISldWorks::AddFileOpenItem3."""
		self._instance.RemoveFileOpenItem2 = value

	@property
	def remove_file_save_as_item(self):
		"""Removes a file type from the File > Save As dialog box that was added using ISldWorks::AddFileSaveAsItem2."""
		return self._instance.RemoveFileSaveAsItem2

	@remove_file_save_as_item.setter
	def remove_file_save_as_item(self, value):
		"""Removes a file type from the File > Save As dialog box that was added using ISldWorks::AddFileSaveAsItem2."""
		self._instance.RemoveFileSaveAsItem2 = value

	@property
	def remove_from_menu(self):
		"""Removes: 


the specified command from all main frame menus or a toolbar or both

the specified command's parent menus"""
		return self._instance.RemoveFromMenu

	@remove_from_menu.setter
	def remove_from_menu(self, value):
		"""Removes: 


the specified command from all main frame menus or a toolbar or both

the specified command's parent menus"""
		self._instance.RemoveFromMenu = value

	@property
	def remove_from_popup_menu(self):
		"""Removes the specified menu item from one or all specified context-sensitive menus (also called shortcut menus and pop-up menus) for the specified document types."""
		return self._instance.RemoveFromPopupMenu

	@remove_from_popup_menu.setter
	def remove_from_popup_menu(self, value):
		"""Removes the specified menu item from one or all specified context-sensitive menus (also called shortcut menus and pop-up menus) for the specified document types."""
		self._instance.RemoveFromPopupMenu = value

	@property
	def remove_item_from_third_party_popup_menu(self):
		"""Removes a menu item and icon from a third-party pop-up (shortcut) menu."""
		return self._instance.RemoveItemFromThirdPartyPopupMenu

	@remove_item_from_third_party_popup_menu.setter
	def remove_item_from_third_party_popup_menu(self, value):
		"""Removes a menu item and icon from a third-party pop-up (shortcut) menu."""
		self._instance.RemoveItemFromThirdPartyPopupMenu = value

	@property
	def remove_menu(self):
		"""Removes a menu item from the specified document frame."""
		return self._instance.RemoveMenu

	@remove_menu.setter
	def remove_menu(self, value):
		"""Removes a menu item from the specified document frame."""
		self._instance.RemoveMenu = value

	@property
	def remove_menu_popup_item(self):
		"""Removes an item on a pop-up (shortcut) menu."""
		return self._instance.RemoveMenuPopupItem2

	@remove_menu_popup_item.setter
	def remove_menu_popup_item(self, value):
		"""Removes an item on a pop-up (shortcut) menu."""
		self._instance.RemoveMenuPopupItem2 = value

	@property
	def remove_toolbar(self):
		"""Removes a toolbar created with ISldWorks::AddToolbar5."""
		return self._instance.RemoveToolbar2

	@remove_toolbar.setter
	def remove_toolbar(self, value):
		"""Removes a toolbar created with ISldWorks::AddToolbar5."""
		self._instance.RemoveToolbar2 = value

	@property
	def remove_user_type_lib_references(self):
		"""Removes the user-specified type library references."""
		return self._instance.RemoveUserTypeLibReferences

	@remove_user_type_lib_references.setter
	def remove_user_type_lib_references(self, value):
		"""Removes the user-specified type library references."""
		self._instance.RemoveUserTypeLibReferences = value

	@property
	def replace_referenced_document(self):
		"""Replaces a referenced document."""
		return self._instance.ReplaceReferencedDocument

	@replace_referenced_document.setter
	def replace_referenced_document(self, value):
		"""Replaces a referenced document."""
		self._instance.ReplaceReferencedDocument = value

	@property
	def reset_preset_drawing_parameters(self):
		"""Resets SOLIDWORKS back to its default behavior after calling ISldWorks::PresetNewDrawingParameters (i.e., display Sheet Format/Size dialog when opening a new drawing document)."""
		return self._instance.ResetPresetDrawingParameters

	@reset_preset_drawing_parameters.setter
	def reset_preset_drawing_parameters(self, value):
		"""Resets SOLIDWORKS back to its default behavior after calling ISldWorks::PresetNewDrawingParameters (i.e., display Sheet Format/Size dialog when opening a new drawing document)."""
		self._instance.ResetPresetDrawingParameters = value

	@property
	def reset_untitled_count(self):
		"""Resets the index of untitled documents."""
		return self._instance.ResetUntitledCount

	@reset_untitled_count.setter
	def reset_untitled_count(self, value):
		"""Resets the index of untitled documents."""
		self._instance.ResetUntitledCount = value

	@property
	def restore_settings(self):
		"""Restores the specified SOLIDWORKS settings from the specified *.sldreg file."""
		return self._instance.RestoreSettings

	@restore_settings.setter
	def restore_settings(self, value):
		"""Restores the specified SOLIDWORKS settings from the specified *.sldreg file."""
		self._instance.RestoreSettings = value

	@property
	def resume_skinning(self):
		"""Resumes skinning windows."""
		return self._instance.ResumeSkinning

	@resume_skinning.setter
	def resume_skinning(self, value):
		"""Resumes skinning windows."""
		self._instance.ResumeSkinning = value

	@property
	def revision_number(self):
		"""Gets the version number of this SOLIDWORKS installation."""
		return self._instance.RevisionNumber

	@revision_number.setter
	def revision_number(self, value):
		"""Gets the version number of this SOLIDWORKS installation."""
		self._instance.RevisionNumber = value

	@property
	def run_attached_macro(self):
		"""Runs the specified attached macro, module, and procedure."""
		return self._instance.RunAttachedMacro

	@run_attached_macro.setter
	def run_attached_macro(self, value):
		"""Runs the specified attached macro, module, and procedure."""
		self._instance.RunAttachedMacro = value

	@property
	def run_command(self):
		"""Runs the specified SOLIDWORKS command."""
		return self._instance.RunCommand

	@run_command.setter
	def run_command(self, value):
		"""Runs the specified SOLIDWORKS command."""
		self._instance.RunCommand = value

	@property
	def run_journal_cmd(self):
		"""Do not use."""
		return self._instance.RunJournalCmd

	@run_journal_cmd.setter
	def run_journal_cmd(self, value):
		"""Do not use."""
		self._instance.RunJournalCmd = value

	@property
	def run_macro(self):
		"""Runs a macro from a project file."""
		return self._instance.RunMacro2

	@run_macro.setter
	def run_macro(self, value):
		"""Runs a macro from a project file."""
		self._instance.RunMacro2 = value

	@property
	def save_settings(self):
		"""Saves the specified SOLIDWORKS settings to the specified *.sldreg file."""
		return self._instance.SaveSettings

	@save_settings.setter
	def save_settings(self, value):
		"""Saves the specified SOLIDWORKS settings to the specified *.sldreg file."""
		self._instance.SaveSettings = value

	@property
	def send_msg_to_user(self):
		"""Displays a message box containing a message to the user, who is required to interact with it before continuing."""
		return self._instance.SendMsgToUser2

	@send_msg_to_user.setter
	def send_msg_to_user(self, value):
		"""Displays a message box containing a message to the user, who is required to interact with it before continuing."""
		self._instance.SendMsgToUser2 = value

	@property
	def set_addin_callback_info(self):
		"""Sets add-in callback commands."""
		return self._instance.SetAddinCallbackInfo2

	@set_addin_callback_info.setter
	def set_addin_callback_info(self, value):
		"""Sets add-in callback commands."""
		self._instance.SetAddinCallbackInfo2 = value

	@property
	def set_apply_selection_filter(self):
		"""Sets the current state of the selection filter."""
		return self._instance.SetApplySelectionFilter

	@set_apply_selection_filter.setter
	def set_apply_selection_filter(self, value):
		"""Sets the current state of the selection filter."""
		self._instance.SetApplySelectionFilter = value

	@property
	def set_current_working_directory(self):
		"""Sets the current working directory to be used by SOLIDWORKS."""
		return self._instance.SetCurrentWorkingDirectory

	@set_current_working_directory.setter
	def set_current_working_directory(self, value):
		"""Sets the current working directory to be used by SOLIDWORKS."""
		self._instance.SetCurrentWorkingDirectory = value

	@property
	def set_missing_reference_path_name(self):
		"""Sets the missing reference file name. Use with the SOLIDWORKS event ReferenceNotFoundNotify."""
		return self._instance.SetMissingReferencePathName

	@set_missing_reference_path_name.setter
	def set_missing_reference_path_name(self, value):
		"""Sets the missing reference file name. Use with the SOLIDWORKS event ReferenceNotFoundNotify."""
		self._instance.SetMissingReferencePathName = value

	@property
	def set_mouse_drag_mode(self):
		"""Sets the command-mouse mode."""
		return self._instance.SetMouseDragMode

	@set_mouse_drag_mode.setter
	def set_mouse_drag_mode(self, value):
		"""Sets the command-mouse mode."""
		self._instance.SetMouseDragMode = value

	@property
	def set_multiple_filenames_prompt(self):
		"""Sets the new filenames to open in response to the ISldWorks PromptForMultipleFileNamesNotify event."""
		return self._instance.SetMultipleFilenamesPrompt

	@set_multiple_filenames_prompt.setter
	def set_multiple_filenames_prompt(self, value):
		"""Sets the new filenames to open in response to the ISldWorks PromptForMultipleFileNamesNotify event."""
		self._instance.SetMultipleFilenamesPrompt = value

	@property
	def set_new_filename(self):
		"""Sets the name of the new SOLIDWORKS file."""
		return self._instance.SetNewFilename

	@set_new_filename.setter
	def set_new_filename(self, value):
		"""Sets the name of the new SOLIDWORKS file."""
		self._instance.SetNewFilename = value

	@property
	def set_prompt_filename(self):
		"""Sets the file to open in response to a SOLIDWORKS event."""
		return self._instance.SetPromptFilename2

	@set_prompt_filename.setter
	def set_prompt_filename(self, value):
		"""Sets the file to open in response to a SOLIDWORKS event."""
		self._instance.SetPromptFilename2 = value

	@property
	def set_search_folders(self):
		"""Sets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for  > Referenced Documents."""
		return self._instance.SetSearchFolders

	@set_search_folders.setter
	def set_search_folders(self, value):
		"""Sets the current folder search path as shown in Tools > Options > System Options > File Locations > Show folders for  > Referenced Documents."""
		self._instance.SetSearchFolders = value

	@property
	def set_selection_filter(self):
		"""Sets the current selection filter values for the specified item type."""
		return self._instance.SetSelectionFilter

	@set_selection_filter.setter
	def set_selection_filter(self, value):
		"""Sets the current selection filter values for the specified item type."""
		self._instance.SetSelectionFilter = value

	@property
	def set_selection_filters(self):
		"""Sets the status for multiple selection filters."""
		return self._instance.SetSelectionFilters

	@set_selection_filters.setter
	def set_selection_filters(self, value):
		"""Sets the status for multiple selection filters."""
		self._instance.SetSelectionFilters = value

	@property
	def set_third_party_popup_menu_state(self):
		"""Sets whether to show or hide a third-party popup (shortcut) menu."""
		return self._instance.SetThirdPartyPopupMenuState

	@set_third_party_popup_menu_state.setter
	def set_third_party_popup_menu_state(self, value):
		"""Sets whether to show or hide a third-party popup (shortcut) menu."""
		self._instance.SetThirdPartyPopupMenuState = value

	@property
	def set_toolbar_dock(self):
		"""Sets the docking state of the toolbar."""
		return self._instance.SetToolbarDock2

	@set_toolbar_dock.setter
	def set_toolbar_dock(self, value):
		"""Sets the docking state of the toolbar."""
		self._instance.SetToolbarDock2 = value

	@property
	def set_toolbar_visibility(self):
		"""Sets whether the specified toolbar is visible."""
		return self._instance.SetToolbarVisibility

	@set_toolbar_visibility.setter
	def set_toolbar_visibility(self, value):
		"""Sets whether the specified toolbar is visible."""
		self._instance.SetToolbarVisibility = value

	@property
	def set_user_preference_double_value(self):
		"""Sets system default user preference values."""
		return self._instance.SetUserPreferenceDoubleValue

	@set_user_preference_double_value.setter
	def set_user_preference_double_value(self, value):
		"""Sets system default user preference values."""
		self._instance.SetUserPreferenceDoubleValue = value

	@property
	def set_user_preference_integer_value(self):
		"""Sets system default user preference values."""
		return self._instance.SetUserPreferenceIntegerValue

	@set_user_preference_integer_value.setter
	def set_user_preference_integer_value(self, value):
		"""Sets system default user preference values."""
		self._instance.SetUserPreferenceIntegerValue = value

	@property
	def set_user_preference_string_list_value(self):
		"""Sets the name of the DXF mapping files."""
		return self._instance.SetUserPreferenceStringListValue

	@set_user_preference_string_list_value.setter
	def set_user_preference_string_list_value(self, value):
		"""Sets the name of the DXF mapping files."""
		self._instance.SetUserPreferenceStringListValue = value

	@property
	def set_user_preference_string_value(self):
		"""Sets system default user preference values."""
		return self._instance.SetUserPreferenceStringValue

	@set_user_preference_string_value.setter
	def set_user_preference_string_value(self, value):
		"""Sets system default user preference values."""
		self._instance.SetUserPreferenceStringValue = value

	@property
	def set_user_preference_toggle(self):
		"""Sets system default user preference values."""
		return self._instance.SetUserPreferenceToggle

	@set_user_preference_toggle.setter
	def set_user_preference_toggle(self, value):
		"""Sets system default user preference values."""
		self._instance.SetUserPreferenceToggle = value

	@property
	def show_bubble_tooltip(self):
		"""Displays a bubble ToolTip and flashes the specified toolbar button."""
		return self._instance.ShowBubbleTooltip

	@show_bubble_tooltip.setter
	def show_bubble_tooltip(self, value):
		"""Displays a bubble ToolTip and flashes the specified toolbar button."""
		self._instance.ShowBubbleTooltip = value

	@property
	def show_bubble_tooltip_at(self):
		"""Displays a bubble ToolTip at the specified location."""
		return self._instance.ShowBubbleTooltipAt2

	@show_bubble_tooltip_at.setter
	def show_bubble_tooltip_at(self, value):
		"""Displays a bubble ToolTip at the specified location."""
		self._instance.ShowBubbleTooltipAt2 = value

	@property
	def show_help(self):
		"""Displays the specified Help topic."""
		return self._instance.ShowHelp

	@show_help.setter
	def show_help(self, value):
		"""Displays the specified Help topic."""
		self._instance.ShowHelp = value

	@property
	def show_third_party_popup_menu(self):
		"""Sets where to show a third-party pop-up (shortcut) menu."""
		return self._instance.ShowThirdPartyPopupMenu

	@show_third_party_popup_menu.setter
	def show_third_party_popup_menu(self, value):
		"""Sets where to show a third-party pop-up (shortcut) menu."""
		self._instance.ShowThirdPartyPopupMenu = value

	@property
	def solid_works_explorer(self):
		"""Starts SOLIDWORKS Explorer."""
		return self._instance.SolidWorksExplorer

	@solid_works_explorer.setter
	def solid_works_explorer(self, value):
		"""Starts SOLIDWORKS Explorer."""
		self._instance.SolidWorksExplorer = value

	@property
	def un_install_quick_tip_guide(self):
		"""Uninstalls your add-in's Quick Tips"""
		return self._instance.UnInstallQuickTipGuide

	@un_install_quick_tip_guide.setter
	def un_install_quick_tip_guide(self, value):
		"""Uninstalls your add-in's Quick Tips"""
		self._instance.UnInstallQuickTipGuide = value

	@property
	def unload_add_in(self):
		"""Unloads the specified add-in from SOLIDWORKS."""
		return self._instance.UnloadAddIn

	@unload_add_in.setter
	def unload_add_in(self, value):
		"""Unloads the specified add-in from SOLIDWORKS."""
		self._instance.UnloadAddIn = value

	@property
	def upload_to_my_solid_works_settings(self):
		"""Uploads the specified SOLIDWORKS Desktop settings to SOLIDWORKS Connected."""
		return self._instance.UploadToMySolidWorksSettings

	@upload_to_my_solid_works_settings.setter
	def upload_to_my_solid_works_settings(self, value):
		"""Uploads the specified SOLIDWORKS Desktop settings to SOLIDWORKS Connected."""
		self._instance.UploadToMySolidWorksSettings = value

	@property
	def version_history(self):
		"""Gets a list of strings indicating the versions in which a model was saved."""
		return self._instance.VersionHistory

	@version_history.setter
	def version_history(self, value):
		"""Gets a list of strings indicating the versions in which a model was saved."""
		self._instance.VersionHistory = value

