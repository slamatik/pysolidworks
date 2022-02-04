# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html
class IDisplayStateSetting:
	def __init__(self, parent=None):
		self._instance = parent

	def entities(self):
		"""Gets and sets the entities for this display state setting."""
		# return self._instance.Entities
		raise NotImplemented

	def names(self):
		"""Gets and sets the display state names for this display state setting."""
		# return self._instance.Names
		raise NotImplemented

	def option(self):
		"""Gets and sets the display state scope for this display state setting."""
		# return self._instance.Option
		raise NotImplemented

	@property
	def part_level(self):
		"""Gets or sets whether to set at the part level."""
		return self._instance.PartLevel

	@part_level.setter
	def part_level(self, value):
		"""Gets or sets whether to set at the part level."""
		self._instance.PartLevel = value

	@property
	def remove_appearance(self):
		"""Gets or sets whether to remove appearances for this display state setting."""
		return self._instance.RemoveAppearance

	@remove_appearance.setter
	def remove_appearance(self, value):
		"""Gets or sets whether to remove appearances for this display state setting."""
		self._instance.RemoveAppearance = value

	@property
	def get_entity_count(self):
		"""Gets the number of entities for this display state setting."""
		return self._instance.GetEntityCount

	@get_entity_count.setter
	def get_entity_count(self, value):
		"""Gets the number of entities for this display state setting."""
		self._instance.GetEntityCount = value

	@property
	def get_name_count(self):
		"""Gets the number of display states for this display state setting."""
		return self._instance.GetNameCount

	@get_name_count.setter
	def get_name_count(self, value):
		"""Gets the number of display states for this display state setting."""
		self._instance.GetNameCount = value

	@property
	def i_get_entities(self):
		"""Gets the entities for this display state setting."""
		return self._instance.IGetEntities

	@i_get_entities.setter
	def i_get_entities(self, value):
		"""Gets the entities for this display state setting."""
		self._instance.IGetEntities = value

	@property
	def i_get_names(self):
		"""Gets the display state names for this display state setting."""
		return self._instance.IGetNames

	@i_get_names.setter
	def i_get_names(self, value):
		"""Gets the display state names for this display state setting."""
		self._instance.IGetNames = value

	@property
	def i_set_entities(self):
		"""Sets the entities for this display state setting."""
		return self._instance.ISetEntities

	@i_set_entities.setter
	def i_set_entities(self, value):
		"""Sets the entities for this display state setting."""
		self._instance.ISetEntities = value

	@property
	def i_set_names(self):
		"""Sets the display state names for this display state setting."""
		return self._instance.ISetNames

	@i_set_names.setter
	def i_set_names(self, value):
		"""Sets the display state names for this display state setting."""
		self._instance.ISetNames = value

