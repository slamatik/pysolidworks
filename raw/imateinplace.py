# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.html
class IMateInPlace:
	def __init__(self, parent=None):
		self._instance = parent

	def component(self):
		"""Gets the component for this Inplace mate."""
		# return self._instance.Component
		raise NotImplemented

	def mate_component_name(self, n_index):
		"""
		Gets the name of the specified component for this Inplace mate.
		:param n_index: 0-based index associated with the specified component
		"""
		# return self._instance.MateComponentName(n_index)
		raise NotImplemented

	def mate_entity(self, n_index):
		"""
		Gets the name of the mated entity associated with the specified index for this Inplace mate.
		:param n_index: 0-based index associated with this entity
		"""
		# return self._instance.MateEntity(n_index)
		raise NotImplemented

	def mate_entity_type(self, n_index):
		"""
		Gets the type of entity in this Inplace mate.
		:param n_index: 0-based index associated with this entity
		"""
		# return self._instance.MateEntityType(n_index)
		raise NotImplemented

	def get_mate_entity_count(self):
		"""Gets the number of Inplace mated entities in this assembly."""
		# return self._instance.GetMateEntityCount
		raise NotImplemented

