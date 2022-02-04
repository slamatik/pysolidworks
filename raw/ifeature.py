# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html
class IFeature:
	def __init__(self, parent=None):
		self._instance = parent

	def created_by(self):
		"""Gets the name of the user who created the feature."""
		# return self._instance.CreatedBy
		raise NotImplemented

	def custom_property_manager(self):
		"""Gets the custom property information for weldment and cut-list item features only."""
		# return self._instance.CustomPropertyManager
		raise NotImplemented

	def date_created(self):
		"""Gets the date on which the feature was created."""
		# return self._instance.DateCreated
		raise NotImplemented

	def date_modified(self):
		"""Gets the date on which the feature was last modified."""
		# return self._instance.DateModified
		raise NotImplemented

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
		return self._instance.Is3DInterconnectFeature

	@is_d_interconnect_feature.setter
	def is_d_interconnect_feature(self, value):
		"""Gets whether this is a 3D Interconnect feature."""
		self._instance.Is3DInterconnectFeature = value

	@property
	def is_d_interconnect_update_available(self):
		"""Gets whether an update is available for this 3D Interconnect part or assembly."""
		return self._instance.Is3DInterconnectUpdateAvailable

	@is_d_interconnect_update_available.setter
	def is_d_interconnect_update_available(self, value):
		"""Gets whether an update is available for this 3D Interconnect part or assembly."""
		self._instance.Is3DInterconnectUpdateAvailable = value

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
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets the visibility state of this feature."""
		self._instance.Visible = value

	@property
	def add_comment(self):
		"""Adds a comment to this feature."""
		return self._instance.AddComment

	@add_comment.setter
	def add_comment(self, value):
		"""Adds a comment to this feature."""
		self._instance.AddComment = value

	@property
	def add_property_extension(self):
		"""Adds a property extension to this feature."""
		return self._instance.AddPropertyExtension

	@add_property_extension.setter
	def add_property_extension(self, value):
		"""Adds a property extension to this feature."""
		self._instance.AddPropertyExtension = value

	@property
	def break_link(self):
		"""Breaks the link to third-party native CAD parts and assemblies."""
		return self._instance.BreakLink

	@break_link.setter
	def break_link(self, value):
		"""Breaks the link to third-party native CAD parts and assemblies."""
		self._instance.BreakLink = value

	@property
	def de_select(self):
		"""Deselects this feature."""
		return self._instance.DeSelect

	@de_select.setter
	def de_select(self, value):
		"""Deselects this feature."""
		self._instance.DeSelect = value

	@property
	def enum_display_dimensions(self):
		"""This method returns a display dimensions enumeration for this feature."""
		return self._instance.EnumDisplayDimensions

	@enum_display_dimensions.setter
	def enum_display_dimensions(self, value):
		"""This method returns a display dimensions enumeration for this feature."""
		self._instance.EnumDisplayDimensions = value

	@property
	def get_affected_face_count(self):
		"""Gets the number of faces modified by a feature, such as a draft feature."""
		return self._instance.GetAffectedFaceCount

	@get_affected_face_count.setter
	def get_affected_face_count(self, value):
		"""Gets the number of faces modified by a feature, such as a draft feature."""
		self._instance.GetAffectedFaceCount = value

	@property
	def get_affected_faces(self):
		"""Gets the faces modified by a feature, such as a draft feature."""
		return self._instance.GetAffectedFaces

	@get_affected_faces.setter
	def get_affected_faces(self, value):
		"""Gets the faces modified by a feature, such as a draft feature."""
		self._instance.GetAffectedFaces = value

	@property
	def get_box(self):
		"""Gets the bounding box for this feature."""
		return self._instance.GetBox

	@get_box.setter
	def get_box(self, value):
		"""Gets the bounding box for this feature."""
		self._instance.GetBox = value

	@property
	def get_children(self):
		"""Gets the child features belonging to this feature."""
		return self._instance.GetChildren

	@get_children.setter
	def get_children(self, value):
		"""Gets the child features belonging to this feature."""
		self._instance.GetChildren = value

	@property
	def get_created_version(self):
		"""Gets the SOLIDWORKS version number in which the selected feature was created."""
		return self._instance.GetCreatedVersion

	@get_created_version.setter
	def get_created_version(self, value):
		"""Gets the SOLIDWORKS version number in which the selected feature was created."""
		self._instance.GetCreatedVersion = value

	@property
	def get_definition(self):
		"""Gets the feature data object for a feature, such as an advanced mate, extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature."""
		return self._instance.GetDefinition

	@get_definition.setter
	def get_definition(self, value):
		"""Gets the feature data object for a feature, such as an advanced mate, extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature."""
		self._instance.GetDefinition = value

	@property
	def get_display_dimension(self):
		"""Gets the display dimension object for the specified pattern property."""
		return self._instance.GetDisplayDimension

	@get_display_dimension.setter
	def get_display_dimension(self, value):
		"""Gets the display dimension object for the specified pattern property."""
		self._instance.GetDisplayDimension = value

	@property
	def get_edit_status(self):
		"""Gets whether the feature can currently be edited."""
		return self._instance.GetEditStatus

	@get_edit_status.setter
	def get_edit_status(self, value):
		"""Gets whether the feature can currently be edited."""
		self._instance.GetEditStatus = value

	@property
	def get_error_code(self):
		"""Gets the error code for this feature."""
		return self._instance.GetErrorCode2

	@get_error_code.setter
	def get_error_code(self, value):
		"""Gets the error code for this feature."""
		self._instance.GetErrorCode2 = value

	@property
	def get_face_count(self):
		"""Gets the number of faces in this feature."""
		return self._instance.GetFaceCount

	@get_face_count.setter
	def get_face_count(self, value):
		"""Gets the number of faces in this feature."""
		self._instance.GetFaceCount = value

	@property
	def get_faces(self):
		"""Gets the faces in this feature."""
		return self._instance.GetFaces

	@get_faces.setter
	def get_faces(self, value):
		"""Gets the faces in this feature."""
		self._instance.GetFaces = value

	@property
	def get_first_display_dimension(self):
		"""Provides access to the dimensions that belong to this feature by returning the first display dimension associated with this feature."""
		return self._instance.GetFirstDisplayDimension

	@get_first_display_dimension.setter
	def get_first_display_dimension(self, value):
		"""Provides access to the dimensions that belong to this feature by returning the first display dimension associated with this feature."""
		self._instance.GetFirstDisplayDimension = value

	@property
	def get_first_sub_feature(self):
		"""Gets the first sub-feature that belongs to this feature."""
		return self._instance.GetFirstSubFeature

	@get_first_sub_feature.setter
	def get_first_sub_feature(self, value):
		"""Gets the first sub-feature that belongs to this feature."""
		self._instance.GetFirstSubFeature = value

	@property
	def get_i_d(self):
		"""Gets the feature ID of this feature."""
		return self._instance.GetID

	@get_i_d.setter
	def get_i_d(self, value):
		"""Gets the feature ID of this feature."""
		self._instance.GetID = value

	@property
	def get_imported_feature_parameters(self):
		"""Gets the data object for this 3D Interconnect part or assembly."""
		return self._instance.GetImportedFeatureParameters

	@get_imported_feature_parameters.setter
	def get_imported_feature_parameters(self, value):
		"""Gets the data object for this 3D Interconnect part or assembly."""
		self._instance.GetImportedFeatureParameters = value

	@property
	def get_imported_file_name(self):
		"""Gets the file name from an imported feature."""
		return self._instance.GetImportedFileName

	@get_imported_file_name.setter
	def get_imported_file_name(self, value):
		"""Gets the file name from an imported feature."""
		self._instance.GetImportedFileName = value

	@property
	def get_material_id_name(self):
		"""Gets the material name."""
		return self._instance.GetMaterialIdName

	@get_material_id_name.setter
	def get_material_id_name(self, value):
		"""Gets the material name."""
		self._instance.GetMaterialIdName = value

	@property
	def get_material_property_values(self):
		"""Gets the material property values for this feature in the specified configurations."""
		return self._instance.GetMaterialPropertyValues2

	@get_material_property_values.setter
	def get_material_property_values(self, value):
		"""Gets the material property values for this feature in the specified configurations."""
		self._instance.GetMaterialPropertyValues2 = value

	@property
	def get_material_user_name(self):
		"""Gets the material name for this feature, which is visible to the user."""
		return self._instance.GetMaterialUserName

	@get_material_user_name.setter
	def get_material_user_name(self, value):
		"""Gets the material name for this feature, which is visible to the user."""
		self._instance.GetMaterialUserName = value

	@property
	def get_modified_version(self):
		"""Gets the SOLIDWORKS version number in which this feature was last modified."""
		return self._instance.GetModifiedVersion

	@get_modified_version.setter
	def get_modified_version(self, value):
		"""Gets the SOLIDWORKS version number in which this feature was last modified."""
		self._instance.GetModifiedVersion = value

	@property
	def get_name_for_selection(self):
		"""Gets the selected feature's type and name."""
		return self._instance.GetNameForSelection

	@get_name_for_selection.setter
	def get_name_for_selection(self, value):
		"""Gets the selected feature's type and name."""
		self._instance.GetNameForSelection = value

	@property
	def get_next_display_dimension(self):
		"""Gets the next display dimension associated with this feature."""
		return self._instance.GetNextDisplayDimension

	@get_next_display_dimension.setter
	def get_next_display_dimension(self, value):
		"""Gets the next display dimension associated with this feature."""
		self._instance.GetNextDisplayDimension = value

	@property
	def get_next_feature(self):
		"""Gets the next feature in the part."""
		return self._instance.GetNextFeature

	@get_next_feature.setter
	def get_next_feature(self, value):
		"""Gets the next feature in the part."""
		self._instance.GetNextFeature = value

	@property
	def get_next_sub_feature(self):
		"""Gets the next sub-feature from the owner of this sub-feature."""
		return self._instance.GetNextSubFeature

	@get_next_sub_feature.setter
	def get_next_sub_feature(self, value):
		"""Gets the next sub-feature from the owner of this sub-feature."""
		self._instance.GetNextSubFeature = value

	@property
	def get_owner_feature(self):
		"""Gets the feature that owns this feature."""
		return self._instance.GetOwnerFeature

	@get_owner_feature.setter
	def get_owner_feature(self, value):
		"""Gets the feature that owns this feature."""
		self._instance.GetOwnerFeature = value

	@property
	def get_parents(self):
		"""Gets the parent features for this feature."""
		return self._instance.GetParents

	@get_parents.setter
	def get_parents(self, value):
		"""Gets the parent features for this feature."""
		self._instance.GetParents = value

	@property
	def get_property_extension(self):
		"""Gets the property extension on this feature."""
		return self._instance.GetPropertyExtension

	@get_property_extension.setter
	def get_property_extension(self, value):
		"""Gets the property extension on this feature."""
		self._instance.GetPropertyExtension = value

	@property
	def get_specific_feature(self):
		"""Gets the more specific interface to a selected feature."""
		return self._instance.GetSpecificFeature2

	@get_specific_feature.setter
	def get_specific_feature(self, value):
		"""Gets the more specific interface to a selected feature."""
		self._instance.GetSpecificFeature2 = value

	@property
	def get_texture(self):
		"""Gets the texture applied to this feature in the specified configuration."""
		return self._instance.GetTexture

	@get_texture.setter
	def get_texture(self, value):
		"""Gets the texture applied to this feature in the specified configuration."""
		self._instance.GetTexture = value

	@property
	def get_type_name(self):
		"""Gets the type of feature. 
NOTE: To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call this method; otherwise, call IFeature::GetTypeName2."""
		return self._instance.GetTypeName

	@get_type_name.setter
	def get_type_name(self, value):
		"""Gets the type of feature. 
NOTE: To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call this method; otherwise, call IFeature::GetTypeName2."""
		self._instance.GetTypeName = value

	@property
	def get_type_name(self):
		"""Gets the type of feature.
NOTE: To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call IFeature::GetTypeName; otherwise, call this method."""
		return self._instance.GetTypeName2

	@get_type_name.setter
	def get_type_name(self, value):
		"""Gets the type of feature.
NOTE: To get the underlying type of feature of an Instant3D feature (i.e., "ICE"), call IFeature::GetTypeName; otherwise, call this method."""
		self._instance.GetTypeName2 = value

	@property
	def get_u_i_state(self):
		"""Gets the user-interface state of the current feature."""
		return self._instance.GetUIState

	@get_u_i_state.setter
	def get_u_i_state(self, value):
		"""Gets the user-interface state of the current feature."""
		self._instance.GetUIState = value

	@property
	def get_update_stamp(self):
		"""Gets the current update stamp for this feature."""
		return self._instance.GetUpdateStamp

	@get_update_stamp.setter
	def get_update_stamp(self, value):
		"""Gets the current update stamp for this feature."""
		self._instance.GetUpdateStamp = value

	@property
	def has_frozen_update_pending(self):
		"""Gets whether this feature has pending freeze updates."""
		return self._instance.HasFrozenUpdatePending

	@has_frozen_update_pending.setter
	def has_frozen_update_pending(self, value):
		"""Gets whether this feature has pending freeze updates."""
		self._instance.HasFrozenUpdatePending = value

	@property
	def has_material_property_values(self):
		"""Gets whether this feature has an appearance."""
		return self._instance.HasMaterialPropertyValues

	@has_material_property_values.setter
	def has_material_property_values(self, value):
		"""Gets whether this feature has an appearance."""
		self._instance.HasMaterialPropertyValues = value

	@property
	def i_get_affected_faces(self):
		"""Gets the faces modified by a feature, such as a draft feature."""
		return self._instance.IGetAffectedFaces

	@i_get_affected_faces.setter
	def i_get_affected_faces(self, value):
		"""Gets the faces modified by a feature, such as a draft feature."""
		self._instance.IGetAffectedFaces = value

	@property
	def i_get_box(self):
		"""Gets the bounding box for this feature."""
		return self._instance.IGetBox

	@i_get_box.setter
	def i_get_box(self, value):
		"""Gets the bounding box for this feature."""
		self._instance.IGetBox = value

	@property
	def i_get_child_count(self):
		"""Gets the number of child features that belong to this feature."""
		return self._instance.IGetChildCount

	@i_get_child_count.setter
	def i_get_child_count(self, value):
		"""Gets the number of child features that belong to this feature."""
		self._instance.IGetChildCount = value

	@property
	def i_get_children(self):
		"""Gets the child features belonging to this feature."""
		return self._instance.IGetChildren

	@i_get_children.setter
	def i_get_children(self, value):
		"""Gets the child features belonging to this feature."""
		self._instance.IGetChildren = value

	@property
	def i_get_definition(self):
		"""Gets the feature data object for a feature, such as an extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature."""
		return self._instance.IGetDefinition

	@i_get_definition.setter
	def i_get_definition(self, value):
		"""Gets the feature data object for a feature, such as an extrusion, loft, fillet, chamfer, etc., in order to access the parameters that control the definition of this feature."""
		self._instance.IGetDefinition = value

	@property
	def i_get_faces(self):
		"""Gets the faces in this feature."""
		return self._instance.IGetFaces2

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets the faces in this feature."""
		self._instance.IGetFaces2 = value

	@property
	def i_get_first_sub_feature(self):
		"""Gets the first sub-feature that belongs to this feature."""
		return self._instance.IGetFirstSubFeature

	@i_get_first_sub_feature.setter
	def i_get_first_sub_feature(self, value):
		"""Gets the first sub-feature that belongs to this feature."""
		self._instance.IGetFirstSubFeature = value

	@property
	def i_get_material_property_values(self):
		"""Gets the material property values for this feature in the specified configurations."""
		return self._instance.IGetMaterialPropertyValues2

	@i_get_material_property_values.setter
	def i_get_material_property_values(self, value):
		"""Gets the material property values for this feature in the specified configurations."""
		self._instance.IGetMaterialPropertyValues2 = value

	@property
	def i_get_next_feature(self):
		"""Gets the next feature."""
		return self._instance.IGetNextFeature

	@i_get_next_feature.setter
	def i_get_next_feature(self, value):
		"""Gets the next feature."""
		self._instance.IGetNextFeature = value

	@property
	def i_get_next_sub_feature(self):
		"""Gets the next sub-feature from the owner of this sub-feature."""
		return self._instance.IGetNextSubFeature

	@i_get_next_sub_feature.setter
	def i_get_next_sub_feature(self, value):
		"""Gets the next sub-feature from the owner of this sub-feature."""
		self._instance.IGetNextSubFeature = value

	@property
	def i_get_parent_count(self):
		"""Gets the number of parent features for this feature."""
		return self._instance.IGetParentCount

	@i_get_parent_count.setter
	def i_get_parent_count(self, value):
		"""Gets the number of parent features for this feature."""
		self._instance.IGetParentCount = value

	@property
	def i_get_parents(self):
		"""Gets the parent features for this feature."""
		return self._instance.IGetParents

	@i_get_parents.setter
	def i_get_parents(self, value):
		"""Gets the parent features for this feature."""
		self._instance.IGetParents = value

	@property
	def i_is_suppressed(self):
		"""Gets whether the feature in the specified configurations is suppressed."""
		return self._instance.IIsSuppressed2

	@i_is_suppressed.setter
	def i_is_suppressed(self, value):
		"""Gets whether the feature in the specified configurations is suppressed."""
		self._instance.IIsSuppressed2 = value

	@property
	def i_list_external_file_references(self):
		"""Gets the names and statuses of the external references for this feature in a part or assembly."""
		return self._instance.IListExternalFileReferences2

	@i_list_external_file_references.setter
	def i_list_external_file_references(self, value):
		"""Gets the names and statuses of the external references for this feature in a part or assembly."""
		self._instance.IListExternalFileReferences2 = value

	@property
	def i_modify_definition(self):
		"""Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::IGetDefinition."""
		return self._instance.IModifyDefinition2

	@i_modify_definition.setter
	def i_modify_definition(self, value):
		"""Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::IGetDefinition."""
		self._instance.IModifyDefinition2 = value

	@property
	def i_parameter(self):
		"""Gets a pointer to the object for the specified parameter or a pointer to the specified parameter."""
		return self._instance.IParameter

	@i_parameter.setter
	def i_parameter(self, value):
		"""Gets a pointer to the object for the specified parameter or a pointer to the specified parameter."""
		self._instance.IParameter = value

	@property
	def i_remove_material_property(self):
		"""Removes material property values from this feature."""
		return self._instance.IRemoveMaterialProperty2

	@i_remove_material_property.setter
	def i_remove_material_property(self, value):
		"""Removes material property values from this feature."""
		self._instance.IRemoveMaterialProperty2 = value

	@property
	def is_base(self):
		"""Gets whether this feature is a base feature."""
		return self._instance.IsBase2

	@is_base.setter
	def is_base(self, value):
		"""Gets whether this feature is a base feature."""
		self._instance.IsBase2 = value

	@property
	def is_dim_xpert_annotation(self):
		"""Gets whether this feature is a DimXpert annotation."""
		return self._instance.IsDimXpertAnnotation

	@is_dim_xpert_annotation.setter
	def is_dim_xpert_annotation(self, value):
		"""Gets whether this feature is a DimXpert annotation."""
		self._instance.IsDimXpertAnnotation = value

	@property
	def is_dim_xpert_feature(self):
		"""Gets whether this feature is a DimXpert feature."""
		return self._instance.IsDimXpertFeature

	@is_dim_xpert_feature.setter
	def is_dim_xpert_feature(self, value):
		"""Gets whether this feature is a DimXpert feature."""
		self._instance.IsDimXpertFeature = value

	@property
	def i_set_body(self):
		"""Replaces the body of the base feature."""
		return self._instance.ISetBody3

	@i_set_body.setter
	def i_set_body(self, value):
		"""Replaces the body of the base feature."""
		self._instance.ISetBody3 = value

	@property
	def i_set_material_property_values(self):
		"""Sets the material property values for this feature in the specified configurations."""
		return self._instance.ISetMaterialPropertyValues2

	@i_set_material_property_values.setter
	def i_set_material_property_values(self, value):
		"""Sets the material property values for this feature in the specified configurations."""
		self._instance.ISetMaterialPropertyValues2 = value

	@property
	def i_set_suppression(self):
		"""Sets the suppression state of this feature."""
		return self._instance.ISetSuppression2

	@i_set_suppression.setter
	def i_set_suppression(self, value):
		"""Sets the suppression state of this feature."""
		self._instance.ISetSuppression2 = value

	@property
	def is_frozen(self):
		"""Gets whether this feature is frozen."""
		return self._instance.IsFrozen

	@is_frozen.setter
	def is_frozen(self, value):
		"""Gets whether this feature is frozen."""
		self._instance.IsFrozen = value

	@property
	def is_hidden_lock(self):
		"""Gets whether this feature is the freeze bar."""
		return self._instance.IsHiddenLock

	@is_hidden_lock.setter
	def is_hidden_lock(self, value):
		"""Gets whether this feature is the freeze bar."""
		self._instance.IsHiddenLock = value

	@property
	def is_rolled_back(self):
		"""Gets whether this feature is rolled back."""
		return self._instance.IsRolledBack

	@is_rolled_back.setter
	def is_rolled_back(self, value):
		"""Gets whether this feature is rolled back."""
		self._instance.IsRolledBack = value

	@property
	def is_suppressed(self):
		"""Gets whether the feature in the specified configurations is suppressed."""
		return self._instance.IsSuppressed2

	@is_suppressed.setter
	def is_suppressed(self, value):
		"""Gets whether the feature in the specified configurations is suppressed."""
		self._instance.IsSuppressed2 = value

	@property
	def list_external_file_references(self):
		"""Gets the names and statuses of the external references on the feature in a part or assembly."""
		return self._instance.ListExternalFileReferences2

	@list_external_file_references.setter
	def list_external_file_references(self, value):
		"""Gets the names and statuses of the external references on the feature in a part or assembly."""
		self._instance.ListExternalFileReferences2 = value

	@property
	def list_external_file_references_count(self):
		"""Gets the number of external references on the feature in a part or assembly."""
		return self._instance.ListExternalFileReferencesCount

	@list_external_file_references_count.setter
	def list_external_file_references_count(self, value):
		"""Gets the number of external references on the feature in a part or assembly."""
		self._instance.ListExternalFileReferencesCount = value

	@property
	def make_sub_feature(self):
		"""Makes a feature become a subfeature of this feature."""
		return self._instance.MakeSubFeature

	@make_sub_feature.setter
	def make_sub_feature(self, value):
		"""Makes a feature become a subfeature of this feature."""
		self._instance.MakeSubFeature = value

	@property
	def modify_definition(self):
		"""Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::GetDefinition."""
		return self._instance.ModifyDefinition

	@modify_definition.setter
	def modify_definition(self, value):
		"""Updates the definition of a feature with the new values in an associated feature data object obtained with IFeature::GetDefinition."""
		self._instance.ModifyDefinition = value

	@property
	def move_freeze_bar_to(self):
		"""Moves the freeze bar to the specified location in the FeatureManager design tree."""
		return self._instance.MoveFreezeBarTo2

	@move_freeze_bar_to.setter
	def move_freeze_bar_to(self, value):
		"""Moves the freeze bar to the specified location in the FeatureManager design tree."""
		self._instance.MoveFreezeBarTo2 = value

	@property
	def parameter(self):
		"""Gets a pointer to the object for the specified parameter or a pointer to the specified parameter."""
		return self._instance.Parameter

	@parameter.setter
	def parameter(self, value):
		"""Gets a pointer to the object for the specified parameter or a pointer to the specified parameter."""
		self._instance.Parameter = value

	@property
	def remove_material_property(self):
		"""Removes material property values from this feature."""
		return self._instance.RemoveMaterialProperty2

	@remove_material_property.setter
	def remove_material_property(self, value):
		"""Removes material property values from this feature."""
		self._instance.RemoveMaterialProperty2 = value

	@property
	def remove_texture(self):
		"""Removes texture from this feature in either all of the configurations or only the specified configuration."""
		return self._instance.RemoveTexture

	@remove_texture.setter
	def remove_texture(self, value):
		"""Removes texture from this feature in either all of the configurations or only the specified configuration."""
		self._instance.RemoveTexture = value

	@property
	def remove_texture_by_display_state(self):
		"""Removes texture from this feature in the specified display state."""
		return self._instance.RemoveTextureByDisplayState

	@remove_texture_by_display_state.setter
	def remove_texture_by_display_state(self, value):
		"""Removes texture from this feature in the specified display state."""
		self._instance.RemoveTextureByDisplayState = value

	@property
	def reset_property_extension(self):
		"""Deletes the property extension for this feature."""
		return self._instance.ResetPropertyExtension

	@reset_property_extension.setter
	def reset_property_extension(self, value):
		"""Deletes the property extension for this feature."""
		self._instance.ResetPropertyExtension = value

	@property
	def select(self):
		"""Selects and marks this feature."""
		return self._instance.Select2

	@select.setter
	def select(self, value):
		"""Selects and marks this feature."""
		self._instance.Select2 = value

	@property
	def set_bodies_to_keep(self):
		"""Set the bodies to keep and their configurations for features that create multiple bodies in parts and assemblies."""
		return self._instance.SetBodiesToKeep

	@set_bodies_to_keep.setter
	def set_bodies_to_keep(self, value):
		"""Set the bodies to keep and their configurations for features that create multiple bodies in parts and assemblies."""
		self._instance.SetBodiesToKeep = value

	@property
	def set_body(self):
		"""Replaces an imported base feature body."""
		return self._instance.SetBody2

	@set_body.setter
	def set_body(self, value):
		"""Replaces an imported base feature body."""
		self._instance.SetBody2 = value

	@property
	def set_imported_feature_parameters(self):
		"""Sets the data object for this 3D Interconnect part or assembly."""
		return self._instance.SetImportedFeatureParameters

	@set_imported_feature_parameters.setter
	def set_imported_feature_parameters(self, value):
		"""Sets the data object for this 3D Interconnect part or assembly."""
		self._instance.SetImportedFeatureParameters = value

	@property
	def set_imported_file_name(self):
		"""Sets the file name of an imported feature."""
		return self._instance.SetImportedFileName

	@set_imported_file_name.setter
	def set_imported_file_name(self, value):
		"""Sets the file name of an imported feature."""
		self._instance.SetImportedFileName = value

	@property
	def set_material_id_name(self):
		"""Sets the material name for this feature."""
		return self._instance.SetMaterialIdName

	@set_material_id_name.setter
	def set_material_id_name(self, value):
		"""Sets the material name for this feature."""
		self._instance.SetMaterialIdName = value

	@property
	def set_material_property_values(self):
		"""Sets the material property values for this feature in the specified configurations."""
		return self._instance.SetMaterialPropertyValues2

	@set_material_property_values.setter
	def set_material_property_values(self, value):
		"""Sets the material property values for this feature in the specified configurations."""
		self._instance.SetMaterialPropertyValues2 = value

	@property
	def set_material_user_name(self):
		"""Sets the material user name for this feature, which is visible to the user."""
		return self._instance.SetMaterialUserName

	@set_material_user_name.setter
	def set_material_user_name(self, value):
		"""Sets the material user name for this feature, which is visible to the user."""
		self._instance.SetMaterialUserName = value

	@property
	def set_suppression(self):
		"""Sets the suppression state of this feature."""
		return self._instance.SetSuppression2

	@set_suppression.setter
	def set_suppression(self, value):
		"""Sets the suppression state of this feature."""
		self._instance.SetSuppression2 = value

	@property
	def set_texture(self):
		"""Applies texture to this feature in either all configurations or only the specified configuration."""
		return self._instance.SetTexture

	@set_texture.setter
	def set_texture(self, value):
		"""Applies texture to this feature in either all configurations or only the specified configuration."""
		self._instance.SetTexture = value

	@property
	def set_texture_by_display_state(self):
		"""Applies texture to this feature in the specified display state."""
		return self._instance.SetTextureByDisplayState

	@set_texture_by_display_state.setter
	def set_texture_by_display_state(self, value):
		"""Applies texture to this feature in the specified display state."""
		self._instance.SetTextureByDisplayState = value

	@property
	def set_u_i_state(self):
		"""Sets the user-interface state of the current feature."""
		return self._instance.SetUIState

	@set_u_i_state.setter
	def set_u_i_state(self, value):
		"""Sets the user-interface state of the current feature."""
		self._instance.SetUIState = value

	@property
	def update_d_interconnect_model(self):
		"""Updates the model for this 3D Interconnect part or assembly."""
		return self._instance.Update3DInterconnectModel

	@update_d_interconnect_model.setter
	def update_d_interconnect_model(self, value):
		"""Updates the model for this 3D Interconnect part or assembly."""
		self._instance.Update3DInterconnectModel = value

	@property
	def update_external_file_references(self):
		"""Updates the external file references on this model."""
		return self._instance.UpdateExternalFileReferences

	@update_external_file_references.setter
	def update_external_file_references(self, value):
		"""Updates the external file references on this model."""
		self._instance.UpdateExternalFileReferences = value

