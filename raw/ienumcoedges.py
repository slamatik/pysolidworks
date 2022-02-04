# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges_members.html
class IEnumCoEdges:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the a coedges enumeration.
		:param ppenum: Pointer to the cloned coedges enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next coedge in the coedges enumeration.
		:param celt: Number of coedges for the coedges enumeration
		:param rgelt: Pointer to an array of coedges of size Celt
		:param pcelt_fetched: Number of coedges returned from the list; this value can be less than Celt if you asked for more coedges than exist, or it can be NULL if no more coedges exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the coedges enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of coedges in the coedges enumeration.
		:param celt: Number of coedges to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

