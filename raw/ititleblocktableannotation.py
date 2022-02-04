# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableAnnotation_members.html
class ITitleBlockTableAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def title_block_table_feature(self):
		"""Gets the title block table feature associated with this annotation."""
		# return self._instance.TitleBlockTableFeature
		raise NotImplemented

