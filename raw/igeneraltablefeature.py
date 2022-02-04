# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature_members.html
class IGeneralTableFeature:
	def __init__(self, parent=None):
		self._instance = parent

	def get_feature(self):
		"""Gets the general table feature."""
		# return self._instance.GetFeature
		raise NotImplemented

	def get_table_annotation_count(self):
		"""Gets the number of table annotations for this general table feature."""
		# return self._instance.GetTableAnnotationCount
		raise NotImplemented

	def get_table_annotations(self):
		"""Gets the table annotations for this general table feature."""
		# return self._instance.GetTableAnnotations
		raise NotImplemented

	def i_get_table_annotations(self, count):
		"""
		Gets the table annotations for this general table feature.
		:param count: Number of table annotations
		"""
		# return self._instance.IGetTableAnnotations(count)
		raise NotImplemented

