# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommentFolder_members.html
class ICommentFolder:
	def __init__(self, parent=None):
		self._instance = parent

	def add_comment(self, text):
		"""
		Adds a comment to this folder.
		:param text: Comment to add to this folder
		"""
		# return self._instance.AddComment(text)
		raise NotImplemented

	def get_comment_count(self):
		"""Gets the number of comments in this folder."""
		# return self._instance.GetCommentCount
		raise NotImplemented

	def get_comments(self):
		"""Gets all of the comments in this folder."""
		# return self._instance.GetComments
		raise NotImplemented

	def get_feature(self):
		"""Gets the feature for this folder."""
		# return self._instance.GetFeature
		raise NotImplemented

	def i_get_comments(self, count):
		"""
		Gets all of the comments in this folder.
		:param count: Number of comments in the folder
		"""
		# return self._instance.IGetComments(count)
		raise NotImplemented

