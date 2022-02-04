# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionGroup_members.html
class ICollisionDetectionGroup:
	def __init__(self, parent=None):
		self._instance = parent

	def apply_transforms(self, component_transforms):
		"""
		Applies the specified transforms to the components in this collision detection group.
		:param component_transforms: Array of IMathTransform
		"""
		# return self._instance.ApplyTransforms(component_transforms)
		raise NotImplemented

	def get_component_count(self):
		"""Gets the number of components in this collision detection group."""
		# return self._instance.GetComponentCount
		raise NotImplemented

	def get_components(self):
		"""Gets the components in this collision detection group."""
		# return self._instance.GetComponents
		raise NotImplemented

	def get_transforms(self):
		"""Gets the current transforms of the components in this collision detection group."""
		# return self._instance.GetTransforms
		raise NotImplemented

	def remove_all_transforms(self):
		"""Removes all collision detection transforms from all components in this collision detection group and restores the original transforms."""
		# return self._instance.RemoveAllTransforms
		raise NotImplemented

	def set_components(self, components):
		"""
		Sets the specified components in this collision detection group.
		:param components: Array of IComponent2
		"""
		# return self._instance.SetComponents(components)
		raise NotImplemented

