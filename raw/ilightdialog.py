# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog_members.html
class ILightDialog:
	def __init__(self, parent=None):
		self._instance = parent

	def add_sub_dialog(self, page):
		"""
		Adds a sub-dialog to the lighting dialog.
		:param page: Pointer to a CDialog object cast to a long
		"""
		# return self._instance.AddSubDialog(page)
		raise NotImplemented

	def get_light_id(self):
		"""Gets the ID of the edited light in the light dialog."""
		# return self._instance.GetLightId
		raise NotImplemented

