# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelationManager_members.html
class ISketchRelationManager:
	def __init__(self, parent=None):
		self._instance = parent

	def add_relation(self, entities, relation_type):
		"""
		Adds a relation to the specified entities in the active sketch.
		:param entities: Array of entities to which add the relation
		:param relation_type: Type of relation as defined by swConstraintType_e
		"""
		# return self._instance.AddRelation(entities, relation_type)
		raise NotImplemented

	def delete_all_relations(self):
		"""Deletes all of the logical sketch relations in the sketch."""
		# return self._instance.DeleteAllRelations
		raise NotImplemented

	def delete_relation(self, this_relation):
		"""
		Deletes the specified logical sketch relation in sketch.
		:param this_relation: Sketch relation
		"""
		# return self._instance.DeleteRelation(this_relation)
		raise NotImplemented

	def get_allowed_relations(self, entities):
		"""
		Gets the types of sketch relations valid for the specified entities.
		:param entities: Array of entities
		"""
		# return self._instance.GetAllowedRelations(entities)
		raise NotImplemented

	def get_relations(self, filter):
		"""
		Gets all of the sketch relations in the sketch based on the specified filter.
		:param filter: Sketch relation as defined in swSketchRelationFilterType_e
		"""
		# return self._instance.GetRelations(filter)
		raise NotImplemented

	def get_relations_count(self, filter):
		"""
		Gets the number of sketch relations in the sketch based on the specified filter.
		:param filter: Sketch relation as defined in swSketchRelationFilterType_e
		"""
		# return self._instance.GetRelationsCount(filter)
		raise NotImplemented

	def i_add_relation(self, num_entities, entity_array, relation_type):
		"""
		Adds a relation to the specified entities in the active sketch.
		:param num_entities: Number of entities to which to add the relation
		:param entity_array: Array of entities to which to add the relation
		:param relation_type: Type of relation as defined by swConstraintType_e
		"""
		# return self._instance.IAddRelation(num_entities, entity_array, relation_type)
		raise NotImplemented

	def i_get_allowed_relations(self, num_entities, entity_array, num_allowed_relations):
		"""
		Gets the types of sketch relations valid for the specified entities.
		:param num_entities: Number of entities
		:param entity_array: Array of entities
		:param num_allowed_relations: Number of relations valid for the specified entities
		"""
		# return self._instance.IGetAllowedRelations(num_entities, entity_array, num_allowed_relations)
		raise NotImplemented

	def i_get_allowed_relations_count(self, num_entities, entity_array):
		"""
		Gets the number of sketch relations valid for the specified entities.
		:param num_entities: Number of entities
		:param entity_array: Array of entities
		"""
		# return self._instance.IGetAllowedRelationsCount(num_entities, entity_array)
		raise NotImplemented

	def i_get_relations(self, filter, count):
		"""
		Gets all of the sketch relations in the sketch based on the specified filter.
		:param filter: Sketch relation as defined in swSketchRelationFilterType_e
		:param count: Number of sketch relations
		"""
		# return self._instance.IGetRelations(filter, count)
		raise NotImplemented

