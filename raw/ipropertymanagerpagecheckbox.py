# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCheckbox_members.html
class IPropertyManagerPageCheckbox:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def caption(self):
		"""Gets or sets the label for this check box."""
		return self._instance.Caption

	@caption.setter
	def caption(self, value):
		"""Gets or sets the label for this check box."""
		self._instance.Caption = value

	@property
	def checked(self):
		"""Gets or sets this check box as selected."""
		return self._instance.Checked

	@checked.setter
	def checked(self, value):
		"""Gets or sets this check box as selected."""
		self._instance.Checked = value

	@property
	def state(self):
		"""Gets or sets the state of this check box."""
		return self._instance.State

	@state.setter
	def state(self, value):
		"""Gets or sets the state of this check box."""
		self._instance.State = value

