# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions_members.html
class ISaveTo3DExperienceOptions:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def file_name(self):
		"""Gets or sets the specified file name when saving a document in SOLIDWORKS Connected."""
		return self._instance.FileName

	@file_name.setter
	def file_name(self, value):
		"""Gets or sets the specified file name when saving a document in SOLIDWORKS Connected."""
		self._instance.FileName = value

	@property
	def set_revision_comments(self):
		"""Sets the specified revision comments when saving a document in SOLIDWORKS Connected."""
		return self._instance.SetRevisionComments

	@set_revision_comments.setter
	def set_revision_comments(self, value):
		"""Sets the specified revision comments when saving a document in SOLIDWORKS Connected."""
		self._instance.SetRevisionComments = value

