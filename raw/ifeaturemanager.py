# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html
class IFeatureManager:
	def __init__(self, parent=None):
		self._instance = parent

	def document(self):
		"""Gets the specified document."""
		# return self._instance.Document
		raise NotImplemented

	@property
	def enable_feature_tree(self):
		"""Gets or sets whether or not to update the FeatureManager design tree."""
		return self._instance.EnableFeatureTree

	@enable_feature_tree.setter
	def enable_feature_tree(self, value):
		"""Gets or sets whether or not to update the FeatureManager design tree."""
		self._instance.EnableFeatureTree = value

	@property
	def enable_feature_tree_window(self):
		"""Gets or sets whether the FeatureManager design tree is enabled or not."""
		return self._instance.EnableFeatureTreeWindow

	@enable_feature_tree_window.setter
	def enable_feature_tree_window(self, value):
		"""Gets or sets whether the FeatureManager design tree is enabled or not."""
		self._instance.EnableFeatureTreeWindow = value

	@property
	def feature_name(self):
		"""Gets the feature name for the specified feature ID."""
		return self._instance.FeatureName

	@feature_name.setter
	def feature_name(self, value):
		"""Gets the feature name for the specified feature ID."""
		self._instance.FeatureName = value

	@property
	def feature_statistics(self):
		"""Gets statistics about the features in a part document."""
		return self._instance.FeatureStatistics

	@feature_statistics.setter
	def feature_statistics(self, value):
		"""Gets statistics about the features in a part document."""
		self._instance.FeatureStatistics = value

	@property
	def group_component_instances(self):
		"""Gets or sets whether to group the same components in the same configuration in an assembly into a folder in the FeatureManager design tree."""
		return self._instance.GroupComponentInstances

	@group_component_instances.setter
	def group_component_instances(self, value):
		"""Gets or sets whether to group the same components in the same configuration in an assembly into a folder in the FeatureManager design tree."""
		self._instance.GroupComponentInstances = value

	@property
	def move_size_features(self):
		"""Shows or hides the feature Instant3D."""
		return self._instance.MoveSizeFeatures

	@move_size_features.setter
	def move_size_features(self, value):
		"""Shows or hides the feature Instant3D."""
		self._instance.MoveSizeFeatures = value

	@property
	def show_component_configuration_descriptions(self):
		"""Gets or sets whether to show the active configuration's component configuration descriptions in the FeatureManager design tree."""
		return self._instance.ShowComponentConfigurationDescriptions

	@show_component_configuration_descriptions.setter
	def show_component_configuration_descriptions(self, value):
		"""Gets or sets whether to show the active configuration's component configuration descriptions in the FeatureManager design tree."""
		self._instance.ShowComponentConfigurationDescriptions = value

	@property
	def show_component_configuration_names(self):
		"""Gets or sets whether to show the active configuration's component configuration names in the FeatureManager design tree."""
		return self._instance.ShowComponentConfigurationNames

	@show_component_configuration_names.setter
	def show_component_configuration_names(self, value):
		"""Gets or sets whether to show the active configuration's component configuration names in the FeatureManager design tree."""
		self._instance.ShowComponentConfigurationNames = value

	@property
	def show_component_descriptions(self):
		"""Gets or sets whether to show the component configuration descriptions in the FeatureManager design tree."""
		return self._instance.ShowComponentDescriptions

	@show_component_descriptions.setter
	def show_component_descriptions(self, value):
		"""Gets or sets whether to show the component configuration descriptions in the FeatureManager design tree."""
		self._instance.ShowComponentDescriptions = value

	@property
	def show_component_names(self):
		"""Gets or sets whether to show the component configuration names in the FeatureManager design tree."""
		return self._instance.ShowComponentNames

	@show_component_names.setter
	def show_component_names(self, value):
		"""Gets or sets whether to show the component configuration names in the FeatureManager design tree."""
		self._instance.ShowComponentNames = value

	@property
	def show_display_state_names(self):
		"""Gets or sets whether to show the display state names in the FeatureManager design tree."""
		return self._instance.ShowDisplayStateNames

	@show_display_state_names.setter
	def show_display_state_names(self, value):
		"""Gets or sets whether to show the display state names in the FeatureManager design tree."""
		self._instance.ShowDisplayStateNames = value

	@property
	def show_feature_description(self):
		"""Gets or sets whether to show the description of the feature in the FeatureManager design tree."""
		return self._instance.ShowFeatureDescription

	@show_feature_description.setter
	def show_feature_description(self, value):
		"""Gets or sets whether to show the description of the feature in the FeatureManager design tree."""
		self._instance.ShowFeatureDescription = value

	@property
	def show_feature_details(self):
		"""Gets or sets whether to show the feature details in the FeatureManager design tree."""
		return self._instance.ShowFeatureDetails

	@show_feature_details.setter
	def show_feature_details(self, value):
		"""Gets or sets whether to show the feature details in the FeatureManager design tree."""
		self._instance.ShowFeatureDetails = value

	@property
	def show_feature_name(self):
		"""Gets or sets whether to show the name of the feature in the FeatureManager design tree."""
		return self._instance.ShowFeatureName

	@show_feature_name.setter
	def show_feature_name(self, value):
		"""Gets or sets whether to show the name of the feature in the FeatureManager design tree."""
		self._instance.ShowFeatureName = value

	@property
	def show_hierarchy_only(self):
		"""Gets or sets whether to show only the hierarchy in the FeatureManager design tree."""
		return self._instance.ShowHierarchyOnly

	@show_hierarchy_only.setter
	def show_hierarchy_only(self, value):
		"""Gets or sets whether to show only the hierarchy in the FeatureManager design tree."""
		self._instance.ShowHierarchyOnly = value

	@property
	def solid_for_trim(self):
		"""Gets or sets whether a surface trim feature is a solid body or a surface body."""
		return self._instance.SolidForTrim

	@solid_for_trim.setter
	def solid_for_trim(self, value):
		"""Gets or sets whether a surface trim feature is a solid body or a surface body."""
		self._instance.SolidForTrim = value

	@property
	def view_dependencies(self):
		"""Gets or sets whether to view the FeatureManager design tree by its dependencies."""
		return self._instance.ViewDependencies

	@view_dependencies.setter
	def view_dependencies(self, value):
		"""Gets or sets whether to view the FeatureManager design tree by its dependencies."""
		self._instance.ViewDependencies = value

	@property
	def view_features(self):
		"""Gets or sets whether to view the FeatureManager design tree by its features."""
		return self._instance.ViewFeatures

	@view_features.setter
	def view_features(self, value):
		"""Gets or sets whether to view the FeatureManager design tree by its features."""
		self._instance.ViewFeatures = value

	@property
	def add_corner_relief_corner(self):
		"""Adds the bend corner of two selected faces of a sheet metal body to the set of corners to which to apply a corner relief."""
		return self._instance.AddCornerReliefCorner

	@add_corner_relief_corner.setter
	def add_corner_relief_corner(self, value):
		"""Adds the bend corner of two selected faces of a sheet metal body to the set of corners to which to apply a corner relief."""
		self._instance.AddCornerReliefCorner = value

	@property
	def add_corner_relief_type(self):
		"""Specifies the type of corner relief to apply to the specified corner of the selected sheet metal body."""
		return self._instance.AddCornerReliefType

	@add_corner_relief_type.setter
	def add_corner_relief_type(self, value):
		"""Specifies the type of corner relief to apply to the specified corner of the selected sheet metal body."""
		self._instance.AddCornerReliefType = value

	@property
	def add_variable_pitch_helix_first_pitch_and_diameter(self):
		"""Adds the first segment to a variable-pitch helix."""
		return self._instance.AddVariablePitchHelixFirstPitchAndDiameter

	@add_variable_pitch_helix_first_pitch_and_diameter.setter
	def add_variable_pitch_helix_first_pitch_and_diameter(self, value):
		"""Adds the first segment to a variable-pitch helix."""
		self._instance.AddVariablePitchHelixFirstPitchAndDiameter = value

	@property
	def add_variable_pitch_helix_segment(self):
		"""Adds a segment to a variable-pitch helix."""
		return self._instance.AddVariablePitchHelixSegment

	@add_variable_pitch_helix_segment.setter
	def add_variable_pitch_helix_segment(self, value):
		"""Adds a segment to a variable-pitch helix."""
		self._instance.AddVariablePitchHelixSegment = value

	@property
	def advanced_hole(self):
		"""Creates an Advanced Hole feature."""
		return self._instance.AdvancedHole2

	@advanced_hole.setter
	def advanced_hole(self, value):
		"""Creates an Advanced Hole feature."""
		self._instance.AdvancedHole2 = value

	@property
	def create_coordinate_system(self):
		"""Creates a coordinate system feature."""
		return self._instance.CreateCoordinateSystem

	@create_coordinate_system.setter
	def create_coordinate_system(self, value):
		"""Creates a coordinate system feature."""
		self._instance.CreateCoordinateSystem = value

	@property
	def create_custom_bend_allowance(self):
		"""Creates a custom bend allowance to use when creating a sheet metal feature."""
		return self._instance.CreateCustomBendAllowance

	@create_custom_bend_allowance.setter
	def create_custom_bend_allowance(self, value):
		"""Creates a custom bend allowance to use when creating a sheet metal feature."""
		self._instance.CreateCustomBendAllowance = value

	@property
	def create_definition(self):
		"""Creates a feature data object of the specified type."""
		return self._instance.CreateDefinition

	@create_definition.setter
	def create_definition(self, value):
		"""Creates a feature data object of the specified type."""
		self._instance.CreateDefinition = value

	@property
	def create_feature(self):
		"""Creates the specified feature."""
		return self._instance.CreateFeature

	@create_feature.setter
	def create_feature(self, value):
		"""Creates the specified feature."""
		self._instance.CreateFeature = value

	@property
	def create_form_tool(self):
		"""Creates a forming tool feature with the specified point of insertion in a sheet metal part."""
		return self._instance.CreateFormTool2

	@create_form_tool.setter
	def create_form_tool(self, value):
		"""Creates a forming tool feature with the specified point of insertion in a sheet metal part."""
		self._instance.CreateFormTool2 = value

	@property
	def create_save_body_feature(self):
		"""Creates a Save Bodies feature and creates part and assembly documents of the save bodies."""
		return self._instance.CreateSaveBodyFeature

	@create_save_body_feature.setter
	def create_save_body_feature(self, value):
		"""Creates a Save Bodies feature and creates part and assembly documents of the save bodies."""
		self._instance.CreateSaveBodyFeature = value

	@property
	def create_structural_member_group(self):
		"""Creates a weldment structural-member group."""
		return self._instance.CreateStructuralMemberGroup

	@create_structural_member_group.setter
	def create_structural_member_group(self, value):
		"""Creates a weldment structural-member group."""
		self._instance.CreateStructuralMemberGroup = value

	@property
	def draft_xpert_change(self):
		"""Changes the parameters on the selected drafted faces, regardless of whether the drafted faces were created manually or with DraftXpert, provided that DraftXpert can process them."""
		return self._instance.DraftXpertChange

	@draft_xpert_change.setter
	def draft_xpert_change(self, value):
		"""Changes the parameters on the selected drafted faces, regardless of whether the drafted faces were created manually or with DraftXpert, provided that DraftXpert can process them."""
		self._instance.DraftXpertChange = value

	@property
	def draft_xpert_remove(self):
		"""Deletes the draft on the selected faces. If all the faces of a draft are selected, then this method deletes the draft feature; if not, then this method edits the draft feature and removes the selected face references from it."""
		return self._instance.DraftXpertRemove

	@draft_xpert_remove.setter
	def draft_xpert_remove(self, value):
		"""Deletes the draft on the selected faces. If all the faces of a draft are selected, then this method deletes the draft feature; if not, then this method edits the draft feature and removes the selected face references from it."""
		self._instance.DraftXpertRemove = value

	@property
	def edit_delete_face(self):
		"""Edits a DeleteFace feature."""
		return self._instance.EditDeleteFace

	@edit_delete_face.setter
	def edit_delete_face(self, value):
		"""Edits a DeleteFace feature."""
		self._instance.EditDeleteFace = value

	@property
	def edit_freeze(self):
		"""Moves the freeze bar to the specified location in the FeatureManager design tree."""
		return self._instance.EditFreeze2

	@edit_freeze.setter
	def edit_freeze(self, value):
		"""Moves the freeze bar to the specified location in the FeatureManager design tree."""
		self._instance.EditFreeze2 = value

	@property
	def edit_reference_point(self):
		"""Edits the selected reference points."""
		return self._instance.EditReferencePoint

	@edit_reference_point.setter
	def edit_reference_point(self, value):
		"""Edits the selected reference points."""
		self._instance.EditReferencePoint = value

	@property
	def edit_rollback(self):
		"""Rolls back or forward the rollback bar to a specific location in the FeatureManager design tree."""
		return self._instance.EditRollback

	@edit_rollback.setter
	def edit_rollback(self, value):
		"""Rolls back or forward the rollback bar to a specific location in the FeatureManager design tree."""
		self._instance.EditRollback = value

	@property
	def end_variable_pitch_helix(self):
		"""Ends and inserts a variable-pitch helix."""
		return self._instance.EndVariablePitchHelix

	@end_variable_pitch_helix.setter
	def end_variable_pitch_helix(self, value):
		"""Ends and inserts a variable-pitch helix."""
		self._instance.EndVariablePitchHelix = value

	@property
	def expand_feature(self):
		"""Expands the specified component in the specified FeatureManager design tree pane."""
		return self._instance.ExpandFeature

	@expand_feature.setter
	def expand_feature(self, value):
		"""Expands the specified component in the specified FeatureManager design tree pane."""
		self._instance.ExpandFeature = value

	@property
	def feature_boss_thicken(self):
		"""Thickens the selected reference surface, and then generates a boss."""
		return self._instance.FeatureBossThicken

	@feature_boss_thicken.setter
	def feature_boss_thicken(self, value):
		"""Thickens the selected reference surface, and then generates a boss."""
		self._instance.FeatureBossThicken = value

	@property
	def feature_cut(self):
		"""Creates a cut extrude feature."""
		return self._instance.FeatureCut4

	@feature_cut.setter
	def feature_cut(self, value):
		"""Creates a cut extrude feature."""
		self._instance.FeatureCut4 = value

	@property
	def feature_cut_thicken(self):
		"""Thickens the selected reference surface feature, and then generates a cut."""
		return self._instance.FeatureCutThicken

	@feature_cut_thicken.setter
	def feature_cut_thicken(self, value):
		"""Thickens the selected reference surface feature, and then generates a cut."""
		self._instance.FeatureCutThicken = value

	@property
	def feature_cut_thin(self):
		"""Inserts a thin cut extrude feature."""
		return self._instance.FeatureCutThin2

	@feature_cut_thin.setter
	def feature_cut_thin(self, value):
		"""Inserts a thin cut extrude feature."""
		self._instance.FeatureCutThin2 = value

	@property
	def feature_dimension_pattern(self):
		"""Not implemented."""
		return self._instance.FeatureDimensionPattern

	@feature_dimension_pattern.setter
	def feature_dimension_pattern(self, value):
		"""Not implemented."""
		self._instance.FeatureDimensionPattern = value

	@property
	def feature_extru_ref_surface(self):
		"""Inserts an extruded surface."""
		return self._instance.FeatureExtruRefSurface3

	@feature_extru_ref_surface.setter
	def feature_extru_ref_surface(self, value):
		"""Inserts an extruded surface."""
		self._instance.FeatureExtruRefSurface3 = value

	@property
	def feature_extrusion(self):
		"""Creates an extruded feature."""
		return self._instance.FeatureExtrusion3

	@feature_extrusion.setter
	def feature_extrusion(self, value):
		"""Creates an extruded feature."""
		self._instance.FeatureExtrusion3 = value

	@property
	def feature_extrusion_thin(self):
		"""Creates an extruded thin feature."""
		return self._instance.FeatureExtrusionThin2

	@feature_extrusion_thin.setter
	def feature_extrusion_thin(self, value):
		"""Creates an extruded thin feature."""
		self._instance.FeatureExtrusionThin2 = value

	@property
	def feature_fillet(self):
		"""Creates a fillet feature for selected edges and control point references."""
		return self._instance.FeatureFillet3

	@feature_fillet.setter
	def feature_fillet(self, value):
		"""Creates a fillet feature for selected edges and control point references."""
		self._instance.FeatureFillet3 = value

	@property
	def feature_folder_location(self):
		"""Gets the folder feature for the specified feature."""
		return self._instance.FeatureFolderLocation

	@feature_folder_location.setter
	def feature_folder_location(self, value):
		"""Gets the folder feature for the specified feature."""
		self._instance.FeatureFolderLocation = value

	@property
	def feature_revolve(self):
		"""Creates a base-, boss-, or cut-revolve feature."""
		return self._instance.FeatureRevolve2

	@feature_revolve.setter
	def feature_revolve(self, value):
		"""Creates a base-, boss-, or cut-revolve feature."""
		self._instance.FeatureRevolve2 = value

	@property
	def fillet_xpert_change(self):
		"""Changes the parameters on the selected filleted faces, regardless of whether the filleted faces were created manually or with FilletXpert, provided that FilletXpert can process them."""
		return self._instance.FilletXpertChange

	@fillet_xpert_change.setter
	def fillet_xpert_change(self, value):
		"""Changes the parameters on the selected filleted faces, regardless of whether the filleted faces were created manually or with FilletXpert, provided that FilletXpert can process them."""
		self._instance.FilletXpertChange = value

	@property
	def fillet_xpert_make_corner(self):
		"""Creates or changes a fillet corner feature."""
		return self._instance.FilletXpertMakeCorner

	@fillet_xpert_make_corner.setter
	def fillet_xpert_make_corner(self, value):
		"""Creates or changes a fillet corner feature."""
		self._instance.FilletXpertMakeCorner = value

	@property
	def fillet_xpert_remove(self):
		"""Deletes the fillets on the selected faces."""
		return self._instance.FilletXpertRemove

	@fillet_xpert_remove.setter
	def fillet_xpert_remove(self, value):
		"""Deletes the fillets on the selected faces."""
		self._instance.FilletXpertRemove = value

	@property
	def finish_corner_relief(self):
		"""Creates a sheet metal corner relief feature."""
		return self._instance.FinishCornerRelief

	@finish_corner_relief.setter
	def finish_corner_relief(self, value):
		"""Creates a sheet metal corner relief feature."""
		self._instance.FinishCornerRelief = value

	@property
	def get_feature_count(self):
		"""Gets the number of features in this document."""
		return self._instance.GetFeatureCount

	@get_feature_count.setter
	def get_feature_count(self, value):
		"""Gets the number of features in this document."""
		self._instance.GetFeatureCount = value

	@property
	def get_features(self):
		"""Gets the features in this document."""
		return self._instance.GetFeatures

	@get_features.setter
	def get_features(self, value):
		"""Gets the features in this document."""
		self._instance.GetFeatures = value

	@property
	def get_feature_tree_root_item(self):
		"""Gets the root item of the FeatureManager design tree in the specified pane."""
		return self._instance.GetFeatureTreeRootItem2

	@get_feature_tree_root_item.setter
	def get_feature_tree_root_item(self, value):
		"""Gets the root item of the FeatureManager design tree in the specified pane."""
		self._instance.GetFeatureTreeRootItem2 = value

	@property
	def get_flat_pattern_folder(self):
		"""Gets the interface to the flat-pattern folder feature in the FeatureManager design tree."""
		return self._instance.GetFlatPatternFolder

	@get_flat_pattern_folder.setter
	def get_flat_pattern_folder(self, value):
		"""Gets the interface to the flat-pattern folder feature in the FeatureManager design tree."""
		self._instance.GetFlatPatternFolder = value

	@property
	def get_freeze_location(self):
		"""Gets the location of the freeze bar in the FeatureManager design tree."""
		return self._instance.GetFreezeLocation

	@get_freeze_location.setter
	def get_freeze_location(self, value):
		"""Gets the location of the freeze bar in the FeatureManager design tree."""
		self._instance.GetFreezeLocation = value

	@property
	def get_pre_trimmed_bodies(self):
		"""Gets the temporary trimmed bodies using the specified target sheet (surface) body according to the trim tools previously defined by IFeatureManager::PreTrimSurface."""
		return self._instance.GetPreTrimmedBodies

	@get_pre_trimmed_bodies.setter
	def get_pre_trimmed_bodies(self, value):
		"""Gets the temporary trimmed bodies using the specified target sheet (surface) body according to the trim tools previously defined by IFeatureManager::PreTrimSurface."""
		self._instance.GetPreTrimmedBodies = value

	@property
	def get_selection_set_folder(self):
		"""Gets the Selection Sets folder."""
		return self._instance.GetSelectionSetFolder

	@get_selection_set_folder.setter
	def get_selection_set_folder(self, value):
		"""Gets the Selection Sets folder."""
		self._instance.GetSelectionSetFolder = value

	@property
	def get_sheet_metal_folder(self):
		"""Gets the interface to the sheet metal folder feature in the FeatureManager design tree."""
		return self._instance.GetSheetMetalFolder

	@get_sheet_metal_folder.setter
	def get_sheet_metal_folder(self, value):
		"""Gets the interface to the sheet metal folder feature in the FeatureManager design tree."""
		self._instance.GetSheetMetalFolder = value

	@property
	def get_slicing_data(self):
		"""Gets a new slicing data object with default parameter values."""
		return self._instance.GetSlicingData

	@get_slicing_data.setter
	def get_slicing_data(self, value):
		"""Gets a new slicing data object with default parameter values."""
		self._instance.GetSlicingData = value

	@property
	def hide_bodies(self):
		"""Hides both solid and surface bodies in the model."""
		return self._instance.HideBodies

	@hide_bodies.setter
	def hide_bodies(self, value):
		"""Hides both solid and surface bodies in the model."""
		self._instance.HideBodies = value

	@property
	def hole_wizard(self):
		"""Creates customized holes of various kinds."""
		return self._instance.HoleWizard5

	@hole_wizard.setter
	def hole_wizard(self, value):
		"""Creates customized holes of various kinds."""
		self._instance.HoleWizard5 = value

	@property
	def i_get_features(self):
		"""Gets the features in this document."""
		return self._instance.IGetFeatures

	@i_get_features.setter
	def i_get_features(self, value):
		"""Gets the features in this document."""
		self._instance.IGetFeatures = value

	@property
	def i_insert_combine_feature(self):
		"""Combines the specified bodies in the multibody part to create a combine feature."""
		return self._instance.IInsertCombineFeature

	@i_insert_combine_feature.setter
	def i_insert_combine_feature(self, value):
		"""Combines the specified bodies in the multibody part to create a combine feature."""
		self._instance.IInsertCombineFeature = value

	@property
	def i_insert_macro_feature(self):
		"""Inserts a macro feature in this model."""
		return self._instance.IInsertMacroFeature3

	@i_insert_macro_feature.setter
	def i_insert_macro_feature(self, value):
		"""Inserts a macro feature in this model."""
		self._instance.IInsertMacroFeature3 = value

	@property
	def i_insert_reference_point(self):
		"""Creates the geometry for the reference points based on any of these selected entities: edges, faces, planes, vertices, or sketch geometry."""
		return self._instance.IInsertReferencePoint

	@i_insert_reference_point.setter
	def i_insert_reference_point(self, value):
		"""Creates the geometry for the reference points based on any of these selected entities: edges, faces, planes, vertices, or sketch geometry."""
		self._instance.IInsertReferencePoint = value

	@property
	def insert_center_of_mass(self):
		"""Inserts a Center of Mass feature."""
		return self._instance.InsertCenterOfMass

	@insert_center_of_mass.setter
	def insert_center_of_mass(self, value):
		"""Inserts a Center of Mass feature."""
		self._instance.InsertCenterOfMass = value

	@property
	def insert_center_of_mass_reference_point(self):
		"""Inserts a Center of Mass Reference Point feature."""
		return self._instance.InsertCenterOfMassReferencePoint

	@insert_center_of_mass_reference_point.setter
	def insert_center_of_mass_reference_point(self, value):
		"""Inserts a Center of Mass Reference Point feature."""
		self._instance.InsertCenterOfMassReferencePoint = value

	@property
	def insert_combine_feature(self):
		"""Combines the specified bodies in the multibody part to create a combine feature."""
		return self._instance.InsertCombineFeature

	@insert_combine_feature.setter
	def insert_combine_feature(self, value):
		"""Combines the specified bodies in the multibody part to create a combine feature."""
		self._instance.InsertCombineFeature = value

	@property
	def insert_connection_point(self):
		"""Adds a connection point based on the selected entities."""
		return self._instance.InsertConnectionPoint

	@insert_connection_point.setter
	def insert_connection_point(self, value):
		"""Adds a connection point based on the selected entities."""
		self._instance.InsertConnectionPoint = value

	@property
	def insert_convert_to_sheet_metal(self):
		"""Converts a solid or surface body into a sheet metal part."""
		return self._instance.InsertConvertToSheetMetal2

	@insert_convert_to_sheet_metal.setter
	def insert_convert_to_sheet_metal(self, value):
		"""Converts a solid or surface body into a sheet metal part."""
		self._instance.InsertConvertToSheetMetal2 = value

	@property
	def insert_coordinate_system(self):
		"""Inserts a coordinate system feature."""
		return self._instance.InsertCoordinateSystem

	@insert_coordinate_system.setter
	def insert_coordinate_system(self, value):
		"""Inserts a coordinate system feature."""
		self._instance.InsertCoordinateSystem = value

	@property
	def insert_cosmetic_thread(self):
		"""Inserts a cosmetic thread."""
		return self._instance.InsertCosmeticThread3

	@insert_cosmetic_thread.setter
	def insert_cosmetic_thread(self, value):
		"""Inserts a cosmetic thread."""
		self._instance.InsertCosmeticThread3 = value

	@property
	def insert_cosmetic_weld_bead(self):
		"""Inserts a cosmetic weld bead using either weld geometry or a weld path."""
		return self._instance.InsertCosmeticWeldBead2

	@insert_cosmetic_weld_bead.setter
	def insert_cosmetic_weld_bead(self, value):
		"""Inserts a cosmetic weld bead using either weld geometry or a weld path."""
		self._instance.InsertCosmeticWeldBead2 = value

	@property
	def insert_cross_break(self):
		"""Inserts a cross break feature on the selected face in a sheet metal part."""
		return self._instance.InsertCrossBreak

	@insert_cross_break.setter
	def insert_cross_break(self, value):
		"""Inserts a cross break feature on the selected face in a sheet metal part."""
		self._instance.InsertCrossBreak = value

	@property
	def insert_cut_blend(self):
		"""Inserts a lofted cut based on the selected profiles, centerline, and guide curves."""
		return self._instance.InsertCutBlend

	@insert_cut_blend.setter
	def insert_cut_blend(self, value):
		"""Inserts a lofted cut based on the selected profiles, centerline, and guide curves."""
		self._instance.InsertCutBlend = value

	@property
	def insert_cut_surface(self):
		"""Inserts a surface-cut feature using the preselected surface or plane."""
		return self._instance.InsertCutSurface

	@insert_cut_surface.setter
	def insert_cut_surface(self, value):
		"""Inserts a surface-cut feature using the preselected surface or plane."""
		self._instance.InsertCutSurface = value

	@property
	def insert_delete_body(self):
		"""Inserts a Body-Delete/Keep feature."""
		return self._instance.InsertDeleteBody2

	@insert_delete_body.setter
	def insert_delete_body(self, value):
		"""Inserts a Body-Delete/Keep feature."""
		self._instance.InsertDeleteBody2 = value

	@property
	def insert_delete_hole_for_surface(self):
		"""Inserts a Delete Hole feature for one or more selected hole edges on a surface."""
		return self._instance.InsertDeleteHoleForSurface

	@insert_delete_hole_for_surface.setter
	def insert_delete_hole_for_surface(self, value):
		"""Inserts a Delete Hole feature for one or more selected hole edges on a surface."""
		self._instance.InsertDeleteHoleForSurface = value

	@property
	def insert_dwg_or_dxf_file(self):
		"""Inserts a DXF/DWG image feature."""
		return self._instance.InsertDwgOrDxfFile2

	@insert_dwg_or_dxf_file.setter
	def insert_dwg_or_dxf_file(self, value):
		"""Inserts a DXF/DWG image feature."""
		self._instance.InsertDwgOrDxfFile2 = value

	@property
	def insert_edge_merge(self):
		"""Merges multiple edges into a single edge using the selected faces when importing data."""
		return self._instance.InsertEdgeMerge

	@insert_edge_merge.setter
	def insert_edge_merge(self, value):
		"""Merges multiple edges into a single edge using the selected faces when importing data."""
		self._instance.InsertEdgeMerge = value

	@property
	def insert_end_cap_feature(self):
		"""Inserts an end cap feature using the specified end faces of a structural member."""
		return self._instance.InsertEndCapFeature2

	@insert_end_cap_feature.setter
	def insert_end_cap_feature(self, value):
		"""Inserts an end cap feature using the specified end faces of a structural member."""
		self._instance.InsertEndCapFeature2 = value

	@property
	def insert_end_cap_feature(self):
		"""Inserts an end cap feature for one or more pre-selected open ends of a structural member."""
		return self._instance.InsertEndCapFeature3

	@insert_end_cap_feature.setter
	def insert_end_cap_feature(self, value):
		"""Inserts an end cap feature for one or more pre-selected open ends of a structural member."""
		self._instance.InsertEndCapFeature3 = value

	@property
	def insert_feature_chamfer(self):
		"""Inserts a chamfer."""
		return self._instance.InsertFeatureChamfer

	@insert_feature_chamfer.setter
	def insert_feature_chamfer(self, value):
		"""Inserts a chamfer."""
		self._instance.InsertFeatureChamfer = value

	@property
	def insert_feature_lock(self):
		"""Locks or freezes a selected feature."""
		return self._instance.InsertFeatureLock

	@insert_feature_lock.setter
	def insert_feature_lock(self, value):
		"""Locks or freezes a selected feature."""
		self._instance.InsertFeatureLock = value

	@property
	def insert_feature_tree_folder(self):
		"""Inserts a folder in the FeatureManager design tree."""
		return self._instance.InsertFeatureTreeFolder2

	@insert_feature_tree_folder.setter
	def insert_feature_tree_folder(self, value):
		"""Inserts a folder in the FeatureManager design tree."""
		self._instance.InsertFeatureTreeFolder2 = value

	@property
	def insert_fillet_bead_feature(self):
		"""Inserts a fillet weld bead feature and also fills the gap between the pre-selected part bodies, if any."""
		return self._instance.InsertFilletBeadFeature2

	@insert_fillet_bead_feature.setter
	def insert_fillet_bead_feature(self, value):
		"""Inserts a fillet weld bead feature and also fills the gap between the pre-selected part bodies, if any."""
		self._instance.InsertFilletBeadFeature2 = value

	@property
	def insert_fillet_bead_feature(self):
		"""Inserts fillet weld bead features for the specified face sets."""
		return self._instance.InsertFilletBeadFeature3

	@insert_fillet_bead_feature.setter
	def insert_fillet_bead_feature(self, value):
		"""Inserts fillet weld bead features for the specified face sets."""
		self._instance.InsertFilletBeadFeature3 = value

	@property
	def insert_fill_surface(self):
		"""Inserts a fill-surface feature in the model."""
		return self._instance.InsertFillSurface2

	@insert_fill_surface.setter
	def insert_fill_surface(self, value):
		"""Inserts a fill-surface feature in the model."""
		self._instance.InsertFillSurface2 = value

	@property
	def insert_flatten_surface(self):
		"""Inserts a surface-flatten feature in the model."""
		return self._instance.InsertFlattenSurface2

	@insert_flatten_surface.setter
	def insert_flatten_surface(self, value):
		"""Inserts a surface-flatten feature in the model."""
		self._instance.InsertFlattenSurface2 = value

	@property
	def insert_flex_feature(self):
		"""Inserts a Flex feature using the selected solid or surface body."""
		return self._instance.InsertFlexFeature

	@insert_flex_feature.setter
	def insert_flex_feature(self, value):
		"""Inserts a Flex feature using the selected solid or surface body."""
		self._instance.InsertFlexFeature = value

	@property
	def insert_form_tool_feature(self):
		"""Inserts a forming tool from the Design Library into a sheet metal part."""
		return self._instance.InsertFormToolFeature

	@insert_form_tool_feature.setter
	def insert_form_tool_feature(self, value):
		"""Inserts a forming tool from the Design Library into a sheet metal part."""
		self._instance.InsertFormToolFeature = value

	@property
	def insert_freeform(self):
		"""Inserts a Freeform feature."""
		return self._instance.InsertFreeform2

	@insert_freeform.setter
	def insert_freeform(self, value):
		"""Inserts a Freeform feature."""
		self._instance.InsertFreeform2 = value

	@property
	def insert_grid_feature(self):
		"""Inserts a Grid System feature."""
		return self._instance.InsertGridFeature

	@insert_grid_feature.setter
	def insert_grid_feature(self, value):
		"""Inserts a Grid System feature."""
		self._instance.InsertGridFeature = value

	@property
	def insert_gusset_feature(self):
		"""Inserts a gusset feature for the specified faces."""
		return self._instance.InsertGussetFeature2

	@insert_gusset_feature.setter
	def insert_gusset_feature(self, value):
		"""Inserts a gusset feature for the specified faces."""
		self._instance.InsertGussetFeature2 = value

	@property
	def insert_gusset_feature(self):
		"""Inserts a gusset feature for pre-selected faces of a weldment."""
		return self._instance.InsertGussetFeature3

	@insert_gusset_feature.setter
	def insert_gusset_feature(self, value):
		"""Inserts a gusset feature for pre-selected faces of a weldment."""
		self._instance.InsertGussetFeature3 = value

	@property
	def insert_indent(self):
		"""Inserts an indent feature using a selected target body and tool body regions."""
		return self._instance.InsertIndent

	@insert_indent.setter
	def insert_indent(self, value):
		"""Inserts an indent feature using a selected target body and tool body regions."""
		self._instance.InsertIndent = value

	@property
	def insert_live_section_plane(self):
		"""Inserts a Live Section Plane using the selected plane or planar face."""
		return self._instance.InsertLiveSectionPlane

	@insert_live_section_plane.setter
	def insert_live_section_plane(self, value):
		"""Inserts a Live Section Plane using the selected plane or planar face."""
		self._instance.InsertLiveSectionPlane = value

	@property
	def insert_macro_feature(self):
		"""Inserts a macro feature in this model."""
		return self._instance.InsertMacroFeature3

	@insert_macro_feature.setter
	def insert_macro_feature(self, value):
		"""Inserts a macro feature in this model."""
		self._instance.InsertMacroFeature3 = value

	@property
	def insert_mate_reference(self):
		"""Inserts a mate reference for a part or assembly document."""
		return self._instance.InsertMateReference2

	@insert_mate_reference.setter
	def insert_mate_reference(self, value):
		"""Inserts a mate reference for a part or assembly document."""
		self._instance.InsertMateReference2 = value

	@property
	def insert_mid_surface(self):
		"""Inserts a midsurface feature."""
		return self._instance.InsertMidSurface

	@insert_mid_surface.setter
	def insert_mid_surface(self, value):
		"""Inserts a midsurface feature."""
		self._instance.InsertMidSurface = value

	@property
	def insert_mirror_feature(self):
		"""Mirrors selected features, faces, and bodies about a selected plane or planar face."""
		return self._instance.InsertMirrorFeature2

	@insert_mirror_feature.setter
	def insert_mirror_feature(self, value):
		"""Mirrors selected features, faces, and bodies about a selected plane or planar face."""
		self._instance.InsertMirrorFeature2 = value

	@property
	def insert_mold_core_cavity_solids(self):
		"""Creates a core/cavity solid feature."""
		return self._instance.InsertMoldCoreCavitySolids

	@insert_mold_core_cavity_solids.setter
	def insert_mold_core_cavity_solids(self, value):
		"""Creates a core/cavity solid feature."""
		self._instance.InsertMoldCoreCavitySolids = value

	@property
	def insert_mold_parting_line(self):
		"""Inserts a mold parting line feature."""
		return self._instance.InsertMoldPartingLine

	@insert_mold_parting_line.setter
	def insert_mold_parting_line(self, value):
		"""Inserts a mold parting line feature."""
		self._instance.InsertMoldPartingLine = value

	@property
	def insert_mold_parting_surface(self):
		"""Inserts a mold parting surface feature."""
		return self._instance.InsertMoldPartingSurface

	@insert_mold_parting_surface.setter
	def insert_mold_parting_surface(self, value):
		"""Inserts a mold parting surface feature."""
		self._instance.InsertMoldPartingSurface = value

	@property
	def insert_mold_shut_off_surface(self):
		"""Inserts the mold shut-off surface feature."""
		return self._instance.InsertMoldShutOffSurface

	@insert_mold_shut_off_surface.setter
	def insert_mold_shut_off_surface(self, value):
		"""Inserts the mold shut-off surface feature."""
		self._instance.InsertMoldShutOffSurface = value

	@property
	def insert_move_copy_body(self):
		"""Moves or makes copies of the selected solid bodies or surfaces."""
		return self._instance.InsertMoveCopyBody2

	@insert_move_copy_body.setter
	def insert_move_copy_body(self, value):
		"""Moves or makes copies of the selected solid bodies or surfaces."""
		self._instance.InsertMoveCopyBody2 = value

	@property
	def insert_move_face(self):
		"""Moves the selected faces on a solid or surface model."""
		return self._instance.InsertMoveFace3

	@insert_move_face.setter
	def insert_move_face(self, value):
		"""Moves the selected faces on a solid or surface model."""
		self._instance.InsertMoveFace3 = value

	@property
	def insert_multi_face_draft(self):
		"""Inserts a multiface draft feature."""
		return self._instance.InsertMultiFaceDraft

	@insert_multi_face_draft.setter
	def insert_multi_face_draft(self, value):
		"""Inserts a multiface draft feature."""
		self._instance.InsertMultiFaceDraft = value

	@property
	def insert_net_blend(self):
		"""This method inserts a boundary feature or a boundary surface feature."""
		return self._instance.InsertNetBlend2

	@insert_net_blend.setter
	def insert_net_blend(self, value):
		"""This method inserts a boundary feature or a boundary surface feature."""
		self._instance.InsertNetBlend2 = value

	@property
	def insert_protrusion_blend(self):
		"""Creates a lofted body or boss from the selected profiles, centerline, and guide curves."""
		return self._instance.InsertProtrusionBlend2

	@insert_protrusion_blend.setter
	def insert_protrusion_blend(self, value):
		"""Creates a lofted body or boss from the selected profiles, centerline, and guide curves."""
		self._instance.InsertProtrusionBlend2 = value

	@property
	def insert_reference_point(self):
		"""Creates the geometry for the reference points based on any of these selected entities: edges, faces, planes, vertices, or sketch geometry."""
		return self._instance.InsertReferencePoint

	@insert_reference_point.setter
	def insert_reference_point(self, value):
		"""Creates the geometry for the reference points based on any of these selected entities: edges, faces, planes, vertices, or sketch geometry."""
		self._instance.InsertReferencePoint = value

	@property
	def insert_ref_plane(self):
		"""Inserts a constraint-based reference plane using the selected reference entities."""
		return self._instance.InsertRefPlane

	@insert_ref_plane.setter
	def insert_ref_plane(self, value):
		"""Inserts a constraint-based reference plane using the selected reference entities."""
		self._instance.InsertRefPlane = value

	@property
	def insert_revolved_ref_surface(self):
		"""Creates a revolved reference surface by revolving a profile around a centerline."""
		return self._instance.InsertRevolvedRefSurface

	@insert_revolved_ref_surface.setter
	def insert_revolved_ref_surface(self, value):
		"""Creates a revolved reference surface by revolving a profile around a centerline."""
		self._instance.InsertRevolvedRefSurface = value

	@property
	def insert_rib(self):
		"""Inserts a rib."""
		return self._instance.InsertRib

	@insert_rib.setter
	def insert_rib(self, value):
		"""Inserts a rib."""
		self._instance.InsertRib = value

	@property
	def insert_ruled_surface_from_edge(self):
		"""Inserts a ruled surface from the selected edge on this feature."""
		return self._instance.InsertRuledSurfaceFromEdge2

	@insert_ruled_surface_from_edge.setter
	def insert_ruled_surface_from_edge(self, value):
		"""Inserts a ruled surface from the selected edge on this feature."""
		self._instance.InsertRuledSurfaceFromEdge2 = value

	@property
	def insert_save_out_bodies(self):
		"""Saves the selected surface bodies or solid bodies or sub-weldments to a file."""
		return self._instance.InsertSaveOutBodies

	@insert_save_out_bodies.setter
	def insert_save_out_bodies(self, value):
		"""Saves the selected surface bodies or solid bodies or sub-weldments to a file."""
		self._instance.InsertSaveOutBodies = value

	@property
	def insert_scale(self):
		"""Applies the specified scaling to either the current model or a selected graphic body."""
		return self._instance.InsertScale

	@insert_scale.setter
	def insert_scale(self, value):
		"""Applies the specified scaling to either the current model or a selected graphic body."""
		self._instance.InsertScale = value

	@property
	def insert_security_note(self):
		"""Inserts a note for the specified macro feature."""
		return self._instance.InsertSecurityNote

	@insert_security_note.setter
	def insert_security_note(self, value):
		"""Inserts a note for the specified macro feature."""
		self._instance.InsertSecurityNote = value

	@property
	def insert_sew_ref_surface(self):
		"""Creates a surface by knitting the selected surfaces together."""
		return self._instance.InsertSewRefSurface

	@insert_sew_ref_surface.setter
	def insert_sew_ref_surface(self, value):
		"""Creates a surface by knitting the selected surfaces together."""
		self._instance.InsertSewRefSurface = value

	@property
	def insert_sheet_metald_bend(self):
		"""Inserts a 3D bend in sheet metal part."""
		return self._instance.InsertSheetMetal3dBend

	@insert_sheet_metald_bend.setter
	def insert_sheet_metald_bend(self, value):
		"""Inserts a 3D bend in sheet metal part."""
		self._instance.InsertSheetMetal3dBend = value

	@property
	def insert_sheet_metal_base_flange(self):
		"""Inserts a sheet metal base flange feature."""
		return self._instance.InsertSheetMetalBaseFlange2

	@insert_sheet_metal_base_flange.setter
	def insert_sheet_metal_base_flange(self, value):
		"""Inserts a sheet metal base flange feature."""
		self._instance.InsertSheetMetalBaseFlange2 = value

	@property
	def insert_sheet_metal_corner_trim(self):
		"""Inserts a break corner trim in the sheet metal part."""
		return self._instance.InsertSheetMetalCornerTrim

	@insert_sheet_metal_corner_trim.setter
	def insert_sheet_metal_corner_trim(self, value):
		"""Inserts a break corner trim in the sheet metal part."""
		self._instance.InsertSheetMetalCornerTrim = value

	@property
	def insert_sheet_metal_hem(self):
		"""Inserts a hem of the specified relief type at the selected edges of the current sheet metal part."""
		return self._instance.InsertSheetMetalHem2

	@insert_sheet_metal_hem.setter
	def insert_sheet_metal_hem(self, value):
		"""Inserts a hem of the specified relief type at the selected edges of the current sheet metal part."""
		self._instance.InsertSheetMetalHem2 = value

	@property
	def insert_sheet_metal_lofted_bend(self):
		"""Inserts a lofted bend in a sheet metal part."""
		return self._instance.InsertSheetMetalLoftedBend2

	@insert_sheet_metal_lofted_bend.setter
	def insert_sheet_metal_lofted_bend(self, value):
		"""Inserts a lofted bend in a sheet metal part."""
		self._instance.InsertSheetMetalLoftedBend2 = value

	@property
	def insert_sheet_metal_miter_flange(self):
		"""Inserts a meter flange in a sheet metal part."""
		return self._instance.InsertSheetMetalMiterFlange

	@insert_sheet_metal_miter_flange.setter
	def insert_sheet_metal_miter_flange(self, value):
		"""Inserts a meter flange in a sheet metal part."""
		self._instance.InsertSheetMetalMiterFlange = value

	@property
	def insert_slicing(self):
		"""Creates and inserts slicing into the FeatureManager design tree."""
		return self._instance.InsertSlicing

	@insert_slicing.setter
	def insert_slicing(self, value):
		"""Creates and inserts slicing into the FeatureManager design tree."""
		self._instance.InsertSlicing = value

	@property
	def insert_split_line_intersect(self):
		"""Creates split lines using the selected intersecting tool and target entities."""
		return self._instance.InsertSplitLineIntersect

	@insert_split_line_intersect.setter
	def insert_split_line_intersect(self, value):
		"""Creates split lines using the selected intersecting tool and target entities."""
		self._instance.InsertSplitLineIntersect = value

	@property
	def insert_structural_weldment(self):
		"""Inserts a structural weldment feature."""
		return self._instance.InsertStructuralWeldment5

	@insert_structural_weldment.setter
	def insert_structural_weldment(self, value):
		"""Inserts a structural weldment feature."""
		self._instance.InsertStructuralWeldment5 = value

	@property
	def insert_sub_folder(self):
		"""Creates a subfolder in the Solid Bodies folder in the FeatureManager design tree and moves the selected solid bodies or subfolders in the Solid Bodies folder to the new subfolder."""
		return self._instance.InsertSubFolder

	@insert_sub_folder.setter
	def insert_sub_folder(self, value):
		"""Creates a subfolder in the Solid Bodies folder in the FeatureManager design tree and moves the selected solid bodies or subfolders in the Solid Bodies folder to the new subfolder."""
		self._instance.InsertSubFolder = value

	@property
	def insert_sub_weld_folder(self):
		"""Creates a sub weld folder feature containing solid bodies that are pre-selected in the user interface."""
		return self._instance.InsertSubWeldFolder

	@insert_sub_weld_folder.setter
	def insert_sub_weld_folder(self, value):
		"""Creates a sub weld folder feature containing solid bodies that are pre-selected in the user interface."""
		self._instance.InsertSubWeldFolder = value

	@property
	def insert_sub_weld_folder(self):
		"""Creates a sub weld folder feature containing the specified weldment bodies."""
		return self._instance.InsertSubWeldFolder2

	@insert_sub_weld_folder.setter
	def insert_sub_weld_folder(self, value):
		"""Creates a sub weld folder feature containing the specified weldment bodies."""
		self._instance.InsertSubWeldFolder2 = value

	@property
	def insert_untrim_surface(self):
		"""Inserts an untrimmed surface to patch surface holes and external edges by extending an existing surface along its natural boundaries."""
		return self._instance.InsertUntrimSurface

	@insert_untrim_surface.setter
	def insert_untrim_surface(self, value):
		"""Inserts an untrimmed surface to patch surface holes and external edges by extending an existing surface along its natural boundaries."""
		self._instance.InsertUntrimSurface = value

	@property
	def insert_variable_pitch_helix(self):
		"""Starts a variable-pitch helix using the selected sketch containing an arc."""
		return self._instance.InsertVariablePitchHelix

	@insert_variable_pitch_helix.setter
	def insert_variable_pitch_helix(self, value):
		"""Starts a variable-pitch helix using the selected sketch containing an arc."""
		self._instance.InsertVariablePitchHelix = value

	@property
	def insert_weldment_cut_list(self):
		"""Inserts a cut-list-item folder feature containing pre-selected weldment bodies."""
		return self._instance.InsertWeldmentCutList

	@insert_weldment_cut_list.setter
	def insert_weldment_cut_list(self, value):
		"""Inserts a cut-list-item folder feature containing pre-selected weldment bodies."""
		self._instance.InsertWeldmentCutList = value

	@property
	def insert_weldment_cut_list(self):
		"""Inserts a cut-list-item folder feature containing the specified weldment bodies."""
		return self._instance.InsertWeldmentCutList2

	@insert_weldment_cut_list.setter
	def insert_weldment_cut_list(self, value):
		"""Inserts a cut-list-item folder feature containing the specified weldment bodies."""
		self._instance.InsertWeldmentCutList2 = value

	@property
	def insert_weldment_feature(self):
		"""Inserts a weldment feature."""
		return self._instance.InsertWeldmentFeature

	@insert_weldment_feature.setter
	def insert_weldment_feature(self, value):
		"""Inserts a weldment feature."""
		self._instance.InsertWeldmentFeature = value

	@property
	def insert_weldment_trim_feature(self):
		"""Inserts a weldment trim feature."""
		return self._instance.InsertWeldmentTrimFeature

	@insert_weldment_trim_feature.setter
	def insert_weldment_trim_feature(self, value):
		"""Inserts a weldment trim feature."""
		self._instance.InsertWeldmentTrimFeature = value

	@property
	def insert_weldment_trim_feature(self):
		"""Inserts a weldment trim feature for the specified weldment bodies or faces."""
		return self._instance.InsertWeldmentTrimFeature2

	@insert_weldment_trim_feature.setter
	def insert_weldment_trim_feature(self, value):
		"""Inserts a weldment trim feature for the specified weldment bodies or faces."""
		self._instance.InsertWeldmentTrimFeature2 = value

	@property
	def insert_wrap_feature(self):
		"""Inserts a wrap feature."""
		return self._instance.InsertWrapFeature2

	@insert_wrap_feature.setter
	def insert_wrap_feature(self, value):
		"""Inserts a wrap feature."""
		self._instance.InsertWrapFeature2 = value

	@property
	def is_name_used(self):
		"""Checks to see whether the specified name is unique in the FeatureManager design tree and valid to use."""
		return self._instance.IsNameUsed

	@is_name_used.setter
	def is_name_used(self, value):
		"""Checks to see whether the specified name is unique in the FeatureManager design tree and valid to use."""
		self._instance.IsNameUsed = value

	@property
	def make_styled_curves(self):
		"""Fits a spline to the preselected sketch segments to make a smooth edge on the model."""
		return self._instance.MakeStyledCurves2

	@make_styled_curves.setter
	def make_styled_curves(self, value):
		"""Fits a spline to the preselected sketch segments to make a smooth edge on the model."""
		self._instance.MakeStyledCurves2 = value

	@property
	def mold_undercut_detect(self):
		"""Detects trapped, also called undercut, areas in a model that cannot be ejected from the mold."""
		return self._instance.MoldUndercutDetect2

	@mold_undercut_detect.setter
	def mold_undercut_detect(self, value):
		"""Detects trapped, also called undercut, areas in a model that cannot be ejected from the mold."""
		self._instance.MoldUndercutDetect2 = value

	@property
	def move_rotate_live_section_plane(self):
		"""Moves or rotates the selected Live Section Plane using the selected Live Section Plane and its manipulator."""
		return self._instance.MoveRotateLiveSectionPlane

	@move_rotate_live_section_plane.setter
	def move_rotate_live_section_plane(self, value):
		"""Moves or rotates the selected Live Section Plane using the selected Live Section Plane and its manipulator."""
		self._instance.MoveRotateLiveSectionPlane = value

	@property
	def move_to_folder(self):
		"""Moves the selected feature or folder in the Solid Bodies Feature Manager design tree structure to the specified folder in the Solid Bodies Feature Manager design tree structure."""
		return self._instance.MoveToFolder

	@move_to_folder.setter
	def move_to_folder(self, value):
		"""Moves the selected feature or folder in the Solid Bodies Feature Manager design tree structure to the specified folder in the Solid Bodies Feature Manager design tree structure."""
		self._instance.MoveToFolder = value

	@property
	def post_intersect(self):
		"""Creates an intersect feature."""
		return self._instance.PostIntersect

	@post_intersect.setter
	def post_intersect(self, value):
		"""Creates an intersect feature."""
		self._instance.PostIntersect = value

	@property
	def post_split_body(self):
		"""Creates a Split feature."""
		return self._instance.PostSplitBody2

	@post_split_body.setter
	def post_split_body(self, value):
		"""Creates a Split feature."""
		self._instance.PostSplitBody2 = value

	@property
	def post_trim_surface(self):
		"""Sets whether to sew the resulting trimmed surfaces."""
		return self._instance.PostTrimSurface

	@post_trim_surface.setter
	def post_trim_surface(self, value):
		"""Sets whether to sew the resulting trimmed surfaces."""
		self._instance.PostTrimSurface = value

	@property
	def pre_intersect(self):
		"""Prepares an intersect feature."""
		return self._instance.PreIntersect2

	@pre_intersect.setter
	def pre_intersect(self, value):
		"""Prepares an intersect feature."""
		self._instance.PreIntersect2 = value

	@property
	def pre_split_body(self):
		"""Gets all of the bodies created by splitting a part."""
		return self._instance.PreSplitBody2

	@pre_split_body.setter
	def pre_split_body(self, value):
		"""Gets all of the bodies created by splitting a part."""
		self._instance.PreSplitBody2 = value

	@property
	def pre_trim_surface(self):
		"""Sets the trimming options before trimming a surface."""
		return self._instance.PreTrimSurface

	@pre_trim_surface.setter
	def pre_trim_surface(self, value):
		"""Sets the trimming options before trimming a surface."""
		self._instance.PreTrimSurface = value

	@property
	def set_freeform_boundary_continuity(self):
		"""Sets the boundary continuity for this Freeform feature."""
		return self._instance.SetFreeformBoundaryContinuity

	@set_freeform_boundary_continuity.setter
	def set_freeform_boundary_continuity(self, value):
		"""Sets the boundary continuity for this Freeform feature."""
		self._instance.SetFreeformBoundaryContinuity = value

	@property
	def set_freeform_curve_data(self):
		"""Adds a curve to the pre-selected face for a Freeform feature."""
		return self._instance.SetFreeformCurveData

	@set_freeform_curve_data.setter
	def set_freeform_curve_data(self, value):
		"""Adds a curve to the pre-selected face for a Freeform feature."""
		self._instance.SetFreeformCurveData = value

	@property
	def set_freeform_point_data(self):
		"""Adds a point to a curve for a Freeform feature."""
		return self._instance.SetFreeformPointData

	@set_freeform_point_data.setter
	def set_freeform_point_data(self, value):
		"""Adds a point to a curve for a Freeform feature."""
		self._instance.SetFreeformPointData = value

	@property
	def set_net_blend_curve_data(self):
		"""Sets the data for a curve for this boundary feature or boundary surface feature."""
		return self._instance.SetNetBlendCurveData

	@set_net_blend_curve_data.setter
	def set_net_blend_curve_data(self, value):
		"""Sets the data for a curve for this boundary feature or boundary surface feature."""
		self._instance.SetNetBlendCurveData = value

	@property
	def set_net_blend_direction_data(self):
		"""Sets the curve set data (one for each of the two directions) for this boundary feature or boundary surface feature."""
		return self._instance.SetNetBlendDirectionData

	@set_net_blend_direction_data.setter
	def set_net_blend_direction_data(self, value):
		"""Sets the curve set data (one for each of the two directions) for this boundary feature or boundary surface feature."""
		self._instance.SetNetBlendDirectionData = value

	@property
	def show_bodies(self):
		"""Shows both hidden solid and surface bodies."""
		return self._instance.ShowBodies

	@show_bodies.setter
	def show_bodies(self, value):
		"""Shows both hidden solid and surface bodies."""
		self._instance.ShowBodies = value

	@property
	def simple_hole(self):
		"""Inserts a simple hole feature."""
		return self._instance.SimpleHole2

	@simple_hole.setter
	def simple_hole(self, value):
		"""Inserts a simple hole feature."""
		self._instance.SimpleHole2 = value

	@property
	def update_feature_tree(self):
		"""Updates the FeatureManager design tree."""
		return self._instance.UpdateFeatureTree

	@update_feature_tree.setter
	def update_feature_tree(self, value):
		"""Updates the FeatureManager design tree."""
		self._instance.UpdateFeatureTree = value

