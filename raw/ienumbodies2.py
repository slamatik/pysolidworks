# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2_members.html
class IEnumBodies2:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones a bodies enumeration.
		:param ppenum: Pointer to the bodies enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next body in the bodies enumeration.
		:param celt: Number of bodies for the bodies enumeration
		:param rgelt: Pointer to an array of bodies of size Celt
		:param pcelt_fetched: Pointer to the number of bodies returned from the list; this value can be less than Celt if you request more bodies than exist, or it can be NULL if no more bodies exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the bodies enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of bodies in the bodies enumeration.
		:param celt: Number of bodies to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

