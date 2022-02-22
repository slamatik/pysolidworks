# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html
class IConfiguration:
    def __init__(self, parent=None):
        self._instance = parent

    def add_rebuild_save_mark(self):
        """Adds or removes the mark indicating whether the configuration needs to be rebuilt and its configuration data
        saved every time you save the model document."""
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

    def b_o_m_part_no_source(self):
        """Gets the source of the part number used in the BOM table."""
        # return self._instance.BOMPartNoSource
        raise NotImplemented

    @property
    def child_component_display_in_b_o_m(self):
        """Gets or sets the child component display option of a configuration in a Bill of Materials (BOM) for an
        assembly document."""
        return self._instance.ChildComponentDisplayInBOM

    @child_component_display_in_b_o_m.setter
    def child_component_display_in_b_o_m(self, value):
        """Gets or sets the child component display option of a configuration in a Bill of Materials (BOM) for an
        assembly document."""
        self._instance.ChildComponentDisplayInBOM = value

    @property
    def comment(self):
        """Gets or sets the configuration comment."""
        return self._instance.Comment

    @comment.setter
    def comment(self, value):
        """Gets or sets the configuration comment."""
        self._instance.Comment = value

    def custom_property_manager(self):
        """Gets the custom property information for this configuration."""
        # return self._instance.CustomPropertyManager
        raise NotImplemented

    @property
    def description(self):
        """Gets or sets the description of the configuration."""
        return self._instance.Description

    @description.setter
    def description(self, value):
        """Gets or sets the description of the configuration."""
        self._instance.Description = value

    def dim_xpert_manager(self, create_schema):
        """
        Gets the DimXpert schema for this configuration.
        :param create_schema: True to create DimXpert schema if it does not already exist; false otherwise
        """
        # return self._instance.DimXpertManager(create_schema)
        raise NotImplemented

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

    def needs_rebuild(self):
        """Gets whether the configuration needs to be rebuilt."""
        # return self._instance.NeedsRebuild
        raise NotImplemented

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

    def type(self):
        """Gets the type of configuration."""
        # return self._instance.Type
        raise NotImplemented

    @property
    def use_alternate_name_in_b_o_m(self):
        """Gets or sets whether the alternate name (i.e., user-specified name) is displayed in the bill of materials for
        this configuration."""
        return self._instance.UseAlternateNameInBOM

    @use_alternate_name_in_b_o_m.setter
    def use_alternate_name_in_b_o_m(self, value):
        """Gets or sets whether the alternate name (i.e., user-specified name) is displayed in the bill of materials for
        this configuration."""
        self._instance.UseAlternateNameInBOM = value

    @property
    def use_description_in_b_o_m(self):
        """Gets or sets whether the description of the configuration is displayed in the bill of materials."""
        return self._instance.UseDescriptionInBOM

    @use_description_in_b_o_m.setter
    def use_description_in_b_o_m(self, value):
        """Gets or sets whether the description of the configuration is displayed in the bill of materials."""
        self._instance.UseDescriptionInBOM = value

    def add_explode_step(self, expl_dist, expl_dir_index, reverse_dir, expl_ang, rot_axis_index, reverse_ang,
                         rotate_about_origin, auto_space_components_on_drag, error):
        """
        Adds a regular (translate and rotate) explode step to the explode view of the active configuration.
        :param expl_dist: Distance in meters to move the components in this explode step
        :param expl_dir_index: Explode direction manipulator index as defined in swExplodeDirectionIndex_e (see Remarks)
        :param reverse_dir: True to reverse the explode direction, false to not
        :param expl_ang: Angle in radians of component rotation (see Remarks)
        :param rot_axis_index: Rotation manipulator index as defined in swRotationAxisIndex_e (see Remarks)
        :param reverse_ang: True to reverse the direction of ExplAng, false to not
        :param rotate_about_origin: True if each component rotates about its origin, false if not (see Remarks)
        :param auto_space_components_on_drag: True to automatically space components on drag, false to not (see Remarks)
        :param error: Error code as defined in swCreateExplodeStepError_e
        """
        # return self._instance.AddExplodeStep2(expl_dist, expl_dir_index, reverse_dir, expl_ang, rot_axis_index, reverse_ang, rotate_about_origin, auto_space_components_on_drag, error)
        raise NotImplemented

    def add_part_explode_step(self, explode_view, expl_dist, expl_dir_index, reverse_dir, auto_space_bodies_on_drag,
                              error):
        """
        Adds an explode step to the specified explode view of a multibody part.
        :param explode_view: Name of the explode view to which to add this explode step
        :param expl_dist: Distance in meters to move the selected bodies in this explode step
        :param expl_dir_index: Explode direction manipulator index as defined in swExplodeDirectionIndex_e (see Remarks)
        :param reverse_dir: True to reverse the explode direction, false to not
        :param auto_space_bodies_on_drag: True to automatically space selected bodies on drag, false to not
        :param error: Error code as defined in swCreatePartExplodeStepError_e
        """
        # return self._instance.AddPartExplodeStep(explode_view, expl_dist, expl_dir_index, reverse_dir, auto_space_bodies_on_drag, error)
        raise NotImplemented

    def add_radial_explode_step(self, expl_dist, expl_ang, diverge_from_axis, error):
        """
        Adds a radial explode step to the explode view of the active configuration.
        :param expl_dist: Distance in meters to move the components in this explode step
        :param expl_ang: Angle in radians of rotation about component origins
        :param diverge_from_axis: True to move components at an angle from the selected explode direction, false to not (see Remarks)
        :param error: Error code as defined in swCreateExplodeStepError_e
        """
        # return self._instance.AddRadialExplodeStep(expl_dist, expl_ang, diverge_from_axis, error)
        raise NotImplemented

    def apply_display_state(self, display_state_name):
        """
        Applies the specified display state to this configuration.
        :param display_state_name: Name of the display state to apply to this configuration
        """
        # return self._instance.ApplyDisplayState(display_state_name)
        raise NotImplemented

    def copy_display_state_from_configuration(self, copy_from_config, display_state_name_to_copy):
        """
        Copies the specified display state from the specified configuration to this configuration.
        :param copy_from_config: Pointer to the configuration from which to copy the display state
        :param display_state_name_to_copy: Name of the display state to copy
        """
        # return self._instance.CopyDisplayStateFromConfiguration(copy_from_config, display_state_name_to_copy)
        raise NotImplemented

    def create_display_state(self, display_state_name):
        """
        Creates a display state for this configuration.
        :param display_state_name: Name of display state to create for this configuration
        """
        # return self._instance.CreateDisplayState(display_state_name)
        raise NotImplemented

    def delete_display_state(self, display_state_name):
        """
        Deletes the specified display state from this configuration.
        :param display_state_name: Name of display state to delete from this configuration
        """
        # return self._instance.DeleteDisplayState(display_state_name)
        raise NotImplemented

    def delete_explode_step(self, explode_step_name):
        """
        Deletes the specified explode step.
        :param explode_step_name: Name of the explode step to delete
        """
        # return self._instance.DeleteExplodeStep(explode_step_name)
        raise NotImplemented

    def get_d_experience_type(self):
        """Gets how this configuration is viewed in SOLIDWORKS Connected."""
        # return self._instance.Get3DExperienceType
        raise NotImplemented

    def get_children(self):
        """Gets all the children configurations of this derived configuration."""
        # return self._instance.GetChildren
        raise NotImplemented

    def get_children_count(self):
        """Gets the number of children for this configuration."""
        # return self._instance.GetChildrenCount
        raise NotImplemented

    def get_component_config_name(self, comp_name):
        """
        Gets the referenced configuration name of the specified component in this configuration.
        :param comp_name: Component name
        """
        # return self._instance.GetComponentConfigName(comp_name)
        raise NotImplemented

    def get_component_suppression_state(self, comp_name):
        """
        Gets the suppression state of the specified component in this configuration.
        :param comp_name: Component name
        """
        # return self._instance.GetComponentSuppressionState(comp_name)
        raise NotImplemented

    def get_current_part_explode_view_name(self):
        """Gets the explode view name in the current configuration."""
        # return self._instance.GetCurrentPartExplodeViewName
        raise NotImplemented

    def get_display_state_body_properties(self, display_state_name, bodies):
        """
        Gets the bodies and their material properties in the specified display state.
        :param display_state_name: Name of the display state
        :param bodies: Array of IBody2 objects
        """
        # return self._instance.GetDisplayStateBodyProperties(display_state_name, bodies)
        raise NotImplemented

    def get_display_state_component_properties(self, display_state_name, components):
        """
        Gets the components and their material properties in the specified display state.
        :param display_state_name: Name of the display state
        :param components: Array of IComponent2s
        """
        # return self._instance.GetDisplayStateComponentProperties(display_state_name, components)
        raise NotImplemented

    def get_display_state_component_visibility(self, display_state_name, onlyhidden, toplevel_only, components):
        """
        Gets the components and their visibilities in the specified display state.
        :param display_state_name: Name of the display state
        :param onlyhidden: True to only return visibilities for hidden components, false to return visibilities for all components
        :param toplevel_only: True to get the top-level components only, false to get all components
        :param components: Array of IComponent2s
        """
        # return self._instance.GetDisplayStateComponentVisibility(display_state_name, onlyhidden, toplevel_only, components)
        raise NotImplemented

    def get_display_state_face_properties(self, display_state_name, faces):
        """
        Gets the faces and their material properties in the specified display state.
        :param display_state_name: Name of the display state
        :param faces: Array if IFace2 objects
        """
        # return self._instance.GetDisplayStateFaceProperties(display_state_name, faces)
        raise NotImplemented

    def get_display_state_feature_properties(self, display_state_name, features):
        """
        Gets the features and their material properties in the specified display state.
        :param display_state_name: Name of the display state
        :param features: Array of IFeature objects
        """
        # return self._instance.GetDisplayStateFeatureProperties(display_state_name, features)
        raise NotImplemented

    def get_display_state_properties(self, display_state_name):
        """
        Gets the material properties of the specified display state.
        :param display_state_name: Name of the display state
        """
        # return self._instance.GetDisplayStateProperties(display_state_name)
        raise NotImplemented

    def get_display_states(self):
        """Gets the names of the display states for this configuration."""
        # return self._instance.GetDisplayStates
        raise NotImplemented

    def get_display_states_count(self):
        """Gets the number of display states for this configuration."""
        # return self._instance.GetDisplayStatesCount
        raise NotImplemented

    def get_expanded(self, which_pane):
        """
        Gets whether this configuration's node is expanded in the specified pane of the ConfigurationManager.
        :param which_pane: Valid options in swFeatMgrPane_e:
            swFeatMgrPaneTop
            swFeatMgrPaneBottom
        """
        # return self._instance.GetExpanded(which_pane)
        raise NotImplemented

    def get_explode_step(self, explode_step_index):
        """
        Gets the specified explode step in this configuration's explode step sequence.
        :param explode_step_index: Index of the explode step in the explode step sequence
        """
        # return self._instance.GetExplodeStep(explode_step_index)
        raise NotImplemented

    def get_i_d(self):
        """Gets the configuration ID of this configuration."""
        # return self._instance.GetID
        raise NotImplemented

    def get_number_of_explode_steps(self):
        """Gets the number of explode steps for this configuration."""
        # return self._instance.GetNumberOfExplodeSteps
        raise NotImplemented

    def get_number_of_part_explode_steps(self):
        """Gets the number of explode steps in the explode view of a multibody part."""
        # return self._instance.GetNumberOfPartExplodeSteps
        raise NotImplemented

    def get_parameter_count(self):
        """Gets the number of parameters for this configuration."""
        # return self._instance.GetParameterCount
        raise NotImplemented

    def get_parameters(self, params, values):
        """
        Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions,
        and so on) for this configuration.
        :param params: Array of the names of the parameters
        :param values: Array of the values of the parameters
        """
        # return self._instance.GetParameters(params, values)
        raise NotImplemented

    def get_parent(self):
        """Gets the parent configuration of this derived configuration."""
        # return self._instance.GetParent
        raise NotImplemented

    def get_part_explode_step(self, index):
        """
        Gets the specified explode step of an explode view of a multibody part.
        :param index: Index of the explode step (see Remarks)
        """
        # return self._instance.GetPartExplodeStep(index)
        raise NotImplemented

    def get_representation_parent(self):
        """Gets the Physical Product represented by this configuration."""
        # return self._instance.GetRepresentationParent
        raise NotImplemented

    def get_root_component(self, resolve):
        """
        Gets the root component for this assembly configuration.
        :param resolve: True to load additional components required by this configuration, false to not
        """
        # return self._instance.GetRootComponent3(resolve)
        raise NotImplemented

    def get_scene(self):
        """Gets the ISwScene object for this configuration."""
        # return self._instance.GetScene
        raise NotImplemented

    def get_stream_name(self):
        """Gets the name of the stream for the current configuration."""
        # return self._instance.GetStreamName
        raise NotImplemented

    def i_add_explode_step(self, expl_dist, reverse_dir, rigid_subassembly, explode_related):
        """
        Adds a new explode step to the configuration.
        :param expl_dist: Explode distance
        :param reverse_dir: True to reverse the direction of the explode step, false to not
        :param rigid_subassembly: True to explode entire sub assembly, false to explode just the selected component
        :param explode_related: True to explode related components together, false to not
        """
        # return self._instance.IAddExplodeStep(expl_dist, reverse_dir, rigid_subassembly, explode_related)
        raise NotImplemented

    def i_get_children(self, num_children):
        """
        Gets all of the children configurations of this derived configuration.
        :param num_children: Number of children configurations of this configuration
        """
        # return self._instance.IGetChildren(num_children)
        raise NotImplemented

    def i_get_display_states(self, count):
        """
        Gets the names of the display states for this configuration.
        :param count: Number of displays states for this configuration
        """
        # return self._instance.IGetDisplayStates(count)
        raise NotImplemented

    def i_get_explode_step(self, explode_step_index):
        """
        Gets a pointer to the specified explode step in the configuration explode step sequence.
        :param explode_step_index: Index number of the explode step in the explode step sequence
        """
        # return self._instance.IGetExplodeStep(explode_step_index)
        raise NotImplemented

    def i_get_parameters(self, n_param_count, params, values):
        """
        Gets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration.
        :param n_param_count: Number of parameters
        :param params: in-process, unmanaged C++: Pointer to an array of the names of the parameters of size NParamCount
        VBA, VB.NET, C#, and C++/CLI: Not supported
        See In-process Methods for details about this type of method.
        :param values: in-process, unmanaged C++: Pointer to an array of the values of the parameters of size NParamCount
        VBA, VB.NET, C#, and C++/CLI: Not supported
        See In-process Methods for details about this type of method.
        """
        # return self._instance.IGetParameters(n_param_count, params, values)
        raise NotImplemented

    def is_derived(self):
        """Gets whether this configuration is a derived configuration."""
        # return self._instance.IsDerived
        raise NotImplemented

    def is_dirty(self):
        """Gets whether this configuration is dirty (i.e., needs to be updated)."""
        # return self._instance.IsDirty
        raise NotImplemented

    def i_set_parameters(self, n_param_count, params, values):
        """
        Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions, and so on) for this configuration.
        :param n_param_count: Number of parameters
        :param params: in-process, unmanaged C++: Pointer to an array of the names of the parameters of size NParamCount
        VBA, VB.NET, C#, and C++/CLI: Not supported
        See In-process Methods for details about this type of method.
        :param values: in-process, unmanaged C++: Pointe to an array of the values for the parameters of size NParamCount
        VBA, VB.NET, C#, and C++/CLI: Not supported
        See In-process Methods for details about this type of method.
        """
        # return self._instance.ISetParameters(n_param_count, params, values)
        raise NotImplemented

    def is_loaded(self):
        """Gets whether a configuration is loaded."""
        # return self._instance.IsLoaded
        raise NotImplemented

    def is_speed_pak(self):
        """Gets whether the configuration is a SpeedPak."""
        # return self._instance.IsSpeedPak
        raise NotImplemented

    def rename_display_state(self, old_display_state_name, new_display_state_name):
        """
        Renames a display state of this configuration.
        :param old_display_state_name: Existing name of the display state
        :param new_display_state_name: New name for the display state
        """
        # return self._instance.RenameDisplayState(old_display_state_name, new_display_state_name)
        raise NotImplemented

    def select(self, append_flag, select_data):
        """
        Selects the configuration.
        :param append_flag: True appends the configuration to the selection list, false replaces the selectionlist with the configuration
        :param select_data: Pointer to the ISelectData object
        """
        # return self._instance.Select2(append_flag, select_data)
        raise NotImplemented

    def set_color(self, color_in):
        """
        Sets the color for this configuration.
        :param color_in: COLORREF value of the color
        """
        # return self._instance.SetColor(color_in)
        raise NotImplemented

    def set_expanded(self, which_pane, expanded):
        """
        Sets whether to expand this configuration's node in the specified pane of the ConfigurationManager.
        :param which_pane: Display pane as defined in swFeatMgrPane_e:
        swFeatMgrPaneTop
        swFeatMgrPaneBottom
        :param expanded: True to expand the node, false to collapse it
        """
        # return self._instance.SetExpanded(which_pane, expanded)
        raise NotImplemented

    def set_parameters(self, params, values):
        """
        Sets the parameters (suppression state of features, suppression state or visibility of components, dimensions,
        and so on) for this configuration.
        :param params: Array of the names of the parameters
        :param values: Array of the values for the parameters
        """
        # return self._instance.SetParameters(params, values)
        raise NotImplemented

    def update_speed_pak(self):
        """Updates the SpeedPak configuration for this configuration."""
        # return self._instance.UpdateSpeedPak
        raise NotImplemented
