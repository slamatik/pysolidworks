# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumEdges_members.html
class IEnumEdges:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the edges enumeration.
		:param ppenum: Pointer to the clones edges enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next edge in the edges enumeration.
		:param celt: Number edges for the edges enumeration
		:param rgelt: Pointer to an array of edges of size Celt
		:param pcelt_fetched: Pointer to the number of edges returned from the list; this value can be less than Celt if you ask for more edges than exist, or it can be NULL if no more edges exist.
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the edges enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number edges in the edges enumeration.
		:param celt: Number of edges to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

