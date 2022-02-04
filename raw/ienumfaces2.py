# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumFaces2_members.html
class IEnumFaces2:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the faces enumeration.
		:param ppenum: Pointer to the cloned faces enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next face in the faces enumeration.
		:param celt: Number of faces for the faces enumeration
		:param rgelt: Pointer to an array of faces of size Celt
		:param pcelt_fetched: Pointer to the number of faces returned from the list; this value can be less than Celt if you asked for more faces than exist, or it can be NULL if no more faces exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the faces enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of faces in the faces enumeration.
		:param celt: Number of faces to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

