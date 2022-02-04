# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html
class IAssemblyDoc:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def enable_assembly_rebuild(self):
		"""Gets or sets whether to suspend the rebuild of the assembly."""
		return self._instance.EnableAssemblyRebuild

	@enable_assembly_rebuild.setter
	def enable_assembly_rebuild(self, value):
		"""Gets or sets whether to suspend the rebuild of the assembly."""
		self._instance.EnableAssemblyRebuild = value

	@property
	def enable_presentation(self):
		"""Gets or sets whether the assembly is in presentation mode."""
		return self._instance.EnablePresentation

	@enable_presentation.setter
	def enable_presentation(self, value):
		"""Gets or sets whether the assembly is in presentation mode."""
		self._instance.EnablePresentation = value

	@property
	def interference_detection_manager(self):
		"""Gets the Interference Detection manager, which allows you to run interference detection on an assembly to determine whether components interfere with each other."""
		return self._instance.InterferenceDetectionManager

	@interference_detection_manager.setter
	def interference_detection_manager(self, value):
		"""Gets the Interference Detection manager, which allows you to run interference detection on an assembly to determine whether components interfere with each other."""
		self._instance.InterferenceDetectionManager = value

	@property
	def large_design_review_transparency_level(self):
		"""Gets or sets the transparency level of unmodified components in the graphics area of this assembly opened in Large Design Review mode."""
		return self._instance.LargeDesignReviewTransparencyLevel

	@large_design_review_transparency_level.setter
	def large_design_review_transparency_level(self, value):
		"""Gets or sets the transparency level of unmodified components in the graphics area of this assembly opened in Large Design Review mode."""
		self._instance.LargeDesignReviewTransparencyLevel = value

	@property
	def large_design_review_transparency_level_dynamic(self):
		"""Gets or sets whether to dynamically modify the transparency level of unmodified components in the graphics area when the transparency level slider is moved on the Filter Modified Components PropertyManager page."""
		return self._instance.LargeDesignReviewTransparencyLevelDynamic

	@large_design_review_transparency_level_dynamic.setter
	def large_design_review_transparency_level_dynamic(self, value):
		"""Gets or sets whether to dynamically modify the transparency level of unmodified components in the graphics area when the transparency level slider is moved on the Filter Modified Components PropertyManager page."""
		self._instance.LargeDesignReviewTransparencyLevelDynamic = value

	@property
	def large_design_review_transparency_level_enabled(self):
		"""Gets or sets whether transparency levels are activated for unmodified components in the graphics area for this assembly opened in Large Design Review mode."""
		return self._instance.LargeDesignReviewTransparencyLevelEnabled

	@large_design_review_transparency_level_enabled.setter
	def large_design_review_transparency_level_enabled(self, value):
		"""Gets or sets whether transparency levels are activated for unmodified components in the graphics area for this assembly opened in Large Design Review mode."""
		self._instance.LargeDesignReviewTransparencyLevelEnabled = value

	@property
	def activate_ground_plane(self):
		"""Activates the ground plane for the specified configurations."""
		return self._instance.ActivateGroundPlane

	@activate_ground_plane.setter
	def activate_ground_plane(self, value):
		"""Activates the ground plane for the specified configurations."""
		self._instance.ActivateGroundPlane = value

	@property
	def add_component(self):
		"""Adds the specified component for the specified configuration options to this assembly."""
		return self._instance.AddComponent5

	@add_component.setter
	def add_component(self, value):
		"""Adds the specified component for the specified configuration options to this assembly."""
		self._instance.AddComponent5 = value

	@property
	def add_component_configuration(self):
		"""Adds a new configuration for the last selected assembly component."""
		return self._instance.AddComponentConfiguration

	@add_component_configuration.setter
	def add_component_configuration(self, value):
		"""Adds a new configuration for the last selected assembly component."""
		self._instance.AddComponentConfiguration = value

	@property
	def add_components(self):
		"""Adds multiple components to the assembly."""
		return self._instance.AddComponents3

	@add_components.setter
	def add_components(self, value):
		"""Adds multiple components to the assembly."""
		self._instance.AddComponents3 = value

	@property
	def add_concentric_mate_with_tolerance(self):
		"""Adds a misaligned concentric mate to this assembly."""
		return self._instance.AddConcentricMateWithTolerance

	@add_concentric_mate_with_tolerance.setter
	def add_concentric_mate_with_tolerance(self, value):
		"""Adds a misaligned concentric mate to this assembly."""
		self._instance.AddConcentricMateWithTolerance = value

	@property
	def add_distance_mate(self):
		"""Adds a distance mate to this assembly."""
		return self._instance.AddDistanceMate

	@add_distance_mate.setter
	def add_distance_mate(self, value):
		"""Adds a distance mate to this assembly."""
		self._instance.AddDistanceMate = value

	@property
	def add_pipe_penetration(self):
		"""Penetrates the adjacent fitting or pipe with the pipe that ends at the selected sketch point."""
		return self._instance.AddPipePenetration

	@add_pipe_penetration.setter
	def add_pipe_penetration(self, value):
		"""Penetrates the adjacent fitting or pipe with the pipe that ends at the selected sketch point."""
		self._instance.AddPipePenetration = value

	@property
	def add_piping_fitting(self):
		"""Adds a pipe fitting to the current piping assembly."""
		return self._instance.AddPipingFitting

	@add_piping_fitting.setter
	def add_piping_fitting(self, value):
		"""Adds a pipe fitting to the current piping assembly."""
		self._instance.AddPipingFitting = value

	@property
	def add_smart_component(self):
		"""Adds the specified component at the specified coordinates as a Smart Component to this assembly."""
		return self._instance.AddSmartComponent

	@add_smart_component.setter
	def add_smart_component(self, value):
		"""Adds the specified component at the specified coordinates as a Smart Component to this assembly."""
		self._instance.AddSmartComponent = value

	@property
	def add_to_feature_scope(self):
		"""Adds a component to the scope of the currently selected assembly feature."""
		return self._instance.AddToFeatureScope

	@add_to_feature_scope.setter
	def add_to_feature_scope(self, value):
		"""Adds a component to the scope of the currently selected assembly feature."""
		self._instance.AddToFeatureScope = value

	@property
	def auto_angle_axis(self):
		"""Automatically detect the axis for an angle mate."""
		return self._instance.AutoAngleAxis

	@auto_angle_axis.setter
	def auto_angle_axis(self, value):
		"""Automatically detect the axis for an angle mate."""
		self._instance.AutoAngleAxis = value

	@property
	def auto_explode(self):
		"""Automatically generates an exploded view of the current assembly configuration."""
		return self._instance.AutoExplode

	@auto_explode.setter
	def auto_explode(self, value):
		"""Automatically generates an exploded view of the current assembly configuration."""
		self._instance.AutoExplode = value

	@property
	def comp_config_properties(self):
		"""Sets the properties for the selected component in the specified configuration."""
		return self._instance.CompConfigProperties6

	@comp_config_properties.setter
	def comp_config_properties(self, value):
		"""Sets the properties for the selected component in the specified configuration."""
		self._instance.CompConfigProperties6 = value

	@property
	def component_reload(self):
		"""Reloads and/or sets the read-only state of the specified component."""
		return self._instance.ComponentReload2

	@component_reload.setter
	def component_reload(self, value):
		"""Reloads and/or sets the read-only state of the specified component."""
		self._instance.ComponentReload2 = value

	@property
	def copy_with_mates(self):
		"""Copies one or more components with mates in this assembly."""
		return self._instance.CopyWithMates2

	@copy_with_mates.setter
	def copy_with_mates(self, value):
		"""Copies one or more components with mates in this assembly."""
		self._instance.CopyWithMates2 = value

	@property
	def create_exploded_view(self):
		"""Creates an explode view of the active assembly configuration."""
		return self._instance.CreateExplodedView

	@create_exploded_view.setter
	def create_exploded_view(self, value):
		"""Creates an explode view of the active assembly configuration."""
		self._instance.CreateExplodedView = value

	@property
	def create_mate(self):
		"""Creates a mate with the specified feature data object."""
		return self._instance.CreateMate

	@create_mate.setter
	def create_mate(self, value):
		"""Creates a mate with the specified feature data object."""
		self._instance.CreateMate = value

	@property
	def create_mate_data(self):
		"""Creates a mate feature data object for the specified mate type."""
		return self._instance.CreateMateData

	@create_mate_data.setter
	def create_mate_data(self, value):
		"""Creates a mate feature data object for the specified mate type."""
		self._instance.CreateMateData = value

	@property
	def create_smart_component(self):
		"""Creates a Smart Component."""
		return self._instance.CreateSmartComponent

	@create_smart_component.setter
	def create_smart_component(self, value):
		"""Creates a Smart Component."""
		self._instance.CreateSmartComponent = value

	@property
	def create_speed_pak(self):
		"""Creates the specified type of SpeedPak for the active configurations of the selected subassemblies in this assembly."""
		return self._instance.CreateSpeedPak

	@create_speed_pak.setter
	def create_speed_pak(self, value):
		"""Creates the specified type of SpeedPak for the active configurations of the selected subassemblies in this assembly."""
		self._instance.CreateSpeedPak = value

	@property
	def delete_selections(self):
		"""Delete either the selected components of a subassembly or the subassembly of the selected component."""
		return self._instance.DeleteSelections

	@delete_selections.setter
	def delete_selections(self, value):
		"""Delete either the selected components of a subassembly or the subassembly of the selected component."""
		self._instance.DeleteSelections = value

	@property
	def dissolve_component_pattern(self):
		"""Dissolves the selected component patterns."""
		return self._instance.DissolveComponentPattern

	@dissolve_component_pattern.setter
	def dissolve_component_pattern(self, value):
		"""Dissolves the selected component patterns."""
		self._instance.DissolveComponentPattern = value

	@property
	def dissolve_sub_assembly(self):
		"""Dissolves the selected subassembly in this assembly."""
		return self._instance.DissolveSubAssembly

	@dissolve_sub_assembly.setter
	def dissolve_sub_assembly(self, value):
		"""Dissolves the selected subassembly in this assembly."""
		self._instance.DissolveSubAssembly = value

	@property
	def edit_assembly(self):
		"""Switches back to the assembly document for editing."""
		return self._instance.EditAssembly

	@edit_assembly.setter
	def edit_assembly(self, value):
		"""Switches back to the assembly document for editing."""
		self._instance.EditAssembly = value

	@property
	def edit_concentric_mate(self):
		"""Edits a misaligned concentric mate."""
		return self._instance.EditConcentricMate

	@edit_concentric_mate.setter
	def edit_concentric_mate(self, value):
		"""Edits a misaligned concentric mate."""
		self._instance.EditConcentricMate = value

	@property
	def edit_distance_mate(self):
		"""Edits a distance mate."""
		return self._instance.EditDistanceMate

	@edit_distance_mate.setter
	def edit_distance_mate(self, value):
		"""Edits a distance mate."""
		self._instance.EditDistanceMate = value

	@property
	def edit_part(self):
		"""Edits the selected part within the context of an assembly."""
		return self._instance.EditPart2

	@edit_part.setter
	def edit_part(self, value):
		"""Edits the selected part within the context of an assembly."""
		self._instance.EditPart2 = value

	@property
	def exit_isolate(self):
		"""Exits isolating the selected components and returns the assembly to its original display state."""
		return self._instance.ExitIsolate

	@exit_isolate.setter
	def exit_isolate(self, value):
		"""Exits isolating the selected components and returns the assembly to its original display state."""
		self._instance.ExitIsolate = value

	@property
	def feature_by_name(self):
		"""Returns the IFeature object for the named feature in the assembly."""
		return self._instance.FeatureByName

	@feature_by_name.setter
	def feature_by_name(self, value):
		"""Returns the IFeature object for the named feature in the assembly."""
		self._instance.FeatureByName = value

	@property
	def file_derive_component_part(self):
		"""Creates a new part document from the currently selected assembly component."""
		return self._instance.FileDeriveComponentPart

	@file_derive_component_part.setter
	def file_derive_component_part(self, value):
		"""Creates a new part document from the currently selected assembly component."""
		self._instance.FileDeriveComponentPart = value

	@property
	def fix_component(self):
		"""Fixes the selected component; i.e., makes it immovable."""
		return self._instance.FixComponent

	@fix_component.setter
	def fix_component(self, value):
		"""Fixes the selected component; i.e., makes it immovable."""
		self._instance.FixComponent = value

	@property
	def force_update_electrical_data(self):
		"""Forces an update of electrical data."""
		return self._instance.ForceUpdateElectricalData2

	@force_update_electrical_data.setter
	def force_update_electrical_data(self, value):
		"""Forces an update of electrical data."""
		self._instance.ForceUpdateElectricalData2 = value

	@property
	def get_active_ground_plane(self):
		"""Gets the active ground plane for the specified configurations."""
		return self._instance.GetActiveGroundPlane

	@get_active_ground_plane.setter
	def get_active_ground_plane(self, value):
		"""Gets the active ground plane for the specified configurations."""
		self._instance.GetActiveGroundPlane = value

	@property
	def get_advanced_selection(self):
		"""Gets the advanced component selection criteria object for this assembly."""
		return self._instance.GetAdvancedSelection

	@get_advanced_selection.setter
	def get_advanced_selection(self, value):
		"""Gets the advanced component selection criteria object for this assembly."""
		self._instance.GetAdvancedSelection = value

	@property
	def get_box(self):
		"""Gets the bounding box."""
		return self._instance.GetBox

	@get_box.setter
	def get_box(self, value):
		"""Gets the bounding box."""
		self._instance.GetBox = value

	@property
	def get_component_by_i_d(self):
		"""Gets a top-level assembly component using its component ID."""
		return self._instance.GetComponentByID

	@get_component_by_i_d.setter
	def get_component_by_i_d(self, value):
		"""Gets a top-level assembly component using its component ID."""
		self._instance.GetComponentByID = value

	@property
	def get_component_by_name(self):
		"""Gets the specified top-level assembly component."""
		return self._instance.GetComponentByName

	@get_component_by_name.setter
	def get_component_by_name(self, value):
		"""Gets the specified top-level assembly component."""
		self._instance.GetComponentByName = value

	@property
	def get_component_count(self):
		"""Gets the number of components in the active configuration of this assembly."""
		return self._instance.GetComponentCount

	@get_component_count.setter
	def get_component_count(self, value):
		"""Gets the number of components in the active configuration of this assembly."""
		self._instance.GetComponentCount = value

	@property
	def get_components(self):
		"""Gets all of the components in the active configuration of this assembly."""
		return self._instance.GetComponents

	@get_components.setter
	def get_components(self, value):
		"""Gets all of the components in the active configuration of this assembly."""
		self._instance.GetComponents = value

	@property
	def get_drag_operator(self):
		"""Gets the drag operator for dynamic drag operations in this assembly."""
		return self._instance.GetDragOperator

	@get_drag_operator.setter
	def get_drag_operator(self, value):
		"""Gets the drag operator for dynamic drag operations in this assembly."""
		self._instance.GetDragOperator = value

	@property
	def get_dropped_at_entity(self):
		"""Gets a pointer to the entity where a file is dropped into this assembly."""
		return self._instance.GetDroppedAtEntity

	@get_dropped_at_entity.setter
	def get_dropped_at_entity(self, value):
		"""Gets a pointer to the entity where a file is dropped into this assembly."""
		self._instance.GetDroppedAtEntity = value

	@property
	def get_edit_target(self):
		"""Gets the model document that is currently being edited."""
		return self._instance.GetEditTarget

	@get_edit_target.setter
	def get_edit_target(self, value):
		"""Gets the model document that is currently being edited."""
		self._instance.GetEditTarget = value

	@property
	def get_edit_target_component(self):
		"""Gets the component that is currently being edited."""
		return self._instance.GetEditTargetComponent

	@get_edit_target_component.setter
	def get_edit_target_component(self, value):
		"""Gets the component that is currently being edited."""
		self._instance.GetEditTargetComponent = value

	@property
	def get_exploded_view_configuration_name(self):
		"""Gets the name of the configuration for the specified exploded view."""
		return self._instance.GetExplodedViewConfigurationName

	@get_exploded_view_configuration_name.setter
	def get_exploded_view_configuration_name(self, value):
		"""Gets the name of the configuration for the specified exploded view."""
		self._instance.GetExplodedViewConfigurationName = value

	@property
	def get_exploded_view_count(self):
		"""Gets the number of exploded views in the specified configuration."""
		return self._instance.GetExplodedViewCount2

	@get_exploded_view_count.setter
	def get_exploded_view_count(self, value):
		"""Gets the number of exploded views in the specified configuration."""
		self._instance.GetExplodedViewCount2 = value

	@property
	def get_exploded_view_names(self):
		"""Gets the names of the exploded views in the specified configuration."""
		return self._instance.GetExplodedViewNames2

	@get_exploded_view_names.setter
	def get_exploded_view_names(self, value):
		"""Gets the names of the exploded views in the specified configuration."""
		self._instance.GetExplodedViewNames2 = value

	@property
	def get_feature_scope(self):
		"""Gets the components affected by this feature."""
		return self._instance.GetFeatureScope

	@get_feature_scope.setter
	def get_feature_scope(self, value):
		"""Gets the components affected by this feature."""
		self._instance.GetFeatureScope = value

	@property
	def get_feature_scope_count(self):
		"""Gets the number of components affected by this feature."""
		return self._instance.GetFeatureScopeCount

	@get_feature_scope_count.setter
	def get_feature_scope_count(self, value):
		"""Gets the number of components affected by this feature."""
		self._instance.GetFeatureScopeCount = value

	@property
	def get_light_weight_component_count(self):
		"""Gets the number of lightweight components in the assembly."""
		return self._instance.GetLightWeightComponentCount

	@get_light_weight_component_count.setter
	def get_light_weight_component_count(self, value):
		"""Gets the number of lightweight components in the assembly."""
		self._instance.GetLightWeightComponentCount = value

	@property
	def get_route_manager(self):
		"""Gets the SOLIDWORKS Routing API."""
		return self._instance.GetRouteManager

	@get_route_manager.setter
	def get_route_manager(self, value):
		"""Gets the SOLIDWORKS Routing API."""
		self._instance.GetRouteManager = value

	@property
	def get_unloaded_component_names(self):
		"""Gets the unloaded components' paths, referenced configuration names, reasons why they are unloaded, document types, and names."""
		return self._instance.GetUnloadedComponentNames

	@get_unloaded_component_names.setter
	def get_unloaded_component_names(self, value):
		"""Gets the unloaded components' paths, referenced configuration names, reasons why they are unloaded, document types, and names."""
		self._instance.GetUnloadedComponentNames = value

	@property
	def get_visible_components_in_view(self):
		"""Gets a list of visible components in this assembly to save as solid bodies."""
		return self._instance.GetVisibleComponentsInView

	@get_visible_components_in_view.setter
	def get_visible_components_in_view(self, value):
		"""Gets a list of visible components in this assembly to save as solid bodies."""
		self._instance.GetVisibleComponentsInView = value

	@property
	def get_visible_components_in_view_count(self):
		"""Gets the number of visible components in this assembly."""
		return self._instance.GetVisibleComponentsInViewCount

	@get_visible_components_in_view_count.setter
	def get_visible_components_in_view_count(self, value):
		"""Gets the number of visible components in this assembly."""
		self._instance.GetVisibleComponentsInViewCount = value

	@property
	def has_unloaded_components(self):
		"""Gets whether this assembly has hidden or suppressed unloaded components."""
		return self._instance.HasUnloadedComponents

	@has_unloaded_components.setter
	def has_unloaded_components(self, value):
		"""Gets whether this assembly has hidden or suppressed unloaded components."""
		self._instance.HasUnloadedComponents = value

	@property
	def i_add_components(self):
		"""Adds multiple components to the assembly."""
		return self._instance.IAddComponents3

	@i_add_components.setter
	def i_add_components(self, value):
		"""Adds multiple components to the assembly."""
		self._instance.IAddComponents3 = value

	@property
	def i_feature_by_name(self):
		"""Returns the IFeature object for the named feature in the assembly."""
		return self._instance.IFeatureByName

	@i_feature_by_name.setter
	def i_feature_by_name(self, value):
		"""Returns the IFeature object for the named feature in the assembly."""
		self._instance.IFeatureByName = value

	@property
	def i_get_box(self):
		"""Gets the bounding box."""
		return self._instance.IGetBox

	@i_get_box.setter
	def i_get_box(self, value):
		"""Gets the bounding box."""
		self._instance.IGetBox = value

	@property
	def i_get_components(self):
		"""Gets all of the components in the active configuration of this assembly."""
		return self._instance.IGetComponents

	@i_get_components.setter
	def i_get_components(self, value):
		"""Gets all of the components in the active configuration of this assembly."""
		self._instance.IGetComponents = value

	@property
	def i_get_drag_operator(self):
		"""Gets the drag operator for dynamic drag operations in this assembly."""
		return self._instance.IGetDragOperator

	@i_get_drag_operator.setter
	def i_get_drag_operator(self, value):
		"""Gets the drag operator for dynamic drag operations in this assembly."""
		self._instance.IGetDragOperator = value

	@property
	def i_get_edit_target(self):
		"""Gets the model document that is currently being edited."""
		return self._instance.IGetEditTarget2

	@i_get_edit_target.setter
	def i_get_edit_target(self, value):
		"""Gets the model document that is currently being edited."""
		self._instance.IGetEditTarget2 = value

	@property
	def i_get_feature_scope(self):
		"""Gets the components affected by this feature."""
		return self._instance.IGetFeatureScope

	@i_get_feature_scope.setter
	def i_get_feature_scope(self, value):
		"""Gets the components affected by this feature."""
		self._instance.IGetFeatureScope = value

	@property
	def i_get_visible_components_in_view(self):
		"""Gets a list of visible components in this assembly to save as solid bodies."""
		return self._instance.IGetVisibleComponentsInView

	@i_get_visible_components_in_view.setter
	def i_get_visible_components_in_view(self, value):
		"""Gets a list of visible components in this assembly to save as solid bodies."""
		self._instance.IGetVisibleComponentsInView = value

	@property
	def insert_cavity(self):
		"""Inserts a cavity to the active part using a selected component."""
		return self._instance.InsertCavity4

	@insert_cavity.setter
	def insert_cavity(self, value):
		"""Inserts a cavity to the active part using a selected component."""
		self._instance.InsertCavity4 = value

	@property
	def insert_envelope(self):
		"""Adds an envelope in the specified configuration name in this assembly."""
		return self._instance.InsertEnvelope

	@insert_envelope.setter
	def insert_envelope(self, value):
		"""Adds an envelope in the specified configuration name in this assembly."""
		self._instance.InsertEnvelope = value

	@property
	def insert_imported_component(self):
		"""Inserts a third-party native CAD part or assembly into the current configuration of this assembly."""
		return self._instance.InsertImportedComponent

	@insert_imported_component.setter
	def insert_imported_component(self, value):
		"""Inserts a third-party native CAD part or assembly into the current configuration of this assembly."""
		self._instance.InsertImportedComponent = value

	@property
	def insert_join(self):
		"""Constructs a feature from merged selected components."""
		return self._instance.InsertJoin2

	@insert_join.setter
	def insert_join(self, value):
		"""Constructs a feature from merged selected components."""
		self._instance.InsertJoin2 = value

	@property
	def insert_load_reference(self):
		"""Creates a mate load reference to the specified or selected mate."""
		return self._instance.InsertLoadReference

	@insert_load_reference.setter
	def insert_load_reference(self, value):
		"""Creates a mate load reference to the specified or selected mate."""
		self._instance.InsertLoadReference = value

	@property
	def insert_new_assembly(self):
		"""Creates a new virtual sub-assembly and optionally saves it to the specified file."""
		return self._instance.InsertNewAssembly

	@insert_new_assembly.setter
	def insert_new_assembly(self, value):
		"""Creates a new virtual sub-assembly and optionally saves it to the specified file."""
		self._instance.InsertNewAssembly = value

	@property
	def insert_new_part(self):
		"""Inserts a new part on the specified face or plane."""
		return self._instance.InsertNewPart2

	@insert_new_part.setter
	def insert_new_part(self, value):
		"""Inserts a new part on the specified face or plane."""
		self._instance.InsertNewPart2 = value

	@property
	def insert_new_virtual_assembly(self):
		"""Creates a new assembly from this assembly and saves it internally as a virtual component."""
		return self._instance.InsertNewVirtualAssembly

	@insert_new_virtual_assembly.setter
	def insert_new_virtual_assembly(self, value):
		"""Creates a new assembly from this assembly and saves it internally as a virtual component."""
		self._instance.InsertNewVirtualAssembly = value

	@property
	def insert_new_virtual_part(self):
		"""Creates a new part in the context of an assembly and saves the part internally in the assembly file as a virtual component."""
		return self._instance.InsertNewVirtualPart

	@insert_new_virtual_part.setter
	def insert_new_virtual_part(self, value):
		"""Creates a new part in the context of an assembly and saves the part internally in the assembly file as a virtual component."""
		self._instance.InsertNewVirtualPart = value

	@property
	def i_reorder_components(self):
		"""Moves components to a different location in the FeatureManager tree."""
		return self._instance.IReorderComponents

	@i_reorder_components.setter
	def i_reorder_components(self, value):
		"""Moves components to a different location in the FeatureManager tree."""
		self._instance.IReorderComponents = value

	@property
	def i_reorganize_components(self):
		"""Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly."""
		return self._instance.IReorganizeComponents

	@i_reorganize_components.setter
	def i_reorganize_components(self, value):
		"""Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly."""
		self._instance.IReorganizeComponents = value

	@property
	def is_component_tree_valid(self):
		"""Checks the validity of the component tree for this assembly."""
		return self._instance.IsComponentTreeValid

	@is_component_tree_valid.setter
	def is_component_tree_valid(self, value):
		"""Checks the validity of the component tree for this assembly."""
		self._instance.IsComponentTreeValid = value

	@property
	def i_set_component_state(self):
		"""Sets the suppression state for the specified components."""
		return self._instance.ISetComponentState

	@i_set_component_state.setter
	def i_set_component_state(self, value):
		"""Sets the suppression state for the specified components."""
		self._instance.ISetComponentState = value

	@property
	def i_set_component_visibility(self):
		"""Hides or shows the selected component in the specified configurations in this assembly document."""
		return self._instance.ISetComponentVisibility

	@i_set_component_visibility.setter
	def i_set_component_visibility(self, value):
		"""Hides or shows the selected component in the specified configurations in this assembly document."""
		self._instance.ISetComponentVisibility = value

	@property
	def isolate(self):
		"""Isolates the selected components."""
		return self._instance.Isolate

	@isolate.setter
	def isolate(self, value):
		"""Isolates the selected components."""
		self._instance.Isolate = value

	@property
	def is_route_assembly(self):
		"""Gets whether the assembly document is a routing assembly."""
		return self._instance.IsRouteAssembly

	@is_route_assembly.setter
	def is_route_assembly(self, value):
		"""Gets whether the assembly document is a routing assembly."""
		self._instance.IsRouteAssembly = value

	@property
	def lightweight_all_resolved(self):
		"""Sets to lightweight all resolved child components of the selected components."""
		return self._instance.LightweightAllResolved

	@lightweight_all_resolved.setter
	def lightweight_all_resolved(self, value):
		"""Sets to lightweight all resolved child components of the selected components."""
		self._instance.LightweightAllResolved = value

	@property
	def make_assembly_from_selected_components(self):
		"""Creates a new assembly comprised of the selected components of this assembly."""
		return self._instance.MakeAssemblyFromSelectedComponents

	@make_assembly_from_selected_components.setter
	def make_assembly_from_selected_components(self, value):
		"""Creates a new assembly comprised of the selected components of this assembly."""
		self._instance.MakeAssemblyFromSelectedComponents = value

	@property
	def make_independent(self):
		"""Makes the selected component independent."""
		return self._instance.MakeIndependent

	@make_independent.setter
	def make_independent(self, value):
		"""Makes the selected component independent."""
		self._instance.MakeIndependent = value

	@property
	def make_light_weight(self):
		"""Sets the selected components to lightweight."""
		return self._instance.MakeLightWeight

	@make_light_weight.setter
	def make_light_weight(self, value):
		"""Sets the selected components to lightweight."""
		self._instance.MakeLightWeight = value

	@property
	def remove_from_feature_scope(self):
		"""Removes a component from the scope of the currently selected assembly feature."""
		return self._instance.RemoveFromFeatureScope

	@remove_from_feature_scope.setter
	def remove_from_feature_scope(self, value):
		"""Removes a component from the scope of the currently selected assembly feature."""
		self._instance.RemoveFromFeatureScope = value

	@property
	def reorder_components(self):
		"""Moves components to a different location in the FeatureManager design tree."""
		return self._instance.ReorderComponents

	@reorder_components.setter
	def reorder_components(self, value):
		"""Moves components to a different location in the FeatureManager design tree."""
		self._instance.ReorderComponents = value

	@property
	def reorganize_components(self):
		"""Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly."""
		return self._instance.ReorganizeComponents

	@reorganize_components.setter
	def reorganize_components(self, value):
		"""Reorganizes an assembly's structure by moving the selected components to the selected assembly or sub-assembly."""
		self._instance.ReorganizeComponents = value

	@property
	def replace_components(self):
		"""Replaces one or more selected components with another model."""
		return self._instance.ReplaceComponents2

	@replace_components.setter
	def replace_components(self, value):
		"""Replaces one or more selected components with another model."""
		self._instance.ReplaceComponents2 = value

	@property
	def resolve_all_lightweight(self):
		"""Resolves all lightweight child components of the selected components"""
		return self._instance.ResolveAllLightweight

	@resolve_all_lightweight.setter
	def resolve_all_lightweight(self, value):
		"""Resolves all lightweight child components of the selected components"""
		self._instance.ResolveAllLightweight = value

	@property
	def resolve_all_light_weight_components(self):
		"""Resolves the lightweight components in this assembly."""
		return self._instance.ResolveAllLightWeightComponents

	@resolve_all_light_weight_components.setter
	def resolve_all_light_weight_components(self, value):
		"""Resolves the lightweight components in this assembly."""
		self._instance.ResolveAllLightWeightComponents = value

	@property
	def resolve_out_of_date_light_weight_components(self):
		"""Resolves the selected out-of-date lightweight component, and any out-of-date lightweight sub-components, in the assembly."""
		return self._instance.ResolveOutOfDateLightWeightComponents

	@resolve_out_of_date_light_weight_components.setter
	def resolve_out_of_date_light_weight_components(self, value):
		"""Resolves the selected out-of-date lightweight component, and any out-of-date lightweight sub-components, in the assembly."""
		self._instance.ResolveOutOfDateLightWeightComponents = value

	@property
	def rotate_component(self):
		"""Displays the Rotate Component PropertyManager page."""
		return self._instance.RotateComponent

	@rotate_component.setter
	def rotate_component(self, value):
		"""Displays the Rotate Component PropertyManager page."""
		self._instance.RotateComponent = value

	@property
	def rotate_component_axis(self):
		"""Rotates the component axis by a fixed amount."""
		return self._instance.RotateComponentAxis

	@rotate_component_axis.setter
	def rotate_component_axis(self, value):
		"""Rotates the component axis by a fixed amount."""
		self._instance.RotateComponentAxis = value

	@property
	def save_isolate(self):
		"""Saves the display characteristics of the isolated components to a new display state."""
		return self._instance.SaveIsolate

	@save_isolate.setter
	def save_isolate(self, value):
		"""Saves the display characteristics of the isolated components to a new display state."""
		self._instance.SaveIsolate = value

	@property
	def select_components_by_size(self):
		"""Selects assembly components by percent of assembly size."""
		return self._instance.SelectComponentsBySize

	@select_components_by_size.setter
	def select_components_by_size(self, value):
		"""Selects assembly components by percent of assembly size."""
		self._instance.SelectComponentsBySize = value

	@property
	def selective_open(self):
		"""Selectively opens the components of an assembly that is opened in Large Design Review mode."""
		return self._instance.SelectiveOpen

	@selective_open.setter
	def selective_open(self, value):
		"""Selectively opens the components of an assembly that is opened in Large Design Review mode."""
		self._instance.SelectiveOpen = value

	@property
	def set_component_state(self):
		"""Sets the suppression state for the specified components."""
		return self._instance.SetComponentState

	@set_component_state.setter
	def set_component_state(self, value):
		"""Sets the suppression state for the specified components."""
		self._instance.SetComponentState = value

	@property
	def set_component_suppression(self):
		"""Suppresses, resolves, or sets to lightweight selected components of this assembly in the active configuration only."""
		return self._instance.SetComponentSuppression

	@set_component_suppression.setter
	def set_component_suppression(self, value):
		"""Suppresses, resolves, or sets to lightweight selected components of this assembly in the active configuration only."""
		self._instance.SetComponentSuppression = value

	@property
	def set_component_transparent(self):
		"""Enables or disables transparency on the selected components."""
		return self._instance.SetComponentTransparent

	@set_component_transparent.setter
	def set_component_transparent(self, value):
		"""Enables or disables transparency on the selected components."""
		self._instance.SetComponentTransparent = value

	@property
	def set_component_visibility(self):
		"""Hides or shows the selected component in the specified configurations in this assembly document."""
		return self._instance.SetComponentVisibility

	@set_component_visibility.setter
	def set_component_visibility(self, value):
		"""Hides or shows the selected component in the specified configurations in this assembly document."""
		self._instance.SetComponentVisibility = value

	@property
	def set_dropped_file_config_name(self):
		"""Sets the configuration name for the recently dropped file."""
		return self._instance.SetDroppedFileConfigName

	@set_dropped_file_config_name.setter
	def set_dropped_file_config_name(self, value):
		"""Sets the configuration name for the recently dropped file."""
		self._instance.SetDroppedFileConfigName = value

	@property
	def set_dropped_file_feature_name(self):
		"""Sets the name of the feature for the recently dropped file."""
		return self._instance.SetDroppedFileFeatureName

	@set_dropped_file_feature_name.setter
	def set_dropped_file_feature_name(self, value):
		"""Sets the name of the feature for the recently dropped file."""
		self._instance.SetDroppedFileFeatureName = value

	@property
	def set_dropped_file_name(self):
		"""Sets the new file name for a recently dropped file."""
		return self._instance.SetDroppedFileName

	@set_dropped_file_name.setter
	def set_dropped_file_name(self, value):
		"""Sets the new file name for a recently dropped file."""
		self._instance.SetDroppedFileName = value

	@property
	def set_isolate_visibility(self):
		"""Sets the display characteristics of all of the components not selected to isolate."""
		return self._instance.SetIsolateVisibility

	@set_isolate_visibility.setter
	def set_isolate_visibility(self, value):
		"""Sets the display characteristics of all of the components not selected to isolate."""
		self._instance.SetIsolateVisibility = value

	@property
	def set_speed_pak_configurations(self):
		"""Sets the configurations in the selected subassemblies to which to apply SpeedPak in this assembly."""
		return self._instance.SetSpeedPakConfigurations

	@set_speed_pak_configurations.setter
	def set_speed_pak_configurations(self, value):
		"""Sets the configurations in the selected subassemblies to which to apply SpeedPak in this assembly."""
		self._instance.SetSpeedPakConfigurations = value

	@property
	def set_speed_pak_to_parent(self):
		"""Switches the selected subassemblies from the SpeedPak configuration to the parent configuration of the SpeedPak configuration."""
		return self._instance.SetSpeedPakToParent

	@set_speed_pak_to_parent.setter
	def set_speed_pak_to_parent(self, value):
		"""Switches the selected subassemblies from the SpeedPak configuration to the parent configuration of the SpeedPak configuration."""
		self._instance.SetSpeedPakToParent = value

	@property
	def show_exploded(self):
		"""Displays the specified exploded view for the current assembly configuration."""
		return self._instance.ShowExploded2

	@show_exploded.setter
	def show_exploded(self, value):
		"""Displays the specified exploded view for the current assembly configuration."""
		self._instance.ShowExploded2 = value

	@property
	def temporary_fix_group(self):
		"""Temporarily fix or group selected components during such operations as drag, move, rotate, etc."""
		return self._instance.TemporaryFixGroup

	@temporary_fix_group.setter
	def temporary_fix_group(self, value):
		"""Temporarily fix or group selected components during such operations as drag, move, rotate, etc."""
		self._instance.TemporaryFixGroup = value

	@property
	def temporary_fix_group_exit(self):
		"""Changes components that were temporarily fixed or grouped back to floating or ungrouped after such operations as drag, move, rotate, etc."""
		return self._instance.TemporaryFixGroupExit

	@temporary_fix_group_exit.setter
	def temporary_fix_group_exit(self, value):
		"""Changes components that were temporarily fixed or grouped back to floating or ungrouped after such operations as drag, move, rotate, etc."""
		self._instance.TemporaryFixGroupExit = value

	@property
	def tools_check_interference(self):
		"""Checks for interference between parts in this assembly."""
		return self._instance.ToolsCheckInterference2

	@tools_check_interference.setter
	def tools_check_interference(self, value):
		"""Checks for interference between parts in this assembly."""
		self._instance.ToolsCheckInterference2 = value

	@property
	def translate_component(self):
		"""Displays the Move Component PropertyManager page."""
		return self._instance.TranslateComponent

	@translate_component.setter
	def translate_component(self, value):
		"""Displays the Move Component PropertyManager page."""
		self._instance.TranslateComponent = value

	@property
	def unfix_component(self):
		"""Floats the selected component; i.e., makes it movable."""
		return self._instance.UnfixComponent

	@unfix_component.setter
	def unfix_component(self, value):
		"""Floats the selected component; i.e., makes it movable."""
		self._instance.UnfixComponent = value

	@property
	def ungroup_components(self):
		"""Ungroups the grouped components in the selected folder in the FeatureManager design tree."""
		return self._instance.UngroupComponents

	@ungroup_components.setter
	def ungroup_components(self, value):
		"""Ungroups the grouped components in the selected folder in the FeatureManager design tree."""
		self._instance.UngroupComponents = value

	@property
	def update_box(self):
		"""Updates the bounding box for this assembly."""
		return self._instance.UpdateBox

	@update_box.setter
	def update_box(self, value):
		"""Updates the bounding box for this assembly."""
		self._instance.UpdateBox = value

	@property
	def update_feature_scope(self):
		"""Updates the feature scope and rebuilds the currently selected assembly feature."""
		return self._instance.UpdateFeatureScope

	@update_feature_scope.setter
	def update_feature_scope(self, value):
		"""Updates the feature scope and rebuilds the currently selected assembly feature."""
		self._instance.UpdateFeatureScope = value

	@property
	def update_speed_pak(self):
		"""Updates out-of-date SpeedPak configurations for the selected subassemblies."""
		return self._instance.UpdateSpeedPak

	@update_speed_pak.setter
	def update_speed_pak(self, value):
		"""Updates out-of-date SpeedPak configurations for the selected subassemblies."""
		self._instance.UpdateSpeedPak = value

	@property
	def update_toolbox_component(self):
		"""Updates SOLIDWORKS Toolbox components in the specified assembly level using the current information in Toolbox settings."""
		return self._instance.UpdateToolboxComponent

	@update_toolbox_component.setter
	def update_toolbox_component(self, value):
		"""Updates SOLIDWORKS Toolbox components in the specified assembly level using the current information in Toolbox settings."""
		self._instance.UpdateToolboxComponent = value

	@property
	def use_speed_pak(self):
		"""Sets whether to switch the selected subassemblies whose active configuration is the parent configuration of a SpeedPak configuration to the SpeedPak configuration."""
		return self._instance.UseSpeedPak

	@use_speed_pak.setter
	def use_speed_pak(self, value):
		"""Sets whether to switch the selected subassemblies whose active configuration is the parent configuration of a SpeedPak configuration to the SpeedPak configuration."""
		self._instance.UseSpeedPak = value

	@property
	def view_collapse_assembly(self):
		"""Collapses the selected exploded view on the Configuration tab of the FeatureManager design tree."""
		return self._instance.ViewCollapseAssembly

	@view_collapse_assembly.setter
	def view_collapse_assembly(self, value):
		"""Collapses the selected exploded view on the Configuration tab of the FeatureManager design tree."""
		self._instance.ViewCollapseAssembly = value

	@property
	def view_explode_assembly(self):
		"""Explodes the selected exploded view on the Configuration tab of the FeatureManager design tree."""
		return self._instance.ViewExplodeAssembly

	@view_explode_assembly.setter
	def view_explode_assembly(self, value):
		"""Explodes the selected exploded view on the Configuration tab of the FeatureManager design tree."""
		self._instance.ViewExplodeAssembly = value

