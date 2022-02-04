# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html
class IExtrudeFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def assembly_feature_scope(self):
		"""Gets or sets whether to use scope for this assembly extrude feature."""
		return self._instance.AssemblyFeatureScope

	@assembly_feature_scope.setter
	def assembly_feature_scope(self, value):
		"""Gets or sets whether to use scope for this assembly extrude feature."""
		self._instance.AssemblyFeatureScope = value

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all or only specific bodies for the extrude feature to affect in the multibody part."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all or only specific bodies for the extrude feature to affect in the multibody part."""
		self._instance.AutoSelect = value

	@property
	def auto_select_components(self):
		"""Gets or sets whether to auto-select all components that this assembly extrude feature affects in model."""
		return self._instance.AutoSelectComponents

	@auto_select_components.setter
	def auto_select_components(self, value):
		"""Gets or sets whether to auto-select all components that this assembly extrude feature affects in model."""
		self._instance.AutoSelectComponents = value

	@property
	def both_directions(self):
		"""Gets or sets whether the extrusion is in both directions."""
		return self._instance.BothDirections

	@both_directions.setter
	def both_directions(self, value):
		"""Gets or sets whether the extrusion is in both directions."""
		self._instance.BothDirections = value

	@property
	def cap_ends(self):
		"""Caps the ends for a thin base extrude feature."""
		return self._instance.CapEnds

	@cap_ends.setter
	def cap_ends(self, value):
		"""Caps the ends for a thin base extrude feature."""
		self._instance.CapEnds = value

	@property
	def cap_thickness(self):
		"""Gets or sets the end cap thickness for a thin base extrude feature."""
		return self._instance.CapThickness

	@cap_thickness.setter
	def cap_thickness(self, value):
		"""Gets or sets the end cap thickness for a thin base extrude feature."""
		self._instance.CapThickness = value

	@property
	def contours(self):
		"""Gets and sets the selected contours in this extrude feature."""
		return self._instance.Contours

	@contours.setter
	def contours(self, value):
		"""Gets and sets the selected contours in this extrude feature."""
		self._instance.Contours = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for the extrude feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for the extrude feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies that the extrude feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies that the extrude feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def flip_side_to_cut(self):
		"""Gets or sets whether to flip the side to cut."""
		return self._instance.FlipSideToCut

	@flip_side_to_cut.setter
	def flip_side_to_cut(self, value):
		"""Gets or sets whether to flip the side to cut."""
		self._instance.FlipSideToCut = value

	@property
	def from_offset_distance(self):
		"""Gets or sets the offset distance if IExtrudeFeatureData2::FromType is swExtrudeFrom_Offset."""
		return self._instance.FromOffsetDistance

	@from_offset_distance.setter
	def from_offset_distance(self, value):
		"""Gets or sets the offset distance if IExtrudeFeatureData2::FromType is swExtrudeFrom_Offset."""
		self._instance.FromOffsetDistance = value

	@property
	def from_offset_reverse(self):
		"""Gets or sets whether the offset is reverse for this extrusion if IExtrudeFeatureData2::FromTypeis swExtrudeFrom_Offset."""
		return self._instance.FromOffsetReverse

	@from_offset_reverse.setter
	def from_offset_reverse(self, value):
		"""Gets or sets whether the offset is reverse for this extrusion if IExtrudeFeatureData2::FromTypeis swExtrudeFrom_Offset."""
		self._instance.FromOffsetReverse = value

	@property
	def from_type(self):
		"""Gets or sets the type from which to create an extrusion."""
		return self._instance.FromType

	@from_type.setter
	def from_type(self, value):
		"""Gets or sets the type from which to create an extrusion."""
		self._instance.FromType = value

	@property
	def link_to_thickness(self):
		"""Gets or sets whether to link the depth of an extruded boss to the thickness of the base feature."""
		return self._instance.LinkToThickness

	@link_to_thickness.setter
	def link_to_thickness(self, value):
		"""Gets or sets whether to link the depth of an extruded boss to the thickness of the base feature."""
		self._instance.LinkToThickness = value

	@property
	def merge(self):
		"""Gets or sets whether to merge the results of the extrude feature in a multibody part."""
		return self._instance.Merge

	@merge.setter
	def merge(self, value):
		"""Gets or sets whether to merge the results of the extrude feature in a multibody part."""
		self._instance.Merge = value

	@property
	def normal_cut(self):
		"""Gets or sets whether the cut is created normal to the thickness of the sheet metal part."""
		return self._instance.NormalCut

	@normal_cut.setter
	def normal_cut(self, value):
		"""Gets or sets whether the cut is created normal to the thickness of the sheet metal part."""
		self._instance.NormalCut = value

	@property
	def optimize_geometry(self):
		"""Gets or sets whether to optimize the geometry of a normal cut in a sheet metal part."""
		return self._instance.OptimizeGeometry

	@optimize_geometry.setter
	def optimize_geometry(self, value):
		"""Gets or sets whether to optimize the geometry of a normal cut in a sheet metal part."""
		self._instance.OptimizeGeometry = value

	@property
	def propagate_feature_to_parts(self):
		"""Gets whether to propagate this assembly extrude feature to the parts that it affects in this model."""
		return self._instance.PropagateFeatureToParts

	@propagate_feature_to_parts.setter
	def propagate_feature_to_parts(self, value):
		"""Gets whether to propagate this assembly extrude feature to the parts that it affects in this model."""
		self._instance.PropagateFeatureToParts = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of the extrusion feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of the extrusion feature."""
		self._instance.ReverseDirection = value

	@property
	def thin_wall_type(self):
		"""Gets or sets the thin wall type for a thin base extrude feature."""
		return self._instance.ThinWallType

	@thin_wall_type.setter
	def thin_wall_type(self, value):
		"""Gets or sets the thin wall type for a thin base extrude feature."""
		self._instance.ThinWallType = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define the extrusion feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define the extrusion feature."""
		self._instance.AccessSelections = value

	@property
	def get_auto_fillet_corners(self):
		"""Gets whether the corners of this thin feature are automatically filleted."""
		return self._instance.GetAutoFilletCorners

	@get_auto_fillet_corners.setter
	def get_auto_fillet_corners(self, value):
		"""Gets whether the corners of this thin feature are automatically filleted."""
		self._instance.GetAutoFilletCorners = value

	@property
	def get_auto_fillet_radius(self):
		"""Gets the automatic corner fillet radius for this thin feature."""
		return self._instance.GetAutoFilletRadius

	@get_auto_fillet_radius.setter
	def get_auto_fillet_radius(self, value):
		"""Gets the automatic corner fillet radius for this thin feature."""
		self._instance.GetAutoFilletRadius = value

	@property
	def get_contours_count(self):
		"""Gets the number of selected contours for this extrude feature."""
		return self._instance.GetContoursCount

	@get_contours_count.setter
	def get_contours_count(self, value):
		"""Gets the number of selected contours for this extrude feature."""
		self._instance.GetContoursCount = value

	@property
	def get_depth(self):
		"""Gets the depth of the extrusion feature in the forward or reverse direction."""
		return self._instance.GetDepth

	@get_depth.setter
	def get_depth(self, value):
		"""Gets the depth of the extrusion feature in the forward or reverse direction."""
		self._instance.GetDepth = value

	@property
	def get_direction_reference(self):
		"""Gets the direction of the extrusion."""
		return self._instance.GetDirectionReference

	@get_direction_reference.setter
	def get_direction_reference(self, value):
		"""Gets the direction of the extrusion."""
		self._instance.GetDirectionReference = value

	@property
	def get_draft_angle(self):
		"""Gets the draft angle of the extrusion in the forward or reverse direction."""
		return self._instance.GetDraftAngle

	@get_draft_angle.setter
	def get_draft_angle(self, value):
		"""Gets the draft angle of the extrusion in the forward or reverse direction."""
		self._instance.GetDraftAngle = value

	@property
	def get_draft_outward(self):
		"""Gets whether the extrusion feature is drafted outward in the forward or reverse direction."""
		return self._instance.GetDraftOutward

	@get_draft_outward.setter
	def get_draft_outward(self, value):
		"""Gets whether the extrusion feature is drafted outward in the forward or reverse direction."""
		self._instance.GetDraftOutward = value

	@property
	def get_draft_while_extruding(self):
		"""Gets whether the feature is drafted while extruding in the forward or reverse direction."""
		return self._instance.GetDraftWhileExtruding

	@get_draft_while_extruding.setter
	def get_draft_while_extruding(self, value):
		"""Gets whether the feature is drafted while extruding in the forward or reverse direction."""
		self._instance.GetDraftWhileExtruding = value

	@property
	def get_end_condition(self):
		"""Gets the type of end condition of this extrusion feature for forward or reverse direction."""
		return self._instance.GetEndCondition

	@get_end_condition.setter
	def get_end_condition(self, value):
		"""Gets the type of end condition of this extrusion feature for forward or reverse direction."""
		self._instance.GetEndCondition = value

	@property
	def get_end_condition_reference(self):
		"""Gets the reference entity defining the end condition in the forward or reverse direction."""
		return self._instance.GetEndConditionReference

	@get_end_condition_reference.setter
	def get_end_condition_reference(self, value):
		"""Gets the reference entity defining the end condition in the forward or reverse direction."""
		self._instance.GetEndConditionReference = value

	@property
	def get_feature_scope_bodies_count(self):
		"""Gets the number of solid bodies affected by the extrude feature in a multibody part."""
		return self._instance.GetFeatureScopeBodiesCount

	@get_feature_scope_bodies_count.setter
	def get_feature_scope_bodies_count(self, value):
		"""Gets the number of solid bodies affected by the extrude feature in a multibody part."""
		self._instance.GetFeatureScopeBodiesCount = value

	@property
	def get_from_entity(self):
		"""Gets the entity and its type from which the extrusion was created."""
		return self._instance.GetFromEntity

	@get_from_entity.setter
	def get_from_entity(self, value):
		"""Gets the entity and its type from which the extrusion was created."""
		self._instance.GetFromEntity = value

	@property
	def get_reverse_offset(self):
		"""Gets the offset direction for this extrude feature."""
		return self._instance.GetReverseOffset

	@get_reverse_offset.setter
	def get_reverse_offset(self, value):
		"""Gets the offset direction for this extrude feature."""
		self._instance.GetReverseOffset = value

	@property
	def get_translate_surface(self):
		"""Gets the translate surface setting for this extrude feature."""
		return self._instance.GetTranslateSurface

	@get_translate_surface.setter
	def get_translate_surface(self, value):
		"""Gets the translate surface setting for this extrude feature."""
		self._instance.GetTranslateSurface = value

	@property
	def get_wall_thickness(self):
		"""Gets the wall thickness of the thin extrusion feature in forward or reverse direction."""
		return self._instance.GetWallThickness

	@get_wall_thickness.setter
	def get_wall_thickness(self, value):
		"""Gets the wall thickness of the thin extrusion feature in forward or reverse direction."""
		self._instance.GetWallThickness = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections used to define the extrusion feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections used to define the extrusion feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_contours(self):
		"""Gets the selected contours for this extrude feature."""
		return self._instance.IGetContours

	@i_get_contours.setter
	def i_get_contours(self, value):
		"""Gets the selected contours for this extrude feature."""
		self._instance.IGetContours = value

	@property
	def i_get_feature_scope_bodies(self):
		"""Gets the solid bodies that the extrude feature affects in a multibody part."""
		return self._instance.IGetFeatureScopeBodies

	@i_get_feature_scope_bodies.setter
	def i_get_feature_scope_bodies(self, value):
		"""Gets the solid bodies that the extrude feature affects in a multibody part."""
		self._instance.IGetFeatureScopeBodies = value

	@property
	def is_boss_feature(self):
		"""Gets whether the extrusion is a boss feature."""
		return self._instance.IsBossFeature

	@is_boss_feature.setter
	def is_boss_feature(self, value):
		"""Gets whether the extrusion is a boss feature."""
		self._instance.IsBossFeature = value

	@property
	def i_set_change_to_configurations(self):
		"""Applies changes made to this extrude feature to the specified configurations."""
		return self._instance.ISetChangeToConfigurations

	@i_set_change_to_configurations.setter
	def i_set_change_to_configurations(self, value):
		"""Applies changes made to this extrude feature to the specified configurations."""
		self._instance.ISetChangeToConfigurations = value

	@property
	def i_set_contours(self):
		"""Sets the selected contours for this extrude feature."""
		return self._instance.ISetContours

	@i_set_contours.setter
	def i_set_contours(self, value):
		"""Sets the selected contours for this extrude feature."""
		self._instance.ISetContours = value

	@property
	def i_set_feature_scope_bodies(self):
		"""Sets the solid bodies that the extrude feature affects in the multibody part."""
		return self._instance.ISetFeatureScopeBodies

	@i_set_feature_scope_bodies.setter
	def i_set_feature_scope_bodies(self, value):
		"""Sets the solid bodies that the extrude feature affects in the multibody part."""
		self._instance.ISetFeatureScopeBodies = value

	@property
	def is_thin_feature(self):
		"""Gets whether the extrusion is a thin feature."""
		return self._instance.IsThinFeature

	@is_thin_feature.setter
	def is_thin_feature(self, value):
		"""Gets whether the extrusion is a thin feature."""
		self._instance.IsThinFeature = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the extrude feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the extrude feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_auto_fillet(self):
		"""Sets the automatic corner fillet properties of this thin feature."""
		return self._instance.SetAutoFillet

	@set_auto_fillet.setter
	def set_auto_fillet(self, value):
		"""Sets the automatic corner fillet properties of this thin feature."""
		self._instance.SetAutoFillet = value

	@property
	def set_change_to_configurations(self):
		"""Applies changes made to this extrude feature to the specified configurations."""
		return self._instance.SetChangeToConfigurations

	@set_change_to_configurations.setter
	def set_change_to_configurations(self, value):
		"""Applies changes made to this extrude feature to the specified configurations."""
		self._instance.SetChangeToConfigurations = value

	@property
	def set_depth(self):
		"""Sets the depth of the feature in the forward or reverse direction."""
		return self._instance.SetDepth

	@set_depth.setter
	def set_depth(self, value):
		"""Sets the depth of the feature in the forward or reverse direction."""
		self._instance.SetDepth = value

	@property
	def set_direction_reference(self):
		"""Sets the direction of the extrusion."""
		return self._instance.SetDirectionReference

	@set_direction_reference.setter
	def set_direction_reference(self, value):
		"""Sets the direction of the extrusion."""
		self._instance.SetDirectionReference = value

	@property
	def set_draft_angle(self):
		"""Sets the draft angle of the extrusion in the forward or reverse direction."""
		return self._instance.SetDraftAngle

	@set_draft_angle.setter
	def set_draft_angle(self, value):
		"""Sets the draft angle of the extrusion in the forward or reverse direction."""
		self._instance.SetDraftAngle = value

	@property
	def set_draft_outward(self):
		"""Sets whether the extrusion feature should draft outward in the forward or reverse direction."""
		return self._instance.SetDraftOutward

	@set_draft_outward.setter
	def set_draft_outward(self, value):
		"""Sets whether the extrusion feature should draft outward in the forward or reverse direction."""
		self._instance.SetDraftOutward = value

	@property
	def set_draft_while_extruding(self):
		"""Sets whether the feature is drafted while extruding in the forward or reverse direction."""
		return self._instance.SetDraftWhileExtruding

	@set_draft_while_extruding.setter
	def set_draft_while_extruding(self, value):
		"""Sets whether the feature is drafted while extruding in the forward or reverse direction."""
		self._instance.SetDraftWhileExtruding = value

	@property
	def set_end_condition(self):
		"""Sets the end condition type of the extrusion feature for the forward or reverse direction."""
		return self._instance.SetEndCondition

	@set_end_condition.setter
	def set_end_condition(self, value):
		"""Sets the end condition type of the extrusion feature for the forward or reverse direction."""
		self._instance.SetEndCondition = value

	@property
	def set_end_condition_reference(self):
		"""Sets the reference entity that defines the end condition in a forward or reverse direction."""
		return self._instance.SetEndConditionReference

	@set_end_condition_reference.setter
	def set_end_condition_reference(self, value):
		"""Sets the reference entity that defines the end condition in a forward or reverse direction."""
		self._instance.SetEndConditionReference = value

	@property
	def set_from_entity(self):
		"""Sets the entity from which to create an extrusion."""
		return self._instance.SetFromEntity

	@set_from_entity.setter
	def set_from_entity(self, value):
		"""Sets the entity from which to create an extrusion."""
		self._instance.SetFromEntity = value

	@property
	def set_reverse_offset(self):
		"""Sets the offset direction for this extrude feature."""
		return self._instance.SetReverseOffset

	@set_reverse_offset.setter
	def set_reverse_offset(self, value):
		"""Sets the offset direction for this extrude feature."""
		self._instance.SetReverseOffset = value

	@property
	def set_translate_surface(self):
		"""Sets the translate surface setting for this extrude feature."""
		return self._instance.SetTranslateSurface

	@set_translate_surface.setter
	def set_translate_surface(self, value):
		"""Sets the translate surface setting for this extrude feature."""
		self._instance.SetTranslateSurface = value

	@property
	def set_wall_thickness(self):
		"""Sets the wall thickness of the thin extrusion feature in a forward or reverse direction."""
		return self._instance.SetWallThickness

	@set_wall_thickness.setter
	def set_wall_thickness(self, value):
		"""Sets the wall thickness of the thin extrusion feature in a forward or reverse direction."""
		self._instance.SetWallThickness = value

