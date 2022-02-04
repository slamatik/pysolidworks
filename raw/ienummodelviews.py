# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumModelViews_members.html
class IEnumModelViews:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the model views enumeration.
		:param ppenum: Pointer to the model views enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next model view in the model views enumeration.
		:param celt: Number of model views for the model views enumeration
		:param rgelt: Pointer to an array of model views of size Celt
		:param pcelt_fetched: Pointer to the number of model views returned from the list; this value can be less than celt if you ask for more model views than exist, or it can be NULL if no more model views exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the model views enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of model views in the model views enumeration.
		:param celt: Number of model views to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

