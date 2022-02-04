# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThickenFeatureData_members.html
class IThickenFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all or only specific bodies for the thicken feature to affect in a multibody part."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all or only specific bodies for the thicken feature to affect in a multibody part."""
		self._instance.AutoSelect = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for the thicken feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for the thicken feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies that the thicken feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies that the thicken feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def fill_volume(self):
		"""Gets or sets whether to fill a volume with this thicken feature."""
		return self._instance.FillVolume

	@fill_volume.setter
	def fill_volume(self, value):
		"""Gets or sets whether to fill a volume with this thicken feature."""
		self._instance.FillVolume = value

	@property
	def merge(self):
		"""Gets or sets whether to merge the results of this thicken feature in a multibody part."""
		return self._instance.Merge

	@merge.setter
	def merge(self, value):
		"""Gets or sets whether to merge the results of this thicken feature in a multibody part."""
		self._instance.Merge = value

	@property
	def surface(self):
		"""Gets or sets the thickened surface."""
		return self._instance.Surface

	@surface.setter
	def surface(self, value):
		"""Gets or sets the thickened surface."""
		self._instance.Surface = value

	@property
	def thickness(self):
		"""Gets or sets the thickness for this thicken feature."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or sets the thickness for this thicken feature."""
		self._instance.Thickness = value

	@property
	def thickness_side(self):
		"""Gets or sets which side to apply thickness."""
		return self._instance.ThicknessSide

	@thickness_side.setter
	def thickness_side(self, value):
		"""Gets or sets which side to apply thickness."""
		self._instance.ThicknessSide = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this thicken feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this thicken feature."""
		self._instance.AccessSelections = value

	@property
	def get_feature_scope_bodies_count(self):
		"""Gets the number of solid bodies affected by the thicken feature in a multibody part."""
		return self._instance.GetFeatureScopeBodiesCount

	@get_feature_scope_bodies_count.setter
	def get_feature_scope_bodies_count(self, value):
		"""Gets the number of solid bodies affected by the thicken feature in a multibody part."""
		self._instance.GetFeatureScopeBodiesCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this thicken feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this thicken feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_feature_scope_bodies(self):
		"""Gets the solid bodies that the thicken feature affects in a multibody part."""
		return self._instance.IGetFeatureScopeBodies

	@i_get_feature_scope_bodies.setter
	def i_get_feature_scope_bodies(self, value):
		"""Gets the solid bodies that the thicken feature affects in a multibody part."""
		self._instance.IGetFeatureScopeBodies = value

	@property
	def is_boss_feature(self):
		"""Gets whether this feature is a boss or a cut."""
		return self._instance.IsBossFeature

	@is_boss_feature.setter
	def is_boss_feature(self, value):
		"""Gets whether this feature is a boss or a cut."""
		self._instance.IsBossFeature = value

	@property
	def i_set_feature_scope_bodies(self):
		"""Sets the solid bodies that the thicken feature affects in a multibody part."""
		return self._instance.ISetFeatureScopeBodies

	@i_set_feature_scope_bodies.setter
	def i_set_feature_scope_bodies(self, value):
		"""Sets the solid bodies that the thicken feature affects in a multibody part."""
		self._instance.ISetFeatureScopeBodies = value

	@property
	def release_selection_access(self):
		"""Releases the selections that created this thicken feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases the selections that created this thicken feature."""
		self._instance.ReleaseSelectionAccess = value

