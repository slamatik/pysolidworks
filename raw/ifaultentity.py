# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity_members.html
class IFaultEntity:
	def __init__(self, parent=None):
		self._instance = parent

	def count(self):
		"""Gets the number of faults that the entity has."""
		# return self._instance.Count
		raise NotImplemented

	def entity(self, index):
		"""
		Gets the specified entity.
		:param index: 0-based index number indicating the entity to get
		"""
		# return self._instance.Entity2(index)
		raise NotImplemented

	def error_code(self, index):
		"""
		Gets the error for the fault for the specified entity.
		:param index: 0-based index number indicating the entity with the fault
		"""
		# return self._instance.ErrorCode(index)
		raise NotImplemented

