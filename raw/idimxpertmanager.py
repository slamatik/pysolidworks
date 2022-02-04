# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.html
class IDimXpertManager:
	def __init__(self, parent=None):
		self._instance = parent

	def dim_xpert_part(self):
		"""Provides access to the detailed geometric dimensioning and tolerancing information for a part."""
		# return self._instance.DimXpertPart
		raise NotImplemented

	def schema_comment(self):
		"""Gets a comment for the DimXpert schema."""
		# return self._instance.SchemaComment
		raise NotImplemented

	def schema_description(self):
		"""Gets the description of the DimXpert schema."""
		# return self._instance.SchemaDescription
		raise NotImplemented

	def schema_name(self):
		"""Gets the name of the DimXpertSchema."""
		# return self._instance.SchemaName
		raise NotImplemented

	def tree_display(self):
		"""Gets the organization of the DimXpertManager tab information:  by annotation, by features, or flat."""
		# return self._instance.TreeDisplay
		raise NotImplemented

