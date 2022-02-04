# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatMgrView_members.html
class IFeatMgrView:
	def __init__(self, parent=None):
		self._instance = parent

	def activate_view(self):
		"""Activates this view in the FeatureManager design tree."""
		# return self._instance.ActivateView
		raise NotImplemented

	def de_activate_view(self):
		"""Deactivates this view in the FeatureManager design tree."""
		# return self._instance.DeActivateView
		raise NotImplemented

	def delete_view(self):
		"""Removes this view from the FeatureManager design tree."""
		# return self._instance.DeleteView
		raise NotImplemented

	def get_control(self):
		"""Gets the control associated with this FeatureManager design tree view."""
		# return self._instance.GetControl
		raise NotImplemented

	def get_feat_mgr_view_wnd(self):
		"""Gets the FeatureManager design tree view window handle as a CWnd object."""
		# return self._instance.GetFeatMgrViewWnd
		raise NotImplemented

	def get_feat_mgr_view_wndx(self):
		"""Gets the FeatureManager design tree view window handle as a CWnd object in 64-bit applications."""
		# return self._instance.GetFeatMgrViewWndx64
		raise NotImplemented

	def i_get_control(self):
		"""Gets the control associated with this FeatureManager design tree view."""
		# return self._instance.IGetControl
		raise NotImplemented

