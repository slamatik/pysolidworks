# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceOffsetFeatureData_members.html
class ISurfaceOffsetFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def distance(self):
		"""Gets or sets the offset distance for this surface offset feature."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the offset distance for this surface offset feature."""
		self._instance.Distance = value

	@property
	def entities(self):
		"""Gets or sets the offset surfaces and faces of this surface offset feature."""
		return self._instance.Entities

	@entities.setter
	def entities(self, value):
		"""Gets or sets the offset surfaces and faces of this surface offset feature."""
		self._instance.Entities = value

	@property
	def flip(self):
		"""Gets or sets the offset flip setting for this surface offset feature."""
		return self._instance.Flip

	@flip.setter
	def flip(self, value):
		"""Gets or sets the offset flip setting for this surface offset feature."""
		self._instance.Flip = value

	@property
	def access_selections(self):
		"""Accesses the selections that define this surface offset feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections that define this surface offset feature."""
		self._instance.AccessSelections = value

	@property
	def get_entities_count(self):
		"""Gets the number of offset surfaces and faces for this surface offset feature."""
		return self._instance.GetEntitiesCount

	@get_entities_count.setter
	def get_entities_count(self, value):
		"""Gets the number of offset surfaces and faces for this surface offset feature."""
		self._instance.GetEntitiesCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections that define this surface offset feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections that define this surface offset feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_entities(self):
		"""Gets the offset surfaces or faces of this surface offset feature."""
		return self._instance.IGetEntities

	@i_get_entities.setter
	def i_get_entities(self, value):
		"""Gets the offset surfaces or faces of this surface offset feature."""
		self._instance.IGetEntities = value

	@property
	def i_set_entities(self):
		"""Sets the offset surfaces or faces for this surface offset feature."""
		return self._instance.ISetEntities

	@i_set_entities.setter
	def i_set_entities(self, value):
		"""Sets the offset surfaces or faces for this surface offset feature."""
		self._instance.ISetEntities = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this surface offset feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this surface offset feature."""
		self._instance.ReleaseSelectionAccess = value

