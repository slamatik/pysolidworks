# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html
class IConfiguration:
	def __init__(self, parent=None):
		self._instance = parent

	def add_rebuild_save_mark(self):
		"""Adds or removes the mark indicating whether the configuration needs to be rebuilt and its configuration data saved every time you save the model document."""
		# return self._instance.AddRebuildSaveMark
		raise NotImplemented

	@property
	def alternate_name(self):
		"""Gets or sets the configuration's alternate name (i.e., user-specified name)."""
		return self._instance.AlternateName

	@alternate_name.setter
	def alternate_name(self, value):
		"""Gets or sets the configuration's alternate name (i.e., user-specified name)."""
		self._instance.AlternateName = value

	@property
	def b_o_m_part_no_source(self):
		"""Gets the source of the part number used in the BOM table."""
		return self._instance.BOMPartNoSource

	@b_o_m_part_no_source.setter
	def b_o_m_part_no_source(self, value):
		"""Gets the source of the part number used in the BOM table."""
		self._instance.BOMPartNoSource = value

	@property
	def child_component_display_in_b_o_m(self):
		"""Gets or sets the child component display option of a configuration in a Bill of Materials (BOM) for an assembly document."""
		return self._instance.ChildComponentDisplayInBOM

	@child_component_display_in_b_o_m.setter
	def child_component_display_in_b_o_m(self, value):
		"""Gets or sets the child component display option of a configuration in a Bill of Materials (BOM) for an assembly document."""
		self._instance.ChildComponentDisplayInBOM = value

	@property
	def comment(self):
		"""Gets or sets the configuration comment."""
		return self._instance.Comment

	@comment.setter
	def comment(self, value):
		"""Gets or sets the configuration comment."""
		self._instance.Comment = value

	@property
	def custom_property_manager(self):
		"""Gets the custom property information for this configuration."""
		return self._instance.CustomPropertyManager

	@custom_property_manager.setter
	def custom_property_manager(self, value):
		"""Gets the custom property information for this configuration."""
		self._instance.CustomPropertyManager = value

	@property
	def description(self):
		"""Gets or sets the description of the configuration."""
		return self._instance.Description

	@description.setter
	def description(self, value):
		"""Gets or sets the description of the configuration."""
		self._instance.Description = value

	@property
	def dim_xpert_manager(self):
		"""Gets the DimXpert schema for this configuration."""
		return self._instance.DimXpertManager

	@dim_xpert_manager.setter
	def dim_xpert_manager(self, value):
		"""Gets the DimXpert schema for this configuration."""
		self._instance.DimXpertManager = value

	@property
	def hide_new_component_models(self):
		"""Gets or sets whether new components are hidden in this inactive configuration."""
		return self._instance.HideNewComponentModels

	@hide_new_component_models.setter
	def hide_new_component_models(self, value):
		"""Gets or sets whether new components are hidden in this inactive configuration."""
		self._instance.HideNewComponentModels = value

	@property
	def large_design_review_mark(self):
		"""Gets or sets whether to generate a display list for this configuration when the document is saved."""
		return self._instance.LargeDesignReviewMark

	@large_design_review_mark.setter
	def large_design_review_mark(self, value):
		"""Gets or sets whether to generate a display list for this configuration when the document is saved."""
		self._instance.LargeDesignReviewMark = value

	@property
	def lock(self):
		"""Gets or sets whether the configuration is locked."""
		return self._instance.Lock

	@lock.setter
	def lock(self, value):
		"""Gets or sets whether the configuration is locked."""
		self._instance.Lock = value

	@property
	def name(self):
		"""Gets or sets the configuration name."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the configuration name."""
		self._instance.Name = value

	@property
	def needs_rebuild(self):
		"""Gets whether the configuration needs to be rebuilt."""
		return self._instance.NeedsRebuild

	@needs_rebuild.setter
	def needs_rebuild(self, value):
		"""Gets whether the configuration needs to be rebuilt."""
		self._instance.NeedsRebuild = value

	@property
	def suppress_new_component_models(self):
		"""Gets or sets whether new components are suppressed in this configuration."""
		return self._instance.SuppressNewComponentModels

	@suppress_new_component_models.setter
	def suppress_new_component_models(self, value):
		"""Gets or sets whether new components are suppressed in this configuration."""
		self._instance.SuppressNewComponentModels = value

	@property
	def suppress_new_features(self):
		"""Gets or sets whether to suppress new features in this configuration."""
		return self._instance.SuppressNewFeatures

	@suppress_new_features.setter
	def suppress_new_features(self, value):
		"""Gets or sets whether to suppress new features in this configuration."""
		self._instance.SuppressNewFeatures = value

	@property
	def type(self):
		"""Gets the type of configuration."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the type of configuration."""
		self._instance.Type = value

	@property
	def use_alternate_name_in_b_o_m(self):
		"""Gets or sets whether the alternate name (i.e., user-specified name) is displayed in the bill of materials for this configuration."""
		return self._instance.UseAlternateNameInBOM

	@use_alternate_name_in_b_o_m.setter
	def use_alternate_name_in_b_o_m(self, value):
		"""Gets or sets whether the alternate name (i.e., user-specified name) is displayed in the bill of materials for this configuration."""
		self._instance.UseAlternateNameInBOM = value

	@property
	def use_description_in_b_o_m(self):
		"""Gets or sets whether the description of the configuration is displayed in the bill of materials."""
		return self._instance.UseDescriptionInBOM

	@use_description_in_b_o_m.setter
	def use_description_in_b_o_m(self, value):
		"""Gets or sets whether the description of the configuration is displayed in the bill of materials."""
		self._instance.UseDescriptionInBOM = value

	@property
	def add_explode_step(self):
		"""Adds a regular (translate and rotate) explode step to the explode view of the active configuration."""
		return self._instance.AddExplodeStep2

	@add_explode_step.setter
	def add_explode_step(self, value):
		"""Adds a regular (translate and rotate) explode step to the explode view of the active configuration."""
		self._instance.AddExplodeStep2 = value

	@property
	def add_part_explode_step(self):
		"""Adds an explode step to the specified explode view of a multibody part."""
		return self._instance.AddPartExplodeStep

	@add_part_explode_step.setter
	def add_part_explode_step(self, value):
		"""Adds an explode step to the specified explode view of a multibody part."""
		self._instance.AddPartExplodeStep = value

	@property
	def add_radial_explode_step(self):
		"""Adds a radial explode step to the explode view of the active configuration."""
		return self._instance.AddRadialExplodeStep

	@add_radial_explode_step.setter
	def add_radial_explode_step(self, value):
		"""Adds a radial explode step to the explode view of the active configuration."""
		self._instance.AddRadialExplodeStep = value

	@property
	def apply_display_state(self):
		"""Applies the specified display state to this configuration."""
		return self._instance.ApplyDisplayState

	@apply_display_state.setter
	def apply_display_state(self, value):
		"""Applies the specified display state to this configuration."""
		self._instance.ApplyDisplayState = value

	@property
	def copy_display_state_from_configuration(self):
		"""Copies the specified display state from the specified configuration to this configuration."""
		return self._instance.CopyDisplayStateFromConfiguration

	@copy_display_state_from_configuration.setter
	def copy_display_state_from_configuration(self, value):
		"""Copies the specified display state from the specified configuration to this configuration."""
		self._instance.CopyDisplayStateFromConfiguration = value

	@property
	def create_display_state(self):
		"""Creates a display state for this configuration."""
		return self._instance.CreateDisplayState

	@create_display_state.setter
	def create_display_state(self, value):
		"""Creates a display state for this configuration."""
		self._instance.CreateDisplayState = value

	@property
	def delete_display_state(self):
		"""Deletes the specified display state from this configuration."""
		return self._instance.DeleteDisplayState

	@delete_display_state.setter
	def delete_display_state(self, value):
		"""Deletes the specified display state from this configuration."""
		self._instance.DeleteDisplayState = value

	@property
	def delete_explode_step(self):
		"""Deletes the specified explode step."""
		return self._instance.DeleteExplodeStep

	@delete_explode_step.setter
	def delete_explode_step(self, value):
		"""Deletes the specified explode step."""
		self._instance.DeleteExplodeStep = value

	@property
	def get_d_experience_type(self):
		"""Gets how this configuration is viewed in SOLIDWORKS Connected."""
		return self._instance.Get3DExperienceType

	@get_d_experience_type.setter
	def get_d_experience_type(self, value):
		"""Gets how this configuration is viewed in SOLIDWORKS Connected."""
		self._instance.Get3DExperienceType = value

	@property
	def get_children(self):
		"""Gets all of the children configurations of this derived configuration."""
		return self._instance.GetChildren

	@get_children.setter
	def get_children(self, value):
		"""Gets all of the children configurations of this derived configuration."""
		self._instance.GetChildren = value

	@property
	def get_children_count(self):
		"""Gets the number of children for this configuration."""
		return self._instance.GetChildrenCount

	@get_children_count.setter
	def get_children_count(self, value):
		"""Gets the number of children for this configuration."""
		self._instance.GetChildrenCount = value

	@property
	def get_component_config_name(self):
		"""Gets the referenced configuration name of the specified component in this configuration."""
		return self._instance.GetComponentConfigName

	@get_component_config_name.setter
	def get_component_config_name(self, value):
		"""Gets the referenced configuration name of the specified component in this configuration."""
		self._instance.GetComponentConfigName = value

	@property
	def get_component_suppression_state(self):
		"""Gets the suppression state of the specified component in this configuration."""
		return self._instance.GetComponentSuppressionState

	@get_component_suppression_state.setter
	def get_component_suppression_state(self, value):
		"""Gets the suppression state of the specified component in this configuration."""
		self._instance.GetComponentSuppressionState = value

	@property
	def get_current_part_explode_view_name(self):
		"""Gets the explode view name in the current configuration."""
		return self._instance.GetCurrentPartExplodeViewName

	@get_current_part_explode_view_name.setter
	def get_current_part_explode_view_name(self, value):
		"""Gets the explode view name in the current configuration."""
		self._instance.GetCurrentPartExplodeViewName = value

	@property
	def get_display_state_body_properties(self):
		"""Gets the bodies and their material properties in the specified display state."""
		return self._instance.GetDisplayStateBodyProperties

	@get_display_state_body_properties.setter
	def get_display_state_body_properties(self, value):
		"""Gets the bodies and their material properties in the specified display state."""
		self._instance.GetDisplayStateBodyProperties = value

	@property
	def get_display_state_component_properties(self):
		"""Gets the components and their material properties in the specified display state."""
		return self._instance.GetDisplayStateComponentProperties

	@get_display_state_component_properties.setter
	def get_display_state_component_properties(self, value):
		"""Gets the components and their material properties in the specified display state."""
		self._instance.GetDisplayStateComponentProperties = value

	@property
	def get_display_state_component_visibility(self):
		"""Gets the components and their visibilities in the specified display state."""
		return self._instance.GetDisplayStateComponentVisibility

	@get_display_state_component_visibility.setter
	def get_display_state_component_visibility(self, value):
		"""Gets the components and their visibilities in the specified display state."""
		self._instance.GetDisplayStateComponentVisibility = value

	@property
	def get_display_state_face_properties(self):
		"""Gets the faces and their material properties in the specified display state."""
		return self._instance.GetDisplayStateFaceProperties

	@get_display_state_face_properties.setter
	def get_display_state_face_properties(self, value):
		"""Gets the faces and their material properties in the specified display state."""
		self._instance.GetDisplayStateFaceProperties = value

	@property
	def get_display_state_feature_properties(self):
		"""Gets the features and their material properties in the specified display state."""
		return self._instance.GetDisplayStateFeatureProperties

	@get_display_state_feature_properties.setter
	def get_display_state_feature_properties(self, value):
		"""Gets the features and their material properties in the specified display state."""
		self._instance.GetDisplayStateFeatureProperties = value

	@property
	def get_display_state_properties(self):
		"""Gets the material properties of the specified display state."""
		return self._instance.GetDisplayStateProperties

	@get_display_state_properties.setter
	def get_display_state_properties(self, value):
		"""Gets the material properties of the specified display state."""
		self._instance.GetDisplayStateProperties = value

	@property
	def get_display_states(self):
		"""Gets the names of the display states for this configuration."""
		return self._instance.GetDisplayStates

	@get_display_states.setter
	def get_display_states(self, value):
		"""Gets the names of the display states for this configuration."""
		self._instance.GetDisplayStates = value

	@property
	def get_display_states_count(self):
		"""Gets the number of display states for this configuration."""
		return self._instance.GetDisplayStatesCount

	@get_display_states_count.setter
	def get_display_states_count(self, value):
		"""Gets the number of display states for this configuration."""
		self._instance.GetDisplayStatesCount = value

	@property
	def get_expanded(self):
		"""Gets whether this configuration's node is expanded in the specified pane of the ConfigurationManager."""
		return self._instance.GetExpanded

	@get_expanded.setter
	def get_expanded(self, value):
		"""Gets whether this configuration's node is expanded in the specified pane of the ConfigurationManager."""
		self._instance.GetExpanded = value

	@property
	def get_explode_step(self):
		"""Gets the specified explode step in this configuration's explode step sequence."""
		return self._instance.GetExplodeStep

	@get_explode_step.setter
	def get_explode_step(self, value):
		"""Gets the specified explode step in this configuration's explode step sequence."""
		self._instance.GetExplodeStep = value

	@property
	def get_i_d(self):
		"""Gets the configuration ID of this configuration."""
		return self._instance.GetID

	@get_i_d.setter
	def get_i_d(self, value):
		"""Gets the configuration ID of this configuration."""
		self._instance.GetID = value

	@property
	def get_number_of_explode_steps(self):
		"""Gets the number of explode steps for this configuration."""
		return self._instance.GetNumberOfExplodeSteps

	@get_number_of_explode_steps.setter
	def get_number_of_explode_steps(self, value):
		"""Gets the number of explode steps for this configuration."""
		self._instance.GetNumberOfExplodeSteps = value

	@property
	def get_number_of_part_explode_steps(self):
		"""Gets the number of explode steps in the explode view of a multibody part."""
		return self._instance.GetNumberOfPartExplodeSteps

	@get_number_of_part_explode_steps.setter
	def get_number_of_part_explode_steps(self, value):
		"""Gets the number of explode steps in the explode view of a multibody part."""
		self._instance.GetNumberOfPartExplodeSteps = value

	@property
	def get_parameter_count(self):
		"""Gets the number of parameters for this configuration."""
		return self._instance.GetParameterCount

	@get_parameter_count.setter
	def get_parameter_count(self, value):
		"""Gets the number of parameters for this configuration."""
		self._instance.GetParameterCount = value

	@property
	def get_parameters(self):
		"""Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration."""
		return self._instance.GetParameters

	@get_parameters.setter
	def get_parameters(self, value):
		"""Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration."""
		self._instance.GetParameters = value

	@property
	def get_parent(self):
		"""Gets the parent configuration of this derived configuration."""
		return self._instance.GetParent

	@get_parent.setter
	def get_parent(self, value):
		"""Gets the parent configuration of this derived configuration."""
		self._instance.GetParent = value

	@property
	def get_part_explode_step(self):
		"""Gets the specified explode step of an explode view of a multibody part."""
		return self._instance.GetPartExplodeStep

	@get_part_explode_step.setter
	def get_part_explode_step(self, value):
		"""Gets the specified explode step of an explode view of a multibody part."""
		self._instance.GetPartExplodeStep = value

	@property
	def get_representation_parent(self):
		"""Gets the Physical Product represented by this configuration."""
		return self._instance.GetRepresentationParent

	@get_representation_parent.setter
	def get_representation_parent(self, value):
		"""Gets the Physical Product represented by this configuration."""
		self._instance.GetRepresentationParent = value

	@property
	def get_root_component(self):
		"""Gets the root component for this assembly configuration."""
		return self._instance.GetRootComponent3

	@get_root_component.setter
	def get_root_component(self, value):
		"""Gets the root component for this assembly configuration."""
		self._instance.GetRootComponent3 = value

	@property
	def get_scene(self):
		"""Gets the ISwScene object for this configuration."""
		return self._instance.GetScene

	@get_scene.setter
	def get_scene(self, value):
		"""Gets the ISwScene object for this configuration."""
		self._instance.GetScene = value

	@property
	def get_stream_name(self):
		"""Gets the name of the stream for the current configuration."""
		return self._instance.GetStreamName

	@get_stream_name.setter
	def get_stream_name(self, value):
		"""Gets the name of the stream for the current configuration."""
		self._instance.GetStreamName = value

	@property
	def i_add_explode_step(self):
		"""Adds a new explode step to the configuration."""
		return self._instance.IAddExplodeStep

	@i_add_explode_step.setter
	def i_add_explode_step(self, value):
		"""Adds a new explode step to the configuration."""
		self._instance.IAddExplodeStep = value

	@property
	def i_get_children(self):
		"""Gets all of the children configurations of this derived configuration."""
		return self._instance.IGetChildren

	@i_get_children.setter
	def i_get_children(self, value):
		"""Gets all of the children configurations of this derived configuration."""
		self._instance.IGetChildren = value

	@property
	def i_get_display_states(self):
		"""Gets the names of the display states for this configuration."""
		return self._instance.IGetDisplayStates

	@i_get_display_states.setter
	def i_get_display_states(self, value):
		"""Gets the names of the display states for this configuration."""
		self._instance.IGetDisplayStates = value

	@property
	def i_get_explode_step(self):
		"""Gets a pointer to the specified explode step in the configuration explode step sequence."""
		return self._instance.IGetExplodeStep

	@i_get_explode_step.setter
	def i_get_explode_step(self, value):
		"""Gets a pointer to the specified explode step in the configuration explode step sequence."""
		self._instance.IGetExplodeStep = value

	@property
	def i_get_parameters(self):
		"""Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration."""
		return self._instance.IGetParameters

	@i_get_parameters.setter
	def i_get_parameters(self, value):
		"""Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration."""
		self._instance.IGetParameters = value

	@property
	def is_derived(self):
		"""Gets whether this configuration is a derived configuration."""
		return self._instance.IsDerived

	@is_derived.setter
	def is_derived(self, value):
		"""Gets whether this configuration is a derived configuration."""
		self._instance.IsDerived = value

	@property
	def is_dirty(self):
		"""Gets whether this configuration is dirty (i.e., needs to be updated)."""
		return self._instance.IsDirty

	@is_dirty.setter
	def is_dirty(self, value):
		"""Gets whether this configuration is dirty (i.e., needs to be updated)."""
		self._instance.IsDirty = value

	@property
	def i_set_parameters(self):
		"""Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration."""
		return self._instance.ISetParameters

	@i_set_parameters.setter
	def i_set_parameters(self, value):
		"""Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration."""
		self._instance.ISetParameters = value

	@property
	def is_loaded(self):
		"""Gets whether a configuration is loaded."""
		return self._instance.IsLoaded

	@is_loaded.setter
	def is_loaded(self, value):
		"""Gets whether a configuration is loaded."""
		self._instance.IsLoaded = value

	@property
	def is_speed_pak(self):
		"""Gets whether the configuration is a SpeedPak."""
		return self._instance.IsSpeedPak

	@is_speed_pak.setter
	def is_speed_pak(self, value):
		"""Gets whether the configuration is a SpeedPak."""
		self._instance.IsSpeedPak = value

	@property
	def rename_display_state(self):
		"""Renames a display state of this configuration."""
		return self._instance.RenameDisplayState

	@rename_display_state.setter
	def rename_display_state(self, value):
		"""Renames a display state of this configuration."""
		self._instance.RenameDisplayState = value

	@property
	def select(self):
		"""Selects the configuration."""
		return self._instance.Select2

	@select.setter
	def select(self, value):
		"""Selects the configuration."""
		self._instance.Select2 = value

	@property
	def set_color(self):
		"""Sets the color for this configuration."""
		return self._instance.SetColor

	@set_color.setter
	def set_color(self, value):
		"""Sets the color for this configuration."""
		self._instance.SetColor = value

	@property
	def set_expanded(self):
		"""Sets whether to expand this configuration's node in the specified pane of the ConfigurationManager."""
		return self._instance.SetExpanded

	@set_expanded.setter
	def set_expanded(self, value):
		"""Sets whether to expand this configuration's node in the specified pane of the ConfigurationManager."""
		self._instance.SetExpanded = value

	@property
	def set_parameters(self):
		"""Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration."""
		return self._instance.SetParameters

	@set_parameters.setter
	def set_parameters(self, value):
		"""Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration."""
		self._instance.SetParameters = value

	@property
	def update_speed_pak(self):
		"""Updates the SpeedPak configuration for this configuration."""
		return self._instance.UpdateSpeedPak

	@update_speed_pak.setter
	def update_speed_pak(self, value):
		"""Updates the SpeedPak configuration for this configuration."""
		self._instance.UpdateSpeedPak = value

