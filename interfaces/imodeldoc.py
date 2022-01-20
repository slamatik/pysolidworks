from com import Com
from .iconfigurationmanager import IConfigurationManager
from .imodeldocextension import IModelDocExtension
from .ifeaturemanager import IFeatureManager
from interfaces.imodelview import IModelView
from interfaces.iselectionmgr import ISelectionMgr
import win32com.client as win32
import pythoncom


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html

class IModelDoc:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def active_view(self):
        return IModelView(self._instance.ActiveView)

    @property
    def configuration_manager(self):
        return IConfigurationManager(self._instance)

    @property
    def extension(self):
        return IModelDocExtension(self._instance)

    @property
    def feature_manager(self):
        return IFeatureManager(self._instance)

    @property
    def feature_manager_splitter_position(self):
        return self._instance.FeatureManagerSplitterPosition

    @feature_manager_splitter_position.setter
    def feature_manager_splitter_position(self, value):
        self._instance.FeatureManagerSplitterPosition = value

    @property
    def length_unit(self):
        return self._instance.LengthUnit

    @property
    def material_user_name(self):
        return self._instance.MaterialUserName

    @material_user_name.setter
    def material_user_name(self, value):
        self._instance.MaterialUserName = value

    @property
    def selection_manager(self):
        return ISelectionMgr(self._instance.SelectionManager)

    def activate_selected_feature(self):
        """Activates the selected feature for editing."""
        # return self._instance.ActivateSelectedFeature
        raise NotImplemented

    def add_configuration(self):
        """Adds a new configuration to this model document."""
        # return self._instance.AddConfiguration3
        raise NotImplemented

    def add_diameter_dimension(self):
        """Adds a diameter dimension at the specified location for the selected item."""
        # return self._instance.AddDiameterDimension2
        raise NotImplemented

    def add_dimension(self):
        """Creates a display dimension at the specified location for selected entities."""
        # return self._instance.AddDimension2
        raise NotImplemented

    def add_feature_mgr_view(self):
        """Adds the specified tab to the FeatureManager design tree view."""
        # return self._instance.AddFeatureMgrView3
        raise NotImplemented

    def add_horizontal_dimension(self):
        """Creates a horizontal dimension for the currently selected entities at the specified location."""
        # return self._instance.AddHorizontalDimension2
        raise NotImplemented

    def add_ins(self):
        """Displays the Add-In Manager dialog box."""
        # return self._instance.AddIns
        raise NotImplemented

    def add_light_source(self):
        """Adds a type of light source to a scene with the specified names."""
        # return self._instance.AddLightSource
        raise NotImplemented

    def add_light_source_ext_property(self):
        """Stores a float, string, or integer value for the light source."""
        # return self._instance.AddLightSourceExtProperty
        raise NotImplemented

    def add_light_to_scene(self):
        """Adds a light source to a scene."""
        # return self._instance.AddLightToScene
        raise NotImplemented

    def add_loft_section(self):
        """Adds a loft section to a blend feature."""
        # return self._instance.AddLoftSection
        raise NotImplemented

    def add_property_extension(self):
        """Adds a property extension to this model."""
        # return self._instance.AddPropertyExtension
        raise NotImplemented

    def add_radial_dimension(self):
        """Adds a radial dimension at the specified location for the selected item."""
        # return self._instance.AddRadialDimension2
        raise NotImplemented

    def add_scene_ext_property(self):
        """Stores a float, string, or integer value for a scene."""
        # return self._instance.AddSceneExtProperty
        raise NotImplemented

    def add_vertical_dimension(self):
        """Creates a vertical dimension for the currently selected entities at the specified location."""
        # return self._instance.AddVerticalDimension2
        raise NotImplemented

    def align_ordinate(self):
        """Aligns the selected group of ordinate dimensions."""
        # return self._instance.AlignOrdinate
        raise NotImplemented

    def align_parallel_dimensions(self):
        """Aligns the selected linear dimensions in a parallel fashion."""
        # return self._instance.AlignParallelDimensions
        raise NotImplemented

    def blank_ref_geom(self):
        """Hides the selected reference geometry in the graphics window."""
        # return self._instance.BlankRefGeom
        raise NotImplemented

    def blank_sketch(self):
        """Hides the selected sketches."""
        # return self._instance.BlankSketch
        raise NotImplemented

    def break_dimension_alignment(self):
        """Breaks the association of any selected dimensions belonging to an alignment group (parallel or collinear)."""
        # return self._instance.BreakDimensionAlignment
        raise NotImplemented

    def clear_selection(self):
        """Clears the selection list."""
        # return self._instance.ClearSelection2
        raise NotImplemented

    def clear_undo_list(self):
        """Clears the undo list for this model document."""
        # return self._instance.ClearUndoList
        raise NotImplemented

    def close(self):
        """Not implemented. Use ISldWorks::CloseDoc."""
        # return self._instance.Close
        raise NotImplemented

    def close_family_table(self):
        """Closes the design table currently being edited."""
        # return self._instance.CloseFamilyTable
        raise NotImplemented

    def close_print_preview(self):
        """Closes the currently displayed Print Preview page for this document."""
        # return self._instance.ClosePrintPreview
        raise NotImplemented

    def closest_distance(self):
        """Calculates the minimum distance between the specified geometric objects."""
        # return self._instance.ClosestDistance
        raise NotImplemented

    def create_arc_by_center(self):
        """Creates an arc by center in this model document."""
        # return self._instance.CreateArcByCenter
        raise NotImplemented

    def create_center_line_v_b(self):
        """Creates a center line from P1 to P2 and can be used in Visual Basic for Applications (VBA) and other forms of Basic that do not support SafeArrays."""
        # return self._instance.CreateCenterLineVB
        raise NotImplemented

    def create_clipped_splines(self):
        """Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch."""
        # return self._instance.CreateClippedSplines
        raise NotImplemented

    def create_group(self):
        """Creates an annotation group from the currently selected annotations."""
        # return self._instance.CreateGroup
        raise NotImplemented

    def de_activate_feature_mgr_view(self):
        """Deactivates a tab in the FeatureManager design tree view."""
        # return self._instance.DeActivateFeatureMgrView
        raise NotImplemented

    def debug_check_iges_geom(self):
        """Dumps a IGES geometry check."""
        # return self._instance.DebugCheckIgesGeom
        raise NotImplemented

    def delete_all_relations(self):
        """Deletes all existing relations."""
        # return self._instance.DeleteAllRelations
        raise NotImplemented

    def delete_bend_table(self):
        """Deletes a bend table."""
        # return self._instance.DeleteBendTable
        raise NotImplemented

    def delete_bkg_image(self):
        """Deletes any background image."""
        # return self._instance.DeleteBkgImage
        raise NotImplemented

    def delete_configuration(self):
        """Deletes a configuration."""
        # return self._instance.DeleteConfiguration2
        raise NotImplemented

    def delete_design_table(self):
        """Deletes the design table for this document, if one exists."""
        # return self._instance.DeleteDesignTable
        raise NotImplemented

    def delete_feature_mgr_view(self):
        """Removes the specified tab in the FeatureManager design tree."""
        # return self._instance.DeleteFeatureMgrView
        raise NotImplemented

    def delete_light_source(self):
        """Deletes a light source."""
        # return self._instance.DeleteLightSource
        raise NotImplemented

    def delete_named_view(self):
        """Deletes the specified model view."""
        # return self._instance.DeleteNamedView
        raise NotImplemented

    def derive_sketch(self):
        """Creates a derived sketch."""
        # return self._instance.DeriveSketch
        raise NotImplemented

    def de_select_by_i_d(self):
        """Removes the selected object from the selection list."""
        # return self._instance.DeSelectByID
        raise NotImplemented

    def dim_preferences(self):
        """Sets dimension preferences."""
        # return self._instance.DimPreferences
        raise NotImplemented

    def dissolve_library_feature(self):
        """Dissolves the selected library features."""
        # return self._instance.DissolveLibraryFeature
        raise NotImplemented

    def dissolve_sketch_text(self):
        """Dissolves sketch text."""
        # return self._instance.DissolveSketchText
        raise NotImplemented

    def drag_to(self):
        """Drags the specified end point."""
        # return self._instance.DragTo
        raise NotImplemented

    def draw_light_icons(self):
        """Draws any visible light icons."""
        # return self._instance.DrawLightIcons
        raise NotImplemented

    def edit_configuration(self):
        """Edits the specified configuration."""
        # return self._instance.EditConfiguration3
        raise NotImplemented

    def edit_copy(self):
        """Copies the currently selected items and places them in the clipboard."""
        # return self._instance.EditCopy
        raise NotImplemented

    def edit_cut(self):
        """Cuts the currently selected items and places them on the Microsoft Windows Clipboard."""
        # return self._instance.EditCut
        raise NotImplemented

    def edit_datum_target_symbol(self):
        """Edits a datum target symbol."""
        # return self._instance.EditDatumTargetSymbol
        raise NotImplemented

    def edit_delete(self):
        """Deletes the selected items."""
        # return self._instance.EditDelete
        raise NotImplemented

    def edit_ordinate(self):
        """Puts the currently selected ordinate dimension into edit mode so you could add more ordinate dimensions to this group."""
        # return self._instance.EditOrdinate
        raise NotImplemented

    def edit_rebuild(self):
        """Rebuilds only those features that need to be rebuilt in the active configuration in the model."""
        # return self._instance.EditRebuild3
        raise NotImplemented

    def edit_redo(self):
        """Repeats the specified number of actions in this SOLIDWORKS session."""
        # return self._instance.EditRedo2
        raise NotImplemented

    def edit_route(self):
        """Makes the last selected route the active route."""
        # return self._instance.EditRoute
        raise NotImplemented

    def edit_seed_feat(self):
        """Gets the pattern seed feature, based on the selected face, and displays the Edit Definition dialog for that feature."""
        # return self._instance.EditSeedFeat
        raise NotImplemented

    def edit_sketch(self):
        """Allows the currently selected sketch to be edited."""
        # return self._instance.EditSketch
        raise NotImplemented

    def edit_sketch_or_single_sketch_feature(self):
        """Edits a selected sketch or feature sketch."""
        # return self._instance.EditSketchOrSingleSketchFeature
        raise NotImplemented

    def edit_suppress(self):
        """Suppresses the selected feature, the selected component, or the owning feature of the selected face."""
        # return self._instance.EditSuppress2
        raise NotImplemented

    def edit_undo(self):
        """Undoes the specified number of actions in the active SOLIDWORKS session."""
        # return self._instance.EditUndo2
        raise NotImplemented

    def edit_unsuppress(self):
        """Unsuppresses the selected feature or component."""
        # return self._instance.EditUnsuppress2
        raise NotImplemented

    def edit_unsuppress_dependent(self):
        """Unsuppresses the selected feature or component and their dependents."""
        # return self._instance.EditUnsuppressDependent2
        raise NotImplemented

    def entity_properties(self):
        """Displays the Properties dialog for the selected edge or face."""
        # return self._instance.EntityProperties
        raise NotImplemented

    def enum_model_views(self):
        """Gets the model views enumeration in this document."""
        # return self._instance.EnumModelViews
        raise NotImplemented

    def feat_edit(self):
        """Puts the current feature into edit mode."""
        # return self._instance.FeatEdit
        raise NotImplemented

    def feat_edit_def(self):
        """Displays the Feature Definition dialog and lets the user edit the values."""
        # return self._instance.FeatEditDef
        raise NotImplemented

    def feature_by_position_reverse(self):
        """Gets the nth from last feature in the document."""
        # return self._instance.FeatureByPositionReverse
        raise NotImplemented

    def feature_chamfer(self):
        """Creates a chamfer feature."""
        # return self._instance.FeatureChamfer
        raise NotImplemented

    def feature_reference_curve(self):
        """Creates a reference curve feature from an array of curves."""
        # return self._instance.FeatureReferenceCurve
        raise NotImplemented

    def file_summary_info(self):
        """Displays the File Summary Information dialog box for this file."""
        # return self._instance.FileSummaryInfo
        raise NotImplemented

    def first_feature(self):
        """Gets the first feature in the document."""
        # return self._instance.FirstFeature
        raise NotImplemented

    def font_bold(self):
        """Enables or disables bold font style in the selected notes, dimensions, and GTols."""
        # return self._instance.FontBold
        raise NotImplemented

    def font_face(self):
        """Changes the font face in the selected notes, dimensions, and GTols."""
        # return self._instance.FontFace
        raise NotImplemented

    def font_italic(self):
        """Enables or disables italic font style in the selected notes, dimensions, and GTols."""
        # return self._instance.FontItalic
        raise NotImplemented

    def font_points(self):
        """Changes the font height (specified in points) in the selected notes, dimensions, and GTols."""
        # return self._instance.FontPoints
        raise NotImplemented

    def font_underline(self):
        """Enables or disables underlining the selected notes, dimensions, and GTols."""
        # return self._instance.FontUnderline
        raise NotImplemented

    def font_units(self):
        """Changes font height (specified in current system units) in the selected notes, dimensions, and GTols."""
        # return self._instance.FontUnits
        raise NotImplemented

    def force_rebuild(self, top_only=False):
        """Forces a rebuild of all features in the active configuration in the model."""
        arg1 = win32.VARIANT(pythoncom.VT_BOOL, top_only)
        return self._instance.ForceRebuild3(arg1)

    def force_release_locks(self):
        """Releases the locks that a file system places on a file when it is opened and detaches that file from the file system."""
        # return self._instance.ForceReleaseLocks
        raise NotImplemented

    def get_add_to_d_b(self):
        """Gets whether entities are added directly to the SOLIDWORKS database."""
        # return self._instance.GetAddToDB
        raise NotImplemented

    def get_ambient_light_properties(self):
        """Gets the ambient light properties for this model document."""
        # return self._instance.GetAmbientLightProperties
        raise NotImplemented

    def get_angular_units(self):
        """Gets the current angular unit settings."""
        # return self._instance.GetAngularUnits
        raise NotImplemented

    def get_arc_centers_displayed(self):
        """Gets whether the arc centers are displayed."""
        # return self._instance.GetArcCentersDisplayed
        raise NotImplemented

    def get_bend_state(self):
        """Gets the current bend state of a sheet metal part."""
        # return self._instance.GetBendState
        raise NotImplemented

    def get_blocking_state(self):
        """Gets the current value of the SOLIDWORKS blocking state, within the range of values accessible by IModelDoc2::SetBlockingState."""
        # return self._instance.GetBlockingState
        raise NotImplemented

    def get_configuration_by_name(self):
        """Gets the specified configuration."""
        # return self._instance.GetConfigurationByName
        raise NotImplemented

    def get_configuration_count(self):
        """Gets the number of configurations."""
        # return self._instance.GetConfigurationCount
        raise NotImplemented

    def get_configuration_names(self):
        """Gets the names of the configurations in this document."""
        # return self._instance.GetConfigurationNames
        raise NotImplemented

    def get_consider_leaders_as_lines(self):
        """Gets whether the display data of a leader is included as lines when the lines are retrieved from a view or annotation in this document."""
        # return self._instance.GetConsiderLeadersAsLines
        raise NotImplemented

    def get_current_coordinate_system_name(self):
        """Gets the name of the current coordinate system or an empty string for the default coordinate system."""
        # return self._instance.GetCurrentCoordinateSystemName
        raise NotImplemented

    def get_default_text_height(self):
        """Gets the default text height in use for this document."""
        # return self._instance.GetDefaultTextHeight
        raise NotImplemented

    def get_design_table(self):
        """Gets the design table associated with this part or assembly document."""
        # return self._instance.GetDesignTable
        raise NotImplemented

    def get_direction_light_properties(self):
        """Gets the directional light properties."""
        # return self._instance.GetDirectionLightProperties
        raise NotImplemented

    def get_display_when_added(self):
        """Gets whether new sketch entities are displayed when created."""
        # return self._instance.GetDisplayWhenAdded
        raise NotImplemented

    def get_entity_name(self):
        """Gets the name of the specified face, edge, or vertex."""
        # return self._instance.GetEntityName
        raise NotImplemented

    def get_equation_mgr(self):
        """Gets the equation manager."""
        # return self._instance.GetEquationMgr
        raise NotImplemented

    def get_external_reference_name(self):
        """Gets the name of the externally referenced document (in the case of a join or mirrored part)."""
        # return self._instance.GetExternalReferenceName
        raise NotImplemented

    def get_feature_count(self):
        """Gets the number of features in this document."""
        # return self._instance.GetFeatureCount
        raise NotImplemented

    def get_feature_manager_width(self):
        """Gets the width of the FeatureManager design tree."""
        # return self._instance.GetFeatureManagerWidth
        raise NotImplemented

    def get_first_annotation(self):
        """Gets the first annotation in the model."""
        # return self._instance.GetFirstAnnotation2
        raise NotImplemented

    def get_first_model_view(self):
        """Gets the first view in a model document."""
        # return self._instance.GetFirstModelView
        raise NotImplemented

    def get_grid_settings(self):
        """Gets the current grid settings."""
        # return self._instance.GetGridSettings
        raise NotImplemented

    def get_layer_manager(self):
        """Gets the layer manager for the current drawing document."""
        # return self._instance.GetLayerManager
        raise NotImplemented

    def get_light_source_count(self):
        """Gets the number of light sources."""
        # return self._instance.GetLightSourceCount
        raise NotImplemented

    def get_light_source_ext_property(self):
        """Gets a float, string, or integer value stored for the light source."""
        # return self._instance.GetLightSourceExtProperty
        raise NotImplemented

    def get_light_source_id_from_name(self):
        """Gets the ID of the specified light source."""
        # return self._instance.GetLightSourceIdFromName
        raise NotImplemented

    def get_light_source_name(self):
        """Gets the name of a light source used internally by the SOLIDWORKS application."""
        # return self._instance.GetLightSourceName
        raise NotImplemented

    def get_line_count(self):
        """Gets the number of lines in the current sketch."""
        # return self._instance.GetLineCount
        raise NotImplemented

    def get_lines(self):
        """Gets all of the lines in the current sketch."""
        # return self._instance.GetLines
        raise NotImplemented

    def get_model_view_names(self):
        """Gets a list containing the names of each model view in this document."""
        # return self._instance.GetModelViewNames
        raise NotImplemented

    def get_next(self):
        """Gets the next document in the current SOLIDWORKS session."""
        # return self._instance.GetNext
        raise NotImplemented

    def get_num_dependencies(self):
        """Gets the number of strings returned by IModelDoc2::GetDependencies2."""
        # return self._instance.GetNumDependencies
        raise NotImplemented

    def get_path_name(self):
        """Gets the full path name for this document, including the file name."""
        return self._instance.GetPathName

    def get_point_light_properties(self):
        """Gets point light properties."""
        # return self._instance.GetPointLightProperties
        raise NotImplemented

    def get_popup_menu_mode(self):
        """Gets the current pop-up menu mode."""
        # return self._instance.GetPopupMenuMode
        raise NotImplemented

    def get_property_extension(self):
        """Gets the specified property extension on this model."""
        # return self._instance.GetPropertyExtension
        raise NotImplemented

    def get_ray_intersections_points(self):
        """Gets the intersection point information generated by IModelDoc2::RayIntersections."""
        # return self._instance.GetRayIntersectionsPoints
        raise NotImplemented

    def get_ray_intersections_topology(self):
        """Gets the topology intersections generated by IModelDoc2::RayIntersections."""
        # return self._instance.GetRayIntersectionsTopology
        raise NotImplemented

    def get_save_flag(self):
        """Gets whether the document is currently dirty and needs to be saved."""
        # return self._instance.GetSaveFlag
        raise NotImplemented

    def get_scene_bkg_d_i_b(self):
        """Gets background image as a LPDIBSECTION."""
        # return self._instance.GetSceneBkgDIB
        raise NotImplemented

    def get_scene_ext_property(self):
        """Gets a float, string, or integer value stored for the scene."""
        # return self._instance.GetSceneExtProperty
        raise NotImplemented

    def get_spotlight_properties(self):
        """Gets the spotlight properties."""
        # return self._instance.GetSpotlightProperties
        raise NotImplemented

    def get_standard_view_rotation(self):
        """Gets the specified view orientation matrix with respect to the Front view."""
        # return self._instance.GetStandardViewRotation
        raise NotImplemented

    def get_tessellation_quality(self):
        """Gets the shaded-display image quality number for the current document."""
        # return self._instance.GetTessellationQuality
        raise NotImplemented

    def get_title(self):
        """Gets the title of the document that appears in the active window's title bar."""
        return self._instance.GetTitle

    def get_toolbar_visibility(self):
        """Gets the visibility of a toolbar."""
        # return self._instance.GetToolbarVisibility
        raise NotImplemented

    def get_type(self):
        """Gets the type of the document."""
        # return self._instance.GetType
        raise NotImplemented

    def get_units(self):
        """Gets the current unit settings, fraction base, fraction value, and significant digits."""
        # return self._instance.GetUnits
        raise NotImplemented

    def get_update_stamp(self):
        """Gets the current update stamp for this document."""
        # return self._instance.GetUpdateStamp
        raise NotImplemented

    def get_user_unit(self):
        """Gets this document's units settings."""
        # return self._instance.GetUserUnit
        raise NotImplemented

    def get_visibility_of_construct_planes(self):
        """Gets whether construction (reference) planes are currently visible."""
        # return self._instance.GetVisibilityOfConstructPlanes
        raise NotImplemented

    def get_zebra_stripe_data(self):
        """Gets zebra line data."""
        # return self._instance.GetZebraStripeData
        raise NotImplemented

    def hide_component(self):
        """Hides the selected component."""
        # return self._instance.HideComponent2
        raise NotImplemented

    def hide_cosmetic_thread(self):
        """Hides the selected cosmetic thread."""
        # return self._instance.HideCosmeticThread
        raise NotImplemented

    def hide_dimension(self):
        """Hides the selected dimension in this document."""
        # return self._instance.HideDimension
        raise NotImplemented

    def hide_show_bodies(self):
        """Sets whether to hide or show the bodies in the model."""
        # return self._instance.HideShowBodies
        raise NotImplemented

    def hide_solid_body(self):
        """Hides the currently selected solid body."""
        # return self._instance.HideSolidBody
        raise NotImplemented

    def l_b_down_at(self):
        """Generates a left mouse button press (down) event."""
        # return self._instance.LBDownAt
        raise NotImplemented

    def l_b_up_at(self):
        """Generates a left-mouse button release (up) event."""
        # return self._instance.LBUpAt
        raise NotImplemented

    def list_auxiliary_external_file_references(self):
        """Gets the names of auxiliary external file references for this model."""
        # return self._instance.ListAuxiliaryExternalFileReferences
        raise NotImplemented

    def list_auxiliary_external_file_references_count(self):
        """Gets the number of auxiliary external file references for this model."""
        # return self._instance.ListAuxiliaryExternalFileReferencesCount
        raise NotImplemented

    def lock(self):
        """Blocks the modifying commands in the user interface, effectively locking the application."""
        # return self._instance.Lock
        raise NotImplemented

    def lock_all_external_references(self):
        """Locks all external references."""
        # return self._instance.LockAllExternalReferences
        raise NotImplemented

    def lock_light_to_model(self):
        """Locks or unlocks the specified light."""
        # return self._instance.LockLightToModel
        raise NotImplemented

    def mold_draft_analysis(self):
        """Performs a mold draft analysis."""
        # return self._instance.MoldDraftAnalysis
        raise NotImplemented

    def multi_select_by_ray(self):
        """Selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius."""
        # return self._instance.MultiSelectByRay
        raise NotImplemented

    def name_view(self):
        """Creates a named view using the current view."""
        # return self._instance.NameView
        raise NotImplemented

    def object_display_as_icon(self):
        """Shows the current OLE object as an icon."""
        # return self._instance.ObjectDisplayAsIcon
        raise NotImplemented

    def object_display_content(self):
        """Shows the current OLE object's content."""
        # return self._instance.ObjectDisplayContent
        raise NotImplemented

    def object_resetsize(self):
        """Sets the size of the current OLE object to the default."""
        # return self._instance.ObjectResetsize
        raise NotImplemented

    def parameter(self):
        """Gets the specified parameter."""
        # return self._instance.Parameter
        raise NotImplemented

    def parent_child_relationship(self):
        """Shows the Parent/Child Relationships dialog for the selected feature."""
        # return self._instance.ParentChildRelationship
        raise NotImplemented

    def paste(self):
        """Pastes the contents of the Microsoft Windows Clipboard at the current insertion point."""
        # return self._instance.Paste
        raise NotImplemented

    def print_direct(self):
        """Prints the current document to the default printer."""
        # return self._instance.PrintDirect
        raise NotImplemented

    def print_preview(self):
        """Displays the Print Preview page for the current document."""
        # return self._instance.PrintPreview
        raise NotImplemented

    def property_sheet(self):
        """Displays the the selected object's property sheet."""
        # return self._instance.PropertySheet
        raise NotImplemented

    def quit(self):
        """Closes the active document without saving changes (see Remarks)."""
        # return self._instance.Quit
        raise NotImplemented

    def reattach_ordinate(self):
        """Reattaches an ordinate dimension to a different entity."""
        # return self._instance.ReattachOrdinate
        raise NotImplemented

    def reload_or_replace(self):
        """Reloads or replaces the current model document."""
        # return self._instance.ReloadOrReplace
        raise NotImplemented

    def remove_groups(self):
        """Removes any annotation groups in the current selection."""
        # return self._instance.RemoveGroups
        raise NotImplemented

    def remove_inspect_curvature(self):
        """Removes curvature combs from the selected curved sketch segment."""
        # return self._instance.RemoveInspectCurvature
        raise NotImplemented

    def remove_items_from_group(self):
        """Removes the selected annotations from their annotation groups."""
        # return self._instance.RemoveItemsFromGroup
        raise NotImplemented

    def reset_blocking_state(self):
        """Resets the blocking state for the SOLIDWORKS menus."""
        # return self._instance.ResetBlockingState
        raise NotImplemented

    def reset_light_source_ext_property(self):
        """Resets the properties for a light source."""
        # return self._instance.ResetLightSourceExtProperty
        raise NotImplemented

    def reset_property_extension(self):
        """Clears all values stored in the property extension."""
        # return self._instance.ResetPropertyExtension
        raise NotImplemented

    def reset_scene_ext_property(self):
        """Resets the extension property for a scene."""
        # return self._instance.ResetSceneExtProperty
        raise NotImplemented

    def save(self, options=1):
        """Saves the current document."""
        arg1 = win32.VARIANT(pythoncom.VT_I4, options)
        arg2 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        arg3 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        self._instance().Save3(arg1, arg2, arg3)
        return arg2.value, arg3.value

    def save_b_m_p(self):
        """Saves the current view as a bitmap (BMP) file."""
        # return self._instance.SaveBMP
        raise NotImplemented

    def scale(self):
        """Scales the part."""
        # return self._instance.Scale
        raise NotImplemented

    def screen_rotate(self):
        """Switches between model and screen center rotation."""
        # return self._instance.ScreenRotate
        raise NotImplemented

    def selected_edge_properties(self):
        """Sets the property values of the selected edge."""
        # return self._instance.SelectedEdgeProperties
        raise NotImplemented

    def selected_face_properties(self):
        """Sets the material property values of the selected face."""
        # return self._instance.SelectedFaceProperties
        raise NotImplemented

    def selected_feature_properties(self):
        """Sets the property values of the selected feature."""
        # return self._instance.SelectedFeatureProperties
        raise NotImplemented

    def select_loop(self):
        """Selects the loop that corresponds to the selected edge."""
        # return self._instance.SelectLoop
        raise NotImplemented

    def select_midpoint(self):
        """Puts the midpoint (swSelMIDPOINTS) of that edge on the selection list and removes the edge from the selection list when an edge is selected."""
        # return self._instance.SelectMidpoint
        raise NotImplemented

    def select_tangency(self):
        """Selects all faces tangent to the selected face."""
        # return self._instance.SelectTangency
        raise NotImplemented

    def set_ambient_light_properties(self):
        """Sets ambient light properties."""
        # return self._instance.SetAmbientLightProperties
        raise NotImplemented

    def set_angular_units(self):
        """Sets the current angular units."""
        # return self._instance.SetAngularUnits
        raise NotImplemented

    def set_arc_centers_displayed(self):
        """Sets the current arc centers displayed setting."""
        # return self._instance.SetArcCentersDisplayed
        raise NotImplemented

    def set_bend_state(self):
        """Sets the bend state of a sheet metal part."""
        # return self._instance.SetBendState
        raise NotImplemented

    def set_blocking_state(self):
        """Sets the blocking state for the SOLIDWORKS menus."""
        # return self._instance.SetBlockingState
        raise NotImplemented

    def set_consider_leaders_as_lines(self):
        """Sets a flag on the document that indicates whether the display data of a leader should be included as lines when the lines are retrieved from a view or annotation in this document."""
        # return self._instance.SetConsiderLeadersAsLines
        raise NotImplemented

    def set_direction_light_properties(self):
        """Sets direction light properties."""
        # return self._instance.SetDirectionLightProperties
        raise NotImplemented

    def set_feature_manager_width(self):
        """Sets the width of the FeatureManager design tree."""
        # return self._instance.SetFeatureManagerWidth
        raise NotImplemented

    def set_light_source_name(self):
        """Sets the light source name used internally by the SOLIDWORKS software."""
        # return self._instance.SetLightSourceName
        raise NotImplemented

    def set_light_source_property_values_v_b(self):
        """Sets the light source property values."""
        # return self._instance.SetLightSourcePropertyValuesVB
        raise NotImplemented

    def set_param_value(self):
        """Sets the value of selected dimension (or parameter)."""
        # return self._instance.SetParamValue
        raise NotImplemented

    def set_pick_mode(self):
        """Returns the user to the default selection mode."""
        # return self._instance.SetPickMode
        raise NotImplemented

    def set_point_light_properties(self):
        """Sets point light properties."""
        # return self._instance.SetPointLightProperties
        raise NotImplemented

    def set_popup_menu_mode(self):
        """Sets the pop-up menu mode."""
        # return self._instance.SetPopupMenuMode
        raise NotImplemented

    def set_read_only_state(self):
        """Sets whether this document is read-only or read-write."""
        # return self._instance.SetReadOnlyState
        raise NotImplemented

    def set_save_as_file_name(self):
        """Sets the Save As filename from within the FileSaveAsNotify2 event handlers, thereby, bypassing the Save As dialog."""
        # return self._instance.SetSaveAsFileName
        raise NotImplemented

    def set_save_flag(self):
        """Flags the document as dirty."""
        # return self._instance.SetSaveFlag
        raise NotImplemented

    def set_scene_bkg_d_i_b(self):
        """Sets background image described by DIBSECTION data."""
        # return self._instance.SetSceneBkgDIB
        raise NotImplemented

    def set_spotlight_properties(self):
        """Sets the spotlight properties."""
        # return self._instance.SetSpotlightProperties
        raise NotImplemented

    def set_tessellation_quality(self):
        """Sets the shaded-display image quality number for the current document."""
        # return self._instance.SetTessellationQuality
        raise NotImplemented

    def set_title(self):
        """Sets the title of a new document."""
        # return self._instance.SetTitle2
        raise NotImplemented

    def set_toolbar_visibility(self):
        """Sets the visibility of a toolbar."""
        # return self._instance.SetToolbarVisibility
        raise NotImplemented

    def set_units(self):
        """Sets the units used by the end-user for the model."""
        # return self._instance.SetUnits
        raise NotImplemented

    def set_zebra_stripe_data(self):
        """Sets the zebra-line data."""
        # return self._instance.SetZebraStripeData
        raise NotImplemented

    def show_component(self):
        """Shows the selected component."""
        # return self._instance.ShowComponent2
        raise NotImplemented

    def show_configuration(self):
        """Shows the named configuration by switching to that configuration and making it the active configuration."""
        # return self._instance.ShowConfiguration2
        raise NotImplemented

    def show_cosmetic_thread(self):
        """Shows the selected cosmetic thread."""
        # return self._instance.ShowCosmeticThread
        raise NotImplemented

    def show_named_view(self):
        """Shows the specified view."""
        # return self._instance.ShowNamedView2
        raise NotImplemented

    def show_solid_body(self):
        """Shows the selected solid body."""
        # return self._instance.ShowSolidBody
        raise NotImplemented

    def sketch_d_intersections(self):
        """Creates new sketch segments based on the selected surfaces."""
        # return self._instance.Sketch3DIntersections
        raise NotImplemented

    def sketch_add_constraints(self):
        """Adds the specified constraint to the selected entities."""
        # return self._instance.SketchAddConstraints
        raise NotImplemented

    def sketch_align(self):
        """Aligns the selected sketch entities."""
        # return self._instance.SketchAlign
        raise NotImplemented

    def sketch_arc(self):
        """Creates an arc in the current model document."""
        # return self._instance.SketchArc
        raise NotImplemented

    def sketch_centerline(self):
        """Adds a centerline to the current model document."""
        # return self._instance.SketchCenterline
        raise NotImplemented

    def sketch_constrain_coincident(self):
        """Makes the selected sketch entities coincident."""
        # return self._instance.SketchConstrainCoincident
        raise NotImplemented

    def sketch_constrain_concentric(self):
        """Makes the selected sketch entities concentric."""
        # return self._instance.SketchConstrainConcentric
        raise NotImplemented

    def sketch_constrain_parallel(self):
        """Makes the selected sketch entities parallel."""
        # return self._instance.SketchConstrainParallel
        raise NotImplemented

    def sketch_constrain_perp(self):
        """Makes the selected sketch entities perpendicular."""
        # return self._instance.SketchConstrainPerp
        raise NotImplemented

    def sketch_constrain_tangent(self):
        """Makes the selected entities tangent."""
        # return self._instance.SketchConstrainTangent
        raise NotImplemented

    def sketch_constraints_del(self):
        """Deletes the specified relationship (constraint) on the currently selected sketch item."""
        # return self._instance.SketchConstraintsDel
        raise NotImplemented

    def sketch_constraints_del_all(self):
        """Deletes all of the constraints on the currently selected sketch segment."""
        # return self._instance.SketchConstraintsDelAll
        raise NotImplemented

    def sketch_convert_iso_curves(self):
        """Converts ISO-parametric curves on a selected surface into a sketch entity."""
        # return self._instance.SketchConvertIsoCurves
        raise NotImplemented

    def sketch_mirror(self):
        """Creates new entities that are mirror images of the selected entities."""
        # return self._instance.SketchMirror
        raise NotImplemented

    def sketch_modify_flip(self):
        """Flips the the active or selected sketch about the specified coordinate system axis."""
        # return self._instance.SketchModifyFlip
        raise NotImplemented

    def sketch_modify_rotate(self):
        """Rotates the coordinate system of the active or selected sketch."""
        # return self._instance.SketchModifyRotate
        raise NotImplemented

    def sketch_modify_scale(self):
        """Scales the active or selected sketch."""
        # return self._instance.SketchModifyScale
        raise NotImplemented

    def sketch_modify_translate(self):
        """Translates the coordinate system of the active or selected sketch."""
        # return self._instance.SketchModifyTranslate
        raise NotImplemented

    def sketch_offset_edges(self):
        """Offsets the edges of the selected entities."""
        # return self._instance.SketchOffsetEdges
        raise NotImplemented

    def sketch_offset_entities(self):
        """Generates entities in the active sketch by offsetting the selected geometry by the specified amount."""
        # return self._instance.SketchOffsetEntities2
        raise NotImplemented

    def sketch_spline(self):
        """Starts a spline, or continues one, using the specified point."""
        # return self._instance.SketchSpline
        raise NotImplemented

    def sketch_tangent_arc(self):
        """Creates a tangent arc in the current model document."""
        # return self._instance.SketchTangentArc
        raise NotImplemented

    def sketch_undo(self):
        """Undoes the last sketch command."""
        # return self._instance.SketchUndo
        raise NotImplemented

    def sketch_use_edge_ctrline(self):
        """Uses this centerline in sketch."""
        # return self._instance.SketchUseEdgeCtrline
        raise NotImplemented

    def sk_tools_auto_constr(self):
        """Automatically constrains the active sketch."""
        # return self._instance.SkToolsAutoConstr
        raise NotImplemented

    def toolbars(self):
        """Turns the specified SOLIDWORKS toolbars on and off."""
        # return self._instance.Toolbars
        raise NotImplemented

    def tools_distance(self):
        """Computes distance."""
        # return self._instance.ToolsDistance
        raise NotImplemented

    def tools_grid(self):
        """Shows and hides the grid in this model document."""
        # return self._instance.ToolsGrid
        raise NotImplemented

    def tools_macro(self):
        """Not implemented."""
        # return self._instance.ToolsMacro
        raise NotImplemented

    def tools_mass_props(self):
        """Calculates the mass properties."""
        # return self._instance.ToolsMassProps
        raise NotImplemented

    def tools_sketch_scale(self):
        """Scales a sketch."""
        # return self._instance.ToolsSketchScale
        raise NotImplemented

    def tools_sketch_translate(self):
        """Translates a sketch."""
        # return self._instance.ToolsSketchTranslate
        raise NotImplemented

    def un_blank_ref_geom(self):
        """Shows the selected, hidden reference geometry in the graphics window."""
        # return self._instance.UnBlankRefGeom
        raise NotImplemented

    def unblank_sketch(self):
        """Shows a hidden sketch."""
        # return self._instance.UnblankSketch
        raise NotImplemented

    def underive_sketch(self):
        """Changes a sketch to underived."""
        # return self._instance.UnderiveSketch
        raise NotImplemented

    def un_lock(self):
        """Reverses IModelDoc2::Lock and changes the status bar message to Process Complete."""
        # return self._instance.UnLock
        raise NotImplemented

    def unlock_all_external_references(self):
        """Unlocks all external references."""
        # return self._instance.UnlockAllExternalReferences
        raise NotImplemented

    def user_favors(self):
        """Specifies whether geometric relations are automatically created as you add sketch entities."""
        # return self._instance.UserFavors
        raise NotImplemented

    def version_history(self):
        """Gets an array of strings indicating the versions in which this document was saved, including the SOLIDWORKS version in which the model document is currently opened and which is the last value returned in the array."""
        # return self._instance.VersionHistory
        raise NotImplemented

    def view_constraint(self):
        """Shows the constraints for the current model document."""
        # return self._instance.ViewConstraint
        raise NotImplemented

    def view_disp_coordinate_systems(self):
        """Toggles the display of coordinate systems on and off."""
        # return self._instance.ViewDispCoordinateSystems
        raise NotImplemented

    def view_display_curvature(self):
        """Toggles the display of surface curvature on and off."""
        # return self._instance.ViewDisplayCurvature
        raise NotImplemented

    def view_display_faceted(self):
        """Sets the current display mode to show the facets that make up a shaded picture of STL output."""
        # return self._instance.ViewDisplayFaceted
        raise NotImplemented

    def view_display_hiddengreyed(self):
        """Sets the current display mode to Hidden Lines Visible."""
        # return self._instance.ViewDisplayHiddengreyed
        raise NotImplemented

    def view_display_hiddenremoved(self):
        """Sets the current display mode to Hidden Lines Removed."""
        # return self._instance.ViewDisplayHiddenremoved
        raise NotImplemented

    def view_display_shaded(self):
        """Sets the current display mode to Shaded."""
        # return self._instance.ViewDisplayShaded
        raise NotImplemented

    def view_display_wireframe(self):
        """Sets the current display mode to Wireframe."""
        # return self._instance.ViewDisplayWireframe
        raise NotImplemented

    def view_disp_origins(self):
        """Toggles the display of origins off and on."""
        # return self._instance.ViewDispOrigins
        raise NotImplemented

    def view_disp_refaxes(self):
        """Toggles the display of reference axis on and off."""
        # return self._instance.ViewDispRefaxes
        raise NotImplemented

    def view_disp_refplanes(self):
        """Toggles the display of reference planes on and off."""
        # return self._instance.ViewDispRefplanes
        raise NotImplemented

    def view_disp_ref_points(self):
        """Shows and hides the reference points for the current model document."""
        # return self._instance.ViewDispRefPoints
        raise NotImplemented

    def view_disp_temp_refaxes(self):
        """Toggles the display of temporary reference axes on and off."""
        # return self._instance.ViewDispTempRefaxes
        raise NotImplemented

    def view_ogl_shading(self):
        """Sets the current display subsystem to use OpenGL."""
        # return self._instance.ViewOglShading
        raise NotImplemented

    def view_orientation_undo(self):
        """Undoes previous view orientation changes that were made interactively by the user."""
        # return self._instance.ViewOrientationUndo
        raise NotImplemented

    def view_rotate(self):
        """Rotates the view of the current model."""
        # return self._instance.ViewRotate
        raise NotImplemented

    def view_rotateminusx(self):
        """Dynamically rotates the view around x in a negative direction with the current increment."""
        # return self._instance.ViewRotateminusx
        raise NotImplemented

    def view_rotateminusy(self):
        """Dynamically rotates the view around y in a negative direction with the current increment."""
        # return self._instance.ViewRotateminusy
        raise NotImplemented

    def view_rotateminusz(self):
        """Dynamically rotates the view around z in a negative direction with the current increment."""
        # return self._instance.ViewRotateminusz
        raise NotImplemented

    def view_rotateplusx(self):
        """Rotates the view around x in a positive direction with the current increment."""
        # return self._instance.ViewRotateplusx
        raise NotImplemented

    def view_rotateplusy(self):
        """Rotates the view around y in a positive direction with the current increment."""
        # return self._instance.ViewRotateplusy
        raise NotImplemented

    def view_rotateplusz(self):
        """Rotates the view around z in a positive direction with the current increment."""
        # return self._instance.ViewRotateplusz
        raise NotImplemented

    def view_rot_x_minus_ninety(self):
        """Dynamically rotates the view by negative 90 about x."""
        # return self._instance.ViewRotXMinusNinety
        raise NotImplemented

    def view_rot_x_plus_ninety(self):
        """Dynamically rotates the view by 90 about x."""
        # return self._instance.ViewRotXPlusNinety
        raise NotImplemented

    def view_rot_y_minus_ninety(self):
        """Dynamically rotates the view by negative 90 about y."""
        # return self._instance.ViewRotYMinusNinety
        raise NotImplemented

    def view_rot_y_plus_ninety(self):
        """Dynamically rotates the view by 90 about y."""
        # return self._instance.ViewRotYPlusNinety
        raise NotImplemented

    def view_rw_shading(self):
        """Sets the current display subsystem to use renderware."""
        # return self._instance.ViewRwShading
        raise NotImplemented

    def view_translate(self):
        """Translates the view."""
        # return self._instance.ViewTranslate
        raise NotImplemented

    def view_translateminusx(self):
        """Dynamically shifts the view left."""
        # return self._instance.ViewTranslateminusx
        raise NotImplemented

    def view_translateminusy(self):
        """Dynamically shifts the view down."""
        # return self._instance.ViewTranslateminusy
        raise NotImplemented

    def view_translateplusx(self):
        """Dynamically shifts the view right."""
        # return self._instance.ViewTranslateplusx
        raise NotImplemented

    def view_translateplusy(self):
        """Dynamically shifts the view up."""
        # return self._instance.ViewTranslateplusy
        raise NotImplemented

    def view_zoomin(self):
        """Zooms the current view in by a factor of 20%."""
        # return self._instance.ViewZoomin
        raise NotImplemented

    def view_zoomout(self):
        """Zooms the current view out by a factor of 20%."""
        # return self._instance.ViewZoomout
        raise NotImplemented

    def view_zoomto(self):
        """Zooms the view to the selected box."""
        # return self._instance.ViewZoomto
        raise NotImplemented

    def view_zoom_to(self):
        """Zooms to the specified region."""
        # return self._instance.ViewZoomTo2
        raise NotImplemented

    def view_zoomtofit(self):
        """Zooms the currently active view to fit the screen."""
        # return self._instance.ViewZoomtofit2
        raise NotImplemented

    def view_zoom_to_selection(self):
        """Zooms the display to the selection."""
        # return self._instance.ViewZoomToSelection
        raise NotImplemented

    def window_redraw(self):
        """Redraws the current window."""
        # return self._instance.WindowRedraw
        raise NotImplemented

    # @property
    def summary_info(self, field_id):
        # http://help.solidworks.com/2021/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSummInfoField_e.html
        return self._instance.SummaryInfo(field_id)



