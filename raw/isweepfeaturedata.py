# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.html
class ISweepFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def advanced_smoothing(self):
		"""Gets or sets whether to apply advanced smoothing to this sweep feature."""
		return self._instance.AdvancedSmoothing

	@advanced_smoothing.setter
	def advanced_smoothing(self, value):
		"""Gets or sets whether to apply advanced smoothing to this sweep feature."""
		self._instance.AdvancedSmoothing = value

	@property
	def align_with_end_faces(self):
		"""Gets or sets whether to align this sweep with the end faces."""
		return self._instance.AlignWithEndFaces

	@align_with_end_faces.setter
	def align_with_end_faces(self, value):
		"""Gets or sets whether to align this sweep with the end faces."""
		self._instance.AlignWithEndFaces = value

	@property
	def assembly_feature_scope(self):
		"""Gets and sets whether this swept-cut feature affects only selected components in the assembly."""
		return self._instance.AssemblyFeatureScope

	@assembly_feature_scope.setter
	def assembly_feature_scope(self, value):
		"""Gets and sets whether this swept-cut feature affects only selected components in the assembly."""
		self._instance.AssemblyFeatureScope = value

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all bodies in a multibody part to be affected by this sweep feature."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all bodies in a multibody part to be affected by this sweep feature."""
		self._instance.AutoSelect = value

	@property
	def auto_select_components(self):
		"""Gets and sets whether to automatically select all assembly components to be affected by this swept-cutfeature."""
		return self._instance.AutoSelectComponents

	@auto_select_components.setter
	def auto_select_components(self, value):
		"""Gets and sets whether to automatically select all assembly components to be affected by this swept-cutfeature."""
		self._instance.AutoSelectComponents = value

	@property
	def circular_profile(self):
		"""Gets or sets whether to use a circular profile for this sweep feature."""
		return self._instance.CircularProfile

	@circular_profile.setter
	def circular_profile(self, value):
		"""Gets or sets whether to use a circular profile for this sweep feature."""
		self._instance.CircularProfile = value

	@property
	def circular_profile_diameter(self):
		"""Gets or sets the diameter of the circular profile for this sweep feature."""
		return self._instance.CircularProfileDiameter

	@circular_profile_diameter.setter
	def circular_profile_diameter(self, value):
		"""Gets or sets the diameter of the circular profile for this sweep feature."""
		self._instance.CircularProfileDiameter = value

	@property
	def d_reverse_twist_dir(self):
		"""Gets or sets whether to reverse the twist of this sweep feature."""
		return self._instance.D1ReverseTwistDir

	@d_reverse_twist_dir.setter
	def d_reverse_twist_dir(self, value):
		"""Gets or sets whether to reverse the twist of this sweep feature."""
		self._instance.D1ReverseTwistDir = value

	@property
	def d_reverse_twist_dir(self):
		"""Gets or sets whether to reverse the twist in Direction 2 of this bidirectional sweep feature."""
		return self._instance.D2ReverseTwistDir

	@d_reverse_twist_dir.setter
	def d_reverse_twist_dir(self, value):
		"""Gets or sets whether to reverse the twist in Direction 2 of this bidirectional sweep feature."""
		self._instance.D2ReverseTwistDir = value

	@property
	def direction(self):
		"""Gets or sets the direction type of this sweep feature."""
		return self._instance.Direction

	@direction.setter
	def direction(self, value):
		"""Gets or sets the direction type of this sweep feature."""
		self._instance.Direction = value

	@property
	def end_tangency_type(self):
		"""Gets or sets tangency at the end of the sweep path of this sweep feature."""
		return self._instance.EndTangencyType

	@end_tangency_type.setter
	def end_tangency_type(self, value):
		"""Gets or sets tangency at the end of the sweep path of this sweep feature."""
		self._instance.EndTangencyType = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope in a multibody part for this sweep feature."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope in a multibody part for this sweep feature."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies in a multibody part affected by this sweep feature."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies in a multibody part affected by this sweep feature."""
		self._instance.FeatureScopeBodies = value

	@property
	def guide_curves(self):
		"""Gets or sets the guide curves for this sweep feature."""
		return self._instance.GuideCurves

	@guide_curves.setter
	def guide_curves(self, value):
		"""Gets or sets the guide curves for this sweep feature."""
		self._instance.GuideCurves = value

	@property
	def maintain_tangency(self):
		"""Gets or sets whether to merge tangent faces in this sweep feature."""
		return self._instance.MaintainTangency

	@maintain_tangency.setter
	def maintain_tangency(self, value):
		"""Gets or sets whether to merge tangent faces in this sweep feature."""
		self._instance.MaintainTangency = value

	@property
	def merge(self):
		"""Gets or sets whether to merge the results of this swept-boss feature for a multibody part."""
		return self._instance.Merge

	@merge.setter
	def merge(self, value):
		"""Gets or sets whether to merge the results of this swept-boss feature for a multibody part."""
		self._instance.Merge = value

	@property
	def merge_smooth_faces(self):
		"""Gets or sets whether to merge the smooth faces of this sweep feature that uses guide curves."""
		return self._instance.MergeSmoothFaces

	@merge_smooth_faces.setter
	def merge_smooth_faces(self, value):
		"""Gets or sets whether to merge the smooth faces of this sweep feature that uses guide curves."""
		self._instance.MergeSmoothFaces = value

	@property
	def path(self):
		"""Gets or sets the sweep path for this sweep feature."""
		return self._instance.Path

	@path.setter
	def path(self, value):
		"""Gets or sets the sweep path for this sweep feature."""
		self._instance.Path = value

	@property
	def path_alignment_type(self):
		"""Gets or sets the alignment of the sweep path in this sweep feature."""
		return self._instance.PathAlignmentType

	@path_alignment_type.setter
	def path_alignment_type(self, value):
		"""Gets or sets the alignment of the sweep path in this sweep feature."""
		self._instance.PathAlignmentType = value

	@property
	def profile(self):
		"""Gets and sets the sketch profile or tool body for this sweep feature."""
		return self._instance.Profile

	@profile.setter
	def profile(self, value):
		"""Gets and sets the sketch profile or tool body for this sweep feature."""
		self._instance.Profile = value

	@property
	def propagate_feature_to_parts(self):
		"""Gets and sets whether to extend the swept-cut feature to all affected parts in the assembly."""
		return self._instance.PropagateFeatureToParts

	@propagate_feature_to_parts.setter
	def propagate_feature_to_parts(self, value):
		"""Gets and sets whether to extend the swept-cut feature to all affected parts in the assembly."""
		self._instance.PropagateFeatureToParts = value

	@property
	def start_tangency_type(self):
		"""Gets and sets the tangency at the start of the sweep path for this sweep feature."""
		return self._instance.StartTangencyType

	@start_tangency_type.setter
	def start_tangency_type(self, value):
		"""Gets and sets the tangency at the start of the sweep path for this sweep feature."""
		self._instance.StartTangencyType = value

	@property
	def sweep_type(self):
		"""Gets the type of this sweep feature."""
		return self._instance.SweepType

	@sweep_type.setter
	def sweep_type(self, value):
		"""Gets the type of this sweep feature."""
		self._instance.SweepType = value

	@property
	def tangent_propagation(self):
		"""Gets or sets whether to propagate the sweep to the next tangent edge for this sweep feature."""
		return self._instance.TangentPropagation

	@tangent_propagation.setter
	def tangent_propagation(self, value):
		"""Gets or sets whether to propagate the sweep to the next tangent edge for this sweep feature."""
		self._instance.TangentPropagation = value

	@property
	def thin_feature(self):
		"""Gets or sets whether to make this sweep feature a thin-walled feature."""
		return self._instance.ThinFeature

	@thin_feature.setter
	def thin_feature(self, value):
		"""Gets or sets whether to make this sweep feature a thin-walled feature."""
		self._instance.ThinFeature = value

	@property
	def thin_wall_type(self):
		"""Gets or sets the type of this thin-walled sweep feature."""
		return self._instance.ThinWallType

	@thin_wall_type.setter
	def thin_wall_type(self, value):
		"""Gets or sets the type of this thin-walled sweep feature."""
		self._instance.ThinWallType = value

	@property
	def twist_control_type(self):
		"""Gets or sets the type of twist control for this sweep feature."""
		return self._instance.TwistControlType

	@twist_control_type.setter
	def twist_control_type(self, value):
		"""Gets or sets the type of twist control for this sweep feature."""
		self._instance.TwistControlType = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this sweep feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this sweep feature."""
		self._instance.AccessSelections = value

	@property
	def get_cut_sweep_option(self):
		"""Gets the type of this cut sweep feature."""
		return self._instance.GetCutSweepOption

	@get_cut_sweep_option.setter
	def get_cut_sweep_option(self, value):
		"""Gets the type of this cut sweep feature."""
		self._instance.GetCutSweepOption = value

	@property
	def get_d_twist_angle(self):
		"""Gets the twist angle in Direction 2 of this bidirectional sweep feature."""
		return self._instance.GetD2TwistAngle

	@get_d_twist_angle.setter
	def get_d_twist_angle(self, value):
		"""Gets the twist angle in Direction 2 of this bidirectional sweep feature."""
		self._instance.GetD2TwistAngle = value

	@property
	def get_feature_scope_bodies_count(self):
		"""Gets the number of solid bodies affected by the sweep feature in a multibody part."""
		return self._instance.GetFeatureScopeBodiesCount

	@get_feature_scope_bodies_count.setter
	def get_feature_scope_bodies_count(self, value):
		"""Gets the number of solid bodies affected by the sweep feature in a multibody part."""
		self._instance.GetFeatureScopeBodiesCount = value

	@property
	def get_guide_curves_count(self):
		"""Gets a number of guide curves for this sweep feature."""
		return self._instance.GetGuideCurvesCount

	@get_guide_curves_count.setter
	def get_guide_curves_count(self, value):
		"""Gets a number of guide curves for this sweep feature."""
		self._instance.GetGuideCurvesCount = value

	@property
	def get_guide_curves_type(self):
		"""Gets the type of guide curves in this sweep feature."""
		return self._instance.GetGuideCurvesType

	@get_guide_curves_type.setter
	def get_guide_curves_type(self, value):
		"""Gets the type of guide curves in this sweep feature."""
		self._instance.GetGuideCurvesType = value

	@property
	def get_path_alignment_direction_vector(self):
		"""Gets the direction vector of the specified type for this sweep feature."""
		return self._instance.GetPathAlignmentDirectionVector

	@get_path_alignment_direction_vector.setter
	def get_path_alignment_direction_vector(self, value):
		"""Gets the direction vector of the specified type for this sweep feature."""
		self._instance.GetPathAlignmentDirectionVector = value

	@property
	def get_path_type(self):
		"""Gets the path type for this sweep feature."""
		return self._instance.GetPathType

	@get_path_type.setter
	def get_path_type(self, value):
		"""Gets the path type for this sweep feature."""
		self._instance.GetPathType = value

	@property
	def get_profile_type(self):
		"""Gets the profile type of this sweep feature."""
		return self._instance.GetProfileType

	@get_profile_type.setter
	def get_profile_type(self, value):
		"""Gets the profile type of this sweep feature."""
		self._instance.GetProfileType = value

	@property
	def get_twist_angle(self):
		"""Gets the angle at which to twist this sweep feature."""
		return self._instance.GetTwistAngle

	@get_twist_angle.setter
	def get_twist_angle(self, value):
		"""Gets the angle at which to twist this sweep feature."""
		self._instance.GetTwistAngle = value

	@property
	def get_wall_thickness(self):
		"""Gets the wall thickness, forward (Direction 1) or reverse (Direction 2), of this thin-walled sweep feature."""
		return self._instance.GetWallThickness

	@get_wall_thickness.setter
	def get_wall_thickness(self, value):
		"""Gets the wall thickness, forward (Direction 1) or reverse (Direction 2), of this thin-walled sweep feature."""
		self._instance.GetWallThickness = value

	@property
	def is_boss_feature(self):
		"""Gets whether the sweep feature is a boss feature."""
		return self._instance.IsBossFeature

	@is_boss_feature.setter
	def is_boss_feature(self, value):
		"""Gets whether the sweep feature is a boss feature."""
		self._instance.IsBossFeature = value

	@property
	def is_thin_feature(self):
		"""Gets whether this is a thin-walled sweep feature."""
		return self._instance.IsThinFeature

	@is_thin_feature.setter
	def is_thin_feature(self, value):
		"""Gets whether this is a thin-walled sweep feature."""
		self._instance.IsThinFeature = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this sweep feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this sweep feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_d_twist_angle(self):
		"""Sets the twist angle in Direction 2 of this bidirectional sweep feature."""
		return self._instance.SetD2TwistAngle

	@set_d_twist_angle.setter
	def set_d_twist_angle(self, value):
		"""Sets the twist angle in Direction 2 of this bidirectional sweep feature."""
		self._instance.SetD2TwistAngle = value

	@property
	def set_path_alignment_direction_vector(self):
		"""Sets the direction vector for path alignment in this sweep feature."""
		return self._instance.SetPathAlignmentDirectionVector

	@set_path_alignment_direction_vector.setter
	def set_path_alignment_direction_vector(self, value):
		"""Sets the direction vector for path alignment in this sweep feature."""
		self._instance.SetPathAlignmentDirectionVector = value

	@property
	def set_twist_angle(self):
		"""Sets the angle at which to twist this sweep feature."""
		return self._instance.SetTwistAngle

	@set_twist_angle.setter
	def set_twist_angle(self, value):
		"""Sets the angle at which to twist this sweep feature."""
		self._instance.SetTwistAngle = value

	@property
	def set_wall_thickness(self):
		"""Sets the wall thickness, forward (Direction 1) or reverse (Direction 2), of this thin-walled sweep feature."""
		return self._instance.SetWallThickness

	@set_wall_thickness.setter
	def set_wall_thickness(self, value):
		"""Sets the wall thickness, forward (Direction 1) or reverse (Direction 2), of this thin-walled sweep feature."""
		self._instance.SetWallThickness = value

