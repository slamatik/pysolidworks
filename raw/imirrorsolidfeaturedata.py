# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html
class IMirrorSolidFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def face(self):
		"""Gets or sets the end-condition face for this mirror solid feature."""
		return self._instance.Face

	@face.setter
	def face(self, value):
		"""Gets or sets the end-condition face for this mirror solid feature."""
		self._instance.Face = value

	@property
	def knit_surface(self):
		"""Gets or sets whether to knit the surface for this mirror solid feature."""
		return self._instance.KnitSurface

	@knit_surface.setter
	def knit_surface(self, value):
		"""Gets or sets whether to knit the surface for this mirror solid feature."""
		self._instance.KnitSurface = value

	@property
	def merge(self):
		"""Gets or sets the merge results option for the mirrored solid feature in a multibody part."""
		return self._instance.Merge

	@merge.setter
	def merge(self, value):
		"""Gets or sets the merge results option for the mirrored solid feature in a multibody part."""
		self._instance.Merge = value

	@property
	def pattern_body_array(self):
		"""Gets or sets the seed bodies to pattern for this mirror solid feature."""
		return self._instance.PatternBodyArray

	@pattern_body_array.setter
	def pattern_body_array(self, value):
		"""Gets or sets the seed bodies to pattern for this mirror solid feature."""
		self._instance.PatternBodyArray = value

	@property
	def propagate_visual_property(self):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all mirrored instances."""
		return self._instance.PropagateVisualProperty

	@propagate_visual_property.setter
	def propagate_visual_property(self, value):
		"""Gets or sets whether to propagate visual properties (e.g., colors, textures, etc.) to all mirrored instances."""
		self._instance.PropagateVisualProperty = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define the mirror solid feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define the mirror solid feature."""
		self._instance.AccessSelections = value

	@property
	def get_pattern_body_count(self):
		"""Gets the number of seed bodies in this mirror solid feature."""
		return self._instance.GetPatternBodyCount

	@get_pattern_body_count.setter
	def get_pattern_body_count(self, value):
		"""Gets the number of seed bodies in this mirror solid feature."""
		self._instance.GetPatternBodyCount = value

	@property
	def get_transform(self):
		"""Gets the transform for this mirror-solid feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform for this mirror-solid feature."""
		self._instance.GetTransform = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define the mirror solid feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define the mirror solid feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_pattern_body_array(self):
		"""Gets the seed bodies for this mirror solid feature."""
		return self._instance.IGetPatternBodyArray

	@i_get_pattern_body_array.setter
	def i_get_pattern_body_array(self, value):
		"""Gets the seed bodies for this mirror solid feature."""
		self._instance.IGetPatternBodyArray = value

	@property
	def i_set_pattern_body_array(self):
		"""Sets the seed bodies for this mirror solid feature."""
		return self._instance.ISetPatternBodyArray

	@i_set_pattern_body_array.setter
	def i_set_pattern_body_array(self, value):
		"""Sets the seed bodies for this mirror solid feature."""
		self._instance.ISetPatternBodyArray = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the mirror solid feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the mirror solid feature."""
		self._instance.ReleaseSelectionAccess = value

