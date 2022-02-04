# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageWindowFromHandle_members.html
class IPropertyManagerPageWindowFromHandle:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def height(self):
		"""Gets or sets the height of this .NET control."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of this .NET control."""
		self._instance.Height = value

	@property
	def set_window_handle(self):
		"""Sets the handle of this .NET control."""
		return self._instance.SetWindowHandle

	@set_window_handle.setter
	def set_window_handle(self, value):
		"""Sets the handle of this .NET control."""
		self._instance.SetWindowHandle = value

	@property
	def set_window_handlex(self):
		"""Sets the handle of this .NET control on 64-bit machines."""
		return self._instance.SetWindowHandlex64

	@set_window_handlex.setter
	def set_window_handlex(self, value):
		"""Sets the handle of this .NET control on 64-bit machines."""
		self._instance.SetWindowHandlex64 = value

