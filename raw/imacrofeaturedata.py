# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html
class IMacroFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def current_configuration(self):
		"""Gets the macro feature configuration being rebuilt."""
		# return self._instance.CurrentConfiguration
		raise NotImplemented

	@property
	def edit_bodies(self):
		"""Gets or sets the bodies to be modified by this macro feature."""
		return self._instance.EditBodies

	@edit_bodies.setter
	def edit_bodies(self, value):
		"""Gets or sets the bodies to be modified by this macro feature."""
		self._instance.EditBodies = value

	@property
	def enable_multi_body_consume(self):
		"""Gets or sets whether to replace the original edit body with multiple solid bodies created during regeneration of a multibody macro feature."""
		return self._instance.EnableMultiBodyConsume

	@enable_multi_body_consume.setter
	def enable_multi_body_consume(self, value):
		"""Gets or sets whether to replace the original edit body with multiple solid bodies created during regeneration of a multibody macro feature."""
		self._instance.EnableMultiBodyConsume = value

	@property
	def feature_transform(self):
		"""Gets and sets the macro feature transform."""
		return self._instance.FeatureTransform

	@feature_transform.setter
	def feature_transform(self, value):
		"""Gets and sets the macro feature transform."""
		self._instance.FeatureTransform = value

	@property
	def icon_files(self):
		"""Gets or sets the file names for the icons for this macro feature."""
		return self._instance.IconFiles

	@icon_files.setter
	def icon_files(self, value):
		"""Gets or sets the file names for the icons for this macro feature."""
		self._instance.IconFiles = value

	@property
	def macro_file_embedded(self):
		"""Gets whether the macro file is embedded ini the model with the macro feature."""
		return self._instance.MacroFileEmbedded

	@macro_file_embedded.setter
	def macro_file_embedded(self, value):
		"""Gets whether the macro file is embedded ini the model with the macro feature."""
		self._instance.MacroFileEmbedded = value

	@property
	def macro_file_name(self):
		"""Gets or sets the path and file name for the macro for the macro feature."""
		return self._instance.MacroFileName

	@macro_file_name.setter
	def macro_file_name(self, value):
		"""Gets or sets the path and file name for the macro for the macro feature."""
		self._instance.MacroFileName = value

	@property
	def module_name(self):
		"""Gets or sets the name of a module in the macro for this macro feature."""
		return self._instance.ModuleName

	@module_name.setter
	def module_name(self, value):
		"""Gets or sets the name of a module in the macro for this macro feature."""
		self._instance.ModuleName = value

	@property
	def parents(self):
		"""Gets or sets the parent features for this macro feature."""
		return self._instance.Parents

	@parents.setter
	def parents(self, value):
		"""Gets or sets the parent features for this macro feature."""
		self._instance.Parents = value

	@property
	def pattern_transform(self):
		"""Gets the pattern transform."""
		return self._instance.PatternTransform

	@pattern_transform.setter
	def pattern_transform(self, value):
		"""Gets the pattern transform."""
		self._instance.PatternTransform = value

	@property
	def procedure_name(self):
		"""Gets or sets a name of the procedure in the macro for this macro feature."""
		return self._instance.ProcedureName

	@procedure_name.setter
	def procedure_name(self, value):
		"""Gets or sets a name of the procedure in the macro for this macro feature."""
		self._instance.ProcedureName = value

	@property
	def property_manager_handle_macro_file_name(self):
		"""Gets or sets the path and file name for the macro file from or to the PropertyManager handle for this macro feature."""
		return self._instance.PropertyManagerHandleMacroFileName

	@property_manager_handle_macro_file_name.setter
	def property_manager_handle_macro_file_name(self, value):
		"""Gets or sets the path and file name for the macro file from or to the PropertyManager handle for this macro feature."""
		self._instance.PropertyManagerHandleMacroFileName = value

	@property
	def property_manager_handle_module_name(self):
		"""Gets or sets the name of the module in the macro file from or to the PropertyManager handle."""
		return self._instance.PropertyManagerHandleModuleName

	@property_manager_handle_module_name.setter
	def property_manager_handle_module_name(self, value):
		"""Gets or sets the name of the module in the macro file from or to the PropertyManager handle."""
		self._instance.PropertyManagerHandleModuleName = value

	@property
	def property_manager_handle_procedure_name(self):
		"""Gets or sets the name of the procedure in the macro file from or to the PropertyManager handle."""
		return self._instance.PropertyManagerHandleProcedureName

	@property_manager_handle_procedure_name.setter
	def property_manager_handle_procedure_name(self, value):
		"""Gets or sets the name of the procedure in the macro file from or to the PropertyManager handle."""
		self._instance.PropertyManagerHandleProcedureName = value

	@property
	def provider(self):
		"""Gets or sets the error message to display in the What's Wrong dialog when a non-embedded macro feature fails to rebuild due to missing files."""
		return self._instance.Provider

	@provider.setter
	def provider(self, value):
		"""Gets or sets the error message to display in the What's Wrong dialog when a non-embedded macro feature fails to rebuild due to missing files."""
		self._instance.Provider = value

	@property
	def security_handle_macro_file_name(self):
		"""Gets or sets the name of the procedure in the macro file from or to the security handle."""
		return self._instance.SecurityHandleMacroFileName

	@security_handle_macro_file_name.setter
	def security_handle_macro_file_name(self, value):
		"""Gets or sets the name of the procedure in the macro file from or to the security handle."""
		self._instance.SecurityHandleMacroFileName = value

	@property
	def security_handle_module_name(self):
		"""Gets and sets the name of the module in the macro file from or to the security handle."""
		return self._instance.SecurityHandleModuleName

	@security_handle_module_name.setter
	def security_handle_module_name(self, value):
		"""Gets and sets the name of the module in the macro file from or to the security handle."""
		self._instance.SecurityHandleModuleName = value

	@property
	def security_handle_procedure_name(self):
		"""Gets or sets the name of the procedure in the macro file from or to the security handle."""
		return self._instance.SecurityHandleProcedureName

	@security_handle_procedure_name.setter
	def security_handle_procedure_name(self, value):
		"""Gets or sets the name of the procedure in the macro file from or to the security handle."""
		self._instance.SecurityHandleProcedureName = value

	@property
	def access_selections(self):
		"""Gains access to the selections associated with this macro feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections associated with this macro feature."""
		self._instance.AccessSelections = value

	@property
	def embed_macro_file(self):
		"""Sets whether to embed the macro file in the model with the macro feature."""
		return self._instance.EmbedMacroFile

	@embed_macro_file.setter
	def embed_macro_file(self, value):
		"""Sets whether to embed the macro file in the model with the macro feature."""
		self._instance.EmbedMacroFile = value

	@property
	def get_base_name(self):
		"""Gets the name of the base feature for this macro feature."""
		return self._instance.GetBaseName

	@get_base_name.setter
	def get_base_name(self, value):
		"""Gets the name of the base feature for this macro feature."""
		self._instance.GetBaseName = value

	@property
	def get_display_dimension_count(self):
		"""Gets the number of display dimensions for this macro feature."""
		return self._instance.GetDisplayDimensionCount

	@get_display_dimension_count.setter
	def get_display_dimension_count(self, value):
		"""Gets the number of display dimensions for this macro feature."""
		self._instance.GetDisplayDimensionCount = value

	@property
	def get_display_dimensions(self):
		"""Gets the display dimensions for this macro feature."""
		return self._instance.GetDisplayDimensions

	@get_display_dimensions.setter
	def get_display_dimensions(self, value):
		"""Gets the display dimensions for this macro feature."""
		self._instance.GetDisplayDimensions = value

	@property
	def get_double_by_name(self):
		"""Gets a double value by parameter name."""
		return self._instance.GetDoubleByName

	@get_double_by_name.setter
	def get_double_by_name(self, value):
		"""Gets a double value by parameter name."""
		self._instance.GetDoubleByName = value

	@property
	def get_edge_id_type(self):
		"""Gets the ID type of the specified edge for the macro feature."""
		return self._instance.GetEdgeIdType

	@get_edge_id_type.setter
	def get_edge_id_type(self, value):
		"""Gets the ID type of the specified edge for the macro feature."""
		self._instance.GetEdgeIdType = value

	@property
	def get_edge_user_id(self):
		"""Gets the user-defined IDs for the specified edge for the macro feature."""
		return self._instance.GetEdgeUserId

	@get_edge_user_id.setter
	def get_edge_user_id(self, value):
		"""Gets the user-defined IDs for the specified edge for the macro feature."""
		self._instance.GetEdgeUserId = value

	@property
	def get_edit_bodies_count(self):
		"""Gets the number of bodies to be modified by this macro feature."""
		return self._instance.GetEditBodiesCount

	@get_edit_bodies_count.setter
	def get_edit_bodies_count(self, value):
		"""Gets the number of bodies to be modified by this macro feature."""
		self._instance.GetEditBodiesCount = value

	@property
	def get_edit_target_transform(self):
		"""Gets the transform of the component where the macro feature resides if at least one selection in the macro feature belongs to a different component."""
		return self._instance.GetEditTargetTransform

	@get_edit_target_transform.setter
	def get_edit_target_transform(self, value):
		"""Gets the transform of the component where the macro feature resides if at least one selection in the macro feature belongs to a different component."""
		self._instance.GetEditTargetTransform = value

	@property
	def get_entities_need_user_id(self):
		"""Gets a list of faces and edges that need be assigned user IDs for the macro feature."""
		return self._instance.GetEntitiesNeedUserId

	@get_entities_need_user_id.setter
	def get_entities_need_user_id(self, value):
		"""Gets a list of faces and edges that need be assigned user IDs for the macro feature."""
		self._instance.GetEntitiesNeedUserId = value

	@property
	def get_entities_need_user_id_count(self):
		"""Gets the number of faces and edges that need to be assigned user IDs for the macro feature."""
		return self._instance.GetEntitiesNeedUserIdCount

	@get_entities_need_user_id_count.setter
	def get_entities_need_user_id_count(self, value):
		"""Gets the number of faces and edges that need to be assigned user IDs for the macro feature."""
		self._instance.GetEntitiesNeedUserIdCount = value

	@property
	def get_face_id_type(self):
		"""Gets the ID type from the face for the macro feature."""
		return self._instance.GetFaceIdType

	@get_face_id_type.setter
	def get_face_id_type(self, value):
		"""Gets the ID type from the face for the macro feature."""
		self._instance.GetFaceIdType = value

	@property
	def get_face_user_id(self):
		"""Gets the user-defined IDs for the specified face."""
		return self._instance.GetFaceUserId

	@get_face_user_id.setter
	def get_face_user_id(self, value):
		"""Gets the user-defined IDs for the specified face."""
		self._instance.GetFaceUserId = value

	@property
	def get_icon_file_count(self):
		"""Gets the number of the files for the icons for this macro feature."""
		return self._instance.GetIconFileCount

	@get_icon_file_count.setter
	def get_icon_file_count(self, value):
		"""Gets the number of the files for the icons for this macro feature."""
		self._instance.GetIconFileCount = value

	@property
	def get_integer_by_name(self):
		"""Gets an integer value by parameter name."""
		return self._instance.GetIntegerByName

	@get_integer_by_name.setter
	def get_integer_by_name(self, value):
		"""Gets an integer value by parameter name."""
		self._instance.GetIntegerByName = value

	@property
	def get_module_count(self):
		"""Gets the number of modules for the macro feature."""
		return self._instance.GetModuleCount

	@get_module_count.setter
	def get_module_count(self, value):
		"""Gets the number of modules for the macro feature."""
		self._instance.GetModuleCount = value

	@property
	def get_module_names(self):
		"""Gets the names of the modules in the macro for the macro feature."""
		return self._instance.GetModuleNames

	@get_module_names.setter
	def get_module_names(self, value):
		"""Gets the names of the modules in the macro for the macro feature."""
		self._instance.GetModuleNames = value

	@property
	def get_parameter_count(self):
		"""Gets the number of user-defined parameters."""
		return self._instance.GetParameterCount

	@get_parameter_count.setter
	def get_parameter_count(self, value):
		"""Gets the number of user-defined parameters."""
		self._instance.GetParameterCount = value

	@property
	def get_parameters(self):
		"""Gets the user-defined parameters."""
		return self._instance.GetParameters

	@get_parameters.setter
	def get_parameters(self, value):
		"""Gets the user-defined parameters."""
		self._instance.GetParameters = value

	@property
	def get_parents_count(self):
		"""Gets the number of parent features for this macro feature."""
		return self._instance.GetParentsCount

	@get_parents_count.setter
	def get_parents_count(self, value):
		"""Gets the number of parent features for this macro feature."""
		self._instance.GetParentsCount = value

	@property
	def get_procedure_count(self):
		"""Gets the number of procedures in the specified module in the macro for this macro feature."""
		return self._instance.GetProcedureCount

	@get_procedure_count.setter
	def get_procedure_count(self, value):
		"""Gets the number of procedures in the specified module in the macro for this macro feature."""
		self._instance.GetProcedureCount = value

	@property
	def get_procedure_names(self):
		"""Gets the names of the procedures in the specified module for the macro for the macro feature."""
		return self._instance.GetProcedureNames

	@get_procedure_names.setter
	def get_procedure_names(self, value):
		"""Gets the names of the procedures in the specified module for the macro for the macro feature."""
		self._instance.GetProcedureNames = value

	@property
	def get_prog_id(self):
		"""Gets the version-independent program ID that is valid for this COM feature."""
		return self._instance.GetProgId

	@get_prog_id.setter
	def get_prog_id(self, value):
		"""Gets the version-independent program ID that is valid for this COM feature."""
		self._instance.GetProgId = value

	@property
	def get_property_manager_handle_module_count(self):
		"""Gets the number of modules in the macro from the PropertyManager handle for the macro feature."""
		return self._instance.GetPropertyManagerHandleModuleCount

	@get_property_manager_handle_module_count.setter
	def get_property_manager_handle_module_count(self, value):
		"""Gets the number of modules in the macro from the PropertyManager handle for the macro feature."""
		self._instance.GetPropertyManagerHandleModuleCount = value

	@property
	def get_property_manager_handle_module_names(self):
		"""Gets the names of the modules in the macro from the PropertyManager handle for the macro feature."""
		return self._instance.GetPropertyManagerHandleModuleNames

	@get_property_manager_handle_module_names.setter
	def get_property_manager_handle_module_names(self, value):
		"""Gets the names of the modules in the macro from the PropertyManager handle for the macro feature."""
		self._instance.GetPropertyManagerHandleModuleNames = value

	@property
	def get_property_manager_handle_procedure_count(self):
		"""Gets the number of procedures in the specified module in the macro from the PropertyManager handle for this macro feature."""
		return self._instance.GetPropertyManagerHandleProcedureCount

	@get_property_manager_handle_procedure_count.setter
	def get_property_manager_handle_procedure_count(self, value):
		"""Gets the number of procedures in the specified module in the macro from the PropertyManager handle for this macro feature."""
		self._instance.GetPropertyManagerHandleProcedureCount = value

	@property
	def get_property_manager_handle_procedure_names(self):
		"""Gets the names of the procedures in the specified module in the macro from the PropertyManager handle for the macro feature."""
		return self._instance.GetPropertyManagerHandleProcedureNames

	@get_property_manager_handle_procedure_names.setter
	def get_property_manager_handle_procedure_names(self, value):
		"""Gets the names of the procedures in the specified module in the macro from the PropertyManager handle for the macro feature."""
		self._instance.GetPropertyManagerHandleProcedureNames = value

	@property
	def get_selection_count(self):
		"""Gets the number of selected objects for the macro feature."""
		return self._instance.GetSelectionCount

	@get_selection_count.setter
	def get_selection_count(self, value):
		"""Gets the number of selected objects for the macro feature."""
		self._instance.GetSelectionCount = value

	@property
	def get_selections(self):
		"""Gets the selected objects for the macro feature."""
		return self._instance.GetSelections3

	@get_selections.setter
	def get_selections(self, value):
		"""Gets the selected objects for the macro feature."""
		self._instance.GetSelections3 = value

	@property
	def get_string_by_name(self):
		"""Gets a string value by the name of the parameter for the macro feature."""
		return self._instance.GetStringByName

	@get_string_by_name.setter
	def get_string_by_name(self, value):
		"""Gets a string value by the name of the parameter for the macro feature."""
		self._instance.GetStringByName = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections associated with this macro feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections associated with this macro feature."""
		self._instance.IAccessSelections = value

	@property
	def i_add_display_dimensions(self):
		"""Adds the specified display dimensions to this macro feature."""
		return self._instance.IAddDisplayDimensions

	@i_add_display_dimensions.setter
	def i_add_display_dimensions(self, value):
		"""Adds the specified display dimensions to this macro feature."""
		self._instance.IAddDisplayDimensions = value

	@property
	def i_get_display_dimensions(self):
		"""Gets the display dimensions for this macro feature."""
		return self._instance.IGetDisplayDimensions

	@i_get_display_dimensions.setter
	def i_get_display_dimensions(self, value):
		"""Gets the display dimensions for this macro feature."""
		self._instance.IGetDisplayDimensions = value

	@property
	def i_get_edit_bodies(self):
		"""Gets the bodies to be modified by this macro feature."""
		return self._instance.IGetEditBodies

	@i_get_edit_bodies.setter
	def i_get_edit_bodies(self, value):
		"""Gets the bodies to be modified by this macro feature."""
		self._instance.IGetEditBodies = value

	@property
	def i_get_entities_need_user_id(self):
		"""Gets a list of faces and edges that need be assigned user IDs for the macro feature."""
		return self._instance.IGetEntitiesNeedUserId

	@i_get_entities_need_user_id.setter
	def i_get_entities_need_user_id(self, value):
		"""Gets a list of faces and edges that need be assigned user IDs for the macro feature."""
		self._instance.IGetEntitiesNeedUserId = value

	@property
	def i_get_icon_files(self):
		"""Gets the file names for the icons for this macro feature."""
		return self._instance.IGetIconFiles

	@i_get_icon_files.setter
	def i_get_icon_files(self, value):
		"""Gets the file names for the icons for this macro feature."""
		self._instance.IGetIconFiles = value

	@property
	def i_get_module_names(self):
		"""Gets the names of the modules in the macro for the macro feature."""
		return self._instance.IGetModuleNames

	@i_get_module_names.setter
	def i_get_module_names(self, value):
		"""Gets the names of the modules in the macro for the macro feature."""
		self._instance.IGetModuleNames = value

	@property
	def i_get_parameters(self):
		"""Gets the user-defined parameters."""
		return self._instance.IGetParameters

	@i_get_parameters.setter
	def i_get_parameters(self, value):
		"""Gets the user-defined parameters."""
		self._instance.IGetParameters = value

	@property
	def i_get_parents(self):
		"""Gets the parent features of this macro feature."""
		return self._instance.IGetParents

	@i_get_parents.setter
	def i_get_parents(self, value):
		"""Gets the parent features of this macro feature."""
		self._instance.IGetParents = value

	@property
	def i_get_procedure_names(self):
		"""Gets the names of the procedures in the specified module in the macro for the macro feature."""
		return self._instance.IGetProcedureNames

	@i_get_procedure_names.setter
	def i_get_procedure_names(self, value):
		"""Gets the names of the procedures in the specified module in the macro for the macro feature."""
		self._instance.IGetProcedureNames = value

	@property
	def i_get_property_manager_handle_module_names(self):
		"""Gets the names of the modules in the macro from the PropertyManager handle for the macro feature."""
		return self._instance.IGetPropertyManagerHandleModuleNames

	@i_get_property_manager_handle_module_names.setter
	def i_get_property_manager_handle_module_names(self, value):
		"""Gets the names of the modules in the macro from the PropertyManager handle for the macro feature."""
		self._instance.IGetPropertyManagerHandleModuleNames = value

	@property
	def i_get_property_manager_handle_procedure_names(self):
		"""Gets the names of the procedures in the specified module in the macro from the PropertyManager handle for the macro feature."""
		return self._instance.IGetPropertyManagerHandleProcedureNames

	@i_get_property_manager_handle_procedure_names.setter
	def i_get_property_manager_handle_procedure_names(self, value):
		"""Gets the names of the procedures in the specified module in the macro from the PropertyManager handle for the macro feature."""
		self._instance.IGetPropertyManagerHandleProcedureNames = value

	@property
	def i_get_selections(self):
		"""Gets the selected objects for the macro feature."""
		return self._instance.IGetSelections3

	@i_get_selections.setter
	def i_get_selections(self, value):
		"""Gets the selected objects for the macro feature."""
		self._instance.IGetSelections3 = value

	@property
	def is_c_o_m_feature(self):
		"""Gets whether the feature is a COM feature."""
		return self._instance.IsCOMFeature

	@is_c_o_m_feature.setter
	def is_c_o_m_feature(self, value):
		"""Gets whether the feature is a COM feature."""
		self._instance.IsCOMFeature = value

	@property
	def i_set_edit_bodies(self):
		"""Sets the bodies to be modified by this macro feature."""
		return self._instance.ISetEditBodies

	@i_set_edit_bodies.setter
	def i_set_edit_bodies(self, value):
		"""Sets the bodies to be modified by this macro feature."""
		self._instance.ISetEditBodies = value

	@property
	def i_set_icon_files(self):
		"""Sets the file names for the icons for this macro feature."""
		return self._instance.ISetIconFiles

	@i_set_icon_files.setter
	def i_set_icon_files(self, value):
		"""Sets the file names for the icons for this macro feature."""
		self._instance.ISetIconFiles = value

	@property
	def i_set_parameters(self):
		"""Sets the user-defined parameters."""
		return self._instance.ISetParameters

	@i_set_parameters.setter
	def i_set_parameters(self, value):
		"""Sets the user-defined parameters."""
		self._instance.ISetParameters = value

	@property
	def i_set_parents(self):
		"""Sets the parent features for this macro feature."""
		return self._instance.ISetParents

	@i_set_parents.setter
	def i_set_parents(self, value):
		"""Sets the parent features for this macro feature."""
		self._instance.ISetParents = value

	@property
	def i_set_selections(self):
		"""Sets the selected objects for the macro feature."""
		return self._instance.ISetSelections2

	@i_set_selections.setter
	def i_set_selections(self, value):
		"""Sets the selected objects for the macro feature."""
		self._instance.ISetSelections2 = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections associated with this macro feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections associated with this macro feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_double_by_name(self):
		"""Sets a double value by parameter name for the macro feature."""
		return self._instance.SetDoubleByName

	@set_double_by_name.setter
	def set_double_by_name(self, value):
		"""Sets a double value by parameter name for the macro feature."""
		self._instance.SetDoubleByName = value

	@property
	def set_edge_user_id(self):
		"""Sets the user-defined IDs for the specified edge for the macro feature."""
		return self._instance.SetEdgeUserId

	@set_edge_user_id.setter
	def set_edge_user_id(self, value):
		"""Sets the user-defined IDs for the specified edge for the macro feature."""
		self._instance.SetEdgeUserId = value

	@property
	def set_face_user_id(self):
		"""Sets user-defined IDs for the face for the macro feature."""
		return self._instance.SetFaceUserId

	@set_face_user_id.setter
	def set_face_user_id(self, value):
		"""Sets user-defined IDs for the face for the macro feature."""
		self._instance.SetFaceUserId = value

	@property
	def set_integer_by_name(self):
		"""Sets an integer value by parameter name."""
		return self._instance.SetIntegerByName

	@set_integer_by_name.setter
	def set_integer_by_name(self, value):
		"""Sets an integer value by parameter name."""
		self._instance.SetIntegerByName = value

	@property
	def set_parameters(self):
		"""Sets the user-defined parameters."""
		return self._instance.SetParameters

	@set_parameters.setter
	def set_parameters(self, value):
		"""Sets the user-defined parameters."""
		self._instance.SetParameters = value

	@property
	def set_prog_id(self):
		"""Sets the version-independent program ID that is valid for this COM feature."""
		return self._instance.SetProgId

	@set_prog_id.setter
	def set_prog_id(self, value):
		"""Sets the version-independent program ID that is valid for this COM feature."""
		self._instance.SetProgId = value

	@property
	def set_selections(self):
		"""Sets the selected objects for the macro feature."""
		return self._instance.SetSelections2

	@set_selections.setter
	def set_selections(self, value):
		"""Sets the selected objects for the macro feature."""
		self._instance.SetSelections2 = value

	@property
	def set_string_by_name(self):
		"""Sets a string value by parameter name."""
		return self._instance.SetStringByName

	@set_string_by_name.setter
	def set_string_by_name(self, value):
		"""Sets a string value by parameter name."""
		self._instance.SetStringByName = value

