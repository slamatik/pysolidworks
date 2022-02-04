# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumComponents2_members.html
class IEnumComponents2:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the components enumeration.
		:param ppenum: Pointer to the cloned components enumeraton
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next component in the components enumeration.
		:param celt: Number of components for the components enumeration
		:param rgelt: Pointer to an array components of size Celt
		:param pcelt_fetched: Pointer to the number of components returned from the list.; this value can be less than Celt if you ask for more components than exist, or it can be NULL if no more components exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the components enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of components in the components enumeration.
		:param celt: Number of components to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

