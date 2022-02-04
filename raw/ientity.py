# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity_members.html
class IEntity:
	def __init__(self, parent=None):
		self._instance = parent

	def is_safe(self):
		"""Gets whether this IEntity object survived a rebuild."""
		# return self._instance.IsSafe
		raise NotImplemented

	@property
	def model_name(self):
		"""Gets or sets the standard Parasolid name attribute of the entity."""
		return self._instance.ModelName

	@model_name.setter
	def model_name(self, value):
		"""Gets or sets the standard Parasolid name attribute of the entity."""
		self._instance.ModelName = value

	@property
	def find_attribute(self):
		"""Finds an attribute on an entity."""
		return self._instance.FindAttribute

	@find_attribute.setter
	def find_attribute(self, value):
		"""Finds an attribute on an entity."""
		self._instance.FindAttribute = value

	@property
	def get_component(self):
		"""Gets the owning component for this entity."""
		return self._instance.GetComponent

	@get_component.setter
	def get_component(self, value):
		"""Gets the owning component for this entity."""
		self._instance.GetComponent = value

	@property
	def get_distance(self):
		"""Gets the minimum or maximum distance between this entity and the given face or edge entity (see Remarks)."""
		return self._instance.GetDistance

	@get_distance.setter
	def get_distance(self, value):
		"""Gets the minimum or maximum distance between this entity and the given face or edge entity (see Remarks)."""
		self._instance.GetDistance = value

	@property
	def get_drawing_component(self):
		"""Gets the drawing component that owns this entity, if the entity is in a drawing view."""
		return self._instance.GetDrawingComponent

	@get_drawing_component.setter
	def get_drawing_component(self, value):
		"""Gets the drawing component that owns this entity, if the entity is in a drawing view."""
		self._instance.GetDrawingComponent = value

	@property
	def get_safe_entity(self):
		"""Gets a safe entity."""
		return self._instance.GetSafeEntity

	@get_safe_entity.setter
	def get_safe_entity(self, value):
		"""Gets a safe entity."""
		self._instance.GetSafeEntity = value

	@property
	def get_type(self):
		"""Gets the type of the entity."""
		return self._instance.GetType

	@get_type.setter
	def get_type(self, value):
		"""Gets the type of the entity."""
		self._instance.GetType = value

	@property
	def i_find_attribute(self):
		"""Finds an attribute on an entity."""
		return self._instance.IFindAttribute

	@i_find_attribute.setter
	def i_find_attribute(self, value):
		"""Finds an attribute on an entity."""
		self._instance.IFindAttribute = value

	@property
	def i_get_component(self):
		"""Gets the owning component for this entity."""
		return self._instance.IGetComponent2

	@i_get_component.setter
	def i_get_component(self, value):
		"""Gets the owning component for this entity."""
		self._instance.IGetComponent2 = value

	@property
	def i_get_distance(self):
		"""Gets the minimum or maximum distance between this entity and the given face or edge entity (see Remarks)."""
		return self._instance.IGetDistance

	@i_get_distance.setter
	def i_get_distance(self, value):
		"""Gets the minimum or maximum distance between this entity and the given face or edge entity (see Remarks)."""
		self._instance.IGetDistance = value

	@property
	def select(self):
		"""Selects an entity and marks it."""
		return self._instance.Select4

	@select.setter
	def select(self, value):
		"""Selects an entity and marks it."""
		self._instance.Select4 = value

