# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData_members.html
class ISurfaceKnitFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entities(self):
		"""Gets or sets the knitted faces and surfaces."""
		return self._instance.Entities

	@entities.setter
	def entities(self, value):
		"""Gets or sets the knitted faces and surfaces."""
		self._instance.Entities = value

	@property
	def knit_tolerance(self):
		"""Gets or sets the knit tolerance for this Surface-Knit feature."""
		return self._instance.KnitTolerance

	@knit_tolerance.setter
	def knit_tolerance(self, value):
		"""Gets or sets the knit tolerance for this Surface-Knit feature."""
		self._instance.KnitTolerance = value

	@property
	def max_value_for_gap_range(self):
		"""Gets or sets the maximum gap range for this Surface-Knit feature."""
		return self._instance.MaxValueForGapRange

	@max_value_for_gap_range.setter
	def max_value_for_gap_range(self, value):
		"""Gets or sets the maximum gap range for this Surface-Knit feature."""
		self._instance.MaxValueForGapRange = value

	@property
	def min_value_for_gap_range(self):
		"""Gets or sets the minimum gap range for this Surface-Knit feature."""
		return self._instance.MinValueForGapRange

	@min_value_for_gap_range.setter
	def min_value_for_gap_range(self, value):
		"""Gets or sets the minimum gap range for this Surface-Knit feature."""
		self._instance.MinValueForGapRange = value

	@property
	def seed_face(self):
		"""Gets or sets the seed face for this surface knit feature."""
		return self._instance.SeedFace

	@seed_face.setter
	def seed_face(self, value):
		"""Gets or sets the seed face for this surface knit feature."""
		self._instance.SeedFace = value

	@property
	def use_gap_filters(self):
		"""Gets or sets whether to use gap filters for this Surface-Knit feature."""
		return self._instance.UseGapFilters

	@use_gap_filters.setter
	def use_gap_filters(self, value):
		"""Gets or sets whether to use gap filters for this Surface-Knit feature."""
		self._instance.UseGapFilters = value

	@property
	def use_merge_entities(self):
		"""Get or sets whether to merge edges and faces by removing redundant vertices and edges when creating the Surface-Knit feature."""
		return self._instance.UseMergeEntities

	@use_merge_entities.setter
	def use_merge_entities(self, value):
		"""Get or sets whether to merge edges and faces by removing redundant vertices and edges when creating the Surface-Knit feature."""
		self._instance.UseMergeEntities = value

	@property
	def use_try_to_form_solid(self):
		"""Gets or sets whether to try to form a solid body when creating the Surface-Knit feature."""
		return self._instance.UseTryToFormSolid

	@use_try_to_form_solid.setter
	def use_try_to_form_solid(self, value):
		"""Gets or sets whether to try to form a solid body when creating the Surface-Knit feature."""
		self._instance.UseTryToFormSolid = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this Surface-Knit feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this Surface-Knit feature."""
		self._instance.AccessSelections = value

	@property
	def get_entities_count(self):
		"""Gets the number of knit faces and surfaces for this Surface-Knit feature."""
		return self._instance.GetEntitiesCount

	@get_entities_count.setter
	def get_entities_count(self, value):
		"""Gets the number of knit faces and surfaces for this Surface-Knit feature."""
		self._instance.GetEntitiesCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this Surface-Knit feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this Surface-Knit feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_entities(self):
		"""Gets the knitted faces and surfaces for this Surface-Knit feature."""
		return self._instance.IGetEntities

	@i_get_entities.setter
	def i_get_entities(self, value):
		"""Gets the knitted faces and surfaces for this Surface-Knit feature."""
		self._instance.IGetEntities = value

	@property
	def i_set_entities(self):
		"""Sets the faces and surfaces to knit."""
		return self._instance.ISetEntities

	@i_set_entities.setter
	def i_set_entities(self, value):
		"""Sets the faces and surfaces to knit."""
		self._instance.ISetEntities = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this Surface-Knit feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this Surface-Knit feature."""
		self._instance.ReleaseSelectionAccess = value

