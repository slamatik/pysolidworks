# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html
class ILoftFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def advanced_smoothing(self):
		"""Gets or sets whether to enable advanced smoothing for this loft feature."""
		return self._instance.AdvancedSmoothing

	@advanced_smoothing.setter
	def advanced_smoothing(self, value):
		"""Gets or sets whether to enable advanced smoothing for this loft feature."""
		self._instance.AdvancedSmoothing = value

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all or only specific bodies for the loft feature to affect in a multibody part."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all or only specific bodies for the loft feature to affect in a multibody part."""
		self._instance.AutoSelect = value

	@property
	def centerline(self):
		"""Gets and sets the centerline for this loft feature."""
		return self._instance.Centerline

	@centerline.setter
	def centerline(self, value):
		"""Gets and sets the centerline for this loft feature."""
		self._instance.Centerline = value

	@property
	def close(self):
		"""Gets or sets whether to close this loft feature."""
		return self._instance.Close

	@close.setter
	def close(self, value):
		"""Gets or sets whether to close this loft feature."""
		self._instance.Close = value

	@property
	def end_constraint_apply_to_all(self):
		"""Gets whether an end constraint was applied to this loft feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.EndConstraintApplyToAll

	@end_constraint_apply_to_all.setter
	def end_constraint_apply_to_all(self, value):
		"""Gets whether an end constraint was applied to this loft feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.EndConstraintApplyToAll = value

	@property
	def end_constraint_draft_angle(self):
		"""Gets or sets the draft angle for the end constraint for the loft feature."""
		return self._instance.EndConstraintDraftAngle

	@end_constraint_draft_angle.setter
	def end_constraint_draft_angle(self, value):
		"""Gets or sets the draft angle for the end constraint for the loft feature."""
		self._instance.EndConstraintDraftAngle = value

	@property
	def end_constraint_draft_angle_direction(self):
		"""Gets or sets the direction of the angle of the draft for the end constraint for the loft feature."""
		return self._instance.EndConstraintDraftAngleDirection

	@end_constraint_draft_angle_direction.setter
	def end_constraint_draft_angle_direction(self, value):
		"""Gets or sets the direction of the angle of the draft for the end constraint for the loft feature."""
		self._instance.EndConstraintDraftAngleDirection = value

	@property
	def end_direction_vector(self):
		"""Gets or sets the direction vector in which to end this loft feature."""
		return self._instance.EndDirectionVector

	@end_direction_vector.setter
	def end_direction_vector(self, value):
		"""Gets or sets the direction vector in which to end this loft feature."""
		self._instance.EndDirectionVector = value

	@property
	def end_tangency_type(self):
		"""Gets or sets the end tangency type for this loft feature."""
		return self._instance.EndTangencyType

	@end_tangency_type.setter
	def end_tangency_type(self, value):
		"""Gets or sets the end tangency type for this loft feature."""
		self._instance.EndTangencyType = value

	@property
	def end_tangent_length(self):
		"""Gets or sets the end tangent length for this loft feature."""
		return self._instance.EndTangentLength

	@end_tangent_length.setter
	def end_tangent_length(self, value):
		"""Gets or sets the end tangent length for this loft feature."""
		self._instance.EndTangentLength = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for the loft feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for the loft feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies that the loft feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies that the loft feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def guide_curve_influence(self):
		"""Gets or sets the type of guide curve influence for this loft feature."""
		return self._instance.GuideCurveInfluence

	@guide_curve_influence.setter
	def guide_curve_influence(self, value):
		"""Gets or sets the type of guide curve influence for this loft feature."""
		self._instance.GuideCurveInfluence = value

	@property
	def guide_curves(self):
		"""Gets and sets the guide curves for this loft feature."""
		return self._instance.GuideCurves

	@guide_curves.setter
	def guide_curves(self, value):
		"""Gets and sets the guide curves for this loft feature."""
		self._instance.GuideCurves = value

	@property
	def maintain_tangency(self):
		"""Gets or sets whether to maintain tangency for this loft feature."""
		return self._instance.MaintainTangency

	@maintain_tangency.setter
	def maintain_tangency(self, value):
		"""Gets or sets whether to maintain tangency for this loft feature."""
		self._instance.MaintainTangency = value

	@property
	def merge(self):
		"""Gets or sets whether to merge the results of this loft feature in a multibody part."""
		return self._instance.Merge

	@merge.setter
	def merge(self, value):
		"""Gets or sets whether to merge the results of this loft feature in a multibody part."""
		self._instance.Merge = value

	@property
	def number_of_sections(self):
		"""Gets and sets the number of sections in this loft feature."""
		return self._instance.NumberOfSections

	@number_of_sections.setter
	def number_of_sections(self, value):
		"""Gets and sets the number of sections in this loft feature."""
		self._instance.NumberOfSections = value

	@property
	def pick_points(self):
		"""Gets or sets the pick points of a loft feature."""
		return self._instance.PickPoints

	@pick_points.setter
	def pick_points(self, value):
		"""Gets or sets the pick points of a loft feature."""
		self._instance.PickPoints = value

	@property
	def profiles(self):
		"""Gets and sets the profiles for this loft feature."""
		return self._instance.Profiles

	@profiles.setter
	def profiles(self, value):
		"""Gets and sets the profiles for this loft feature."""
		self._instance.Profiles = value

	@property
	def reverse_end_tangent_direction(self):
		"""Reverses the tangent direction for the end point of this loft feature."""
		return self._instance.ReverseEndTangentDirection

	@reverse_end_tangent_direction.setter
	def reverse_end_tangent_direction(self, value):
		"""Reverses the tangent direction for the end point of this loft feature."""
		self._instance.ReverseEndTangentDirection = value

	@property
	def reverse_start_tangent_direction(self):
		"""Reverses the tangent direction for the start point of this loft feature."""
		return self._instance.ReverseStartTangentDirection

	@reverse_start_tangent_direction.setter
	def reverse_start_tangent_direction(self, value):
		"""Reverses the tangent direction for the start point of this loft feature."""
		self._instance.ReverseStartTangentDirection = value

	@property
	def start_constraint_apply_to_all(self):
		"""Gets whether a start constraint was applied to this loft feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.StartConstraintApplyToAll

	@start_constraint_apply_to_all.setter
	def start_constraint_apply_to_all(self, value):
		"""Gets whether a start constraint was applied to this loft feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.StartConstraintApplyToAll = value

	@property
	def start_constraint_draft_angle(self):
		"""Gets or sets the angle of the draft for the start constraint of the loft feature."""
		return self._instance.StartConstraintDraftAngle

	@start_constraint_draft_angle.setter
	def start_constraint_draft_angle(self, value):
		"""Gets or sets the angle of the draft for the start constraint of the loft feature."""
		self._instance.StartConstraintDraftAngle = value

	@property
	def start_constraint_draft_angle_direction(self):
		"""Gets or sets the direction of the angle of the draft for the start constraint for the loft feature."""
		return self._instance.StartConstraintDraftAngleDirection

	@start_constraint_draft_angle_direction.setter
	def start_constraint_draft_angle_direction(self, value):
		"""Gets or sets the direction of the angle of the draft for the start constraint for the loft feature."""
		self._instance.StartConstraintDraftAngleDirection = value

	@property
	def start_direction_vector(self):
		"""Gets or sets the direction vector in which to start this loft feature."""
		return self._instance.StartDirectionVector

	@start_direction_vector.setter
	def start_direction_vector(self, value):
		"""Gets or sets the direction vector in which to start this loft feature."""
		self._instance.StartDirectionVector = value

	@property
	def start_tangency_type(self):
		"""Gets or sets the start tangency type for this loft feature."""
		return self._instance.StartTangencyType

	@start_tangency_type.setter
	def start_tangency_type(self, value):
		"""Gets or sets the start tangency type for this loft feature."""
		self._instance.StartTangencyType = value

	@property
	def start_tangent_length(self):
		"""Gets or sets the start tangent length for this loft feature."""
		return self._instance.StartTangentLength

	@start_tangent_length.setter
	def start_tangent_length(self, value):
		"""Gets or sets the start tangent length for this loft feature."""
		self._instance.StartTangentLength = value

	@property
	def thin_wall_type(self):
		"""Gets or sets the thin wall type for this loft feature."""
		return self._instance.ThinWallType

	@thin_wall_type.setter
	def thin_wall_type(self, value):
		"""Gets or sets the thin wall type for this loft feature."""
		self._instance.ThinWallType = value

	@property
	def access_selections(self):
		"""Accesses the selections used to define the loft feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections used to define the loft feature."""
		self._instance.AccessSelections = value

	@property
	def get_feature_scope_bodies_count(self):
		"""Gets the number of solid bodies affected by the loft feature in a multibody part."""
		return self._instance.GetFeatureScopeBodiesCount

	@get_feature_scope_bodies_count.setter
	def get_feature_scope_bodies_count(self, value):
		"""Gets the number of solid bodies affected by the loft feature in a multibody part."""
		self._instance.GetFeatureScopeBodiesCount = value

	@property
	def get_guide_curves_count(self):
		"""Gets the number of guide curves for this loft feature."""
		return self._instance.GetGuideCurvesCount

	@get_guide_curves_count.setter
	def get_guide_curves_count(self, value):
		"""Gets the number of guide curves for this loft feature."""
		self._instance.GetGuideCurvesCount = value

	@property
	def get_guide_curves_type(self):
		"""Gets the guide curve types for this loft feature."""
		return self._instance.GetGuideCurvesType

	@get_guide_curves_type.setter
	def get_guide_curves_type(self, value):
		"""Gets the guide curve types for this loft feature."""
		self._instance.GetGuideCurvesType = value

	@property
	def get_guide_tangency_type(self):
		"""Gets the tangency type of the guide curve (i.e., controls the tangency where the loft meets the guide curves) for this loft feature."""
		return self._instance.GetGuideTangencyType

	@get_guide_tangency_type.setter
	def get_guide_tangency_type(self, value):
		"""Gets the tangency type of the guide curve (i.e., controls the tangency where the loft meets the guide curves) for this loft feature."""
		self._instance.GetGuideTangencyType = value

	@property
	def get_profile_count(self):
		"""Gets the number of profiles associated with this loft feature."""
		return self._instance.GetProfileCount

	@get_profile_count.setter
	def get_profile_count(self, value):
		"""Gets the number of profiles associated with this loft feature."""
		self._instance.GetProfileCount = value

	@property
	def get_wall_thickness(self):
		"""Gets the wall thickness in the specified direction for this loft feature."""
		return self._instance.GetWallThickness

	@get_wall_thickness.setter
	def get_wall_thickness(self, value):
		"""Gets the wall thickness in the specified direction for this loft feature."""
		self._instance.GetWallThickness = value

	@property
	def i_access_selections(self):
		"""Accesses the selections used to define the loft feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections used to define the loft feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_feature_scope_bodies(self):
		"""Gets the solid bodies that the loft feature affects in a multibody part."""
		return self._instance.IGetFeatureScopeBodies

	@i_get_feature_scope_bodies.setter
	def i_get_feature_scope_bodies(self, value):
		"""Gets the solid bodies that the loft feature affects in a multibody part."""
		self._instance.IGetFeatureScopeBodies = value

	@property
	def i_get_guide_curves(self):
		"""Gets the guide curves for this loft feature."""
		return self._instance.IGetGuideCurves

	@i_get_guide_curves.setter
	def i_get_guide_curves(self, value):
		"""Gets the guide curves for this loft feature."""
		self._instance.IGetGuideCurves = value

	@property
	def i_get_guide_curves_type(self):
		"""Gets the guide curve types for this loft feature."""
		return self._instance.IGetGuideCurvesType

	@i_get_guide_curves_type.setter
	def i_get_guide_curves_type(self, value):
		"""Gets the guide curve types for this loft feature."""
		self._instance.IGetGuideCurvesType = value

	@property
	def i_get_profiles(self):
		"""Gets the profiles associated with this loft feature."""
		return self._instance.IGetProfiles

	@i_get_profiles.setter
	def i_get_profiles(self, value):
		"""Gets the profiles associated with this loft feature."""
		self._instance.IGetProfiles = value

	@property
	def is_boss_feature(self):
		"""Gets whether the loft feature is a boss feature."""
		return self._instance.IsBossFeature

	@is_boss_feature.setter
	def is_boss_feature(self, value):
		"""Gets whether the loft feature is a boss feature."""
		self._instance.IsBossFeature = value

	@property
	def i_set_feature_scope_bodies(self):
		"""Sets the solid bodies that the loft feature affects in a multibody part."""
		return self._instance.ISetFeatureScopeBodies

	@i_set_feature_scope_bodies.setter
	def i_set_feature_scope_bodies(self, value):
		"""Sets the solid bodies that the loft feature affects in a multibody part."""
		self._instance.ISetFeatureScopeBodies = value

	@property
	def i_set_guide_curves(self):
		"""Sets the guide curves for this loft feature."""
		return self._instance.ISetGuideCurves

	@i_set_guide_curves.setter
	def i_set_guide_curves(self, value):
		"""Sets the guide curves for this loft feature."""
		self._instance.ISetGuideCurves = value

	@property
	def i_set_profiles(self):
		"""Sets the profiles for this loft feature."""
		return self._instance.ISetProfiles

	@i_set_profiles.setter
	def i_set_profiles(self, value):
		"""Sets the profiles for this loft feature."""
		self._instance.ISetProfiles = value

	@property
	def is_thin_feature(self):
		"""Gets whether this loft feature is a thin feature."""
		return self._instance.IsThinFeature

	@is_thin_feature.setter
	def is_thin_feature(self, value):
		"""Gets whether this loft feature is a thin feature."""
		self._instance.IsThinFeature = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this loft feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this loft feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_guide_tangency_type(self):
		"""Sets the tangency type of the guide curve (i.e., controls the tangency where the loft meets the guide curves) for this loft feature."""
		return self._instance.SetGuideTangencyType

	@set_guide_tangency_type.setter
	def set_guide_tangency_type(self, value):
		"""Sets the tangency type of the guide curve (i.e., controls the tangency where the loft meets the guide curves) for this loft feature."""
		self._instance.SetGuideTangencyType = value

	@property
	def set_wall_thickness(self):
		"""Sets the wall thickness for this loft feature in the forward or reverse direction."""
		return self._instance.SetWallThickness

	@set_wall_thickness.setter
	def set_wall_thickness(self, value):
		"""Sets the wall thickness for this loft feature in the forward or reverse direction."""
		self._instance.SetWallThickness = value

