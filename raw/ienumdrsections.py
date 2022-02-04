# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDrSections_members.html
class IEnumDrSections:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the section views enumeration.
		:param ppenum: Pointer to the cloned section views enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next section view in the section views enumeration.
		:param celt: Number of section views for the section views enumeration
		:param rgelt: Pointer to an array of section views of size Celt
		:param pcelt_fetched: Pointer to the number of drawing sections returned from the list; this value can be less than Celt if you ask for more drawing sections than exist, or it can be NULL if no more drawing sections exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the section views enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of section views in the section views enumeration.
		:param celt: Number of section views to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

