# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfacePlanarFeatureData_members.html
class ISurfacePlanarFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bounding_entities(self):
		"""Gets or sets the bounding entities for this planar surface feature."""
		return self._instance.BoundingEntities

	@bounding_entities.setter
	def bounding_entities(self, value):
		"""Gets or sets the bounding entities for this planar surface feature."""
		self._instance.BoundingEntities = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this planar surface feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this planar surface feature."""
		self._instance.AccessSelections = value

	@property
	def get_bounding_entities_count(self):
		"""Gets the number of bounding entities for this planar surface feature."""
		return self._instance.GetBoundingEntitiesCount

	@get_bounding_entities_count.setter
	def get_bounding_entities_count(self, value):
		"""Gets the number of bounding entities for this planar surface feature."""
		self._instance.GetBoundingEntitiesCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this planar surface feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this planar surface feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_bounding_entities(self):
		"""Gets the bounding entities for this planar surface feature."""
		return self._instance.IGetBoundingEntities

	@i_get_bounding_entities.setter
	def i_get_bounding_entities(self, value):
		"""Gets the bounding entities for this planar surface feature."""
		self._instance.IGetBoundingEntities = value

	@property
	def i_set_bounding_entities(self):
		"""Sets the bounding entities for this planar surface feature."""
		return self._instance.ISetBoundingEntities

	@i_set_bounding_entities.setter
	def i_set_bounding_entities(self, value):
		"""Sets the bounding entities for this planar surface feature."""
		self._instance.ISetBoundingEntities = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this planar surface feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this planar surface feature."""
		self._instance.ReleaseSelectionAccess = value

