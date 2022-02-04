# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot_members.html
class ISnapShot:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def comment(self):
		"""Gets or sets the comment on this snapshot."""
		return self._instance.Comment

	@comment.setter
	def comment(self, value):
		"""Gets or sets the comment on this snapshot."""
		self._instance.Comment = value

	@property
	def name(self):
		"""Gets or sets the name of this snapshot."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the name of this snapshot."""
		self._instance.Name = value

	@property
	def view_id(self):
		"""Gets the ID of this snapshot."""
		return self._instance.ViewId

	@view_id.setter
	def view_id(self, value):
		"""Gets the ID of this snapshot."""
		self._instance.ViewId = value

	@property
	def activate(self):
		"""Activates this snapshot."""
		return self._instance.Activate

	@activate.setter
	def activate(self, value):
		"""Activates this snapshot."""
		self._instance.Activate = value

