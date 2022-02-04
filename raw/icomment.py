# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComment_members.html
class IComment:
	def __init__(self, parent=None):
		self._instance = parent

	def feature_owner(self):
		"""Gets the feature that owns this comment."""
		# return self._instance.FeatureOwner
		raise NotImplemented

	@property
	def name(self):
		"""Gets or sets the name of the comment as it appears in the FeatureManager design tree."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the name of the comment as it appears in the FeatureManager design tree."""
		self._instance.Name = value

	@property
	def text(self):
		"""Gets or sets the text for the comment."""
		return self._instance.Text

	@text.setter
	def text(self, value):
		"""Gets or sets the text for the comment."""
		self._instance.Text = value

	@property
	def delete(self):
		"""Deletes a comment."""
		return self._instance.Delete

	@delete.setter
	def delete(self, value):
		"""Deletes a comment."""
		self._instance.Delete = value

