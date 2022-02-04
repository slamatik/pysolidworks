# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.html
class ISketchRelation:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def suppressed(self):
		"""Gets or sets whether this relation is suppressed or not."""
		return self._instance.Suppressed

	@suppressed.setter
	def suppressed(self, value):
		"""Gets or sets whether this relation is suppressed or not."""
		self._instance.Suppressed = value

	@property
	def get_definition_entities(self):
		"""Gets the actual entities associated with this sketch relation."""
		return self._instance.GetDefinitionEntities2

	@get_definition_entities.setter
	def get_definition_entities(self, value):
		"""Gets the actual entities associated with this sketch relation."""
		self._instance.GetDefinitionEntities2 = value

	@property
	def get_display_dimension(self):
		"""Gets the display dimension object for this sketch relation."""
		return self._instance.GetDisplayDimension

	@get_display_dimension.setter
	def get_display_dimension(self, value):
		"""Gets the display dimension object for this sketch relation."""
		self._instance.GetDisplayDimension = value

	@property
	def get_entities(self):
		"""Gets the entities associated with this sketch relation."""
		return self._instance.GetEntities

	@get_entities.setter
	def get_entities(self, value):
		"""Gets the entities associated with this sketch relation."""
		self._instance.GetEntities = value

	@property
	def get_entities_count(self):
		"""Gets the number of entities associated with this sketch relation."""
		return self._instance.GetEntitiesCount

	@get_entities_count.setter
	def get_entities_count(self, value):
		"""Gets the number of entities associated with this sketch relation."""
		self._instance.GetEntitiesCount = value

	@property
	def get_entities_type(self):
		"""Gets the types of entities in this sketch relation."""
		return self._instance.GetEntitiesType

	@get_entities_type.setter
	def get_entities_type(self, value):
		"""Gets the types of entities in this sketch relation."""
		self._instance.GetEntitiesType = value

	@property
	def get_relation_type(self):
		"""Gets the type of sketch relation."""
		return self._instance.GetRelationType

	@get_relation_type.setter
	def get_relation_type(self, value):
		"""Gets the type of sketch relation."""
		self._instance.GetRelationType = value

	@property
	def i_get_definition_entities(self):
		"""Gets the actual entities associated with this sketch relation."""
		return self._instance.IGetDefinitionEntities2

	@i_get_definition_entities.setter
	def i_get_definition_entities(self, value):
		"""Gets the actual entities associated with this sketch relation."""
		self._instance.IGetDefinitionEntities2 = value

	@property
	def i_get_entities(self):
		"""Gets the entities associated with this sketch relation."""
		return self._instance.IGetEntities

	@i_get_entities.setter
	def i_get_entities(self, value):
		"""Gets the entities associated with this sketch relation."""
		self._instance.IGetEntities = value

	@property
	def i_get_entities_type(self):
		"""Gets the types of entities in this sketch relation."""
		return self._instance.IGetEntitiesType

	@i_get_entities_type.setter
	def i_get_entities_type(self, value):
		"""Gets the types of entities in this sketch relation."""
		self._instance.IGetEntitiesType = value

	@property
	def replace_entity(self):
		"""Replaces an entity in this sketch relation."""
		return self._instance.ReplaceEntity

	@replace_entity.setter
	def replace_entity(self, value):
		"""Replaces an entity in this sketch relation."""
		self._instance.ReplaceEntity = value

