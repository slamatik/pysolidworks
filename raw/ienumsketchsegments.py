# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchSegments_members.html
class IEnumSketchSegments:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the sketch segments enumeration.
		:param ppenum: Pointer to the cloned sketch segments enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next sketch segment in the sketch segments enumeration.
		:param celt: Number of sketch segments for the sketch segments enumeration
		:param rgelt: Pointer to an array of sketch segments of size Celt
		:param pcelt_fetched: Pointer to the number of sketch segments returned from the list;  this value can be less than celt if you ask for more sketch segments than exist, or it can be NULL if no more sketch segments exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the sketch segments enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of sketch segments in the sketch segments enumeration.
		:param celt: Number of sketch segments to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

