# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html
class IModelDoc2:
	def __init__(self, parent=None):
		self._instance = parent

	def active_view(self):
		"""Gets the current active model view in read-only mode.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.ActiveView
		raise NotImplemented

	def configuration_manager(self):
		"""Gets the IConfigurationManager object, which allows access to a configuration in a model."""
		# return self._instance.ConfigurationManager
		raise NotImplemented

	def extension(self):
		"""Gets the IModelDocExtension object, which also allows access to the model document."""
		# return self._instance.Extension
		raise NotImplemented

	def feature_manager(self):
		"""Gets the IFeatureManager object, which allows access to the FeatureManager design tree."""
		# return self._instance.FeatureManager
		raise NotImplemented

	def feature_manager_splitter_position(self):
		"""Splits the FeatureManager design tree and gets or sets the location of the split bar in the FeatureManager design tree panel."""
		# return self._instance.FeatureManagerSplitterPosition
		raise NotImplemented

	def i_active_view(self):
		"""Gets the current active model view in read-only mode.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.IActiveView
		raise NotImplemented

	def i_light_source_property_values(self, i_d):
		"""
		Gets and sets the light source property values.
		:param i_d: Light source ID
		"""
		# return self._instance.ILightSourcePropertyValues(i_d)
		raise NotImplemented

	@property
	def i_material_property_values(self):
		"""Gets or sets a material's properties in the active configuration."""
		return self._instance.IMaterialPropertyValues

	@i_material_property_values.setter
	def i_material_property_values(self, value):
		"""Gets or sets a material's properties in the active configuration."""
		self._instance.IMaterialPropertyValues = value

	@property
	def i_page_setup(self):
		"""Gets the page setup for this document."""
		return self._instance.IPageSetup

	@i_page_setup.setter
	def i_page_setup(self, value):
		"""Gets the page setup for this document."""
		self._instance.IPageSetup = value

	@property
	def i_selection_manager(self):
		"""Gets the ISelectionMgr object for this document, which makes the currently selected object available."""
		return self._instance.ISelectionManager

	@i_selection_manager.setter
	def i_selection_manager(self, value):
		"""Gets the ISelectionMgr object for this document, which makes the currently selected object available."""
		self._instance.ISelectionManager = value

	@property
	def large_assembly_mode(self):
		"""Gets or sets Large Assembly Mode for this document."""
		return self._instance.LargeAssemblyMode

	@large_assembly_mode.setter
	def large_assembly_mode(self, value):
		"""Gets or sets Large Assembly Mode for this document."""
		self._instance.LargeAssemblyMode = value

	@property
	def length_unit(self):
		"""Gets and sets the same LengthUnit value used by IModelDoc2::GetUnits, IModelDoc2::IGetUnits, and IModelDoc2::SetUnits."""
		return self._instance.LengthUnit

	@length_unit.setter
	def length_unit(self, value):
		"""Gets and sets the same LengthUnit value used by IModelDoc2::GetUnits, IModelDoc2::IGetUnits, and IModelDoc2::SetUnits."""
		self._instance.LengthUnit = value

	@property
	def light_source_property_values(self):
		"""Gets and sets the light source property values."""
		return self._instance.LightSourcePropertyValues

	@light_source_property_values.setter
	def light_source_property_values(self, value):
		"""Gets and sets the light source property values."""
		self._instance.LightSourcePropertyValues = value

	@property
	def light_source_user_name(self):
		"""Gets or sets the light source name that is displayed in the SOLIDWORKS user interface."""
		return self._instance.LightSourceUserName

	@light_source_user_name.setter
	def light_source_user_name(self, value):
		"""Gets or sets the light source name that is displayed in the SOLIDWORKS user interface."""
		self._instance.LightSourceUserName = value

	@property
	def material_property_values(self):
		"""Gets or sets a material's properties in the active configuration."""
		return self._instance.MaterialPropertyValues

	@material_property_values.setter
	def material_property_values(self, value):
		"""Gets or sets a material's properties in the active configuration."""
		self._instance.MaterialPropertyValues = value

	@property
	def material_user_name(self):
		"""Gets or sets the material name."""
		return self._instance.MaterialUserName

	@material_user_name.setter
	def material_user_name(self, value):
		"""Gets or sets the material name."""
		self._instance.MaterialUserName = value

	@property
	def model_view_manager(self):
		"""Gets the IModelViewManager object, which allows access to the model view."""
		return self._instance.ModelViewManager

	@model_view_manager.setter
	def model_view_manager(self, value):
		"""Gets the IModelViewManager object, which allows access to the model view."""
		self._instance.ModelViewManager = value

	@property
	def page_setup(self):
		"""Gets the page setup for this document."""
		return self._instance.PageSetup

	@page_setup.setter
	def page_setup(self, value):
		"""Gets the page setup for this document."""
		self._instance.PageSetup = value

	@property
	def printer(self):
		"""Gets or sets the default printer for this document."""
		return self._instance.Printer

	@printer.setter
	def printer(self, value):
		"""Gets or sets the default printer for this document."""
		self._instance.Printer = value

	@property
	def scene_bkg_image_file_name(self):
		"""Controls the image filename used as the current background picture."""
		return self._instance.SceneBkgImageFileName

	@scene_bkg_image_file_name.setter
	def scene_bkg_image_file_name(self, value):
		"""Controls the image filename used as the current background picture."""
		self._instance.SceneBkgImageFileName = value

	@property
	def scene_name(self):
		"""Gets and sets the name of the scene."""
		return self._instance.SceneName

	@scene_name.setter
	def scene_name(self, value):
		"""Gets and sets the name of the scene."""
		self._instance.SceneName = value

	@property
	def scene_user_name(self):
		"""Gets and sets the user name of the scene."""
		return self._instance.SceneUserName

	@scene_user_name.setter
	def scene_user_name(self, value):
		"""Gets and sets the user name of the scene."""
		self._instance.SceneUserName = value

	@property
	def selection_manager(self):
		"""Gets the ISelectionMgr object for this document, which makes the currently selected object available.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.SelectionManager

	@selection_manager.setter
	def selection_manager(self, value):
		"""Gets the ISelectionMgr object for this document, which makes the currently selected object available.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.SelectionManager = value

	@property
	def show_feature_error_dialog(self):
		"""Gets or sets whether to display the feature error dialog."""
		return self._instance.ShowFeatureErrorDialog

	@show_feature_error_dialog.setter
	def show_feature_error_dialog(self, value):
		"""Gets or sets whether to display the feature error dialog."""
		self._instance.ShowFeatureErrorDialog = value

	@property
	def sketch_manager(self):
		"""Gets the sketch manager, which allows access to sketch-creation routines."""
		return self._instance.SketchManager

	@sketch_manager.setter
	def sketch_manager(self, value):
		"""Gets the sketch manager, which allows access to sketch-creation routines."""
		self._instance.SketchManager = value

	@property
	def summary_info(self):
		"""Gets or sets file summary information for the SOLIDWORKS document."""
		return self._instance.SummaryInfo

	@summary_info.setter
	def summary_info(self, value):
		"""Gets or sets file summary information for the SOLIDWORKS document."""
		self._instance.SummaryInfo = value

	@property
	def visible(self):
		"""Gets or sets the visibility of the active document."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets the visibility of the active document."""
		self._instance.Visible = value

	@property
	def activate_selected_feature(self):
		"""Activates the selected feature for editing."""
		return self._instance.ActivateSelectedFeature

	@activate_selected_feature.setter
	def activate_selected_feature(self, value):
		"""Activates the selected feature for editing."""
		self._instance.ActivateSelectedFeature = value

	@property
	def add_configuration(self):
		"""Adds a new configuration to this model document."""
		return self._instance.AddConfiguration3

	@add_configuration.setter
	def add_configuration(self, value):
		"""Adds a new configuration to this model document."""
		self._instance.AddConfiguration3 = value

	@property
	def add_diameter_dimension(self):
		"""Adds a diameter dimension at the specified location for the selected item."""
		return self._instance.AddDiameterDimension2

	@add_diameter_dimension.setter
	def add_diameter_dimension(self, value):
		"""Adds a diameter dimension at the specified location for the selected item."""
		self._instance.AddDiameterDimension2 = value

	@property
	def add_dimension(self):
		"""Creates a display dimension at the specified location for selected entities."""
		return self._instance.AddDimension2

	@add_dimension.setter
	def add_dimension(self, value):
		"""Creates a display dimension at the specified location for selected entities."""
		self._instance.AddDimension2 = value

	@property
	def add_feature_mgr_view(self):
		"""Adds the specified tab to the FeatureManager design tree view."""
		return self._instance.AddFeatureMgrView3

	@add_feature_mgr_view.setter
	def add_feature_mgr_view(self, value):
		"""Adds the specified tab to the FeatureManager design tree view."""
		self._instance.AddFeatureMgrView3 = value

	@property
	def add_horizontal_dimension(self):
		"""Creates a horizontal dimension for the currently selected entities at the specified location."""
		return self._instance.AddHorizontalDimension2

	@add_horizontal_dimension.setter
	def add_horizontal_dimension(self, value):
		"""Creates a horizontal dimension for the currently selected entities at the specified location."""
		self._instance.AddHorizontalDimension2 = value

	@property
	def add_ins(self):
		"""Displays the Add-In Manager dialog box."""
		return self._instance.AddIns

	@add_ins.setter
	def add_ins(self, value):
		"""Displays the Add-In Manager dialog box."""
		self._instance.AddIns = value

	@property
	def add_light_source(self):
		"""Adds a type of light source to a scene with the specified names."""
		return self._instance.AddLightSource

	@add_light_source.setter
	def add_light_source(self, value):
		"""Adds a type of light source to a scene with the specified names."""
		self._instance.AddLightSource = value

	@property
	def add_light_source_ext_property(self):
		"""Stores a float, string, or integer value for the light source."""
		return self._instance.AddLightSourceExtProperty

	@add_light_source_ext_property.setter
	def add_light_source_ext_property(self, value):
		"""Stores a float, string, or integer value for the light source."""
		self._instance.AddLightSourceExtProperty = value

	@property
	def add_light_to_scene(self):
		"""Adds a light source to a scene."""
		return self._instance.AddLightToScene

	@add_light_to_scene.setter
	def add_light_to_scene(self, value):
		"""Adds a light source to a scene."""
		self._instance.AddLightToScene = value

	@property
	def add_loft_section(self):
		"""Adds a loft section to a blend feature."""
		return self._instance.AddLoftSection

	@add_loft_section.setter
	def add_loft_section(self, value):
		"""Adds a loft section to a blend feature."""
		self._instance.AddLoftSection = value

	@property
	def add_property_extension(self):
		"""Adds a property extension to this model."""
		return self._instance.AddPropertyExtension

	@add_property_extension.setter
	def add_property_extension(self, value):
		"""Adds a property extension to this model."""
		self._instance.AddPropertyExtension = value

	@property
	def add_radial_dimension(self):
		"""Adds a radial dimension at the specified location for the selected item."""
		return self._instance.AddRadialDimension2

	@add_radial_dimension.setter
	def add_radial_dimension(self, value):
		"""Adds a radial dimension at the specified location for the selected item."""
		self._instance.AddRadialDimension2 = value

	@property
	def add_scene_ext_property(self):
		"""Stores a float, string, or integer value for a scene."""
		return self._instance.AddSceneExtProperty

	@add_scene_ext_property.setter
	def add_scene_ext_property(self, value):
		"""Stores a float, string, or integer value for a scene."""
		self._instance.AddSceneExtProperty = value

	@property
	def add_vertical_dimension(self):
		"""Creates a vertical dimension for the currently selected entities at the specified location."""
		return self._instance.AddVerticalDimension2

	@add_vertical_dimension.setter
	def add_vertical_dimension(self, value):
		"""Creates a vertical dimension for the currently selected entities at the specified location."""
		self._instance.AddVerticalDimension2 = value

	@property
	def align_ordinate(self):
		"""Aligns the selected group of ordinate dimensions."""
		return self._instance.AlignOrdinate

	@align_ordinate.setter
	def align_ordinate(self, value):
		"""Aligns the selected group of ordinate dimensions."""
		self._instance.AlignOrdinate = value

	@property
	def align_parallel_dimensions(self):
		"""Aligns the selected linear dimensions in a parallel fashion."""
		return self._instance.AlignParallelDimensions

	@align_parallel_dimensions.setter
	def align_parallel_dimensions(self, value):
		"""Aligns the selected linear dimensions in a parallel fashion."""
		self._instance.AlignParallelDimensions = value

	@property
	def blank_ref_geom(self):
		"""Hides the selected reference geometry in the graphics window."""
		return self._instance.BlankRefGeom

	@blank_ref_geom.setter
	def blank_ref_geom(self, value):
		"""Hides the selected reference geometry in the graphics window."""
		self._instance.BlankRefGeom = value

	@property
	def blank_sketch(self):
		"""Hides the selected sketches."""
		return self._instance.BlankSketch

	@blank_sketch.setter
	def blank_sketch(self, value):
		"""Hides the selected sketches."""
		self._instance.BlankSketch = value

	@property
	def break_dimension_alignment(self):
		"""Breaks the association of any selected dimensions belonging to an alignment group (parallel or collinear)."""
		return self._instance.BreakDimensionAlignment

	@break_dimension_alignment.setter
	def break_dimension_alignment(self, value):
		"""Breaks the association of any selected dimensions belonging to an alignment group (parallel or collinear)."""
		self._instance.BreakDimensionAlignment = value

	@property
	def clear_selection(self):
		"""Clears the selection list."""
		return self._instance.ClearSelection2

	@clear_selection.setter
	def clear_selection(self, value):
		"""Clears the selection list."""
		self._instance.ClearSelection2 = value

	@property
	def clear_undo_list(self):
		"""Clears the undo list for this model document."""
		return self._instance.ClearUndoList

	@clear_undo_list.setter
	def clear_undo_list(self, value):
		"""Clears the undo list for this model document."""
		self._instance.ClearUndoList = value

	@property
	def close(self):
		"""Not implemented. Use ISldWorks::CloseDoc."""
		return self._instance.Close

	@close.setter
	def close(self, value):
		"""Not implemented. Use ISldWorks::CloseDoc."""
		self._instance.Close = value

	@property
	def close_family_table(self):
		"""Closes the design table currently being edited."""
		return self._instance.CloseFamilyTable

	@close_family_table.setter
	def close_family_table(self, value):
		"""Closes the design table currently being edited."""
		self._instance.CloseFamilyTable = value

	@property
	def close_print_preview(self):
		"""Closes the currently displayed Print Preview page for this document."""
		return self._instance.ClosePrintPreview

	@close_print_preview.setter
	def close_print_preview(self, value):
		"""Closes the currently displayed Print Preview page for this document."""
		self._instance.ClosePrintPreview = value

	@property
	def closest_distance(self):
		"""Calculates the minimum distance between the specified geometric objects."""
		return self._instance.ClosestDistance

	@closest_distance.setter
	def closest_distance(self, value):
		"""Calculates the minimum distance between the specified geometric objects."""
		self._instance.ClosestDistance = value

	@property
	def create_arc_by_center(self):
		"""Creates an arc by center in this model document."""
		return self._instance.CreateArcByCenter

	@create_arc_by_center.setter
	def create_arc_by_center(self, value):
		"""Creates an arc by center in this model document."""
		self._instance.CreateArcByCenter = value

	@property
	def create_center_line_v_b(self):
		"""Creates a center line from P1 to P2 and can be used in Visual Basic for Applications (VBA) and other forms of Basic that do not support SafeArrays."""
		return self._instance.CreateCenterLineVB

	@create_center_line_v_b.setter
	def create_center_line_v_b(self, value):
		"""Creates a center line from P1 to P2 and can be used in Visual Basic for Applications (VBA) and other forms of Basic that do not support SafeArrays."""
		self._instance.CreateCenterLineVB = value

	@property
	def create_clipped_splines(self):
		"""Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch."""
		return self._instance.CreateClippedSplines

	@create_clipped_splines.setter
	def create_clipped_splines(self, value):
		"""Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch."""
		self._instance.CreateClippedSplines = value

	@property
	def create_group(self):
		"""Creates an annotation group from the currently selected annotations."""
		return self._instance.CreateGroup

	@create_group.setter
	def create_group(self, value):
		"""Creates an annotation group from the currently selected annotations."""
		self._instance.CreateGroup = value

	@property
	def de_activate_feature_mgr_view(self):
		"""Deactivates a tab in the FeatureManager design tree view."""
		return self._instance.DeActivateFeatureMgrView

	@de_activate_feature_mgr_view.setter
	def de_activate_feature_mgr_view(self, value):
		"""Deactivates a tab in the FeatureManager design tree view."""
		self._instance.DeActivateFeatureMgrView = value

	@property
	def debug_check_iges_geom(self):
		"""Dumps a IGES geometry check."""
		return self._instance.DebugCheckIgesGeom

	@debug_check_iges_geom.setter
	def debug_check_iges_geom(self, value):
		"""Dumps a IGES geometry check."""
		self._instance.DebugCheckIgesGeom = value

	@property
	def delete_all_relations(self):
		"""Deletes all existing relations."""
		return self._instance.DeleteAllRelations

	@delete_all_relations.setter
	def delete_all_relations(self, value):
		"""Deletes all existing relations."""
		self._instance.DeleteAllRelations = value

	@property
	def delete_bend_table(self):
		"""Deletes a bend table."""
		return self._instance.DeleteBendTable

	@delete_bend_table.setter
	def delete_bend_table(self, value):
		"""Deletes a bend table."""
		self._instance.DeleteBendTable = value

	@property
	def delete_bkg_image(self):
		"""Deletes any background image."""
		return self._instance.DeleteBkgImage

	@delete_bkg_image.setter
	def delete_bkg_image(self, value):
		"""Deletes any background image."""
		self._instance.DeleteBkgImage = value

	@property
	def delete_configuration(self):
		"""Deletes a configuration."""
		return self._instance.DeleteConfiguration2

	@delete_configuration.setter
	def delete_configuration(self, value):
		"""Deletes a configuration."""
		self._instance.DeleteConfiguration2 = value

	@property
	def delete_design_table(self):
		"""Deletes the design table for this document, if one exists."""
		return self._instance.DeleteDesignTable

	@delete_design_table.setter
	def delete_design_table(self, value):
		"""Deletes the design table for this document, if one exists."""
		self._instance.DeleteDesignTable = value

	@property
	def delete_feature_mgr_view(self):
		"""Removes the specified tab in the FeatureManager design tree."""
		return self._instance.DeleteFeatureMgrView

	@delete_feature_mgr_view.setter
	def delete_feature_mgr_view(self, value):
		"""Removes the specified tab in the FeatureManager design tree."""
		self._instance.DeleteFeatureMgrView = value

	@property
	def delete_light_source(self):
		"""Deletes a light source."""
		return self._instance.DeleteLightSource

	@delete_light_source.setter
	def delete_light_source(self, value):
		"""Deletes a light source."""
		self._instance.DeleteLightSource = value

	@property
	def delete_named_view(self):
		"""Deletes the specified model view."""
		return self._instance.DeleteNamedView

	@delete_named_view.setter
	def delete_named_view(self, value):
		"""Deletes the specified model view."""
		self._instance.DeleteNamedView = value

	@property
	def derive_sketch(self):
		"""Creates a derived sketch."""
		return self._instance.DeriveSketch

	@derive_sketch.setter
	def derive_sketch(self, value):
		"""Creates a derived sketch."""
		self._instance.DeriveSketch = value

	@property
	def de_select_by_i_d(self):
		"""Removes the selected object from the selection list."""
		return self._instance.DeSelectByID

	@de_select_by_i_d.setter
	def de_select_by_i_d(self, value):
		"""Removes the selected object from the selection list."""
		self._instance.DeSelectByID = value

	@property
	def dim_preferences(self):
		"""Sets dimension preferences."""
		return self._instance.DimPreferences

	@dim_preferences.setter
	def dim_preferences(self, value):
		"""Sets dimension preferences."""
		self._instance.DimPreferences = value

	@property
	def dissolve_library_feature(self):
		"""Dissolves the selected library features."""
		return self._instance.DissolveLibraryFeature

	@dissolve_library_feature.setter
	def dissolve_library_feature(self, value):
		"""Dissolves the selected library features."""
		self._instance.DissolveLibraryFeature = value

	@property
	def dissolve_sketch_text(self):
		"""Dissolves sketch text."""
		return self._instance.DissolveSketchText

	@dissolve_sketch_text.setter
	def dissolve_sketch_text(self, value):
		"""Dissolves sketch text."""
		self._instance.DissolveSketchText = value

	@property
	def drag_to(self):
		"""Drags the specified end point."""
		return self._instance.DragTo

	@drag_to.setter
	def drag_to(self, value):
		"""Drags the specified end point."""
		self._instance.DragTo = value

	@property
	def draw_light_icons(self):
		"""Draws any visible light icons."""
		return self._instance.DrawLightIcons

	@draw_light_icons.setter
	def draw_light_icons(self, value):
		"""Draws any visible light icons."""
		self._instance.DrawLightIcons = value

	@property
	def edit_configuration(self):
		"""Edits the specified configuration."""
		return self._instance.EditConfiguration3

	@edit_configuration.setter
	def edit_configuration(self, value):
		"""Edits the specified configuration."""
		self._instance.EditConfiguration3 = value

	@property
	def edit_copy(self):
		"""Copies the currently selected items and places them in the clipboard."""
		return self._instance.EditCopy

	@edit_copy.setter
	def edit_copy(self, value):
		"""Copies the currently selected items and places them in the clipboard."""
		self._instance.EditCopy = value

	@property
	def edit_cut(self):
		"""Cuts the currently selected items and places them on the Microsoft Windows Clipboard."""
		return self._instance.EditCut

	@edit_cut.setter
	def edit_cut(self, value):
		"""Cuts the currently selected items and places them on the Microsoft Windows Clipboard."""
		self._instance.EditCut = value

	@property
	def edit_datum_target_symbol(self):
		"""Edits a datum target symbol."""
		return self._instance.EditDatumTargetSymbol

	@edit_datum_target_symbol.setter
	def edit_datum_target_symbol(self, value):
		"""Edits a datum target symbol."""
		self._instance.EditDatumTargetSymbol = value

	@property
	def edit_delete(self):
		"""Deletes the selected items."""
		return self._instance.EditDelete

	@edit_delete.setter
	def edit_delete(self, value):
		"""Deletes the selected items."""
		self._instance.EditDelete = value

	@property
	def edit_ordinate(self):
		"""Puts the currently selected ordinate dimension into edit mode so you could add more ordinate dimensions to this group."""
		return self._instance.EditOrdinate

	@edit_ordinate.setter
	def edit_ordinate(self, value):
		"""Puts the currently selected ordinate dimension into edit mode so you could add more ordinate dimensions to this group."""
		self._instance.EditOrdinate = value

	@property
	def edit_rebuild(self):
		"""Rebuilds only those features that need to be rebuilt in the active configuration in the model."""
		return self._instance.EditRebuild3

	@edit_rebuild.setter
	def edit_rebuild(self, value):
		"""Rebuilds only those features that need to be rebuilt in the active configuration in the model."""
		self._instance.EditRebuild3 = value

	@property
	def edit_redo(self):
		"""Repeats the specified number of actions in this SOLIDWORKS session."""
		return self._instance.EditRedo2

	@edit_redo.setter
	def edit_redo(self, value):
		"""Repeats the specified number of actions in this SOLIDWORKS session."""
		self._instance.EditRedo2 = value

	@property
	def edit_route(self):
		"""Makes the last selected route the active route."""
		return self._instance.EditRoute

	@edit_route.setter
	def edit_route(self, value):
		"""Makes the last selected route the active route."""
		self._instance.EditRoute = value

	@property
	def edit_seed_feat(self):
		"""Gets the pattern seed feature, based on the selected face, and displays the Edit Definition dialog for that feature."""
		return self._instance.EditSeedFeat

	@edit_seed_feat.setter
	def edit_seed_feat(self, value):
		"""Gets the pattern seed feature, based on the selected face, and displays the Edit Definition dialog for that feature."""
		self._instance.EditSeedFeat = value

	@property
	def edit_sketch(self):
		"""Allows the currently selected sketch to be edited."""
		return self._instance.EditSketch

	@edit_sketch.setter
	def edit_sketch(self, value):
		"""Allows the currently selected sketch to be edited."""
		self._instance.EditSketch = value

	@property
	def edit_sketch_or_single_sketch_feature(self):
		"""Edits a selected sketch or feature sketch."""
		return self._instance.EditSketchOrSingleSketchFeature

	@edit_sketch_or_single_sketch_feature.setter
	def edit_sketch_or_single_sketch_feature(self, value):
		"""Edits a selected sketch or feature sketch."""
		self._instance.EditSketchOrSingleSketchFeature = value

	@property
	def edit_suppress(self):
		"""Suppresses the selected feature, the selected component, or the owning feature of the selected face."""
		return self._instance.EditSuppress2

	@edit_suppress.setter
	def edit_suppress(self, value):
		"""Suppresses the selected feature, the selected component, or the owning feature of the selected face."""
		self._instance.EditSuppress2 = value

	@property
	def edit_undo(self):
		"""Undoes the specified number of actions in the active SOLIDWORKS session."""
		return self._instance.EditUndo2

	@edit_undo.setter
	def edit_undo(self, value):
		"""Undoes the specified number of actions in the active SOLIDWORKS session."""
		self._instance.EditUndo2 = value

	@property
	def edit_unsuppress(self):
		"""Unsuppresses the selected feature or component."""
		return self._instance.EditUnsuppress2

	@edit_unsuppress.setter
	def edit_unsuppress(self, value):
		"""Unsuppresses the selected feature or component."""
		self._instance.EditUnsuppress2 = value

	@property
	def edit_unsuppress_dependent(self):
		"""Unsuppresses the selected feature or component and their dependents."""
		return self._instance.EditUnsuppressDependent2

	@edit_unsuppress_dependent.setter
	def edit_unsuppress_dependent(self, value):
		"""Unsuppresses the selected feature or component and their dependents."""
		self._instance.EditUnsuppressDependent2 = value

	@property
	def entity_properties(self):
		"""Displays the Properties dialog for the selected edge or face."""
		return self._instance.EntityProperties

	@entity_properties.setter
	def entity_properties(self, value):
		"""Displays the Properties dialog for the selected edge or face."""
		self._instance.EntityProperties = value

	@property
	def enum_model_views(self):
		"""Gets the model views enumeration in this document."""
		return self._instance.EnumModelViews

	@enum_model_views.setter
	def enum_model_views(self, value):
		"""Gets the model views enumeration in this document."""
		self._instance.EnumModelViews = value

	@property
	def feat_edit(self):
		"""Puts the current feature into edit mode."""
		return self._instance.FeatEdit

	@feat_edit.setter
	def feat_edit(self, value):
		"""Puts the current feature into edit mode."""
		self._instance.FeatEdit = value

	@property
	def feat_edit_def(self):
		"""Displays the Feature Definition dialog and lets the user edit the values."""
		return self._instance.FeatEditDef

	@feat_edit_def.setter
	def feat_edit_def(self, value):
		"""Displays the Feature Definition dialog and lets the user edit the values."""
		self._instance.FeatEditDef = value

	@property
	def feature_by_position_reverse(self):
		"""Gets the nth from last feature in the document."""
		return self._instance.FeatureByPositionReverse

	@feature_by_position_reverse.setter
	def feature_by_position_reverse(self, value):
		"""Gets the nth from last feature in the document."""
		self._instance.FeatureByPositionReverse = value

	@property
	def feature_chamfer(self):
		"""Creates a chamfer feature."""
		return self._instance.FeatureChamfer

	@feature_chamfer.setter
	def feature_chamfer(self, value):
		"""Creates a chamfer feature."""
		self._instance.FeatureChamfer = value

	@property
	def feature_reference_curve(self):
		"""Creates a reference curve feature from an array of curves."""
		return self._instance.FeatureReferenceCurve

	@feature_reference_curve.setter
	def feature_reference_curve(self, value):
		"""Creates a reference curve feature from an array of curves."""
		self._instance.FeatureReferenceCurve = value

	@property
	def file_summary_info(self):
		"""Displays the File Summary Information dialog box for this file."""
		return self._instance.FileSummaryInfo

	@file_summary_info.setter
	def file_summary_info(self, value):
		"""Displays the File Summary Information dialog box for this file."""
		self._instance.FileSummaryInfo = value

	@property
	def first_feature(self):
		"""Gets the first feature in the document."""
		return self._instance.FirstFeature

	@first_feature.setter
	def first_feature(self, value):
		"""Gets the first feature in the document."""
		self._instance.FirstFeature = value

	@property
	def font_bold(self):
		"""Enables or disables bold font style in the selected notes, dimensions, and GTols."""
		return self._instance.FontBold

	@font_bold.setter
	def font_bold(self, value):
		"""Enables or disables bold font style in the selected notes, dimensions, and GTols."""
		self._instance.FontBold = value

	@property
	def font_face(self):
		"""Changes the font face in the selected notes, dimensions, and GTols."""
		return self._instance.FontFace

	@font_face.setter
	def font_face(self, value):
		"""Changes the font face in the selected notes, dimensions, and GTols."""
		self._instance.FontFace = value

	@property
	def font_italic(self):
		"""Enables or disables italic font style in the selected notes, dimensions, and GTols."""
		return self._instance.FontItalic

	@font_italic.setter
	def font_italic(self, value):
		"""Enables or disables italic font style in the selected notes, dimensions, and GTols."""
		self._instance.FontItalic = value

	@property
	def font_points(self):
		"""Changes the font height (specified in points) in the selected notes, dimensions, and GTols."""
		return self._instance.FontPoints

	@font_points.setter
	def font_points(self, value):
		"""Changes the font height (specified in points) in the selected notes, dimensions, and GTols."""
		self._instance.FontPoints = value

	@property
	def font_underline(self):
		"""Enables or disables underlining the selected notes, dimensions, and GTols."""
		return self._instance.FontUnderline

	@font_underline.setter
	def font_underline(self, value):
		"""Enables or disables underlining the selected notes, dimensions, and GTols."""
		self._instance.FontUnderline = value

	@property
	def font_units(self):
		"""Changes font height (specified in current system units) in the selected notes, dimensions, and GTols."""
		return self._instance.FontUnits

	@font_units.setter
	def font_units(self, value):
		"""Changes font height (specified in current system units) in the selected notes, dimensions, and GTols."""
		self._instance.FontUnits = value

	@property
	def force_rebuild(self):
		"""Forces a rebuild of all features in the active configuration in the model."""
		return self._instance.ForceRebuild3

	@force_rebuild.setter
	def force_rebuild(self, value):
		"""Forces a rebuild of all features in the active configuration in the model."""
		self._instance.ForceRebuild3 = value

	@property
	def force_release_locks(self):
		"""Releases the locks that a file system places on a file when it is opened and detaches that file from the file system."""
		return self._instance.ForceReleaseLocks

	@force_release_locks.setter
	def force_release_locks(self, value):
		"""Releases the locks that a file system places on a file when it is opened and detaches that file from the file system."""
		self._instance.ForceReleaseLocks = value

	@property
	def get_add_to_d_b(self):
		"""Gets whether entities are added directly to the SOLIDWORKS database."""
		return self._instance.GetAddToDB

	@get_add_to_d_b.setter
	def get_add_to_d_b(self, value):
		"""Gets whether entities are added directly to the SOLIDWORKS database."""
		self._instance.GetAddToDB = value

	@property
	def get_ambient_light_properties(self):
		"""Gets the ambient light properties for this model document."""
		return self._instance.GetAmbientLightProperties

	@get_ambient_light_properties.setter
	def get_ambient_light_properties(self, value):
		"""Gets the ambient light properties for this model document."""
		self._instance.GetAmbientLightProperties = value

	@property
	def get_angular_units(self):
		"""Gets the current angular unit settings."""
		return self._instance.GetAngularUnits

	@get_angular_units.setter
	def get_angular_units(self, value):
		"""Gets the current angular unit settings."""
		self._instance.GetAngularUnits = value

	@property
	def get_arc_centers_displayed(self):
		"""Gets whether the arc centers are displayed."""
		return self._instance.GetArcCentersDisplayed

	@get_arc_centers_displayed.setter
	def get_arc_centers_displayed(self, value):
		"""Gets whether the arc centers are displayed."""
		self._instance.GetArcCentersDisplayed = value

	@property
	def get_bend_state(self):
		"""Gets the current bend state of a sheet metal part."""
		return self._instance.GetBendState

	@get_bend_state.setter
	def get_bend_state(self, value):
		"""Gets the current bend state of a sheet metal part."""
		self._instance.GetBendState = value

	@property
	def get_blocking_state(self):
		"""Gets the current value of the SOLIDWORKS blocking state, within the range of values accessible by IModelDoc2::SetBlockingState."""
		return self._instance.GetBlockingState

	@get_blocking_state.setter
	def get_blocking_state(self, value):
		"""Gets the current value of the SOLIDWORKS blocking state, within the range of values accessible by IModelDoc2::SetBlockingState."""
		self._instance.GetBlockingState = value

	@property
	def get_configuration_by_name(self):
		"""Gets the specified configuration."""
		return self._instance.GetConfigurationByName

	@get_configuration_by_name.setter
	def get_configuration_by_name(self, value):
		"""Gets the specified configuration."""
		self._instance.GetConfigurationByName = value

	@property
	def get_configuration_count(self):
		"""Gets the number of configurations."""
		return self._instance.GetConfigurationCount

	@get_configuration_count.setter
	def get_configuration_count(self, value):
		"""Gets the number of configurations."""
		self._instance.GetConfigurationCount = value

	@property
	def get_configuration_names(self):
		"""Gets the names of the configurations in this document."""
		return self._instance.GetConfigurationNames

	@get_configuration_names.setter
	def get_configuration_names(self, value):
		"""Gets the names of the configurations in this document."""
		self._instance.GetConfigurationNames = value

	@property
	def get_consider_leaders_as_lines(self):
		"""Gets whether the display data of a leader is included as lines when the lines are retrieved from a view or annotation in this document."""
		return self._instance.GetConsiderLeadersAsLines

	@get_consider_leaders_as_lines.setter
	def get_consider_leaders_as_lines(self, value):
		"""Gets whether the display data of a leader is included as lines when the lines are retrieved from a view or annotation in this document."""
		self._instance.GetConsiderLeadersAsLines = value

	@property
	def get_current_coordinate_system_name(self):
		"""Gets the name of the current coordinate system or an empty string for the default coordinate system."""
		return self._instance.GetCurrentCoordinateSystemName

	@get_current_coordinate_system_name.setter
	def get_current_coordinate_system_name(self, value):
		"""Gets the name of the current coordinate system or an empty string for the default coordinate system."""
		self._instance.GetCurrentCoordinateSystemName = value

	@property
	def get_default_text_height(self):
		"""Gets the default text height in use for this document."""
		return self._instance.GetDefaultTextHeight

	@get_default_text_height.setter
	def get_default_text_height(self, value):
		"""Gets the default text height in use for this document."""
		self._instance.GetDefaultTextHeight = value

	@property
	def get_design_table(self):
		"""Gets the design table associated with this part or assembly document."""
		return self._instance.GetDesignTable

	@get_design_table.setter
	def get_design_table(self, value):
		"""Gets the design table associated with this part or assembly document."""
		self._instance.GetDesignTable = value

	@property
	def get_direction_light_properties(self):
		"""Gets the directional light properties."""
		return self._instance.GetDirectionLightProperties

	@get_direction_light_properties.setter
	def get_direction_light_properties(self, value):
		"""Gets the directional light properties."""
		self._instance.GetDirectionLightProperties = value

	@property
	def get_display_when_added(self):
		"""Gets whether new sketch entities are displayed when created."""
		return self._instance.GetDisplayWhenAdded

	@get_display_when_added.setter
	def get_display_when_added(self, value):
		"""Gets whether new sketch entities are displayed when created."""
		self._instance.GetDisplayWhenAdded = value

	@property
	def get_entity_name(self):
		"""Gets the name of the specified face, edge, or vertex."""
		return self._instance.GetEntityName

	@get_entity_name.setter
	def get_entity_name(self, value):
		"""Gets the name of the specified face, edge, or vertex."""
		self._instance.GetEntityName = value

	@property
	def get_equation_mgr(self):
		"""Gets the equation manager."""
		return self._instance.GetEquationMgr

	@get_equation_mgr.setter
	def get_equation_mgr(self, value):
		"""Gets the equation manager."""
		self._instance.GetEquationMgr = value

	@property
	def get_external_reference_name(self):
		"""Gets the name of the externally referenced document (in the case of a join or mirrored part)."""
		return self._instance.GetExternalReferenceName

	@get_external_reference_name.setter
	def get_external_reference_name(self, value):
		"""Gets the name of the externally referenced document (in the case of a join or mirrored part)."""
		self._instance.GetExternalReferenceName = value

	@property
	def get_feature_count(self):
		"""Gets the number of features in this document."""
		return self._instance.GetFeatureCount

	@get_feature_count.setter
	def get_feature_count(self, value):
		"""Gets the number of features in this document."""
		self._instance.GetFeatureCount = value

	@property
	def get_feature_manager_width(self):
		"""Gets the width of the FeatureManager design tree."""
		return self._instance.GetFeatureManagerWidth

	@get_feature_manager_width.setter
	def get_feature_manager_width(self, value):
		"""Gets the width of the FeatureManager design tree."""
		self._instance.GetFeatureManagerWidth = value

	@property
	def get_first_annotation(self):
		"""Gets the first annotation in the model."""
		return self._instance.GetFirstAnnotation2

	@get_first_annotation.setter
	def get_first_annotation(self, value):
		"""Gets the first annotation in the model."""
		self._instance.GetFirstAnnotation2 = value

	@property
	def get_first_model_view(self):
		"""Gets the first view in a model document."""
		return self._instance.GetFirstModelView

	@get_first_model_view.setter
	def get_first_model_view(self, value):
		"""Gets the first view in a model document."""
		self._instance.GetFirstModelView = value

	@property
	def get_grid_settings(self):
		"""Gets the current grid settings."""
		return self._instance.GetGridSettings

	@get_grid_settings.setter
	def get_grid_settings(self, value):
		"""Gets the current grid settings."""
		self._instance.GetGridSettings = value

	@property
	def get_layer_manager(self):
		"""Gets the layer manager for the current drawing document."""
		return self._instance.GetLayerManager

	@get_layer_manager.setter
	def get_layer_manager(self, value):
		"""Gets the layer manager for the current drawing document."""
		self._instance.GetLayerManager = value

	@property
	def get_light_source_count(self):
		"""Gets the number of light sources."""
		return self._instance.GetLightSourceCount

	@get_light_source_count.setter
	def get_light_source_count(self, value):
		"""Gets the number of light sources."""
		self._instance.GetLightSourceCount = value

	@property
	def get_light_source_ext_property(self):
		"""Gets a float, string, or integer value stored for the light source."""
		return self._instance.GetLightSourceExtProperty

	@get_light_source_ext_property.setter
	def get_light_source_ext_property(self, value):
		"""Gets a float, string, or integer value stored for the light source."""
		self._instance.GetLightSourceExtProperty = value

	@property
	def get_light_source_id_from_name(self):
		"""Gets the ID of the specified light source."""
		return self._instance.GetLightSourceIdFromName

	@get_light_source_id_from_name.setter
	def get_light_source_id_from_name(self, value):
		"""Gets the ID of the specified light source."""
		self._instance.GetLightSourceIdFromName = value

	@property
	def get_light_source_name(self):
		"""Gets the name of a light source used internally by the SOLIDWORKS application."""
		return self._instance.GetLightSourceName

	@get_light_source_name.setter
	def get_light_source_name(self, value):
		"""Gets the name of a light source used internally by the SOLIDWORKS application."""
		self._instance.GetLightSourceName = value

	@property
	def get_line_count(self):
		"""Gets the number of lines in the current sketch."""
		return self._instance.GetLineCount

	@get_line_count.setter
	def get_line_count(self, value):
		"""Gets the number of lines in the current sketch."""
		self._instance.GetLineCount = value

	@property
	def get_lines(self):
		"""Gets all of the lines in the current sketch."""
		return self._instance.GetLines

	@get_lines.setter
	def get_lines(self, value):
		"""Gets all of the lines in the current sketch."""
		self._instance.GetLines = value

	@property
	def get_model_view_names(self):
		"""Gets a list containing the names of each model view in this document."""
		return self._instance.GetModelViewNames

	@get_model_view_names.setter
	def get_model_view_names(self, value):
		"""Gets a list containing the names of each model view in this document."""
		self._instance.GetModelViewNames = value

	@property
	def get_next(self):
		"""Gets the next document in the current SOLIDWORKS session."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next document in the current SOLIDWORKS session."""
		self._instance.GetNext = value

	@property
	def get_num_dependencies(self):
		"""Gets the number of strings returned by IModelDoc2::GetDependencies2."""
		return self._instance.GetNumDependencies

	@get_num_dependencies.setter
	def get_num_dependencies(self, value):
		"""Gets the number of strings returned by IModelDoc2::GetDependencies2."""
		self._instance.GetNumDependencies = value

	@property
	def get_path_name(self):
		"""Gets the full path name for this document, including the file name."""
		return self._instance.GetPathName

	@get_path_name.setter
	def get_path_name(self, value):
		"""Gets the full path name for this document, including the file name."""
		self._instance.GetPathName = value

	@property
	def get_point_light_properties(self):
		"""Gets point light properties."""
		return self._instance.GetPointLightProperties

	@get_point_light_properties.setter
	def get_point_light_properties(self, value):
		"""Gets point light properties."""
		self._instance.GetPointLightProperties = value

	@property
	def get_popup_menu_mode(self):
		"""Gets the current pop-up menu mode."""
		return self._instance.GetPopupMenuMode

	@get_popup_menu_mode.setter
	def get_popup_menu_mode(self, value):
		"""Gets the current pop-up menu mode."""
		self._instance.GetPopupMenuMode = value

	@property
	def get_property_extension(self):
		"""Gets the specified property extension on this model."""
		return self._instance.GetPropertyExtension

	@get_property_extension.setter
	def get_property_extension(self, value):
		"""Gets the specified property extension on this model."""
		self._instance.GetPropertyExtension = value

	@property
	def get_ray_intersections_points(self):
		"""Gets the intersection point information generated by IModelDoc2::RayIntersections."""
		return self._instance.GetRayIntersectionsPoints

	@get_ray_intersections_points.setter
	def get_ray_intersections_points(self, value):
		"""Gets the intersection point information generated by IModelDoc2::RayIntersections."""
		self._instance.GetRayIntersectionsPoints = value

	@property
	def get_ray_intersections_topology(self):
		"""Gets the topology intersections generated by IModelDoc2::RayIntersections."""
		return self._instance.GetRayIntersectionsTopology

	@get_ray_intersections_topology.setter
	def get_ray_intersections_topology(self, value):
		"""Gets the topology intersections generated by IModelDoc2::RayIntersections."""
		self._instance.GetRayIntersectionsTopology = value

	@property
	def get_save_flag(self):
		"""Gets whether the document is currently dirty and needs to be saved."""
		return self._instance.GetSaveFlag

	@get_save_flag.setter
	def get_save_flag(self, value):
		"""Gets whether the document is currently dirty and needs to be saved."""
		self._instance.GetSaveFlag = value

	@property
	def get_scene_bkg_d_i_b(self):
		"""Gets background image as a LPDIBSECTION."""
		return self._instance.GetSceneBkgDIB

	@get_scene_bkg_d_i_b.setter
	def get_scene_bkg_d_i_b(self, value):
		"""Gets background image as a LPDIBSECTION."""
		self._instance.GetSceneBkgDIB = value

	@property
	def get_scene_ext_property(self):
		"""Gets a float, string, or integer value stored for the scene."""
		return self._instance.GetSceneExtProperty

	@get_scene_ext_property.setter
	def get_scene_ext_property(self, value):
		"""Gets a float, string, or integer value stored for the scene."""
		self._instance.GetSceneExtProperty = value

	@property
	def get_spotlight_properties(self):
		"""Gets the spotlight properties."""
		return self._instance.GetSpotlightProperties

	@get_spotlight_properties.setter
	def get_spotlight_properties(self, value):
		"""Gets the spotlight properties."""
		self._instance.GetSpotlightProperties = value

	@property
	def get_standard_view_rotation(self):
		"""Gets the specified view orientation matrix with respect to the Front view."""
		return self._instance.GetStandardViewRotation

	@get_standard_view_rotation.setter
	def get_standard_view_rotation(self, value):
		"""Gets the specified view orientation matrix with respect to the Front view."""
		self._instance.GetStandardViewRotation = value

	@property
	def get_tessellation_quality(self):
		"""Gets the shaded-display image quality number for the current document."""
		return self._instance.GetTessellationQuality

	@get_tessellation_quality.setter
	def get_tessellation_quality(self, value):
		"""Gets the shaded-display image quality number for the current document."""
		self._instance.GetTessellationQuality = value

	@property
	def get_title(self):
		"""Gets the title of the document that appears in the active window's title bar."""
		return self._instance.GetTitle

	@get_title.setter
	def get_title(self, value):
		"""Gets the title of the document that appears in the active window's title bar."""
		self._instance.GetTitle = value

	@property
	def get_toolbar_visibility(self):
		"""Gets the visibility of a toolbar."""
		return self._instance.GetToolbarVisibility

	@get_toolbar_visibility.setter
	def get_toolbar_visibility(self, value):
		"""Gets the visibility of a toolbar."""
		self._instance.GetToolbarVisibility = value

	@property
	def get_type(self):
		"""Gets the type of the document."""
		return self._instance.GetType

	@get_type.setter
	def get_type(self, value):
		"""Gets the type of the document."""
		self._instance.GetType = value

	@property
	def get_units(self):
		"""Gets the current unit settings, fraction base, fraction value, and significant digits."""
		return self._instance.GetUnits

	@get_units.setter
	def get_units(self, value):
		"""Gets the current unit settings, fraction base, fraction value, and significant digits."""
		self._instance.GetUnits = value

	@property
	def get_update_stamp(self):
		"""Gets the current update stamp for this document."""
		return self._instance.GetUpdateStamp

	@get_update_stamp.setter
	def get_update_stamp(self, value):
		"""Gets the current update stamp for this document."""
		self._instance.GetUpdateStamp = value

	@property
	def get_user_unit(self):
		"""Gets this document's units settings."""
		return self._instance.GetUserUnit

	@get_user_unit.setter
	def get_user_unit(self, value):
		"""Gets this document's units settings."""
		self._instance.GetUserUnit = value

	@property
	def get_visibility_of_construct_planes(self):
		"""Gets whether construction (reference) planes are currently visible."""
		return self._instance.GetVisibilityOfConstructPlanes

	@get_visibility_of_construct_planes.setter
	def get_visibility_of_construct_planes(self, value):
		"""Gets whether construction (reference) planes are currently visible."""
		self._instance.GetVisibilityOfConstructPlanes = value

	@property
	def get_zebra_stripe_data(self):
		"""Gets zebra line data."""
		return self._instance.GetZebraStripeData

	@get_zebra_stripe_data.setter
	def get_zebra_stripe_data(self, value):
		"""Gets zebra line data."""
		self._instance.GetZebraStripeData = value

	@property
	def hide_component(self):
		"""Hides the selected component."""
		return self._instance.HideComponent2

	@hide_component.setter
	def hide_component(self, value):
		"""Hides the selected component."""
		self._instance.HideComponent2 = value

	@property
	def hide_cosmetic_thread(self):
		"""Hides the selected cosmetic thread."""
		return self._instance.HideCosmeticThread

	@hide_cosmetic_thread.setter
	def hide_cosmetic_thread(self, value):
		"""Hides the selected cosmetic thread."""
		self._instance.HideCosmeticThread = value

	@property
	def hide_dimension(self):
		"""Hides the selected dimension in this document."""
		return self._instance.HideDimension

	@hide_dimension.setter
	def hide_dimension(self, value):
		"""Hides the selected dimension in this document."""
		self._instance.HideDimension = value

	@property
	def hide_show_bodies(self):
		"""Sets whether to hide or show the bodies in the model."""
		return self._instance.HideShowBodies

	@hide_show_bodies.setter
	def hide_show_bodies(self, value):
		"""Sets whether to hide or show the bodies in the model."""
		self._instance.HideShowBodies = value

	@property
	def hide_solid_body(self):
		"""Hides the currently selected solid body."""
		return self._instance.HideSolidBody

	@hide_solid_body.setter
	def hide_solid_body(self, value):
		"""Hides the currently selected solid body."""
		self._instance.HideSolidBody = value

	@property
	def i_add_configuration(self):
		"""Adds a new configuration to this model document."""
		return self._instance.IAddConfiguration3

	@i_add_configuration.setter
	def i_add_configuration(self, value):
		"""Adds a new configuration to this model document."""
		self._instance.IAddConfiguration3 = value

	@property
	def i_add_diameter_dimension(self):
		"""Adds a diameter dimension at the specified location for the selected item."""
		return self._instance.IAddDiameterDimension2

	@i_add_diameter_dimension.setter
	def i_add_diameter_dimension(self, value):
		"""Adds a diameter dimension at the specified location for the selected item."""
		self._instance.IAddDiameterDimension2 = value

	@property
	def i_add_horizontal_dimension(self):
		"""Creates a horizontal dimension for the current selected entities at the specified location."""
		return self._instance.IAddHorizontalDimension2

	@i_add_horizontal_dimension.setter
	def i_add_horizontal_dimension(self, value):
		"""Creates a horizontal dimension for the current selected entities at the specified location."""
		self._instance.IAddHorizontalDimension2 = value

	@property
	def i_add_radial_dimension(self):
		"""Adds a radial dimension at the specified location for the selected item."""
		return self._instance.IAddRadialDimension2

	@i_add_radial_dimension.setter
	def i_add_radial_dimension(self, value):
		"""Adds a radial dimension at the specified location for the selected item."""
		self._instance.IAddRadialDimension2 = value

	@property
	def i_add_vertical_dimension(self):
		"""Creates a vertical dimension for the currently selected entities at the specified location."""
		return self._instance.IAddVerticalDimension2

	@i_add_vertical_dimension.setter
	def i_add_vertical_dimension(self, value):
		"""Creates a vertical dimension for the currently selected entities at the specified location."""
		self._instance.IAddVerticalDimension2 = value

	@property
	def i_closest_distance(self):
		"""Calculates the distance and closest points between two geometric objects."""
		return self._instance.IClosestDistance

	@i_closest_distance.setter
	def i_closest_distance(self, value):
		"""Calculates the distance and closest points between two geometric objects."""
		self._instance.IClosestDistance = value

	@property
	def i_create_arc(self):
		"""Creates an arc based on a center point, a start, an end point, and a direction."""
		return self._instance.ICreateArc2

	@i_create_arc.setter
	def i_create_arc(self, value):
		"""Creates an arc based on a center point, a start, an end point, and a direction."""
		self._instance.ICreateArc2 = value

	@property
	def i_create_center_line(self):
		"""Creates a center line from P1 to P2."""
		return self._instance.ICreateCenterLine

	@i_create_center_line.setter
	def i_create_center_line(self, value):
		"""Creates a center line from P1 to P2."""
		self._instance.ICreateCenterLine = value

	@property
	def i_create_circle(self):
		"""Creates a circle based on a center point and a point on the circle."""
		return self._instance.ICreateCircle2

	@i_create_circle.setter
	def i_create_circle(self, value):
		"""Creates a circle based on a center point and a point on the circle."""
		self._instance.ICreateCircle2 = value

	@property
	def i_create_circle_by_radius(self):
		"""Creates a circle based on a center point and a specified radius."""
		return self._instance.ICreateCircleByRadius2

	@i_create_circle_by_radius.setter
	def i_create_circle_by_radius(self, value):
		"""Creates a circle based on a center point and a specified radius."""
		self._instance.ICreateCircleByRadius2 = value

	@property
	def i_create_clipped_splines(self):
		"""Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch."""
		return self._instance.ICreateClippedSplines

	@i_create_clipped_splines.setter
	def i_create_clipped_splines(self, value):
		"""Creates one or more sketch spline segments that are clipped against a given (x1, y1), (x2, y2) rectangle. This rectangle lies in the space of the active 2D sketch."""
		self._instance.ICreateClippedSplines = value

	@property
	def i_create_ellipse(self):
		"""Creates an ellipse using the specified center point and points."""
		return self._instance.ICreateEllipse2

	@i_create_ellipse.setter
	def i_create_ellipse(self, value):
		"""Creates an ellipse using the specified center point and points."""
		self._instance.ICreateEllipse2 = value

	@property
	def i_create_elliptical_arc(self):
		"""Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points."""
		return self._instance.ICreateEllipticalArc2

	@i_create_elliptical_arc.setter
	def i_create_elliptical_arc(self, value):
		"""Creates a partial ellipse given a center point, two points that specify the major and minor axis, and two points that define the elliptical start and end points."""
		self._instance.ICreateEllipticalArc2 = value

	@property
	def i_create_elliptical_arc_by_center(self):
		"""Creates an elliptical arc trimmed between two points."""
		return self._instance.ICreateEllipticalArcByCenter

	@i_create_elliptical_arc_by_center.setter
	def i_create_elliptical_arc_by_center(self, value):
		"""Creates an elliptical arc trimmed between two points."""
		self._instance.ICreateEllipticalArcByCenter = value

	@property
	def i_create_line(self):
		"""Creates a sketch line in the currently active 2D or 3D sketch."""
		return self._instance.ICreateLine2

	@i_create_line.setter
	def i_create_line(self, value):
		"""Creates a sketch line in the currently active 2D or 3D sketch."""
		self._instance.ICreateLine2 = value

	@property
	def i_feature_by_position_reverse(self):
		"""Gets the nth from last feature in the document."""
		return self._instance.IFeatureByPositionReverse

	@i_feature_by_position_reverse.setter
	def i_feature_by_position_reverse(self, value):
		"""Gets the nth from last feature in the document."""
		self._instance.IFeatureByPositionReverse = value

	@property
	def i_feature_reference_curve(self):
		"""Creates a reference curve feature from an array of curves."""
		return self._instance.IFeatureReferenceCurve

	@i_feature_reference_curve.setter
	def i_feature_reference_curve(self, value):
		"""Creates a reference curve feature from an array of curves."""
		self._instance.IFeatureReferenceCurve = value

	@property
	def i_first_feature(self):
		"""Gets the first feature in the document."""
		return self._instance.IFirstFeature

	@i_first_feature.setter
	def i_first_feature(self, value):
		"""Gets the first feature in the document."""
		self._instance.IFirstFeature = value

	@property
	def i_getrd_party_storage(self):
		"""Gets the IStream interface to the specified third-party stream inside this SOLIDWORKS document."""
		return self._instance.IGet3rdPartyStorage

	@i_getrd_party_storage.setter
	def i_getrd_party_storage(self, value):
		"""Gets the IStream interface to the specified third-party stream inside this SOLIDWORKS document."""
		self._instance.IGet3rdPartyStorage = value

	@property
	def i_get_active_sketch(self):
		"""Gets the active sketch."""
		return self._instance.IGetActiveSketch2

	@i_get_active_sketch.setter
	def i_get_active_sketch(self, value):
		"""Gets the active sketch."""
		self._instance.IGetActiveSketch2 = value

	@property
	def i_get_angular_units(self):
		"""Gets the current angular unit settings."""
		return self._instance.IGetAngularUnits

	@i_get_angular_units.setter
	def i_get_angular_units(self, value):
		"""Gets the current angular unit settings."""
		self._instance.IGetAngularUnits = value

	@property
	def i_get_configuration_by_name(self):
		"""Gets the specified configuration."""
		return self._instance.IGetConfigurationByName

	@i_get_configuration_by_name.setter
	def i_get_configuration_by_name(self, value):
		"""Gets the specified configuration."""
		self._instance.IGetConfigurationByName = value

	@property
	def i_get_configuration_names(self):
		"""Gets the names of the configurations in this document."""
		return self._instance.IGetConfigurationNames

	@i_get_configuration_names.setter
	def i_get_configuration_names(self, value):
		"""Gets the names of the configurations in this document."""
		self._instance.IGetConfigurationNames = value

	@property
	def i_get_dependencies(self):
		"""Gets all of the model's dependencies."""
		return self._instance.IGetDependencies2

	@i_get_dependencies.setter
	def i_get_dependencies(self, value):
		"""Gets all of the model's dependencies."""
		self._instance.IGetDependencies2 = value

	@property
	def i_get_design_table(self):
		"""Gets the design table associated with this part or assembly document."""
		return self._instance.IGetDesignTable

	@i_get_design_table.setter
	def i_get_design_table(self, value):
		"""Gets the design table associated with this part or assembly document."""
		self._instance.IGetDesignTable = value

	@property
	def i_get_entity_name(self):
		"""Gets the name of the specified face, edge, or vertex."""
		return self._instance.IGetEntityName

	@i_get_entity_name.setter
	def i_get_entity_name(self, value):
		"""Gets the name of the specified face, edge, or vertex."""
		self._instance.IGetEntityName = value

	@property
	def i_get_first_annotation(self):
		"""Gets the first annotation in the model."""
		return self._instance.IGetFirstAnnotation2

	@i_get_first_annotation.setter
	def i_get_first_annotation(self, value):
		"""Gets the first annotation in the model."""
		self._instance.IGetFirstAnnotation2 = value

	@property
	def i_get_first_model_view(self):
		"""Gets the first view in a model document."""
		return self._instance.IGetFirstModelView

	@i_get_first_model_view.setter
	def i_get_first_model_view(self, value):
		"""Gets the first view in a model document."""
		self._instance.IGetFirstModelView = value

	@property
	def i_get_layer_manager(self):
		"""Gets the layer manager ofr the current drawing document."""
		return self._instance.IGetLayerManager

	@i_get_layer_manager.setter
	def i_get_layer_manager(self, value):
		"""Gets the layer manager ofr the current drawing document."""
		self._instance.IGetLayerManager = value

	@property
	def i_get_lines(self):
		"""Gets all of the lines in the current sketch."""
		return self._instance.IGetLines

	@i_get_lines.setter
	def i_get_lines(self, value):
		"""Gets all of the lines in the current sketch."""
		self._instance.IGetLines = value

	@property
	def i_get_model_view_names(self):
		"""Gets a list containing the names of each model view in this document."""
		return self._instance.IGetModelViewNames

	@i_get_model_view_names.setter
	def i_get_model_view_names(self, value):
		"""Gets a list containing the names of each model view in this document."""
		self._instance.IGetModelViewNames = value

	@property
	def i_get_next(self):
		"""Gets the next document in the current SOLIDWORKS session."""
		return self._instance.IGetNext

	@i_get_next.setter
	def i_get_next(self, value):
		"""Gets the next document in the current SOLIDWORKS session."""
		self._instance.IGetNext = value

	@property
	def i_get_num_dependencies(self):
		"""Gets the number of strings returned by IModelDoc2::IGetDependencies2."""
		return self._instance.IGetNumDependencies2

	@i_get_num_dependencies.setter
	def i_get_num_dependencies(self, value):
		"""Gets the number of strings returned by IModelDoc2::IGetDependencies2."""
		self._instance.IGetNumDependencies2 = value

	@property
	def i_get_ray_intersections_points(self):
		"""Gets the intersection point information generated by IModelDoc2::IRayIntersections."""
		return self._instance.IGetRayIntersectionsPoints

	@i_get_ray_intersections_points.setter
	def i_get_ray_intersections_points(self, value):
		"""Gets the intersection point information generated by IModelDoc2::IRayIntersections."""
		self._instance.IGetRayIntersectionsPoints = value

	@property
	def i_get_ray_intersections_topology(self):
		"""Gets the topology intersections generated by IModelDoc2::IRayIntersections."""
		return self._instance.IGetRayIntersectionsTopology

	@i_get_ray_intersections_topology.setter
	def i_get_ray_intersections_topology(self, value):
		"""Gets the topology intersections generated by IModelDoc2::IRayIntersections."""
		self._instance.IGetRayIntersectionsTopology = value

	@property
	def i_get_standard_view_rotation(self):
		"""Gets the specified view orientation matrix with respect to the Front view."""
		return self._instance.IGetStandardViewRotation

	@i_get_standard_view_rotation.setter
	def i_get_standard_view_rotation(self, value):
		"""Gets the specified view orientation matrix with respect to the Front view."""
		self._instance.IGetStandardViewRotation = value

	@property
	def i_get_units(self):
		"""Gets the current unit settings, fraction base, fraction value, and significant digits."""
		return self._instance.IGetUnits

	@i_get_units.setter
	def i_get_units(self, value):
		"""Gets the current unit settings, fraction base, fraction value, and significant digits."""
		self._instance.IGetUnits = value

	@property
	def i_get_user_unit(self):
		"""Gets this document's units settings."""
		return self._instance.IGetUserUnit

	@i_get_user_unit.setter
	def i_get_user_unit(self, value):
		"""Gets this document's units settings."""
		self._instance.IGetUserUnit = value

	@property
	def i_get_version_history_count(self):
		"""Gets the size of the array required to hold data returend by IModleDoc2::IVersionHistory."""
		return self._instance.IGetVersionHistoryCount

	@i_get_version_history_count.setter
	def i_get_version_history_count(self, value):
		"""Gets the size of the array required to hold data returend by IModleDoc2::IVersionHistory."""
		self._instance.IGetVersionHistoryCount = value

	@property
	def i_insert_datum_tag(self):
		"""Inserts a datum tag symbol at the selected location."""
		return self._instance.IInsertDatumTag2

	@i_insert_datum_tag.setter
	def i_insert_datum_tag(self, value):
		"""Inserts a datum tag symbol at the selected location."""
		self._instance.IInsertDatumTag2 = value

	@property
	def i_insert_gtol(self):
		"""Creates a new geometric tolerance symbol (GTol) in this document."""
		return self._instance.IInsertGtol

	@i_insert_gtol.setter
	def i_insert_gtol(self, value):
		"""Creates a new geometric tolerance symbol (GTol) in this document."""
		self._instance.IInsertGtol = value

	@property
	def i_insert_note(self):
		"""Inserts a note in this document."""
		return self._instance.IInsertNote

	@i_insert_note.setter
	def i_insert_note(self, value):
		"""Inserts a note in this document."""
		self._instance.IInsertNote = value

	@property
	def i_insert_projected_sketch(self):
		"""Projects the selected sketch items from the current sketch onto a selected surface."""
		return self._instance.IInsertProjectedSketch2

	@i_insert_projected_sketch.setter
	def i_insert_projected_sketch(self, value):
		"""Projects the selected sketch items from the current sketch onto a selected surface."""
		self._instance.IInsertProjectedSketch2 = value

	@property
	def i_insert_sketch_for_edge_flange(self):
		"""Inserts a sketch for IFeatureManager::InsertSheetMetalEdgeFlange2 in this sheet metal part."""
		return self._instance.IInsertSketchForEdgeFlange

	@i_insert_sketch_for_edge_flange.setter
	def i_insert_sketch_for_edge_flange(self, value):
		"""Inserts a sketch for IFeatureManager::InsertSheetMetalEdgeFlange2 in this sheet metal part."""
		self._instance.IInsertSketchForEdgeFlange = value

	@property
	def i_insert_sketch_text(self):
		"""Inserts sketch text."""
		return self._instance.IInsertSketchText

	@i_insert_sketch_text.setter
	def i_insert_sketch_text(self, value):
		"""Inserts sketch text."""
		self._instance.IInsertSketchText = value

	@property
	def i_insert_weld_symbol(self):
		"""Inserts a weld symbol into the model."""
		return self._instance.IInsertWeldSymbol3

	@i_insert_weld_symbol.setter
	def i_insert_weld_symbol(self, value):
		"""Inserts a weld symbol into the model."""
		self._instance.IInsertWeldSymbol3 = value

	@property
	def i_list_auxiliary_external_file_references(self):
		"""Gets the names of auxiliary external file references for this model."""
		return self._instance.IListAuxiliaryExternalFileReferences

	@i_list_auxiliary_external_file_references.setter
	def i_list_auxiliary_external_file_references(self, value):
		"""Gets the names of auxiliary external file references for this model."""
		self._instance.IListAuxiliaryExternalFileReferences = value

	@property
	def i_multi_select_by_ray(self):
		"""Selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius."""
		return self._instance.IMultiSelectByRay

	@i_multi_select_by_ray.setter
	def i_multi_select_by_ray(self, value):
		"""Selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius."""
		self._instance.IMultiSelectByRay = value

	@property
	def insert_d_spline_curve(self):
		"""Inserts a 3D-spline curve through the selected reference points."""
		return self._instance.Insert3DSplineCurve

	@insert_d_spline_curve.setter
	def insert_d_spline_curve(self, value):
		"""Inserts a 3D-spline curve through the selected reference points."""
		self._instance.Insert3DSplineCurve = value

	@property
	def insert_axis(self):
		"""Inserts a reference axis based on the currently selected items with an option to automatically size the axis."""
		return self._instance.InsertAxis2

	@insert_axis.setter
	def insert_axis(self, value):
		"""Inserts a reference axis based on the currently selected items with an option to automatically size the axis."""
		self._instance.InsertAxis2 = value

	@property
	def insert_bend_table_edit(self):
		"""Inserts a bend table and puts the bend table into its edit state."""
		return self._instance.InsertBendTableEdit

	@insert_bend_table_edit.setter
	def insert_bend_table_edit(self, value):
		"""Inserts a bend table and puts the bend table into its edit state."""
		self._instance.InsertBendTableEdit = value

	@property
	def insert_bend_table_new(self):
		"""Inserts a new bend table into the model document."""
		return self._instance.InsertBendTableNew

	@insert_bend_table_new.setter
	def insert_bend_table_new(self, value):
		"""Inserts a new bend table into the model document."""
		self._instance.InsertBendTableNew = value

	@property
	def insert_bend_table_open(self):
		"""Inserts an existing bend table from a file into this model document."""
		return self._instance.InsertBendTableOpen

	@insert_bend_table_open.setter
	def insert_bend_table_open(self, value):
		"""Inserts an existing bend table from a file into this model document."""
		self._instance.InsertBendTableOpen = value

	@property
	def insert_bkg_image(self):
		"""Inserts the scene background image."""
		return self._instance.InsertBkgImage

	@insert_bkg_image.setter
	def insert_bkg_image(self, value):
		"""Inserts the scene background image."""
		self._instance.InsertBkgImage = value

	@property
	def insert_composite_curve(self):
		"""Inserts a composite curve based on selections."""
		return self._instance.InsertCompositeCurve

	@insert_composite_curve.setter
	def insert_composite_curve(self, value):
		"""Inserts a composite curve based on selections."""
		self._instance.InsertCompositeCurve = value

	@property
	def insert_connection_point(self):
		"""Adds a connection point based on the selected point and selected planar item."""
		return self._instance.InsertConnectionPoint

	@insert_connection_point.setter
	def insert_connection_point(self, value):
		"""Adds a connection point based on the selected point and selected planar item."""
		self._instance.InsertConnectionPoint = value

	@property
	def insert_curve_file(self):
		"""Creates a curve."""
		return self._instance.InsertCurveFile

	@insert_curve_file.setter
	def insert_curve_file(self, value):
		"""Creates a curve."""
		self._instance.InsertCurveFile = value

	@property
	def insert_curve_file_begin(self):
		"""Creates a curve."""
		return self._instance.InsertCurveFileBegin

	@insert_curve_file_begin.setter
	def insert_curve_file_begin(self, value):
		"""Creates a curve."""
		self._instance.InsertCurveFileBegin = value

	@property
	def insert_curve_file_end(self):
		"""Creates a curve."""
		return self._instance.InsertCurveFileEnd

	@insert_curve_file_end.setter
	def insert_curve_file_end(self, value):
		"""Creates a curve."""
		self._instance.InsertCurveFileEnd = value

	@property
	def insert_curve_file_point(self):
		"""Creates a point for a curve."""
		return self._instance.InsertCurveFilePoint

	@insert_curve_file_point.setter
	def insert_curve_file_point(self, value):
		"""Creates a point for a curve."""
		self._instance.InsertCurveFilePoint = value

	@property
	def insert_datum_tag(self):
		"""Inserts a datum tag symbol at a selected location."""
		return self._instance.InsertDatumTag2

	@insert_datum_tag.setter
	def insert_datum_tag(self, value):
		"""Inserts a datum tag symbol at a selected location."""
		self._instance.InsertDatumTag2 = value

	@property
	def insert_dome(self):
		"""Inserts a dome."""
		return self._instance.InsertDome

	@insert_dome.setter
	def insert_dome(self, value):
		"""Inserts a dome."""
		self._instance.InsertDome = value

	@property
	def insert_extend_surface(self):
		"""Extends a surface along the selected faces or edges."""
		return self._instance.InsertExtendSurface

	@insert_extend_surface.setter
	def insert_extend_surface(self, value):
		"""Extends a surface along the selected faces or edges."""
		self._instance.InsertExtendSurface = value

	@property
	def insert_family_table_edit(self):
		"""Edits an open design table from Microsoft Excel."""
		return self._instance.InsertFamilyTableEdit

	@insert_family_table_edit.setter
	def insert_family_table_edit(self, value):
		"""Edits an open design table from Microsoft Excel."""
		self._instance.InsertFamilyTableEdit = value

	@property
	def insert_family_table_new(self):
		"""Inserts an existing design table from the model into the selected drawing view."""
		return self._instance.InsertFamilyTableNew

	@insert_family_table_new.setter
	def insert_family_table_new(self, value):
		"""Inserts an existing design table from the model into the selected drawing view."""
		self._instance.InsertFamilyTableNew = value

	@property
	def insert_family_table_open(self):
		"""Inserts the specified Microsoft Excel design table."""
		return self._instance.InsertFamilyTableOpen

	@insert_family_table_open.setter
	def insert_family_table_open(self, value):
		"""Inserts the specified Microsoft Excel design table."""
		self._instance.InsertFamilyTableOpen = value

	@property
	def insert_feature_replace_face(self):
		"""Creates a Replace Face feature."""
		return self._instance.InsertFeatureReplaceFace

	@insert_feature_replace_face.setter
	def insert_feature_replace_face(self, value):
		"""Creates a Replace Face feature."""
		self._instance.InsertFeatureReplaceFace = value

	@property
	def insert_feature_shell(self):
		"""Creates a shell feature."""
		return self._instance.InsertFeatureShell

	@insert_feature_shell.setter
	def insert_feature_shell(self, value):
		"""Creates a shell feature."""
		self._instance.InsertFeatureShell = value

	@property
	def insert_feature_shell_add_thickness(self):
		"""Adds thickness to a face in a multi-thickness shell feature."""
		return self._instance.InsertFeatureShellAddThickness

	@insert_feature_shell_add_thickness.setter
	def insert_feature_shell_add_thickness(self, value):
		"""Adds thickness to a face in a multi-thickness shell feature."""
		self._instance.InsertFeatureShellAddThickness = value

	@property
	def insert_gtol(self):
		"""Creates a new geometric tolerance symbol (GTol) in this document."""
		return self._instance.InsertGtol

	@insert_gtol.setter
	def insert_gtol(self, value):
		"""Creates a new geometric tolerance symbol (GTol) in this document."""
		self._instance.InsertGtol = value

	@property
	def insert_hatched_face(self):
		"""Hatches the selected faces or closed sketch segments in a drawing."""
		return self._instance.InsertHatchedFace

	@insert_hatched_face.setter
	def insert_hatched_face(self, value):
		"""Hatches the selected faces or closed sketch segments in a drawing."""
		self._instance.InsertHatchedFace = value

	@property
	def insert_helix(self):
		"""Creates a constant-pitch helix or spiral."""
		return self._instance.InsertHelix

	@insert_helix.setter
	def insert_helix(self, value):
		"""Creates a constant-pitch helix or spiral."""
		self._instance.InsertHelix = value

	@property
	def insert_loft_ref_surface(self):
		"""Creates a loft surface from the selected profiles, centerline, and guide curves."""
		return self._instance.InsertLoftRefSurface2

	@insert_loft_ref_surface.setter
	def insert_loft_ref_surface(self, value):
		"""Creates a loft surface from the selected profiles, centerline, and guide curves."""
		self._instance.InsertLoftRefSurface2 = value

	@property
	def insert_new_note(self):
		"""Creates a new note."""
		return self._instance.InsertNewNote3

	@insert_new_note.setter
	def insert_new_note(self, value):
		"""Creates a new note."""
		self._instance.InsertNewNote3 = value

	@property
	def insert_note(self):
		"""Inserts a note in this document."""
		return self._instance.InsertNote

	@insert_note.setter
	def insert_note(self, value):
		"""Inserts a note in this document."""
		self._instance.InsertNote = value

	@property
	def insert_object(self):
		"""Activates the Microsoft Insert Object dialog."""
		return self._instance.InsertObject

	@insert_object.setter
	def insert_object(self, value):
		"""Activates the Microsoft Insert Object dialog."""
		self._instance.InsertObject = value

	@property
	def insert_offset_surface(self):
		"""Inserts an offset surface."""
		return self._instance.InsertOffsetSurface

	@insert_offset_surface.setter
	def insert_offset_surface(self, value):
		"""Inserts an offset surface."""
		self._instance.InsertOffsetSurface = value

	@property
	def insert_planar_ref_surface(self):
		"""Inserts a planar reference surface."""
		return self._instance.InsertPlanarRefSurface

	@insert_planar_ref_surface.setter
	def insert_planar_ref_surface(self, value):
		"""Inserts a planar reference surface."""
		self._instance.InsertPlanarRefSurface = value

	@property
	def insert_point(self):
		"""Inserts a point in this model document."""
		return self._instance.InsertPoint

	@insert_point.setter
	def insert_point(self, value):
		"""Inserts a point in this model document."""
		self._instance.InsertPoint = value

	@property
	def insert_radiate_surface(self):
		"""Creates a radiate surface based on the selections."""
		return self._instance.InsertRadiateSurface

	@insert_radiate_surface.setter
	def insert_radiate_surface(self, value):
		"""Creates a radiate surface based on the selections."""
		self._instance.InsertRadiateSurface = value

	@property
	def insert_ref_point(self):
		"""Inserts a reference point based on the current selections."""
		return self._instance.InsertRefPoint

	@insert_ref_point.setter
	def insert_ref_point(self, value):
		"""Inserts a reference point based on the current selections."""
		self._instance.InsertRefPoint = value

	@property
	def insert_rip(self):
		"""Creates a rip feature."""
		return self._instance.InsertRip

	@insert_rip.setter
	def insert_rip(self, value):
		"""Creates a rip feature."""
		self._instance.InsertRip = value

	@property
	def insert_route_point(self):
		"""Adds a route point based on the selected point."""
		return self._instance.InsertRoutePoint

	@insert_route_point.setter
	def insert_route_point(self, value):
		"""Adds a route point based on the selected point."""
		self._instance.InsertRoutePoint = value

	@property
	def insert_sheet_metal_break_corner(self):
		"""Inserts a break corner into a sheet metal part."""
		return self._instance.InsertSheetMetalBreakCorner

	@insert_sheet_metal_break_corner.setter
	def insert_sheet_metal_break_corner(self, value):
		"""Inserts a break corner into a sheet metal part."""
		self._instance.InsertSheetMetalBreakCorner = value

	@property
	def insert_sheet_metal_closed_corner(self):
		"""Inserts a sheet metal closed corner into this model document."""
		return self._instance.InsertSheetMetalClosedCorner

	@insert_sheet_metal_closed_corner.setter
	def insert_sheet_metal_closed_corner(self, value):
		"""Inserts a sheet metal closed corner into this model document."""
		self._instance.InsertSheetMetalClosedCorner = value

	@property
	def insert_sheet_metal_fold(self):
		"""Inserts a fold feature at the selected objects."""
		return self._instance.InsertSheetMetalFold

	@insert_sheet_metal_fold.setter
	def insert_sheet_metal_fold(self, value):
		"""Inserts a fold feature at the selected objects."""
		self._instance.InsertSheetMetalFold = value

	@property
	def insert_sheet_metal_jog(self):
		"""Inserts a sheet metal jog in the current model document."""
		return self._instance.InsertSheetMetalJog

	@insert_sheet_metal_jog.setter
	def insert_sheet_metal_jog(self, value):
		"""Inserts a sheet metal jog in the current model document."""
		self._instance.InsertSheetMetalJog = value

	@property
	def insert_sheet_metal_unfold(self):
		"""Inserts an unfold feature at the selected objects."""
		return self._instance.InsertSheetMetalUnfold

	@insert_sheet_metal_unfold.setter
	def insert_sheet_metal_unfold(self, value):
		"""Inserts an unfold feature at the selected objects."""
		self._instance.InsertSheetMetalUnfold = value

	@property
	def insert_sketch_for_edge_flange(self):
		"""Inserts a profile sketch of an edge flange in this sheet metal part."""
		return self._instance.InsertSketchForEdgeFlange

	@insert_sketch_for_edge_flange.setter
	def insert_sketch_for_edge_flange(self, value):
		"""Inserts a profile sketch of an edge flange in this sheet metal part."""
		self._instance.InsertSketchForEdgeFlange = value

	@property
	def insert_sketch_picture(self):
		"""Inserts a picture into the current sketch."""
		return self._instance.InsertSketchPicture

	@insert_sketch_picture.setter
	def insert_sketch_picture(self, value):
		"""Inserts a picture into the current sketch."""
		self._instance.InsertSketchPicture = value

	@property
	def insert_sketch_picture_data(self):
		"""Inserts a picture into the current sketch."""
		return self._instance.InsertSketchPictureData

	@insert_sketch_picture_data.setter
	def insert_sketch_picture_data(self, value):
		"""Inserts a picture into the current sketch."""
		self._instance.InsertSketchPictureData = value

	@property
	def insert_sketch_picture_datax(self):
		"""Inserts a picture into the current sketch in 64-bit applications."""
		return self._instance.InsertSketchPictureDatax64

	@insert_sketch_picture_datax.setter
	def insert_sketch_picture_datax(self, value):
		"""Inserts a picture into the current sketch in 64-bit applications."""
		self._instance.InsertSketchPictureDatax64 = value

	@property
	def insert_sketch_text(self):
		"""Inserts sketch text."""
		return self._instance.InsertSketchText

	@insert_sketch_text.setter
	def insert_sketch_text(self, value):
		"""Inserts sketch text."""
		self._instance.InsertSketchText = value

	@property
	def insert_spline_point(self):
		"""Inserts a spline point."""
		return self._instance.InsertSplinePoint

	@insert_spline_point.setter
	def insert_spline_point(self, value):
		"""Inserts a spline point."""
		self._instance.InsertSplinePoint = value

	@property
	def insert_split_line_project(self):
		"""Splits a face by projecting sketch lines onto the face."""
		return self._instance.InsertSplitLineProject

	@insert_split_line_project.setter
	def insert_split_line_project(self, value):
		"""Splits a face by projecting sketch lines onto the face."""
		self._instance.InsertSplitLineProject = value

	@property
	def insert_split_line_sil(self):
		"""Splits a face by creating split lines along the silhouette of the selected faces."""
		return self._instance.InsertSplitLineSil

	@insert_split_line_sil.setter
	def insert_split_line_sil(self, value):
		"""Splits a face by creating split lines along the silhouette of the selected faces."""
		self._instance.InsertSplitLineSil = value

	@property
	def insert_weld_symbol(self):
		"""Inserts a weld symbol into the model."""
		return self._instance.InsertWeldSymbol3

	@insert_weld_symbol.setter
	def insert_weld_symbol(self, value):
		"""Inserts a weld symbol into the model."""
		self._instance.InsertWeldSymbol3 = value

	@property
	def inspect_curvature(self):
		"""Adds curvature combs to the selected sketch segment."""
		return self._instance.InspectCurvature

	@inspect_curvature.setter
	def inspect_curvature(self, value):
		"""Adds curvature combs to the selected sketch segment."""
		self._instance.InspectCurvature = value

	@property
	def i_parameter(self):
		"""Gets the specified parameter."""
		return self._instance.IParameter

	@i_parameter.setter
	def i_parameter(self, value):
		"""Gets the specified parameter."""
		self._instance.IParameter = value

	@property
	def i_releaserd_party_storage(self):
		"""Releases the specified third-party stream."""
		return self._instance.IRelease3rdPartyStorage

	@i_releaserd_party_storage.setter
	def i_releaserd_party_storage(self, value):
		"""Releases the specified third-party stream."""
		self._instance.IRelease3rdPartyStorage = value

	@property
	def is_active(self):
		"""Gets whether the specified assembly component is shown or hidden in this model document."""
		return self._instance.IsActive

	@is_active.setter
	def is_active(self, value):
		"""Gets whether the specified assembly component is shown or hidden in this model document."""
		self._instance.IsActive = value

	@property
	def is_editing_self(self):
		"""Gets whether this model is being edited in the context of another document."""
		return self._instance.IsEditingSelf

	@is_editing_self.setter
	def is_editing_self(self, value):
		"""Gets whether this model is being edited in the context of another document."""
		self._instance.IsEditingSelf = value

	@property
	def i_set_angular_units(self):
		"""Sets the current angular units."""
		return self._instance.ISetAngularUnits

	@i_set_angular_units.setter
	def i_set_angular_units(self, value):
		"""Sets the current angular units."""
		self._instance.ISetAngularUnits = value

	@property
	def i_set_next_selection_group_id(self):
		"""Sets the group ID for all remaining selections."""
		return self._instance.ISetNextSelectionGroupId

	@i_set_next_selection_group_id.setter
	def i_set_next_selection_group_id(self, value):
		"""Sets the group ID for all remaining selections."""
		self._instance.ISetNextSelectionGroupId = value

	@property
	def i_sketch_spline_by_eqn_params(self):
		"""Creates a spline on the active 2D sketch using the specified b-curve parameters."""
		return self._instance.ISketchSplineByEqnParams

	@i_sketch_spline_by_eqn_params.setter
	def i_sketch_spline_by_eqn_params(self, value):
		"""Creates a spline on the active 2D sketch using the specified b-curve parameters."""
		self._instance.ISketchSplineByEqnParams = value

	@property
	def is_light_locked_to_model(self):
		"""Gets whether the specified light is fixed."""
		return self._instance.IsLightLockedToModel

	@is_light_locked_to_model.setter
	def is_light_locked_to_model(self, value):
		"""Gets whether the specified light is fixed."""
		self._instance.IsLightLockedToModel = value

	@property
	def is_opened_read_only(self):
		"""Gets whether a SOLIDWORKS document is open in read-only mode."""
		return self._instance.IsOpenedReadOnly

	@is_opened_read_only.setter
	def is_opened_read_only(self, value):
		"""Gets whether a SOLIDWORKS document is open in read-only mode."""
		self._instance.IsOpenedReadOnly = value

	@property
	def is_opened_view_only(self):
		"""Gets whether a SOLIDWORKS document is open in view-only mode."""
		return self._instance.IsOpenedViewOnly

	@is_opened_view_only.setter
	def is_opened_view_only(self, value):
		"""Gets whether a SOLIDWORKS document is open in view-only mode."""
		self._instance.IsOpenedViewOnly = value

	@property
	def is_tessellation_valid(self):
		"""Gets whether the current set of facets is valid."""
		return self._instance.IsTessellationValid

	@is_tessellation_valid.setter
	def is_tessellation_valid(self, value):
		"""Gets whether the current set of facets is valid."""
		self._instance.IsTessellationValid = value

	@property
	def i_version_history(self):
		"""Gets an array of strings indicating the versions in which this model document was saved, including the SOLIDWORKS version in which the model document is currently opened and which is the last value returned in the array."""
		return self._instance.IVersionHistory

	@i_version_history.setter
	def i_version_history(self, value):
		"""Gets an array of strings indicating the versions in which this model document was saved, including the SOLIDWORKS version in which the model document is currently opened and which is the last value returned in the array."""
		self._instance.IVersionHistory = value

	@property
	def l_b_down_at(self):
		"""Generates a left mouse button press (down) event."""
		return self._instance.LBDownAt

	@l_b_down_at.setter
	def l_b_down_at(self, value):
		"""Generates a left mouse button press (down) event."""
		self._instance.LBDownAt = value

	@property
	def l_b_up_at(self):
		"""Generates a left-mouse button release (up) event."""
		return self._instance.LBUpAt

	@l_b_up_at.setter
	def l_b_up_at(self, value):
		"""Generates a left-mouse button release (up) event."""
		self._instance.LBUpAt = value

	@property
	def list_auxiliary_external_file_references(self):
		"""Gets the names of auxiliary external file references for this model."""
		return self._instance.ListAuxiliaryExternalFileReferences

	@list_auxiliary_external_file_references.setter
	def list_auxiliary_external_file_references(self, value):
		"""Gets the names of auxiliary external file references for this model."""
		self._instance.ListAuxiliaryExternalFileReferences = value

	@property
	def list_auxiliary_external_file_references_count(self):
		"""Gets the number of auxiliary external file references for this model."""
		return self._instance.ListAuxiliaryExternalFileReferencesCount

	@list_auxiliary_external_file_references_count.setter
	def list_auxiliary_external_file_references_count(self, value):
		"""Gets the number of auxiliary external file references for this model."""
		self._instance.ListAuxiliaryExternalFileReferencesCount = value

	@property
	def lock(self):
		"""Blocks the modifying commands in the user interface, effectively locking the application."""
		return self._instance.Lock

	@lock.setter
	def lock(self, value):
		"""Blocks the modifying commands in the user interface, effectively locking the application."""
		self._instance.Lock = value

	@property
	def lock_all_external_references(self):
		"""Locks all external references."""
		return self._instance.LockAllExternalReferences

	@lock_all_external_references.setter
	def lock_all_external_references(self, value):
		"""Locks all external references."""
		self._instance.LockAllExternalReferences = value

	@property
	def lock_light_to_model(self):
		"""Locks or unlocks the specified light."""
		return self._instance.LockLightToModel

	@lock_light_to_model.setter
	def lock_light_to_model(self, value):
		"""Locks or unlocks the specified light."""
		self._instance.LockLightToModel = value

	@property
	def mold_draft_analysis(self):
		"""Performs a mold draft analysis."""
		return self._instance.MoldDraftAnalysis

	@mold_draft_analysis.setter
	def mold_draft_analysis(self, value):
		"""Performs a mold draft analysis."""
		self._instance.MoldDraftAnalysis = value

	@property
	def multi_select_by_ray(self):
		"""Selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius."""
		return self._instance.MultiSelectByRay

	@multi_select_by_ray.setter
	def multi_select_by_ray(self, value):
		"""Selects multiple objects of the specified type that are intersected by a ray from point (x,y,z in meters) in direction vector (x,y,z) within a distance radius."""
		self._instance.MultiSelectByRay = value

	@property
	def name_view(self):
		"""Creates a named view using the current view."""
		return self._instance.NameView

	@name_view.setter
	def name_view(self, value):
		"""Creates a named view using the current view."""
		self._instance.NameView = value

	@property
	def object_display_as_icon(self):
		"""Shows the current OLE object as an icon."""
		return self._instance.ObjectDisplayAsIcon

	@object_display_as_icon.setter
	def object_display_as_icon(self, value):
		"""Shows the current OLE object as an icon."""
		self._instance.ObjectDisplayAsIcon = value

	@property
	def object_display_content(self):
		"""Shows the current OLE object's content."""
		return self._instance.ObjectDisplayContent

	@object_display_content.setter
	def object_display_content(self, value):
		"""Shows the current OLE object's content."""
		self._instance.ObjectDisplayContent = value

	@property
	def object_resetsize(self):
		"""Sets the size of the current OLE object to the default."""
		return self._instance.ObjectResetsize

	@object_resetsize.setter
	def object_resetsize(self, value):
		"""Sets the size of the current OLE object to the default."""
		self._instance.ObjectResetsize = value

	@property
	def parameter(self):
		"""Gets the specified parameter."""
		return self._instance.Parameter

	@parameter.setter
	def parameter(self, value):
		"""Gets the specified parameter."""
		self._instance.Parameter = value

	@property
	def parent_child_relationship(self):
		"""Shows the Parent/Child Relationships dialog for the selected feature."""
		return self._instance.ParentChildRelationship

	@parent_child_relationship.setter
	def parent_child_relationship(self, value):
		"""Shows the Parent/Child Relationships dialog for the selected feature."""
		self._instance.ParentChildRelationship = value

	@property
	def paste(self):
		"""Pastes the contents of the Microsoft Windows Clipboard at the current insertion point."""
		return self._instance.Paste

	@paste.setter
	def paste(self, value):
		"""Pastes the contents of the Microsoft Windows Clipboard at the current insertion point."""
		self._instance.Paste = value

	@property
	def print_direct(self):
		"""Prints the current document to the default printer."""
		return self._instance.PrintDirect

	@print_direct.setter
	def print_direct(self, value):
		"""Prints the current document to the default printer."""
		self._instance.PrintDirect = value

	@property
	def print_preview(self):
		"""Displays the Print Preview page for the current document."""
		return self._instance.PrintPreview

	@print_preview.setter
	def print_preview(self, value):
		"""Displays the Print Preview page for the current document."""
		self._instance.PrintPreview = value

	@property
	def property_sheet(self):
		"""Displays the the selected object's property sheet."""
		return self._instance.PropertySheet

	@property_sheet.setter
	def property_sheet(self, value):
		"""Displays the the selected object's property sheet."""
		self._instance.PropertySheet = value

	@property
	def quit(self):
		"""Closes the active document without saving changes (see Remarks)."""
		return self._instance.Quit

	@quit.setter
	def quit(self, value):
		"""Closes the active document without saving changes (see Remarks)."""
		self._instance.Quit = value

	@property
	def reattach_ordinate(self):
		"""Reattaches an ordinate dimension to a different entity."""
		return self._instance.ReattachOrdinate

	@reattach_ordinate.setter
	def reattach_ordinate(self, value):
		"""Reattaches an ordinate dimension to a different entity."""
		self._instance.ReattachOrdinate = value

	@property
	def reload_or_replace(self):
		"""Reloads or replaces the current model document."""
		return self._instance.ReloadOrReplace

	@reload_or_replace.setter
	def reload_or_replace(self, value):
		"""Reloads or replaces the current model document."""
		self._instance.ReloadOrReplace = value

	@property
	def remove_groups(self):
		"""Removes any annotation groups in the current selection."""
		return self._instance.RemoveGroups

	@remove_groups.setter
	def remove_groups(self, value):
		"""Removes any annotation groups in the current selection."""
		self._instance.RemoveGroups = value

	@property
	def remove_inspect_curvature(self):
		"""Removes curvature combs from the selected curved sketch segment."""
		return self._instance.RemoveInspectCurvature

	@remove_inspect_curvature.setter
	def remove_inspect_curvature(self, value):
		"""Removes curvature combs from the selected curved sketch segment."""
		self._instance.RemoveInspectCurvature = value

	@property
	def remove_items_from_group(self):
		"""Removes the selected annotations from their annotation groups."""
		return self._instance.RemoveItemsFromGroup

	@remove_items_from_group.setter
	def remove_items_from_group(self, value):
		"""Removes the selected annotations from their annotation groups."""
		self._instance.RemoveItemsFromGroup = value

	@property
	def reset_blocking_state(self):
		"""Resets the blocking state for the SOLIDWORKS menus."""
		return self._instance.ResetBlockingState

	@reset_blocking_state.setter
	def reset_blocking_state(self, value):
		"""Resets the blocking state for the SOLIDWORKS menus."""
		self._instance.ResetBlockingState = value

	@property
	def reset_light_source_ext_property(self):
		"""Resets the properties for a light source."""
		return self._instance.ResetLightSourceExtProperty

	@reset_light_source_ext_property.setter
	def reset_light_source_ext_property(self, value):
		"""Resets the properties for a light source."""
		self._instance.ResetLightSourceExtProperty = value

	@property
	def reset_property_extension(self):
		"""Clears all values stored in the property extension."""
		return self._instance.ResetPropertyExtension

	@reset_property_extension.setter
	def reset_property_extension(self, value):
		"""Clears all values stored in the property extension."""
		self._instance.ResetPropertyExtension = value

	@property
	def reset_scene_ext_property(self):
		"""Resets the extension property for a scene."""
		return self._instance.ResetSceneExtProperty

	@reset_scene_ext_property.setter
	def reset_scene_ext_property(self, value):
		"""Resets the extension property for a scene."""
		self._instance.ResetSceneExtProperty = value

	@property
	def save(self):
		"""Saves the current document."""
		return self._instance.Save3

	@save.setter
	def save(self, value):
		"""Saves the current document."""
		self._instance.Save3 = value

	@property
	def save_b_m_p(self):
		"""Saves the current view as a bitmap (BMP) file."""
		return self._instance.SaveBMP

	@save_b_m_p.setter
	def save_b_m_p(self, value):
		"""Saves the current view as a bitmap (BMP) file."""
		self._instance.SaveBMP = value

	@property
	def scale(self):
		"""Scales the part."""
		return self._instance.Scale

	@scale.setter
	def scale(self, value):
		"""Scales the part."""
		self._instance.Scale = value

	@property
	def screen_rotate(self):
		"""Switches between model and screen center rotation."""
		return self._instance.ScreenRotate

	@screen_rotate.setter
	def screen_rotate(self, value):
		"""Switches between model and screen center rotation."""
		self._instance.ScreenRotate = value

	@property
	def selected_edge_properties(self):
		"""Sets the property values of the selected edge."""
		return self._instance.SelectedEdgeProperties

	@selected_edge_properties.setter
	def selected_edge_properties(self, value):
		"""Sets the property values of the selected edge."""
		self._instance.SelectedEdgeProperties = value

	@property
	def selected_face_properties(self):
		"""Sets the material property values of the selected face."""
		return self._instance.SelectedFaceProperties

	@selected_face_properties.setter
	def selected_face_properties(self, value):
		"""Sets the material property values of the selected face."""
		self._instance.SelectedFaceProperties = value

	@property
	def selected_feature_properties(self):
		"""Sets the property values of the selected feature."""
		return self._instance.SelectedFeatureProperties

	@selected_feature_properties.setter
	def selected_feature_properties(self, value):
		"""Sets the property values of the selected feature."""
		self._instance.SelectedFeatureProperties = value

	@property
	def select_loop(self):
		"""Selects the loop that corresponds to the selected edge."""
		return self._instance.SelectLoop

	@select_loop.setter
	def select_loop(self, value):
		"""Selects the loop that corresponds to the selected edge."""
		self._instance.SelectLoop = value

	@property
	def select_midpoint(self):
		"""Puts the midpoint (swSelMIDPOINTS) of that edge on the selection list and removes the edge from the selection list when an edge is selected."""
		return self._instance.SelectMidpoint

	@select_midpoint.setter
	def select_midpoint(self, value):
		"""Puts the midpoint (swSelMIDPOINTS) of that edge on the selection list and removes the edge from the selection list when an edge is selected."""
		self._instance.SelectMidpoint = value

	@property
	def select_tangency(self):
		"""Selects all faces tangent to the selected face."""
		return self._instance.SelectTangency

	@select_tangency.setter
	def select_tangency(self, value):
		"""Selects all faces tangent to the selected face."""
		self._instance.SelectTangency = value

	@property
	def set_ambient_light_properties(self):
		"""Sets ambient light properties."""
		return self._instance.SetAmbientLightProperties

	@set_ambient_light_properties.setter
	def set_ambient_light_properties(self, value):
		"""Sets ambient light properties."""
		self._instance.SetAmbientLightProperties = value

	@property
	def set_angular_units(self):
		"""Sets the current angular units."""
		return self._instance.SetAngularUnits

	@set_angular_units.setter
	def set_angular_units(self, value):
		"""Sets the current angular units."""
		self._instance.SetAngularUnits = value

	@property
	def set_arc_centers_displayed(self):
		"""Sets the current arc centers displayed setting."""
		return self._instance.SetArcCentersDisplayed

	@set_arc_centers_displayed.setter
	def set_arc_centers_displayed(self, value):
		"""Sets the current arc centers displayed setting."""
		self._instance.SetArcCentersDisplayed = value

	@property
	def set_bend_state(self):
		"""Sets the bend state of a sheet metal part."""
		return self._instance.SetBendState

	@set_bend_state.setter
	def set_bend_state(self, value):
		"""Sets the bend state of a sheet metal part."""
		self._instance.SetBendState = value

	@property
	def set_blocking_state(self):
		"""Sets the blocking state for the SOLIDWORKS menus."""
		return self._instance.SetBlockingState

	@set_blocking_state.setter
	def set_blocking_state(self, value):
		"""Sets the blocking state for the SOLIDWORKS menus."""
		self._instance.SetBlockingState = value

	@property
	def set_consider_leaders_as_lines(self):
		"""Sets a flag on the document that indicates whether the display data of a leader should be included as lines when the lines are retrieved from a view or annotation in this document."""
		return self._instance.SetConsiderLeadersAsLines

	@set_consider_leaders_as_lines.setter
	def set_consider_leaders_as_lines(self, value):
		"""Sets a flag on the document that indicates whether the display data of a leader should be included as lines when the lines are retrieved from a view or annotation in this document."""
		self._instance.SetConsiderLeadersAsLines = value

	@property
	def set_direction_light_properties(self):
		"""Sets direction light properties."""
		return self._instance.SetDirectionLightProperties

	@set_direction_light_properties.setter
	def set_direction_light_properties(self, value):
		"""Sets direction light properties."""
		self._instance.SetDirectionLightProperties = value

	@property
	def set_feature_manager_width(self):
		"""Sets the width of the FeatureManager design tree."""
		return self._instance.SetFeatureManagerWidth

	@set_feature_manager_width.setter
	def set_feature_manager_width(self, value):
		"""Sets the width of the FeatureManager design tree."""
		self._instance.SetFeatureManagerWidth = value

	@property
	def set_light_source_name(self):
		"""Sets the light source name used internally by the SOLIDWORKS software."""
		return self._instance.SetLightSourceName

	@set_light_source_name.setter
	def set_light_source_name(self, value):
		"""Sets the light source name used internally by the SOLIDWORKS software."""
		self._instance.SetLightSourceName = value

	@property
	def set_light_source_property_values_v_b(self):
		"""Sets the light source property values."""
		return self._instance.SetLightSourcePropertyValuesVB

	@set_light_source_property_values_v_b.setter
	def set_light_source_property_values_v_b(self, value):
		"""Sets the light source property values."""
		self._instance.SetLightSourcePropertyValuesVB = value

	@property
	def set_param_value(self):
		"""Sets the value of selected dimension (or parameter)."""
		return self._instance.SetParamValue

	@set_param_value.setter
	def set_param_value(self, value):
		"""Sets the value of selected dimension (or parameter)."""
		self._instance.SetParamValue = value

	@property
	def set_pick_mode(self):
		"""Returns the user to the default selection mode."""
		return self._instance.SetPickMode

	@set_pick_mode.setter
	def set_pick_mode(self, value):
		"""Returns the user to the default selection mode."""
		self._instance.SetPickMode = value

	@property
	def set_point_light_properties(self):
		"""Sets point light properties."""
		return self._instance.SetPointLightProperties

	@set_point_light_properties.setter
	def set_point_light_properties(self, value):
		"""Sets point light properties."""
		self._instance.SetPointLightProperties = value

	@property
	def set_popup_menu_mode(self):
		"""Sets the pop-up menu mode."""
		return self._instance.SetPopupMenuMode

	@set_popup_menu_mode.setter
	def set_popup_menu_mode(self, value):
		"""Sets the pop-up menu mode."""
		self._instance.SetPopupMenuMode = value

	@property
	def set_read_only_state(self):
		"""Sets whether this document is read-only or read-write."""
		return self._instance.SetReadOnlyState

	@set_read_only_state.setter
	def set_read_only_state(self, value):
		"""Sets whether this document is read-only or read-write."""
		self._instance.SetReadOnlyState = value

	@property
	def set_save_as_file_name(self):
		"""Sets the Save As filename from within the FileSaveAsNotify2 event handlers, thereby, bypassing the Save As dialog."""
		return self._instance.SetSaveAsFileName

	@set_save_as_file_name.setter
	def set_save_as_file_name(self, value):
		"""Sets the Save As filename from within the FileSaveAsNotify2 event handlers, thereby, bypassing the Save As dialog."""
		self._instance.SetSaveAsFileName = value

	@property
	def set_save_flag(self):
		"""Flags the document as dirty."""
		return self._instance.SetSaveFlag

	@set_save_flag.setter
	def set_save_flag(self, value):
		"""Flags the document as dirty."""
		self._instance.SetSaveFlag = value

	@property
	def set_scene_bkg_d_i_b(self):
		"""Sets background image described by DIBSECTION data."""
		return self._instance.SetSceneBkgDIB

	@set_scene_bkg_d_i_b.setter
	def set_scene_bkg_d_i_b(self, value):
		"""Sets background image described by DIBSECTION data."""
		self._instance.SetSceneBkgDIB = value

	@property
	def set_spotlight_properties(self):
		"""Sets the spotlight properties."""
		return self._instance.SetSpotlightProperties

	@set_spotlight_properties.setter
	def set_spotlight_properties(self, value):
		"""Sets the spotlight properties."""
		self._instance.SetSpotlightProperties = value

	@property
	def set_tessellation_quality(self):
		"""Sets the shaded-display image quality number for the current document."""
		return self._instance.SetTessellationQuality

	@set_tessellation_quality.setter
	def set_tessellation_quality(self, value):
		"""Sets the shaded-display image quality number for the current document."""
		self._instance.SetTessellationQuality = value

	@property
	def set_title(self):
		"""Sets the title of a new document."""
		return self._instance.SetTitle2

	@set_title.setter
	def set_title(self, value):
		"""Sets the title of a new document."""
		self._instance.SetTitle2 = value

	@property
	def set_toolbar_visibility(self):
		"""Sets the visibility of a toolbar."""
		return self._instance.SetToolbarVisibility

	@set_toolbar_visibility.setter
	def set_toolbar_visibility(self, value):
		"""Sets the visibility of a toolbar."""
		self._instance.SetToolbarVisibility = value

	@property
	def set_units(self):
		"""Sets the units used by the end-user for the model."""
		return self._instance.SetUnits

	@set_units.setter
	def set_units(self, value):
		"""Sets the units used by the end-user for the model."""
		self._instance.SetUnits = value

	@property
	def set_zebra_stripe_data(self):
		"""Sets the zebra-line data."""
		return self._instance.SetZebraStripeData

	@set_zebra_stripe_data.setter
	def set_zebra_stripe_data(self, value):
		"""Sets the zebra-line data."""
		self._instance.SetZebraStripeData = value

	@property
	def show_component(self):
		"""Shows the selected component."""
		return self._instance.ShowComponent2

	@show_component.setter
	def show_component(self, value):
		"""Shows the selected component."""
		self._instance.ShowComponent2 = value

	@property
	def show_configuration(self):
		"""Shows the named configuration by switching to that configuration and making it the active configuration."""
		return self._instance.ShowConfiguration2

	@show_configuration.setter
	def show_configuration(self, value):
		"""Shows the named configuration by switching to that configuration and making it the active configuration."""
		self._instance.ShowConfiguration2 = value

	@property
	def show_cosmetic_thread(self):
		"""Shows the selected cosmetic thread."""
		return self._instance.ShowCosmeticThread

	@show_cosmetic_thread.setter
	def show_cosmetic_thread(self, value):
		"""Shows the selected cosmetic thread."""
		self._instance.ShowCosmeticThread = value

	@property
	def show_named_view(self):
		"""Shows the specified view."""
		return self._instance.ShowNamedView2

	@show_named_view.setter
	def show_named_view(self, value):
		"""Shows the specified view."""
		self._instance.ShowNamedView2 = value

	@property
	def show_solid_body(self):
		"""Shows the selected solid body."""
		return self._instance.ShowSolidBody

	@show_solid_body.setter
	def show_solid_body(self, value):
		"""Shows the selected solid body."""
		self._instance.ShowSolidBody = value

	@property
	def sketch_d_intersections(self):
		"""Creates new sketch segments based on the selected surfaces."""
		return self._instance.Sketch3DIntersections

	@sketch_d_intersections.setter
	def sketch_d_intersections(self, value):
		"""Creates new sketch segments based on the selected surfaces."""
		self._instance.Sketch3DIntersections = value

	@property
	def sketch_add_constraints(self):
		"""Adds the specified constraint to the selected entities."""
		return self._instance.SketchAddConstraints

	@sketch_add_constraints.setter
	def sketch_add_constraints(self, value):
		"""Adds the specified constraint to the selected entities."""
		self._instance.SketchAddConstraints = value

	@property
	def sketch_align(self):
		"""Aligns the selected sketch entities."""
		return self._instance.SketchAlign

	@sketch_align.setter
	def sketch_align(self, value):
		"""Aligns the selected sketch entities."""
		self._instance.SketchAlign = value

	@property
	def sketch_arc(self):
		"""Creates an arc in the current model document."""
		return self._instance.SketchArc

	@sketch_arc.setter
	def sketch_arc(self, value):
		"""Creates an arc in the current model document."""
		self._instance.SketchArc = value

	@property
	def sketch_centerline(self):
		"""Adds a centerline to the current model document."""
		return self._instance.SketchCenterline

	@sketch_centerline.setter
	def sketch_centerline(self, value):
		"""Adds a centerline to the current model document."""
		self._instance.SketchCenterline = value

	@property
	def sketch_constrain_coincident(self):
		"""Makes the selected sketch entities coincident."""
		return self._instance.SketchConstrainCoincident

	@sketch_constrain_coincident.setter
	def sketch_constrain_coincident(self, value):
		"""Makes the selected sketch entities coincident."""
		self._instance.SketchConstrainCoincident = value

	@property
	def sketch_constrain_concentric(self):
		"""Makes the selected sketch entities concentric."""
		return self._instance.SketchConstrainConcentric

	@sketch_constrain_concentric.setter
	def sketch_constrain_concentric(self, value):
		"""Makes the selected sketch entities concentric."""
		self._instance.SketchConstrainConcentric = value

	@property
	def sketch_constrain_parallel(self):
		"""Makes the selected sketch entities parallel."""
		return self._instance.SketchConstrainParallel

	@sketch_constrain_parallel.setter
	def sketch_constrain_parallel(self, value):
		"""Makes the selected sketch entities parallel."""
		self._instance.SketchConstrainParallel = value

	@property
	def sketch_constrain_perp(self):
		"""Makes the selected sketch entities perpendicular."""
		return self._instance.SketchConstrainPerp

	@sketch_constrain_perp.setter
	def sketch_constrain_perp(self, value):
		"""Makes the selected sketch entities perpendicular."""
		self._instance.SketchConstrainPerp = value

	@property
	def sketch_constrain_tangent(self):
		"""Makes the selected entities tangent."""
		return self._instance.SketchConstrainTangent

	@sketch_constrain_tangent.setter
	def sketch_constrain_tangent(self, value):
		"""Makes the selected entities tangent."""
		self._instance.SketchConstrainTangent = value

	@property
	def sketch_constraints_del(self):
		"""Deletes the specified relationship (constraint) on the currently selected sketch item."""
		return self._instance.SketchConstraintsDel

	@sketch_constraints_del.setter
	def sketch_constraints_del(self, value):
		"""Deletes the specified relationship (constraint) on the currently selected sketch item."""
		self._instance.SketchConstraintsDel = value

	@property
	def sketch_constraints_del_all(self):
		"""Deletes all of the constraints on the currently selected sketch segment."""
		return self._instance.SketchConstraintsDelAll

	@sketch_constraints_del_all.setter
	def sketch_constraints_del_all(self, value):
		"""Deletes all of the constraints on the currently selected sketch segment."""
		self._instance.SketchConstraintsDelAll = value

	@property
	def sketch_convert_iso_curves(self):
		"""Converts ISO-parametric curves on a selected surface into a sketch entity."""
		return self._instance.SketchConvertIsoCurves

	@sketch_convert_iso_curves.setter
	def sketch_convert_iso_curves(self, value):
		"""Converts ISO-parametric curves on a selected surface into a sketch entity."""
		self._instance.SketchConvertIsoCurves = value

	@property
	def sketch_mirror(self):
		"""Creates new entities that are mirror images of the selected entities."""
		return self._instance.SketchMirror

	@sketch_mirror.setter
	def sketch_mirror(self, value):
		"""Creates new entities that are mirror images of the selected entities."""
		self._instance.SketchMirror = value

	@property
	def sketch_modify_flip(self):
		"""Flips the the active or selected sketch about the specified coordinate system axis."""
		return self._instance.SketchModifyFlip

	@sketch_modify_flip.setter
	def sketch_modify_flip(self, value):
		"""Flips the the active or selected sketch about the specified coordinate system axis."""
		self._instance.SketchModifyFlip = value

	@property
	def sketch_modify_rotate(self):
		"""Rotates the coordinate system of the active or selected sketch."""
		return self._instance.SketchModifyRotate

	@sketch_modify_rotate.setter
	def sketch_modify_rotate(self, value):
		"""Rotates the coordinate system of the active or selected sketch."""
		self._instance.SketchModifyRotate = value

	@property
	def sketch_modify_scale(self):
		"""Scales the active or selected sketch."""
		return self._instance.SketchModifyScale

	@sketch_modify_scale.setter
	def sketch_modify_scale(self, value):
		"""Scales the active or selected sketch."""
		self._instance.SketchModifyScale = value

	@property
	def sketch_modify_translate(self):
		"""Translates the coordinate system of the active or selected sketch."""
		return self._instance.SketchModifyTranslate

	@sketch_modify_translate.setter
	def sketch_modify_translate(self, value):
		"""Translates the coordinate system of the active or selected sketch."""
		self._instance.SketchModifyTranslate = value

	@property
	def sketch_offset_edges(self):
		"""Offsets the edges of the selected entities."""
		return self._instance.SketchOffsetEdges

	@sketch_offset_edges.setter
	def sketch_offset_edges(self, value):
		"""Offsets the edges of the selected entities."""
		self._instance.SketchOffsetEdges = value

	@property
	def sketch_offset_entities(self):
		"""Generates entities in the active sketch by offsetting the selected geometry by the specified amount."""
		return self._instance.SketchOffsetEntities2

	@sketch_offset_entities.setter
	def sketch_offset_entities(self, value):
		"""Generates entities in the active sketch by offsetting the selected geometry by the specified amount."""
		self._instance.SketchOffsetEntities2 = value

	@property
	def sketch_spline(self):
		"""Starts a spline, or continues one, using the specified point."""
		return self._instance.SketchSpline

	@sketch_spline.setter
	def sketch_spline(self, value):
		"""Starts a spline, or continues one, using the specified point."""
		self._instance.SketchSpline = value

	@property
	def sketch_tangent_arc(self):
		"""Creates a tangent arc in the current model document."""
		return self._instance.SketchTangentArc

	@sketch_tangent_arc.setter
	def sketch_tangent_arc(self, value):
		"""Creates a tangent arc in the current model document."""
		self._instance.SketchTangentArc = value

	@property
	def sketch_undo(self):
		"""Undoes the last sketch command."""
		return self._instance.SketchUndo

	@sketch_undo.setter
	def sketch_undo(self, value):
		"""Undoes the last sketch command."""
		self._instance.SketchUndo = value

	@property
	def sketch_use_edge_ctrline(self):
		"""Uses this centerline in sketch."""
		return self._instance.SketchUseEdgeCtrline

	@sketch_use_edge_ctrline.setter
	def sketch_use_edge_ctrline(self, value):
		"""Uses this centerline in sketch."""
		self._instance.SketchUseEdgeCtrline = value

	@property
	def sk_tools_auto_constr(self):
		"""Automatically constrains the active sketch."""
		return self._instance.SkToolsAutoConstr

	@sk_tools_auto_constr.setter
	def sk_tools_auto_constr(self, value):
		"""Automatically constrains the active sketch."""
		self._instance.SkToolsAutoConstr = value

	@property
	def toolbars(self):
		"""Turns the specified SOLIDWORKS toolbars on and off."""
		return self._instance.Toolbars

	@toolbars.setter
	def toolbars(self, value):
		"""Turns the specified SOLIDWORKS toolbars on and off."""
		self._instance.Toolbars = value

	@property
	def tools_distance(self):
		"""Computes distance."""
		return self._instance.ToolsDistance

	@tools_distance.setter
	def tools_distance(self, value):
		"""Computes distance."""
		self._instance.ToolsDistance = value

	@property
	def tools_grid(self):
		"""Shows and hides the grid in this model document."""
		return self._instance.ToolsGrid

	@tools_grid.setter
	def tools_grid(self, value):
		"""Shows and hides the grid in this model document."""
		self._instance.ToolsGrid = value

	@property
	def tools_macro(self):
		"""Not implemented."""
		return self._instance.ToolsMacro

	@tools_macro.setter
	def tools_macro(self, value):
		"""Not implemented."""
		self._instance.ToolsMacro = value

	@property
	def tools_mass_props(self):
		"""Calculates the mass properties."""
		return self._instance.ToolsMassProps

	@tools_mass_props.setter
	def tools_mass_props(self, value):
		"""Calculates the mass properties."""
		self._instance.ToolsMassProps = value

	@property
	def tools_sketch_scale(self):
		"""Scales a sketch."""
		return self._instance.ToolsSketchScale

	@tools_sketch_scale.setter
	def tools_sketch_scale(self, value):
		"""Scales a sketch."""
		self._instance.ToolsSketchScale = value

	@property
	def tools_sketch_translate(self):
		"""Translates a sketch."""
		return self._instance.ToolsSketchTranslate

	@tools_sketch_translate.setter
	def tools_sketch_translate(self, value):
		"""Translates a sketch."""
		self._instance.ToolsSketchTranslate = value

	@property
	def un_blank_ref_geom(self):
		"""Shows the selected, hidden reference geometry in the graphics window."""
		return self._instance.UnBlankRefGeom

	@un_blank_ref_geom.setter
	def un_blank_ref_geom(self, value):
		"""Shows the selected, hidden reference geometry in the graphics window."""
		self._instance.UnBlankRefGeom = value

	@property
	def unblank_sketch(self):
		"""Shows a hidden sketch."""
		return self._instance.UnblankSketch

	@unblank_sketch.setter
	def unblank_sketch(self, value):
		"""Shows a hidden sketch."""
		self._instance.UnblankSketch = value

	@property
	def underive_sketch(self):
		"""Changes a sketch to underived."""
		return self._instance.UnderiveSketch

	@underive_sketch.setter
	def underive_sketch(self, value):
		"""Changes a sketch to underived."""
		self._instance.UnderiveSketch = value

	@property
	def un_lock(self):
		"""Reverses IModelDoc2::Lock and changes the status bar message to Process Complete."""
		return self._instance.UnLock

	@un_lock.setter
	def un_lock(self, value):
		"""Reverses IModelDoc2::Lock and changes the status bar message to Process Complete."""
		self._instance.UnLock = value

	@property
	def unlock_all_external_references(self):
		"""Unlocks all external references."""
		return self._instance.UnlockAllExternalReferences

	@unlock_all_external_references.setter
	def unlock_all_external_references(self, value):
		"""Unlocks all external references."""
		self._instance.UnlockAllExternalReferences = value

	@property
	def user_favors(self):
		"""Specifies whether geometric relations are automatically created as you add sketch entities."""
		return self._instance.UserFavors

	@user_favors.setter
	def user_favors(self, value):
		"""Specifies whether geometric relations are automatically created as you add sketch entities."""
		self._instance.UserFavors = value

	@property
	def version_history(self):
		"""Gets an array of strings indicating the versions in which this document was saved, including the SOLIDWORKS version in which the model document is currently opened and which is the last value returned in the array."""
		return self._instance.VersionHistory

	@version_history.setter
	def version_history(self, value):
		"""Gets an array of strings indicating the versions in which this document was saved, including the SOLIDWORKS version in which the model document is currently opened and which is the last value returned in the array."""
		self._instance.VersionHistory = value

	@property
	def view_constraint(self):
		"""Shows the constraints for the current model document."""
		return self._instance.ViewConstraint

	@view_constraint.setter
	def view_constraint(self, value):
		"""Shows the constraints for the current model document."""
		self._instance.ViewConstraint = value

	@property
	def view_disp_coordinate_systems(self):
		"""Toggles the display of coordinate systems on and off."""
		return self._instance.ViewDispCoordinateSystems

	@view_disp_coordinate_systems.setter
	def view_disp_coordinate_systems(self, value):
		"""Toggles the display of coordinate systems on and off."""
		self._instance.ViewDispCoordinateSystems = value

	@property
	def view_display_curvature(self):
		"""Toggles the display of surface curvature on and off."""
		return self._instance.ViewDisplayCurvature

	@view_display_curvature.setter
	def view_display_curvature(self, value):
		"""Toggles the display of surface curvature on and off."""
		self._instance.ViewDisplayCurvature = value

	@property
	def view_display_faceted(self):
		"""Sets the current display mode to show the facets that make up a shaded picture of STL output."""
		return self._instance.ViewDisplayFaceted

	@view_display_faceted.setter
	def view_display_faceted(self, value):
		"""Sets the current display mode to show the facets that make up a shaded picture of STL output."""
		self._instance.ViewDisplayFaceted = value

	@property
	def view_display_hiddengreyed(self):
		"""Sets the current display mode to Hidden Lines Visible."""
		return self._instance.ViewDisplayHiddengreyed

	@view_display_hiddengreyed.setter
	def view_display_hiddengreyed(self, value):
		"""Sets the current display mode to Hidden Lines Visible."""
		self._instance.ViewDisplayHiddengreyed = value

	@property
	def view_display_hiddenremoved(self):
		"""Sets the current display mode to Hidden Lines Removed."""
		return self._instance.ViewDisplayHiddenremoved

	@view_display_hiddenremoved.setter
	def view_display_hiddenremoved(self, value):
		"""Sets the current display mode to Hidden Lines Removed."""
		self._instance.ViewDisplayHiddenremoved = value

	@property
	def view_display_shaded(self):
		"""Sets the current display mode to Shaded."""
		return self._instance.ViewDisplayShaded

	@view_display_shaded.setter
	def view_display_shaded(self, value):
		"""Sets the current display mode to Shaded."""
		self._instance.ViewDisplayShaded = value

	@property
	def view_display_wireframe(self):
		"""Sets the current display mode to Wireframe."""
		return self._instance.ViewDisplayWireframe

	@view_display_wireframe.setter
	def view_display_wireframe(self, value):
		"""Sets the current display mode to Wireframe."""
		self._instance.ViewDisplayWireframe = value

	@property
	def view_disp_origins(self):
		"""Toggles the display of origins off and on."""
		return self._instance.ViewDispOrigins

	@view_disp_origins.setter
	def view_disp_origins(self, value):
		"""Toggles the display of origins off and on."""
		self._instance.ViewDispOrigins = value

	@property
	def view_disp_refaxes(self):
		"""Toggles the display of reference axis on and off."""
		return self._instance.ViewDispRefaxes

	@view_disp_refaxes.setter
	def view_disp_refaxes(self, value):
		"""Toggles the display of reference axis on and off."""
		self._instance.ViewDispRefaxes = value

	@property
	def view_disp_refplanes(self):
		"""Toggles the display of reference planes on and off."""
		return self._instance.ViewDispRefplanes

	@view_disp_refplanes.setter
	def view_disp_refplanes(self, value):
		"""Toggles the display of reference planes on and off."""
		self._instance.ViewDispRefplanes = value

	@property
	def view_disp_ref_points(self):
		"""Shows and hides the reference points for the current model document."""
		return self._instance.ViewDispRefPoints

	@view_disp_ref_points.setter
	def view_disp_ref_points(self, value):
		"""Shows and hides the reference points for the current model document."""
		self._instance.ViewDispRefPoints = value

	@property
	def view_disp_temp_refaxes(self):
		"""Toggles the display of temporary reference axes on and off."""
		return self._instance.ViewDispTempRefaxes

	@view_disp_temp_refaxes.setter
	def view_disp_temp_refaxes(self, value):
		"""Toggles the display of temporary reference axes on and off."""
		self._instance.ViewDispTempRefaxes = value

	@property
	def view_ogl_shading(self):
		"""Sets the current display subsystem to use OpenGL."""
		return self._instance.ViewOglShading

	@view_ogl_shading.setter
	def view_ogl_shading(self, value):
		"""Sets the current display subsystem to use OpenGL."""
		self._instance.ViewOglShading = value

	@property
	def view_orientation_undo(self):
		"""Undoes previous view orientation changes that were made interactively by the user."""
		return self._instance.ViewOrientationUndo

	@view_orientation_undo.setter
	def view_orientation_undo(self, value):
		"""Undoes previous view orientation changes that were made interactively by the user."""
		self._instance.ViewOrientationUndo = value

	@property
	def view_rotate(self):
		"""Rotates the view of the current model."""
		return self._instance.ViewRotate

	@view_rotate.setter
	def view_rotate(self, value):
		"""Rotates the view of the current model."""
		self._instance.ViewRotate = value

	@property
	def view_rotateminusx(self):
		"""Dynamically rotates the view around x in a negative direction with the current increment."""
		return self._instance.ViewRotateminusx

	@view_rotateminusx.setter
	def view_rotateminusx(self, value):
		"""Dynamically rotates the view around x in a negative direction with the current increment."""
		self._instance.ViewRotateminusx = value

	@property
	def view_rotateminusy(self):
		"""Dynamically rotates the view around y in a negative direction with the current increment."""
		return self._instance.ViewRotateminusy

	@view_rotateminusy.setter
	def view_rotateminusy(self, value):
		"""Dynamically rotates the view around y in a negative direction with the current increment."""
		self._instance.ViewRotateminusy = value

	@property
	def view_rotateminusz(self):
		"""Dynamically rotates the view around z in a negative direction with the current increment."""
		return self._instance.ViewRotateminusz

	@view_rotateminusz.setter
	def view_rotateminusz(self, value):
		"""Dynamically rotates the view around z in a negative direction with the current increment."""
		self._instance.ViewRotateminusz = value

	@property
	def view_rotateplusx(self):
		"""Rotates the view around x in a positive direction with the current increment."""
		return self._instance.ViewRotateplusx

	@view_rotateplusx.setter
	def view_rotateplusx(self, value):
		"""Rotates the view around x in a positive direction with the current increment."""
		self._instance.ViewRotateplusx = value

	@property
	def view_rotateplusy(self):
		"""Rotates the view around y in a positive direction with the current increment."""
		return self._instance.ViewRotateplusy

	@view_rotateplusy.setter
	def view_rotateplusy(self, value):
		"""Rotates the view around y in a positive direction with the current increment."""
		self._instance.ViewRotateplusy = value

	@property
	def view_rotateplusz(self):
		"""Rotates the view around z in a positive direction with the current increment."""
		return self._instance.ViewRotateplusz

	@view_rotateplusz.setter
	def view_rotateplusz(self, value):
		"""Rotates the view around z in a positive direction with the current increment."""
		self._instance.ViewRotateplusz = value

	@property
	def view_rot_x_minus_ninety(self):
		"""Dynamically rotates the view by negative 90 about x."""
		return self._instance.ViewRotXMinusNinety

	@view_rot_x_minus_ninety.setter
	def view_rot_x_minus_ninety(self, value):
		"""Dynamically rotates the view by negative 90 about x."""
		self._instance.ViewRotXMinusNinety = value

	@property
	def view_rot_x_plus_ninety(self):
		"""Dynamically rotates the view by 90 about x."""
		return self._instance.ViewRotXPlusNinety

	@view_rot_x_plus_ninety.setter
	def view_rot_x_plus_ninety(self, value):
		"""Dynamically rotates the view by 90 about x."""
		self._instance.ViewRotXPlusNinety = value

	@property
	def view_rot_y_minus_ninety(self):
		"""Dynamically rotates the view by negative 90 about y."""
		return self._instance.ViewRotYMinusNinety

	@view_rot_y_minus_ninety.setter
	def view_rot_y_minus_ninety(self, value):
		"""Dynamically rotates the view by negative 90 about y."""
		self._instance.ViewRotYMinusNinety = value

	@property
	def view_rot_y_plus_ninety(self):
		"""Dynamically rotates the view by 90 about y."""
		return self._instance.ViewRotYPlusNinety

	@view_rot_y_plus_ninety.setter
	def view_rot_y_plus_ninety(self, value):
		"""Dynamically rotates the view by 90 about y."""
		self._instance.ViewRotYPlusNinety = value

	@property
	def view_rw_shading(self):
		"""Sets the current display subsystem to use renderware."""
		return self._instance.ViewRwShading

	@view_rw_shading.setter
	def view_rw_shading(self, value):
		"""Sets the current display subsystem to use renderware."""
		self._instance.ViewRwShading = value

	@property
	def view_translate(self):
		"""Translates the view."""
		return self._instance.ViewTranslate

	@view_translate.setter
	def view_translate(self, value):
		"""Translates the view."""
		self._instance.ViewTranslate = value

	@property
	def view_translateminusx(self):
		"""Dynamically shifts the view left."""
		return self._instance.ViewTranslateminusx

	@view_translateminusx.setter
	def view_translateminusx(self, value):
		"""Dynamically shifts the view left."""
		self._instance.ViewTranslateminusx = value

	@property
	def view_translateminusy(self):
		"""Dynamically shifts the view down."""
		return self._instance.ViewTranslateminusy

	@view_translateminusy.setter
	def view_translateminusy(self, value):
		"""Dynamically shifts the view down."""
		self._instance.ViewTranslateminusy = value

	@property
	def view_translateplusx(self):
		"""Dynamically shifts the view right."""
		return self._instance.ViewTranslateplusx

	@view_translateplusx.setter
	def view_translateplusx(self, value):
		"""Dynamically shifts the view right."""
		self._instance.ViewTranslateplusx = value

	@property
	def view_translateplusy(self):
		"""Dynamically shifts the view up."""
		return self._instance.ViewTranslateplusy

	@view_translateplusy.setter
	def view_translateplusy(self, value):
		"""Dynamically shifts the view up."""
		self._instance.ViewTranslateplusy = value

	@property
	def view_zoomin(self):
		"""Zooms the current view in by a factor of 20%."""
		return self._instance.ViewZoomin

	@view_zoomin.setter
	def view_zoomin(self, value):
		"""Zooms the current view in by a factor of 20%."""
		self._instance.ViewZoomin = value

	@property
	def view_zoomout(self):
		"""Zooms the current view out by a factor of 20%."""
		return self._instance.ViewZoomout

	@view_zoomout.setter
	def view_zoomout(self, value):
		"""Zooms the current view out by a factor of 20%."""
		self._instance.ViewZoomout = value

	@property
	def view_zoomto(self):
		"""Zooms the view to the selected box."""
		return self._instance.ViewZoomto

	@view_zoomto.setter
	def view_zoomto(self, value):
		"""Zooms the view to the selected box."""
		self._instance.ViewZoomto = value

	@property
	def view_zoom_to(self):
		"""Zooms to the specified region."""
		return self._instance.ViewZoomTo2

	@view_zoom_to.setter
	def view_zoom_to(self, value):
		"""Zooms to the specified region."""
		self._instance.ViewZoomTo2 = value

	@property
	def view_zoomtofit(self):
		"""Zooms the currently active view to fit the screen."""
		return self._instance.ViewZoomtofit2

	@view_zoomtofit.setter
	def view_zoomtofit(self, value):
		"""Zooms the currently active view to fit the screen."""
		self._instance.ViewZoomtofit2 = value

	@property
	def view_zoom_to_selection(self):
		"""Zooms the display to the selection."""
		return self._instance.ViewZoomToSelection

	@view_zoom_to_selection.setter
	def view_zoom_to_selection(self, value):
		"""Zooms the display to the selection."""
		self._instance.ViewZoomToSelection = value

	@property
	def window_redraw(self):
		"""Redraws the current window."""
		return self._instance.WindowRedraw

	@window_redraw.setter
	def window_redraw(self, value):
		"""Redraws the current window."""
		self._instance.WindowRedraw = value

