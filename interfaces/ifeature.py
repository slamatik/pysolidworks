from enums import VisibilityState


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html

class IFeature:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def created_by(self):
        """Gets the name of the user who created the feature."""
        return self._instance.CreatedBy

    @property
    def custom_property_manager(self):
        """Gets the custom property information for weldment and cut-list item features only."""
        return self._instance.CustomPropertyManager

    @property
    def date_created(self):
        """Gets the date on which the feature was created."""
        return self._instance.DateCreated

    @property
    def date_modified(self):
        """Gets the date on which the feature was last modified."""
        return self._instance.DateModified

    @property
    def description(self):
        """Gets or sets the description for this feature."""
        return self._instance.Description

    @description.setter
    def description(self, value):
        """Gets or sets the description for this feature."""
        self._instance.Description = value

    @property
    def exclude_from_cut_list(self):
        """Gets or sets whether to exclude this feature from the cut list."""
        return self._instance.ExcludeFromCutList

    @exclude_from_cut_list.setter
    def exclude_from_cut_list(self, value):
        """Gets or sets whether to exclude this feature from the cut list."""
        self._instance.ExcludeFromCutList = value

    @property
    def is_d_interconnect_feature(self):
        """Gets whether this is a 3D Interconnect feature."""
        # return self._instance.Is3DInterconnectFeature
        raise NotImplemented

    @property
    def is_d_interconnect_update_available(self):
        """Gets whether an update is available for this 3D Interconnect part or assembly."""
        # return self._instance.Is3DInterconnectUpdateAvailable
        raise NotImplemented

    @property
    def name(self):
        """Gets or sets the name of the current feature."""
        return self._instance.Name

    @name.setter
    def name(self, value):
        """Gets or sets the name of the current feature."""
        self._instance.Name = value

    @property
    def visible(self):
        """Gets the visibility state of this feature."""
        return VisibilityState(self._instance.Visible)

    def add_comment(self, text):
        """
        Adds a comment to this feature.
        :param text: Comment to add to this feature
        """
        # return self._instance.AddComment(text)
        raise NotImplemented

    def add_property_extension(self, property_extension):
        """
        Adds a property extension to this feature.
        :param property_extension: Value of the property extension to add to this feature
        """
        # return self._instance.AddPropertyExtension(property_extension)
        raise NotImplemented

    def break_link(self, all_components, silent):
        """
        Breaks the link to third-party native CAD parts and assemblies.
        :param all_components: True to break the link for all subcomponents within a top-level subassembly, false to not (see Remarks)
        :param silent: True to suppress dialog windows, false to not
        """
        # return self._instance.BreakLink(all_components, silent)
        raise NotImplemented

    def de_select(self):
        """Deselects this feature."""
        # return self._instance.DeSelect
        raise NotImplemented

    def enum_display_dimensions(self):
        """This method returns a display dimensions enumeration for this feature."""
        # return self._instance.EnumDisplayDimensions
        raise NotImplemented

    def get_affected_face_count(self):
        """Gets the number of faces modified by a feature, such as a draft feature."""
        # return self._instance.GetAffectedFaceCount
        raise NotImplemented

    def get_affected_faces(self):
        """Gets the faces modified by a feature, such as a draft feature."""
        # return self._instance.GetAffectedFaces
        raise NotImplemented

    def get_box(self, b_box):
        """
        Gets the bounding box for this feature.
        :param b_box: Array containing the two diagonal points
        """
        # return self._instance.GetBox(b_box)
        raise NotImplemented

    def get_children(self):
        """Gets the child features belonging to this feature."""
        # return self._instance.GetChildren
        raise NotImplemented

    def get_created_version(self):
        """Gets the SOLIDWORKS version number in which the selected feature was created."""
        # return self._instance.GetCreatedVersion
        raise NotImplemented

    def get_definition(self):
        """Gets the feature data object for a feature, such as an advanced mate, extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature."""
        # return self._instance.GetDefinition
        raise NotImplemented

    def get_display_dimension(self, index):
        """
        Gets the display dimension object for the specified pattern property.
        :param index: Pattern property as defined by swFeatureDimensionParameter_e
        """
        # return self._instance.GetDisplayDimension(index)
        raise NotImplemented

    def get_edit_status(self):
        """Gets whether the feature can currently be edited."""
        # return self._instance.GetEditStatus
        raise NotImplemented

    def get_error_code(self, is_warning):
        """
        Gets the error code for this feature.
        :param is_warning: True if the error is a warning, false if not
NOTE: This parameter should only be examined if the return value is non-zero.
        """
        # return self._instance.GetErrorCode2(is_warning)
        raise NotImplemented

    def get_face_count(self):
        """Gets the number of faces in this feature."""
        # return self._instance.GetFaceCount
        raise NotImplemented

    def get_faces(self):
        """Gets the faces in this feature."""
        # return self._instance.GetFaces
        raise NotImplemented

    def get_first_display_dimension(self):
        """Provides access to the dimensions that belong to this feature by returning the first display dimension associated with this feature."""
        # return self._instance.GetFirstDisplayDimension
        raise NotImplemented

    def get_first_sub_feature(self):
        """Gets the first sub-feature that belongs to this feature."""
        # return self._instance.GetFirstSubFeature
        raise NotImplemented

    def get_i_d(self):
        """Gets the feature ID of this feature."""
        # return self._instance.GetID
        raise NotImplemented

    def get_imported_feature_parameters(self, data_obj):
        """
        Gets the data object for this 3D Interconnect part or assembly.
        :param data_obj: IImport3DInterconnectData
        """
        # return self._instance.GetImportedFeatureParameters(data_obj)
        raise NotImplemented

    def get_imported_file_name(self):
        """Gets the file name from an imported feature."""
        # return self._instance.GetImportedFileName
        raise NotImplemented

    def get_material_id_name(self):
        """Gets the material name."""
        # return self._instance.GetMaterialIdName
        raise NotImplemented

    def get_material_property_values(self, config_opt, config_names):
        """
        Gets the material property values for this feature in the specified configurations.
        :param config_opt: Configuration options as defined by swInConfigurationOpts_e
        :param config_names: Array of configuration names for this component (see Remarks)
        """
        # return self._instance.GetMaterialPropertyValues2(config_opt, config_names)
        raise NotImplemented

    def get_material_user_name(self):
        """Gets the material name for this feature, which is visible to the user."""
        # return self._instance.GetMaterialUserName
        raise NotImplemented

    def get_modified_version(self):
        """Gets the SOLIDWORKS version number in which this feature was last modified."""
        # return self._instance.GetModifiedVersion
        raise NotImplemented

    def get_name_for_selection(self, type):
        """
        Gets the selected feature's type and name.
        :param type: Type of feature as defined in swSelectType_e
        """
        # return self._instance.GetNameForSelection(type)
        raise NotImplemented

    def get_next_display_dimension(self, disp_in):
        """
        Gets the next display dimension associated with this feature.
        :param disp_in: IDisplayDimension object obtained with IFeature::GetFirstDisplayDimension or from your previous call to this method
        """
        # return self._instance.GetNextDisplayDimension(disp_in)
        raise NotImplemented

    def get_next_feature(self):
        """Gets the next feature in the part."""
        # return self._instance.GetNextFeature
        raise NotImplemented

    def get_next_sub_feature(self):
        """Gets the next sub-feature from the owner of this sub-feature."""
        # return self._instance.GetNextSubFeature
        raise NotImplemented

    def get_owner_feature(self):
        """Gets the feature that owns this feature."""
        # return self._instance.GetOwnerFeature
        raise NotImplemented

    def get_parents(self):
        """Gets the parent features for this feature."""
        # return self._instance.GetParents
        raise NotImplemented

    def get_property_extension(self, i_d):
        """
        Gets the property extension on this feature.
        :param i_d: 0
        """
        # return self._instance.GetPropertyExtension(i_d)
        raise NotImplemented

    def get_specific_feature(self):
        """Gets the more specific interface to a selected feature."""
        # return self._instance.GetSpecificFeature2
        raise NotImplemented

    def get_texture(self, config_name):
        """
        Gets the texture applied to this feature in the specified configuration.
        :param config_name: Name of the configuration
        """
        # return self._instance.GetTexture(config_name)
        raise NotImplemented

    def get_type_name(self):
        """Gets the type of feature.
NOTE: To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call this method; otherwise, call IFeature::GetTypeName2."""
        # return self._instance.GetTypeName
        raise NotImplemented

    def get_type_name(self):
        """Gets the type of feature.
NOTE: To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call IFeature::GetTypeName; otherwise, call this method."""
        # return self._instance.GetTypeName2
        raise NotImplemented

    def get_u_i_state(self, state_type):
        """
        Gets the user-interface state of the current feature.
        :param state_type: User interface state type as defined in swUIStates_e
        """
        # return self._instance.GetUIState(state_type)
        raise NotImplemented

    def get_update_stamp(self):
        """Gets the current update stamp for this feature."""
        # return self._instance.GetUpdateStamp
        raise NotImplemented

    def has_frozen_update_pending(self):
        """Gets whether this feature has pending freeze updates."""
        # return self._instance.HasFrozenUpdatePending
        raise NotImplemented

    def has_material_property_values(self):
        """Gets whether this feature has an appearance."""
        # return self._instance.HasMaterialPropertyValues
        raise NotImplemented

    def i_get_affected_faces(self, n_count):
        """
        Gets the faces modified by a feature, such as a draft feature.
        :param n_count: Number of faces modified by a feature
        """
        # return self._instance.IGetAffectedFaces(n_count)
        raise NotImplemented

    def i_get_box(self, b_box):
        """
        Gets the bounding box for this feature.
        :param b_box: Array containing the two diagonal points
        """
        # return self._instance.IGetBox(b_box)
        raise NotImplemented

    def i_get_child_count(self):
        """Gets the number of child features that belong to this feature."""
        # return self._instance.IGetChildCount
        raise NotImplemented

    def i_get_children(self):
        """Gets the child features belonging to this feature."""
        # return self._instance.IGetChildren
        raise NotImplemented

    def i_get_definition(self):
        """Gets the feature data object for a feature, such as an extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature."""
        # return self._instance.IGetDefinition
        raise NotImplemented

    def i_get_faces(self, face_count):
        """
        Gets the faces in this feature.
        :param face_count: Number of faces in this feature
        """
        # return self._instance.IGetFaces2(face_count)
        raise NotImplemented

    def i_get_first_sub_feature(self):
        """Gets the first sub-feature that belongs to this feature."""
        # return self._instance.IGetFirstSubFeature
        raise NotImplemented

    def i_get_material_property_values(self, config_opt, config_count, config_names):
        """
        Gets the material property values for this feature in the specified configurations.
        :param config_opt: Configuration options as defined by swInConfigurationOpts_e
        :param config_count: Number of configurations
        :param config_names: Array of configuration names of size Config_count
        """
        # return self._instance.IGetMaterialPropertyValues2(config_opt, config_count, config_names)
        raise NotImplemented

    def i_get_next_feature(self):
        """Gets the next feature."""
        # return self._instance.IGetNextFeature
        raise NotImplemented

    def i_get_next_sub_feature(self):
        """Gets the next sub-feature from the owner of this sub-feature."""
        # return self._instance.IGetNextSubFeature
        raise NotImplemented

    def i_get_parent_count(self):
        """Gets the number of parent features for this feature."""
        # return self._instance.IGetParentCount
        raise NotImplemented

    def i_get_parents(self):
        """Gets the parent features for this feature."""
        # return self._instance.IGetParents
        raise NotImplemented

    def i_is_suppressed(self, config_opt, config_count, config_names):
        """
        Gets whether the feature in the specified configurations is suppressed.
        :param config_opt: Configuration option as defined by swInConfigurationOpts_e
        :param config_count: Number of configurations in this feature
        :param config_names: Array of configuration names
        """
        # return self._instance.IIsSuppressed2(config_opt, config_count, config_names)
        raise NotImplemented

    def i_list_external_file_references(self, num_refs, model_path_name, comp_path_name, feature, data_type, status,
                                        ref_entity, feat_comp, config_option, config_name):
        """
        Gets the names and statuses of the external references for this feature in a part or assembly.
        :param num_refs: Number of external references
        :param model_path_name:
in-process, unmanaged C++: Pointer to an array of path names of documents of size NumRefs

VBA, VB.NET, C#, and C++/CLI: Not supported
        :param comp_path_name:
in-process, unmanaged C++: Pointer to an array of path names of referenced components of size NumRefs

VBA, VB.NET, C#, and C++/CLI: Not supported
        :param feature:
in-process, unmanaged C++: Pointer to an array of in-context items (sketches, features, and so on) of size NumRefs
VBA, VB.NET, C#, and C++/CLI: Not supported
        :param data_type:
in-process, unmanaged C+: Pointer to an array of data used to create the items (converted edge or face, converted or offset sketch entity, body, and so on) of size NumRefs
VBA, VB.NET, C#, and C++/CLI: Not supported
        :param status:
in-process, unmanaged C++: Pointer of an array of the statuses of external references as defined in swExternalReferenceStatus_e
VBA, VB.NET, C#, and C++/CLI: Not supported
        :param ref_entity:
in-process, unmanaged C++: Pointer to an array of actual items being used and the names of the documents that contain the items of size NumRefs
VBA, VB.NET, C#, and C++/CLI: Not supported
        :param feat_comp:
in-process, unmanaged C++: Pointer to an array of the names of the components in which the affected features exist of size NumRefs; this information is only displayed when one or more RefEntity is in a different component in an assembly and does not apply to derived parts
VBA, VB.NET, C#, and C++/CLI: Not supported
        :param config_option: Configuration option as defined by swExternalFileReferencesConfig_e
        :param config_name: Name of the configuration when ConfigOption is swExternalFileReferencesNamedConfig
        """
        # return self._instance.IListExternalFileReferences2(num_refs, model_path_name, comp_path_name, feature, data_type, status, ref_entity, feat_comp, config_option, config_name)
        raise NotImplemented

    def i_modify_definition(self, data, top_doc, component):
        """
        Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::IGetDefinition.
        :param data: IUnknown interface to the feature data object; use QueryInterface to get the interface to the actual object
        :param top_doc: Top-level document (see Remarks)
        :param component: Component for the feature (see Remarks)
        """
        # return self._instance.IModifyDefinition2(data, top_doc, component)
        raise NotImplemented

    def i_parameter(self, name):
        """
        Gets a pointer to the object for the specified parameter or a pointer to the specified parameter.
        :param name: Name of parameter (for example, "D1")
        """
        # return self._instance.IParameter(name)
        raise NotImplemented

    def i_remove_material_property(self, config_opt, config_count, config_names):
        """
        Removes material property values from this feature.
        :param config_opt: Configuration option as defined in swInConfigurationOpts_e
        :param config_count: Number of configurations
        :param config_names:
in-process, unmanaged C++: Pointer to an array of configuration names
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
        """
        # return self._instance.IRemoveMaterialProperty2(config_opt, config_count, config_names)
        raise NotImplemented

    def is_base(self):
        """Gets whether this feature is a base feature."""
        # return self._instance.IsBase2
        raise NotImplemented

    def is_dim_xpert_annotation(self):
        """Gets whether this feature is a DimXpert annotation."""
        # return self._instance.IsDimXpertAnnotation
        raise NotImplemented

    def is_dim_xpert_feature(self):
        """Gets whether this feature is a DimXpert feature."""
        # return self._instance.IsDimXpertFeature
        raise NotImplemented

    def i_set_body(self, body_in, apply_user_ids):
        """
        Replaces the body of the base feature.
        :param body_in: Pointer to the temporary body that replaces the base feature body
        :param apply_user_ids: True applies user-defined face IDs, false does not
        """
        # return self._instance.ISetBody3(body_in, apply_user_ids)
        raise NotImplemented

    def i_set_material_property_values(self, material_values, config_opt, config_count, config_names):
        """
        Sets the material property values for this feature in the specified configurations.
        :param material_values:

in-process, unmanaged C++: Pointer to an array of material property values (see Remarks)

VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
        :param config_opt: Configuration option as defined in swInConfigurationOpts_e
        :param config_count: Number of configurations (see Remarks)
        :param config_names:
in-process, unmanaged C++: Pointer to an array of configuration names of size Config_count
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
        """
        # return self._instance.ISetMaterialPropertyValues2(material_values, config_opt, config_count, config_names)
        raise NotImplemented

    def i_set_suppression(self, suppression_state, config_opt, config_count, config_names):
        """
        Sets the suppression state of this feature.
        :param suppression_state: Suppression state as defined in swFeatureSuppressionAction_e
        :param config_opt: Configuration option as defined in swInConfigurationOpts_e
        :param config_count: Number of configurations
        :param config_names: Array of configuration names of size Config_count
        """
        # return self._instance.ISetSuppression2(suppression_state, config_opt, config_count, config_names)
        raise NotImplemented

    def is_frozen(self):
        """Gets whether this feature is frozen."""
        # return self._instance.IsFrozen
        raise NotImplemented

    def is_hidden_lock(self):
        """Gets whether this feature is the freeze bar."""
        # return self._instance.IsHiddenLock
        raise NotImplemented

    def is_rolled_back(self):
        """Gets whether this feature is rolled back."""
        # return self._instance.IsRolledBack
        raise NotImplemented

    def is_suppressed(self, config_opt, config_names):
        """
        Gets whether the feature in the specified configurations is suppressed.
        :param config_opt: Configuration option as defined by swInConfigurationOpts_e
        :param config_names: Array of configuration names
        """
        # return self._instance.IsSuppressed2(config_opt, config_names)
        raise NotImplemented

    def list_external_file_references(self, model_path_name, component_path_name, feature, data_type, status,
                                      ref_entity, feat_com, config_option, config_name):
        """
        Gets the names and statuses of the external references on the feature in a part or assembly.
        :param model_path_name: Array of path names of documents
        :param component_path_name: Array of path names of referenced components
        :param feature: Array of in-context items (sketches, features, and so on)
        :param data_type: Array of data used to create the items (converted edge or face, converted or offset sketch entity, body, and so on)
        :param status: Array of statuses of external reference as defined in swExternalReferenceStatus_e
        :param ref_entity: Array of actual items being used and the names of the documents that contain the items
        :param feat_com: Array of the names of the components in which the affected features exist; this information is only displayed when one or more RefEntity is in a different component in an assembly and does not apply to derived parts
        :param config_option: Configuration option as defined by swExternalFileReferencesConfig_e
        :param config_name: Name of the configuration when ConfigOption is swExternalFileReferencesNamedConfig
        """
        # return self._instance.ListExternalFileReferences2(model_path_name, component_path_name, feature, data_type, status, ref_entity, feat_com, config_option, config_name)
        raise NotImplemented

    def list_external_file_references_count(self):
        """Gets the number of external references on the feature in a part or assembly."""
        # return self._instance.ListExternalFileReferencesCount
        raise NotImplemented

    def make_sub_feature(self, sub_feature):
        """
        Makes a feature become a subfeature of this feature.
        :param sub_feature: Pointer to the feature to become a subfeature
        """
        # return self._instance.MakeSubFeature(sub_feature)
        raise NotImplemented

    def modify_definition(self, data, top_doc, component):
        """
        Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::GetDefinition.
        :param data: Feature data object
        :param top_doc: Top-level document (see Remarks)
        :param component: Component for the feature (see Remarks)
        """
        # return self._instance.ModifyDefinition(data, top_doc, component)
        raise NotImplemented

    def move_freeze_bar_to(self, location, update_all_configs, unlock_configs):
        """
        Moves the freeze bar to the specified location in the FeatureManager design tree.
        :param location:
swMoveFreezeBarTo_e.swMoveFreezeBarToBeforeFeature-or-

swMoveFreezeBarTo_e.swMoveFreezeBarToAfterFeature
        :param update_all_configs: True to update all configurations, false to not
        :param unlock_configs: True to unlock configurations, false to not
        """
        # return self._instance.MoveFreezeBarTo2(location, update_all_configs, unlock_configs)
        raise NotImplemented

    def parameter(self, name):
        """
        Gets a pointer to the object for the specified parameter or a pointer to the specified parameter.
        :param name: Name of parameter (for example, "D1")
        """
        # return self._instance.Parameter(name)
        raise NotImplemented

    def remove_material_property(self, config_opt, config_names):
        """
        Removes material property values from this feature.
        :param config_opt: Configuration option as defined in swInConfigurationOpts_e
        :param config_names: Array of configuration names
        """
        # return self._instance.RemoveMaterialProperty2(config_opt, config_names)
        raise NotImplemented

    def remove_texture(self, b_all_config, config_name):
        """
        Removes texture from this feature in either all of the configurations or only the specified configuration.
        :param b_all_config: True to remove texture from this feature in all configurations, false to remove texture from this feature in the configuration specified in Config_name only
        :param config_name: Name of configuration
        """
        # return self._instance.RemoveTexture(b_all_config, config_name)
        raise NotImplemented

    def remove_texture_by_display_state(self, display_state_name):
        """
        Removes texture from this feature in the specified display state.
        :param display_state_name: Display state name
        """
        # return self._instance.RemoveTextureByDisplayState(display_state_name)
        raise NotImplemented

    def reset_property_extension(self):
        """Deletes the property extension for this feature."""
        # return self._instance.ResetPropertyExtension
        raise NotImplemented

    def select(self, append, mark):
        """
        Selects and marks this feature.
        :param append: True appends the feature to the current selection list, false replaces the current selection list
        :param mark: Value you want to use as a mark; this number is used by functions that require ordered selection
        """
        # return self._instance.Select2(append, mark)
        raise NotImplemented

    def set_bodies_to_keep(self, all_bodies, bodies_to_keep, config_option, config_names):
        """
        Set the bodies to keep and their configurations for features that create multiple bodies in parts and assemblies.
        :param all_bodies: True to keep all bodies, false to not
        :param bodies_to_keep: Array of bodies to keep
        :param config_option: Configuration options as defined in swInConfigurationOpts_e
        :param config_names: Array of configuration names
        """
        # return self._instance.SetBodiesToKeep(all_bodies, bodies_to_keep, config_option, config_names)
        raise NotImplemented

    def set_body(self, body_in, apply_user_ids):
        """
        Replaces an imported base feature body.
        :param body_in: Temporary body that replaces the base feature body
        :param apply_user_ids: True applies user-defined face IDs, false does not
        """
        # return self._instance.SetBody2(body_in, apply_user_ids)
        raise NotImplemented

    def set_imported_feature_parameters(self, data_obj):
        """
        Sets the data object for this 3D Interconnect part or assembly.
        :param data_obj: IImport3DInterconnectData
        """
        # return self._instance.SetImportedFeatureParameters(data_obj)
        raise NotImplemented

    def set_imported_file_name(self, imp_name):
        """
        Sets the file name of an imported feature.
        :param imp_name: New filename of the imported feature
        """
        # return self._instance.SetImportedFileName(imp_name)
        raise NotImplemented

    def set_material_id_name(self, name):
        """
        Sets the material name for this feature.
        :param name: Material name for this feature
        """
        # return self._instance.SetMaterialIdName(name)
        raise NotImplemented

    def set_material_property_values(self, material_values, config_opt, config_names):
        """
        Sets the material property values for this feature in the specified configurations.
        :param material_values: Array of material property values
        :param config_opt: Configuration option as defined in swInConfigurationOpts_e
        :param config_names: Array of configuration names
        """
        # return self._instance.SetMaterialPropertyValues2(material_values, config_opt, config_names)
        raise NotImplemented

    def set_material_user_name(self, name):
        """
        Sets the material user name for this feature, which is visible to the user.
        :param name: Material user name property for this feature
        """
        # return self._instance.SetMaterialUserName(name)
        raise NotImplemented

    def set_suppression(self, suppression_state, config_opt, config_names):
        """
        Sets the suppression state of this feature.
        :param suppression_state: Suppression state as defined in swFeatureSuppressionAction_e
        :param config_opt: Configuration option as defined in swInConfigurationOpts_e (see Remarks)
        :param config_names: Array of configuration names; valid only if Config_opt set to swInConfigurationOpts_e.swSpecifyConfiguration
        """
        # return self._instance.SetSuppression2(suppression_state, config_opt, config_names)
        raise NotImplemented

    def set_texture(self, b_all_config, config_name, texture_in):
        """
        Applies texture to this feature in either all configurations or only the specified configuration.
        :param b_all_config: True to apply texture to this feature all configurations, false to apply texture to this feature in the configuration specified in config_name only
        :param config_name: Name of configuration
        :param texture_in: Pointer to the ITexture object
        """
        # return self._instance.SetTexture(b_all_config, config_name, texture_in)
        raise NotImplemented

    def set_texture_by_display_state(self, display_state_name, texture_in):
        """
        Applies texture to this feature in the specified display state.
        :param display_state_name: Display state name
        :param texture_in: Texture
        """
        # return self._instance.SetTextureByDisplayState(display_state_name, texture_in)
        raise NotImplemented

    def set_u_i_state(self, state_type, flag):
        """
        Sets the user-interface state of the current feature.
        :param state_type: User interface state type as defined in swUIStates_e
        :param flag: True to set the user-interface state, false to not
        """
        # return self._instance.SetUIState(state_type, flag)
        raise NotImplemented

    def update_d_interconnect_model(self):
        """Updates the model for this 3D Interconnect part or assembly."""
        # return self._instance.Update3DInterconnectModel
        raise NotImplemented

    def update_external_file_references(self, config_option, config_name, update_status):
        """
        Updates the external file references on this model.
        :param config_option: Configuration options as defined by swExternalFileReferencesConfig_e
        :param config_name: Name of configuration; required when ConfigOption set to swExternalFileReferencesNamedConfig
        :param update_status: Update status option as defined byswExternalFileReferencesUpdate_e
        """
        # return self._instance.UpdateExternalFileReferences(config_option, config_name, update_status)
        raise NotImplemented
