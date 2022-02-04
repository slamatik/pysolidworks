# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html
class IRevolveFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def assembly_feature_scope(self):
		"""Gets or sets whether to use scope for this assembly revolve feature."""
		return self._instance.AssemblyFeatureScope

	@assembly_feature_scope.setter
	def assembly_feature_scope(self, value):
		"""Gets or sets whether to use scope for this assembly revolve feature."""
		self._instance.AssemblyFeatureScope = value

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all or only specific bodies for the revolve feature to affect in a multibody body."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all or only specific bodies for the revolve feature to affect in a multibody body."""
		self._instance.AutoSelect = value

	@property
	def auto_select_components(self):
		"""Gets or sets whether to auto-select all components that this assembly revolve feature affects in model."""
		return self._instance.AutoSelectComponents

	@auto_select_components.setter
	def auto_select_components(self, value):
		"""Gets or sets whether to auto-select all components that this assembly revolve feature affects in model."""
		self._instance.AutoSelectComponents = value

	@property
	def axis(self):
		"""Gets or sets the axis of revolution for this revolve feature."""
		return self._instance.Axis

	@axis.setter
	def axis(self, value):
		"""Gets or sets the axis of revolution for this revolve feature."""
		self._instance.Axis = value

	@property
	def contours(self):
		"""Gets and sets the selected contours on this revolve feature."""
		return self._instance.Contours

	@contours.setter
	def contours(self, value):
		"""Gets and sets the selected contours on this revolve feature."""
		self._instance.Contours = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for the revolve feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for the revolve feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies that the revolve feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies that the revolve feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def merge(self):
		"""Gets or sets whether to merge the results of this revolve feature in a multibody part."""
		return self._instance.Merge

	@merge.setter
	def merge(self, value):
		"""Gets or sets whether to merge the results of this revolve feature in a multibody part."""
		self._instance.Merge = value

	@property
	def propagate_feature_to_parts(self):
		"""Gets whether to propagate this assembly revolve feature to the parts that it affects in this model."""
		return self._instance.PropagateFeatureToParts

	@propagate_feature_to_parts.setter
	def propagate_feature_to_parts(self, value):
		"""Gets whether to propagate this assembly revolve feature to the parts that it affects in this model."""
		self._instance.PropagateFeatureToParts = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether the direction of the revolution feature should be reversed."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether the direction of the revolution feature should be reversed."""
		self._instance.ReverseDirection = value

	@property
	def thin_wall_type(self):
		"""Gets and sets the thin wall type for a thin revolve feature."""
		return self._instance.ThinWallType

	@thin_wall_type.setter
	def thin_wall_type(self, value):
		"""Gets and sets the thin wall type for a thin revolve feature."""
		self._instance.ThinWallType = value

	@property
	def type(self):
		"""Gets or sets the revolution feature type."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the revolution feature type."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this revolve feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this revolve feature."""
		self._instance.AccessSelections = value

	@property
	def get_axis_type(self):
		"""Gets the type of axis of revolution for this revolve feature."""
		return self._instance.GetAxisType

	@get_axis_type.setter
	def get_axis_type(self, value):
		"""Gets the type of axis of revolution for this revolve feature."""
		self._instance.GetAxisType = value

	@property
	def get_contours_count(self):
		"""Gets the number of selected contours for this revolve feature."""
		return self._instance.GetContoursCount

	@get_contours_count.setter
	def get_contours_count(self, value):
		"""Gets the number of selected contours for this revolve feature."""
		self._instance.GetContoursCount = value

	@property
	def get_feature_scope_bodies_count(self):
		"""Gets the number of solid bodies affected by the revolve feature in a multibody part."""
		return self._instance.GetFeatureScopeBodiesCount

	@get_feature_scope_bodies_count.setter
	def get_feature_scope_bodies_count(self, value):
		"""Gets the number of solid bodies affected by the revolve feature in a multibody part."""
		self._instance.GetFeatureScopeBodiesCount = value

	@property
	def get_revolution_angle(self):
		"""Gets the angle of the revolve feature in Direction 1 or Direction 2."""
		return self._instance.GetRevolutionAngle

	@get_revolution_angle.setter
	def get_revolution_angle(self, value):
		"""Gets the angle of the revolve feature in Direction 1 or Direction 2."""
		self._instance.GetRevolutionAngle = value

	@property
	def get_wall_thickness(self):
		"""Gets the wall thickness of the thin revolution feature in forward or reverse direction."""
		return self._instance.GetWallThickness

	@get_wall_thickness.setter
	def get_wall_thickness(self, value):
		"""Gets the wall thickness of the thin revolution feature in forward or reverse direction."""
		self._instance.GetWallThickness = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this revolve feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this revolve feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_contours(self):
		"""Gets the selected contours for this revolve feature."""
		return self._instance.IGetContours

	@i_get_contours.setter
	def i_get_contours(self, value):
		"""Gets the selected contours for this revolve feature."""
		self._instance.IGetContours = value

	@property
	def i_get_feature_scope_bodies(self):
		"""Gets the solid bodies that the revolve feature affects in a multibody part."""
		return self._instance.IGetFeatureScopeBodies

	@i_get_feature_scope_bodies.setter
	def i_get_feature_scope_bodies(self, value):
		"""Gets the solid bodies that the revolve feature affects in a multibody part."""
		self._instance.IGetFeatureScopeBodies = value

	@property
	def is_boss_feature(self):
		"""Gets whether the revolution is a boss feature."""
		return self._instance.IsBossFeature

	@is_boss_feature.setter
	def is_boss_feature(self, value):
		"""Gets whether the revolution is a boss feature."""
		self._instance.IsBossFeature = value

	@property
	def i_set_contours(self):
		"""Sets the selected contours for this revolve feature."""
		return self._instance.ISetContours

	@i_set_contours.setter
	def i_set_contours(self, value):
		"""Sets the selected contours for this revolve feature."""
		self._instance.ISetContours = value

	@property
	def i_set_feature_scope_bodies(self):
		"""Sets the solid bodies that the revolve feature affects in a multibody part."""
		return self._instance.ISetFeatureScopeBodies

	@i_set_feature_scope_bodies.setter
	def i_set_feature_scope_bodies(self, value):
		"""Sets the solid bodies that the revolve feature affects in a multibody part."""
		self._instance.ISetFeatureScopeBodies = value

	@property
	def is_thin_feature(self):
		"""Gets whether the revolution is a thin feature."""
		return self._instance.IsThinFeature

	@is_thin_feature.setter
	def is_thin_feature(self, value):
		"""Gets whether the revolution is a thin feature."""
		self._instance.IsThinFeature = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this revolve feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this revolve feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_revolution_angle(self):
		"""Sets the angle of the revolve feature in Direction 1 or Direction 2."""
		return self._instance.SetRevolutionAngle

	@set_revolution_angle.setter
	def set_revolution_angle(self, value):
		"""Sets the angle of the revolve feature in Direction 1 or Direction 2."""
		self._instance.SetRevolutionAngle = value

	@property
	def set_wall_thickness(self):
		"""Sets the wall thickness of the thin revolution feature in forward/reverse direction."""
		return self._instance.SetWallThickness

	@set_wall_thickness.setter
	def set_wall_thickness(self, value):
		"""Sets the wall thickness of the thin revolution feature in forward/reverse direction."""
		self._instance.SetWallThickness = value

