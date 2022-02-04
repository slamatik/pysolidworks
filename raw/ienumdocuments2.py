# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumDocuments2_members.html
class IEnumDocuments2:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the documents enumeration.
		:param ppenum: Pointer to the cloned documents enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next document in the documents enumeration.
		:param celt: Number of documents for the documents enumeration
		:param rgelt: Pointer to an array of documents of size Celt
		:param pcelt_fetched: Pointer to the number of documents returned from the list; this value can be less than Celt if you ask for more documents than exist, or it can be NULL if no more documents exist.
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the documents enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of documents in the documents enumeration.
		:param celt: Number of documents to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

