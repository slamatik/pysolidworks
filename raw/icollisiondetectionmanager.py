# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.html
class ICollisionDetectionManager:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def graphics_redraw_enabled(self):
		"""Gets or sets whether to display components in their transformed positions."""
		return self._instance.GraphicsRedrawEnabled

	@graphics_redraw_enabled.setter
	def graphics_redraw_enabled(self, value):
		"""Gets or sets whether to display components in their transformed positions."""
		self._instance.GraphicsRedrawEnabled = value

	@property
	def create_group(self):
		"""Creates a collision detection group of non-colliding components."""
		return self._instance.CreateGroup

	@create_group.setter
	def create_group(self, value):
		"""Creates a collision detection group of non-colliding components."""
		self._instance.CreateGroup = value

	@property
	def get_assembly(self):
		"""Gets the active assembly for this collision detection manager."""
		return self._instance.GetAssembly

	@get_assembly.setter
	def get_assembly(self, value):
		"""Gets the active assembly for this collision detection manager."""
		self._instance.GetAssembly = value

	@property
	def get_collisions(self):
		"""Gets the collisions detected."""
		return self._instance.GetCollisions

	@get_collisions.setter
	def get_collisions(self, value):
		"""Gets the collisions detected."""
		self._instance.GetCollisions = value

	@property
	def get_group(self):
		"""Gets the specified collision detection group."""
		return self._instance.GetGroup

	@get_group.setter
	def get_group(self, value):
		"""Gets the specified collision detection group."""
		self._instance.GetGroup = value

	@property
	def get_group_count(self):
		"""Gets the number of collision detection groups currently defined."""
		return self._instance.GetGroupCount

	@get_group_count.setter
	def get_group_count(self, value):
		"""Gets the number of collision detection groups currently defined."""
		self._instance.GetGroupCount = value

	@property
	def is_collision_present(self):
		"""Performs collision detection analysis between all groups of components."""
		return self._instance.IsCollisionPresent

	@is_collision_present.setter
	def is_collision_present(self, value):
		"""Performs collision detection analysis between all groups of components."""
		self._instance.IsCollisionPresent = value

	@property
	def remove_group(self):
		"""Removes the specified collision detection group from collision detection."""
		return self._instance.RemoveGroup

	@remove_group.setter
	def remove_group(self, value):
		"""Removes the specified collision detection group from collision detection."""
		self._instance.RemoveGroup = value

	@property
	def set_assembly(self):
		"""Sets the active assembly for this collision detection manager."""
		return self._instance.SetAssembly

	@set_assembly.setter
	def set_assembly(self, value):
		"""Sets the active assembly for this collision detection manager."""
		self._instance.SetAssembly = value

