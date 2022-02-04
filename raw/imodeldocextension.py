# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html
class IModelDocExtension:
	def __init__(self, parent=None):
		self._instance = parent

	def active_command_tab(self):
		"""Gets and sets the active SOLIDWORKS CommandManager tab."""
		# return self._instance.ActiveCommandTab
		raise NotImplemented

	def active_command_tab_index(self):
		"""Gets and sets the index of the active SOLIDWORKS CommandManager tab."""
		# return self._instance.ActiveCommandTabIndex
		raise NotImplemented

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

	def command_tab_visible(self, tab_index):
		"""
		Gets and sets the visibility of the specified SOLIDWORKS CommandManager tab.
		:param tab_index: Index of the tab for which to get or set visibility
		"""
		# return self._instance.CommandTabVisible(tab_index)
		raise NotImplemented

	@property
	def custom_property_builder_template(self):
		"""Gets or sets the custom property builder template for this part."""
		return self._instance.CustomPropertyBuilderTemplate

	@custom_property_builder_template.setter
	def custom_property_builder_template(self, value):
		"""Gets or sets the custom property builder template for this part."""
		self._instance.CustomPropertyBuilderTemplate = value

	@property
	def custom_property_manager(self):
		"""Gets the custom properties for this document or configuration."""
		return self._instance.CustomPropertyManager

	@custom_property_manager.setter
	def custom_property_manager(self, value):
		"""Gets the custom properties for this document or configuration."""
		self._instance.CustomPropertyManager = value

	@property
	def dim_xpert_manager(self):
		"""Gets the DimXpert schema for this configuration."""
		return self._instance.DimXpertManager

	@dim_xpert_manager.setter
	def dim_xpert_manager(self, value):
		"""Gets the DimXpert schema for this configuration."""
		self._instance.DimXpertManager = value

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

	@property
	def document(self):
		"""Gets the model document."""
		return self._instance.Document

	@document.setter
	def document(self, value):
		"""Gets the model document."""
		self._instance.Document = value

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

	@property
	def needs_rebuild(self):
		"""Gets whether the model document needs to be rebuilt."""
		return self._instance.NeedsRebuild2

	@needs_rebuild.setter
	def needs_rebuild(self, value):
		"""Gets whether the model document needs to be rebuilt."""
		self._instance.NeedsRebuild2 = value

	@property
	def show_part_rebuild_indicators(self):
		"""Gets or sets whether to display rebuild indicators on parts that have out-of-date frozen features."""
		return self._instance.ShowPartRebuildIndicators

	@show_part_rebuild_indicators.setter
	def show_part_rebuild_indicators(self, value):
		"""Gets or sets whether to display rebuild indicators on parts that have out-of-date frozen features."""
		self._instance.ShowPartRebuildIndicators = value

	@property
	def sun_light_information(self):
		"""Gets the specified sunlight information."""
		return self._instance.SunLightInformation

	@sun_light_information.setter
	def sun_light_information(self, value):
		"""Gets the specified sunlight information."""
		self._instance.SunLightInformation = value

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
		"""Gets or sets whether this document uses its own page setup values, SOLIDWORKS application page setup values, or setup values on individual drawing sheets."""
		return self._instance.UsePageSetup

	@use_page_setup.setter
	def use_page_setup(self, value):
		"""Gets or sets whether this document uses its own page setup values, SOLIDWORKS application page setup values, or setup values on individual drawing sheets."""
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

	@property
	def add_angular_running_dim(self):
		"""Adds the specified angular running dimension for selected entities."""
		return self._instance.AddAngularRunningDim

	@add_angular_running_dim.setter
	def add_angular_running_dim(self, value):
		"""Adds the specified angular running dimension for selected entities."""
		self._instance.AddAngularRunningDim = value

	@property
	def add_comment(self):
		"""Adds a comment to this document's Comment Folder."""
		return self._instance.AddComment

	@add_comment.setter
	def add_comment(self, value):
		"""Adds a comment to this document's Comment Folder."""
		self._instance.AddComment = value

	@property
	def add_decal(self):
		"""Adds a decal to the model."""
		return self._instance.AddDecal

	@add_decal.setter
	def add_decal(self, value):
		"""Adds a decal to the model."""
		self._instance.AddDecal = value

	@property
	def add_default_render_material(self):
		"""Not supported in SOLIDWORKS 2011 and later and not superseded."""
		return self._instance.AddDefaultRenderMaterial

	@add_default_render_material.setter
	def add_default_render_material(self, value):
		"""Not supported in SOLIDWORKS 2011 and later and not superseded."""
		self._instance.AddDefaultRenderMaterial = value

	@property
	def add_dimension(self):
		"""Creates a display dimension at the specified location for selected entities."""
		return self._instance.AddDimension

	@add_dimension.setter
	def add_dimension(self, value):
		"""Creates a display dimension at the specified location for selected entities."""
		self._instance.AddDimension = value

	@property
	def add_display_state_specific_render_material(self):
		"""Adds the specified appearance to the specified display states in the active configuration and returns the IDs assigned to that appearance."""
		return self._instance.AddDisplayStateSpecificRenderMaterial

	@add_display_state_specific_render_material.setter
	def add_display_state_specific_render_material(self, value):
		"""Adds the specified appearance to the specified display states in the active configuration and returns the IDs assigned to that appearance."""
		self._instance.AddDisplayStateSpecificRenderMaterial = value

	@property
	def add_ordinate_dimension(self):
		"""Inserts an ordinate dimension."""
		return self._instance.AddOrdinateDimension

	@add_ordinate_dimension.setter
	def add_ordinate_dimension(self, value):
		"""Inserts an ordinate dimension."""
		self._instance.AddOrdinateDimension = value

	@property
	def add_or_update_search_data(self):
		"""Adds or updates the SOLIDWORKS Search, third-party, application keyword and value to the model document."""
		return self._instance.AddOrUpdateSearchData

	@add_or_update_search_data.setter
	def add_or_update_search_data(self, value):
		"""Adds or updates the SOLIDWORKS Search, third-party, application keyword and value to the model document."""
		self._instance.AddOrUpdateSearchData = value

	@property
	def add_path_length_dim(self):
		"""Inserts a path length dimension at the specified coordinates for a selected path."""
		return self._instance.AddPathLengthDim

	@add_path_length_dim.setter
	def add_path_length_dim(self, value):
		"""Inserts a path length dimension at the specified coordinates for a selected path."""
		self._instance.AddPathLengthDim = value

	@property
	def add_render_material(self):
		"""Not supported in SOLIDWORKS 2011 and later. Superseded by IModelDocExtension::AddDisplayStateSpecificRenderMaterial and IModelDocExtension::IAddDisplayStateSpecificRenderMaterial."""
		return self._instance.AddRenderMaterial

	@add_render_material.setter
	def add_render_material(self, value):
		"""Not supported in SOLIDWORKS 2011 and later. Superseded by IModelDocExtension::AddDisplayStateSpecificRenderMaterial and IModelDocExtension::IAddDisplayStateSpecificRenderMaterial."""
		self._instance.AddRenderMaterial = value

	@property
	def add_specific_dimension(self):
		"""Creates the specified display dimension at the specified location for selected entities."""
		return self._instance.AddSpecificDimension

	@add_specific_dimension.setter
	def add_specific_dimension(self, value):
		"""Creates the specified display dimension at the specified location for selected entities."""
		self._instance.AddSpecificDimension = value

	@property
	def add_symmetric_dimension(self):
		"""Creates a full symmetrical angular dimension at the specified location for the selected entities."""
		return self._instance.AddSymmetricDimension

	@add_symmetric_dimension.setter
	def add_symmetric_dimension(self, value):
		"""Creates a full symmetrical angular dimension at the specified location for the selected entities."""
		self._instance.AddSymmetricDimension = value

	@property
	def align_dimensions(self):
		"""Aligns the selected dimensions in drawing documents."""
		return self._instance.AlignDimensions

	@align_dimensions.setter
	def align_dimensions(self, value):
		"""Aligns the selected dimensions in drawing documents."""
		self._instance.AlignDimensions = value

	@property
	def align_running_dimension(self):
		"""Aligns the extension lines of all angular dimensions to be the same distance from the center as the baseline dimension (0⁰) in the set of angular running dimensions."""
		return self._instance.AlignRunningDimension

	@align_running_dimension.setter
	def align_running_dimension(self, value):
		"""Aligns the extension lines of all angular dimensions to be the same distance from the center as the baseline dimension (0⁰) in the set of angular running dimensions."""
		self._instance.AlignRunningDimension = value

	@property
	def apply_format_painter_to_all(self):
		"""Applies Format Painter to all dimensions and annotations in the active document."""
		return self._instance.ApplyFormatPainterToAll

	@apply_format_painter_to_all.setter
	def apply_format_painter_to_all(self, value):
		"""Applies Format Painter to all dimensions and annotations in the active document."""
		self._instance.ApplyFormatPainterToAll = value

	@property
	def break_all_external_file_references(self):
		"""Breaks all external references and allows you to insert the features of the original part, or parts, if the external references are broken."""
		return self._instance.BreakAllExternalFileReferences2

	@break_all_external_file_references.setter
	def break_all_external_file_references(self, value):
		"""Breaks all external references and allows you to insert the features of the original part, or parts, if the external references are broken."""
		self._instance.BreakAllExternalFileReferences2 = value

	@property
	def capture_d_view(self):
		"""Captures the 3D View of this part or assembly."""
		return self._instance.Capture3DView

	@capture_d_view.setter
	def capture_d_view(self, value):
		"""Captures the 3D View of this part or assembly."""
		self._instance.Capture3DView = value

	@property
	def change_sketch_plane(self):
		"""Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations."""
		return self._instance.ChangeSketchPlane

	@change_sketch_plane.setter
	def change_sketch_plane(self, value):
		"""Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations."""
		self._instance.ChangeSketchPlane = value

	@property
	def compare_d_p_m_i(self):
		"""Compare DimXpert annotations, reference dimensions, and other annotations between different versions of the same part document."""
		return self._instance.Compare3DPMI

	@compare_d_p_m_i.setter
	def compare_d_p_m_i(self, value):
		"""Compare DimXpert annotations, reference dimensions, and other annotations between different versions of the same part document."""
		self._instance.Compare3DPMI = value

	@property
	def copy_drafting_standard(self):
		"""Copy the current custom drafting standard."""
		return self._instance.CopyDraftingStandard

	@copy_drafting_standard.setter
	def copy_drafting_standard(self, value):
		"""Copy the current custom drafting standard."""
		self._instance.CopyDraftingStandard = value

	@property
	def create_d_bounding_box(self):
		"""Creates a 3D bounding box for a cut list item in a weldment part."""
		return self._instance.Create3DBoundingBox

	@create_d_bounding_box.setter
	def create_d_bounding_box(self, value):
		"""Creates a 3D bounding box for a cut list item in a weldment part."""
		self._instance.Create3DBoundingBox = value

	@property
	def create_advanced_hole_element_data(self):
		"""Creates an Advanced Hole element data object of the specified type."""
		return self._instance.CreateAdvancedHoleElementData

	@create_advanced_hole_element_data.setter
	def create_advanced_hole_element_data(self, value):
		"""Creates an Advanced Hole element data object of the specified type."""
		self._instance.CreateAdvancedHoleElementData = value

	@property
	def create_balloon_options(self):
		"""Creates an object that stores BOM balloon options."""
		return self._instance.CreateBalloonOptions

	@create_balloon_options.setter
	def create_balloon_options(self, value):
		"""Creates an object that stores BOM balloon options."""
		self._instance.CreateBalloonOptions = value

	@property
	def create_callout(self):
		"""Creates a callout independent of a selection."""
		return self._instance.CreateCallout

	@create_callout.setter
	def create_callout(self, value):
		"""Creates a callout independent of a selection."""
		self._instance.CreateCallout = value

	@property
	def create_decal(self):
		"""Creates a decal for this model."""
		return self._instance.CreateDecal

	@create_decal.setter
	def create_decal(self, value):
		"""Creates a decal for this model."""
		self._instance.CreateDecal = value

	@property
	def create_mass_property(self):
		"""Creates a mass properties object."""
		return self._instance.CreateMassProperty2

	@create_mass_property.setter
	def create_mass_property(self, value):
		"""Creates a mass properties object."""
		self._instance.CreateMassProperty2 = value

	@property
	def create_measure(self):
		"""Creates a measure tool."""
		return self._instance.CreateMeasure

	@create_measure.setter
	def create_measure(self, value):
		"""Creates a measure tool."""
		self._instance.CreateMeasure = value

	@property
	def create_o_l_e_object(self):
		"""Creates an OLE object on the active document."""
		return self._instance.CreateOLEObject

	@create_o_l_e_object.setter
	def create_o_l_e_object(self, value):
		"""Creates an OLE object on the active document."""
		self._instance.CreateOLEObject = value

	@property
	def create_render_material(self):
		"""Creates an appearance for this model."""
		return self._instance.CreateRenderMaterial

	@create_render_material.setter
	def create_render_material(self, value):
		"""Creates an appearance for this model."""
		self._instance.CreateRenderMaterial = value

	@property
	def create_stacked_balloon_options(self):
		"""Creates an object that stores options for stacked balloons."""
		return self._instance.CreateStackedBalloonOptions

	@create_stacked_balloon_options.setter
	def create_stacked_balloon_options(self, value):
		"""Creates an object that stores options for stacked balloons."""
		self._instance.CreateStackedBalloonOptions = value

	@property
	def create_texture(self):
		"""Creates a texture."""
		return self._instance.CreateTexture

	@create_texture.setter
	def create_texture(self, value):
		"""Creates a texture."""
		self._instance.CreateTexture = value

	@property
	def delete_all_decals(self):
		"""Deletes all decals on this model."""
		return self._instance.DeleteAllDecals

	@delete_all_decals.setter
	def delete_all_decals(self, value):
		"""Deletes all decals on this model."""
		self._instance.DeleteAllDecals = value

	@property
	def delete_attachment(self):
		"""Deletes the specified file in the Attachments folder in the FeatureManager design tree."""
		return self._instance.DeleteAttachment

	@delete_attachment.setter
	def delete_attachment(self, value):
		"""Deletes the specified file in the Attachments folder in the FeatureManager design tree."""
		self._instance.DeleteAttachment = value

	@property
	def delete_decal(self):
		"""Removes the specified decal from this model."""
		return self._instance.DeleteDecal

	@delete_decal.setter
	def delete_decal(self, value):
		"""Removes the specified decal from this model."""
		self._instance.DeleteDecal = value

	@property
	def delete_display_state_specific_render_material(self):
		"""Deletes the specified appearances, using the IDs of the appearances, from the active configuration."""
		return self._instance.DeleteDisplayStateSpecificRenderMaterial

	@delete_display_state_specific_render_material.setter
	def delete_display_state_specific_render_material(self, value):
		"""Deletes the specified appearances, using the IDs of the appearances, from the active configuration."""
		self._instance.DeleteDisplayStateSpecificRenderMaterial = value

	@property
	def delete_drafting_standard(self):
		"""Delete the current custom drafting standard."""
		return self._instance.DeleteDraftingStandard

	@delete_drafting_standard.setter
	def delete_drafting_standard(self, value):
		"""Delete the current custom drafting standard."""
		self._instance.DeleteDraftingStandard = value

	@property
	def delete_feature_mgr_viewx(self):
		"""Removes the specified tab in the FeatureManager design tree in 64-bit applications."""
		return self._instance.DeleteFeatureMgrViewx64

	@delete_feature_mgr_viewx.setter
	def delete_feature_mgr_viewx(self, value):
		"""Removes the specified tab in the FeatureManager design tree in 64-bit applications."""
		self._instance.DeleteFeatureMgrViewx64 = value

	@property
	def delete_render_material(self):
		"""Not supported in SOLIDWORKS 2011 and later. Superseded by IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial and IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial."""
		return self._instance.DeleteRenderMaterial

	@delete_render_material.setter
	def delete_render_material(self, value):
		"""Not supported in SOLIDWORKS 2011 and later. Superseded by IModelDocExtension::DeleteDisplayStateSpecificRenderMaterial and IModelDocExtension::IDeleteDisplayStateSpecificRenderMaterial."""
		self._instance.DeleteRenderMaterial = value

	@property
	def delete_scene(self):
		"""Deletes the scene applied to this model."""
		return self._instance.DeleteScene

	@delete_scene.setter
	def delete_scene(self, value):
		"""Deletes the scene applied to this model."""
		self._instance.DeleteScene = value

	@property
	def delete_search_data(self):
		"""Deletes the specified SOLIDWORKS Search third-party keywords from the model document."""
		return self._instance.DeleteSearchData

	@delete_search_data.setter
	def delete_search_data(self, value):
		"""Deletes the specified SOLIDWORKS Search third-party keywords from the model document."""
		self._instance.DeleteSearchData = value

	@property
	def delete_selection(self):
		"""Deletes the selected items, with the option to delete absorbed features, child features, or both."""
		return self._instance.DeleteSelection2

	@delete_selection.setter
	def delete_selection(self, value):
		"""Deletes the selected items, with the option to delete absorbed features, child features, or both."""
		self._instance.DeleteSelection2 = value

	@property
	def edit_balloon_properties(self):
		"""Edits the selected balloon's properties."""
		return self._instance.EditBalloonProperties2

	@edit_balloon_properties.setter
	def edit_balloon_properties(self, value):
		"""Edits the selected balloon's properties."""
		self._instance.EditBalloonProperties2 = value

	@property
	def edit_dimension_properties(self):
		"""Edits the selected dimension."""
		return self._instance.EditDimensionProperties

	@edit_dimension_properties.setter
	def edit_dimension_properties(self, value):
		"""Edits the selected dimension."""
		self._instance.EditDimensionProperties = value

	@property
	def edit_rebuild_all(self):
		"""Rebuilds only those features that need to be rebuilt in all configurations without activating each configuration."""
		return self._instance.EditRebuildAll

	@edit_rebuild_all.setter
	def edit_rebuild_all(self, value):
		"""Rebuilds only those features that need to be rebuilt in all configurations without activating each configuration."""
		self._instance.EditRebuildAll = value

	@property
	def find_tracked_objects(self):
		"""Finds the tracking IDs assigned to entities in this document."""
		return self._instance.FindTrackedObjects

	@find_tracked_objects.setter
	def find_tracked_objects(self, value):
		"""Finds the tracking IDs assigned to entities in this document."""
		self._instance.FindTrackedObjects = value

	@property
	def finish_recording_undo_object(self):
		"""Ends recording of a SOLIDWORKS Undo object with the specified name and visibility."""
		return self._instance.FinishRecordingUndoObject2

	@finish_recording_undo_object.setter
	def finish_recording_undo_object(self, value):
		"""Ends recording of a SOLIDWORKS Undo object with the specified name and visibility."""
		self._instance.FinishRecordingUndoObject2 = value

	@property
	def force_rebuild_all(self):
		"""Forces a rebuild of all features in all configurations without activating each configuration."""
		return self._instance.ForceRebuildAll

	@force_rebuild_all.setter
	def force_rebuild_all(self, value):
		"""Forces a rebuild of all features in all configurations without activating each configuration."""
		self._instance.ForceRebuildAll = value

	@property
	def geodesic_sketch_offset(self):
		"""Creates a geodesic sketch offset along the curvature of a surface."""
		return self._instance.GeodesicSketchOffset

	@geodesic_sketch_offset.setter
	def geodesic_sketch_offset(self, value):
		"""Creates a geodesic sketch offset along the curvature of a surface."""
		self._instance.GeodesicSketchOffset = value

	@property
	def get_d_experience_model_type(self):
		"""Gets the type of 3DEXPERIENCE application that owns this model."""
		return self._instance.Get3DExperienceModelType

	@get_d_experience_model_type.setter
	def get_d_experience_model_type(self, value):
		"""Gets the type of 3DEXPERIENCE application that owns this model."""
		self._instance.Get3DExperienceModelType = value

	@property
	def get_d_view(self):
		"""Gets the 3D View with the specified name for this part or assembly."""
		return self._instance.Get3DView

	@get_d_view.setter
	def get_d_view(self, value):
		"""Gets the 3D View with the specified name for this part or assembly."""
		self._instance.Get3DView = value

	@property
	def get_d_view_count(self):
		"""Gets the number of 3D Views in this part or assembly."""
		return self._instance.Get3DViewCount

	@get_d_view_count.setter
	def get_d_view_count(self, value):
		"""Gets the number of 3D Views in this part or assembly."""
		self._instance.Get3DViewCount = value

	@property
	def get_d_view_names(self):
		"""Gets names of the 3D Views in this part or assembly."""
		return self._instance.Get3DViewNames

	@get_d_view_names.setter
	def get_d_view_names(self, value):
		"""Gets names of the 3D Views in this part or assembly."""
		self._instance.Get3DViewNames = value

	@property
	def get_d_views(self):
		"""Gets the 3D Views for this part or assembly."""
		return self._instance.Get3DViews

	@get_d_views.setter
	def get_d_views(self, value):
		"""Gets the 3D Views for this part or assembly."""
		self._instance.Get3DViews = value

	@property
	def get_active_property_manager_page(self):
		"""Gets the name of the active PropertyManager page."""
		return self._instance.GetActivePropertyManagerPage

	@get_active_property_manager_page.setter
	def get_active_property_manager_page(self, value):
		"""Gets the name of the active PropertyManager page."""
		self._instance.GetActivePropertyManagerPage = value

	@property
	def get_advanced_save_as_options(self):
		"""Gets the advanced File > Save As options."""
		return self._instance.GetAdvancedSaveAsOptions

	@get_advanced_save_as_options.setter
	def get_advanced_save_as_options(self, value):
		"""Gets the advanced File > Save As options."""
		self._instance.GetAdvancedSaveAsOptions = value

	@property
	def get_advanced_spot_light_properties(self):
		"""Gets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model."""
		return self._instance.GetAdvancedSpotLightProperties

	@get_advanced_spot_light_properties.setter
	def get_advanced_spot_light_properties(self, value):
		"""Gets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model."""
		self._instance.GetAdvancedSpotLightProperties = value

	@property
	def get_annotation_count(self):
		"""Gets the number of annotations on this part."""
		return self._instance.GetAnnotationCount

	@get_annotation_count.setter
	def get_annotation_count(self, value):
		"""Gets the number of annotations on this part."""
		self._instance.GetAnnotationCount = value

	@property
	def get_annotations(self):
		"""Gets the annotations on this part."""
		return self._instance.GetAnnotations

	@get_annotations.setter
	def get_annotations(self, value):
		"""Gets the annotations on this part."""
		self._instance.GetAnnotations = value

	@property
	def get_appearance_setting(self):
		"""Gets the appearance setting for this document."""
		return self._instance.GetAppearanceSetting

	@get_appearance_setting.setter
	def get_appearance_setting(self, value):
		"""Gets the appearance setting for this document."""
		self._instance.GetAppearanceSetting = value

	@property
	def get_attachment_count(self):
		"""Gets the number of attachments for this document."""
		return self._instance.GetAttachmentCount

	@get_attachment_count.setter
	def get_attachment_count(self, value):
		"""Gets the number of attachments for this document."""
		self._instance.GetAttachmentCount = value

	@property
	def get_attachments(self):
		"""Gets the attachments for this document."""
		return self._instance.GetAttachments

	@get_attachments.setter
	def get_attachments(self, value):
		"""Gets the attachments for this document."""
		self._instance.GetAttachments = value

	@property
	def get_callout_variable_string(self):
		"""Gets the string for the specified callout variable."""
		return self._instance.GetCalloutVariableString

	@get_callout_variable_string.setter
	def get_callout_variable_string(self, value):
		"""Gets the string for the specified callout variable."""
		self._instance.GetCalloutVariableString = value

	@property
	def get_camera_by_id(self):
		"""Gets a camera using the specified camera ID."""
		return self._instance.GetCameraById

	@get_camera_by_id.setter
	def get_camera_by_id(self, value):
		"""Gets a camera using the specified camera ID."""
		self._instance.GetCameraById = value

	@property
	def get_camera_count(self):
		"""Gets the number of cameras in the document."""
		return self._instance.GetCameraCount

	@get_camera_count.setter
	def get_camera_count(self, value):
		"""Gets the number of cameras in the document."""
		self._instance.GetCameraCount = value

	@property
	def get_camera_definition(self):
		"""Gets a camera, but does not add the newly created camera to the model."""
		return self._instance.GetCameraDefinition

	@get_camera_definition.setter
	def get_camera_definition(self, value):
		"""Gets a camera, but does not add the newly created camera to the model."""
		self._instance.GetCameraDefinition = value

	@property
	def get_command_tabs(self):
		"""Gets all of the SOLIDWORKS CommandManager tab names in this document."""
		return self._instance.GetCommandTabs

	@get_command_tabs.setter
	def get_command_tabs(self, value):
		"""Gets all of the SOLIDWORKS CommandManager tab names in this document."""
		self._instance.GetCommandTabs = value

	@property
	def get_coordinate_system_transform_by_name(self):
		"""Gets the transform of the specified coordinate system."""
		return self._instance.GetCoordinateSystemTransformByName

	@get_coordinate_system_transform_by_name.setter
	def get_coordinate_system_transform_by_name(self, value):
		"""Gets the transform of the specified coordinate system."""
		self._instance.GetCoordinateSystemTransformByName = value

	@property
	def get_corresponding(self):
		"""Gets the object in the underlying part or subassembly document that corresponds to the specified input object in this drawing view or assembly."""
		return self._instance.GetCorresponding2

	@get_corresponding.setter
	def get_corresponding(self, value):
		"""Gets the object in the underlying part or subassembly document that corresponds to the specified input object in this drawing view or assembly."""
		self._instance.GetCorresponding2 = value

	@property
	def get_corresponding_entity(self):
		"""Gets the entity in the underlying part or subassembly that corresponds to the specified entity in this assembly or drawing view."""
		return self._instance.GetCorrespondingEntity2

	@get_corresponding_entity.setter
	def get_corresponding_entity(self, value):
		"""Gets the entity in the underlying part or subassembly that corresponds to the specified entity in this assembly or drawing view."""
		self._instance.GetCorrespondingEntity2 = value

	@property
	def get_costing_manager(self):
		"""Gets the entry-point interface to the SOLIDWORKS Costing API and gets the CostingManager."""
		return self._instance.GetCostingManager

	@get_costing_manager.setter
	def get_costing_manager(self, value):
		"""Gets the entry-point interface to the SOLIDWORKS Costing API and gets the CostingManager."""
		self._instance.GetCostingManager = value

	@property
	def get_decal(self):
		"""Gets the specified decal in this model."""
		return self._instance.GetDecal

	@get_decal.setter
	def get_decal(self, value):
		"""Gets the specified decal in this model."""
		self._instance.GetDecal = value

	@property
	def get_decals(self):
		"""Gets the decals applied to the model."""
		return self._instance.GetDecals

	@get_decals.setter
	def get_decals(self, value):
		"""Gets the decals applied to the model."""
		self._instance.GetDecals = value

	@property
	def get_decals_count(self):
		"""Gets the number of decals applied to this model."""
		return self._instance.GetDecalsCount

	@get_decals_count.setter
	def get_decals_count(self, value):
		"""Gets the number of decals applied to this model."""
		self._instance.GetDecalsCount = value

	@property
	def get_dependencies(self):
		"""Gets all of this model's dependencies."""
		return self._instance.GetDependencies

	@get_dependencies.setter
	def get_dependencies(self, value):
		"""Gets all of this model's dependencies."""
		self._instance.GetDependencies = value

	@property
	def get_display_state_setting(self):
		"""Gets the display state setting for the specified scope."""
		return self._instance.GetDisplayStateSetting

	@get_display_state_setting.setter
	def get_display_state_setting(self, value):
		"""Gets the display state setting for the specified scope."""
		self._instance.GetDisplayStateSetting = value

	@property
	def get_drafting_standard_names(self):
		"""Get the names of all currently available drafting standards."""
		return self._instance.GetDraftingStandardNames

	@get_drafting_standard_names.setter
	def get_drafting_standard_names(self, value):
		"""Get the names of all currently available drafting standards."""
		self._instance.GetDraftingStandardNames = value

	@property
	def get_flatten_sheet_metal_persist_reference(self):
		"""Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part."""
		return self._instance.GetFlattenSheetMetalPersistReference

	@get_flatten_sheet_metal_persist_reference.setter
	def get_flatten_sheet_metal_persist_reference(self, value):
		"""Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part."""
		self._instance.GetFlattenSheetMetalPersistReference = value

	@property
	def get_general_table_annotation(self):
		"""Creates a general table annotation for SOLIDWORKS MBD 3D PDF."""
		return self._instance.GetGeneralTableAnnotation

	@get_general_table_annotation.setter
	def get_general_table_annotation(self, value):
		"""Creates a general table annotation for SOLIDWORKS MBD 3D PDF."""
		self._instance.GetGeneralTableAnnotation = value

	@property
	def get_keep_light_in_render_scene(self):
		"""Gets whether a light is kept when the scene changes."""
		return self._instance.GetKeepLightInRenderScene

	@get_keep_light_in_render_scene.setter
	def get_keep_light_in_render_scene(self, value):
		"""Gets whether a light is kept when the scene changes."""
		self._instance.GetKeepLightInRenderScene = value

	@property
	def get_last_feature_added(self):
		"""Gets the last feature added to the model."""
		return self._instance.GetLastFeatureAdded

	@get_last_feature_added.setter
	def get_last_feature_added(self, value):
		"""Gets the last feature added to the model."""
		self._instance.GetLastFeatureAdded = value

	@property
	def get_license_type(self):
		"""Gets the type of SOLIDWORKS license used when the model was created."""
		return self._instance.GetLicenseType

	@get_license_type.setter
	def get_license_type(self, value):
		"""Gets the type of SOLIDWORKS license used when the model was created."""
		self._instance.GetLicenseType = value

	@property
	def get_light_enabled_in_render(self):
		"""Gets whether a light is on in this model."""
		return self._instance.GetLightEnabledInRender

	@get_light_enabled_in_render.setter
	def get_light_enabled_in_render(self, value):
		"""Gets whether a light is on in this model."""
		self._instance.GetLightEnabledInRender = value

	@property
	def get_material(self):
		"""Gets the appearance for the specified appearance ID in the specified configuration in this model document"""
		return self._instance.GetMaterial

	@get_material.setter
	def get_material(self, value):
		"""Gets the appearance for the specified appearance ID in the specified configuration in this model document"""
		self._instance.GetMaterial = value

	@property
	def get_material_property_values(self):
		"""Gets the material properties for this model document."""
		return self._instance.GetMaterialPropertyValues

	@get_material_property_values.setter
	def get_material_property_values(self, value):
		"""Gets the material properties for this model document."""
		self._instance.GetMaterialPropertyValues = value

	@property
	def get_m_b_d_d_pdf_data(self):
		"""Gets the SOLIDWORKS MBD 3D PDF data object."""
		return self._instance.GetMBD3DPdfData

	@get_m_b_d_d_pdf_data.setter
	def get_m_b_d_d_pdf_data(self, value):
		"""Gets the SOLIDWORKS MBD 3D PDF data object."""
		self._instance.GetMBD3DPdfData = value

	@property
	def get_model_break_view_names(self):
		"""Gets the names and number of the Model Break Views in the current configuration of the active model."""
		return self._instance.GetModelBreakViewNames

	@get_model_break_view_names.setter
	def get_model_break_view_names(self, value):
		"""Gets the names and number of the Model Break Views in the current configuration of the active model."""
		self._instance.GetModelBreakViewNames = value

	@property
	def get_model_view_count(self):
		"""Gets the number of model views in this document."""
		return self._instance.GetModelViewCount

	@get_model_view_count.setter
	def get_model_view_count(self, value):
		"""Gets the number of model views in this document."""
		self._instance.GetModelViewCount = value

	@property
	def get_model_views(self):
		"""Gets the model views in this document."""
		return self._instance.GetModelViews

	@get_model_views.setter
	def get_model_views(self, value):
		"""Gets the model views in this document."""
		self._instance.GetModelViews = value

	@property
	def get_motion_study_manager(self):
		"""Gets the SOLIDWORKS motion study's MotionManager."""
		return self._instance.GetMotionStudyManager

	@get_motion_study_manager.setter
	def get_motion_study_manager(self, value):
		"""Gets the SOLIDWORKS motion study's MotionManager."""
		self._instance.GetMotionStudyManager = value

	@property
	def get_named_view_rotation(self):
		"""Gets the specified named view orientation matrix with respect to the Front view."""
		return self._instance.GetNamedViewRotation

	@get_named_view_rotation.setter
	def get_named_view_rotation(self, value):
		"""Gets the specified named view orientation matrix with respect to the Front view."""
		self._instance.GetNamedViewRotation = value

	@property
	def get_object_by_persist_reference(self):
		"""Gets the object assigned to the specified persistent reference ID."""
		return self._instance.GetObjectByPersistReference3

	@get_object_by_persist_reference.setter
	def get_object_by_persist_reference(self, value):
		"""Gets the object assigned to the specified persistent reference ID."""
		self._instance.GetObjectByPersistReference3 = value

	@property
	def get_object_id(self):
		"""Gets the object ID for the specified annotation."""
		return self._instance.GetObjectId

	@get_object_id.setter
	def get_object_id(self, value):
		"""Gets the object ID for the specified annotation."""
		self._instance.GetObjectId = value

	@property
	def get_o_l_e_object_count(self):
		"""Gets the number of OLE objects."""
		return self._instance.GetOLEObjectCount

	@get_o_l_e_object_count.setter
	def get_o_l_e_object_count(self, value):
		"""Gets the number of OLE objects."""
		self._instance.GetOLEObjectCount = value

	@property
	def get_o_l_e_objects(self):
		"""Get the OLE objects."""
		return self._instance.GetOLEObjects

	@get_o_l_e_objects.setter
	def get_o_l_e_objects(self, value):
		"""Get the OLE objects."""
		self._instance.GetOLEObjects = value

	@property
	def get_pack_and_go(self):
		"""Gets a Pack and Go object."""
		return self._instance.GetPackAndGo

	@get_pack_and_go.setter
	def get_pack_and_go(self, value):
		"""Gets a Pack and Go object."""
		self._instance.GetPackAndGo = value

	@property
	def get_persist_reference(self):
		"""Gets the persistent reference ID for the specified object in this model document."""
		return self._instance.GetPersistReference3

	@get_persist_reference.setter
	def get_persist_reference(self, value):
		"""Gets the persistent reference ID for the specified object in this model document."""
		self._instance.GetPersistReference3 = value

	@property
	def get_persist_reference_count(self):
		"""Gets the size of the persistent reference ID assigned to the selected object in this model document."""
		return self._instance.GetPersistReferenceCount3

	@get_persist_reference_count.setter
	def get_persist_reference_count(self, value):
		"""Gets the size of the persistent reference ID assigned to the selected object in this model document."""
		self._instance.GetPersistReferenceCount3 = value

	@property
	def get_p_l_m_i_d(self):
		"""Gets the ID of this SOLIDWORKS Connected document."""
		return self._instance.GetPLMID

	@get_p_l_m_i_d.setter
	def get_p_l_m_i_d(self, value):
		"""Gets the ID of this SOLIDWORKS Connected document."""
		self._instance.GetPLMID = value

	@property
	def get_print_d_dialog(self):
		"""Gets the IPrint3DDialog object."""
		return self._instance.GetPrint3DDialog

	@get_print_d_dialog.setter
	def get_print_d_dialog(self, value):
		"""Gets the IPrint3DDialog object."""
		self._instance.GetPrint3DDialog = value

	@property
	def get_print_specification(self):
		"""Gets the IPrintSpecification object for this document."""
		return self._instance.GetPrintSpecification

	@get_print_specification.setter
	def get_print_specification(self, value):
		"""Gets the IPrintSpecification object for this document."""
		self._instance.GetPrintSpecification = value

	@property
	def get_render_custom_references(self):
		"""Get the custom render references for this model."""
		return self._instance.GetRenderCustomReferences

	@get_render_custom_references.setter
	def get_render_custom_references(self, value):
		"""Get the custom render references for this model."""
		self._instance.GetRenderCustomReferences = value

	@property
	def get_render_materials(self):
		"""Gets the appearances applied to this model document in the specified display states."""
		return self._instance.GetRenderMaterials2

	@get_render_materials.setter
	def get_render_materials(self, value):
		"""Gets the appearances applied to this model document in the specified display states."""
		self._instance.GetRenderMaterials2 = value

	@property
	def get_render_materials_count(self):
		"""Gets the number of appearances applied to this model document in the specified display states."""
		return self._instance.GetRenderMaterialsCount2

	@get_render_materials_count.setter
	def get_render_materials_count(self, value):
		"""Gets the number of appearances applied to this model document in the specified display states."""
		self._instance.GetRenderMaterialsCount2 = value

	@property
	def get_render_stock_references(self):
		"""Gets the SOLIDWORKS-supplied (stock) render references for this model."""
		return self._instance.GetRenderStockReferences

	@get_render_stock_references.setter
	def get_render_stock_references(self, value):
		"""Gets the SOLIDWORKS-supplied (stock) render references for this model."""
		self._instance.GetRenderStockReferences = value

	@property
	def get_routing_component_manager(self):
		"""Gets the routing component manager."""
		return self._instance.GetRoutingComponentManager

	@get_routing_component_manager.setter
	def get_routing_component_manager(self, value):
		"""Gets the routing component manager."""
		self._instance.GetRoutingComponentManager = value

	@property
	def get_scanto_d(self):
		"""Gets the IScanTo3D object for this document."""
		return self._instance.GetScanto3D

	@get_scanto_d.setter
	def get_scanto_d(self, value):
		"""Gets the IScanTo3D object for this document."""
		self._instance.GetScanto3D = value

	@property
	def get_scene_bkg_d_i_bx(self):
		"""Gets the background image as DIBSECTION in 64-bit applications."""
		return self._instance.GetSceneBkgDIBx64

	@get_scene_bkg_d_i_bx.setter
	def get_scene_bkg_d_i_bx(self, value):
		"""Gets the background image as DIBSECTION in 64-bit applications."""
		self._instance.GetSceneBkgDIBx64 = value

	@property
	def get_search_data(self):
		"""Gets the SOLIDWORKS Search, third-party, application keywords from the model document."""
		return self._instance.GetSearchData

	@get_search_data.setter
	def get_search_data(self, value):
		"""Gets the SOLIDWORKS Search, third-party, application keywords from the model document."""
		self._instance.GetSearchData = value

	@property
	def get_search_data_count(self):
		"""Gets the number of SOLIDWORKS Search keywords for the specified third-party application previously added to this model document."""
		return self._instance.GetSearchDataCount

	@get_search_data_count.setter
	def get_search_data_count(self, value):
		"""Gets the number of SOLIDWORKS Search keywords for the specified third-party application previously added to this model document."""
		self._instance.GetSearchDataCount = value

	@property
	def get_section_properties(self):
		"""Gets the section properties for the following types of selected items: 


Planar model face in any document

Face on a section plane

Crosshatch section face in a section view in a drawing a sketch

Sketch"""
		return self._instance.GetSectionProperties2

	@get_section_properties.setter
	def get_section_properties(self, value):
		"""Gets the section properties for the following types of selected items: 


Planar model face in any document

Face on a section plane

Crosshatch section face in a section view in a drawing a sketch

Sketch"""
		self._instance.GetSectionProperties2 = value

	@property
	def get_sheet_metal_objects_by_persist_reference(self):
		"""Gets the objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part."""
		return self._instance.GetSheetMetalObjectsByPersistReference

	@get_sheet_metal_objects_by_persist_reference.setter
	def get_sheet_metal_objects_by_persist_reference(self, value):
		"""Gets the objects in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part."""
		self._instance.GetSheetMetalObjectsByPersistReference = value

	@property
	def get_stream(self):
		"""Gets the handle for the specified stream."""
		return self._instance.GetStream

	@get_stream.setter
	def get_stream(self, value):
		"""Gets the handle for the specified stream."""
		self._instance.GetStream = value

	@property
	def get_sun_light_advanced_property_values(self):
		"""Gets the specified sunlight advanced properties."""
		return self._instance.GetSunLightAdvancedPropertyValues

	@get_sun_light_advanced_property_values.setter
	def get_sun_light_advanced_property_values(self, value):
		"""Gets the specified sunlight advanced properties."""
		self._instance.GetSunLightAdvancedPropertyValues = value

	@property
	def get_sun_light_source_property_values(self):
		"""Gets the property values for a sunlight source."""
		return self._instance.GetSunLightSourcePropertyValues

	@get_sun_light_source_property_values.setter
	def get_sun_light_source_property_values(self, value):
		"""Gets the property values for a sunlight source."""
		self._instance.GetSunLightSourcePropertyValues = value

	@property
	def get_sustainability(self):
		"""Gets the entry-point interface to the SOLIDWORKS Sustainability API."""
		return self._instance.GetSustainability

	@get_sustainability.setter
	def get_sustainability(self, value):
		"""Gets the entry-point interface to the SOLIDWORKS Sustainability API."""
		self._instance.GetSustainability = value

	@property
	def get_template_sheet_metal(self):
		"""Gets the sheet metal folder feature from this sheet metal model created in SOLIDWORKS 2013 or later."""
		return self._instance.GetTemplateSheetMetal

	@get_template_sheet_metal.setter
	def get_template_sheet_metal(self, value):
		"""Gets the sheet metal folder feature from this sheet metal model created in SOLIDWORKS 2013 or later."""
		self._instance.GetTemplateSheetMetal = value

	@property
	def get_texture(self):
		"""Gets the texture applied to the specified configuration."""
		return self._instance.GetTexture

	@get_texture.setter
	def get_texture(self, value):
		"""Gets the texture applied to the specified configuration."""
		self._instance.GetTexture = value

	@property
	def get_user_preference_double(self):
		"""Gets document default user preference values. This method is intended for user preferences of type double."""
		return self._instance.GetUserPreferenceDouble

	@get_user_preference_double.setter
	def get_user_preference_double(self, value):
		"""Gets document default user preference values. This method is intended for user preferences of type double."""
		self._instance.GetUserPreferenceDouble = value

	@property
	def get_user_preference_double_value_range(self):
		"""Gets the current document default user preference value, and the minimum and maximum valid document user preference values."""
		return self._instance.GetUserPreferenceDoubleValueRange

	@get_user_preference_double_value_range.setter
	def get_user_preference_double_value_range(self, value):
		"""Gets the current document default user preference value, and the minimum and maximum valid document user preference values."""
		self._instance.GetUserPreferenceDoubleValueRange = value

	@property
	def get_user_preference_integer(self):
		"""Sets document default user preference values. This method is intended for user preferences of type integer."""
		return self._instance.GetUserPreferenceInteger

	@get_user_preference_integer.setter
	def get_user_preference_integer(self, value):
		"""Sets document default user preference values. This method is intended for user preferences of type integer."""
		self._instance.GetUserPreferenceInteger = value

	@property
	def get_user_preference_string(self):
		"""Gets document default user preference values. This method is intended for user preferences of type string."""
		return self._instance.GetUserPreferenceString

	@get_user_preference_string.setter
	def get_user_preference_string(self, value):
		"""Gets document default user preference values. This method is intended for user preferences of type string."""
		self._instance.GetUserPreferenceString = value

	@property
	def get_user_preference_text_format(self):
		"""Gets document default user preference values. This method is intended for getting detailing text formats."""
		return self._instance.GetUserPreferenceTextFormat

	@get_user_preference_text_format.setter
	def get_user_preference_text_format(self, value):
		"""Gets document default user preference values. This method is intended for getting detailing text formats."""
		self._instance.GetUserPreferenceTextFormat = value

	@property
	def get_user_preference_toggle(self):
		"""Gets document default user preference values. This method is intended for user preferences that can be toggled."""
		return self._instance.GetUserPreferenceToggle

	@get_user_preference_toggle.setter
	def get_user_preference_toggle(self, value):
		"""Gets document default user preference values. This method is intended for user preferences that can be toggled."""
		self._instance.GetUserPreferenceToggle = value

	@property
	def get_visible_box(self):
		"""Gets the visible bounding box set by IModelDocExtension::SetVisibleBox for a part or an assembly."""
		return self._instance.GetVisibleBox

	@get_visible_box.setter
	def get_visible_box(self, value):
		"""Gets the visible bounding box set by IModelDocExtension::SetVisibleBox for a part or an assembly."""
		self._instance.GetVisibleBox = value

	@property
	def get_whats_wrong(self):
		"""Gets the What's Wrong dialog information for this model document."""
		return self._instance.GetWhatsWrong

	@get_whats_wrong.setter
	def get_whats_wrong(self, value):
		"""Gets the What's Wrong dialog information for this model document."""
		self._instance.GetWhatsWrong = value

	@property
	def get_whats_wrong_count(self):
		"""Gets the number of items in the What's Wrong dialog."""
		return self._instance.GetWhatsWrongCount

	@get_whats_wrong_count.setter
	def get_whats_wrong_count(self, value):
		"""Gets the number of items in the What's Wrong dialog."""
		self._instance.GetWhatsWrongCount = value

	@property
	def has_design_table(self):
		"""Gets whether a document has a design table."""
		return self._instance.HasDesignTable

	@has_design_table.setter
	def has_design_table(self, value):
		"""Gets whether a document has a design table."""
		self._instance.HasDesignTable = value

	@property
	def has_material_property_values(self):
		"""Gets whether this model has an appearance."""
		return self._instance.HasMaterialPropertyValues

	@has_material_property_values.setter
	def has_material_property_values(self, value):
		"""Gets whether this model has an appearance."""
		self._instance.HasMaterialPropertyValues = value

	@property
	def has_renamed_documents(self):
		"""Gets whether the document has renamed files."""
		return self._instance.HasRenamedDocuments

	@has_renamed_documents.setter
	def has_renamed_documents(self, value):
		"""Gets whether the document has renamed files."""
		self._instance.HasRenamedDocuments = value

	@property
	def hide_decal(self):
		"""Hides or shows the specified decal applied to this model."""
		return self._instance.HideDecal

	@hide_decal.setter
	def hide_decal(self, value):
		"""Hides or shows the specified decal applied to this model."""
		self._instance.HideDecal = value

	@property
	def hide_feature_manager(self):
		"""Hides or shows the Manager Pane."""
		return self._instance.HideFeatureManager

	@hide_feature_manager.setter
	def hide_feature_manager(self, value):
		"""Hides or shows the Manager Pane."""
		self._instance.HideFeatureManager = value

	@property
	def i_add_display_state_specific_render_material(self):
		"""Adds the specified material to the specified display states in the active configuration and returns the IDs assigned to that material."""
		return self._instance.IAddDisplayStateSpecificRenderMaterial

	@i_add_display_state_specific_render_material.setter
	def i_add_display_state_specific_render_material(self, value):
		"""Adds the specified material to the specified display states in the active configuration and returns the IDs assigned to that material."""
		self._instance.IAddDisplayStateSpecificRenderMaterial = value

	@property
	def i_change_sketch_plane(self):
		"""Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations."""
		return self._instance.IChangeSketchPlane

	@i_change_sketch_plane.setter
	def i_change_sketch_plane(self, value):
		"""Changes the plane used by a sketch by moving the selected sketch to the selected plane in the specified configurations."""
		self._instance.IChangeSketchPlane = value

	@property
	def i_create_o_l_e_object(self):
		"""Creates an OLE object on the active document."""
		return self._instance.ICreateOLEObject

	@i_create_o_l_e_object.setter
	def i_create_o_l_e_object(self, value):
		"""Creates an OLE object on the active document."""
		self._instance.ICreateOLEObject = value

	@property
	def i_delete_display_state_specific_render_material(self):
		"""Deletes the specified materials, using the IDs of the materials, from the active configuration."""
		return self._instance.IDeleteDisplayStateSpecificRenderMaterial

	@i_delete_display_state_specific_render_material.setter
	def i_delete_display_state_specific_render_material(self, value):
		"""Deletes the specified materials, using the IDs of the materials, from the active configuration."""
		self._instance.IDeleteDisplayStateSpecificRenderMaterial = value

	@property
	def i_edit_dimension_properties(self):
		"""Edits the selected dimension."""
		return self._instance.IEditDimensionProperties

	@i_edit_dimension_properties.setter
	def i_edit_dimension_properties(self, value):
		"""Edits the selected dimension."""
		self._instance.IEditDimensionProperties = value

	@property
	def i_getrd_party_storage_store(self):
		"""Gets the IStorage interface to the specified third-party storage in this SOLIDWORKS document."""
		return self._instance.IGet3rdPartyStorageStore

	@i_getrd_party_storage_store.setter
	def i_getrd_party_storage_store(self, value):
		"""Gets the IStorage interface to the specified third-party storage in this SOLIDWORKS document."""
		self._instance.IGet3rdPartyStorageStore = value

	@property
	def i_get_annotations(self):
		"""Gets the annotations on this model."""
		return self._instance.IGetAnnotations

	@i_get_annotations.setter
	def i_get_annotations(self, value):
		"""Gets the annotations on this model."""
		self._instance.IGetAnnotations = value

	@property
	def i_get_annotation_views(self):
		"""Gets the annotation views in this part or assembly document."""
		return self._instance.IGetAnnotationViews

	@i_get_annotation_views.setter
	def i_get_annotation_views(self, value):
		"""Gets the annotation views in this part or assembly document."""
		self._instance.IGetAnnotationViews = value

	@property
	def i_get_attachments(self):
		"""Gets the attachments for this document."""
		return self._instance.IGetAttachments

	@i_get_attachments.setter
	def i_get_attachments(self, value):
		"""Gets the attachments for this document."""
		self._instance.IGetAttachments = value

	@property
	def i_get_decals(self):
		"""Gets the decals applied to the model."""
		return self._instance.IGetDecals

	@i_get_decals.setter
	def i_get_decals(self, value):
		"""Gets the decals applied to the model."""
		self._instance.IGetDecals = value

	@property
	def i_get_flatten_sheet_metal_persist_reference(self):
		"""Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part."""
		return self._instance.IGetFlattenSheetMetalPersistReference

	@i_get_flatten_sheet_metal_persist_reference.setter
	def i_get_flatten_sheet_metal_persist_reference(self, value):
		"""Gets a byte array of persistent reference IDs for the specified entity (a face, edge, or vertex) in a flattened sheet metal part."""
		self._instance.IGetFlattenSheetMetalPersistReference = value

	@property
	def i_get_material_property_values(self):
		"""Gets the material properties for this model."""
		return self._instance.IGetMaterialPropertyValues

	@i_get_material_property_values.setter
	def i_get_material_property_values(self, value):
		"""Gets the material properties for this model."""
		self._instance.IGetMaterialPropertyValues = value

	@property
	def i_get_model_views(self):
		"""Gets the model views in this document."""
		return self._instance.IGetModelViews

	@i_get_model_views.setter
	def i_get_model_views(self, value):
		"""Gets the model views in this document."""
		self._instance.IGetModelViews = value

	@property
	def i_get_named_view_rotation(self):
		"""Gets the specified named view orientation matrix with respect to the Front view."""
		return self._instance.IGetNamedViewRotation

	@i_get_named_view_rotation.setter
	def i_get_named_view_rotation(self, value):
		"""Gets the specified named view orientation matrix with respect to the Front view."""
		self._instance.IGetNamedViewRotation = value

	@property
	def i_get_object_by_persist_reference(self):
		"""Gets the object assigned to the specified persistent reference ID."""
		return self._instance.IGetObjectByPersistReference3

	@i_get_object_by_persist_reference.setter
	def i_get_object_by_persist_reference(self, value):
		"""Gets the object assigned to the specified persistent reference ID."""
		self._instance.IGetObjectByPersistReference3 = value

	@property
	def i_get_o_l_e_objects(self):
		"""Get the OLE objects."""
		return self._instance.IGetOLEObjects

	@i_get_o_l_e_objects.setter
	def i_get_o_l_e_objects(self, value):
		"""Get the OLE objects."""
		self._instance.IGetOLEObjects = value

	@property
	def i_get_persist_reference(self):
		"""Gets the persistent reference ID for the specified object in this model document."""
		return self._instance.IGetPersistReference3

	@i_get_persist_reference.setter
	def i_get_persist_reference(self, value):
		"""Gets the persistent reference ID for the specified object in this model document."""
		self._instance.IGetPersistReference3 = value

	@property
	def i_get_search_data(self):
		"""Gets the SOLIDWORKS Search, third-party, application keywords from the model document."""
		return self._instance.IGetSearchData

	@i_get_search_data.setter
	def i_get_search_data(self, value):
		"""Gets the SOLIDWORKS Search, third-party, application keywords from the model document."""
		self._instance.IGetSearchData = value

	@property
	def i_get_section_properties(self):
		"""Gets the section properties for the following types of selected items: 


Planar model face in any document

Face on a section plane

Crosshatch section face in a section view in a drawing a sketch

Sketch"""
		return self._instance.IGetSectionProperties2

	@i_get_section_properties.setter
	def i_get_section_properties(self, value):
		"""Gets the section properties for the following types of selected items: 


Planar model face in any document

Face on a section plane

Crosshatch section face in a section view in a drawing a sketch

Sketch"""
		self._instance.IGetSectionProperties2 = value

	@property
	def i_get_sheet_metal_objects_by_persist_reference(self):
		"""Gets the object, or objects, in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part."""
		return self._instance.IGetSheetMetalObjectsByPersistReference

	@i_get_sheet_metal_objects_by_persist_reference.setter
	def i_get_sheet_metal_objects_by_persist_reference(self, value):
		"""Gets the object, or objects, in a folded sheet metal part that correspond to the byte array of persistent reference IDs of an entity in a flattened sheet metal part."""
		self._instance.IGetSheetMetalObjectsByPersistReference = value

	@property
	def i_list_external_file_references(self):
		"""Gets the names and statuses of the external file references on this part or assembly."""
		return self._instance.IListExternalFileReferences

	@i_list_external_file_references.setter
	def i_list_external_file_references(self, value):
		"""Gets the names and statuses of the external file references on this part or assembly."""
		self._instance.IListExternalFileReferences = value

	@property
	def insert_annotation_favorite(self):
		"""Inserts annotations from the specified favorite file at the specified location."""
		return self._instance.InsertAnnotationFavorite

	@insert_annotation_favorite.setter
	def insert_annotation_favorite(self, value):
		"""Inserts annotations from the specified favorite file at the specified location."""
		self._instance.InsertAnnotationFavorite = value

	@property
	def insert_annotation_view(self):
		"""Inserts an annotation view in this part or assembly document."""
		return self._instance.InsertAnnotationView

	@insert_annotation_view.setter
	def insert_annotation_view(self, value):
		"""Inserts an annotation view in this part or assembly document."""
		self._instance.InsertAnnotationView = value

	@property
	def insert_attachment(self):
		"""Inserts a file as an Attachment to this document."""
		return self._instance.InsertAttachment

	@insert_attachment.setter
	def insert_attachment(self, value):
		"""Inserts a file as an Attachment to this document."""
		self._instance.InsertAttachment = value

	@property
	def insert_b_o_m_balloon(self):
		"""Inserts a BOM balloon for the selected item."""
		return self._instance.InsertBOMBalloon2

	@insert_b_o_m_balloon.setter
	def insert_b_o_m_balloon(self, value):
		"""Inserts a BOM balloon for the selected item."""
		self._instance.InsertBOMBalloon2 = value

	@property
	def insert_bom_table(self):
		"""Inserts a bill of materials (BOM) table in a part or assembly document."""
		return self._instance.InsertBomTable3

	@insert_bom_table.setter
	def insert_bom_table(self, value):
		"""Inserts a bill of materials (BOM) table in a part or assembly document."""
		self._instance.InsertBomTable3 = value

	@property
	def insert_camera(self):
		"""Inserts a camera in this document."""
		return self._instance.InsertCamera

	@insert_camera.setter
	def insert_camera(self, value):
		"""Inserts a camera in this document."""
		self._instance.InsertCamera = value

	@property
	def insert_chain_dimensions(self):
		"""Chains dimensions for the specified entities in this drawing or sketch."""
		return self._instance.InsertChainDimensions

	@insert_chain_dimensions.setter
	def insert_chain_dimensions(self, value):
		"""Chains dimensions for the specified entities in this drawing or sketch."""
		self._instance.InsertChainDimensions = value

	@property
	def insert_datum_target_symbol(self):
		"""Creates a datum target symbol."""
		return self._instance.InsertDatumTargetSymbol3

	@insert_datum_target_symbol.setter
	def insert_datum_target_symbol(self, value):
		"""Creates a datum target symbol."""
		self._instance.InsertDatumTargetSymbol3 = value

	@property
	def insert_delete_face(self):
		"""Inserts a DeleteFace feature."""
		return self._instance.InsertDeleteFace

	@insert_delete_face.setter
	def insert_delete_face(self, value):
		"""Inserts a DeleteFace feature."""
		self._instance.InsertDeleteFace = value

	@property
	def insert_general_table_annotation(self):
		"""Inserts the a general table annotation in this model document."""
		return self._instance.InsertGeneralTableAnnotation

	@insert_general_table_annotation.setter
	def insert_general_table_annotation(self, value):
		"""Inserts the a general table annotation in this model document."""
		self._instance.InsertGeneralTableAnnotation = value

	@property
	def insert_general_tolerance_table_annotation(self):
		"""Inserts a general tolerance table annotation in this model document."""
		return self._instance.InsertGeneralToleranceTableAnnotation

	@insert_general_tolerance_table_annotation.setter
	def insert_general_tolerance_table_annotation(self, value):
		"""Inserts a general tolerance table annotation in this model document."""
		self._instance.InsertGeneralToleranceTableAnnotation = value

	@property
	def insert_object_from_file(self):
		"""Inserts an OLE object from a file."""
		return self._instance.InsertObjectFromFile

	@insert_object_from_file.setter
	def insert_object_from_file(self, value):
		"""Inserts an OLE object from a file."""
		self._instance.InsertObjectFromFile = value

	@property
	def insert_scene(self):
		"""Applies the specified scene to the model."""
		return self._instance.InsertScene

	@insert_scene.setter
	def insert_scene(self, value):
		"""Applies the specified scene to the model."""
		self._instance.InsertScene = value

	@property
	def insert_stacked_balloon(self):
		"""Inserts a stack of balloons for selected items."""
		return self._instance.InsertStackedBalloon2

	@insert_stacked_balloon.setter
	def insert_stacked_balloon(self, value):
		"""Inserts a stack of balloons for selected items."""
		self._instance.InsertStackedBalloon2 = value

	@property
	def insert_surface_finish_symbol(self):
		"""Creates a surface-finish symbol based on the last selection."""
		return self._instance.InsertSurfaceFinishSymbol3

	@insert_surface_finish_symbol.setter
	def insert_surface_finish_symbol(self, value):
		"""Creates a surface-finish symbol based on the last selection."""
		self._instance.InsertSurfaceFinishSymbol3 = value

	@property
	def insert_title_block_table(self):
		"""Inserts a title block table in a part or assembly document."""
		return self._instance.InsertTitleBlockTable

	@insert_title_block_table.setter
	def insert_title_block_table(self, value):
		"""Inserts a title block table in a part or assembly document."""
		self._instance.InsertTitleBlockTable = value

	@property
	def install_model_colorizer(self):
		"""Installs your implemented interface of the ISwColorContour interface."""
		return self._instance.InstallModelColorizer

	@install_model_colorizer.setter
	def install_model_colorizer(self, value):
		"""Installs your implemented interface of the ISwColorContour interface."""
		self._instance.InstallModelColorizer = value

	@property
	def i_releaserd_party_storage_store(self):
		"""Releases the specified third-party storage in this document."""
		return self._instance.IRelease3rdPartyStorageStore

	@i_releaserd_party_storage_store.setter
	def i_releaserd_party_storage_store(self, value):
		"""Releases the specified third-party storage in this document."""
		self._instance.IRelease3rdPartyStorageStore = value

	@property
	def i_remove_material_property(self):
		"""Removes material property values from this model."""
		return self._instance.IRemoveMaterialProperty

	@i_remove_material_property.setter
	def i_remove_material_property(self, value):
		"""Removes material property values from this model."""
		self._instance.IRemoveMaterialProperty = value

	@property
	def is_abbreviated_view_active(self):
		"""Gets or sets whether the abbreviated view is active."""
		return self._instance.IsAbbreviatedViewActive

	@is_abbreviated_view_active.setter
	def is_abbreviated_view_active(self, value):
		"""Gets or sets whether the abbreviated view is active."""
		self._instance.IsAbbreviatedViewActive = value

	@property
	def is_converted(self):
		"""Gets whether the active document was converted to the current release uponing opening but has not yet been saved."""
		return self._instance.IsConverted

	@is_converted.setter
	def is_converted(self, value):
		"""Gets whether the active document was converted to the current release uponing opening but has not yet been saved."""
		self._instance.IsConverted = value

	@property
	def i_set_material_property_values(self):
		"""Sets the material property values for this model document."""
		return self._instance.ISetMaterialPropertyValues

	@i_set_material_property_values.setter
	def i_set_material_property_values(self, value):
		"""Sets the material property values for this model document."""
		self._instance.ISetMaterialPropertyValues = value

	@property
	def is_exploded(self):
		"""Gets the name of the exploded view currently shown in the model."""
		return self._instance.IsExploded

	@is_exploded.setter
	def is_exploded(self, value):
		"""Gets the name of the exploded view currently shown in the model."""
		self._instance.IsExploded = value

	@property
	def is_future_version(self):
		"""Gets whether this document is for a future version of SOLIDWORKS."""
		return self._instance.IsFutureVersion

	@is_future_version.setter
	def is_future_version(self, value):
		"""Gets whether this document is for a future version of SOLIDWORKS."""
		self._instance.IsFutureVersion = value

	@property
	def is_same_persistent_i_d(self):
		"""Gets whether the two specified objects have the same persistent reference IDs."""
		return self._instance.IsSamePersistentID

	@is_same_persistent_i_d.setter
	def is_same_persistent_i_d(self, value):
		"""Gets whether the two specified objects have the same persistent reference IDs."""
		self._instance.IsSamePersistentID = value

	@property
	def is_virtual_component(self):
		"""Gets the paths to parent assembly components, up to and including the first non-virtual parent, if the model is a virtual component."""
		return self._instance.IsVirtualComponent3

	@is_virtual_component.setter
	def is_virtual_component(self, value):
		"""Gets the paths to parent assembly components, up to and including the first non-virtual parent, if the model is a virtual component."""
		self._instance.IsVirtualComponent3 = value

	@property
	def jog_dimension(self):
		"""Gets or sets whether jog points are on or off on an interactively selected linear or ordinate dimension."""
		return self._instance.JogDimension

	@jog_dimension.setter
	def jog_dimension(self, value):
		"""Gets or sets whether jog points are on or off on an interactively selected linear or ordinate dimension."""
		self._instance.JogDimension = value

	@property
	def list_external_file_references(self):
		"""Gets the specified external file reference information for this part or assembly."""
		return self._instance.ListExternalFileReferences2

	@list_external_file_references.setter
	def list_external_file_references(self, value):
		"""Gets the specified external file reference information for this part or assembly."""
		self._instance.ListExternalFileReferences2 = value

	@property
	def list_external_file_references_count(self):
		"""Gets the number of external references on this part or assembly."""
		return self._instance.ListExternalFileReferencesCount

	@list_external_file_references_count.setter
	def list_external_file_references_count(self, value):
		"""Gets the number of external references on this part or assembly."""
		self._instance.ListExternalFileReferencesCount = value

	@property
	def load_drafting_standard(self):
		"""Loads a custom drafting standard from a file."""
		return self._instance.LoadDraftingStandard

	@load_drafting_standard.setter
	def load_drafting_standard(self, value):
		"""Loads a custom drafting standard from a file."""
		self._instance.LoadDraftingStandard = value

	@property
	def move_decal(self):
		"""Moves the decal up or down in the list of decals applied to the model."""
		return self._instance.MoveDecal

	@move_decal.setter
	def move_decal(self, value):
		"""Moves the decal up or down in the list of decals applied to the model."""
		self._instance.MoveDecal = value

	@property
	def move_or_copy(self):
		"""Moves and optionally copies the selected sketch entities or annotations."""
		return self._instance.MoveOrCopy

	@move_or_copy.setter
	def move_or_copy(self, value):
		"""Moves and optionally copies the selected sketch entities or annotations."""
		self._instance.MoveOrCopy = value

	@property
	def multi_select(self):
		"""Selects multiple objects and returns the number of objects selected in the model."""
		return self._instance.MultiSelect2

	@multi_select.setter
	def multi_select(self, value):
		"""Selects multiple objects and returns the number of objects selected in the model."""
		self._instance.MultiSelect2 = value

	@property
	def print_out(self):
		"""Prints this document without displaying any dialogs or message boxes."""
		return self._instance.PrintOut4

	@print_out.setter
	def print_out(self, value):
		"""Prints this document without displaying any dialogs or message boxes."""
		self._instance.PrintOut4 = value

	@property
	def publish_s_t_e_p_file(self):
		"""Exports the SOLIDWORKS MBD 3D part or assembly to a STEP 242 file."""
		return self._instance.PublishSTEP242File

	@publish_s_t_e_p_file.setter
	def publish_s_t_e_p_file(self, value):
		"""Exports the SOLIDWORKS MBD 3D part or assembly to a STEP 242 file."""
		self._instance.PublishSTEP242File = value

	@property
	def publish_to_d_p_d_f(self):
		"""Creates a 3D PDF for SOLIDWORKS MBD."""
		return self._instance.PublishTo3DPDF

	@publish_to_d_p_d_f.setter
	def publish_to_d_p_d_f(self, value):
		"""Creates a 3D PDF for SOLIDWORKS MBD."""
		self._instance.PublishTo3DPDF = value

	@property
	def purge_display_state(self):
		"""Purges identical display states so that only unique display states remain."""
		return self._instance.PurgeDisplayState

	@purge_display_state.setter
	def purge_display_state(self, value):
		"""Purges identical display states so that only unique display states remain."""
		self._instance.PurgeDisplayState = value

	@property
	def ray_intersections(self):
		"""Finds the intersections between the specified set of rays and the specified set of bodies."""
		return self._instance.RayIntersections

	@ray_intersections.setter
	def ray_intersections(self, value):
		"""Finds the intersections between the specified set of rays and the specified set of bodies."""
		self._instance.RayIntersections = value

	@property
	def rebuild(self):
		"""Rebuilds the model in assembly and drawing documents and returns the status of the rebuild."""
		return self._instance.Rebuild

	@rebuild.setter
	def rebuild(self, value):
		"""Rebuilds the model in assembly and drawing documents and returns the status of the rebuild."""
		self._instance.Rebuild = value

	@property
	def refresh_d_views(self):
		"""Updates the 3D Views of this part or assembly."""
		return self._instance.Refresh3DViews

	@refresh_d_views.setter
	def refresh_d_views(self, value):
		"""Updates the 3D Views of this part or assembly."""
		self._instance.Refresh3DViews = value

	@property
	def re_jog_running_dimension(self):
		"""Applies jogs where extension lines overlap dimension text in an angular running dimension."""
		return self._instance.ReJogRunningDimension

	@re_jog_running_dimension.setter
	def re_jog_running_dimension(self, value):
		"""Applies jogs where extension lines overlap dimension text in an angular running dimension."""
		self._instance.ReJogRunningDimension = value

	@property
	def release_stream(self):
		"""Releases a previously obtained stream."""
		return self._instance.ReleaseStream

	@release_stream.setter
	def release_stream(self, value):
		"""Releases a previously obtained stream."""
		self._instance.ReleaseStream = value

	@property
	def remove_material_property(self):
		"""Removes material property values from this model."""
		return self._instance.RemoveMaterialProperty

	@remove_material_property.setter
	def remove_material_property(self, value):
		"""Removes material property values from this model."""
		self._instance.RemoveMaterialProperty = value

	@property
	def remove_model_colorizer(self):
		"""Removes your installed implemented interface of the ISwColorContour interface."""
		return self._instance.RemoveModelColorizer

	@remove_model_colorizer.setter
	def remove_model_colorizer(self, value):
		"""Removes your installed implemented interface of the ISwColorContour interface."""
		self._instance.RemoveModelColorizer = value

	@property
	def remove_texture(self):
		"""Removes the texture from the specified configuration."""
		return self._instance.RemoveTexture2

	@remove_texture.setter
	def remove_texture(self, value):
		"""Removes the texture from the specified configuration."""
		self._instance.RemoveTexture2 = value

	@property
	def remove_texture_by_display_state(self):
		"""Removes the texture applied to this model in the specified display state."""
		return self._instance.RemoveTextureByDisplayState

	@remove_texture_by_display_state.setter
	def remove_texture_by_display_state(self, value):
		"""Removes the texture applied to this model in the specified display state."""
		self._instance.RemoveTextureByDisplayState = value

	@property
	def remove_visible_box(self):
		"""Removes the visible bounding box set by IModelDocExtension::SetVisibleBox and resets the size of the bounding box to the size calculated by SOLIDWORKS for a part or an assembly."""
		return self._instance.RemoveVisibleBox

	@remove_visible_box.setter
	def remove_visible_box(self, value):
		"""Removes the visible bounding box set by IModelDocExtension::SetVisibleBox and resets the size of the bounding box to the size calculated by SOLIDWORKS for a part or an assembly."""
		self._instance.RemoveVisibleBox = value

	@property
	def rename_document(self):
		"""Temporarily renames the selected component using the specified name."""
		return self._instance.RenameDocument

	@rename_document.setter
	def rename_document(self, value):
		"""Temporarily renames the selected component using the specified name."""
		self._instance.RenameDocument = value

	@property
	def rename_drafting_standard(self):
		"""Rename the current custom drafting to the specifed name."""
		return self._instance.RenameDraftingStandard

	@rename_drafting_standard.setter
	def rename_drafting_standard(self, value):
		"""Rename the current custom drafting to the specifed name."""
		self._instance.RenameDraftingStandard = value

	@property
	def reorder_feature(self):
		"""Moves the specified feature to another location in the FeatureManager design tree of this part or assembly."""
		return self._instance.ReorderFeature

	@reorder_feature.setter
	def reorder_feature(self, value):
		"""Moves the specified feature to another location in the FeatureManager design tree of this part or assembly."""
		self._instance.ReorderFeature = value

	@property
	def reset_standard_views(self):
		"""Returns all standard model views to their default settings."""
		return self._instance.ResetStandardViews

	@reset_standard_views.setter
	def reset_standard_views(self, value):
		"""Returns all standard model views to their default settings."""
		self._instance.ResetStandardViews = value

	@property
	def reverse_decals_order(self):
		"""Reverses the order of the decals on the model."""
		return self._instance.ReverseDecalsOrder

	@reverse_decals_order.setter
	def reverse_decals_order(self, value):
		"""Reverses the order of the decals on the model."""
		self._instance.ReverseDecalsOrder = value

	@property
	def rotate_or_copy(self):
		"""Rotates and optionally copies the selected sketch entities or annotations."""
		return self._instance.RotateOrCopy

	@rotate_or_copy.setter
	def rotate_or_copy(self, value):
		"""Rotates and optionally copies the selected sketch entities or annotations."""
		self._instance.RotateOrCopy = value

	@property
	def run_command(self):
		"""Runs the specified SOLIDWORKS command."""
		return self._instance.RunCommand

	@run_command.setter
	def run_command(self, value):
		"""Runs the specified SOLIDWORKS command."""
		self._instance.RunCommand = value

	@property
	def save_as(self):
		"""Saves the active document to the specified name with advanced options."""
		return self._instance.SaveAs3

	@save_as.setter
	def save_as(self, value):
		"""Saves the active document to the specified name with advanced options."""
		self._instance.SaveAs3 = value

	@property
	def save_de_featured_file(self):
		"""Removes all CAD data except the outer surface from a loaded part or assembly document and saves the outer surface as a part."""
		return self._instance.SaveDeFeaturedFile

	@save_de_featured_file.setter
	def save_de_featured_file(self, value):
		"""Removes all CAD data except the outer surface from a loaded part or assembly document and saves the outer surface as a part."""
		self._instance.SaveDeFeaturedFile = value

	@property
	def save_drafting_standard(self):
		"""Saves the current custom drafting standard to a file."""
		return self._instance.SaveDraftingStandard

	@save_drafting_standard.setter
	def save_drafting_standard(self, value):
		"""Saves the current custom drafting standard to a file."""
		self._instance.SaveDraftingStandard = value

	@property
	def save_pack_and_go(self):
		"""Saves the files designated for Pack and Go to either a folder or Zip file."""
		return self._instance.SavePackAndGo

	@save_pack_and_go.setter
	def save_pack_and_go(self, value):
		"""Saves the files designated for Pack and Go to either a folder or Zip file."""
		self._instance.SavePackAndGo = value

	@property
	def save_selection(self):
		"""Creates a new selection set containing the selected entities."""
		return self._instance.SaveSelection

	@save_selection.setter
	def save_selection(self, value):
		"""Creates a new selection set containing the selected entities."""
		self._instance.SaveSelection = value

	@property
	def save_to_d_experience(self):
		"""Saves this document in SOLIDWORKS Connected using the specified save options."""
		return self._instance.SaveTo3DExperience

	@save_to_d_experience.setter
	def save_to_d_experience(self, value):
		"""Saves this document in SOLIDWORKS Connected using the specified save options."""
		self._instance.SaveTo3DExperience = value

	@property
	def scale_or_copy(self):
		"""Scales and optionally copies the selected sketch items or annotations."""
		return self._instance.ScaleOrCopy

	@scale_or_copy.setter
	def scale_or_copy(self, value):
		"""Scales and optionally copies the selected sketch items or annotations."""
		self._instance.ScaleOrCopy = value

	@property
	def select_all(self):
		"""Selects all edges in a part, all components in an assembly, or all entities (by default, sketch entities, dimensions, and annotations) in a drawing."""
		return self._instance.SelectAll

	@select_all.setter
	def select_all(self, value):
		"""Selects all edges in a part, all components in an assembly, or all entities (by default, sketch entities, dimensions, and annotations) in a drawing."""
		self._instance.SelectAll = value

	@property
	def select_by_i_d(self):
		"""Selects the specified entity."""
		return self._instance.SelectByID2

	@select_by_i_d.setter
	def select_by_i_d(self, value):
		"""Selects the specified entity."""
		self._instance.SelectByID2 = value

	@property
	def select_by_ray(self):
		"""Selects the first entity of the specified type that is intersected by a ray that starts at the specified point and runs parallel to the specified direction vector within the specified radius."""
		return self._instance.SelectByRay

	@select_by_ray.setter
	def select_by_ray(self, value):
		"""Selects the first entity of the specified type that is intersected by a ray that starts at the specified point and runs parallel to the specified direction vector within the specified radius."""
		self._instance.SelectByRay = value

	@property
	def set_advanced_spot_light_properties(self):
		"""Sets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model."""
		return self._instance.SetAdvancedSpotLightProperties

	@set_advanced_spot_light_properties.setter
	def set_advanced_spot_light_properties(self, value):
		"""Sets the attenuation-related, advanced properties for the specified SOLIDWORKS spot light in this model."""
		self._instance.SetAdvancedSpotLightProperties = value

	@property
	def set_api_undo_object(self):
		"""Implements an undo object for an add-in application."""
		return self._instance.SetApiUndoObject

	@set_api_undo_object.setter
	def set_api_undo_object(self, value):
		"""Implements an undo object for an add-in application."""
		self._instance.SetApiUndoObject = value

	@property
	def set_keep_light_in_render_scene(self):
		"""Sets whether to keep a light when the scene changes."""
		return self._instance.SetKeepLightInRenderScene

	@set_keep_light_in_render_scene.setter
	def set_keep_light_in_render_scene(self, value):
		"""Sets whether to keep a light when the scene changes."""
		self._instance.SetKeepLightInRenderScene = value

	@property
	def set_light_enabled_in_render(self):
		"""Sets whether a light is on in this model."""
		return self._instance.SetLightEnabledInRender

	@set_light_enabled_in_render.setter
	def set_light_enabled_in_render(self, value):
		"""Sets whether a light is on in this model."""
		self._instance.SetLightEnabledInRender = value

	@property
	def set_material_property_values(self):
		"""Sets the material property values for this model document."""
		return self._instance.SetMaterialPropertyValues

	@set_material_property_values.setter
	def set_material_property_values(self, value):
		"""Sets the material property values for this model document."""
		self._instance.SetMaterialPropertyValues = value

	@property
	def set_scene_bkg_d_i_bx(self):
		"""Sets the background image in 64-bit applications."""
		return self._instance.SetSceneBkgDIBx64

	@set_scene_bkg_d_i_bx.setter
	def set_scene_bkg_d_i_bx(self, value):
		"""Sets the background image in 64-bit applications."""
		self._instance.SetSceneBkgDIBx64 = value

	@property
	def set_sun_light_advanced_property_values(self):
		"""Sets the specified sunlight advanced properties."""
		return self._instance.SetSunLightAdvancedPropertyValues

	@set_sun_light_advanced_property_values.setter
	def set_sun_light_advanced_property_values(self, value):
		"""Sets the specified sunlight advanced properties."""
		self._instance.SetSunLightAdvancedPropertyValues = value

	@property
	def set_sun_light_source_property_values(self):
		"""Sets the property values for a sunlight source."""
		return self._instance.SetSunLightSourcePropertyValues

	@set_sun_light_source_property_values.setter
	def set_sun_light_source_property_values(self, value):
		"""Sets the property values for a sunlight source."""
		self._instance.SetSunLightSourcePropertyValues = value

	@property
	def set_texture(self):
		"""Applies texture to the specified configuration."""
		return self._instance.SetTexture

	@set_texture.setter
	def set_texture(self, value):
		"""Applies texture to the specified configuration."""
		self._instance.SetTexture = value

	@property
	def set_texture_by_display_state(self):
		"""Sets the texture applied to this model in the specified display state."""
		return self._instance.SetTextureByDisplayState

	@set_texture_by_display_state.setter
	def set_texture_by_display_state(self, value):
		"""Sets the texture applied to this model in the specified display state."""
		self._instance.SetTextureByDisplayState = value

	@property
	def set_top_level_transparency(self):
		"""Sets the transparency of this part or top-level assembly."""
		return self._instance.SetTopLevelTransparency

	@set_top_level_transparency.setter
	def set_top_level_transparency(self, value):
		"""Sets the transparency of this part or top-level assembly."""
		self._instance.SetTopLevelTransparency = value

	@property
	def set_user_preference_double(self):
		"""Sets document default user preference values. This method is intended for user preferences of type double."""
		return self._instance.SetUserPreferenceDouble

	@set_user_preference_double.setter
	def set_user_preference_double(self, value):
		"""Sets document default user preference values. This method is intended for user preferences of type double."""
		self._instance.SetUserPreferenceDouble = value

	@property
	def set_user_preference_integer(self):
		"""Sets document default user preference values. This method is intended for user preferences of type integer."""
		return self._instance.SetUserPreferenceInteger

	@set_user_preference_integer.setter
	def set_user_preference_integer(self, value):
		"""Sets document default user preference values. This method is intended for user preferences of type integer."""
		self._instance.SetUserPreferenceInteger = value

	@property
	def set_user_preference_string(self):
		"""Sets document default user preference values. This method is intended for user preferences of type string."""
		return self._instance.SetUserPreferenceString

	@set_user_preference_string.setter
	def set_user_preference_string(self, value):
		"""Sets document default user preference values. This method is intended for user preferences of type string."""
		self._instance.SetUserPreferenceString = value

	@property
	def set_user_preference_text_format(self):
		"""Sets document default user preference values. This method is intended for setting detailing text formats."""
		return self._instance.SetUserPreferenceTextFormat

	@set_user_preference_text_format.setter
	def set_user_preference_text_format(self, value):
		"""Sets document default user preference values. This method is intended for setting detailing text formats."""
		self._instance.SetUserPreferenceTextFormat = value

	@property
	def set_user_preference_toggle(self):
		"""Sets document default user preference values. This method is intended for user preferences that can be toggled."""
		return self._instance.SetUserPreferenceToggle

	@set_user_preference_toggle.setter
	def set_user_preference_toggle(self, value):
		"""Sets document default user preference values. This method is intended for user preferences that can be toggled."""
		self._instance.SetUserPreferenceToggle = value

	@property
	def set_visible_box(self):
		"""Sets the visible bounding box for Zoom to Fit for a part or an assembly."""
		return self._instance.SetVisibleBox

	@set_visible_box.setter
	def set_visible_box(self, value):
		"""Sets the visible bounding box for Zoom to Fit for a part or an assembly."""
		self._instance.SetVisibleBox = value

	@property
	def show_model_break_view(self):
		"""Gets whether to show or hide the specified Model Break View in the current configuration of the active model."""
		return self._instance.ShowModelBreakView

	@show_model_break_view.setter
	def show_model_break_view(self, value):
		"""Gets whether to show or hide the specified Model Break View in the current configuration of the active model."""
		self._instance.ShowModelBreakView = value

	@property
	def show_smart_message(self):
		"""Displays a SOLIDWORKS-style message as a ToolTip in the graphics area and on the status bar."""
		return self._instance.ShowSmartMessage

	@show_smart_message.setter
	def show_smart_message(self, value):
		"""Displays a SOLIDWORKS-style message as a ToolTip in the graphics area and on the status bar."""
		self._instance.ShowSmartMessage = value

	@property
	def sketch_box_select(self):
		"""Box selects all of the entities in a sketch within the specified coordinates of the selection box."""
		return self._instance.SketchBoxSelect

	@sketch_box_select.setter
	def sketch_box_select(self, value):
		"""Box selects all of the entities in a sketch within the specified coordinates of the selection box."""
		self._instance.SketchBoxSelect = value

	@property
	def sketch_offset_on_surface(self):
		"""Creates a Euclidean sketch offset from selected edges of a face or surface."""
		return self._instance.SketchOffsetOnSurface

	@sketch_offset_on_surface.setter
	def sketch_offset_on_surface(self, value):
		"""Creates a Euclidean sketch offset from selected edges of a face or surface."""
		self._instance.SketchOffsetOnSurface = value

	@property
	def start_format_painter(self):
		"""Starts the Format Painter."""
		return self._instance.StartFormatPainter

	@start_format_painter.setter
	def start_format_painter(self, value):
		"""Starts the Format Painter."""
		self._instance.StartFormatPainter = value

	@property
	def start_recording_undo_object(self):
		"""Starts recording the SOLIDWORKS Undo object."""
		return self._instance.StartRecordingUndoObject

	@start_recording_undo_object.setter
	def start_recording_undo_object(self, value):
		"""Starts recording the SOLIDWORKS Undo object."""
		self._instance.StartRecordingUndoObject = value

	@property
	def stop_format_painter(self):
		"""Stops the Format Painter."""
		return self._instance.StopFormatPainter

	@stop_format_painter.setter
	def stop_format_painter(self, value):
		"""Stops the Format Painter."""
		self._instance.StopFormatPainter = value

	@property
	def stretch(self):
		"""Stretch the selected entities."""
		return self._instance.Stretch

	@stretch.setter
	def stretch(self, value):
		"""Stretch the selected entities."""
		self._instance.Stretch = value

	@property
	def update_external_file_references(self):
		"""Updates the external files references on this model."""
		return self._instance.UpdateExternalFileReferences

	@update_external_file_references.setter
	def update_external_file_references(self, value):
		"""Updates the external files references on this model."""
		self._instance.UpdateExternalFileReferences = value

	@property
	def update_frozen_features(self):
		"""Updates frozen features of the model."""
		return self._instance.UpdateFrozenFeatures

	@update_frozen_features.setter
	def update_frozen_features(self, value):
		"""Updates frozen features of the model."""
		self._instance.UpdateFrozenFeatures = value

	@property
	def update_render_materials_in_scene_graph(self):
		"""Sets whether to update the appearances in the graphics area in the model."""
		return self._instance.UpdateRenderMaterialsInSceneGraph

	@update_render_materials_in_scene_graph.setter
	def update_render_materials_in_scene_graph(self, value):
		"""Sets whether to update the appearances in the graphics area in the model."""
		self._instance.UpdateRenderMaterialsInSceneGraph = value

	@property
	def update_standard_views(self):
		"""Changes the specified standard view to the current model view."""
		return self._instance.UpdateStandardViews

	@update_standard_views.setter
	def update_standard_views(self, value):
		"""Changes the specified standard view to the current model view."""
		self._instance.UpdateStandardViews = value

	@property
	def update_sun_light(self):
		"""Updates sunlight position, color, and background image."""
		return self._instance.UpdateSunLight

	@update_sun_light.setter
	def update_sun_light(self, value):
		"""Updates sunlight position, color, and background image."""
		self._instance.UpdateSunLight = value

	@property
	def upgrade_legacy_c_threads(self):
		"""Upgrades cosmetic thread features in this legacy model to the latest cosmetic thread architecture."""
		return self._instance.UpgradeLegacyCThreads

	@upgrade_legacy_c_threads.setter
	def upgrade_legacy_c_threads(self, value):
		"""Upgrades cosmetic thread features in this legacy model to the latest cosmetic thread architecture."""
		self._instance.UpgradeLegacyCThreads = value

	@property
	def view_zoom_to_sheet(self):
		"""Zooms a drawing sheet to its maximum size within the window."""
		return self._instance.ViewZoomToSheet

	@view_zoom_to_sheet.setter
	def view_zoom_to_sheet(self, value):
		"""Zooms a drawing sheet to its maximum size within the window."""
		self._instance.ViewZoomToSheet = value

