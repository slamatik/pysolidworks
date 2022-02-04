# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton_members.html
class IPropertyManagerPageButton:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def caption(self):
		"""Gets or sets the caption for this button."""
		return self._instance.Caption

	@caption.setter
	def caption(self, value):
		"""Gets or sets the caption for this button."""
		self._instance.Caption = value

