# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDisplayDimensions_members.html
class IEnumDisplayDimensions:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the display dimensions enumeration.
		:param ppenum: Pointer to the cloned display dimensions enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next display dimension in the display dimensions enumeration.
		:param celt: Number of display dimensions for the display dimension enumeration
		:param rgelt: Pointer to an array of display dimensions in of size Celt
		:param pcelt_fetched: Pointer to the number of display dimensions from the list; this value can be less than Celt if you ask for more display dimensions than exist, or it can be
NULL if no more display dimensions exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the display dimensions enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of display dimensions in the display dimensions enumeration.
		:param celt: Number of display dimensions to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

