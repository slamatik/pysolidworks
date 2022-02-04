# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundaryBossFeatureData_members.html
class IBoundaryBossFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all or only specific bodies for the boundary feature to affect in the multibody part."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all or only specific bodies for the boundary feature to affect in the multibody part."""
		self._instance.AutoSelect = value

	@property
	def d_curve_influence(self):
		"""Gets or sets the type of curve influence for Direction 1 for this boundary feature."""
		return self._instance.D1CurveInfluence

	@d_curve_influence.setter
	def d_curve_influence(self, value):
		"""Gets or sets the type of curve influence for Direction 1 for this boundary feature."""
		self._instance.D1CurveInfluence = value

	@property
	def d_curves(self):
		"""Gets or sets the curves for Direction 1 for this boundary feature."""
		return self._instance.D1Curves

	@d_curves.setter
	def d_curves(self, value):
		"""Gets or sets the curves for Direction 1 for this boundary feature."""
		self._instance.D1Curves = value

	@property
	def d_curve_influence(self):
		"""Gets or sets the type of curve influence for Direction 2 for this boundary feature."""
		return self._instance.D2CurveInfluence

	@d_curve_influence.setter
	def d_curve_influence(self, value):
		"""Gets or sets the type of curve influence for Direction 2 for this boundary feature."""
		self._instance.D2CurveInfluence = value

	@property
	def d_curves(self):
		"""Gets or sets the curves for Direction 2 for this boundary feature."""
		return self._instance.D2Curves

	@d_curves.setter
	def d_curves(self, value):
		"""Gets or sets the curves for Direction 2 for this boundary feature."""
		self._instance.D2Curves = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for the boundary feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for the boundary feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the bodies that this boundary feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the bodies that this boundary feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def feature_scope_bodies_count(self):
		"""Gets the number of bodies that this boundary feature affects in a multibody part."""
		return self._instance.FeatureScopeBodiesCount

	@feature_scope_bodies_count.setter
	def feature_scope_bodies_count(self, value):
		"""Gets the number of bodies that this boundary feature affects in a multibody part."""
		self._instance.FeatureScopeBodiesCount = value

	@property
	def merge_result(self):
		"""Gets or sets whether to merge all boundary feature elements."""
		return self._instance.MergeResult

	@merge_result.setter
	def merge_result(self, value):
		"""Gets or sets whether to merge all boundary feature elements."""
		self._instance.MergeResult = value

	@property
	def merge_tangent_faces(self):
		"""Gets or sets whether to make the surfaces in the resulting boundary feature tangent if the corresponding boundary segments are tangent."""
		return self._instance.MergeTangentFaces

	@merge_tangent_faces.setter
	def merge_tangent_faces(self, value):
		"""Gets or sets whether to make the surfaces in the resulting boundary feature tangent if the corresponding boundary segments are tangent."""
		self._instance.MergeTangentFaces = value

	@property
	def thin_feature_reversed(self):
		"""Gets whether this thin feature boundary feature is reversed."""
		return self._instance.ThinFeatureReversed

	@thin_feature_reversed.setter
	def thin_feature_reversed(self, value):
		"""Gets whether this thin feature boundary feature is reversed."""
		self._instance.ThinFeatureReversed = value

	@property
	def thin_feature_thickness(self):
		"""Gets or sets the thickness of this thin feature boundary feature."""
		return self._instance.ThinFeatureThickness

	@thin_feature_thickness.setter
	def thin_feature_thickness(self, value):
		"""Gets or sets the thickness of this thin feature boundary feature."""
		self._instance.ThinFeatureThickness = value

	@property
	def thin_feature_type(self):
		"""Gets or sets the type of thin feature for this boundary feature."""
		return self._instance.ThinFeatureType

	@thin_feature_type.setter
	def thin_feature_type(self, value):
		"""Gets or sets the type of thin feature for this boundary feature."""
		self._instance.ThinFeatureType = value

	@property
	def trim_by_d(self):
		"""Gets whether to trim surfaces in Direction 1 when curves do not form a closed boundary feature."""
		return self._instance.TrimByD1

	@trim_by_d.setter
	def trim_by_d(self, value):
		"""Gets whether to trim surfaces in Direction 1 when curves do not form a closed boundary feature."""
		self._instance.TrimByD1 = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this boundary feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this boundary feature."""
		self._instance.AccessSelections = value

	@property
	def get_alignment_type(self):
		"""Gets the type of alignment for the specified curve in the specified direction for this boundary feature."""
		return self._instance.GetAlignmentType

	@get_alignment_type.setter
	def get_alignment_type(self, value):
		"""Gets the type of alignment for the specified curve in the specified direction for this boundary feature."""
		self._instance.GetAlignmentType = value

	@property
	def get_curves_count(self):
		"""Gets the number of curves in the specified direction in this boundary feature."""
		return self._instance.GetCurvesCount

	@get_curves_count.setter
	def get_curves_count(self, value):
		"""Gets the number of curves in the specified direction in this boundary feature."""
		self._instance.GetCurvesCount = value

	@property
	def get_direction_vector(self):
		"""Gets the entity used as the direction vector for the specified curve in the specified direction in this boundary feature."""
		return self._instance.GetDirectionVector

	@get_direction_vector.setter
	def get_direction_vector(self, value):
		"""Gets the entity used as the direction vector for the specified curve in the specified direction in this boundary feature."""
		self._instance.GetDirectionVector = value

	@property
	def get_draft_angle(self):
		"""Gets the draft angle for the specified curve in the specified direction in this boundary feature."""
		return self._instance.GetDraftAngle

	@get_draft_angle.setter
	def get_draft_angle(self, value):
		"""Gets the draft angle for the specified curve in the specified direction in this boundary feature."""
		self._instance.GetDraftAngle = value

	@property
	def get_draft_angle_reverse_direction(self):
		"""Gets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature."""
		return self._instance.GetDraftAngleReverseDirection

	@get_draft_angle_reverse_direction.setter
	def get_draft_angle_reverse_direction(self, value):
		"""Gets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature."""
		self._instance.GetDraftAngleReverseDirection = value

	@property
	def get_guide_tangency_type(self):
		"""Gets the type of tangency for the specified curve in the specified direction in this boundary feature."""
		return self._instance.GetGuideTangencyType

	@get_guide_tangency_type.setter
	def get_guide_tangency_type(self, value):
		"""Gets the type of tangency for the specified curve in the specified direction in this boundary feature."""
		self._instance.GetGuideTangencyType = value

	@property
	def get_tangent_apply_to_all(self):
		"""Gets whether one handle that controls all constraints for the entire profile is displayed for the specified curve in the specified direction in this boundary feature."""
		return self._instance.GetTangentApplyToAll

	@get_tangent_apply_to_all.setter
	def get_tangent_apply_to_all(self, value):
		"""Gets whether one handle that controls all constraints for the entire profile is displayed for the specified curve in the specified direction in this boundary feature."""
		self._instance.GetTangentApplyToAll = value

	@property
	def get_tangent_direction_reversed(self):
		"""Gets whether the direction of adjacent tangent faces is flipped for the specified curve in the specified direction in this boundary feature."""
		return self._instance.GetTangentDirectionReversed

	@get_tangent_direction_reversed.setter
	def get_tangent_direction_reversed(self, value):
		"""Gets whether the direction of adjacent tangent faces is flipped for the specified curve in the specified direction in this boundary feature."""
		self._instance.GetTangentDirectionReversed = value

	@property
	def get_tangent_influence(self):
		"""Gets the curve influence for the specified curve in the specified direction in this boundary feature."""
		return self._instance.GetTangentInfluence

	@get_tangent_influence.setter
	def get_tangent_influence(self, value):
		"""Gets the curve influence for the specified curve in the specified direction in this boundary feature."""
		self._instance.GetTangentInfluence = value

	@property
	def get_tangent_length(self):
		"""Gets the tangent length, which controls the amount of influence for the specified curve in the specified direction in this boundary feature."""
		return self._instance.GetTangentLength

	@get_tangent_length.setter
	def get_tangent_length(self, value):
		"""Gets the tangent length, which controls the amount of influence for the specified curve in the specified direction in this boundary feature."""
		self._instance.GetTangentLength = value

	@property
	def is_thin_feature(self):
		"""Gets whether the boundary feature is a thin feature."""
		return self._instance.IsThinFeature

	@is_thin_feature.setter
	def is_thin_feature(self, value):
		"""Gets whether the boundary feature is a thin feature."""
		self._instance.IsThinFeature = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this boundary feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this boundary feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_alignment_type(self):
		"""Sets the type of alignment for the specified curve in the specified direction for this boundary feature."""
		return self._instance.SetAlignmentType

	@set_alignment_type.setter
	def set_alignment_type(self, value):
		"""Sets the type of alignment for the specified curve in the specified direction for this boundary feature."""
		self._instance.SetAlignmentType = value

	@property
	def set_direction_vector(self):
		"""Sets the entity to use as the direction vector for the specified curve in the specified direction in this boundary feature."""
		return self._instance.SetDirectionVector

	@set_direction_vector.setter
	def set_direction_vector(self, value):
		"""Sets the entity to use as the direction vector for the specified curve in the specified direction in this boundary feature."""
		self._instance.SetDirectionVector = value

	@property
	def set_draft_angle(self):
		"""Sets the draft angle for the specified curve in the specified direction in this boundary feature."""
		return self._instance.SetDraftAngle

	@set_draft_angle.setter
	def set_draft_angle(self, value):
		"""Sets the draft angle for the specified curve in the specified direction in this boundary feature."""
		self._instance.SetDraftAngle = value

	@property
	def set_draft_angle_reverse_direction(self):
		"""Sets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature."""
		return self._instance.SetDraftAngleReverseDirection

	@set_draft_angle_reverse_direction.setter
	def set_draft_angle_reverse_direction(self, value):
		"""Sets whether the draft angle is flipped for the specified curve in the specified direction in this boundary feature."""
		self._instance.SetDraftAngleReverseDirection = value

	@property
	def set_guide_tangency_type(self):
		"""Sets the type of tangency for the specified curve in the specified direction in this boundary feature."""
		return self._instance.SetGuideTangencyType

	@set_guide_tangency_type.setter
	def set_guide_tangency_type(self, value):
		"""Sets the type of tangency for the specified curve in the specified direction in this boundary feature."""
		self._instance.SetGuideTangencyType = value

	@property
	def set_tangent_apply_to_all(self):
		"""Sets whether to display one handle that controls all constraints for the entire profile for the specified curve in the specified direction in this boundary feature."""
		return self._instance.SetTangentApplyToAll

	@set_tangent_apply_to_all.setter
	def set_tangent_apply_to_all(self, value):
		"""Sets whether to display one handle that controls all constraints for the entire profile for the specified curve in the specified direction in this boundary feature."""
		self._instance.SetTangentApplyToAll = value

	@property
	def set_tangent_direction_reversed(self):
		"""Sets whether the direction of adjacent tangent faces is flipped for the specified curve in the specified direction in this boundary feature."""
		return self._instance.SetTangentDirectionReversed

	@set_tangent_direction_reversed.setter
	def set_tangent_direction_reversed(self, value):
		"""Sets whether the direction of adjacent tangent faces is flipped for the specified curve in the specified direction in this boundary feature."""
		self._instance.SetTangentDirectionReversed = value

	@property
	def set_tangent_influence(self):
		"""Sets the curve influence toward the next curve for the specified curve in the specified direction in this boundary feature."""
		return self._instance.SetTangentInfluence

	@set_tangent_influence.setter
	def set_tangent_influence(self, value):
		"""Sets the curve influence toward the next curve for the specified curve in the specified direction in this boundary feature."""
		self._instance.SetTangentInfluence = value

	@property
	def set_tangent_length(self):
		"""Sets the tangent length, which controls the amount of influence for the specified curve in the specified direction in this boundary feature."""
		return self._instance.SetTangentLength

	@set_tangent_length.setter
	def set_tangent_length(self, value):
		"""Sets the tangent length, which controls the amount of influence for the specified curve in the specified direction in this boundary feature."""
		self._instance.SetTangentLength = value

