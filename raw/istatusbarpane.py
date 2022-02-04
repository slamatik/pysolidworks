# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStatusBarPane_members.html
class IStatusBarPane:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def text(self):
		"""Gets or sets the text for this pane."""
		return self._instance.Text

	@text.setter
	def text(self, value):
		"""Gets or sets the text for this pane."""
		self._instance.Text = value

	@property
	def visible(self):
		"""Shows or hides this pane."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Shows or hides this pane."""
		self._instance.Visible = value

