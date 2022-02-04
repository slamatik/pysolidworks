# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep_members.html
class IPartExplodeStep:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_space_bodies_on_drag(self):
		"""Gets or sets whether to automatically space a group of bodies equally along an axis as you drag them in this explode step."""
		return self._instance.AutoSpaceBodiesOnDrag

	@auto_space_bodies_on_drag.setter
	def auto_space_bodies_on_drag(self, value):
		"""Gets or sets whether to automatically space a group of bodies equally along an axis as you drag them in this explode step."""
		self._instance.AutoSpaceBodiesOnDrag = value

	@property
	def explode_distance(self):
		"""Gets or sets the distance to move bodies in this explode step."""
		return self._instance.ExplodeDistance

	@explode_distance.setter
	def explode_distance(self, value):
		"""Gets or sets the distance to move bodies in this explode step."""
		self._instance.ExplodeDistance = value

	@property
	def name(self):
		"""Gets or sets the name of this explode step."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the name of this explode step."""
		self._instance.Name = value

	@property
	def reverse_translation_direction(self):
		"""Gets or sets whether to reverse the direction of explode in this explode step."""
		return self._instance.ReverseTranslationDirection

	@reverse_translation_direction.setter
	def reverse_translation_direction(self, value):
		"""Gets or sets whether to reverse the direction of explode in this explode step."""
		self._instance.ReverseTranslationDirection = value

	@property
	def get_bodies(self):
		"""Gets the bodies of this explode step."""
		return self._instance.GetBodies

	@get_bodies.setter
	def get_bodies(self, value):
		"""Gets the bodies of this explode step."""
		self._instance.GetBodies = value

	@property
	def get_explode_direction(self):
		"""Gets the explode direction (manipulator index and entity) for this explode step."""
		return self._instance.GetExplodeDirection

	@get_explode_direction.setter
	def get_explode_direction(self, value):
		"""Gets the explode direction (manipulator index and entity) for this explode step."""
		self._instance.GetExplodeDirection = value

	@property
	def set_bodies(self):
		"""Sets the bodies of this explode step."""
		return self._instance.SetBodies

	@set_bodies.setter
	def set_bodies(self, value):
		"""Sets the bodies of this explode step."""
		self._instance.SetBodies = value

	@property
	def set_explode_direction(self):
		"""Sets the explode direction (manipulator index and entity) for this explode step."""
		return self._instance.SetExplodeDirection

	@set_explode_direction.setter
	def set_explode_direction(self, value):
		"""Sets the explode direction (manipulator index and entity) for this explode step."""
		self._instance.SetExplodeDirection = value

