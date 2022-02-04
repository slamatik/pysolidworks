# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature_members.html
class IGeneralToleranceTableFeature:
	def __init__(self, parent=None):
		self._instance = parent

	def get_feature(self):
		"""Gets the general tolerance table feature."""
		# return self._instance.GetFeature
		raise NotImplemented

	def get_table_annotations(self):
		"""Gets the table annotations for this general tolerance table feature."""
		# return self._instance.GetTableAnnotations
		raise NotImplemented

