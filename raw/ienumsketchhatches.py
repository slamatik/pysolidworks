# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumSketchHatches_members.html
class IEnumSketchHatches:
	def __init__(self, parent=None):
		self._instance = parent

	def clone(self, ppenum):
		"""
		Clones the sketch hatches enumeration.
		:param ppenum: Pointer to the cloned sketch hatches enumeration
		"""
		# return self._instance.Clone(ppenum)
		raise NotImplemented

	def next(self, celt, rgelt, pcelt_fetched):
		"""
		Gets the next sketch hatch in the sketch hatch enumeration.
		:param celt: Number of sketch hatches for this sketch hatch enumeration
		:param rgelt: Pointer to an array of sketch hatches of size Celt
		:param pcelt_fetched: Pointer to the number of sketch hatches returned from the list; this value can be less than celt if you ask for more SketchHatch objects than exist, or it can be NULL if no more SketchHatch objects exist
		"""
		# return self._instance.Next(celt, rgelt, pcelt_fetched)
		raise NotImplemented

	def reset(self):
		"""Resets the sequence to the beginning of the sketch hatches enumeration."""
		# return self._instance.Reset
		raise NotImplemented

	def skip(self, celt):
		"""
		Skips the specified number of sketch hatches in the sketch hatches enumeration.
		:param celt: Number of sketch hatches to skip
		"""
		# return self._instance.Skip(celt)
		raise NotImplemented

