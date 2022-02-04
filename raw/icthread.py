# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.html
class ICThread:
	def __init__(self, parent=None):
		self._instance = parent

	def patterned_transforms(self):
		"""Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature."""
		# return self._instance.PatternedTransforms
		raise NotImplemented

	def thread_callout(self):
		"""Gets the note for this cosmetic thread callout in a drawing."""
		# return self._instance.ThreadCallout
		raise NotImplemented

	def get_annotation(self):
		"""Gets the annotation for this cosmetic thread."""
		# return self._instance.GetAnnotation
		raise NotImplemented

	def get_display_data(self):
		"""Gets the display data for this cosmetic thread."""
		# return self._instance.GetDisplayData
		raise NotImplemented

	def get_next(self):
		"""Gets the next cosmetic thread."""
		# return self._instance.GetNext
		raise NotImplemented

	def get_patterned_transforms_count(self):
		"""Gets the number of instances of this cosmetic thread that are patterns of this feature."""
		# return self._instance.GetPatternedTransformsCount
		raise NotImplemented

	def i_get_annotation(self):
		"""Gets the annotation for this cosmetic thread."""
		# return self._instance.IGetAnnotation
		raise NotImplemented

	def i_get_display_data(self):
		"""Gets the display data for this cosmetic thread."""
		# return self._instance.IGetDisplayData
		raise NotImplemented

	def i_get_next(self):
		"""Gets the next cosmetic thread."""
		# return self._instance.IGetNext
		raise NotImplemented

	def i_get_patterned_transforms(self, count):
		"""
		Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature.
		:param count: Size of the output array (see Remarks)
		"""
		# return self._instance.IGetPatternedTransforms(count)
		raise NotImplemented

