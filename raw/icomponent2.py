# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html
class IComponent2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def component_reference(self):
		"""Gets or sets a component reference for this component."""
		return self._instance.ComponentReference

	@component_reference.setter
	def component_reference(self, value):
		"""Gets or sets a component reference for this component."""
		self._instance.ComponentReference = value

	@property
	def display_title(self):
		"""Gets this component's title as displayed in the FeatureManager design tree."""
		return self._instance.DisplayTitle

	@display_title.setter
	def display_title(self, value):
		"""Gets this component's title as displayed in the FeatureManager design tree."""
		self._instance.DisplayTitle = value

	@property
	def i_material_property_values(self):
		"""Gets or sets the material properties for the selected component in the active configuration."""
		return self._instance.IMaterialPropertyValues

	@i_material_property_values.setter
	def i_material_property_values(self, value):
		"""Gets or sets the material properties for the selected component in the active configuration."""
		self._instance.IMaterialPropertyValues = value

	@property
	def is_graphics_only(self):
		"""Gets whether this component is graphics only."""
		return self._instance.IsGraphicsOnly

	@is_graphics_only.setter
	def is_graphics_only(self, value):
		"""Gets whether this component is graphics only."""
		self._instance.IsGraphicsOnly = value

	@property
	def is_speed_pak(self):
		"""Gets whether the active configuration for this component is SpeedPak."""
		return self._instance.IsSpeedPak

	@is_speed_pak.setter
	def is_speed_pak(self, value):
		"""Gets whether the active configuration for this component is SpeedPak."""
		self._instance.IsSpeedPak = value

	@property
	def is_virtual(self):
		"""Gets whether this component is a virtual component.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.IsVirtual

	@is_virtual.setter
	def is_virtual(self, value):
		"""Gets whether this component is a virtual component.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.IsVirtual = value

	@property
	def material_property_values(self):
		"""Gets or sets the material properties for the selected component in the active configuration."""
		return self._instance.MaterialPropertyValues

	@material_property_values.setter
	def material_property_values(self, value):
		"""Gets or sets the material properties for the selected component in the active configuration."""
		self._instance.MaterialPropertyValues = value

	@property
	def name(self):
		"""Gets or sets the name of the selected component."""
		return self._instance.Name2

	@name.setter
	def name(self, value):
		"""Gets or sets the name of the selected component."""
		self._instance.Name2 = value

	@property
	def presentation_transform(self):
		"""Gets or sets the component transform."""
		return self._instance.PresentationTransform

	@presentation_transform.setter
	def presentation_transform(self, value):
		"""Gets or sets the component transform."""
		self._instance.PresentationTransform = value

	@property
	def referenced_configuration(self):
		"""Gets or sets the active configuration used by this component."""
		return self._instance.ReferencedConfiguration

	@referenced_configuration.setter
	def referenced_configuration(self, value):
		"""Gets or sets the active configuration used by this component."""
		self._instance.ReferencedConfiguration = value

	@property
	def referenced_display_state(self):
		"""Gets or sets the active display state of this component."""
		return self._instance.ReferencedDisplayState2

	@referenced_display_state.setter
	def referenced_display_state(self, value):
		"""Gets or sets the active display state of this component."""
		self._instance.ReferencedDisplayState2 = value

	@property
	def solving(self):
		"""Gets the Solve as option (rigid or flexible) of this component."""
		return self._instance.Solving

	@solving.setter
	def solving(self, value):
		"""Gets the Solve as option (rigid or flexible) of this component."""
		self._instance.Solving = value

	@property
	def transform(self):
		"""Gets or sets the component transform."""
		return self._instance.Transform2

	@transform.setter
	def transform(self, value):
		"""Gets or sets the component transform."""
		self._instance.Transform2 = value

	@property
	def use_named_configuration(self):
		"""Gets whether a specified configuration or the in-use/last active configuration is used."""
		return self._instance.UseNamedConfiguration

	@use_named_configuration.setter
	def use_named_configuration(self, value):
		"""Gets whether a specified configuration or the in-use/last active configuration is used."""
		self._instance.UseNamedConfiguration = value

	@property
	def visible(self):
		"""Gets or sets the visibility state of this component."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets the visibility state of this component."""
		self._instance.Visible = value

	@property
	def add_property_extension(self):
		"""Adds a property extension to this component."""
		return self._instance.AddPropertyExtension

	@add_property_extension.setter
	def add_property_extension(self, value):
		"""Adds a property extension to this component."""
		self._instance.AddPropertyExtension = value

	@property
	def de_select(self):
		"""Deselects this component."""
		return self._instance.DeSelect

	@de_select.setter
	def de_select(self, value):
		"""Deselects this component."""
		self._instance.DeSelect = value

	@property
	def enum_bodies(self):
		"""Gets the bodies in the component in a multibody part."""
		return self._instance.EnumBodies3

	@enum_bodies.setter
	def enum_bodies(self, value):
		"""Gets the bodies in the component in a multibody part."""
		self._instance.EnumBodies3 = value

	@property
	def enum_related_bodies(self):
		"""Creates an enumerated list of bodies."""
		return self._instance.EnumRelatedBodies

	@enum_related_bodies.setter
	def enum_related_bodies(self, value):
		"""Creates an enumerated list of bodies."""
		self._instance.EnumRelatedBodies = value

	@property
	def enum_sectioned_bodies(self):
		"""Gets the sectioned bodies seen in the specified view and returns them in an enumerated list."""
		return self._instance.EnumSectionedBodies

	@enum_sectioned_bodies.setter
	def enum_sectioned_bodies(self, value):
		"""Gets the sectioned bodies seen in the specified view and returns them in an enumerated list."""
		self._instance.EnumSectionedBodies = value

	@property
	def feature_by_name(self):
		"""Gets the specified feature for this component."""
		return self._instance.FeatureByName

	@feature_by_name.setter
	def feature_by_name(self, value):
		"""Gets the specified feature for this component."""
		self._instance.FeatureByName = value

	@property
	def find_attribute(self):
		"""Finds an attribute on a component."""
		return self._instance.FindAttribute

	@find_attribute.setter
	def find_attribute(self, value):
		"""Finds an attribute on a component."""
		self._instance.FindAttribute = value

	@property
	def first_feature(self):
		"""Gets the first feature in this component."""
		return self._instance.FirstFeature

	@first_feature.setter
	def first_feature(self, value):
		"""Gets the first feature in this component."""
		self._instance.FirstFeature = value

	@property
	def get_bodies(self):
		"""Gets the bodies in this component."""
		return self._instance.GetBodies3

	@get_bodies.setter
	def get_bodies(self, value):
		"""Gets the bodies in this component."""
		self._instance.GetBodies3 = value

	@property
	def get_body(self):
		"""Gets the body that belongs to this instance of this component."""
		return self._instance.GetBody

	@get_body.setter
	def get_body(self, value):
		"""Gets the body that belongs to this instance of this component."""
		self._instance.GetBody = value

	@property
	def get_box(self):
		"""Gets the bounding box for component."""
		return self._instance.GetBox

	@get_box.setter
	def get_box(self, value):
		"""Gets the bounding box for component."""
		self._instance.GetBox = value

	@property
	def get_children(self):
		"""Gets all of the children components of this component."""
		return self._instance.GetChildren

	@get_children.setter
	def get_children(self, value):
		"""Gets all of the children components of this component."""
		self._instance.GetChildren = value

	@property
	def get_constrained_status(self):
		"""Gets the constrained status of this component."""
		return self._instance.GetConstrainedStatus

	@get_constrained_status.setter
	def get_constrained_status(self, value):
		"""Gets the constrained status of this component."""
		self._instance.GetConstrainedStatus = value

	@property
	def get_corresponding(self):
		"""Gets the corresponding object in the context of the assembly for a specific instance of the component."""
		return self._instance.GetCorresponding

	@get_corresponding.setter
	def get_corresponding(self, value):
		"""Gets the corresponding object in the context of the assembly for a specific instance of the component."""
		self._instance.GetCorresponding = value

	@property
	def get_corresponding_entity(self):
		"""Gets the entity that corresponds with the Dispatch pointer in the context of the component."""
		return self._instance.GetCorrespondingEntity

	@get_corresponding_entity.setter
	def get_corresponding_entity(self, value):
		"""Gets the entity that corresponds with the Dispatch pointer in the context of the component."""
		self._instance.GetCorrespondingEntity = value

	@property
	def get_decals(self):
		"""Gets the decals applied to this component."""
		return self._instance.GetDecals

	@get_decals.setter
	def get_decals(self, value):
		"""Gets the decals applied to this component."""
		self._instance.GetDecals = value

	@property
	def get_decals_count(self):
		"""Gets the number of decals applied to this component."""
		return self._instance.GetDecalsCount

	@get_decals_count.setter
	def get_decals_count(self, value):
		"""Gets the number of decals applied to this component."""
		self._instance.GetDecalsCount = value

	@property
	def get_drawing_component(self):
		"""Gets the drawing component for this component."""
		return self._instance.GetDrawingComponent

	@get_drawing_component.setter
	def get_drawing_component(self, value):
		"""Gets the drawing component for this component."""
		self._instance.GetDrawingComponent = value

	@property
	def get_exclude_from_b_o_m(self):
		"""Gets whether this component is excluded from the bills of materials (BOMs) in the specified configurations."""
		return self._instance.GetExcludeFromBOM2

	@get_exclude_from_b_o_m.setter
	def get_exclude_from_b_o_m(self, value):
		"""Gets whether this component is excluded from the bills of materials (BOMs) in the specified configurations."""
		self._instance.GetExcludeFromBOM2 = value

	@property
	def get_hidden_unloaded_children_count(self):
		"""Gets the number of hidden children components of this component that were not loaded when an assembly was opened selectively."""
		return self._instance.GetHiddenUnloadedChildrenCount

	@get_hidden_unloaded_children_count.setter
	def get_hidden_unloaded_children_count(self, value):
		"""Gets the number of hidden children components of this component that were not loaded when an assembly was opened selectively."""
		self._instance.GetHiddenUnloadedChildrenCount = value

	@property
	def get_i_d(self):
		"""Gets the component ID for this component."""
		return self._instance.GetID

	@get_i_d.setter
	def get_i_d(self, value):
		"""Gets the component ID for this component."""
		self._instance.GetID = value

	@property
	def get_imported_path(self):
		"""Gets the full path name of the model imported for this component."""
		return self._instance.GetImportedPath

	@get_imported_path.setter
	def get_imported_path(self, value):
		"""Gets the full path name of the model imported for this component."""
		self._instance.GetImportedPath = value

	@property
	def get_material_id_name(self):
		"""Gets the material name for this component."""
		return self._instance.GetMaterialIdName

	@get_material_id_name.setter
	def get_material_id_name(self, value):
		"""Gets the material name for this component."""
		self._instance.GetMaterialIdName = value

	@property
	def get_material_property_values(self):
		"""Gets the material properties for this component."""
		return self._instance.GetMaterialPropertyValues2

	@get_material_property_values.setter
	def get_material_property_values(self, value):
		"""Gets the material properties for this component."""
		self._instance.GetMaterialPropertyValues2 = value

	@property
	def get_material_user_name(self):
		"""Gets the user-visible name of the material for this component."""
		return self._instance.GetMaterialUserName

	@get_material_user_name.setter
	def get_material_user_name(self, value):
		"""Gets the user-visible name of the material for this component."""
		self._instance.GetMaterialUserName = value

	@property
	def get_mates(self):
		"""Gets the mates for this component."""
		return self._instance.GetMates

	@get_mates.setter
	def get_mates(self, value):
		"""Gets the mates for this component."""
		self._instance.GetMates = value

	@property
	def get_model_doc(self):
		"""Gets the model document for this component."""
		return self._instance.GetModelDoc2

	@get_model_doc.setter
	def get_model_doc(self, value):
		"""Gets the model document for this component."""
		self._instance.GetModelDoc2 = value

	@property
	def get_model_material_property_values(self):
		"""Gets the material properties of this lightweight component in the specified configuration."""
		return self._instance.GetModelMaterialPropertyValues

	@get_model_material_property_values.setter
	def get_model_material_property_values(self, value):
		"""Gets the material properties of this lightweight component in the specified configuration."""
		self._instance.GetModelMaterialPropertyValues = value

	@property
	def get_model_texture(self):
		"""Gets the texture applied to this lightweight component in the specified configuration."""
		return self._instance.GetModelTexture

	@get_model_texture.setter
	def get_model_texture(self, value):
		"""Gets the texture applied to this lightweight component in the specified configuration."""
		self._instance.GetModelTexture = value

	@property
	def get_parent(self):
		"""Gets the parent component."""
		return self._instance.GetParent

	@get_parent.setter
	def get_parent(self, value):
		"""Gets the parent component."""
		self._instance.GetParent = value

	@property
	def get_path_name(self):
		"""Gets the full path name for this component."""
		return self._instance.GetPathName

	@get_path_name.setter
	def get_path_name(self, value):
		"""Gets the full path name for this component."""
		self._instance.GetPathName = value

	@property
	def get_property_extension(self):
		"""Gets the property extension on this component."""
		return self._instance.GetPropertyExtension

	@get_property_extension.setter
	def get_property_extension(self, value):
		"""Gets the property extension on this component."""
		self._instance.GetPropertyExtension = value

	@property
	def get_referenced_display_states(self):
		"""Gets the display states of this component that are referenced by the specified assembly display state(s)."""
		return self._instance.GetReferencedDisplayStates

	@get_referenced_display_states.setter
	def get_referenced_display_states(self, value):
		"""Gets the display states of this component that are referenced by the specified assembly display state(s)."""
		self._instance.GetReferencedDisplayStates = value

	@property
	def get_render_materials(self):
		"""Gets the appearances applied to this component in the specified display states."""
		return self._instance.GetRenderMaterials2

	@get_render_materials.setter
	def get_render_materials(self, value):
		"""Gets the appearances applied to this component in the specified display states."""
		self._instance.GetRenderMaterials2 = value

	@property
	def get_render_materials_count(self):
		"""Gets the number of appearances applied to this component in the specified display states."""
		return self._instance.GetRenderMaterialsCount2

	@get_render_materials_count.setter
	def get_render_materials_count(self, value):
		"""Gets the number of appearances applied to this component in the specified display states."""
		self._instance.GetRenderMaterialsCount2 = value

	@property
	def get_sectioned_bodies(self):
		"""Gets the sectioned bodies in the specified section view."""
		return self._instance.GetSectionedBodies

	@get_sectioned_bodies.setter
	def get_sectioned_bodies(self, value):
		"""Gets the sectioned bodies in the specified section view."""
		self._instance.GetSectionedBodies = value

	@property
	def get_select_by_i_d_string(self):
		"""Gets the name of the component for possible use with IModelDocExtension::SelectByID2, for selectively opening a document using ISldWorks::OpenDoc7 and IDocumentSpecification, etc."""
		return self._instance.GetSelectByIDString

	@get_select_by_i_d_string.setter
	def get_select_by_i_d_string(self, value):
		"""Gets the name of the component for possible use with IModelDocExtension::SelectByID2, for selectively opening a document using ISldWorks::OpenDoc7 and IDocumentSpecification, etc."""
		self._instance.GetSelectByIDString = value

	@property
	def get_smart_component_data(self):
		"""Gets the features, components, and feature references of a Smart Component."""
		return self._instance.GetSmartComponentData

	@get_smart_component_data.setter
	def get_smart_component_data(self, value):
		"""Gets the features, components, and feature references of a Smart Component."""
		self._instance.GetSmartComponentData = value

	@property
	def get_specific_transform(self):
		"""Get the collapsed or exploded transform of a component when the assembly is exploded."""
		return self._instance.GetSpecificTransform

	@get_specific_transform.setter
	def get_specific_transform(self, value):
		"""Get the collapsed or exploded transform of a component when the assembly is exploded."""
		self._instance.GetSpecificTransform = value

	@property
	def get_suppression(self):
		"""Gets the suppression state of this component."""
		return self._instance.GetSuppression2

	@get_suppression.setter
	def get_suppression(self, value):
		"""Gets the suppression state of this component."""
		self._instance.GetSuppression2 = value

	@property
	def get_tess_norms(self):
		"""Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component."""
		return self._instance.GetTessNorms

	@get_tess_norms.setter
	def get_tess_norms(self, value):
		"""Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component."""
		self._instance.GetTessNorms = value

	@property
	def get_tess_triangles(self):
		"""Gets the triangles that make up the shaded picture tessellation for this component."""
		return self._instance.GetTessTriangles

	@get_tess_triangles.setter
	def get_tess_triangles(self, value):
		"""Gets the triangles that make up the shaded picture tessellation for this component."""
		self._instance.GetTessTriangles = value

	@property
	def get_tess_tri_strip_edges(self):
		"""Gets the edge IDs for the triangle strips."""
		return self._instance.GetTessTriStripEdges

	@get_tess_tri_strip_edges.setter
	def get_tess_tri_strip_edges(self, value):
		"""Gets the edge IDs for the triangle strips."""
		self._instance.GetTessTriStripEdges = value

	@property
	def get_tess_tri_strip_norms(self):
		"""Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component."""
		return self._instance.GetTessTriStripNorms

	@get_tess_tri_strip_norms.setter
	def get_tess_tri_strip_norms(self, value):
		"""Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component."""
		self._instance.GetTessTriStripNorms = value

	@property
	def get_tess_tri_strips(self):
		"""Gets the vertices that make up the shaded picture tessellation for this component."""
		return self._instance.GetTessTriStrips

	@get_tess_tri_strips.setter
	def get_tess_tri_strips(self, value):
		"""Gets the vertices that make up the shaded picture tessellation for this component."""
		self._instance.GetTessTriStrips = value

	@property
	def get_texture(self):
		"""Gets the texture applied to this component in the specified configuration."""
		return self._instance.GetTexture

	@get_texture.setter
	def get_texture(self, value):
		"""Gets the texture applied to this component in the specified configuration."""
		self._instance.GetTexture = value

	@property
	def get_total_transform(self):
		"""Combines the original transform of this component with the presentation transform of this component."""
		return self._instance.GetTotalTransform

	@get_total_transform.setter
	def get_total_transform(self, value):
		"""Combines the original transform of this component with the presentation transform of this component."""
		self._instance.GetTotalTransform = value

	@property
	def get_unloaded_component_names(self):
		"""Gets the component's unloaded children components' path names, referenced configuration names, reasons why they are unloaded, document types, and names."""
		return self._instance.GetUnloadedComponentNames

	@get_unloaded_component_names.setter
	def get_unloaded_component_names(self, value):
		"""Gets the component's unloaded children components' path names, referenced configuration names, reasons why they are unloaded, document types, and names."""
		self._instance.GetUnloadedComponentNames = value

	@property
	def get_visibility(self):
		"""Gets the visibility state for this component."""
		return self._instance.GetVisibility

	@get_visibility.setter
	def get_visibility(self, value):
		"""Gets the visibility state for this component."""
		self._instance.GetVisibility = value

	@property
	def get_visibility_in_asm_display_states(self):
		"""Gets the visibilities of this component in the specified assembly display state(s)."""
		return self._instance.GetVisibilityInAsmDisplayStates

	@get_visibility_in_asm_display_states.setter
	def get_visibility_in_asm_display_states(self, value):
		"""Gets the visibilities of this component in the specified assembly display state(s)."""
		self._instance.GetVisibilityInAsmDisplayStates = value

	@property
	def has_material_property_values(self):
		"""Gets whether this component has an appearance."""
		return self._instance.HasMaterialPropertyValues

	@has_material_property_values.setter
	def has_material_property_values(self, value):
		"""Gets whether this component has an appearance."""
		self._instance.HasMaterialPropertyValues = value

	@property
	def has_unloaded_components(self):
		"""Gets whether this component has hidden or suppressed unloaded children components."""
		return self._instance.HasUnloadedComponents

	@has_unloaded_components.setter
	def has_unloaded_components(self, value):
		"""Gets whether this component has hidden or suppressed unloaded children components."""
		self._instance.HasUnloadedComponents = value

	@property
	def i_find_attribute(self):
		"""Finds an attribute on a component."""
		return self._instance.IFindAttribute

	@i_find_attribute.setter
	def i_find_attribute(self, value):
		"""Finds an attribute on a component."""
		self._instance.IFindAttribute = value

	@property
	def i_get_body(self):
		"""Gets the body that belongs to this instance of this component."""
		return self._instance.IGetBody

	@i_get_body.setter
	def i_get_body(self, value):
		"""Gets the body that belongs to this instance of this component."""
		self._instance.IGetBody = value

	@property
	def i_get_box(self):
		"""Gets the bounding box for component."""
		return self._instance.IGetBox

	@i_get_box.setter
	def i_get_box(self, value):
		"""Gets the bounding box for component."""
		self._instance.IGetBox = value

	@property
	def i_get_children(self):
		"""Gets all of the children components of this component."""
		return self._instance.IGetChildren

	@i_get_children.setter
	def i_get_children(self, value):
		"""Gets all of the children components of this component."""
		self._instance.IGetChildren = value

	@property
	def i_get_children_count(self):
		"""Gets the number of children components for this component."""
		return self._instance.IGetChildrenCount

	@i_get_children_count.setter
	def i_get_children_count(self, value):
		"""Gets the number of children components for this component."""
		self._instance.IGetChildrenCount = value

	@property
	def i_get_corresponding_entity(self):
		"""Gets the entity that corresponds with the Dispatch pointer in the context of the component."""
		return self._instance.IGetCorrespondingEntity

	@i_get_corresponding_entity.setter
	def i_get_corresponding_entity(self, value):
		"""Gets the entity that corresponds with the Dispatch pointer in the context of the component."""
		self._instance.IGetCorrespondingEntity = value

	@property
	def i_get_decals(self):
		"""Gets the decals applied to this component."""
		return self._instance.IGetDecals

	@i_get_decals.setter
	def i_get_decals(self, value):
		"""Gets the decals applied to this component."""
		self._instance.IGetDecals = value

	@property
	def i_get_material_property_values(self):
		"""Gets the material properties for this component."""
		return self._instance.IGetMaterialPropertyValues2

	@i_get_material_property_values.setter
	def i_get_material_property_values(self, value):
		"""Gets the material properties for this component."""
		self._instance.IGetMaterialPropertyValues2 = value

	@property
	def i_get_material_property_values_for_face(self):
		"""Gets the color of the specified face."""
		return self._instance.IGetMaterialPropertyValuesForFace

	@i_get_material_property_values_for_face.setter
	def i_get_material_property_values_for_face(self, value):
		"""Gets the color of the specified face."""
		self._instance.IGetMaterialPropertyValuesForFace = value

	@property
	def i_get_model_material_property_values(self):
		"""Gets the material properties of this lightweight component in the specified configuration."""
		return self._instance.IGetModelMaterialPropertyValues

	@i_get_model_material_property_values.setter
	def i_get_model_material_property_values(self, value):
		"""Gets the material properties of this lightweight component in the specified configuration."""
		self._instance.IGetModelMaterialPropertyValues = value

	@property
	def i_get_temporary_body_i_d(self):
		"""Gets the current body tag ID, which is not a permanent ID."""
		return self._instance.IGetTemporaryBodyID

	@i_get_temporary_body_i_d.setter
	def i_get_temporary_body_i_d(self, value):
		"""Gets the current body tag ID, which is not a permanent ID."""
		self._instance.IGetTemporaryBodyID = value

	@property
	def i_get_tess_norms(self):
		"""Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component."""
		return self._instance.IGetTessNorms

	@i_get_tess_norms.setter
	def i_get_tess_norms(self, value):
		"""Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for the component."""
		self._instance.IGetTessNorms = value

	@property
	def i_get_tess_triangle_count(self):
		"""Gets the number of triangles that make up the shaded picture tessellation for this component."""
		return self._instance.IGetTessTriangleCount

	@i_get_tess_triangle_count.setter
	def i_get_tess_triangle_count(self, value):
		"""Gets the number of triangles that make up the shaded picture tessellation for this component."""
		self._instance.IGetTessTriangleCount = value

	@property
	def i_get_tess_triangles(self):
		"""Gets the triangles that make up the shaded picture tessellation for this component."""
		return self._instance.IGetTessTriangles

	@i_get_tess_triangles.setter
	def i_get_tess_triangles(self, value):
		"""Gets the triangles that make up the shaded picture tessellation for this component."""
		self._instance.IGetTessTriangles = value

	@property
	def i_get_tess_tri_strip_edges(self):
		"""Gets the edge IDs for the triangle strips."""
		return self._instance.IGetTessTriStripEdges

	@i_get_tess_tri_strip_edges.setter
	def i_get_tess_tri_strip_edges(self, value):
		"""Gets the edge IDs for the triangle strips."""
		self._instance.IGetTessTriStripEdges = value

	@property
	def i_get_tess_tri_strip_edge_size(self):
		"""Gets the number of tessellation triangle edges."""
		return self._instance.IGetTessTriStripEdgeSize

	@i_get_tess_tri_strip_edge_size.setter
	def i_get_tess_tri_strip_edge_size(self, value):
		"""Gets the number of tessellation triangle edges."""
		self._instance.IGetTessTriStripEdgeSize = value

	@property
	def i_get_tess_tri_strip_norms(self):
		"""Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component."""
		return self._instance.IGetTessTriStripNorms

	@i_get_tess_tri_strip_norms.setter
	def i_get_tess_tri_strip_norms(self, value):
		"""Gets the normal vector for each of the triangles, which make up the shaded picture tessellation for this component."""
		self._instance.IGetTessTriStripNorms = value

	@property
	def i_get_tess_tri_strips(self):
		"""Gets the vertices that make up the shaded picture tessellation for this component."""
		return self._instance.IGetTessTriStrips

	@i_get_tess_tri_strips.setter
	def i_get_tess_tri_strips(self, value):
		"""Gets the vertices that make up the shaded picture tessellation for this component."""
		self._instance.IGetTessTriStrips = value

	@property
	def i_get_tess_tri_strip_size(self):
		"""Gets the array size of floats required to contain the data returned when calling IComponent2::IGetTessTriStrips."""
		return self._instance.IGetTessTriStripSize

	@i_get_tess_tri_strip_size.setter
	def i_get_tess_tri_strip_size(self, value):
		"""Gets the array size of floats required to contain the data returned when calling IComponent2::IGetTessTriStrips."""
		self._instance.IGetTessTriStripSize = value

	@property
	def i_get_visibility(self):
		"""Gets the visibility state for this component."""
		return self._instance.IGetVisibility

	@i_get_visibility.setter
	def i_get_visibility(self, value):
		"""Gets the visibility state for this component."""
		self._instance.IGetVisibility = value

	@property
	def i_list_external_file_references(self):
		"""Gets the names and statuses of the external references on the component."""
		return self._instance.IListExternalFileReferences2

	@i_list_external_file_references.setter
	def i_list_external_file_references(self, value):
		"""Gets the names and statuses of the external references on the component."""
		self._instance.IListExternalFileReferences2 = value

	@property
	def i_remove_material_property(self):
		"""Removes material property values from the component."""
		return self._instance.IRemoveMaterialProperty2

	@i_remove_material_property.setter
	def i_remove_material_property(self, value):
		"""Removes material property values from the component."""
		self._instance.IRemoveMaterialProperty2 = value

	@property
	def is_display_data_out_of_date(self):
		"""Gets the status of the display data for this component."""
		return self._instance.IsDisplayDataOutOfDate

	@is_display_data_out_of_date.setter
	def is_display_data_out_of_date(self, value):
		"""Gets the status of the display data for this component."""
		self._instance.IsDisplayDataOutOfDate = value

	@property
	def is_envelope(self):
		"""Gets whether this component is an envelope."""
		return self._instance.IsEnvelope

	@is_envelope.setter
	def is_envelope(self, value):
		"""Gets whether this component is an envelope."""
		self._instance.IsEnvelope = value

	@property
	def i_set_material_property_values(self):
		"""Sets the material properties for this component."""
		return self._instance.ISetMaterialPropertyValues2

	@i_set_material_property_values.setter
	def i_set_material_property_values(self, value):
		"""Sets the material properties for this component."""
		self._instance.ISetMaterialPropertyValues2 = value

	@property
	def i_set_visibility(self):
		"""Sets the visibility state for this component."""
		return self._instance.ISetVisibility

	@i_set_visibility.setter
	def i_set_visibility(self, value):
		"""Sets the visibility state for this component."""
		self._instance.ISetVisibility = value

	@property
	def is_fixed(self):
		"""Gets whether the component is fixed or floating."""
		return self._instance.IsFixed

	@is_fixed.setter
	def is_fixed(self, value):
		"""Gets whether the component is fixed or floating."""
		self._instance.IsFixed = value

	@property
	def is_hidden(self):
		"""Gets whether this component is hidden or suppressed."""
		return self._instance.IsHidden

	@is_hidden.setter
	def is_hidden(self, value):
		"""Gets whether this component is hidden or suppressed."""
		self._instance.IsHidden = value

	@property
	def is_loaded(self):
		"""Gets whether a component is loaded."""
		return self._instance.IsLoaded

	@is_loaded.setter
	def is_loaded(self, value):
		"""Gets whether a component is loaded."""
		self._instance.IsLoaded = value

	@property
	def is_mirrored(self):
		"""Gets whether this component is mirrored."""
		return self._instance.IsMirrored

	@is_mirrored.setter
	def is_mirrored(self, value):
		"""Gets whether this component is mirrored."""
		self._instance.IsMirrored = value

	@property
	def is_pattern_instance(self):
		"""Gets whether the component is a member of a pattern instance."""
		return self._instance.IsPatternInstance

	@is_pattern_instance.setter
	def is_pattern_instance(self, value):
		"""Gets whether the component is a member of a pattern instance."""
		self._instance.IsPatternInstance = value

	@property
	def is_root(self):
		"""Gets whether this component is the root component."""
		return self._instance.IsRoot

	@is_root.setter
	def is_root(self, value):
		"""Gets whether this component is the root component."""
		self._instance.IsRoot = value

	@property
	def is_smart_component(self):
		"""Gets whether this component is a Smart Component."""
		return self._instance.IsSmartComponent

	@is_smart_component.setter
	def is_smart_component(self, value):
		"""Gets whether this component is a Smart Component."""
		self._instance.IsSmartComponent = value

	@property
	def is_suppressed(self):
		"""Gets whether this component is suppressed."""
		return self._instance.IsSuppressed

	@is_suppressed.setter
	def is_suppressed(self, value):
		"""Gets whether this component is suppressed."""
		self._instance.IsSuppressed = value

	@property
	def list_external_file_references(self):
		"""Gets the names and statuses of the external file references on the component."""
		return self._instance.ListExternalFileReferences2

	@list_external_file_references.setter
	def list_external_file_references(self, value):
		"""Gets the names and statuses of the external file references on the component."""
		self._instance.ListExternalFileReferences2 = value

	@property
	def list_external_file_references_count(self):
		"""Gets the number of external references on the component."""
		return self._instance.ListExternalFileReferencesCount

	@list_external_file_references_count.setter
	def list_external_file_references_count(self, value):
		"""Gets the number of external references on the component."""
		self._instance.ListExternalFileReferencesCount = value

	@property
	def make_virtual(self):
		"""Makes this component and optionally its child components virtual by saving them in the current assembly."""
		return self._instance.MakeVirtual2

	@make_virtual.setter
	def make_virtual(self, value):
		"""Makes this component and optionally its child components virtual by saving them in the current assembly."""
		self._instance.MakeVirtual2 = value

	@property
	def remove_material_property(self):
		"""Removes the appearance from the component."""
		return self._instance.RemoveMaterialProperty2

	@remove_material_property.setter
	def remove_material_property(self, value):
		"""Removes the appearance from the component."""
		self._instance.RemoveMaterialProperty2 = value

	@property
	def remove_presentation_transform(self):
		"""Removes the presentation transform from this component."""
		return self._instance.RemovePresentationTransform

	@remove_presentation_transform.setter
	def remove_presentation_transform(self, value):
		"""Removes the presentation transform from this component."""
		self._instance.RemovePresentationTransform = value

	@property
	def remove_texture(self):
		"""Removes the texture from this component in the specified configuration."""
		return self._instance.RemoveTexture

	@remove_texture.setter
	def remove_texture(self, value):
		"""Removes the texture from this component in the specified configuration."""
		self._instance.RemoveTexture = value

	@property
	def remove_texture_by_display_state(self):
		"""Removes the texture applied to this component in the specified display state."""
		return self._instance.RemoveTextureByDisplayState

	@remove_texture_by_display_state.setter
	def remove_texture_by_display_state(self, value):
		"""Removes the texture applied to this component in the specified display state."""
		self._instance.RemoveTextureByDisplayState = value

	@property
	def reset_property_extension(self):
		"""Clears all of the values stored in the property extension."""
		return self._instance.ResetPropertyExtension

	@reset_property_extension.setter
	def reset_property_extension(self, value):
		"""Clears all of the values stored in the property extension."""
		self._instance.ResetPropertyExtension = value

	@property
	def save_virtual_component(self):
		"""Saves a virtual component to an external file."""
		return self._instance.SaveVirtualComponent

	@save_virtual_component.setter
	def save_virtual_component(self, value):
		"""Saves a virtual component to an external file."""
		self._instance.SaveVirtualComponent = value

	@property
	def select(self):
		"""Selects this component."""
		return self._instance.Select4

	@select.setter
	def select(self, value):
		"""Selects this component."""
		self._instance.Select4 = value

	@property
	def set_cosmos_works_material(self):
		"""Assigns the material to use during analysis to this component."""
		return self._instance.SetCosmosWorksMaterial

	@set_cosmos_works_material.setter
	def set_cosmos_works_material(self, value):
		"""Assigns the material to use during analysis to this component."""
		self._instance.SetCosmosWorksMaterial = value

	@property
	def set_exclude_from_b_o_m(self):
		"""Sets whether to exclude this component from the bills of materials (BOMs) in the specified configurations."""
		return self._instance.SetExcludeFromBOM2

	@set_exclude_from_b_o_m.setter
	def set_exclude_from_b_o_m(self, value):
		"""Sets whether to exclude this component from the bills of materials (BOMs) in the specified configurations."""
		self._instance.SetExcludeFromBOM2 = value

	@property
	def set_material_id_name(self):
		"""Sets the material name for this component."""
		return self._instance.SetMaterialIdName

	@set_material_id_name.setter
	def set_material_id_name(self, value):
		"""Sets the material name for this component."""
		self._instance.SetMaterialIdName = value

	@property
	def set_material_property_values(self):
		"""Sets the material properties for this component."""
		return self._instance.SetMaterialPropertyValues2

	@set_material_property_values.setter
	def set_material_property_values(self, value):
		"""Sets the material properties for this component."""
		self._instance.SetMaterialPropertyValues2 = value

	@property
	def set_material_user_name(self):
		"""Sets the material user name for this component."""
		return self._instance.SetMaterialUserName

	@set_material_user_name.setter
	def set_material_user_name(self, value):
		"""Sets the material user name for this component."""
		self._instance.SetMaterialUserName = value

	@property
	def set_referenced_display_states(self):
		"""Sets the specified display state of this component to be referenced by the specified assembly display state(s)."""
		return self._instance.SetReferencedDisplayStates

	@set_referenced_display_states.setter
	def set_referenced_display_states(self, value):
		"""Sets the specified display state of this component to be referenced by the specified assembly display state(s)."""
		self._instance.SetReferencedDisplayStates = value

	@property
	def set_smart_component_data(self):
		"""Sets the features, components, and feature references of a Smart Component."""
		return self._instance.SetSmartComponentData

	@set_smart_component_data.setter
	def set_smart_component_data(self, value):
		"""Sets the features, components, and feature references of a Smart Component."""
		self._instance.SetSmartComponentData = value

	@property
	def set_suppression(self):
		"""Sets the suppression state of this component."""
		return self._instance.SetSuppression2

	@set_suppression.setter
	def set_suppression(self, value):
		"""Sets the suppression state of this component."""
		self._instance.SetSuppression2 = value

	@property
	def set_texture(self):
		"""Applies texture to this component in the specified configuration."""
		return self._instance.SetTexture

	@set_texture.setter
	def set_texture(self, value):
		"""Applies texture to this component in the specified configuration."""
		self._instance.SetTexture = value

	@property
	def set_texture_by_display_state(self):
		"""Sets the texture applied to this component in the specified display state."""
		return self._instance.SetTextureByDisplayState

	@set_texture_by_display_state.setter
	def set_texture_by_display_state(self, value):
		"""Sets the texture applied to this component in the specified display state."""
		self._instance.SetTextureByDisplayState = value

	@property
	def set_transform_and_solve(self):
		"""Sets the transform and solves for the mates for this component."""
		return self._instance.SetTransformAndSolve3

	@set_transform_and_solve.setter
	def set_transform_and_solve(self, value):
		"""Sets the transform and solves for the mates for this component."""
		self._instance.SetTransformAndSolve3 = value

	@property
	def set_visibility(self):
		"""Sets the visibility state for this component."""
		return self._instance.SetVisibility

	@set_visibility.setter
	def set_visibility(self, value):
		"""Sets the visibility state for this component."""
		self._instance.SetVisibility = value

	@property
	def set_visibility_in_asm_display_states(self):
		"""Sets the visibility of this component in the specified assembly display state(s)."""
		return self._instance.SetVisibilityInAsmDisplayStates

	@set_visibility_in_asm_display_states.setter
	def set_visibility_in_asm_display_states(self, value):
		"""Sets the visibility of this component in the specified assembly display state(s)."""
		self._instance.SetVisibilityInAsmDisplayStates = value

	@property
	def update_external_file_references(self):
		"""Updates the external file references of this model."""
		return self._instance.UpdateExternalFileReferences

	@update_external_file_references.setter
	def update_external_file_references(self, value):
		"""Updates the external file references of this model."""
		self._instance.UpdateExternalFileReferences = value

