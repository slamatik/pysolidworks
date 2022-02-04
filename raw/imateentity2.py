# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.html
class IMateEntity2:
	def __init__(self, parent=None):
		self._instance = parent

	def entity_params(self):
		"""Gets the parameters for this mate entity."""
		# return self._instance.EntityParams
		raise NotImplemented

	def reference(self):
		"""Gets the mate reference for this mate entity."""
		# return self._instance.Reference
		raise NotImplemented

	def reference_component(self):
		"""Gets the reference component for this mate entity."""
		# return self._instance.ReferenceComponent
		raise NotImplemented

	def reference_type(self):
		"""Gets the mate entity reference type for this mate entity."""
		# return self._instance.ReferenceType2
		raise NotImplemented

	def get_entity_params_size(self):
		"""Gets the number of parameters for this mate entity."""
		# return self._instance.GetEntityParamsSize
		raise NotImplemented

	def i_get_entity_params(self, n_params_size):
		"""
		Gets the parameters of this mate entity.
		:param n_params_size: Number of parameters for this mate entity
		"""
		# return self._instance.IGetEntityParams(n_params_size)
		raise NotImplemented

