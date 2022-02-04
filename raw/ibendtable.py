# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendTable_members.html
class IBendTable:
	def __init__(self, parent=None):
		self._instance = parent

	def starting_value(self):
		"""Gets and sets the starting datum tag for this bend table."""
		# return self._instance.StartingValue
		raise NotImplemented

	def tag_style(self):
		"""Gets and sets the tag style for this bend table."""
		# return self._instance.TagStyle
		raise NotImplemented

	def get_feature(self):
		"""Gets the feature for this bend table."""
		# return self._instance.GetFeature
		raise NotImplemented

	def get_table_annotation_count(self):
		"""Gets the number of bend table annotations."""
		# return self._instance.GetTableAnnotationCount
		raise NotImplemented

	def get_table_annotations(self):
		"""Gets the annotations for this bend table."""
		# return self._instance.GetTableAnnotations
		raise NotImplemented

	def i_get_table_annotations(self, count):
		"""
		Gets the annotations for this bend table.
		:param count: Number of bend table annotations
		"""
		# return self._instance.IGetTableAnnotations(count)
		raise NotImplemented

