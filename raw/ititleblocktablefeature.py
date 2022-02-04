# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature_members.html
class ITitleBlockTableFeature:
	def __init__(self, parent=None):
		self._instance = parent

	def get_feature(self):
		"""Provides access to the feature associated with this title block table."""
		# return self._instance.GetFeature
		raise NotImplemented

	def get_table_annotation_count(self):
		"""Gets the number of title block table annotations in this title block table feature."""
		# return self._instance.GetTableAnnotationCount
		raise NotImplemented

	def get_table_annotations(self):
		"""Gets all of the title block table annotations in this title block table feature."""
		# return self._instance.GetTableAnnotations
		raise NotImplemented

	def i_get_table_annotations(self, count):
		"""
		Gets all of the title block table annotations in this title block table feature.
		:param count: Number of annotations in this title block feature
		"""
		# return self._instance.IGetTableAnnotations(count)
		raise NotImplemented

