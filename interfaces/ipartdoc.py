# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html
class IPartDoc:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def i_material_property_values(self):
        """Gets or sets a material's properties in the active configuration."""
        return self._instance.IMaterialPropertyValues

    @i_material_property_values.setter
    def i_material_property_values(self, value):
        """Gets or sets a material's properties in the active configuration."""
        self._instance.IMaterialPropertyValues = value

    @property
    def material_id_name(self):
        """Gets or sets the material name."""
        return self._instance.MaterialIdName

    @material_id_name.setter
    def material_id_name(self, value):
        """Gets or sets the material name."""
        self._instance.MaterialIdName = value

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
        """Gets or sets the material name. This name is visible to the user."""
        return self._instance.MaterialUserName

    @material_user_name.setter
    def material_user_name(self, value):
        """Gets or sets the material name. This name is visible to the user."""
        self._instance.MaterialUserName = value

    @property
    def add_property_extension(self):
        """Adds a property extension to this part."""
        return self._instance.AddPropertyExtension

    @add_property_extension.setter
    def add_property_extension(self, value):
        """Adds a property extension to this part."""
        self._instance.AddPropertyExtension = value

    @property
    def create_exploded_view(self):
        """Creates an explode view of this multibody part."""
        return self._instance.CreateExplodedView

    @create_exploded_view.setter
    def create_exploded_view(self, value):
        """Creates an explode view of this multibody part."""
        self._instance.CreateExplodedView = value

    @property
    def create_feature_from_body(self):
        """Creates a new imported feature from the specified temporary body."""
        return self._instance.CreateFeatureFromBody3

    @create_feature_from_body.setter
    def create_feature_from_body(self, value):
        """Creates a new imported feature from the specified temporary body."""
        self._instance.CreateFeatureFromBody3 = value

    @property
    def create_new_body(self):
        """Creates a new body to use for import sewing operations and returns it to the caller."""
        return self._instance.CreateNewBody

    @create_new_body.setter
    def create_new_body(self, value):
        """Creates a new body to use for import sewing operations and returns it to the caller."""
        self._instance.CreateNewBody = value

    @property
    def create_surface_feature_from_body(self):
        """Creates a surface feature from a body."""
        return self._instance.CreateSurfaceFeatureFromBody

    @create_surface_feature_from_body.setter
    def create_surface_feature_from_body(self, value):
        """Creates a surface feature from a body."""
        self._instance.CreateSurfaceFeatureFromBody = value

    @property
    def delete_entity_name(self):
        """Deletes the name associated with the specified entity."""
        return self._instance.DeleteEntityName

    @delete_entity_name.setter
    def delete_entity_name(self, value):
        """Deletes the name associated with the specified entity."""
        self._instance.DeleteEntityName = value

    @property
    def edit_rollback(self):
        """Rolls back the part's history to the feature just before the currently selected feature in the FeatureManager
        design tree."""
        return self._instance.EditRollback

    @edit_rollback.setter
    def edit_rollback(self, value):
        """Rolls back the part's history to the feature just before the currently selected feature in the FeatureManager
        design tree."""
        self._instance.EditRollback = value

    @property
    def enum_bodies(self):
        """Enumerates the bodies in this part."""
        return self._instance.EnumBodies3

    @enum_bodies.setter
    def enum_bodies(self, value):
        """Enumerates the bodies in this part."""
        self._instance.EnumBodies3 = value

    @property
    def enum_related_bodies(self):
        """Creates an enumerated list of bodies."""
        return self._instance.EnumRelatedBodies2

    @enum_related_bodies.setter
    def enum_related_bodies(self, value):
        """Creates an enumerated list of bodies."""
        self._instance.EnumRelatedBodies2 = value

    @property
    def enum_related_sectioned_bodies(self):
        """Gets an enumeration of the related sectioned bodies in a part."""
        return self._instance.EnumRelatedSectionedBodies2

    @enum_related_sectioned_bodies.setter
    def enum_related_sectioned_bodies(self, value):
        """Gets an enumeration of the related sectioned bodies in a part."""
        self._instance.EnumRelatedSectionedBodies2 = value

    @property
    def export_to_d_w_g(self):
        """Saves various aspects of a part (sheet metal, faces, loops, and annotation views) to one or more DXF/DWG
        files, preserving the specified file name."""
        return self._instance.ExportToDWG2

    @export_to_d_w_g.setter
    def export_to_d_w_g(self, value):
        """Saves various aspects of a part (sheet metal, faces, loops, and annotation views) to one or more DXF/DWG
        iles, preserving the specified file name."""
        self._instance.ExportToDWG2 = value

    @property
    def feature_by_id(self):
        """Gets the feature with the specified ID in the part."""
        return self._instance.FeatureById

    @feature_by_id.setter
    def feature_by_id(self, value):
        """Gets the feature with the specified ID in the part."""
        self._instance.FeatureById = value

    @property
    def feature_by_name(self):
        """Gets the named feature in the part."""
        return self._instance.FeatureByName

    @feature_by_name.setter
    def feature_by_name(self, value):
        """Gets the named feature in the part."""
        self._instance.FeatureByName = value

    @property
    def feature_xpert(self):
        """Executes FeatureXpert, powered by SOLIDWORKS Intelligent Feature Technology ( SWIFT), in parts."""
        return self._instance.FeatureXpert

    @feature_xpert.setter
    def feature_xpert(self, value):
        """Executes FeatureXpert, powered by SOLIDWORKS Intelligent Feature Technology ( SWIFT), in parts."""
        self._instance.FeatureXpert = value

    @property
    def first_feature(self):
        """Gets the first feature in the part."""
        return self._instance.FirstFeature

    @first_feature.setter
    def first_feature(self, value):
        """Gets the first feature in the part."""
        self._instance.FirstFeature = value

    @property
    def get_bodies(self):
        """Gets the bodies in this part."""
        return self._instance.GetBodies2

    @get_bodies.setter
    def get_bodies(self, value):
        """Gets the bodies in this part."""
        self._instance.GetBodies2 = value

    @property
    def get_entity_by_name(self):
        """Gets an entity (face, edge, vertex) by name."""
        return self._instance.GetEntityByName

    @get_entity_by_name.setter
    def get_entity_by_name(self, value):
        """Gets an entity (face, edge, vertex) by name."""
        self._instance.GetEntityByName = value

    @property
    def get_entity_name(self):
        """Gets the name of the specified entity."""
        return self._instance.GetEntityName

    @get_entity_name.setter
    def get_entity_name(self, value):
        """Gets the name of the specified entity."""
        self._instance.GetEntityName = value

    @property
    def get_exploded_view_configuration_name(self):
        """Gets the name of the configuration for the specified explode view of this multibody part."""
        return self._instance.GetExplodedViewConfigurationName

    @get_exploded_view_configuration_name.setter
    def get_exploded_view_configuration_name(self, value):
        """Gets the name of the configuration for the specified explode view of this multibody part."""
        self._instance.GetExplodedViewConfigurationName = value

    @property
    def get_exploded_view_count(self):
        """Gets the number of explode views in the specified configuration of this multibody part."""
        return self._instance.GetExplodedViewCount

    @get_exploded_view_count.setter
    def get_exploded_view_count(self, value):
        """Gets the number of explode views in the specified configuration of this multibody part."""
        self._instance.GetExplodedViewCount = value

    @property
    def get_exploded_view_names(self):
        """Gets the names of all the explode views in the specified configuration of this multibody part."""
        return self._instance.GetExplodedViewNames

    @get_exploded_view_names.setter
    def get_exploded_view_names(self, value):
        """Gets the names of all the explode views in the specified configuration of this multibody part."""
        self._instance.GetExplodedViewNames = value

    @property
    def get_mate_reference_entity(self):
        """Gets the mate reference entity."""
        return self._instance.GetMateReferenceEntity

    @get_mate_reference_entity.setter
    def get_mate_reference_entity(self, value):
        """Gets the mate reference entity."""
        self._instance.GetMateReferenceEntity = value

    @property
    def get_material_property_name(self):
        """Gets the names of the material database and the material for the specified configuration."""
        return self._instance.GetMaterialPropertyName2

    @get_material_property_name.setter
    def get_material_property_name(self, value):
        """Gets the names of the material database and the material for the specified configuration."""
        self._instance.GetMaterialPropertyName2 = value

    @property
    def get_material_visual_properties(self):
        """Gets the material visual properties for this part."""
        return self._instance.GetMaterialVisualProperties

    @get_material_visual_properties.setter
    def get_material_visual_properties(self, value):
        """Gets the material visual properties for this part."""
        self._instance.GetMaterialVisualProperties = value

    @property
    def get_named_entities(self):
        """Gets an array of names of named entities (face, edge, vertex, and so on) in this part."""
        return self._instance.GetNamedEntities

    @get_named_entities.setter
    def get_named_entities(self, value):
        """Gets an array of names of named entities (face, edge, vertex, and so on) in this part."""
        self._instance.GetNamedEntities = value

    @property
    def get_named_entities_count(self):
        """Gets the number of named entities (face, edge, vertex, and so on) in this part."""
        return self._instance.GetNamedEntitiesCount

    @get_named_entities_count.setter
    def get_named_entities_count(self, value):
        """Gets the number of named entities (face, edge, vertex, and so on) in this part."""
        self._instance.GetNamedEntitiesCount = value

    @property
    def get_part_box(self):
        """Gets the box enclosing the part."""
        return self._instance.GetPartBox

    @get_part_box.setter
    def get_part_box(self, value):
        """Gets the box enclosing the part."""
        self._instance.GetPartBox = value

    @property
    def get_property_extension(self):
        """Gets the specified property extension on this part document."""
        return self._instance.GetPropertyExtension

    @get_property_extension.setter
    def get_property_extension(self, value):
        """Gets the specified property extension on this part document."""
        self._instance.GetPropertyExtension = value

    @property
    def get_related_bodies(self):
        """Creates a list of all the related bodies in a part."""
        return self._instance.GetRelatedBodies

    @get_related_bodies.setter
    def get_related_bodies(self, value):
        """Creates a list of all the related bodies in a part."""
        self._instance.GetRelatedBodies = value

    @property
    def get_related_sectioned_bodies(self):
        """Gets all of the related sectioned bodies in a part."""
        return self._instance.GetRelatedSectionedBodies

    @get_related_sectioned_bodies.setter
    def get_related_sectioned_bodies(self, value):
        """Gets all of the related sectioned bodies in a part."""
        self._instance.GetRelatedSectionedBodies = value

    @property
    def get_sectioned_body(self):
        """Gets the sectioned body seen in the specified drawing view."""
        return self._instance.GetSectionedBody

    @get_sectioned_body.setter
    def get_sectioned_body(self, value):
        """Gets the sectioned body seen in the specified drawing view."""
        self._instance.GetSectionedBody = value

    @property
    def get_tess_norms(self):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation."""
        return self._instance.GetTessNorms

    @get_tess_norms.setter
    def get_tess_norms(self, value):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation."""
        self._instance.GetTessNorms = value

    @property
    def get_tess_triangle_count(self):
        """Gets the number of triangles that make up the shaded picture tessellation for this part."""
        return self._instance.GetTessTriangleCount

    @get_tess_triangle_count.setter
    def get_tess_triangle_count(self, value):
        """Gets the number of triangles that make up the shaded picture tessellation for this part."""
        self._instance.GetTessTriangleCount = value

    @property
    def get_tess_triangles(self):
        """Gets the triangles that make up the shaded picture tessellation for this part."""
        return self._instance.GetTessTriangles

    @get_tess_triangles.setter
    def get_tess_triangles(self, value):
        """Gets the triangles that make up the shaded picture tessellation for this part."""
        self._instance.GetTessTriangles = value

    @property
    def get_tess_tri_strip_edges(self):
        """Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part."""
        return self._instance.GetTessTriStripEdges

    @get_tess_tri_strip_edges.setter
    def get_tess_tri_strip_edges(self, value):
        """Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part."""
        self._instance.GetTessTriStripEdges = value

    @property
    def get_tess_tri_strip_norms(self):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this
        part."""
        return self._instance.GetTessTriStripNorms

    @get_tess_tri_strip_norms.setter
    def get_tess_tri_strip_norms(self, value):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this
        part."""
        self._instance.GetTessTriStripNorms = value

    @property
    def get_tess_tri_strips(self):
        """Gets the vertices that make up the shaded picture tessellation for this part."""
        return self._instance.GetTessTriStrips

    @get_tess_tri_strips.setter
    def get_tess_tri_strips(self, value):
        """Gets the vertices that make up the shaded picture tessellation for this part."""
        self._instance.GetTessTriStrips = value

    @property
    def get_tess_tri_strip_size(self):
        """Gets the size of the array floats required to contain the data returned when calling
        IPartDoc::GetTessTriStrips and IPartDoc::IGetTessTriStrips."""
        return self._instance.GetTessTriStripSize

    @get_tess_tri_strip_size.setter
    def get_tess_tri_strip_size(self, value):
        """Gets the size of the array floats required to contain the data returned when calling
        IPartDoc::GetTessTriStrips and IPartDoc::IGetTessTriStrips."""
        self._instance.GetTessTriStripSize = value

    @property
    def i_create_feature_from_body(self):
        """Creates a new imported feature from the specified temporary body."""
        return self._instance.ICreateFeatureFromBody4

    @i_create_feature_from_body.setter
    def i_create_feature_from_body(self, value):
        """Creates a new imported feature from the specified temporary body."""
        self._instance.ICreateFeatureFromBody4 = value

    @property
    def i_create_new_body(self):
        """Creates a new body to use for import sewing operations and returns it to the caller."""
        return self._instance.ICreateNewBody2

    @i_create_new_body.setter
    def i_create_new_body(self, value):
        """Creates a new body to use for import sewing operations and returns it to the caller."""
        self._instance.ICreateNewBody2 = value

    @property
    def i_create_surface_feature_from_body(self):
        """Creates a surface feature from a body."""
        return self._instance.ICreateSurfaceFeatureFromBody

    @i_create_surface_feature_from_body.setter
    def i_create_surface_feature_from_body(self, value):
        """Creates a surface feature from a body."""
        self._instance.ICreateSurfaceFeatureFromBody = value

    @property
    def i_create_surface_feature_from_body_count(self):
        """Gets the number of surface features to create from the body."""
        return self._instance.ICreateSurfaceFeatureFromBodyCount2

    @i_create_surface_feature_from_body_count.setter
    def i_create_surface_feature_from_body_count(self, value):
        """Gets the number of surface features to create from the body."""
        self._instance.ICreateSurfaceFeatureFromBodyCount2 = value

    @property
    def i_delete_entity_name(self):
        """Deletes the name associated with the specified entity."""
        return self._instance.IDeleteEntityName

    @i_delete_entity_name.setter
    def i_delete_entity_name(self, value):
        """Deletes the name associated with the specified entity."""
        self._instance.IDeleteEntityName = value

    @property
    def i_export_to_d_w_g(self):
        """Saves various aspects of a part (sheet metal, faces, loops, and annotation views) to one or more DXF/DWG
        files, preserving the specified filename."""
        return self._instance.IExportToDWG2

    @i_export_to_d_w_g.setter
    def i_export_to_d_w_g(self, value):
        """Saves various aspects of a part (sheet metal, faces, loops, and annotation views) to one or more DXF/DWG
        files, preserving the specified filename."""
        self._instance.IExportToDWG2 = value

    @property
    def i_feature_by_id(self):
        """Gets the feature with the specified ID in the part."""
        return self._instance.IFeatureById

    @i_feature_by_id.setter
    def i_feature_by_id(self, value):
        """Gets the feature with the specified ID in the part."""
        self._instance.IFeatureById = value

    @property
    def i_feature_by_name(self):
        """Gets the named feature in the part."""
        return self._instance.IFeatureByName

    @i_feature_by_name.setter
    def i_feature_by_name(self, value):
        """Gets the named feature in the part."""
        self._instance.IFeatureByName = value

    @property
    def i_first_feature(self):
        """Gets the first feature in the part."""
        return self._instance.IFirstFeature

    @i_first_feature.setter
    def i_first_feature(self, value):
        """Gets the first feature in the part."""
        self._instance.IFirstFeature = value

    @property
    def i_get_entity_by_name(self):
        """Gets an entity (face, edge, vertex) by name."""
        return self._instance.IGetEntityByName

    @i_get_entity_by_name.setter
    def i_get_entity_by_name(self, value):
        """Gets an entity (face, edge, vertex) by name."""
        self._instance.IGetEntityByName = value

    @property
    def i_get_entity_name(self):
        """Gets the name of the specified entity."""
        return self._instance.IGetEntityName

    @i_get_entity_name.setter
    def i_get_entity_name(self, value):
        """Gets the name of the specified entity."""
        self._instance.IGetEntityName = value

    @property
    def i_get_named_entities(self):
        """Gets an array of names of named entities (face, edge, vertex, and so on) in this part."""
        return self._instance.IGetNamedEntities

    @i_get_named_entities.setter
    def i_get_named_entities(self, value):
        """Gets an array of names of named entities (face, edge, vertex, and so on) in this part."""
        self._instance.IGetNamedEntities = value

    @property
    def i_get_part_box(self):
        """Gets the box enclosing the part."""
        return self._instance.IGetPartBox

    @i_get_part_box.setter
    def i_get_part_box(self, value):
        """Gets the box enclosing the part."""
        self._instance.IGetPartBox = value

    @property
    def i_get_processed_body(self):
        """Pre-processes the geometry of a body so that:


Closed periodic faces (for example, the lateral face of a cylinder) are split into two faces.

Faces that straddle the seam, if any, of the underlying surface are split into two faces."""
        return self._instance.IGetProcessedBody2

    @i_get_processed_body.setter
    def i_get_processed_body(self, value):
        """Pre-processes the geometry of a body so that:


Closed periodic faces (for example, the lateral face of a cylinder) are split into two faces.

Faces that straddle the seam, if any, of the underlying surface are split into two faces."""
        self._instance.IGetProcessedBody2 = value

    @property
    def i_get_processed_body_with_sel_face(self):
        """Gets a processed body."""
        return self._instance.IGetProcessedBodyWithSelFace2

    @i_get_processed_body_with_sel_face.setter
    def i_get_processed_body_with_sel_face(self, value):
        """Gets a processed body."""
        self._instance.IGetProcessedBodyWithSelFace2 = value

    @property
    def i_get_sectioned_body(self):
        """Gets the sectioned body seen in the specified drawing view."""
        return self._instance.IGetSectionedBody2

    @i_get_sectioned_body.setter
    def i_get_sectioned_body(self, value):
        """Gets the sectioned body seen in the specified drawing view."""
        self._instance.IGetSectionedBody2 = value

    @property
    def i_get_tess_norms(self):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation."""
        return self._instance.IGetTessNorms

    @i_get_tess_norms.setter
    def i_get_tess_norms(self, value):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation."""
        self._instance.IGetTessNorms = value

    @property
    def i_get_tess_triangles(self):
        """Gets the triangles that make up the shaded picture tessellation for this part."""
        return self._instance.IGetTessTriangles

    @i_get_tess_triangles.setter
    def i_get_tess_triangles(self, value):
        """Gets the triangles that make up the shaded picture tessellation for this part."""
        self._instance.IGetTessTriangles = value

    @property
    def i_get_tess_tri_strip_edges(self):
        """Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part."""
        return self._instance.IGetTessTriStripEdges

    @i_get_tess_tri_strip_edges.setter
    def i_get_tess_tri_strip_edges(self, value):
        """Gets the edge ID for each of the edges in the triangles that make up the tessellation for this part."""
        self._instance.IGetTessTriStripEdges = value

    @property
    def i_get_tess_tri_strip_edge_size(self):
        """Gets the size of the array returned by IPartDoc::GetTessTriStripEdges and IPartDoc::IGetTessTriStripEdges."""
        return self._instance.IGetTessTriStripEdgeSize

    @i_get_tess_tri_strip_edge_size.setter
    def i_get_tess_tri_strip_edge_size(self, value):
        """Gets the size of the array returned by IPartDoc::GetTessTriStripEdges and IPartDoc::IGetTessTriStripEdges."""
        self._instance.IGetTessTriStripEdgeSize = value

    @property
    def i_get_tess_tri_strip_norms(self):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this
        part."""
        return self._instance.IGetTessTriStripNorms

    @i_get_tess_tri_strip_norms.setter
    def i_get_tess_tri_strip_norms(self, value):
        """Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this
        part."""
        self._instance.IGetTessTriStripNorms = value

    @property
    def i_get_tess_tri_strips(self):
        """Gets the vertices that make up the shaded picture tessellation for this part."""
        return self._instance.IGetTessTriStrips

    @i_get_tess_tri_strips.setter
    def i_get_tess_tri_strips(self, value):
        """Gets the vertices that make up the shaded picture tessellation for this part."""
        self._instance.IGetTessTriStrips = value

    @property
    def import_diagnosis(self):
        """Diagnoses and repairs any gaps or bad faces on imported features."""
        return self._instance.ImportDiagnosis

    @import_diagnosis.setter
    def import_diagnosis(self, value):
        """Diagnoses and repairs any gaps or bad faces on imported features."""
        self._instance.ImportDiagnosis = value

    @property
    def import_diagnosis_gap_closer(self):
        """Allows you to repair a gap by moving the vertices on the edges surrounding the gap to new positions to close
        the gap on the imported model."""
        return self._instance.ImportDiagnosisGapCloser

    @import_diagnosis_gap_closer.setter
    def import_diagnosis_gap_closer(self, value):
        """Allows you to repair a gap by moving the vertices on the edges surrounding the gap to new positions to close
        the gap on the imported model."""
        self._instance.ImportDiagnosisGapCloser = value

    @property
    def insert_bend_notes(self):
        """Inserts bend notes for the specified flat-pattern feature of this sheet metal part."""
        return self._instance.InsertBendNotes

    @insert_bend_notes.setter
    def insert_bend_notes(self, value):
        """Inserts bend notes for the specified flat-pattern feature of this sheet metal part."""
        self._instance.InsertBendNotes = value

    @property
    def insert_bends(self):
        """Creates bends in a thin-feature part."""
        return self._instance.InsertBends2

    @insert_bends.setter
    def insert_bends(self, value):
        """Creates bends in a thin-feature part."""
        self._instance.InsertBends2 = value

    @property
    def insert_bend_table(self):
        """Creates a bend table annotation for the flat pattern of this sheet metal part."""
        return self._instance.InsertBendTable

    @insert_bend_table.setter
    def insert_bend_table(self, value):
        """Creates a bend table annotation for the flat pattern of this sheet metal part."""
        self._instance.InsertBendTable = value

    @property
    def insert_imported_feature(self):
        """Inserts a third-party native CAD file into this part."""
        return self._instance.InsertImportedFeature

    @insert_imported_feature.setter
    def insert_imported_feature(self, value):
        """Inserts a third-party native CAD file into this part."""
        self._instance.InsertImportedFeature = value

    @property
    def insert_mirror_all(self):
        """Mirrors the part about a selected planar face."""
        return self._instance.InsertMirrorAll

    @insert_mirror_all.setter
    def insert_mirror_all(self, value):
        """Mirrors the part about a selected planar face."""
        self._instance.InsertMirrorAll = value

    @property
    def insert_part(self):
        """Inserts the specified part in the specified configuration into this part."""
        return self._instance.InsertPart3

    @insert_part.setter
    def insert_part(self, value):
        """Inserts the specified part in the specified configuration into this part."""
        self._instance.InsertPart3 = value

    @property
    def i_set_entity_name(self):
        """Sets the name of the entity if the entity does not have a name."""
        return self._instance.ISetEntityName

    @i_set_entity_name.setter
    def i_set_entity_name(self, value):
        """Sets the name of the entity if the entity does not have a name."""
        self._instance.ISetEntityName = value

    @property
    def is_mirrored(self):
        """Gets whether this part is mirrored."""
        return self._instance.IsMirrored

    @is_mirrored.setter
    def is_mirrored(self, value):
        """Gets whether this part is mirrored."""
        self._instance.IsMirrored = value

    @property
    def is_weldment(self):
        """Gets whether this part contains a weldment feature."""
        return self._instance.IsWeldment

    @is_weldment.setter
    def is_weldment(self, value):
        """Gets whether this part contains a weldment feature."""
        self._instance.IsWeldment = value

    @property
    def make_section(self):
        """Saves sketch profiles for use in the wizard."""
        return self._instance.MakeSection

    @make_section.setter
    def make_section(self, value):
        """Saves sketch profiles for use in the wizard."""
        self._instance.MakeSection = value

    @property
    def mirror_feature(self):
        """Displays a dialog that allows the end-user to mirror a feature about a selected plane or planar face."""
        return self._instance.MirrorFeature

    @mirror_feature.setter
    def mirror_feature(self, value):
        """Displays a dialog that allows the end-user to mirror a feature about a selected plane or planar face."""
        self._instance.MirrorFeature = value

    @property
    def mirror_part(self):
        """Creates a new part document that mirrors this part about a selected reference plane or planar face."""
        return self._instance.MirrorPart2

    @mirror_part.setter
    def mirror_part(self, value):
        """Creates a new part document that mirrors this part about a selected reference plane or planar face."""
        self._instance.MirrorPart2 = value

    @property
    def remove_all_display_states(self):
        """Removes all display states and appearances from this part document."""
        return self._instance.RemoveAllDisplayStates

    @remove_all_display_states.setter
    def remove_all_display_states(self, value):
        """Removes all display states and appearances from this part document."""
        self._instance.RemoveAllDisplayStates = value

    @property
    def reorder_feature(self):
        """Reorders features and their operations."""
        return self._instance.ReorderFeature

    @reorder_feature.setter
    def reorder_feature(self, value):
        """Reorders features and their operations."""
        self._instance.ReorderFeature = value

    @property
    def reset_property_extension(self):
        """Clears all values stored in the property extension."""
        return self._instance.ResetPropertyExtension

    @reset_property_extension.setter
    def reset_property_extension(self, value):
        """Clears all values stored in the property extension."""
        self._instance.ResetPropertyExtension = value

    @property
    def save_to_file(self):
        """Saves the selected weldment member, surface body, or solid body to another part document."""
        return self._instance.SaveToFile3

    @save_to_file.setter
    def save_to_file(self, value):
        """Saves the selected weldment member, surface body, or solid body to another part document."""
        self._instance.SaveToFile3 = value

    @property
    def set_cosmos_works_material(self):
        """Assigns the material to use during analysis to this part."""
        return self._instance.SetCosmosWorksMaterial

    @set_cosmos_works_material.setter
    def set_cosmos_works_material(self, value):
        """Assigns the material to use during analysis to this part."""
        self._instance.SetCosmosWorksMaterial = value

    @property
    def set_dropped_file_name(self):
        """Sets the filename for a recently dropped file."""
        return self._instance.SetDroppedFileName

    @set_dropped_file_name.setter
    def set_dropped_file_name(self, value):
        """Sets the filename for a recently dropped file."""
        self._instance.SetDroppedFileName = value

    @property
    def set_entity_name(self):
        """Sets the name of the entity if the entity does not have a name and the name is unique to the part."""
        return self._instance.SetEntityName

    @set_entity_name.setter
    def set_entity_name(self, value):
        """Sets the name of the entity if the entity does not have a name and the name is unique to the part."""
        self._instance.SetEntityName = value

    @property
    def set_line_color(self):
        """Sets the color for the lines in the part document."""
        return self._instance.SetLineColor

    @set_line_color.setter
    def set_line_color(self, value):
        """Sets the color for the lines in the part document."""
        self._instance.SetLineColor = value

    @property
    def set_line_style(self):
        """Sets the style or font for the lines in the part document."""
        return self._instance.SetLineStyle

    @set_line_style.setter
    def set_line_style(self, value):
        """Sets the style or font for the lines in the part document."""
        self._instance.SetLineStyle = value

    @property
    def set_line_width(self):
        """Sets the thickness or weight for the lines in the part document."""
        return self._instance.SetLineWidth

    @set_line_width.setter
    def set_line_width(self, value):
        """Sets the thickness or weight for the lines in the part document."""
        self._instance.SetLineWidth = value

    @property
    def set_material_property_name(self):
        """Sets the name of the material property for the specified configuration."""
        return self._instance.SetMaterialPropertyName2

    @set_material_property_name.setter
    def set_material_property_name(self, value):
        """Sets the name of the material property for the specified configuration."""
        self._instance.SetMaterialPropertyName2 = value

    @property
    def set_material_visual_properties(self):
        """Sets the material visual properties for the active configuration and any specified configurations of this
        part."""
        return self._instance.SetMaterialVisualProperties

    @set_material_visual_properties.setter
    def set_material_visual_properties(self, value):
        """Sets the material visual properties for the active configuration and any specified configurations of this
        part."""
        self._instance.SetMaterialVisualProperties = value

    @property
    def show_exploded(self):
        """Displays the specified explode view for this multibody part."""
        return self._instance.ShowExploded

    @show_exploded.setter
    def show_exploded(self, value):
        """Displays the specified explode view for this multibody part."""
        self._instance.ShowExploded = value
