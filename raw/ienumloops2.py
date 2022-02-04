# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumLoops2_members.html
class IEnumLoops2:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the loops enumeration.
		:param ppenum: Pointer to the clones loops enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next loop in the loops enumeration.
		:param celt: Number of loops for the loops enumeration
		:param rgelt: Pointer to an array of loops of size Celt
		:param pcelt_fetched: Pointer to the number of loops returned from the list; this value can be less than celt if you ask for more loops than exist, or it can be NULL if no more loops exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the loops enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of loops in the loops enumeration.
		:param celt: Number of loops
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

