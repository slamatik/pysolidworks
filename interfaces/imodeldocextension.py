from .icustompropertymanager import ICustomPropertyManager
import win32com.client as win32
import pythoncom
from com import Com


# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension.html

class IModelDocExtension:
    def __init__(self, parent):
        self._instance = parent.Extension

    @property
    def active_command_tab(self):
        """Gets and sets the active SOLIDWORKS CommandManager tab."""
        return self._instance.ActiveCommandTab

    @active_command_tab.setter
    def active_command_tab(self, value):
        """Gets and sets the active SOLIDWORKS CommandManager tab."""
        self._instance.ActiveCommandTab = value

    @property
    def active_command_tab_index(self):
        """Gets and sets the index of the active SOLIDWORKS CommandManager tab."""
        return self._instance.ActiveCommandTabIndex

    @active_command_tab_index.setter
    def active_command_tab_index(self, value):
        """Gets and sets the index of the active SOLIDWORKS CommandManager tab."""
        self._instance.ActiveCommandTabIndex = value

    def annotation_view_count(self):
        """Gets the number of annotation views in this part or assembly document."""
        # return self._instance.AnnotationViewCount
        raise NotImplemented

    def annotation_views(self):
        """Gets the annotation views in this part or assembly document."""
        # return self._instance.AnnotationViews
        raise NotImplemented

    def app_page_setup(self):
        """Gets the SOLIDWORKS application page setup interface for this document."""
        # return self._instance.AppPageSetup
        raise NotImplemented

    @property
    def command_tab_visible(self):
        """Gets and sets the visibility of the specified SOLIDWORKS CommandManager tab."""
        return self._instance.CommandTabVisible

    @command_tab_visible.setter
    def command_tab_visible(self, value):
        """Gets and sets the visibility of the specified SOLIDWORKS CommandManager tab."""
        self._instance.CommandTabVisible = value

    @property
    def custom_property_builder_template(self):
        """Gets or sets the custom property builder template for this part."""
        return self._instance.CustomPropertyBuilderTemplate

    @custom_property_builder_template.setter
    def custom_property_builder_template(self, value):
        """Gets or sets the custom property builder template for this part."""
        self._instance.CustomPropertyBuilderTemplate = value

    def custom_property_manager(self, config_name=''):
        """
        Gets the custom properties for this document or configuration.
        :param config_name: Name of configuration
        """
        return ICustomPropertyManager(self._instance.CustomPropertyManager(config_name))

    def dim_xpert_manager(self, configuration, create_schema):
        """
        Gets the DimXpert schema for this configuration.
        :param configuration: Name of the configuration for which to retrieve the DimXpert schema
        :param create_schema: True to create DimXpert schema if it does not already exist; false otherwise
        """
        # return self._instance.DimXpertManager(configuration, create_schema)
        raise NotImplemented

    @property
    def display_mode(self):
        """Gets and sets the display modes for the specified display state setting."""
        return self._instance.DisplayMode

    @display_mode.setter
    def display_mode(self, value):
        """Gets and sets the display modes for the specified display state setting."""
        self._instance.DisplayMode = value

    @property
    def display_state_spec_material_property_values(self):
        """Gets and sets the appearance settings for the specified display state setting."""
        return self._instance.DisplayStateSpecMaterialPropertyValues

    @display_state_spec_material_property_values.setter
    def display_state_spec_material_property_values(self, value):
        """Gets and sets the appearance settings for the specified display state setting."""
        self._instance.DisplayStateSpecMaterialPropertyValues = value

    @property
    def display_title(self):
        """Gets and sets this model's title to display in the FeatureManager design tree."""
        return self._instance.DisplayTitle

    @display_title.setter
    def display_title(self, value):
        """Gets and sets this model's title to display in the FeatureManager design tree."""
        self._instance.DisplayTitle = value

    def document(self):
        """Gets the model document."""
        # return self._instance.Document
        raise NotImplemented

    @property
    def feature_manager_filter_string(self):
        """Gets or sets the string in the FeatureManager design tree filter."""
        return self._instance.FeatureManagerFilterString

    @feature_manager_filter_string.setter
    def feature_manager_filter_string(self, value):
        """Gets or sets the string in the FeatureManager design tree filter."""
        self._instance.FeatureManagerFilterString = value

    @property
    def flyout_feature_tree_visibility(self):
        """Gets or sets the state of the flyout FeatureManager design tree."""
        return self._instance.FlyoutFeatureTreeVisibility

    @flyout_feature_tree_visibility.setter
    def flyout_feature_tree_visibility(self, value):
        """Gets or sets the state of the flyout FeatureManager design tree."""
        self._instance.FlyoutFeatureTreeVisibility = value

    @property
    def include_mass_properties_of_hidden_bodies(self):
        """Gets or sets whether to include the mass properties of hidden components in the assembly."""
        return self._instance.IncludeMassPropertiesOfHiddenBodies

    @include_mass_properties_of_hidden_bodies.setter
    def include_mass_properties_of_hidden_bodies(self, value):
        """Gets or sets whether to include the mass properties of hidden components in the assembly."""
        self._instance.IncludeMassPropertiesOfHiddenBodies = value

    @property
    def linked_display_state(self):
        """Gets or sets whether a display state is linked in this part."""
        return self._instance.LinkedDisplayState

    @linked_display_state.setter
    def linked_display_state(self, value):
        """Gets or sets whether a display state is linked in this part."""
        self._instance.LinkedDisplayState = value

    def needs_rebuild(self):
        """Gets whether the model document needs to be rebuilt."""
        # return self._instance.NeedsRebuild2
        raise NotImplemented

    @property
    def show_part_rebuild_indicators(self):
        """Gets or sets whether to display rebuild indicators on parts that have out-of-date frozen features."""
        return self._instance.ShowPartRebuildIndicators

    @show_part_rebuild_indicators.setter
    def show_part_rebuild_indicators(self, value):
        """Gets or sets whether to display rebuild indicators on parts that have out-of-date frozen features."""
        self._instance.ShowPartRebuildIndicators = value

    def sun_light_information(self, type):
        """
        Gets the specified sunlight information.
        :param type: Sunlight information as defined by swSunlightInfoType_e
        """
        # return self._instance.SunLightInformation(type)
        raise NotImplemented

    @property
    def toolbox_part_type(self):
        """Gets and sets whether this part is a SOLIDWORKS Toolbox part."""
        return self._instance.ToolboxPartType

    @toolbox_part_type.setter
    def toolbox_part_type(self, value):
        """Gets and sets whether this part is a SOLIDWORKS Toolbox part."""
        self._instance.ToolboxPartType = value

    @property
    def transparency(self):
        """Gets and sets the transparency states for the specified display state setting."""
        return self._instance.Transparency

    @transparency.setter
    def transparency(self, value):
        """Gets and sets the transparency states for the specified display state setting."""
        self._instance.Transparency = value

    @property
    def use_page_setup(self):
        """Gets or sets whether this document uses its own page setup values, SOLIDWORKS application page setup values,
        or setup values on individual drawing sheets."""
        return self._instance.UsePageSetup

    @use_page_setup.setter
    def use_page_setup(self, value):
        """Gets or sets whether this document uses its own page setup values, SOLIDWORKS application page setup values,
        or setup values on individual drawing sheets."""
        self._instance.UsePageSetup = value

    @property
    def view_display_real_view(self):
        """Gets or sets the RealView Graphics setting."""
        return self._instance.ViewDisplayRealView

    @view_display_real_view.setter
    def view_display_real_view(self, value):
        """Gets or sets the RealView Graphics setting."""
        self._instance.ViewDisplayRealView = value

    @property
    def visibility(self):
        """Gets and sets the visibility states for the specified display state setting."""
        return self._instance.Visibility

    @visibility.setter
    def visibility(self, value):
        """Gets and sets the visibility states for the specified display state setting."""
        self._instance.Visibility = value

    def add_angular_running_dim(self, display_as_chain, run_bidirectionally,
                                extension_line_extends_from_center_of_set, loc_x, loc_y, loc_z, retval):
        """
        Adds the specified angular running dimension for selected entities.
        :param display_as_chain: True to chain the angular dimensions together, false to not
        :param run_bidirectionally: True if each angular dimension runs in a direction closest to the baseline, false if
        all angular dimensions run in the same direction (see Remarks)
        :param extension_line_extends_from_center_of_set: True to extend the extension lines from the center of the set
        of angular running dimensions, false to not
        :param loc_x: X coordinate of baseline dimension (see Remarks)
        :param loc_y: Y coordinate of baseline dimension (see Remarks)
        :param loc_z: Z coordinate of baseline dimension (see Remarks)
        :param retval: Error as defined by swCreateAngRunDimError_e
        """
        # return self._instance.AddAngularRunningDim(display_as_chain, run_bidirectionally, extension_line_extends_from_center_of_set, loc_x, loc_y, loc_z, retval)
        raise NotImplemented

    def add_comment(self, text):
        """
        Adds a comment to this document's Comment Folder.
        :param text: Comment to add to the document's Comment folder
        """
        # return self._instance.AddComment(text)
        raise NotImplemented

    def add_decal(self, p_decal, decal_i_d):
        """
        Adds a decal to the model.
        :param p_decal: Decal
        :param decal_i_d: Decal ID
        """
        # return self._instance.AddDecal(p_decal, decal_i_d)
        raise NotImplemented

    def add_default_render_material(self, p_render_material, pw_material_id):
        """
        Not supported in SOLIDWORKS 2011 and later and not superseded.
        :param p_render_material: Appearance to add to the model
        :param pw_material_id: Appearance ID
        """
        # return self._instance.AddDefaultRenderMaterial(p_render_material, pw_material_id)
        raise NotImplemented

    def add_dimension(self, x, y, z, direction):
        """
        Creates a display dimension at the specified location for selected entities.
        :param x: X coordinate of display dimension text
        :param y: Y coordinate of display dimension text
        :param z: Z coordinate of display dimension text
        :param direction: Direction of dimensioning extension line or rapid dimensioning quadrant as defined in
        swSmartDimensionDirection_e (see Remarks)
        """
        # return self._instance.AddDimension(x, y, z, direction)
        raise NotImplemented

    def add_display_state_specific_render_material(self, p_render_material, display_state_option,
                                                   display_state_names, p_w_material_id1, p_w_material_id2):
        """
        Adds the specified appearance to the specified display states in the active configuration and returns the IDs
        assigned to that appearance.
        :param p_render_material: Appearance to add
        :param display_state_option: Display states as defined in swDisplayStateOpts_e
        :param display_state_names: Names of display states to which to add the appearance
        :param p_w_material_id1: First ID of appearance
        :param p_w_material_id2: Second ID of appearance
        """
        # return self._instance.AddDisplayStateSpecificRenderMaterial(p_render_material, display_state_option, display_state_names, p_w_material_id1, p_w_material_id2)
        raise NotImplemented

    def add_ordinate_dimension(self, dim_type, loc_x, loc_y, loc_z):
        """
        Inserts an ordinate dimension.
        :param dim_type: Dimension type as defined in swAddOrdinateDims_e
        :param loc_x: X location for the dimension
        :param loc_y: Y location for the dimension
        :param loc_z: Z location for the dimension
        """
        # return self._instance.AddOrdinateDimension(dim_type, loc_x, loc_y, loc_z)
        raise NotImplemented

    def add_or_update_search_data(self, app_name, app_keyword, app_value):
        """
        Adds or updates the SOLIDWORKS Search, third-party, application keyword and value to the model document.
        :param app_name: Third-party application name
        :param app_keyword: Third-party application keyword
        :param app_value: Value for AppKeyword
        """
        # return self._instance.AddOrUpdateSearchData(app_name, app_keyword, app_value)
        raise NotImplemented

    def add_path_length_dim(self, x, y, z):
        """
        Inserts a path length dimension at the specified coordinates for a selected path.
        :param x: X coordinate of display dimension
        :param y: Y coordinate of display dimension
        :param z: Z coordinate of display dimension
        """
        # return self._instance.AddPathLengthDim(x, y, z)
        raise NotImplemented

    def add_render_material(self, p_render_material, pw_material_id):
        """
        Not supported in SOLIDWORKS 2011 and later. Superseded by
        IModelDocExtension::AddDisplayStateSpecificRenderMaterial and
        IModelDocExtension::IAddDisplayStateSpecificRenderMaterial.
        :param p_render_material: Appearance to add to the model
        :param pw_material_id: Appearance ID
        """
        # return self._instance.AddRenderMaterial(p_render_material, pw_material_id)
        raise NotImplemented

    def add_specific_dimension(self, x, y, z, dimension_type, error):
        """
        Creates the specified display dimension at the specified location for selected entities.
        :param x: X coordinate of display dimension text
        :param y: Y coordinate of display dimension text
        :param z: Z coordinate of display dimension text
        :param dimension_type: Type of dimension to add as defined in swDimensionType_e (see Remarks)
        :param error: Result status as defined in swAddSpecificDimension_e
        """
        # return self._instance.AddSpecificDimension(x, y, z, dimension_type, error)
        raise NotImplemented

    def add_symmetric_dimension(self, x, y, z):
        """
        Creates a full symmetrical angular dimension at the specified location for the selected entities.
        :param x: X coordinate of the symmetrical angular dimension
        :param y: Y coordinate of the symmetrical angular dimension
        :param z: Z coordinate of the symmetrical angular dimension
        """
        # return self._instance.AddSymmetricDimension(x, y, z)
        raise NotImplemented

    def align_dimensions(self, align_type, space_value):
        """
        Aligns the selected dimensions in drawing documents.
        :param align_type: Type of alignment as defined by swAlignDimensionType_e
        :param space_value: Distance between dimensions
        """
        # return self._instance.AlignDimensions(align_type, space_value)
        raise NotImplemented

    def align_running_dimension(self):
        """Aligns the extension lines of all angular dimensions to be the same distance from the center as the baseline
        dimension (0⁰) in the set of angular running dimensions."""
        # return self._instance.AlignRunningDimension
        raise NotImplemented

    def apply_format_painter_to_all(self):
        """Applies Format Painter to all dimensions and annotations in the active document."""
        # return self._instance.ApplyFormatPainterToAll
        raise NotImplemented

    def break_all_external_file_references(self, insert_features):
        """
        Breaks all external references and allows you to insert the features of the original part, or parts, if the
        external references are broken.
        :param insert_features: True to insert the features of the original parts if the external references are broken,
        false to not
        """
        # return self._instance.BreakAllExternalFileReferences2(insert_features)
        raise NotImplemented

    def capture_d_view(self):
        """Captures the 3D View of this part or assembly."""
        # return self._instance.Capture3DView
        raise NotImplemented

    def change_sketch_plane(self, config_opt, config_names):
        """
        Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified
        configurations.
        :param config_opt: Configurations as defined by swInConfigurationOpts_e
        :param config_names: Array of configuration names
        """
        # return self._instance.ChangeSketchPlane(config_opt, config_names)
        raise NotImplemented

    def compare_d_p_m_i(self, reference_document, modified_document, report_name, report_folder_path,
                        report_save_options):
        """
        Compare DimXpert annotations, reference dimensions, and other annotations between different versions of the same
        part document.
        :param reference_document: Path and file name of the open part document
        :param modified_document: Path and file name of a different and open version of ReferenceDocument
        :param report_name: Name for the report and name of the folder to which to save the report and bitmap image
        files
        :param report_folder_path: Path to the folder specified in ReportName in which to save the report and bitmap
        image files
        :param report_save_options: Save options for the report as defined in sw3DPMISaveOptions_e
        """
        # return self._instance.Compare3DPMI(reference_document, modified_document, report_name, report_folder_path, report_save_options)
        raise NotImplemented

    def copy_drafting_standard(self, name):
        """
        Copy the current custom drafting standard.
        :param name: Name of current custom drafting standard
        """
        # return self._instance.CopyDraftingStandard(name)
        raise NotImplemented

    def create_d_bounding_box(self):
        """Creates a 3D bounding box for a cut list item in a weldment part."""
        # return self._instance.Create3DBoundingBox
        raise NotImplemented

    def create_advanced_hole_element_data(self, elm_type):
        """
        Creates an Advanced Hole element data object of the specified type.
        :param elm_type: Advanced Hole element type as defined in swAdvWzdGeneralHoleTypes_e
        """
        # return self._instance.CreateAdvancedHoleElementData(elm_type)
        raise NotImplemented

    def create_balloon_options(self):
        """Creates an object that stores BOM balloon options."""
        # return self._instance.CreateBalloonOptions
        raise NotImplemented

    def create_callout(self, number_of_rows, handler):
        """
        Creates a callout independent of a selection.
        :param number_of_rows: Number of rows in the callout
        :param handler: Pointer to the event handler for the callout (ISwCalloutHandler)
        """
        # return self._instance.CreateCallout(number_of_rows, handler)
        raise NotImplemented

    def create_decal(self):
        """Creates a decal for this model."""
        # return self._instance.CreateDecal
        raise NotImplemented

    def create_mass_property(self):
        """Creates a mass properties object."""
        # return self._instance.CreateMassProperty2
        raise NotImplemented

    def create_measure(self):
        """Creates a measure tool."""
        # return self._instance.CreateMeasure
        raise NotImplemented

    def create_o_l_e_object(self, aspect, position, buffer, error_code):
        """
        Creates an OLE object on the active document.
        :param aspect: Viewing aspect of the OLE object as defined in the DVASPECT enumeration (see Remarks)
        :param position: Top-left and bottom-right positions (see Remarks)
        :param buffer: Data for the OLE object (see Remarks)
        :param error_code: 0 if True or 1 if false
        """
        # return self._instance.CreateOLEObject(aspect, position, buffer, error_code)
        raise NotImplemented

    def create_render_material(self, path_name):
        """
        Creates an appearance for this model.
        :param path_name: Fully qualified or relative path and filename of the appearance to add to the model
        """
        # return self._instance.CreateRenderMaterial(path_name)
        raise NotImplemented

    def create_stacked_balloon_options(self):
        """Creates an object that stores options for stacked balloons."""
        # return self._instance.CreateStackedBalloonOptions
        raise NotImplemented

    def create_texture(self, mat_name, scale, angle, blend):
        """
        Creates a texture.
        :param mat_name: Name of the texture file
        :param scale: Value by which to adjust the granularity of the texture; value between 0.001 and 1000000.00
        :param angle: Value by which to adjust the rotation of the texture; value between 0.0 and 360.0
        :param blend: True to blend the part color with the texture color, false to not
        """
        # return self._instance.CreateTexture(mat_name, scale, angle, blend)
        raise NotImplemented

    def delete_all_decals(self):
        """Deletes all decals on this model."""
        # return self._instance.DeleteAllDecals
        raise NotImplemented

    def delete_attachment(self, file_name):
        """
        Deletes the specified file in the Attachments folder in the FeatureManager design tree.
        :param file_name: Name of the file to delete from the Attachments folder in the FeatureManager design tree
        """
        # return self._instance.DeleteAttachment(file_name)
        raise NotImplemented

    def delete_decal(self, decal_i_d, b_reassign_ids_and_invalidate):
        """
        Removes the specified decal from this model.
        :param decal_i_d: Decal ID
        :param b_reassign_ids_and_invalidate: True if the decal IDs are reassigned and this decal ID is invalidated, false if not
        """
        # return self._instance.DeleteDecal(decal_i_d, b_reassign_ids_and_invalidate)
        raise NotImplemented

    def delete_display_state_specific_render_material(self, p_w_material_id1, p_w_material_id2):
        """
        Deletes the specified appearances, using the IDs of the appearances, from the active configuration.
        :param p_w_material_id1:
Array of the first IDs of the appearances to delete
        :param p_w_material_id2: Array of the first IDs of the appearances to delete
        """
        # return self._instance.DeleteDisplayStateSpecificRenderMaterial(p_w_material_id1, p_w_material_id2)
        raise NotImplemented

    def delete_drafting_standard(self):
        """Delete the current custom drafting standard."""
        # return self._instance.DeleteDraftingStandard
        raise NotImplemented

    def delete_feature_mgr_viewx(self, app_view):
        """
        Removes the specified tab in the FeatureManager design tree in 64-bit applications.
        :param app_view: View handle of the FeatureManager design tree view to delete
        """
        # return self._instance.DeleteFeatureMgrViewx64(app_view)
        raise NotImplemented

    def delete_render_material(self, pw_material_id, b_reassign_ids_and_invalidate):
        """
        Not supported in SOLIDWORKS 2011 and later. Superseded by IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial and IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial.
        :param pw_material_id: Appearance ID
        :param b_reassign_ids_and_invalidate: True if the appearance IDs are reassigned and this appearance ID is invalidated, false if not
        """
        # return self._instance.DeleteRenderMaterial(pw_material_id, b_reassign_ids_and_invalidate)
        raise NotImplemented

    def delete_scene(self):
        """Deletes the scene applied to this model."""
        # return self._instance.DeleteScene
        raise NotImplemented

    def delete_search_data(self, app_name):
        """
        Deletes the specified SOLIDWORKS Search third-party keywords from the model document.
        :param app_name: Application name whose keywords to delete
        """
        # return self._instance.DeleteSearchData(app_name)
        raise NotImplemented

    def delete_selection(self, delete_options):
        """
        Deletes the selected items, with the option to delete absorbed features, child features, or both.
        :param delete_options: Options as defined in swDeleteSelectionOptions_e
        """
        # return self._instance.DeleteSelection2(delete_options)
        raise NotImplemented

    def edit_balloon_properties(self, style, size, upper_text_style, upper_text, lower_text_style, lower_text,
                                custom_size, show_quantity, quantity_placement, quantity_denotation_text,
                                quantity_distance):
        """
        Edits the selected balloon's properties.
        :param style: Style of balloon as defined in swBalloonStyle_e
        :param size: Balloon size as defined in swBalloonFit_e
        :param upper_text_style: Balloon text style as defined in swBalloonTextContent_e
        :param upper_text: Text for the balloon; valid only if UpperTextStyle is one of the following:

swBalloonTextContent_e.swBalloonTextCustom
swBalloonTextContent_e.swBalloonTextCustomProperties
swBalloonTextContent_e.swBalloonTextCutListProperties
        :param lower_text_style: Lower text style as defined in swBalloonTextContent_e; valid only if Style is swBalloonStyle_e.swBS_SplitCirc
        :param lower_text: Text for the lower text in the balloon; valid only if Style is swBalloonStyle_e.swBS_SplitCirc and LowerTextStyle is one of the following:

swBalloonTextContent_e.swBalloonTextCustom
swBalloonTextContent_e.swBalloonTextCustomProperties
swBalloonTextContent_e.swBalloonTextCutListProperties
        :param custom_size: User-defined size of the balloon; valid only if Size is swBalloonFit_e.swBF_UserDef
        :param show_quantity: True to show quantity, false to not
        :param quantity_placement: Placement of quantity value as defined in swBalloonQuantityPlacement_e; valid only if ShowQuantity is true 
        :param quantity_denotation_text: Denotation text for quantity; valid only if ShowQuantity is true
        :param quantity_distance: Distance between the balloon and the quantity; valid only if ShowQuantity is true
        """
        # return self._instance.EditBalloonProperties2(style, size, upper_text_style, upper_text, lower_text_style, lower_text, custom_size, show_quantity, quantity_placement, quantity_denotation_text, quantity_distance)
        raise NotImplemented

    def edit_dimension_properties(self, tol_type, tol_max, tol_min, tol_max_fit, tol_min_fit, use_doc_prec,
                                  precision, arrows_in, use_doc_arrows, arrow1, arrow2, prefix_text, suffix_text,
                                  show_value, callout_text1, callout_text2, dimension_lower_text, center_text,
                                  config_option, config_names):
        """
        Edits the selected dimension.
        :param tol_type: Type of tolerance as defined in swTolType_e
        :param tol_max: Maximum value for the tolerance
        :param tol_min: Minimum value for the tolerance
        :param tol_max_fit: Text for the maximum FIT value when using a fit tolerance type
        :param tol_min_fit: Text for the minimum FIT value when using a fit tolerance type
        :param use_doc_prec: True to use the document's precision value, false to use value specified for Precision
        :param precision: Precision to use for this dimension if UseDocPrec is false
        :param arrows_in: Arrow direction as defined in swDimensionArrowsSide_e
        :param use_doc_arrows: True to use the document's arrow types, false to use values specified for Arrow1 and Arrow2
        :param arrow1: Type of arrow to use for the first arrow of this dimension as defined in swArrowStyle_e if UseDocArrows is false
        :param arrow2: Type of arrow to use for the second arrow of this dimension as defined in swArrowStyle_e if UseDocArrows is false
        :param prefix_text: Text to display before the dimension, but on the same line (see Remarks)
        :param suffix_text: Text to display after the dimension, but on the same line (see Remarks)
        :param show_value: True to display the value of the dimension in the user interface, false to not
        :param callout_text1: Callout text to display above the dimension
        :param callout_text2: Callout text to display below the dimension
        :param dimension_lower_text: Text to display below the dimension line; valid for display dimensions in drawings only
        :param center_text: True to center the text in the dimension, false to not
        :param config_option: Configuration option as defined in swInConfigurationOpts_e
        :param config_names: Names of the configurations to which to apply these edits (see Remarks)
        """
        # return self._instance.EditDimensionProperties(tol_type, tol_max, tol_min, tol_max_fit, tol_min_fit, use_doc_prec, precision, arrows_in, use_doc_arrows, arrow1, arrow2, prefix_text, suffix_text, show_value, callout_text1, callout_text2, dimension_lower_text, center_text, config_option, config_names)
        raise NotImplemented

    def edit_rebuild_all(self):
        """Rebuilds only those features that need to be rebuilt in all configurations without activating each configuration."""
        # return self._instance.EditRebuildAll
        raise NotImplemented

    def find_tracked_objects(self, tracking_cookie, search_object, types_filter, tracking_i_ds):
        """
        Finds the tracking IDs assigned to entities in this document.
        :param tracking_cookie: Cookie obtained from ISldWorks::RegisterTrackingDefinition
        :param search_object: Body or face to search for tracking IDs; if empty, then all bodies in the document are searched
        :param types_filter: Array of the type of entities for which to search as defined by swTopoEntity_e; valid values are swTopoVertex, swTopoEdge, swTopoLoop, swTopoFace, and swTopoBody; if empty or set to 0, then all types are searched
        :param tracking_i_ds: Array of tracking IDs for which to search; if empty, then search for all tracking IDs
        """
        # return self._instance.FindTrackedObjects(tracking_cookie, search_object, types_filter, tracking_i_ds)
        raise NotImplemented

    def finish_recording_undo_object(self, undo_object_name, make_hidden):
        """
        Ends recording of a SOLIDWORKS Undo object with the specified name and visibility.
        :param undo_object_name: String that appears in the SOLIDWORKS Undo list
        :param make_hidden: True to hide this object in the Undo list and from the user; false to make this object visible in the Undo list and to the user
        """
        # return self._instance.FinishRecordingUndoObject2(undo_object_name, make_hidden)
        raise NotImplemented

    def force_rebuild_all(self):
        """Forces a rebuild of all features in all configurations without activating each configuration."""
        # return self._instance.ForceRebuildAll
        raise NotImplemented

    def geodesic_sketch_offset(self, offset, reverse, make_construct):
        """
        Creates a geodesic sketch offset along the curvature of a surface.
        :param offset: Offset distance
        :param reverse: True to reverse the offset direction, false to not
        :param make_construct: True to make sketch construction geometry after offsetting, false to not
        """
        # return self._instance.GeodesicSketchOffset(offset, reverse, make_construct)
        raise NotImplemented

    def get_d_experience_model_type(self):
        """Gets the type of 3DEXPERIENCE application that owns this model."""
        # return self._instance.Get3DExperienceModelType
        raise NotImplemented

    def get_d_view(self, name):
        """
        Gets the 3D View with the specified name for this part or assembly.
        :param name: Name of 3D View to get
        """
        # return self._instance.Get3DView(name)
        raise NotImplemented

    def get_d_view_count(self):
        """Gets the number of 3D Views in this part or assembly."""
        # return self._instance.Get3DViewCount
        raise NotImplemented

    def get_d_view_names(self):
        """Gets names of the 3D Views in this part or assembly."""
        # return self._instance.Get3DViewNames
        raise NotImplemented

    def get_d_views(self):
        """Gets the 3D Views for this part or assembly."""
        # return self._instance.Get3DViews
        raise NotImplemented

    def get_active_property_manager_page(self):
        """Gets the name of the active PropertyManager page."""
        # return self._instance.GetActivePropertyManagerPage
        raise NotImplemented

    def get_advanced_save_as_options(self, options):
        """
        Gets the advanced File > Save As options.
        :param options: Save with references options as defined in swSaveWithReferencesOptions (see Remarks)
        """
        # return self._instance.GetAdvancedSaveAsOptions(options)
        raise NotImplemented

    def get_advanced_spot_light_properties(self, name, exponent, attenuation_const, attenuation_linear,
                                           attenuation_quad):
        """
        Gets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model.
        :param name: SOLIDWORKS light source name
        :param exponent: Attenuation exponent
        :param attenuation_const: Constant attenuation factor
        :param attenuation_linear: Linear attenuation factor
        :param attenuation_quad: Quadratic attenuation factor
        """
        # return self._instance.GetAdvancedSpotLightProperties(name, exponent, attenuation_const, attenuation_linear, attenuation_quad)
        raise NotImplemented

    def get_annotation_count(self):
        """Gets the number of annotations on this part."""
        # return self._instance.GetAnnotationCount
        raise NotImplemented

    def get_annotations(self):
        """Gets the annotations on this part."""
        # return self._instance.GetAnnotations
        raise NotImplemented

    def get_appearance_setting(self):
        """Gets the appearance setting for this document."""
        # return self._instance.GetAppearanceSetting
        raise NotImplemented

    def get_attachment_count(self):
        """Gets the number of attachments for this document."""
        # return self._instance.GetAttachmentCount
        raise NotImplemented

    def get_attachments(self, linked_var):
        """
        Gets the attachments for this document.
        :param linked_var: Array of VARIANT_BOOL values indicating if a document is linked or not
        """
        # return self._instance.GetAttachments(linked_var)
        raise NotImplemented

    def get_callout_variable_string(self, variable):
        """
        Gets the string for the specified callout variable.
        :param variable: Callout variable as defined in swCalloutVariable_e
        """
        # return self._instance.GetCalloutVariableString(variable)
        raise NotImplemented

    def get_camera_by_id(self, camera_id):
        """
        Gets a camera using the specified camera ID.
        :param camera_id: Camera ID (see Remarks)
        """
        # return self._instance.GetCameraById(camera_id)
        raise NotImplemented

    def get_camera_count(self):
        """Gets the number of cameras in the document."""
        # return self._instance.GetCameraCount
        raise NotImplemented

    def get_camera_definition(self):
        """Gets a camera, but does not add the newly created camera to the model."""
        # return self._instance.GetCameraDefinition
        raise NotImplemented

    def get_command_tabs(self):
        """Gets all of the SOLIDWORKS CommandManager tab names in this document."""
        # return self._instance.GetCommandTabs
        raise NotImplemented

    def get_coordinate_system_transform_by_name(self, name_in):
        """
        Gets the transform of the specified coordinate system.
        :param name_in: Name of the coordinate system
        """
        # return self._instance.GetCoordinateSystemTransformByName(name_in)
        raise NotImplemented

    def get_corresponding(self, input_object):
        """
        Gets the object in the underlying part or subassembly document that corresponds to the specified input object in this drawing view or assembly.
        :param input_object: Object in this drawing view or assembly (see Remarks)
        """
        # return self._instance.GetCorresponding2(input_object)
        raise NotImplemented

    def get_corresponding_entity(self, entity):
        """
        Gets the entity in the underlying part or subassembly that corresponds to the specified entity in this assembly or drawing view.
        :param entity: Dispatch pointer to a vertex, face, or edge entity in this drawing view or assembly
        """
        # return self._instance.GetCorrespondingEntity2(entity)
        raise NotImplemented

    def get_costing_manager(self):
        """Gets the entry-point interface to the SOLIDWORKS Costing API and gets the CostingManager."""
        # return self._instance.GetCostingManager
        raise NotImplemented

    def get_decal(self, i_d, configuration):
        """
        Gets the specified decal in this model.
        :param i_d: Decal ID (see Remarks)
        :param configuration: Name of the configuration where to get the decal
        """
        # return self._instance.GetDecal(i_d, configuration)
        raise NotImplemented

    def get_decals(self):
        """Gets the decals applied to the model."""
        # return self._instance.GetDecals
        raise NotImplemented

    def get_decals_count(self):
        """Gets the number of decals applied to this model."""
        # return self._instance.GetDecalsCount
        raise NotImplemented

    def get_dependencies(self, traverseflag, searchflag, add_read_only_info, list_broken_refs,
                         append_imported_paths):
        """
        Gets all of this model's dependencies.
        :param traverseflag: True to traverse all dependency levels, false to get first level (see Remarks)
        :param searchflag: True to use the search rules to find dependencies, false to look where the documents were last saved (see Remarks)
        :param add_read_only_info: True to show read-only information in the returned strings, false to not (see Remarks)
        :param list_broken_refs: True to get broken references, false to not
        :param append_imported_paths: True to append imported path names, false to not (see Remarks)
        """
        # return self._instance.GetDependencies(traverseflag, searchflag, add_read_only_info, list_broken_refs, append_imported_paths)
        raise NotImplemented

    def get_display_state_setting(self, option):
        """
        Gets the display state setting for the specified scope.
        :param option: Scope of the display state setting as defined in swDisplayStateOpts_e
        """
        # return self._instance.GetDisplayStateSetting(option)
        raise NotImplemented

    def get_drafting_standard_names(self):
        """Get the names of all currently available drafting standards."""
        # return self._instance.GetDraftingStandardNames
        raise NotImplemented

    def get_flatten_sheet_metal_persist_reference(self, disp_obj):
        """
        Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part.
        :param disp_obj: Entity (a face, edge, or vertex) in the flattened sheet metal part whose persistent reference IDs you want
        """
        # return self._instance.GetFlattenSheetMetalPersistReference(disp_obj)
        raise NotImplemented

    def get_general_table_annotation(self, use_anchor_point, x, y, anchor_type, table_template, rows, columns):
        """
        Creates a general table annotation for SOLIDWORKS MBD 3D PDF.
        :param use_anchor_point: True to anchor the table by AnchorType and ignore any coordinates specified by X and Y, false to use the coordinates specified by X and Y
        :param x: X coordinate of this table annotation; valid only if UseAnchorPoint is false
        :param y: Y coordinate of this table annotation; valid only if UseAnchorPoint is false
        :param anchor_type: Type of anchor as defined in swBOMConfigurationAnchorType_e; valid only if UseAnchorPoint is true, and TableTemplate is empty (see Remarks)
        :param table_template: Path and file name of the general table template to use (see Remarks)
        :param rows: Number of rows in the table annotation; valid only if TableTemplate is empty (see Remarks)
        :param columns: Number of columns in the table annotation; valid only if TableTemplate is empty (see Remarks)
        """
        # return self._instance.GetGeneralTableAnnotation(use_anchor_point, x, y, anchor_type, table_template, rows, columns)
        raise NotImplemented

    def get_keep_light_in_render_scene(self, i_d):
        """
        Gets whether a light is kept when the scene changes.
        :param i_d: Light ID
        """
        # return self._instance.GetKeepLightInRenderScene(i_d)
        raise NotImplemented

    def get_last_feature_added(self):
        """Gets the last feature added to the model."""
        # return self._instance.GetLastFeatureAdded
        raise NotImplemented

    def get_license_type(self):
        """Gets the type of SOLIDWORKS license used when the model was created."""
        # return self._instance.GetLicenseType
        raise NotImplemented

    def get_light_enabled_in_render(self, i_d):
        """
        Gets whether a light is on in this model.
        :param i_d: Light ID
        """
        # return self._instance.GetLightEnabledInRender(i_d)
        raise NotImplemented

    def get_material(self, i_d, configuration):
        """
        Gets the appearance for the specified appearance ID in the specified configuration in this model document
        :param i_d: Appearance Id
        :param configuration: Name of the configuration where the appearance is applied
        """
        # return self._instance.GetMaterial(i_d, configuration)
        raise NotImplemented

    def get_material_property_values(self, config_opt, config_names):
        """
        Gets the material properties for this model document.
        :param config_opt: Configuration options as defined by swInConfigurationOpts_e
        :param config_names: Array of configuration names for this component
        """
        # return self._instance.GetMaterialPropertyValues(config_opt, config_names)
        raise NotImplemented

    def get_m_b_d_d_pdf_data(self):
        """Gets the SOLIDWORKS MBD 3D PDF data object."""
        # return self._instance.GetMBD3DPdfData
        raise NotImplemented

    def get_model_break_view_names(self, views):
        """
        Gets the names and number of the Model Break Views in the current configuration of the active model.
        :param views: Names of Model Break Views
        """
        # return self._instance.GetModelBreakViewNames(views)
        raise NotImplemented

    def get_model_view_count(self):
        """Gets the number of model views in this document."""
        # return self._instance.GetModelViewCount
        raise NotImplemented

    def get_model_views(self):
        """Gets the model views in this document."""
        # return self._instance.GetModelViews
        raise NotImplemented

    def get_motion_study_manager(self):
        """Gets the SOLIDWORKS motion study's MotionManager."""
        # return self._instance.GetMotionStudyManager
        raise NotImplemented

    def get_named_view_rotation(self, name):
        """
        Gets the specified named view orientation matrix with respect to the Front view.
        :param name: Name of the named view
        """
        # return self._instance.GetNamedViewRotation(name)
        raise NotImplemented

    def get_object_by_persist_reference(self, persist_id, error_code):
        """
        Gets the object assigned to the specified persistent reference ID.
        :param persist_id: Object's persistent reference ID (see Remarks)
        :param error_code: Success or error code as defined by swPersistReferencedObjectStates_e (see Remarks)
        """
        # return self._instance.GetObjectByPersistReference3(persist_id, error_code)
        raise NotImplemented

    def get_object_id(self, annotation):
        """
        Gets the object ID for the specified annotation.
        :param annotation: Annotation
        """
        # return self._instance.GetObjectId(annotation)
        raise NotImplemented

    def get_o_l_e_object_count(self, options):
        """
        Gets the number of OLE objects.
        :param options: Options as defined in swOleObjectOptions_e
        """
        # return self._instance.GetOLEObjectCount(options)
        raise NotImplemented

    def get_o_l_e_objects(self, options):
        """
        Get the OLE objects.
        :param options: Options as defined in swOleObjectOptions_e
        """
        # return self._instance.GetOLEObjects(options)
        raise NotImplemented

    def get_pack_and_go(self):
        """Gets a Pack and Go object."""
        # return self._instance.GetPackAndGo
        raise NotImplemented

    def get_persist_reference(self, disp_obj):
        """
        Gets the persistent reference ID for the specified object in this model document.
        :param disp_obj: Object
        """
        # return self._instance.GetPersistReference3(disp_obj)
        raise NotImplemented

    def get_persist_reference_count(self, disp_obj):
        """
        Gets the size of the persistent reference ID assigned to the selected object in this model document.
        :param disp_obj: Selected object
        """
        # return self._instance.GetPersistReferenceCount3(disp_obj)
        raise NotImplemented

    def get_p_l_m_i_d(self):
        """Gets the ID of this SOLIDWORKS Connected document."""
        # return self._instance.GetPLMID
        raise NotImplemented

    def get_print_d_dialog(self):
        """Gets the IPrint3DDialog object."""
        # return self._instance.GetPrint3DDialog
        raise NotImplemented

    def get_print_specification(self):
        """Gets the IPrintSpecification object for this document."""
        # return self._instance.GetPrintSpecification
        raise NotImplemented

    def get_render_custom_references(self):
        """Get the custom render references for this model."""
        # return self._instance.GetRenderCustomReferences
        raise NotImplemented

    def get_render_materials(self, display_state_option, display_state_names):
        """
        Gets the appearances applied to this model document in the specified display states.
        :param display_state_option: Display states as defined in swDisplayStateOpts_e
        :param display_state_names: Array of display state names
        """
        # return self._instance.GetRenderMaterials2(display_state_option, display_state_names)
        raise NotImplemented

    def get_render_materials_count(self, display_state_option, display_state_names):
        """
        Gets the number of appearances applied to this model document in the specified display states.
        :param display_state_option: Display states as defined in swDisplayStateOpts_e
        :param display_state_names: Array of display state names
        """
        # return self._instance.GetRenderMaterialsCount2(display_state_option, display_state_names)
        raise NotImplemented

    def get_render_stock_references(self):
        """Gets the SOLIDWORKS-supplied (stock) render references for this model."""
        # return self._instance.GetRenderStockReferences
        raise NotImplemented

    def get_routing_component_manager(self):
        """Gets the routing component manager."""
        # return self._instance.GetRoutingComponentManager
        raise NotImplemented

    def get_scanto_d(self):
        """Gets the IScanTo3D object for this document."""
        # return self._instance.GetScanto3D
        raise NotImplemented

    def get_scene_bkg_d_i_bx(self):
        """Gets the background image as DIBSECTION in 64-bit applications."""
        # return self._instance.GetSceneBkgDIBx64
        raise NotImplemented

    def get_search_data(self, app_name, app_names, node_names, node_values):
        """
        Gets the SOLIDWORKS Search, third-party, application keywords from the model document.
        :param app_name: Third-party application name whose keywords to get
        :param app_names: Array of strings of the third-party application name
        :param node_names: Array of strings of the third-party application name's keywords
        :param node_values: Array of strings of the third-party application name's keyword values
        """
        # return self._instance.GetSearchData(app_name, app_names, node_names, node_values)
        raise NotImplemented

    def get_search_data_count(self, app_name):
        """
        Gets the number of SOLIDWORKS Search keywords for the specified third-party application previously added to this model document.
        :param app_name: Third-party application name
        """
        # return self._instance.GetSearchDataCount(app_name)
        raise NotImplemented

    def get_section_properties(self, sections):
        """
        Gets the section properties for the following types of selected items:


Planar model face in any document

Face on a section plane

Crosshatch section face in a section view in a drawing a sketch

Sketch
        :param sections: Array of sections
        """
        # return self._instance.GetSectionProperties2(sections)
        raise NotImplemented

    def get_sheet_metal_objects_by_persist_reference(self, persist_id, error_code):
        """
        Gets the objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part.
        :param persist_id: Persistent reference IDs returned by IModelDocExtension::GetFlattenSheetMetalPersistReference or IModelDocExtension::IGetFlattenSheetMetalPersistReference
        :param error_code: Error as defined by swPersistReferencedObjectStates_e
        """
        # return self._instance.GetSheetMetalObjectsByPersistReference(persist_id, error_code)
        raise NotImplemented

    def get_stream(self, stream_type, read_only):
        """
        Gets the handle for the specified stream.
        :param stream_type: 1 = material stream
        :param read_only: True if the stream is read-only, false if not
        """
        # return self._instance.GetStream(stream_type, read_only)
        raise NotImplemented

    def get_sun_light_advanced_property_values(self, haze, sun_diameter, ground_albedo, sky_gamma):
        """
        Gets the specified sunlight advanced properties.
        :param haze: 0.0 <= Haze setting < = 1.0
        :param sun_diameter: 0.01 < = sun diameter visible in the scene <= 21474836.47
        :param ground_albedo: RGB color reflected from the ground upwards
        :param sky_gamma: 0.1 <= visible sky Output Gamma <= 100.0
        """
        # return self._instance.GetSunLightAdvancedPropertyValues(haze, sun_diameter, ground_albedo, sky_gamma)
        raise NotImplemented

    def get_sun_light_source_property_values(self, north_direction, north_latitude, east_longitude, time_zone,
                                             date_time):
        """
        Gets the property values for a sunlight source.
        :param north_direction: IMathVector; north direction of the sunlight source
        :param north_latitude: North latitude of the sunlight source
        :param east_longitude: East longitude of the sunlight source
        :param time_zone: Standard time zone of the sunlight source
        :param date_time: Date and time stamp in the specified TimeZone
        """
        # return self._instance.GetSunLightSourcePropertyValues(north_direction, north_latitude, east_longitude, time_zone, date_time)
        raise NotImplemented

    def get_sustainability(self):
        """Gets the entry-point interface to the SOLIDWORKS Sustainability API."""
        # return self._instance.GetSustainability
        raise NotImplemented

    def get_template_sheet_metal(self):
        """Gets the sheet metal folder feature from this sheet metal model created in SOLIDWORKS 2013 or later."""
        # return self._instance.GetTemplateSheetMetal
        raise NotImplemented

    def get_texture(self, config_name):
        """
        Gets the texture applied to the specified configuration.
        :param config_name: Name of configuration or NULL if texture is not present
        """
        # return self._instance.GetTexture(config_name)
        raise NotImplemented

    def get_user_preference_double(self, user_pref, user_pref_option):
        """
        Gets document default user preference values. This method is intended for user preferences of type double.
        :param user_pref: User preference as defined in swUserPreferenceDoubleValue_e
        :param user_pref_option: User-preference option for customizing annotation and dimension drafting standards and as defined in swUserPreferenceOption_e; if not needed, then specify swDetailingNoOptionSpecified
        """
        # return self._instance.GetUserPreferenceDouble(user_pref, user_pref_option)
        raise NotImplemented

    def get_user_preference_double_value_range(self, user_pref, value, min_value, max_value):
        """
        Gets the current document default user preference value, and the minimum and maximum valid document user preference values.
        :param user_pref: User preference as defined in swUserPreferenceDoubleValue_e
        :param value: Current value of UserPref; if the return value >= 0, see Remarks
        :param min_value: Minimum value of UserPref; if the return value = 0, see Remarks
        :param max_value: Maximum value of UserPref; if the return value= 0, see Remarks
        """
        # return self._instance.GetUserPreferenceDoubleValueRange(user_pref, value, min_value, max_value)
        raise NotImplemented

    def get_user_preference_integer(self, user_pref, user_pref_option):
        """
        Sets document default user preference values. This method is intended for user preferences of type integer.
        :param user_pref: User preference as defined in swUserPreferenceIntegerValue_e
        :param user_pref_option: User-preference option for customizing annotation and dimension drafting standards and as defined in swUserPreferenceOption_e; if not needed, then specify swDetailingNoOptionSpecified
        """
        # return self._instance.GetUserPreferenceInteger(user_pref, user_pref_option)
        raise NotImplemented

    def get_user_preference_string(self, user_pref, user_pref_option):
        """
        Gets document default user preference values. This method is intended for user preferences of type string.
        :param user_pref: User preference as defined in swUserPreferenceStringValue_e
        :param user_pref_option: User preference as defined in swUserPreferenceStringValue_e
        """
        # return self._instance.GetUserPreferenceString(user_pref, user_pref_option)
        raise NotImplemented

    def get_user_preference_text_format(self, user_pref, user_pref_option):
        """
        Gets document default user preference values. This method is intended for getting detailing text formats.
        :param user_pref: User preference as defined in swUserPreferenceTextFormat_e
        :param user_pref_option: User-preference option for customizing annotation and dimension drafting standards and as defined in swUserPreferenceOption_e; if not needed, then specify swDetailingNoOptionSpecified
        """
        # return self._instance.GetUserPreferenceTextFormat(user_pref, user_pref_option)
        raise NotImplemented

    def get_user_preference_toggle(self, user_pref, user_pref_option):
        """
        Gets document default user preference values. This method is intended for user preferences that can be toggled.
        :param user_pref: User preference as defined in swUserPreferenceToggle_e
        :param user_pref_option: User-preference option for customizing annotation and dimension drafting standards and as defined in swUserPreferenceOption_e; if not needed, then specify swDetailingNoOptionSpecified
        """
        # return self._instance.GetUserPreferenceToggle(user_pref, user_pref_option)
        raise NotImplemented

    def get_visible_box(self, upper_left, lower_right):
        """
        Gets the visible bounding box set by IModelDocExtension::SetVisibleBox for a part or an assembly.
        :param upper_left: Upper-left point of the bounding box
        :param lower_right: Lower-right point of the bounding box
        """
        # return self._instance.GetVisibleBox(upper_left, lower_right)
        raise NotImplemented

    def get_whats_wrong(self, features, error_codes, warnings):
        """
        Gets the What's Wrong dialog information for this model document.
        :param features: Array of features in the What's Wrong dialog
        :param error_codes: Array of error codes corresponding to the features in the What's Wrong dialog as defined in swFeatureError_e
        :param warnings: Array of Booleans corresponding to the features in the What's Wrong dialog indicating whether SOLIDWORKS detected a What's Wrong item as a warning; true if SOLIDWORKS detected a What's Wrong item as a warning, false if not
        """
        # return self._instance.GetWhatsWrong(features, error_codes, warnings)
        raise NotImplemented

    def get_whats_wrong_count(self):
        """Gets the number of items in the What's Wrong dialog."""
        # return self._instance.GetWhatsWrongCount
        raise NotImplemented

    def has_design_table(self):
        """Gets whether a document has a design table."""
        # return self._instance.HasDesignTable
        raise NotImplemented

    def has_material_property_values(self):
        """Gets whether this model has an appearance."""
        # return self._instance.HasMaterialPropertyValues
        raise NotImplemented

    def has_renamed_documents(self):
        """Gets whether the document has renamed files."""
        # return self._instance.HasRenamedDocuments
        raise NotImplemented

    def hide_decal(self, decal_i_d, hide):
        """
        Hides or shows the specified decal applied to this model.
        :param decal_i_d: Decal ID
        :param hide: True to hide the decal, false to show it
        """
        # return self._instance.HideDecal(decal_i_d, hide)
        raise NotImplemented

    def hide_feature_manager(self, hide):
        """
        Hides or shows the Manager Pane.
        :param hide: True to hide the Manager Pane, false to not
        """
        # return self._instance.HideFeatureManager(hide)
        raise NotImplemented

    def i_add_display_state_specific_render_material(self, p_render_material, display_state_option,
                                                     display_state_count, display_state_names, p_w_material_id1,
                                                     p_w_material_id2):
        """
        Adds the specified material to the specified display states in the active configuration and returns the IDs assigned to that material.
        :param p_render_material: Material to add
        :param display_state_option: Display states as defined in swDisplayStateOpts_e
        :param display_state_count: Number of display states (see Remarks)
        :param display_state_names:
in-process, unmanaged C++: Pointer to an array of the names of the display states to which to add material
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method. 
        :param p_w_material_id1: First ID of material
        :param p_w_material_id2: Second ID of material
        """
        # return self._instance.IAddDisplayStateSpecificRenderMaterial(p_render_material, display_state_option, display_state_count, display_state_names, p_w_material_id1, p_w_material_id2)
        raise NotImplemented

    def i_change_sketch_plane(self, config_opt, config_count, config_names):
        """
        Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations.
        :param config_opt: Configurations as defined by swInConfigurationOpts_e
        :param config_count: Number of configurations
        :param config_names: Array of configuration names
        """
        # return self._instance.IChangeSketchPlane(config_opt, config_count, config_names)
        raise NotImplemented

    def i_create_o_l_e_object(self, aspect, position, byte_count, buffer, error_code):
        """
        Creates an OLE object on the active document.
        :param aspect: Viewing aspect of the OLE object as defined in the DVASPECT enumeration (see Remarks)
        :param position: Top-left and bottom-right positions (see Remarks)
        :param byte_count: Number of bytes
        :param buffer: Data for the OLE object (see Remarks)
        :param error_code: 0 if True or 1 if false
        """
        # return self._instance.ICreateOLEObject(aspect, position, byte_count, buffer, error_code)
        raise NotImplemented

    def i_delete_display_state_specific_render_material(self, id_count, p_w_material_id1, p_w_material_id2):
        """
        Deletes the specified materials, using the IDs of the materials, from the active configuration.
        :param id_count: Number of material IDs
        :param p_w_material_id1:

in-process, unmanaged C++: Pointer to an array of the first IDs of the material to delete

VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.PWMaterialId2


in-process, unmanaged C++: Pointer to an array of the second IDs of the material to delete

VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
        :param p_w_material_id2:

in-process, unmanaged C++: Pointer to an array of the first IDs of the material to delete

VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
        """
        # return self._instance.IDeleteDisplayStateSpecificRenderMaterial(id_count, p_w_material_id1, p_w_material_id2)
        raise NotImplemented

    def i_edit_dimension_properties(self, tol_type, tol_max, tol_min, tol_max_fit, tol_min_fit, use_doc_prec,
                                    precision, arrows_in, use_doc_arrows, arrow1, arrow2, prefix_text, suffix_text,
                                    show_value, callout_text1, callout_text2, dimension_lower_text, center_text,
                                    config_option, count, config_names):
        """
        Edits the selected dimension.
        :param tol_type: Type of tolerance as defined in swTolType_e
        :param tol_max: Maximum value for the tolerance
        :param tol_min: Minimum value for the tolerance
        :param tol_max_fit: Text for the maximum FIT value when using a fit tolerance type
        :param tol_min_fit: Text for the minimum FIT value when using a fit tolerance type
        :param use_doc_prec: True to use the document's precision value, false to use value specified for Precision
        :param precision: Precision to use for this dimension if UseDocPrec is false
        :param arrows_in: Arrow direction as defined in swDimensionArrowsSide_e
        :param use_doc_arrows: True to use the document's arrow types, false to use values specified for Arrow1 and Arrow2
        :param arrow1: Type of arrow to use for the first arrow of this dimension as defined in swArrowStyle_e if UseDocArrows is false
        :param arrow2: Type of arrow to use for the second arrow of this dimension as defined in swArrowStyle_e if UseDocArrows is false
        :param prefix_text: Text for the prefix of the dimension
        :param suffix_text: Text for the suffix of the dimension
        :param show_value: True to display the value of the dimension in the user interface, false to not
        :param callout_text1: Callout text to display above the dimension
        :param callout_text2: Callout text to display below the dimension
        :param dimension_lower_text: Text to display below the dimension line; valid for display dimensions in drawings only
        :param center_text: True to center the text in the dimension, false to not
        :param config_option: Configuration option as defined in swInConfigurationOpts_e
        :param count: Number of configurations
        :param config_names:
in-process, unmanaged C++: Pointer to an array of configuration names to which to apply these edits (see Remarks)
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
        """
        # return self._instance.IEditDimensionProperties(tol_type, tol_max, tol_min, tol_max_fit, tol_min_fit, use_doc_prec, precision, arrows_in, use_doc_arrows, arrow1, arrow2, prefix_text, suffix_text, show_value, callout_text1, callout_text2, dimension_lower_text, center_text, config_option, count, config_names)
        raise NotImplemented

    def i_getrd_party_storage_store(self, sub_storage_name, is_storing):
        """
        Gets the IStorage interface to the specified third-party storage in this SOLIDWORKS document.
        :param sub_storage_name: Name of the storage
        :param is_storing: True if you are storing data, false if not
        """
        # return self._instance.IGet3rdPartyStorageStore(sub_storage_name, is_storing)
        raise NotImplemented

    def i_get_annotations(self, num_annotations):
        """
        Gets the annotations on this model.
        :param num_annotations: Number of annotations
        """
        # return self._instance.IGetAnnotations(num_annotations)
        raise NotImplemented

    def i_get_annotation_views(self, annotation_view_count):
        """
        Gets the annotation views in this part or assembly document.
        :param annotation_view_count: Number of annotation views in this part or assembly document
        """
        # return self._instance.IGetAnnotationViews(annotation_view_count)
        raise NotImplemented

    def i_get_attachments(self, num_attachments, linked_arr):
        """
        Gets the attachments for this document.
        :param num_attachments: Number of attachments for this document
        :param linked_arr:

in-process, unmanaged C++: Pointer to an array of VARIANT_BOOL values indicating if a document is linked or not
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
        """
        # return self._instance.IGetAttachments(num_attachments, linked_arr)
        raise NotImplemented

    def i_get_decals(self, count):
        """
        Gets the decals applied to the model.
        :param count: Number of decals
        """
        # return self._instance.IGetDecals(count)
        raise NotImplemented

    def i_get_flatten_sheet_metal_persist_reference(self, disp_obj, count):
        """
        Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part.
        :param disp_obj: Entity (a face, edge, or vertex) in the flattened sheet metal part whose persistent reference IDs you want
        :param count: Number of persistent reference IDs
        """
        # return self._instance.IGetFlattenSheetMetalPersistReference(disp_obj, count)
        raise NotImplemented

    def i_get_material_property_values(self, config_opt, config_count, config_names):
        """
        Gets the material properties for this model.
        :param config_opt: Configuration options as defined by swInConfigurationOpts_e
        :param config_count: Number of configurations for this component
        :param config_names:
in-process, unmanaged C++: Pointer to an array of configuration names for this component
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method. 
        """
        # return self._instance.IGetMaterialPropertyValues(config_opt, config_count, config_names)
        raise NotImplemented

    def i_get_model_views(self, num_model_views):
        """
        Gets the model views in this document.
        :param num_model_views: Number of model views in this document
        """
        # return self._instance.IGetModelViews(num_model_views)
        raise NotImplemented

    def i_get_named_view_rotation(self, name):
        """
        Gets the specified named view orientation matrix with respect to the Front view.
        :param name: Name of the named view
        """
        # return self._instance.IGetNamedViewRotation(name)
        raise NotImplemented

    def i_get_object_by_persist_reference(self, count, persist_id, error_code):
        """
        Gets the object assigned to the specified persistent reference ID.
        :param count: Size of persistent reference ID (see Remarks)
        :param persist_id: Object's persistent reference ID (see Remarks)
        :param error_code: Success or error code as defined by swPersistReferencedObjectStates_e (see Remarks)
        """
        # return self._instance.IGetObjectByPersistReference3(count, persist_id, error_code)
        raise NotImplemented

    def i_get_o_l_e_objects(self, options, ole_object_count, lp_ole_objects):
        """
        Get the OLE objects.
        :param options: Options as defined in swOleObjectOptions_e
        :param ole_object_count: Number of OLE objects
        :param lp_ole_objects:
in-process, unmanaged C++: Pointer to an array of the OLE objects
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method. 
        """
        # return self._instance.IGetOLEObjects(options, ole_object_count, lp_ole_objects)
        raise NotImplemented

    def i_get_persist_reference(self, dips_obj, count):
        """
        Gets the persistent reference ID for the specified object in this model document.
        :param dips_obj: Object  
        :param count: Size of returned array assigned to that object (see Remarks)
        """
        # return self._instance.IGetPersistReference3(dips_obj, count)
        raise NotImplemented

    def i_get_search_data(self, app_name, count, app_names, node_names, node_values):
        """
        Gets the SOLIDWORKS Search, third-party, application keywords from the model document.
        :param app_name: Third-party application name whose keywords to get
        :param count: Number of third-party application keywords
        :param app_names:
in-process, unmanaged C++: Pointer to an array of the third-party application names
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method. 
        :param node_names:
in-process, unmanaged C++: Pointer to an array of the third-party application name's keywords
VBA, VB.NET, C#, and C++/CLI: Not supported 
        :param node_values:
in-process, unmanaged C++: Pointer to an array of the third-party application name's keyword values
VBA, VB.NET, C#, and C++/CLI: Not supported
        """
        # return self._instance.IGetSearchData(app_name, count, app_names, node_names, node_values)
        raise NotImplemented

    def i_get_section_properties(self, count, sections):
        """
        Gets the section properties for the following types of selected items:


Planar model face in any document

Face on a section plane

Crosshatch section face in a section view in a drawing a sketch

Sketch
        :param count: Number of sections
        :param sections: Array of sections
        """
        # return self._instance.IGetSectionProperties2(count, sections)
        raise NotImplemented

    def i_get_sheet_metal_objects_by_persist_reference(self, count, persist_id, error_code):
        """
        Gets the object, or objects, in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part.
        :param count: Number of persistent reference IDs
        :param persist_id: Persistent reference IDs returned by IModelDocExtension::GetFlattenSheetMetalPersistReference or IModelDocExtension::IGetFlattenSheetMetalPersistReference
        :param error_code: Error as defined by swPersistReferencedObjectStates_e
        """
        # return self._instance.IGetSheetMetalObjectsByPersistReference(count, persist_id, error_code)
        raise NotImplemented

    def i_list_external_file_references(self, num_refs, model_path_name, comp_path_name, feature, data_type, status,
                                        ref_entity, feat_comp, config_option, config_name):
        """
        Gets the names and statuses of the external file references on this part or assembly.
        :param num_refs: Number of external references
        :param model_path_name:

in-process, unmanaged C++: Pointer to an array of path names of documents of size NumRefs

VBA, VB.NET, C#, and C++/CLI: Not supported
        :param comp_path_name:

in-process, unmanaged C++: Pointer to an array of path names of referenced components of size NumRefs

VBA, VB.NET, C#, and C++/CLI: Not supported
        :param feature:

in-process, unmanaged C++: Pointer to an array of in-context items (sketches, features, and so on) of size NumRefs
VBA, VB.NET, C#, and C++/CLI: Not supported
        :param data_type:

in-process, unmanaged C++: Pointer to an array of the type data used to create the items (converted edge or face, converted or offset sketch entity, body, and so on) of size NumRefs
VBA, VB.NET, C#, and C++/CLI: Not supported
        :param status:

in-process, unmanaged C++: Array of statuses of the external references as defined in swExternalReferenceStatus_e
VBA, VB.NET, C#, and C++/CLI: Not supported
        :param ref_entity:

in-process, unmanaged C++: Pointer to an array of actual items being used and the names of the documents that contain the items of size NumRefs

VBA, VB.NET, C#, and C++/CLI: Not supported
        :param feat_comp:

in-process, unmanaged C++: Pointer to an array of the names of the components in which the affected features exist of size NumRefs; this information is only displayed when one or more RefEntity is in a different component in an assembly and does not apply to derived parts

VBA, VB.NET, C#, and C++/CLI: Not supported
        :param config_option: Configuration option as defined by swExternalFileReferencesConfig_e
        :param config_name: Name of the configuration when configOption is swExternalFileReferencesNamedConfig
        """
        # return self._instance.IListExternalFileReferences(num_refs, model_path_name, comp_path_name, feature, data_type, status, ref_entity, feat_comp, config_option, config_name)
        raise NotImplemented

    def insert_annotation_favorite(self, bstr_file_name, x, y, z):
        """
        Inserts annotations from the specified favorite file at the specified location.
        :param bstr_file_name: Path and filename of favorites file
        :param x: x coordinate where to insert the annotations
        :param y: y coordinate where to insert the annotations
        :param z: z coordinate where to insert the annotations
        """
        # return self._instance.InsertAnnotationFavorite(bstr_file_name, x, y, z)
        raise NotImplemented

    def insert_annotation_view(self, annotation_viewing_direction, direction_reference, flip_direction,
                               horizontal_direction_reference, angle_made_with_horizontal):
        """
        Inserts an annotation view in this part or assembly document.
        :param annotation_viewing_direction: Defined by either any swStandardViews_e enumerator or 0 for selection
        :param direction_reference: If 0 specified for AnnotationViewingDirection, then specifiy a face or plane to define the direction of the annotation view
        :param flip_direction: True to flip the annotation view in the opposite direction, false to not
        :param horizontal_direction_reference: An edge, sketch, or face
        :param angle_made_with_horizontal: Angle used to make the annotation view horizontal
        """
        # return self._instance.InsertAnnotationView(annotation_viewing_direction, direction_reference, flip_direction, horizontal_direction_reference, angle_made_with_horizontal)
        raise NotImplemented

    def insert_attachment(self, file_name, linked):
        """
        Inserts a file as an Attachment to this document.
        :param file_name: Path and filename of file to insert as an Attachment to this document
        :param linked: True to link the document to the file, false to not
        """
        # return self._instance.InsertAttachment(file_name, linked)
        raise NotImplemented

    def insert_b_o_m_balloon(self, balloon_options):
        """
        Inserts a BOM balloon for the selected item.
        :param balloon_options: IBalloonOptions
        """
        # return self._instance.InsertBOMBalloon2(balloon_options)
        raise NotImplemented

    def insert_bom_table(self, template_name, x, y, bom_type, configuration_name, hidden, indented_numbering_type,
                         detailed_cut_list):
        """
        Inserts a bill of materials (BOM) table in a part or assembly document.
        :param template_name: Path and name of BOM table template (see Remarks)
        :param x: X coordinate for the placement of the BOM table
        :param y: Y coordinate for the placement of the BOM table
        :param bom_type: Type of BOM table as defined by swBomType_e
        :param configuration_name: Name of the configuration for this BOM table (see Remarks)
        :param hidden: True to hide the BOM table, false to show it
        :param indented_numbering_type: Type of numbering as defined by swNumberingType_e; valid only if BomType = swBomType_e.swBomType_Indented
        :param detailed_cut_list: True to show the detailed cut list, false to not; valid only if BomType = swBomType_e.swBomType_Indented
        """
        # return self._instance.InsertBomTable3(template_name, x, y, bom_type, configuration_name, hidden, indented_numbering_type, detailed_cut_list)
        raise NotImplemented

    def insert_camera(self):
        """Inserts a camera in this document."""
        # return self._instance.InsertCamera
        raise NotImplemented

    def insert_chain_dimensions(self, entities):
        """
        Chains dimensions for the specified entities in this drawing or sketch.
        :param entities: Array of entities, e.g., edges, vertices, circles, and midpoints with which to chain dimensions (see Remarks)
        """
        # return self._instance.InsertChainDimensions(entities)
        raise NotImplemented

    def insert_datum_target_symbol(self, datum1, datum2, datum3, area_style, area_outside, value1, value2,
                                   value_str1, value_str2, arrows_smart, arrow_style, leader_line_style,
                                   leader_bent, show_area, show_symbol, moveable_datum_style):
        """
        Creates a datum target symbol.
        :param datum1: Datum reference string 1
        :param datum2: Datum reference string 2
        :param datum3: Datum reference string 3
        :param area_style:
0 = point
1 = circle
2 = rectangle
        :param area_outside: True to display the target area outside, false to not
        :param value1: Numeric datum target area diameter or width
        :param value2: Numeric datum target area height
        :param value_str1: Value for datum target area diameter or width
        :param value_str2: Value for datum target area height
        :param arrows_smart: True to use smart arrows, false to not
        :param arrow_style: Arrowhead style as defined by swArrowStyle_e
        :param leader_line_style: Leaderline style as defined by swLeaderStyle_e
        :param leader_bent: True to create a bent leader line, false to not
        :param show_area: True to show the target area, false to not
        :param show_symbol: True to display the target symbol, false to not
        :param moveable_datum_style: Moveable datum target symbol style as defined in swMoveableDatumStyle_e
        """
        # return self._instance.InsertDatumTargetSymbol3(datum1, datum2, datum3, area_style, area_outside, value1, value2, value_str1, value_str2, arrows_smart, arrow_style, leader_line_style, leader_bent, show_area, show_symbol, moveable_datum_style)
        raise NotImplemented

    def insert_delete_face(self, option):
        """
        Inserts a DeleteFace feature.
        :param option: Option as defined in swFaceDeleteOption_e
        """
        # return self._instance.InsertDeleteFace(option)
        raise NotImplemented

    def insert_general_table_annotation(self, use_anchor_point, x, y, anchor_type, table_template, rows, columns):
        """
        Inserts the a general table annotation in this model document.
        :param use_anchor_point: True to anchor the table by AnchorType and ignore any coordinates specified by X and Y, false to use the coordinates specified by X and Y
        :param x: X coordinate of this table annotation
        :param y: Y coordinate of this table annotation
        :param anchor_type: Type of anchor as defined in swBOMConfigurationAnchorType_e; valid only if UseAnchorPoint is true and TableTemplate is empty (see Remarks)
        :param table_template: Path and file name of the general table template to use (see Remarks)
        :param rows: Number of rows in the table annotation; valid only if TableTemplate is empty (see Remarks)
        :param columns: Number of columns in the table annotation; valid only if TableTemplate is empty (see Remarks)
        """
        # return self._instance.InsertGeneralTableAnnotation(use_anchor_point, x, y, anchor_type, table_template, rows, columns)
        raise NotImplemented

    def insert_general_tolerance_table_annotation(self, template_name, x, y):
        """
        Inserts a general tolerance table annotation in this model document.
        :param template_name: Path and file name of the table template to use (see Remarks)
        :param x: X coordinate of this table annotation
        :param y: Y coordinate of this table annotation
        """
        # return self._instance.InsertGeneralToleranceTableAnnotation(template_name, x, y)
        raise NotImplemented

    def insert_object_from_file(self, file_path, create_link, aspect, x_pos, y_pos, z_pos):
        """
        Inserts an OLE object from a file.
        :param file_path: Path and filename for the OLE object file
        :param create_link: True to create an external link to the OLE object file, false to embed the OLE object on the document
        :param aspect: Viewing aspect of the object as defined in the DVASPECT enumeration (see Remarks)
        :param x_pos: x coordinate for the OLE object
        :param y_pos: y coordinate for the OLE object
        :param z_pos: z coordinate for the OLE object
        """
        # return self._instance.InsertObjectFromFile(file_path, create_link, aspect, x_pos, y_pos, z_pos)
        raise NotImplemented

    def insert_scene(self, scene_definition_file):
        """
        Applies the specified scene to the model.
        :param scene_definition_file: Fully qualified path and filename for the scene
        """
        # return self._instance.InsertScene(scene_definition_file)
        raise NotImplemented

    def insert_stacked_balloon(self, balloon_options):
        """
        Inserts a stack of balloons for selected items.
        :param balloon_options: IStackedBalloonOptions
        """
        # return self._instance.InsertStackedBalloon2(balloon_options)
        raise NotImplemented

    def insert_surface_finish_symbol(self, sym_type, leader_type, loc_x, loc_y, loc_z, lay_symbol, arrow_type,
                                     mach_allowance, other_vals, prod_method, sample_len, max_roughness,
                                     min_roughness, roughness_spacing):
        """
        Creates a surface-finish symbol based on the last selection.
        :param sym_type: Type of symbol as defined in swSFSymType_e
        :param leader_type: Type of leader as defined in swLeaderStyle_e
        :param loc_x: x location for symbol
        :param loc_y: y location for symbol
        :param loc_z: z location for symbol
        :param lay_symbol: Type of lay direction as defined in swSFLaySym_e
        :param arrow_type: Type of arrow head as defined in swArrowStyle_e
        :param mach_allowance: Material removal allowance
        :param other_vals: Other roughness values
        :param prod_method: Production method and treatment
        :param sample_len: Sampling length
        :param max_roughness: Maximum roughness
        :param min_roughness: Minimum roughness
        :param roughness_spacing: Roughness spacing
        """
        # return self._instance.InsertSurfaceFinishSymbol3(sym_type, leader_type, loc_x, loc_y, loc_z, lay_symbol, arrow_type, mach_allowance, other_vals, prod_method, sample_len, max_roughness, min_roughness, roughness_spacing)
        raise NotImplemented

    def insert_title_block_table(self, template_name, x, y):
        """
        Inserts a title block table in a part or assembly document.
        :param template_name: Fully qualified path and name of the title block table template
        :param x: x coordinate for upper-left corner of title block table
        :param y: y coordinate for upper-left corner of title block table
        """
        # return self._instance.InsertTitleBlockTable(template_name, x, y)
        raise NotImplemented

    def install_model_colorizer(self, p_interface):
        """
        Installs your implemented interface of the ISwColorContour interface.
        :param p_interface: Pointer to your implemented interface
        """
        # return self._instance.InstallModelColorizer(p_interface)
        raise NotImplemented

    def i_releaserd_party_storage_store(self, sub_storage_name):
        """
        Releases the specified third-party storage in this document.
        :param sub_storage_name: Name of the third-party storage
        """
        # return self._instance.IRelease3rdPartyStorageStore(sub_storage_name)
        raise NotImplemented

    def i_remove_material_property(self, config_opt, config_count, config_names):
        """
        Removes material property values from this model.
        :param config_opt: Configuration options as defined by swInConfigurationOpts_e
        :param config_count: Number of configurations
        :param config_names: Array of configurations
        """
        # return self._instance.IRemoveMaterialProperty(config_opt, config_count, config_names)
        raise NotImplemented

    @property
    def is_abbreviated_view_active(self):
        """Gets or sets whether the abbreviated view is active."""
        return self._instance.IsAbbreviatedViewActive

    @is_abbreviated_view_active.setter
    def is_abbreviated_view_active(self, value):
        """Gets or sets whether the abbreviated view is active."""
        self._instance.IsAbbreviatedViewActive = value

    def is_converted(self):
        """Gets whether the active document was converted to the current release uponing opening but has not yet been saved."""
        # return self._instance.IsConverted
        raise NotImplemented

    def i_set_material_property_values(self, material_values, config_opt, config_count, config_names):
        """
        Sets the material property values for this model document.
        :param material_values: Array of doubles of size 9 of material property values (see Remarks)
        :param config_opt: Configuration option as defined in swInConfigurationOpts_e
        :param config_count: Number of configuration names
        :param config_names: Array of configuration names of size Config_count
        """
        # return self._instance.ISetMaterialPropertyValues(material_values, config_opt, config_count, config_names)
        raise NotImplemented

    def is_exploded(self, view_name):
        """
        Gets the name of the exploded view currently shown in the model.
        :param view_name: Name of the exploded view currently shown in the model or an empty string if the model is collapsed
        """
        # return self._instance.IsExploded(view_name)
        raise NotImplemented

    def is_future_version(self):
        """Gets whether this document is for a future version of SOLIDWORKS."""
        # return self._instance.IsFutureVersion
        raise NotImplemented

    def is_same_persistent_i_d(self, persistent_i_d1, persistent_i_d2):
        """
        Gets whether the two specified objects have the same persistent reference IDs.
        :param persistent_i_d1: Object
        :param persistent_i_d2: Object
        """
        # return self._instance.IsSamePersistentID(persistent_i_d1, persistent_i_d2)
        raise NotImplemented

    def is_virtual_component(self, path_chain, title_chain):
        """
        Gets the paths to parent assembly components, up to and including the first non-virtual parent, if the model is a virtual component.
        :param path_chain: Array of fully qualified paths to parent assembly components, up to and including the first non-virtual parent assembly component, if the model is a virtual component
        :param title_chain: Array of document titles; each document title corresponds to a fully qualified path in PathChain
        """
        # return self._instance.IsVirtualComponent3(path_chain, title_chain)
        raise NotImplemented

    @property
    def jog_dimension(self):
        """Gets or sets whether jog points are on or off on an interactively selected linear or ordinate dimension."""
        return self._instance.JogDimension

    @jog_dimension.setter
    def jog_dimension(self, value):
        """Gets or sets whether jog points are on or off on an interactively selected linear or ordinate dimension."""
        self._instance.JogDimension = value

    def list_external_file_references(self, model_path_name, component_path_name, feature, data_type, status,
                                      ref_entity, feat_com, config_options, config_names):
        """
        Gets the specified external file reference information for this part or assembly.
        :param model_path_name: Array of path names of externally referenced model documents
        :param component_path_name: Array of path names of externally referenced assembly components
        :param feature: Array of in-context items (e.g., FeatureManager design tree sketches, features, and so on) that externally reference ModelPathName and ComponentPathName elements
        :param data_type: Array of data types used to create RefEntity (e.g., arc, line, sketch plane, converted edge or face, converted or offset sketch entity, body, and so on)
        :param status: Array of statuses of the external references as defined by swExternalReferenceStatus_e
        :param ref_entity: Array of actual items being used (FeatureManager design tree entities in the Feature parameter's external references) including the names of the documents that contain the items
        :param feat_com: Array of names of the components in which the affected Features exist; valid only if one or more RefEntity is in a different component in an assembly; not valid for derived parts
        :param config_options: Array of configuration options as defined by swExternalFileReferencesConfig_e
        :param config_names: Array of configuration names and empty strings; configuration name when corresponding element of ConfigOptions array contains swExternalFileReferencesNamedConfig, empty string otherwise
        """
        # return self._instance.ListExternalFileReferences2(model_path_name, component_path_name, feature, data_type, status, ref_entity, feat_com, config_options, config_names)
        raise NotImplemented

    def list_external_file_references_count(self):
        """Gets the number of external references on this part or assembly."""
        # return self._instance.ListExternalFileReferencesCount
        raise NotImplemented

    def load_drafting_standard(self, file_name):
        """
        Loads a custom drafting standard from a file.
        :param file_name: Path and filename of the drafting standard to load
        """
        # return self._instance.LoadDraftingStandard(file_name)
        raise NotImplemented

    def move_decal(self, decal_i_d, move_up):
        """
        Moves the decal up or down in the list of decals applied to the model.
        :param decal_i_d: Decal ID
        :param move_up: True to move the decal up in the list of decals, false to move the decal down in the list of decals
        """
        # return self._instance.MoveDecal(decal_i_d, move_up)
        raise NotImplemented

    def move_or_copy(self, copy, num_copies, keep_relations, base_x, base_y, base_z, dest_x, dest_y, dest_z):
        """
        Moves and optionally copies the selected sketch entities or annotations.
        :param copy: True to copy the sketch entities or annotations, false to not
        :param num_copies: Number of copies
        :param keep_relations: True to keep sketch relations, false to not
        :param base_x: X coordinate of the base point from which to move the sketch entities or annotations
        :param base_y: Y coordinate of the base point from which to move the sketch entities or annotations
        :param base_z: Z coordinate of the base point from which to move the sketch entities or annotations
        :param dest_x: X coordinate of the destination point to which to move the sketch entities or annotations
        :param dest_y: Y coordinate of the destination point to which to move the sketch entities or annotations
        :param dest_z: Z coordinate of the destination point to which to move the sketch entities or annotations
        """
        # return self._instance.MoveOrCopy(copy, num_copies, keep_relations, base_x, base_y, base_z, dest_x, dest_y, dest_z)
        raise NotImplemented

    def multi_select(self, objects, append_flag, data):
        """
        Selects multiple objects and returns the number of objects selected in the model.
        :param objects: Array of selectable objects:


can be the same type of objects (e.g., an array of faces or an array of edges) or different types of objects (e.g., an array of entities of faces and edges )

if an object is not selected, then it is ignored
        :param append_flag: True to append the objects to the selection list, false to replace the current selection list with these objects
        :param data: ISelectData object, Nothing, or null
        """
        # return self._instance.MultiSelect2(objects, append_flag, data)
        raise NotImplemented

    def print_out(self, printer, print_file_name, print_specification):
        """
        Prints this document without displaying any dialogs or message boxes.
        :param printer: Name of the printer to which to print (see Remarks)
        :param print_file_name: Name of file to which to print (see Remarks)
        :param print_specification: IPrintSpecification (see Remarks)
        """
        # return self._instance.PrintOut4(printer, print_file_name, print_specification)
        raise NotImplemented

    def publish_s_t_e_p_file(self, path):
        """
        Exports the SOLIDWORKS MBD 3D part or assembly to a STEP 242 file.
        :param path: Full qualified path to which to export the SOLIDWORKS MBD 3D part or assembly; use .STP for the
        file name extension
        """
        # return self._instance.PublishSTEP242File(path)
        raise NotImplemented

    def publish_to_d_p_d_f(self, m_b_d_pdf_data):
        """
        Creates a 3D PDF for SOLIDWORKS MBD.
        :param m_b_d_pdf_data: SOLIDWORKS MBD 3D PDF data
        """
        # return self._instance.PublishTo3DPDF(m_b_d_pdf_data)
        raise NotImplemented

    def purge_display_state(self):
        """Purges identical display states so that only unique display states remain."""
        # return self._instance.PurgeDisplayState
        raise NotImplemented

    def ray_intersections(self, bodies_in, base_points_in, vectors_in, options, hit_radius, offset, high_precision):
        """
        Finds the intersections between the specified set of rays and the specified set of bodies.
        :param bodies_in: Array of bodies that are hit by the rays (see Remarks)
        :param base_points_in: Array of doubles containing the x,y,z base points of each ray
        :param vectors_in: Array of doubles containing the direction vectors of each ray
        :param options: Options as defined in swRayPtsOpts_e (see Remarks)
        :param hit_radius: Radius of hit cylinder; this is used mainly in grazing cases to establish a hit (see Remarks)
        :param offset: Length tolerance to use to establish whether a hit on a face represents the entry or exit of the ray from the body (see Remarks)
        :param high_precision: True to use maximum precision when evaluating intersections close to the ray boundary, false to use dynamic precision based on the ray radius (see Remarks)
        """
        # return self._instance.RayIntersections(bodies_in, base_points_in, vectors_in, options, hit_radius, offset, high_precision)
        raise NotImplemented

    def rebuild(self, options):
        """
        Rebuilds the model in assembly and drawing documents and returns the status of the rebuild.
        :param options: Type of rebuild as defined in swRebuildOptions_e
        """
        # return self._instance.Rebuild(options)
        raise NotImplemented

    def refresh_d_views(self):
        """Updates the 3D Views of this part or assembly."""
        # return self._instance.Refresh3DViews
        raise NotImplemented

    def re_jog_running_dimension(self):
        """Applies jogs where extension lines overlap dimension text in an angular running dimension."""
        # return self._instance.ReJogRunningDimension
        raise NotImplemented

    def release_stream(self, stream_type):
        """
        Releases a previously obtained stream.
        :param stream_type: 1 = material stream
        """
        # return self._instance.ReleaseStream(stream_type)
        raise NotImplemented

    def remove_material_property(self, config_opt, config_names):
        """
        Removes material property values from this model.
        :param config_opt: Configuration options as defined by swInConfigurationOpts_e
        :param config_names: Array of configurations
        """
        # return self._instance.RemoveMaterialProperty(config_opt, config_names)
        raise NotImplemented

    def remove_model_colorizer(self, p_interface):
        """
        Removes your installed implemented interface of the ISwColorContour interface.
        :param p_interface: Pointer to your installed implemented interface
        """
        # return self._instance.RemoveModelColorizer(p_interface)
        raise NotImplemented

    def remove_texture(self, config_name):
        """
        Removes the texture from the specified configuration.
        :param config_name: Name of the configuration
        """
        # return self._instance.RemoveTexture2(config_name)
        raise NotImplemented

    def remove_texture_by_display_state(self, display_state_name):
        """
        Removes the texture applied to this model in the specified display state.
        :param display_state_name: Name of display state
        """
        # return self._instance.RemoveTextureByDisplayState(display_state_name)
        raise NotImplemented

    def remove_visible_box(self):
        """Removes the visible bounding box set by IModelDocExtension::SetVisibleBox and resets the size of the bounding
        box to the size calculated by SOLIDWORKS for a part or an assembly."""
        # return self._instance.RemoveVisibleBox
        raise NotImplemented

    def rename_document(self, new_name):
        """
        Temporarily renames the selected component using the specified name.
        :param new_name: New name for the component
        """
        # return self._instance.RenameDocument(new_name)
        raise NotImplemented

    def rename_drafting_standard(self, name):
        """
        Rename the current custom drafting to the specifed name.
        :param name: New name for current custom drafting standard
        """
        # return self._instance.RenameDraftingStandard(name)
        raise NotImplemented

    def reorder_feature(self, feature_to_move, target_feature, move_location):
        """
        Moves the specified feature to another location in the FeatureManager design tree of this part or assembly.
        :param feature_to_move: Name of feature to move
        :param target_feature: Name of feature before or after which to move FeatureToMove; valid only if MoveLocation
        is swMoveLocation_e.swMoveAfter or Name of folder; valid only if MoveLocation is swMoveLocation_e.swMoveToFolder
        :param move_location: Move type as defined by swMoveLocation_e
        """
        # return self._instance.ReorderFeature(feature_to_move, target_feature, move_location)
        raise NotImplemented

    def reset_standard_views(self):
        """Returns all standard model views to their default settings."""
        # return self._instance.ResetStandardViews
        raise NotImplemented

    def reverse_decals_order(self, decal_i_d):
        """
        Reverses the order of the decals on the model.
        :param decal_i_d: Decal ID
        """
        # return self._instance.ReverseDecalsOrder(decal_i_d)
        raise NotImplemented

    def rotate_or_copy(self, copy, num_copies, keep_relations, base_x, base_y, base_z, dest_x, dest_y, dest_z,
                       angle):
        """
        Rotates and optionally copies the selected sketch entities or annotations.
        :param copy: True to copy sketch entities or annotations, false to not
        :param num_copies: Number of copies
        :param keep_relations: True to keep sketch relations, false to not
        :param base_x: X coordinate of the base point from which to rotate the sketch entities or annotations
        :param base_y: Y coordinate of the base point from which to rotate the sketch entities or annotations
        :param base_z: Z coordinate of the base point from which to rotate the sketch entities or annotations
        :param dest_x: X vector component of the axis of rotation parallel to the base point
        :param dest_y: Y vector component of the axis of rotation parallel to the base point
        :param dest_z: Z vector component of the axis of rotation parallel to the base point
        :param angle: Angle at which to rotate or move the sketch entities or annotations
        """
        # return self._instance.RotateOrCopy(copy, num_copies, keep_relations, base_x, base_y, base_z, dest_x, dest_y, dest_z, angle)
        raise NotImplemented

    def run_command(self, command_i_d, new_title):
        """
        Runs the specified SOLIDWORKS command.
        :param command_i_d: SOLIDWORKS command as defined in swCommands_e
        :param new_title: Your title for the SOLIDWORKS PropertyManager page, if invoked by this command
        """
        # return self._instance.RunCommand(command_i_d, new_title)
        raise NotImplemented

    def save_as(self, name, version=0, options=1, export_data=None):
        """
        Saves the active document to the specified name with advanced options.
        :param name: Full pathname of the document to save; the file extension indicates any conversion that should be
        performed
        :param version: Format in which to save this document
        :param options: Option indicating how to save the document
        :param export_data: IExportPdfData object for exporting drawing sheets to PDF
        :return: True if the save is successful, false if not
        """
        arg1 = win32.VARIANT(pythoncom.VT_BSTR, name)
        arg2 = win32.VARIANT(pythoncom.VT_I4, version)
        arg3 = win32.VARIANT(pythoncom.VT_I4, options)
        arg5 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        arg6 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        # self._instance.SaveAs(arg1, arg2, arg3, arg4, arg5, arg6)
        result = self._instance.SaveAs(arg1, arg2, arg3, Com(export_data), arg5, arg6)
        # print(arg5.value, arg6.value)
        return result

    def save_de_featured_file(self, file_name):
        """
        Removes all CAD data except the outer surface from a loaded part or assembly document and saves the outer
        surface as a part.
        :param file_name: Path and file name for the new, de-featured part
        """
        # return self._instance.SaveDeFeaturedFile(file_name)
        raise NotImplemented

    def save_drafting_standard(self, file_name):
        """
        Saves the current custom drafting standard to a file.
        :param file_name: Path and filename for the current custom drafting standard to save to a file
        """
        # return self._instance.SaveDraftingStandard(file_name)
        raise NotImplemented

    def save_pack_and_go(self, pack_and_go):
        """
        Saves the files designated for Pack and Go to either a folder or Zip file.
        :param pack_and_go: Pack and Go object
        """
        # return self._instance.SavePackAndGo(pack_and_go)
        raise NotImplemented

    def save_selection(self, status):
        """
        Creates a new selection set containing the selected entities.
        :param status: 1 if a selection set is created, 0 if not
        """
        # return self._instance.SaveSelection(status)
        raise NotImplemented

    def save_to_d_experience(self, options, errors, warnings):
        """
        Saves this document in SOLIDWORKS Connected using the specified save options.
        :param options: ISaveTo3DExperienceOptions
        :param errors: Error codes
        :param warnings: Warning codes
        """
        # return self._instance.SaveTo3DExperience(options, errors, warnings)
        raise NotImplemented

    def scale_or_copy(self, copy, num_copies, base_x, base_y, base_z, scale):
        """
        Scales and optionally copies the selected sketch items or annotations.
        :param copy: True to copy the sketch items or annotations, false to not
        :param num_copies: Number of copies
        :param base_x: X coordinate of the base point
        :param base_y: Y coordinate of the base point
        :param base_z: Z coordinate of the base point
        :param scale: Factor by which to scale the sketch entities or annotations
        """
        # return self._instance.ScaleOrCopy(copy, num_copies, base_x, base_y, base_z, scale)
        raise NotImplemented

    def select_all(self):
        """Selects all edges in a part, all components in an assembly, or all entities (by default, sketch entities,
        dimensions, and annotations) in a drawing."""
        # return self._instance.SelectAll
        raise NotImplemented

    def select_by_i_d(self, name, type, x, y, z, append, mark, callout, select_option):
        """
        Selects the specified entity.
        :param name: Name of object to select or an empty string
        :param type: Type of object (uppercase) as defined in swSelectType_e or an empty string
        :param x: X selection location or 0
        :param y: Y selection location or 0
        :param z: Z selection location or 0
        :param append:
        If...
        An, if entity is...
        Then...
        True
        Not already selected
        Entity is appended to the current selection list

        Already selected
        Entity is removed from the current selection list

        False
        Not already selected
        Current selection is cleared and then the entity is put on the list


        Already selected
        Current selection list remains the same
        :param mark: Value that you want to use as a mark; this value is used by other functions that require ordered
        selection (see Remarks)
        :param callout: Pointer to the associated callout
        :param select_option: Selection option as defined in swSelectOption_e (see Remarks)
        """
        # return self._instance.SelectByID2(name, type, x, y, z, append, mark, callout, select_option)
        raise NotImplemented

    def select_by_ray(self, world_x, world_y, world_z, ray_vec_x, ray_vec_y, ray_vec_z, ray_radius, type_wanted,
                      append, mark, option):
        """
        Selects the first entity of the specified type that is intersected by a ray that starts at the specified point
        and runs parallel to the specified direction vector within the specified radius.
        :param world_x: x coordinate of ray start point
        :param world_y: y coordinate of ray start point
        :param world_z: z coordinate of ray start point
        :param ray_vec_x: x coordinate of ray direction vector
        :param ray_vec_y: y coordinate of ray direction vector
        :param ray_vec_z: z coordinate of ray direction vector
        :param ray_radius: Radius
        :param type_wanted: Type of entities to select as defined in swSelectType_e
        :param append:


        If...
        And if entity is...
        Then...


        True
        Not already selected
        Entity is appended to the current selection list


        Already selected
        Entity is removed from the current selection list

        False
        Not already selected
        Current selection is cleared and then the entity is put on the list


        Already selected
        Current selection list remains the same
        :param mark: Value to use as a mark; this value is used by other functions that require ordered selection
        :param option: Selection option as defined in swSelectOption_e (see Remarks)
        """
        # return self._instance.SelectByRay(world_x, world_y, world_z, ray_vec_x, ray_vec_y, ray_vec_z, ray_radius, type_wanted, append, mark, option)
        raise NotImplemented

    def set_advanced_spot_light_properties(self, name, exponent, attenuation_const, attenuation_linear,
                                           attenuation_quad):
        """
        Sets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model.
        :param name: SOLIDWORKS light source name
        :param exponent: Attenuation exponent
        :param attenuation_const: Constant attenuation factor
        :param attenuation_linear: Linear attenuation factor
        :param attenuation_quad: Quadratic attenuation factor
        """
        # return self._instance.SetAdvancedSpotLightProperties(name, exponent, attenuation_const, attenuation_linear, attenuation_quad)
        raise NotImplemented

    def set_api_undo_object(self, p_handler, display_name):
        """
        Implements an undo object for an add-in application.
        :param p_handler: Undo object
        :param display_name: Name to display in the SOLIDWORKS undo list
        """
        # return self._instance.SetApiUndoObject(p_handler, display_name)
        raise NotImplemented

    def set_keep_light_in_render_scene(self, i_d, val):
        """
        Sets whether to keep a light when the scene changes.
        :param i_d: Light ID
        :param val: True to keep a light when the scene changes, false to not
        """
        # return self._instance.SetKeepLightInRenderScene(i_d, val)
        raise NotImplemented

    def set_light_enabled_in_render(self, i_d, val):
        """
        Sets whether a light is on in this model.
        :param i_d: Light ID
        :param val: True to enable the light, false to not
        """
        # return self._instance.SetLightEnabledInRender(i_d, val)
        raise NotImplemented

    def set_material_property_values(self, material_property_values, config_opt, config_names):
        """
        Sets the material property values for this model document.
        :param material_property_values: Array of material property values
        :param config_opt: Configuration option as defined in swInConfigurationOpts_e
        :param config_names: Array of configuration names
        """
        # return self._instance.SetMaterialPropertyValues(material_property_values, config_opt, config_names)
        raise NotImplemented

    def set_scene_bkg_d_i_bx(self, l_dib):
        """
        Sets the background image in 64-bit applications.
        :param l_dib: Background image as DIBSECTION
        """
        # return self._instance.SetSceneBkgDIBx64(l_dib)
        raise NotImplemented

    def set_sun_light_advanced_property_values(self, haze, sun_diameter, ground_albedo, sky_gamma):
        """
        Sets the specified sunlight advanced properties.
        :param haze: 0.0 <= Haze setting < = 1.0
        :param sun_diameter: 0.01 < = sun diameter visible in the scene <= 21474836.47
        :param ground_albedo: RGB color reflected from the ground upwards
        :param sky_gamma: 0.1 <= visible sky Output Gamma <= 100.0
        """
        # return self._instance.SetSunLightAdvancedPropertyValues(haze, sun_diameter, ground_albedo, sky_gamma)
        raise NotImplemented

    def set_sun_light_source_property_values(self, north_direction, north_latitude, east_longitude, time_zone,
                                             date_time):
        """
        Sets the property values for a sunlight source.
        :param north_direction: IMathVector; north direction of the sunlight source
        :param north_latitude: North latitude of the sunlight source
        :param east_longitude: East longitude of the sunlight source
        :param time_zone: Standard time zone of the sunlight source
        :param date_time: Date and time stamp in the specified TimeZone
        """
        # return self._instance.SetSunLightSourcePropertyValues(north_direction, north_latitude, east_longitude, time_zone, date_time)
        raise NotImplemented

    def set_texture(self, config_name, texture_in):
        """
        Applies texture to the specified configuration.
        :param config_name: Name of configuration
        :param texture_in: Texture
        """
        # return self._instance.SetTexture(config_name, texture_in)
        raise NotImplemented

    def set_texture_by_display_state(self, display_state_name, texture_in):
        """
        Sets the texture applied to this model in the specified display state.
        :param display_state_name: Name of display state
        :param texture_in: Texture
        """
        # return self._instance.SetTextureByDisplayState(display_state_name, texture_in)
        raise NotImplemented

    def set_top_level_transparency(self, in_value):
        """
        Sets the transparency of this part or top-level assembly.
        :param in_value: True to make this part or top-level assembly transparent, false to not
        """
        # return self._instance.SetTopLevelTransparency(in_value)
        raise NotImplemented

    def set_user_preference_double(self, user_pref, user_pref_option, value):
        """
        Sets document default user preference values. This method is intended for user preferences of type double.
        :param user_pref: User preference as defined in swUserPreferenceDoubleValue_e
        :param user_pref_option: User-preference option for customizing annotation and dimension drafting standards and
        as defined in swUserPreferenceOption_e; if not needed, then specify swDetailingNoOptionSpecified
        :param value: Value to assign to the user preference specified in UserPref
        """
        # return self._instance.SetUserPreferenceDouble(user_pref, user_pref_option, value)
        raise NotImplemented

    def set_user_preference_integer(self, user_pref, user_pref_option, value):
        """
        Sets document default user preference values. This method is intended for user preferences of type integer.
        :param user_pref: User preference as defined in swUserPreferenceIntegerValue_e
        :param user_pref_option: User-preference option for customizing annotation and dimension drafting standards and
        as defined in swUserPreferenceOption_e; if not needed, then specify swDetailingNoOptionSpecified
        :param value: Value to assign to the user preference specified in UserPref
        """
        # return self._instance.SetUserPreferenceInteger(user_pref, user_pref_option, value)
        raise NotImplemented

    def set_user_preference_string(self, user_pref, user_pref_option, value):
        """
        Sets document default user preference values. This method is intended for user preferences of type string.
        :param user_pref: User preference as defined in swUserPreferenceStringValue_e
        :param user_pref_option: User-preference option for customizing annotation and dimension drafting standards and
        as defined in swUserPreferenceOption_e; if not needed, then specify swDetailingNoOptionSpecified
        :param value: Value of the user preference specified in UserPreference
        """
        # return self._instance.SetUserPreferenceString(user_pref, user_pref_option, value)
        raise NotImplemented

    def set_user_preference_text_format(self, user_pref, user_pref_option, value):
        """
        Sets document default user preference values. This method is intended for setting detailing text formats.
        :param user_pref: User preference as defined by swUserPreferenceTextFormat_e
        :param user_pref_option: User-preference option for customizing annotation and dimension drafting standards and
        as defined in swUserPreferenceOption_e; if not needed, then specify swDetailingNoOptionSpecified
        :param value: Text format to which to assign the user preference specified in UserPref
        """
        # return self._instance.SetUserPreferenceTextFormat(user_pref, user_pref_option, value)
        raise NotImplemented

    def set_user_preference_toggle(self, user_pref, user_pref_option, value):
        """
        Sets document default user preference values. This method is intended for user preferences that can be toggled.
        :param user_pref: User preference as defined in swUserPreferenceToggle_e
        :param user_pref_option: User-preference option for customizing annotation and dimension drafting standards and
        as defined in swUserPreferenceOption_e; if not needed, then specify swDetailingNoOptionSpecified
        :param value: True to toggle UserPref on, false to toggle UserPref off
        """
        # return self._instance.SetUserPreferenceToggle(user_pref, user_pref_option, value)
        raise NotImplemented

    def set_visible_box(self, upper_left, lower_right):
        """
        Sets the visible bounding box for Zoom to Fit for a part or an assembly.
        :param upper_left: Upper-left point of the visible bounding box
        :param lower_right: Lower-right point of the visible bounding box
        """
        # return self._instance.SetVisibleBox(upper_left, lower_right)
        raise NotImplemented

    def show_model_break_view(self, show_view, view_name):
        """
        Gets whether to show or hide the specified Model Break View in the current configuration of the active model.
        :param show_view: True to show the Model Break View, false to hide it
        :param view_name: Name of Model Break View to show or hide
        """
        # return self._instance.ShowModelBreakView(show_view, view_name)
        raise NotImplemented

    def show_smart_message(self, name, time_in_mill_sec, show_in_status_bar, remove_default_tip):
        """
        Displays a SOLIDWORKS-style message as a ToolTip in the graphics area and on the status bar.
        :param name: Message to display in the ToolTip
        :param time_in_mill_sec: Time, in milliseconds, to display the message
        :param show_in_status_bar: True to show the message on the SOLIDWORKS status bar, false to not
        :param remove_default_tip: True to replace the default SOLIDWORKS ToolTip with this message for TimeInMillSec,
        false to not
        """
        # return self._instance.ShowSmartMessage(name, time_in_mill_sec, show_in_status_bar, remove_default_tip)
        raise NotImplemented

    def sketch_box_select(self, first_pt_x, first_pt_y, first_pt_z, second_pt_x, second_pt_y, second_pt_z):
        """
        Box selects all of the entities in a sketch within the specified coordinates of the selection box.
        :param first_pt_x: x coordinate of the first corner of the box
        :param first_pt_y: y coordinate of the first corner of the box
        :param first_pt_z: z coordinate of the first corner of the box
        :param second_pt_x: x coordinate of the opposite diagonal corner of the box
        :param second_pt_y: y coordinate of the opposite diagonal corner of the box
        :param second_pt_z: z coordinate of the opposite diagonal corner of the box
        """
        # return self._instance.SketchBoxSelect(first_pt_x, first_pt_y, first_pt_z, second_pt_x, second_pt_y, second_pt_z)
        raise NotImplemented

    def sketch_offset_on_surface(self, offset, reverse, use_front, make_construct):
        """
        Creates a Euclidean sketch offset from selected edges of a face or surface.
        :param offset: Offset distance
        :param reverse: True to reverse the 3D sketch, false to not
        :param use_front: Although not currently used, must be set to true
        :param make_construct: True to make the 3D sketch construction geometry after offsetting, false to not
        """
        # return self._instance.SketchOffsetOnSurface(offset, reverse, use_front, make_construct)
        raise NotImplemented

    def start_format_painter(self):
        """Starts the Format Painter."""
        # return self._instance.StartFormatPainter
        raise NotImplemented

    def start_recording_undo_object(self):
        """Starts recording the SOLIDWORKS Undo object."""
        # return self._instance.StartRecordingUndoObject
        raise NotImplemented

    def stop_format_painter(self):
        """Stops the Format Painter."""
        # return self._instance.StopFormatPainter
        raise NotImplemented

    def stretch(self, keep_relations, base_x, base_y, dest_x, dest_y):
        """
        Stretch the selected entities.
        :param keep_relations: True to keep the sketch relations intact, false to sever them
        :param base_x: x coordinate of the base point
        :param base_y: y coordinate of the base point
        :param dest_x: x coordinate of the destination stretch
        :param dest_y: y coordinate of the destination of the stretch
        """
        # return self._instance.Stretch(keep_relations, base_x, base_y, dest_x, dest_y)
        raise NotImplemented

    def update_external_file_references(self, config_option, config_name, update_status):
        """
        Updates the external files references on this model.
        :param config_option: Configuration options as defined by swExternalFileReferencesConfig_e
        :param config_name: Name of configuration; required when configOption set to swExternalFileReferencesNamedConfig
        :param update_status: Update status option as defined by swExternalFileReferencesUpdate_e
        """
        # return self._instance.UpdateExternalFileReferences(config_option, config_name, update_status)
        raise NotImplemented

    def update_frozen_features(self, update_all_configs):
        """
        Updates frozen features of the model.
        :param update_all_configs: True to update all configurations, false to not
        """
        # return self._instance.UpdateFrozenFeatures(update_all_configs)
        raise NotImplemented

    def update_render_materials_in_scene_graph(self, add_to_s_g):
        """
        Sets whether to update the appearances in the graphics area in the model.
        :param add_to_s_g: True to update the appearances in the graphics area, false to not
        """
        # return self._instance.UpdateRenderMaterialsInSceneGraph(add_to_s_g)
        raise NotImplemented

    def update_standard_views(self, view_name, view_id):
        """
        Changes the specified standard view to the current model view.
        :param view_name: Name of the standard model view to change; empty string to use ViewId (see Remarks)
        :param view_id: View ID as defined in swStandardViews_e; -1 to use ViewName (see Remarks)
        """
        # return self._instance.UpdateStandardViews(view_name, view_id)
        raise NotImplemented

    def update_sun_light(self):
        """Updates sunlight position, color, and background image."""
        # return self._instance.UpdateSunLight
        raise NotImplemented

    def upgrade_legacy_c_threads(self):
        """Upgrades cosmetic thread features in this legacy model to the latest cosmetic thread architecture."""
        # return self._instance.UpgradeLegacyCThreads
        raise NotImplemented

    def view_zoom_to_sheet(self):
        """Zooms a drawing sheet to its maximum size within the window."""
        # return self._instance.ViewZoomToSheet
        raise NotImplemented
