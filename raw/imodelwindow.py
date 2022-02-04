# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelWindow_members.html
class IModelWindow:
	def __init__(self, parent=None):
		self._instance = parent

	def h_wnd(self):
		"""Gets the handle to this model window."""
		# return self._instance.HWnd
		raise NotImplemented

	def h_wndx(self):
		"""Gets the handle to this model window in 64-bit applications."""
		# return self._instance.HWndx64
		raise NotImplemented

	def model_doc(self):
		"""Gets the model document in this model window."""
		# return self._instance.ModelDoc
		raise NotImplemented

	def title(self):
		"""Gets the title of this model window."""
		# return self._instance.Title
		raise NotImplemented

	def activate(self):
		"""Activates this model window."""
		# return self._instance.Activate
		raise NotImplemented

