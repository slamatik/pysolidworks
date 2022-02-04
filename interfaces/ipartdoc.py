# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html
class IPartDoc:
    def __init__(self, parent=None):
        self._instance = parent

    def i_material_property_values(self):
        """Gets or sets a material's properties in the active configuration."""
        # return self._instance.IMaterialPropertyValues
        raise NotImplemented

    def material_id_name(self):
        """Gets or sets the material name."""
        # return self._instance.MaterialIdName
        raise NotImplemented

    def material_property_values(self):
        """Gets or sets a material's properties in the active configuration."""
        # return self._instance.MaterialPropertyValues
        raise NotImplemented

    def material_user_name(self):
        """Gets or sets the material name. This name is visible to the user."""
        # return self._instance.MaterialUserName
        raise NotImplemented

    def add_property_extension(self, property_extension):
        """
        Adds a property extension to this part.
        :param property_extension: Value of the property extension to add to this part (see Remarks)
        """
        # return self._instance.AddPropertyExtension(property_extension)
        raise NotImplemented

    def create_exploded_view(self):
        """Creates an explode view of this multibody part."""
        # return self._instance.CreateExplodedView
        raise NotImplemented

    def create_feature_from_body(self, body, make_ref_surface, options):
        """
        Creates a new imported feature from the specified temporary body.
        :param body: Temporary body
        :param make_ref_surface: If the body cannot be knitted to a solid or if a solid body already exists in this
        model, then True creates a reference surface feature
        :param options: Options as defined in swCreateFeatureBodyOpts_e
        """
        # return self._instance.CreateFeatureFromBody3(body, make_ref_surface, options)
        raise NotImplemented

    def create_new_body(self):
        """Creates a new body to use for import sewing operations and returns it to the caller."""
        # return self._instance.CreateNewBody
        raise NotImplemented

    def create_surface_feature_from_body(self, body, options):
        """
        Creates a surface feature from a body.
        :param body: Body from which to create surface feature
        :param options: Surface feature options as defined in swCreateFeatureBodyOpts_e
        """
        # return self._instance.CreateSurfaceFeatureFromBody(body, options)
        raise NotImplemented

    def delete_entity_name(self, entity):
        """
        Deletes the name associated with the specified entity.
        :param entity: Entity whose name to remove
        """
        # return self._instance.DeleteEntityName(entity)
        raise NotImplemented

    def edit_rollback(self):
        """Rolls back the part's history to the feature just before the currently selected feature in the FeatureManager
        design tree."""
        # return self._instance.EditRollback
        raise NotImplemented

    def enum_bodies(self, body_type, b_visible_only):
        """
        Enumerates the bodies in this part.
        :param body_type: Type of body as defined in swBodyType_e
        :param b_visible_only: True gets only visible bodies, false gets all bodies
        """
        # return self._instance.EnumBodies3(body_type, b_visible_only)
        raise NotImplemented

    def enum_related_bodies(self):
        """Creates an enumerated list of bodies."""
        # return self._instance.EnumRelatedBodies2
        raise NotImplemented

    def enum_related_sectioned_bodies(self, view_in):
        """
        Gets an enumeration of the related sectioned bodies in a part.
        :param view_in: Model view
        """
        # return self._instance.EnumRelatedSectionedBodies2(view_in)
        raise NotImplemented

    def export_to_d_w_g(self, file_path, model_name, action, export_to_single_file, alignment, is_x_dir_flipped,
                        is_y_dir_flipped, sheet_metal_options, views):
        """
        Saves various aspects of a part (sheet metal, faces, loops, and annotation views) to one or more DXF/DWG files,
        preserving the specified file name.
        :param file_path: Path and file name of the exported DXF/DWG file
        :param model_name: Path and file name of the active part document
        :param action: Export action as defined in swExportToDWG_e
        :param export_to_single_file: True to save as one file; false to save as multiple files
        :param alignment: Array of 12 double values that contain information related to output alignment
        :param is_x_dir_flipped: True to flip the x direction; false otherwise
        :param is_y_dir_flipped: True to flip the y direction; false otherwise
        :param sheet_metal_options: Bitmask that contains sheet metal export options; valid only if
        Action = swExportToDWG_e.swExportToDWG_ExportSheetMetal
        :param views: Array of annotation view names to export; valid only if A
        ction = swExportToDWG_e.swExportToDWG_ExportAnnotationViews
        """
        # return self._instance.ExportToDWG2(file_path, model_name, action, export_to_single_file, alignment, is_x_dir_flipped, is_y_dir_flipped, sheet_metal_options, views)
        raise NotImplemented

    def feature_by_id(self, i_d):
        """
        Gets the feature with the specified ID in the part.
        :param i_d: ID of feature
        """
        # return self._instance.FeatureById(i_d)
        raise NotImplemented

    def feature_by_name(self, name):
        """
        Gets the named feature in the part.
        :param name: Name of feature
        """
        # return self._instance.FeatureByName(name)
        raise NotImplemented

    def feature_xpert(self):
        """Executes FeatureXpert, powered by SOLIDWORKS Intelligent Feature Technology ( SWIFT), in parts."""
        # return self._instance.FeatureXpert
        raise NotImplemented

    def first_feature(self):
        """Gets the first feature in the part."""
        # return self._instance.FirstFeature
        raise NotImplemented

    def get_bodies(self, body_type, b_visible_only):
        """
        Gets the bodies in this part.
        :param body_type: Type of body as defined in swBodyType_e
        :param b_visible_only: True gets only the visible bodies, false gets all of the bodies in the part
        """
        # return self._instance.GetBodies2(body_type, b_visible_only)
        raise NotImplemented

    def get_entity_by_name(self, name, entity_type):
        """
        Gets an entity (face, edge, vertex) by name.
        :param name: Name of entity
        :param entity_type: Entity type as defined in swSelectType_e (see Remarks)
        """
        # return self._instance.GetEntityByName(name, entity_type)
        raise NotImplemented

    def get_entity_name(self, entity):
        """
        Gets the name of the specified entity.
        :param entity: Entity
        """
        # return self._instance.GetEntityName(entity)
        raise NotImplemented

    def get_exploded_view_configuration_name(self, exploded_view_name):
        """
        Gets the name of the configuration for the specified explode view of this multibody part.
        :param exploded_view_name: Name of the explode view whose configuration to get
        """
        # return self._instance.GetExplodedViewConfigurationName(exploded_view_name)
        raise NotImplemented

    def get_exploded_view_count(self, configuration_name):
        """
        Gets the number of explode views in the specified configuration of this multibody part.
        :param configuration_name: Name of the configuration
        """
        # return self._instance.GetExplodedViewCount(configuration_name)
        raise NotImplemented

    def get_exploded_view_names(self, configuration_name):
        """
        Gets the names of all the explode views in the specified configuration of this multibody part.
        :param configuration_name: Name of the configuration
        """
        # return self._instance.GetExplodedViewNames(configuration_name)
        raise NotImplemented

    def get_mate_reference_entity(self):
        """Gets the mate reference entity."""
        # return self._instance.GetMateReferenceEntity
        raise NotImplemented

    def get_material_property_name(self, config_name, database):
        """
        Gets the names of the material database and the material for the specified configuration.
        :param config_name: Name of configuration  (see Remarks)
        :param database: Name of material database
        """
        # return self._instance.GetMaterialPropertyName2(config_name, database)
        raise NotImplemented

    def get_material_visual_properties(self):
        """Gets the material visual properties for this part."""
        # return self._instance.GetMaterialVisualProperties
        raise NotImplemented

    def get_named_entities(self):
        """Gets an array of names of named entities (face, edge, vertex, and so on) in this part."""
        # return self._instance.GetNamedEntities
        raise NotImplemented

    def get_named_entities_count(self):
        """Gets the number of named entities (face, edge, vertex, and so on) in this part."""
        # return self._instance.GetNamedEntitiesCount
        raise NotImplemented

    def get_part_box(self, no_conversion):
        """
        Gets the box enclosing the part.
        :param no_conversion: Convert to user units or not; true retains system units, false changes to user units
        """
        # return self._instance.GetPartBox(no_conversion)
        raise NotImplemented

    def get_property_extension(self, i_d):
        """
        Gets the specified property extension on this part document.
        :param i_d: (Size of the array returned by IPartDoc::AddPropertyExtension) - (Position of the property extension
        in the array) (see Remarks)
        """
        # return self._instance.GetPropertyExtension(i_d)
        raise NotImplemented

    def get_related_bodies(self):
        """Creates a list of all the related bodies in a part."""
        # return self._instance.GetRelatedBodies
        raise NotImplemented

    def get_related_sectioned_bodies(self, view_in):
        """
        Gets all of the related sectioned bodies in a part.
        :param view_in: Model view
        """
        # return self._instance.GetRelatedSectionedBodies(view_in)
        raise NotImplemented

    def get_sectioned_body(self, view_in):
        """
        Gets the sectioned body seen in the specified drawing view.
        :param view_in: Model view
        """
        # return self._instance.GetSectionedBody(view_in)
        raise NotImplemented

    def get_tess_norms(self):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation."""
        # return self._instance.GetTessNorms
        raise NotImplemented

    def get_tess_triangle_count(self):
        """Gets the number of triangles that make up the shaded picture tessellation for this part."""
        # return self._instance.GetTessTriangleCount
        raise NotImplemented

    def get_tess_triangles(self, no_conversion):
        """
        Gets the triangles that make up the shaded picture tessellation for this part.
        :param no_conversion: True to prohibit conversion to user units from system units , false to do so
        """
        # return self._instance.GetTessTriangles(no_conversion)
        raise NotImplemented

    def get_tess_tri_strip_edges(self):
        """Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part."""
        # return self._instance.GetTessTriStripEdges
        raise NotImplemented

    def get_tess_tri_strip_norms(self):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this
        part."""
        # return self._instance.GetTessTriStripNorms
        raise NotImplemented

    def get_tess_tri_strips(self, no_conversion):
        """
        Gets the vertices that make up the shaded picture tessellation for this part.
        :param no_conversion: True prohibits converting to user units from system units, false does not
        """
        # return self._instance.GetTessTriStrips(no_conversion)
        raise NotImplemented

    def get_tess_tri_strip_size(self):
        """Gets the size of the array floats required to contain the data returned when calling
        IPartDoc::GetTessTriStrips and IPartDoc::IGetTessTriStrips."""
        # return self._instance.GetTessTriStripSize
        raise NotImplemented

    def i_create_feature_from_body(self, body, make_ref_surface, options):
        """
        Creates a new imported feature from the specified temporary body.
        :param body: Temporary body
        :param make_ref_surface: If the body cannot be knit to a solid or if a solid body already exists in this model,
        then True creates of a reference surface feature
        :param options: Option as defined by swCreateFeatureBodyOpts_e
        """
        # return self._instance.ICreateFeatureFromBody4(body, make_ref_surface, options)
        raise NotImplemented

    def i_create_new_body(self):
        """Creates a new body to use for import sewing operations and returns it to the caller."""
        # return self._instance.ICreateNewBody2
        raise NotImplemented

    def i_create_surface_feature_from_body(self):
        """Creates a surface feature from a body."""
        # return self._instance.ICreateSurfaceFeatureFromBody
        raise NotImplemented

    def i_create_surface_feature_from_body_count(self, body, options):
        """
        Gets the number of surface features to create from the body.
        :param body: Body from which to create surface features
        :param options: Options as defined in swCreateFeatureBodyOpts_e
        """
        # return self._instance.ICreateSurfaceFeatureFromBodyCount2(body, options)
        raise NotImplemented

    def i_delete_entity_name(self, entity):
        """
        Deletes the name associated with the specified entity.
        :param entity: Entity whose name to remove
        """
        # return self._instance.IDeleteEntityName(entity)
        raise NotImplemented

    def i_export_to_d_w_g(self, file_path, model_name, action, export_to_single_file, alignment, is_x_dir_flipped,
                          is_y_dir_flipped, sheet_metal_options, views_count, views):
        """
        Saves various aspects of a part (sheet metal, faces, loops, and annotation views) to one or more DXF/DWG files,
        preserving the specified filename.
        :param file_path: Path and filename of the exported DXF/DWG file
        :param model_name: Path and filename of the active part document
        :param action: Export action as defined in swExportToDWG_e
        :param export_to_single_file: True to save as one file; false to save as multiple files
        :param alignment:
In-process, unmanaged C++: Pointer to an array of 12 double values that contain information related to output alignment
(see Remarks)
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
        :param is_x_dir_flipped: True to flip the x direction; false otherwise
        :param is_y_dir_flipped: True to flip the y direction; false otherwise
        :param sheet_metal_options: Bitmask that contains sheet metal export options; valid only if Action = swExportToDWG_e.swExportToDWG_ExportSheetMetal (See Remarks)
        :param views_count: Number of annotation views to export; valid only if Action = swExportToDWG_e.swExportToDWG_ExportAnnotationViews
        :param views:
In-process, unmanaged C++: Pointer to an array of annotation view names to export; valid only if Action = swExportToDWG_e.swExportToDWG_ExportAnnotationViews
VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
        """
        # return self._instance.IExportToDWG2(file_path, model_name, action, export_to_single_file, alignment, is_x_dir_flipped, is_y_dir_flipped, sheet_metal_options, views_count, views)
        raise NotImplemented

    def i_feature_by_id(self, i_d):
        """
        Gets the feature with the specified ID in the part.
        :param i_d: ID of feature
        """
        # return self._instance.IFeatureById(i_d)
        raise NotImplemented

    def i_feature_by_name(self, name):
        """
        Gets the named feature in the part.
        :param name: Name of feature
        """
        # return self._instance.IFeatureByName(name)
        raise NotImplemented

    def i_first_feature(self):
        """Gets the first feature in the part."""
        # return self._instance.IFirstFeature
        raise NotImplemented

    def i_get_entity_by_name(self, name, entity_type):
        """
        Gets an entity (face, edge, vertex) by name.
        :param name: Name of entity
        :param entity_type: Entity type as defined in swSelectType_e (see Remarks)
        """
        # return self._instance.IGetEntityByName(name, entity_type)
        raise NotImplemented

    def i_get_entity_name(self, entity):
        """
        Gets the name of the specified entity.
        :param entity: Entity
        """
        # return self._instance.IGetEntityName(entity)
        raise NotImplemented

    def i_get_named_entities(self, count):
        """
        Gets an array of names of named entities (face, edge, vertex, and so on) in this part.
        :param count: Number of named entities
        """
        # return self._instance.IGetNamedEntities(count)
        raise NotImplemented

    def i_get_part_box(self, no_conversion):
        """
        Gets the box enclosing the part.
        :param no_conversion: Convert to user units or not; True retains system units, false changes to user units
        """
        # return self._instance.IGetPartBox(no_conversion)
        raise NotImplemented

    def i_get_processed_body(self):
        """Pre-processes the geometry of a body so that:


Closed periodic faces (for example, the lateral face of a cylinder) are split into two faces.

Faces that straddle the seam, if any, of the underlying surface are split into two faces."""
        # return self._instance.IGetProcessedBody2
        raise NotImplemented

    def i_get_processed_body_with_sel_face(self):
        """Gets a processed body."""
        # return self._instance.IGetProcessedBodyWithSelFace2
        raise NotImplemented

    def i_get_sectioned_body(self, view_in):
        """
        Gets the sectioned body seen in the specified drawing view.
        :param view_in: Model view
        """
        # return self._instance.IGetSectionedBody2(view_in)
        raise NotImplemented

    def i_get_tess_norms(self):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation."""
        # return self._instance.IGetTessNorms
        raise NotImplemented

    def i_get_tess_triangles(self, no_conversion):
        """
        Gets the triangles that make up the shaded picture tessellation for this part.
        :param no_conversion: True to prohibit conversion to user units from system units , false to do so
        """
        # return self._instance.IGetTessTriangles(no_conversion)
        raise NotImplemented

    def i_get_tess_tri_strip_edges(self):
        """Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part."""
        # return self._instance.IGetTessTriStripEdges
        raise NotImplemented

    def i_get_tess_tri_strip_edge_size(self):
        """Gets the size of the array returned by IPartDoc::GetTessTriStripEdges and IPartDoc::IGetTessTriStripEdges."""
        # return self._instance.IGetTessTriStripEdgeSize
        raise NotImplemented

    def i_get_tess_tri_strip_norms(self):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this part."""
        # return self._instance.IGetTessTriStripNorms
        raise NotImplemented

    def i_get_tess_tri_strips(self, no_conversion):
        """
        Gets the vertices that make up the shaded picture tessellation for this part.
        :param no_conversion: True prohibits converting to user units from system units, false does not
        """
        # return self._instance.IGetTessTriStrips(no_conversion)
        raise NotImplemented

    def import_diagnosis(self, close_all_gaps, remove_faces, fix_faces, options):
        """
        Diagnoses and repairs any gaps or bad faces on imported features.
        :param close_all_gaps: True to repair any gaps, false to not
        :param remove_faces: True to remove any bad faces and create gaps in the feature, false to not
        :param fix_faces: True to fix the bad faces, false to not
        :param options: Not used
        """
        # return self._instance.ImportDiagnosis(close_all_gaps, remove_faces, fix_faces, options)
        raise NotImplemented

    def import_diagnosis_gap_closer(self, old_x, old_y, old_z, new_x, new_y, new_z, last_move):
        """
        Allows you to repair a gap by moving the vertices on the edges surrounding the gap to new positions to close the gap on the imported model.
        :param old_x: x coordinate of vertex to move
        :param old_y: y coordinate of vertex to move
        :param old_z: z coordinate of vertex to move
        :param new_x: x coordinate where to move the vertex
        :param new_y: y coordinate where to move the vertex
        :param new_z: z coordinate where to move the vertex
        :param last_move: True if this move is the last move in a series of moves to close the gap, false if not
        """
        # return self._instance.ImportDiagnosisGapCloser(old_x, old_y, old_z, new_x, new_y, new_z, last_move)
        raise NotImplemented

    def insert_bend_notes(self, flat_pattern_feature):
        """
        Inserts bend notes for the specified flat-pattern feature of this sheet metal part.
        :param flat_pattern_feature: IFeature
        """
        # return self._instance.InsertBendNotes(flat_pattern_feature)
        raise NotImplemented

    def insert_bends(self, radius, use_bend_table, use_kfactor, use_bend_allowance, use_auto_relief, offset_ratio,
                     do_flatten):
        """
        Creates bends in a thin-feature part.
        :param radius: Radius of the bends
        :param use_bend_table: Bend table name (.btl file)
        :param use_kfactor: K-Factor ratio or -1 if not used
        :param use_bend_allowance: Bend allowance value or -1 if not used
        :param use_auto_relief: True if auto-relief cuts are to be added, false if not
        :param offset_ratio: Distance relief cut extends beyond bend (see Remarks)
        :param do_flatten: True to create these three features: Sheet-Metal, Flatten-Bends, and Process-Bends, false to create only the Sheet-Metal feature
        """
        # return self._instance.InsertBends2(radius, use_bend_table, use_kfactor, use_bend_allowance, use_auto_relief, offset_ratio, do_flatten)
        raise NotImplemented

    def insert_bend_table(self, x, y, start_value, table_template):
        """
        Creates a bend table annotation for the flat pattern of this sheet metal part.
        :param x: X-coordinate for placement of the bend table
        :param y: Y-coordinate for placement of the bend table
        :param start_value: Starting datum tag; a value from A to Z for letter tags; a positive integer for number tags
        :param table_template: Full pathname of the template (e.g., install_dir\lang\language\bendtable-standard.sldbndtbt)
        """
        # return self._instance.InsertBendTable(x, y, start_value, table_template)
        raise NotImplemented

    def insert_imported_feature(self, file_name, errors):
        """
        Inserts a third-party native CAD file into this part.
        :param file_name: Full path name of the third-party native CAD file to insert
        :param errors: Error code as defined in swFileLoadError_e
        """
        # return self._instance.InsertImportedFeature(file_name, errors)
        raise NotImplemented

    def insert_mirror_all(self):
        """Mirrors the part about a selected planar face."""
        # return self._instance.InsertMirrorAll
        raise NotImplemented

    def insert_part(self, file_name, options, configuration_name):
        """
        Inserts the specified part in the specified configuration into this part.
        :param file_name: Name of the part file to insert
        :param options: Insertion options as defined in swInsertPartOptions_e
        :param configuration_name: Name of FileName's configuration
        """
        # return self._instance.InsertPart3(file_name, options, configuration_name)
        raise NotImplemented

    def i_set_entity_name(self, entity, string_value):
        """
        Sets the name of the entity if the entity does not have a name.
        :param entity: Entity  
        :param string_value: Name of the entity 
        """
        # return self._instance.ISetEntityName(entity, string_value)
        raise NotImplemented

    def is_mirrored(self):
        """Gets whether this part is mirrored."""
        # return self._instance.IsMirrored
        raise NotImplemented

    def is_weldment(self):
        """Gets whether this part contains a weldment feature."""
        # return self._instance.IsWeldment
        raise NotImplemented

    def make_section(self):
        """Saves sketch profiles for use in the wizard."""
        # return self._instance.MakeSection
        raise NotImplemented

    def mirror_feature(self):
        """Displays a dialog that allows the end-user to mirror a feature about a selected plane or planar face."""
        # return self._instance.MirrorFeature
        raise NotImplemented

    def mirror_part(self, break_link, options, result_part):
        """
        Creates a new part document that mirrors this part about a selected reference plane or planar face.
        :param break_link: True to break the link to the original part, false to not
        :param options: Insertion options as defined in swMirrorPartOptions_e
        :param result_part: IModelDoc2
        """
        # return self._instance.MirrorPart2(break_link, options, result_part)
        raise NotImplemented

    def remove_all_display_states(self):
        """Removes all display states and appearances from this part document."""
        # return self._instance.RemoveAllDisplayStates
        raise NotImplemented

    def reorder_feature(self, feature_to_move, move_after_feature):
        """
        Reorders features and their operations.
        :param feature_to_move: Name of the feature to move
        :param move_after_feature: Name of the feature that now precedes the feature in the FeatureManager design tree
        """
        # return self._instance.ReorderFeature(feature_to_move, move_after_feature)
        raise NotImplemented

    def reset_property_extension(self):
        """Clears all values stored in the property extension."""
        # return self._instance.ResetPropertyExtension
        raise NotImplemented

    def save_to_file(self, name, options, cut_list_props, override_template, template_path, errors, warnings):
        """
        Saves the selected weldment member, surface body, or solid body to another part document.
        :param name: Path and name of the part document to which to save the selected weldment member, solid body, or surface body
        :param options: How to save the document as defined in swSaveAsOptions_e
        :param cut_list_props: Option for transferring the cut list of the selected weldment member, solid body, or surface body to the new part as defined in swCutListTransferOptions_e
        :param override_template: True to override the part template with the template specified by TemplatePath, false to not
        :param template_path: Path to part template; valid only if OverrideTemplate is true
        :param errors: Save errors as defined in swFileSaveError_e
        :param warnings: Warnings or extra information generated during the save operation as defined in swFileSaveWarning_e
        """
        # return self._instance.SaveToFile3(name, options, cut_list_props, override_template, template_path, errors, warnings)
        raise NotImplemented

    def set_cosmos_works_material(self, config_name, type):
        """
        Assigns the material to use during analysis to this part.
        :param config_name: Name of the configuration
        :param type: Type of material to assign as defined by swCosmosWorksMat
        """
        # return self._instance.SetCosmosWorksMaterial(config_name, type)
        raise NotImplemented

    def set_dropped_file_name(self, file_name):
        """
        Sets the filename for a recently dropped file.
        :param file_name: Name of the file to use for the rest of the drop process
        """
        # return self._instance.SetDroppedFileName(file_name)
        raise NotImplemented

    def set_entity_name(self, entity, string_value):
        """
        Sets the name of the entity if the entity does not have a name and the name is unique to the part.
        :param entity: Entity
        :param string_value: Name of the entity
        """
        # return self._instance.SetEntityName(entity, string_value)
        raise NotImplemented

    def set_line_color(self, color):
        """
        Sets the color for the lines in the part document.
        :param color: Color definition as a COLORREF
        """
        # return self._instance.SetLineColor(color)
        raise NotImplemented

    def set_line_style(self, style_name):
        """
        Sets the style or font for the lines in the part document.
        :param style_name: Style or font for the line as defined in swLineStyles_e
        """
        # return self._instance.SetLineStyle(style_name)
        raise NotImplemented

    def set_line_width(self, width):
        """
        Sets the thickness or weight for the lines in the part document.
        :param width: Line thickness or weight as defined in swLineWeights_e
        """
        # return self._instance.SetLineWidth(width)
        raise NotImplemented

    def set_material_property_name(self, config_name, database, name):
        """
        Sets the name of the material property for the specified configuration.
        :param config_name: Name of configuration
        :param database: Name of the material database (see Remarks)
        :param name: Name of material (see Remarks)
        """
        # return self._instance.SetMaterialPropertyName2(config_name, database, name)
        raise NotImplemented

    def set_material_visual_properties(self, properties, config_option, config_names):
        """
        Sets the material visual properties for the active configuration and any specified configurations of this part.
        :param properties: Material visual properties
        :param config_option: Configurations as defined in swInConfigurationOpts_e
        :param config_names: Array of strings of the names of the configurations whose material visual properties to set
        """
        # return self._instance.SetMaterialVisualProperties(properties, config_option, config_names)
        raise NotImplemented

    def show_exploded(self, show_it, explode_view_name):
        """
        Displays the specified explode view for this multibody part.
        :param show_it: True to show ExplodeViewName in its exploded state, false to show it in its collapsed state
        :param explode_view_name: Name of the explode view to show
        """
        # return self._instance.ShowExploded(show_it, explode_view_name)
        raise NotImplemented
