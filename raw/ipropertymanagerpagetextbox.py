# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTextbox_members.html
class IPropertyManagerPageTextbox:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def height(self):
		"""Gets or sets the height of this PropertyManager text box."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of this PropertyManager text box."""
		self._instance.Height = value

	@property
	def style(self):
		"""Gets or sets various style-related properties for this text box."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets various style-related properties for this text box."""
		self._instance.Style = value

	@property
	def text(self):
		"""Gets and sets the text that appears in the text box."""
		return self._instance.Text

	@text.setter
	def text(self, value):
		"""Gets and sets the text that appears in the text box."""
		self._instance.Text = value

