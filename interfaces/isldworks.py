from com import Com
from doc import Doc
import win32com.client as win32
import pythoncom
import os
import interfaces.ienumdocuments
import interfaces.iexportpdfdata


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html

class ISldWorks:
    def __init__(self):
        self._instance = Com('SldWorks.Application')
        # self._instance.Visible = True

    @property
    def active_doc(self):
        """
        Gets the currently active document.
        :return: IModelDoc
        """
        return Doc(self._instance.ActiveDoc)

    @property
    def command_in_progress(self):
        """
        Improves performance of out-of-process applications by informing SOLIDWORKS that a sequence of API calls will be
        made by the out-of-process application.
        :return: bool
        """
        return self._instance.CommandInProgress

    @command_in_progress.setter
    def command_in_progress(self, state):
        """
        Improves performance of out-of-process applications by informing SOLIDWORKS that a sequence of API calls will be
        made by the out-of-process application.
        :param state: bool
        :return: None
        """
        self._instance.CommandInProgress = state

    @property
    def enable_background_processing(self):
        """
        Gets or sets whether to enable background processing.
        :return: bool
        """
        return self._instance.EnableBackgroundProcessing

    @enable_background_processing.setter
    def enable_background_processing(self, state):
        """
        Gets or sets whether to enable background processing.
        :param state: bool
        :return: None
        """
        self._instance.EnableBackgroundProcessing = state

    @property
    def visible(self):
        """
        Gets and sets the visibility property of the SOLIDWORKS application.
        :return: bool
        """
        return self._instance.Visible

    @visible.setter
    def visible(self, state):
        """
        Gets and sets the visibility property of the SOLIDWORKS application.
        :param state: bool
        :return: bool
        """
        self._instance.Visible = state

    def activate_doc(self, name, use_user_preferences=False, option=2):
        """
        Activates a loaded document and rebuilds it as specified.
        :param name: Name of the loaded document to activate
        :param use_user_preferences: True to rebuild as per the system option; false to rebuild as per Option
        :param option: Rebuild option as defined below
        :return: error? pointer?

        1 = do not rebuild the activated document
        2 = rebuild the activated document
        0 = prompt the user whether to rebuild the activated document
        """
        arg1 = win32.VARIANT(pythoncom.VT_BSTR, name)
        arg2 = win32.VARIANT(pythoncom.VT_BOOL, use_user_preferences)
        arg3 = win32.VARIANT(pythoncom.VT_I4, option)
        arg4 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        self._instance.ActivateDoc3(arg1, arg2, arg3, arg4)
        return arg4

    def activate_task_pane(self, task_pane_id):
        """
        Activates the specified task pane.
        :param task_pane_id: ID of task pane as defined below
        :return: bool
        4 = Clipboard tab
        5 = Custom Properties tab
        1 = Design Library tab
        2 = File Explorer tab
        6 = P&ID tab
        3 = SOLIDWORKS Resources tab
        """
        return self._instance.ActivateTaskPane(task_pane_id)

    def add_callback(self):
        """Registers a general purpose callback handler."""
        # return self._instance.AddCallback
        raise NotImplemented

    def add_file_open_item(self):
        """Adds file types to the File > Open dialog box."""
        # return self._instance.AddFileOpenItem3
        raise NotImplemented

    def add_file_save_as_item(self):
        """Adds a file type to the SOLIDWORKS File > Save As dialog box."""
        # return self._instance.AddFileSaveAsItem2
        raise NotImplemented

    # def add_item_to_third_party_popup_menu(self):
    #     """Adds menu items to a pop-up (shortcut) menu in a C++ SOLIDWORKS add-in."""
    #     # return self._instance.AddItemToThirdPartyPopupMenu
    #     raise NotImplemented

    def add_item_to_third_party_popup_menu(self):
        """Adds menu items to a pop-up (shortcut) menu in a SOLIDWORKS add-in."""
        # return self._instance.AddItemToThirdPartyPopupMenu2
        raise NotImplemented

    def add_menu(self):
        """Adds a menu item to a SOLIDWORKS menu for DLL applications."""
        # return self._instance.AddMenu
        raise NotImplemented

    def add_menu_item(self):
        """Adds a menu item and image to the SOLIDWORKS user interface."""
        # return self._instance.AddMenuItem5
        raise NotImplemented

    # def add_menu_popup_item(self):
    #     """Adds a menu item and zero or more submenus to shortcut menus of entities of the specified type in documents
    #     of the specified type."""
    #     # return self._instance.AddMenuPopupItem3
    #     raise NotImplemented

    def add_menu_popup_item(self):
        """Adds a menu item and zero or more submenus to shortcut menus of features of the specified type in documents
        of the specified type."""
        # return self._instance.AddMenuPopupItem4
        raise NotImplemented

    def add_toolbar(self):
        """Creates a Windows-style dockable toolbar."""
        # return self._instance.AddToolbar5
        raise NotImplemented

    def add_toolbar_command(self):
        """Specifies the application functions to call when a toolbar button is clicked or sets a separator."""
        # return self._instance.AddToolbarCommand2
        raise NotImplemented

    def allow_failed_feature_creation(self, yes_no):
        """Sets whether to allow the creation of a feature that has rebuild errors."""
        return self._instance.AllowFailedFeatureCreation(yes_no)

    def arrange_icons(self):
        """Arranges the icons in SOLIDWORKS."""
        return self._instance.ArrangeIcons

    def arrange_windows(self):
        """Arranges the open windows in SOLIDWORKS."""
        return self._instance.ArrangeWindows

    def block_skinning(self):
        """Blocks skinning a window, which prevents a window from looking like a SOLIDWORKS window."""
        # return self._instance.BlockSkinning
        raise NotImplemented

    def call_back(self):
        """Allows an out-of-process executable or a SOLIDWORKS macro to call back a function in a SOLIDWORKS add-in
        DLL."""
        # return self._instance.CallBack
        raise NotImplemented

    def checkpoint_converted_document(self):
        """Saves the specified open document if its version is older than the version of the SOLIDWORKS product being
        used."""
        # return self._instance.CheckpointConvertedDocument
        raise NotImplemented

    def close_all_documents(self, include_unsaved=False):
        """
        Closes all open documents in the SOLIDWORKS session.
        :param include_unsaved: bool, True = Close all documents, including dirty documents, False = Close all documents
        , excluding dirty documents
        :return: bool
        """
        return self._instance.CloseAllDocuments(include_unsaved)

    def close_and_reopen(self):
        """Closes and reopens the specified drawing document without unloading its references from memory."""
        # return self._instance.CloseAndReopen
        raise NotImplemented

    def close_doc(self, name):
        """Closes the specified document."""
        return self._instance.CloseDoc(name)

    def command(self):
        """Opens the specified dialog or file."""
        # return self._instance.Command
        raise NotImplemented

    def copy_appearance(self):
        """Copies the appearance of the specified entity to the clipboard."""
        # return self._instance.CopyAppearance
        raise NotImplemented

    def copy_document(self):
        """Copies a document and optionally updates references to it."""
        # return self._instance.CopyDocument
        raise NotImplemented

    def create_new_window(self):
        """Creates a client window containing the active document."""
        return self._instance.CreateNewWindow

    def create_property_manager_page(self):
        """Creates a PropertyManager page."""
        # return self._instance.CreatePropertyManagerPage
        raise NotImplemented

    def create_taskpane_view(self):
        """Creates an application-level Task Pane view."""
        # return self._instance.CreateTaskpaneView3
        raise NotImplemented

    def define_attribute(self):
        """Creates an attribute definition, which is the first step in generating attributes."""
        # return self._instance.DefineAttribute
        raise NotImplemented

    def display_status_bar(self, on_off):
        """Sets whether to display the status bar."""
        self._instance.DisplayStatusBar(on_off)

    def document_visible(self):
        """Allows the application to control the display of a document in a window upon creation or retrieval."""
        # return self._instance.DocumentVisible
        raise NotImplemented

    def download_from_my_solid_works_settings(self):
        """Downloads the specified SOLIDWORKS Connected settings to SOLIDWORKS Desktop."""
        # return self._instance.DownloadFromMySolidWorksSettings
        raise NotImplemented

    def drag_toolbar_button(self):
        """Copies the specified toolbar button from the specified native SOLIDWORKS toolbar or ICommandGroup toolbar
        to the specified native SOLIDWORKS toolbar or ICommandGroup toolbar."""
        # return self._instance.DragToolbarButton
        raise NotImplemented

    def drag_toolbar_button_from_command_i_d(self):
        """Copies a button to a toolbar using a command ID."""
        # return self._instance.DragToolbarButtonFromCommandID
        raise NotImplemented

    def enum_documents(self):
        """Gets a list of documents currently open in the application."""
        # return interfaces.ienumdocuments.IEnumDocuments(self._instance.EnumDocuments2)
        raise NotImplemented

    def exit_app(self):
        """Shuts down SOLIDWORKS."""
        return self._instance.ExitApp()
        # raise NotImplemented

    def export_hole_wizard_item(self):
        """Exports data for the specified Hole Wizard standard."""
        # return self._instance.ExportHoleWizardItem
        raise NotImplemented

    def export_toolbox_item(self):
        """Exports data for the specified Toolbox standard."""
        # return self._instance.ExportToolboxItem
        raise NotImplemented

    def frame(self):
        """Gets the SOLIDWORKS main frame."""
        # return self._instance.Frame
        raise NotImplemented

    def get_active_configuration_name(self):
        """Gets the name of the active configuration in the specified SOLIDWORKS document."""
        # return self._instance.GetActiveConfigurationName
        raise NotImplemented

    def get_add_in_object(self):
        """Gets an add-in object for the specified SOLIDWORKS add-in."""
        # return self._instance.GetAddInObject
        raise NotImplemented

    def get_apply_selection_filter(self):
        """Gets the current state of the selection filter."""
        # return self._instance.GetApplySelectionFilter
        raise NotImplemented

    def get_build_numbers(self):
        """Gets the build, major revision, and hot fix numbers of the SOLIDWORKS application."""
        # return self._instance.GetBuildNumbers2
        raise NotImplemented

    def get_button_position(self):
        """Gets the center coordinates of the specified SOLIDWORKS toolbar button."""
        # return self._instance.GetButtonPosition
        raise NotImplemented

    def get_collision_detection_manager(self):
        """Gets the collision detection manager."""
        # return self._instance.GetCollisionDetectionManager
        raise NotImplemented

    def get_color_table(self):
        """Gets a color table from the SOLIDWORKS application."""
        # return self._instance.GetColorTable
        raise NotImplemented

    def get_command_i_d(self):
        """Gets the SOLIDWORKS command ID for an instance of an add-in's control (e.g., an add-in's toolbar button)."""
        # return self._instance.GetCommandID
        raise NotImplemented

    def get_command_manager(self):
        """Gets the CommandManager for the specified add-in."""
        # return self._instance.GetCommandManager
        raise NotImplemented

    def get_configuration_count(self):
        """Gets the number of configurations in the SOLIDWORKS document, whether the document is opened or closed."""
        # return self._instance.GetConfigurationCount
        raise NotImplemented

    def get_configuration_names(self, file_path_name):
        """Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed."""
        return self._instance.GetConfigurationNames(file_path_name)

    def get_current_file_user(self):
        """Gets the name of the user who has the the specified document open."""
        # return self._instance.GetCurrentFileUser
        raise NotImplemented

    def get_current_language(self):
        """Gets the current language used by SOLIDWORKS."""
        # return self._instance.GetCurrentLanguage
        raise NotImplemented

    def get_current_license_type(self):
        """Gets the type of license for the current SOLIDWORKS session."""
        # return self._instance.GetCurrentLicenseType
        raise NotImplemented

    def get_current_macro_path_folder(self):
        """Gets the name of the folder where the macro resides."""
        # return self._instance.GetCurrentMacroPathFolder
        raise NotImplemented

    def get_current_macro_path_name(self):
        """Gets the path name for the macro currently running."""
        # return self._instance.GetCurrentMacroPathName
        raise NotImplemented

    def get_current_working_directory(self):
        """Gets the current working directory being used by the SOLIDWORKS application."""
        # return self._instance.GetCurrentWorkingDirectory
        raise NotImplemented

    def get_data_folder(self):
        """Gets the data directory name currently used by SOLIDWORKS."""
        # return self._instance.GetDataFolder
        raise NotImplemented

    def get_document_count(self):
        """Gets the number of open documents in the current SOLIDWORKS session."""
        # return self._instance.GetDocumentCount
        raise NotImplemented

    def get_document_dependencies(self):
        """Gets all of the model dependencies for a document."""
        # return self._instance.GetDocumentDependencies2
        raise NotImplemented

    def get_documents(self):
        """Gets the open documents in this SOLIDWORKS session."""
        # return self._instance.GetDocuments
        raise NotImplemented

    def get_document_template(self):
        """Gets the name of document template that can be used in ISldWorks::NewDocument or ISldWorks::INewDocument2."""
        # return self._instance.GetDocumentTemplate
        raise NotImplemented

    def get_document_visible(self):
        """Gets the visibility of the document to open."""
        # return self._instance.GetDocumentVisible
        raise NotImplemented

    def get_environment(self):
        """Gets the IEnvironment object."""
        # return self._instance.GetEnvironment
        raise NotImplemented

    def get_error_messages(self):
        """Gets the last 20 messages issued by SOLIDWORKS in the current SOLIDWORKS session."""
        # return self._instance.GetErrorMessages
        raise NotImplemented

    def get_executable_path(self):
        """Gets the path to the SOLIDWORKS executable, sldworks.exe."""
        # return self._instance.GetExecutablePath
        raise NotImplemented

    def get_export_file_data(self, file_type=1):
        """Gets the data interface for the specified file type to which to export one or more drawing sheets."""
        return interfaces.iexportpdfdata.IExportPdfData(self._instance.GetExportFileData(file_type))

    def get_first_document(self):
        """Gets the document opened first in this SOLIDWORKS session."""
        # return self._instance.GetFirstDocument
        raise NotImplemented

    def get_hole_standards_data(self):
        """Gets the hole standards for the specified hole type."""
        # return self._instance.GetHoleStandardsData
        raise NotImplemented

    def get_image_size(self):
        """asdasd"""
        # return self._instance.GetImageSize
        raise NotImplemented

    def get_import_file_data(self):
        """Gets the IGES or DXF/DWG import data for the specified file."""
        # return self._instance.GetImportFileData
        raise NotImplemented

    def get_interface_brightness_theme_colors(self):
        """Gets the theme and colors of the SOLIDWORKS background."""
        # return self._instance.GetInterfaceBrightnessThemeColors
        raise NotImplemented

    def get_last_save_error(self):
        """Gets the last save error issued by Microsoft in the current session."""
        # return self._instance.GetLastSaveError
        raise NotImplemented

    def get_last_toolbar_i_d(self):
        """Gets the ID of the last toolbar added to the CommandManager."""
        # return self._instance.GetLastToolbarID
        raise NotImplemented

    def get_latest_supported_file_version(self):
        """Gets the version number that this instance of SOLIDWORKS reads and writes."""
        # return self._instance.GetLatestSupportedFileVersion
        raise NotImplemented

    def get_line_styles(self):
        """Gets all of the line styles in the specified file."""
        # return self._instance.GetLineStyles
        raise NotImplemented

    def get_localized_menu_name(self):
        """Gets a localized menu name for the specified menu ID."""
        # return self._instance.GetLocalizedMenuName
        raise NotImplemented

    def get_macro_methods(self):
        """Gets the names of the modules in the specified macro."""
        # return self._instance.GetMacroMethods
        raise NotImplemented

    def get_mass_properties(self):
        """Gets the mass properties from the specified document for the specified configuration."""
        # return self._instance.GetMassProperties2
        raise NotImplemented

    def get_material_database_count(self):
        """Gets the number of material databases."""
        # return self._instance.GetMaterialDatabaseCount
        raise NotImplemented

    def get_material_databases(self):
        """Gets the names of the material databases."""
        # return self._instance.GetMaterialDatabases
        raise NotImplemented

    def get_material_schema_path_name(self):
        """Gets the path for the XML material schema file."""
        # return self._instance.GetMaterialSchemaPathName
        raise NotImplemented

    def get_math_utility(self):
        """Gets IMathUtility."""
        # return self._instance.GetMathUtility
        raise NotImplemented

    def get_menu_strings(self):
        """Gets the name of the parent menu of the specified menu command."""
        # return self._instance.GetMenuStrings
        raise NotImplemented

    def get_modeler(self):
        """Gets the IModeler interface."""
        # return self._instance.GetModeler
        raise NotImplemented

    def get_mouse_drag_mode(self):
        """Gets whether the specified command-mouse mode is in effect."""
        # return self._instance.GetMouseDragMode
        raise NotImplemented

    def get_open_doc_spec(self):
        """Gets the specifications to use when opening a model document."""
        # return self._instance.GetOpenDocSpec
        raise NotImplemented

    def get_open_document(self):
        """Gets the open document with the specified name."""
        # return self._instance.GetOpenDocument
        raise NotImplemented

    def get_open_document_by_name(self):
        """Gets the open document with the specified name."""
        # return self._instance.GetOpenDocumentByName
        raise NotImplemented

    def get_opened_file_info(self):
        """Gets the name of the last model successfully opened by SOLIDWORKS and the options that were in effect when
        it opened."""
        # return self._instance.GetOpenedFileInfo
        raise NotImplemented

    def get_open_file_name(self):
        """Prompts the user for the name of the file to open."""
        # return self._instance.GetOpenFileName
        raise NotImplemented

    def get_preview_bitmap(self):
        """Gets the preview bitmap (.bmp) for the specified configuration, regardless if the SOLIDWORKS document is
        open or closed."""
        # return self._instance.GetPreviewBitmap
        raise NotImplemented

    def get_preview_bitmap_file(self):
        """Gets the specified preview bitmap of a document and saves it as a Windows bitmap file (.bmp) using the
        specified filename."""
        # return self._instance.GetPreviewBitmapFile
        raise NotImplemented

    def get_process_i_d(self):
        """Gets the process ID for the current SOLIDWORKS session."""
        # return self._instance.GetProcessID
        raise NotImplemented

    def get_ray_trace_renderer(self):
        """Get a ray-trace rendering engine, such as PhotoView 360."""
        # return self._instance.GetRayTraceRenderer
        raise NotImplemented

    def get_recent_files(self):
        """Gets a list of the most recently used files."""
        # return self._instance.GetRecentFiles
        raise NotImplemented

    def get_routing_settings(self):
        """Gets routing settings."""
        # return self._instance.GetRoutingSettings
        raise NotImplemented

    def get_running_command_info(self):
        """Get a command's ID or PropertyManager page's command ID, title, and whether it is active in the
        user-interface."""
        # return self._instance.GetRunningCommandInfo
        raise NotImplemented

    def get_safe_array_utility(self):
        """Gets the ISafeArrayUtility object."""
        # return self._instance.GetSafeArrayUtility
        raise NotImplemented

    def get_save_to_d_experience_options(self):
        """Initializes save options for a SOLIDWORKS Connected document."""
        # return self._instance.GetSaveTo3DExperienceOptions
        raise NotImplemented

    def get_search_folders(self):
        """Gets the current folder search path as shown in Tools > Options > System Options > File Locations > Show
        folders for > Referenced Documents."""
        # return self._instance.GetSearchFolders
        raise NotImplemented

    def get_selection_filter(self):
        """Gets the current selection filter settings for the specified item type."""
        # return self._instance.GetSelectionFilter
        raise NotImplemented

    def get_selection_filters(self):
        """Gets all active selection filters."""
        # return self._instance.GetSelectionFilters
        raise NotImplemented

    def get_s_s_o_formatted_u_r_l(self):
        """Formats the specified URL for single sign-on."""
        # return self._instance.GetSSOFormattedURL
        raise NotImplemented

    def get_template_sizes(self):
        """Gets the sheet properties from a template document."""
        # return self._instance.GetTemplateSizes
        raise NotImplemented

    def get_toolbar_dock(self):
        """Gets the docking state of the toolbar."""
        # return self._instance.GetToolbarDock2
        raise NotImplemented

    def get_toolbar_state(self):
        """Gets the state of the toolbar."""
        # return self._instance.GetToolbarState2
        raise NotImplemented

    def get_toolbar_visibility(self):
        """Gets whether this toolbar is visible."""
        # return self._instance.GetToolbarVisibility
        raise NotImplemented

    def get_user_preference_double_value(self):
        """Gets system default user preference values."""
        # return self._instance.GetUserPreferenceDoubleValue
        raise NotImplemented

    def get_user_preference_integer_value(self):
        """Gets system default user preference values."""
        # return self._instance.GetUserPreferenceIntegerValue
        raise NotImplemented

    def get_user_preference_string_list_value(self):
        """Gets the name of the DXF mapping file."""
        # return self._instance.GetUserPreferenceStringListValue
        raise NotImplemented

    def get_user_preference_string_value(self):
        """Gets system default user preference values."""
        # return self._instance.GetUserPreferenceStringValue
        raise NotImplemented

    def get_user_preference_toggle(self):
        """Gets document default user preference values."""
        # return self._instance.GetUserPreferenceToggle
        raise NotImplemented

    def get_user_progress_bar(self):
        """Gets a progress indicator."""
        # return self._instance.GetUserProgressBar
        raise NotImplemented

    def get_user_type_lib_reference_count(self):
        """Gets the number of user-specified type library references."""
        # return self._instance.GetUserTypeLibReferenceCount
        raise NotImplemented

    def get_user_unit(self):
        """Gets an empty IUserUnit object of the specified type."""
        # return self._instance.GetUserUnit
        raise NotImplemented

    def hide_bubble_tooltip(self):
        """Hides the bubble ToolTip displayed by ISldWorks::ShowBubbleTooltipAt2."""
        # return self._instance.HideBubbleTooltip
        raise NotImplemented

    def hide_toolbar(self):
        """Hides a toolbar created with ISldWorks::AddToolbar5."""
        # return self._instance.HideToolbar2
        raise NotImplemented

    def load_add_in(self):
        """Loads the specified add-in in SOLIDWORKS."""
        # return self._instance.LoadAddIn
        raise NotImplemented

    def load_file(self):
        """Loads a third-party native CAD file into a new SOLIDWORKS document using 3D Interconnect."""
        # return self._instance.LoadFile4
        raise NotImplemented

    def move_document(self):
        """Moves a document and optionally updates references to it."""
        # return self._instance.MoveDocument
        raise NotImplemented

    def new_document(self):
        """Creates a new document based on the specified template."""
        # return self._instance.NewDocument
        raise NotImplemented

    def open_doc(self, file_name, options=1, configuration=''):
        """Opens an existing document and returns a pointer to the document object."""
        extension = os.path.splitext(file_name)[1]
        if extension == ".SLDPRT":
            doc_type = 1
        elif extension == ".SLDASM":
            doc_type = 2
        elif extension == ".SLDDRW":
            doc_type = 3
        else:
            raise ValueError("Incompatible File Type")

        arg1 = win32.VARIANT(pythoncom.VT_BSTR, file_name.replace("\\", "/"))
        arg2 = win32.VARIANT(pythoncom.VT_I4, doc_type)
        arg3 = win32.VARIANT(pythoncom.VT_I4, options)
        arg4 = win32.VARIANT(pythoncom.VT_BSTR, configuration)
        arg5 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        arg6 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        pointer = self._instance.OpenDoc6(arg1, arg2, arg3, arg4, arg5, arg6)
        return Doc(pointer), arg5.value, arg6.value

    def paste_appearance(self):
        """Applies to the specified entity an appearance that has been copied to the clipboard."""
        # return self._instance.PasteAppearance
        raise NotImplemented

    def post_message_to_application(self):
        """Posts a message to the application that invoked this method."""
        # return self._instance.PostMessageToApplication
        raise NotImplemented

    def post_message_to_applicationx(self):
        """Posts a message to the application that invoked this method in 64-bit applications."""
        # return self._instance.PostMessageToApplicationx64
        raise NotImplemented

    def pre_select_dwg_template_size(self):
        """Establishes which template to use when creating a drawing."""
        # return self._instance.PreSelectDwgTemplateSize
        raise NotImplemented

    def preset_new_drawing_parameters(self):
        """Presets the drawing template and sheet size parameters to avoid showing the Sheet Format/Size dialog when
        creating a new drawing document in the user-interface."""
        # return self._instance.PresetNewDrawingParameters
        raise NotImplemented

    def preview_doc(self):
        """Displays a preview of a document to the specified window."""
        # return self._instance.PreviewDoc
        raise NotImplemented

    def preview_docx(self):
        """Displays a preview of a document to the specified window in 64-bit applications."""
        # return self._instance.PreviewDocx64
        raise NotImplemented

    def quit_doc(self, name):
        """Closes the specified document without saving changes."""
        return self._instance.QuitDoc(name)

    def record_line(self):
        """Adds a line of code to a VBA macro and the SOLIDWORKS journal file."""
        # return self._instance.RecordLine
        raise NotImplemented

    def record_line_c_sharp(self):
        """Adds a line of code to a C# macro and the SOLIDWORKS journal file."""
        # return self._instance.RecordLineCSharp
        raise NotImplemented

    def record_line_v_bnet(self):
        """Adds a line of code to a VB.NET macro and the SOLIDWORKS journal file."""
        # return self._instance.RecordLineVBnet
        raise NotImplemented

    def refresh_quick_tip_window(self):
        """Tells the SOLIDWORKS application that your add-in's state has changed and triggers a query for the current
        URL page."""
        # return self._instance.RefreshQuickTipWindow
        raise NotImplemented

    def refresh_taskpane_content(self):
        """Refreshes the view of the Design Library tab in the Task Pane."""
        # return self._instance.RefreshTaskpaneContent
        raise NotImplemented

    def register_third_party_popup_menu(self):
        """Registers a third-party pop-up (shortcut) menu."""
        # return self._instance.RegisterThirdPartyPopupMenu
        raise NotImplemented

    def register_tracking_definition(self):
        """Registers a tracking definition."""
        # return self._instance.RegisterTrackingDefinition
        raise NotImplemented

    def remove_callback(self):
        """Unregisters a general purpose callback handler."""
        # return self._instance.RemoveCallback
        raise NotImplemented

    def remove_file_open_item(self):
        """Removes a file type from the File > Open dialog box that was added using ISldWorks::AddFileOpenItem3."""
        # return self._instance.RemoveFileOpenItem2
        raise NotImplemented

    def remove_file_save_as_item(self):
        """Removes a file type from the File > Save As dialog box that was added using ISldWorks::AddFileSaveAsItem2."""
        # return self._instance.RemoveFileSaveAsItem2
        raise NotImplemented

    def remove_from_menu(self):
        """asdasd"""
        # return self._instance.RemoveFromMenu
        raise NotImplemented

    def remove_from_popup_menu(self):
        """Removes the specified menu item from one or all specified context-sensitive menus (also called shortcut
        menus and pop-up menus) for the specified document types."""
        # return self._instance.RemoveFromPopupMenu
        raise NotImplemented

    def remove_item_from_third_party_popup_menu(self):
        """Removes a menu item and icon from a third-party pop-up (shortcut) menu."""
        # return self._instance.RemoveItemFromThirdPartyPopupMenu
        raise NotImplemented

    def remove_menu(self):
        """Removes a menu item from the specified document frame."""
        # return self._instance.RemoveMenu
        raise NotImplemented

    def remove_menu_popup_item(self):
        """Removes an item on a pop-up (shortcut) menu."""
        # return self._instance.RemoveMenuPopupItem2
        raise NotImplemented

    def remove_toolbar(self):
        """Removes a toolbar created with ISldWorks::AddToolbar5."""
        # return self._instance.RemoveToolbar2
        raise NotImplemented

    def remove_user_type_lib_references(self):
        """Removes the user-specified type library references."""
        # return self._instance.RemoveUserTypeLibReferences
        raise NotImplemented

    def replace_referenced_document(self):
        """Replaces a referenced document."""
        # return self._instance.ReplaceReferencedDocument
        raise NotImplemented

    def reset_preset_drawing_parameters(self):
        """Resets SOLIDWORKS back to its default behavior after calling ISldWorks::PresetNewDrawingParameters
        (i.e., display Sheet Format/Size dialog when opening a new drawing document)."""
        # return self._instance.ResetPresetDrawingParameters
        raise NotImplemented

    def reset_untitled_count(self):
        """Resets the index of untitled documents."""
        # return self._instance.ResetUntitledCount
        raise NotImplemented

    def restore_settings(self):
        """Restores the specified SOLIDWORKS settings from the specified *.sldreg file."""
        # return self._instance.RestoreSettings
        raise NotImplemented

    def resume_skinning(self):
        """Resumes skinning windows."""
        # return self._instance.ResumeSkinning
        raise NotImplemented

    def revision_number(self):
        """Gets the version number of this SOLIDWORKS installation."""
        # return self._instance.RevisionNumber
        raise NotImplemented

    def run_attached_macro(self):
        """Runs the specified attached macro, module, and procedure."""
        # return self._instance.RunAttachedMacro
        raise NotImplemented

    def run_command(self):
        """Runs the specified SOLIDWORKS command."""
        # return self._instance.RunCommand
        raise NotImplemented

    def run_journal_cmd(self):
        """Do not use."""
        # return self._instance.RunJournalCmd
        raise NotImplemented

    def run_macro(self):
        """Runs a macro from a project file."""
        # return self._instance.RunMacro2
        raise NotImplemented

    def save_settings(self):
        """Saves the specified SOLIDWORKS settings to the specified *.sldreg file."""
        # return self._instance.SaveSettings
        raise NotImplemented

    def send_msg_to_user(self):
        """Displays a message box containing a message to the user, who is required to interact with it before
        continuing."""
        # return self._instance.SendMsgToUser2
        raise NotImplemented

    def set_addin_callback_info(self):
        """Sets add-in callback commands."""
        # return self._instance.SetAddinCallbackInfo2
        raise NotImplemented

    def set_apply_selection_filter(self):
        """Sets the current state of the selection filter."""
        # return self._instance.SetApplySelectionFilter
        raise NotImplemented

    def set_current_working_directory(self):
        """Sets the current working directory to be used by SOLIDWORKS."""
        # return self._instance.SetCurrentWorkingDirectory
        raise NotImplemented

    def set_missing_reference_path_name(self):
        """Sets the missing reference file name. Use with the SOLIDWORKS event ReferenceNotFoundNotify."""
        # return self._instance.SetMissingReferencePathName
        raise NotImplemented

    def set_mouse_drag_mode(self):
        """Sets the command-mouse mode."""
        # return self._instance.SetMouseDragMode
        raise NotImplemented

    def set_multiple_filenames_prompt(self):
        """Sets the new filenames to open in response to the ISldWorks PromptForMultipleFileNamesNotify event."""
        # return self._instance.SetMultipleFilenamesPrompt
        raise NotImplemented

    def set_new_filename(self):
        """Sets the name of the new SOLIDWORKS file."""
        # return self._instance.SetNewFilename
        raise NotImplemented

    def set_prompt_filename(self):
        """Sets the file to open in response to a SOLIDWORKS event."""
        # return self._instance.SetPromptFilename2
        raise NotImplemented

    def set_search_folders(self):
        """Sets the current folder search path as shown in Tools > Options > System Options > File Locations > Show
        folders for  > Referenced Documents."""
        # return self._instance.SetSearchFolders
        raise NotImplemented

    def set_selection_filter(self):
        """Sets the current selection filter values for the specified item type."""
        # return self._instance.SetSelectionFilter
        raise NotImplemented

    def set_selection_filters(self):
        """Sets the status for multiple selection filters."""
        # return self._instance.SetSelectionFilters
        raise NotImplemented

    def set_third_party_popup_menu_state(self):
        """Sets whether to show or hide a third-party popup (shortcut) menu."""
        # return self._instance.SetThirdPartyPopupMenuState
        raise NotImplemented

    def set_toolbar_dock(self):
        """Sets the docking state of the toolbar."""
        # return self._instance.SetToolbarDock2
        raise NotImplemented

    def set_toolbar_visibility(self):
        """Sets whether the specified toolbar is visible."""
        # return self._instance.SetToolbarVisibility
        raise NotImplemented

    def set_user_preference_double_value(self):
        """Sets system default user preference values."""
        # return self._instance.SetUserPreferenceDoubleValue
        raise NotImplemented

    def set_user_preference_integer_value(self):
        """Sets system default user preference values."""
        # return self._instance.SetUserPreferenceIntegerValue
        raise NotImplemented

    def set_user_preference_string_list_value(self):
        """Sets the name of the DXF mapping files."""
        # return self._instance.SetUserPreferenceStringListValue
        raise NotImplemented

    def set_user_preference_string_value(self):
        """Sets system default user preference values."""
        # return self._instance.SetUserPreferenceStringValue
        raise NotImplemented

    def set_user_preference_toggle(self):
        """Sets system default user preference values."""
        # return self._instance.SetUserPreferenceToggle
        raise NotImplemented

    def show_bubble_tooltip(self):
        """Displays a bubble ToolTip and flashes the specified toolbar button."""
        # return self._instance.ShowBubbleTooltip
        raise NotImplemented

    def show_bubble_tooltip_at(self):
        """Displays a bubble ToolTip at the specified location."""
        # return self._instance.ShowBubbleTooltipAt2
        raise NotImplemented

    def show_help(self):
        """Displays the specified Help topic."""
        # return self._instance.ShowHelp
        raise NotImplemented

    def show_third_party_popup_menu(self):
        """Sets where to show a third-party pop-up (shortcut) menu."""
        # return self._instance.ShowThirdPartyPopupMenu
        raise NotImplemented

    def solid_works_explorer(self):
        """Starts SOLIDWORKS Explorer."""
        # return self._instance.SolidWorksExplorer
        raise NotImplemented

    def un_install_quick_tip_guide(self):
        """Uninstalls your add-in's Quick Tips"""
        # return self._instance.UnInstallQuickTipGuide
        raise NotImplemented

    def unload_add_in(self):
        """Unloads the specified add-in from SOLIDWORKS."""
        # return self._instance.UnloadAddIn
        raise NotImplemented

    def upload_to_my_solid_works_settings(self):
        """Uploads the specified SOLIDWORKS Desktop settings to SOLIDWORKS Connected."""
        # return self._instance.UploadToMySolidWorksSettings
        raise NotImplemented

    def version_history(self):
        """Gets a list of strings indicating the versions in which a model was saved."""
        # return self._instance.VersionHistory
        raise NotImplemented
