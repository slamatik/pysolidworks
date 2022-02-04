# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableAnnotation_members.html
class IGeneralToleranceTableAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def general_tolerance_table_feature(self):
		"""Gets the general tolerance table feature for this annotation."""
		# return self._instance.GeneralToleranceTableFeature
		raise NotImplemented

