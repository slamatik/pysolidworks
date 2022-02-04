# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchPoints_members.html
class IEnumSketchPoints:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the sketch points enumeration.
		:param ppenum: Pointer to the cloned sketch points enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next sketch point in the sketch points enumeration.
		:param celt: Number of sketch points for the sketch points enumeration
		:param rgelt: Pointer to an array of sketch points of size Celt
		:param pcelt_fetched: Pointer to the number of sketch points returned from the list; this value can be less than celt if you ask for more sketch points than exist, or it can be NULL if no more sketch points exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the sketch points enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of sketch points in the sketch points enumeration.
		:param celt: Number of sketch points to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

