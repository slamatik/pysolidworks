# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFolder_members.html
class IFlatPatternFolder:
	def __init__(self, parent=None):
		self._instance = parent

	def get_feature(self):
		"""Gets the feature for this flat-pattern folder."""
		# return self._instance.GetFeature
		raise NotImplemented

	def get_flat_pattern_count(self):
		"""Gets the number of flat patterns in this folder."""
		# return self._instance.GetFlatPatternCount
		raise NotImplemented

	def get_flat_patterns(self):
		"""Gets the flat-pattern features in this folder."""
		# return self._instance.GetFlatPatterns
		raise NotImplemented

