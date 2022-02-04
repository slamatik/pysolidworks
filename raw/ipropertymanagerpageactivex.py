# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX_members.html
class IPropertyManagerPageActiveX:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def height(self):
		"""Gets or sets the height of this ActiveX control."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of this ActiveX control."""
		self._instance.Height = value

	@property
	def get_control(self):
		"""Gets the interface to this ActiveX control."""
		return self._instance.GetControl

	@get_control.setter
	def get_control(self, value):
		"""Gets the interface to this ActiveX control."""
		self._instance.GetControl = value

	@property
	def i_get_control(self):
		"""Gets the interface to this ActiveX control."""
		return self._instance.IGetControl

	@i_get_control.setter
	def i_get_control(self, value):
		"""Gets the interface to this ActiveX control."""
		self._instance.IGetControl = value

	@property
	def set_class(self):
		"""Sets the interface to this ActiveX control."""
		return self._instance.SetClass

	@set_class.setter
	def set_class(self, value):
		"""Sets the interface to this ActiveX control."""
		self._instance.SetClass = value

