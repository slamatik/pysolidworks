# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceParameterizationData_members.html
class ISurfaceParameterizationData:
	def __init__(self, parent=None):
		self._instance = parent

	def u_max(self):
		"""Gets the highest value in the U parameter range."""
		# return self._instance.UMax
		raise NotImplemented

	def u_max_bound_type(self):
		"""Gets the behavior at the end of the U range."""
		# return self._instance.UMaxBoundType
		raise NotImplemented

	def u_min(self):
		"""Gets the lowest value in the U parameter range."""
		# return self._instance.UMin
		raise NotImplemented

	def u_min_bound_type(self):
		"""Gets the behavior at the start of the U range."""
		# return self._instance.UMinBoundType
		raise NotImplemented

	def u_properties(self):
		"""Gets the U parameterization properties."""
		# return self._instance.UProperties
		raise NotImplemented

	def u_property_number(self):
		"""Gets the number of U properties."""
		# return self._instance.UPropertyNumber
		raise NotImplemented

	def v_max(self):
		"""Gets the highest value in the V parameter range."""
		# return self._instance.VMax
		raise NotImplemented

	def v_max_bound_type(self):
		"""Gets the behavior at the end of the V range."""
		# return self._instance.VMaxBoundType
		raise NotImplemented

	def v_min(self):
		"""Gets the lowest value in the V parameter range."""
		# return self._instance.VMin
		raise NotImplemented

	def v_min_bound_type(self):
		"""Gets the behavior at the start of the V range."""
		# return self._instance.VMinBoundType
		raise NotImplemented

	def v_properties(self):
		"""Gets the V parameterization properties."""
		# return self._instance.VProperties
		raise NotImplemented

	def v_property_number(self):
		"""Gets the number of V properties."""
		# return self._instance.VPropertyNumber
		raise NotImplemented

