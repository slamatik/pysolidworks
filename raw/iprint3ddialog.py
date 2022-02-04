# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrint3DDialog_members.html
class IPrint3DDialog:
	def __init__(self, parent=None):
		self._instance = parent

	def update_dialog(self):
		"""Updates the build statistics on the Print 3D dialog for a local 3D printer."""
		# return self._instance.UpdateDialog
		raise NotImplemented

