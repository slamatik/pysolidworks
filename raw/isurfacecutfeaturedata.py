# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceCutFeatureData_members.html
class ISurfaceCutFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all or only specific bodies for the surface-cut feature to affect in a multibody part."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all or only specific bodies for the surface-cut feature to affect in a multibody part."""
		self._instance.AutoSelect = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for the surface-cut feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for the surface-cut feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies that the surface-cut feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies that the surface-cut feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def flip(self):
		"""Gets or sets the flip setting for this surface cut."""
		return self._instance.Flip

	@flip.setter
	def flip(self, value):
		"""Gets or sets the flip setting for this surface cut."""
		self._instance.Flip = value

	@property
	def surface_for_cut(self):
		"""Gets or sets the surface to use to cut the solid bodies."""
		return self._instance.SurfaceForCut

	@surface_for_cut.setter
	def surface_for_cut(self, value):
		"""Gets or sets the surface to use to cut the solid bodies."""
		self._instance.SurfaceForCut = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this surface-cut feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this surface-cut feature."""
		self._instance.AccessSelections = value

	@property
	def get_body_index_kept(self):
		"""Gets the index of the body kept while resolving ambiguity for this surface-cut feature."""
		return self._instance.GetBodyIndexKept

	@get_body_index_kept.setter
	def get_body_index_kept(self, value):
		"""Gets the index of the body kept while resolving ambiguity for this surface-cut feature."""
		self._instance.GetBodyIndexKept = value

	@property
	def get_feature_scope_bodies_count(self):
		"""Gets the number of bodies affected by this surface-cut feature."""
		return self._instance.GetFeatureScopeBodiesCount

	@get_feature_scope_bodies_count.setter
	def get_feature_scope_bodies_count(self, value):
		"""Gets the number of bodies affected by this surface-cut feature."""
		self._instance.GetFeatureScopeBodiesCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this surface-cut feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this surface-cut feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_feature_scope_bodies(self):
		"""Gets the solid bodies that the surface-cut feature affects in a multibody part."""
		return self._instance.IGetFeatureScopeBodies

	@i_get_feature_scope_bodies.setter
	def i_get_feature_scope_bodies(self, value):
		"""Gets the solid bodies that the surface-cut feature affects in a multibody part."""
		self._instance.IGetFeatureScopeBodies = value

	@property
	def i_set_feature_scope_bodies(self):
		"""Sets the solid bodies that this surface-cut feature affects in a multibody part."""
		return self._instance.ISetFeatureScopeBodies

	@i_set_feature_scope_bodies.setter
	def i_set_feature_scope_bodies(self, value):
		"""Sets the solid bodies that this surface-cut feature affects in a multibody part."""
		self._instance.ISetFeatureScopeBodies = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created this surface-cut feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created this surface-cut feature."""
		self._instance.ReleaseSelectionAccess = value

