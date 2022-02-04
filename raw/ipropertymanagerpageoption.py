# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageOption_members.html
class IPropertyManagerPageOption:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def caption(self):
		"""Gets or sets the caption for this option."""
		return self._instance.Caption

	@caption.setter
	def caption(self, value):
		"""Gets or sets the caption for this option."""
		self._instance.Caption = value

	@property
	def checked(self):
		"""gets or sets whether the option is selected."""
		return self._instance.Checked

	@checked.setter
	def checked(self, value):
		"""gets or sets whether the option is selected."""
		self._instance.Checked = value

	@property
	def style(self):
		"""Gets or sets style-related properties for an option on a PropertyManager page."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets style-related properties for an option on a PropertyManager page."""
		self._instance.Style = value

