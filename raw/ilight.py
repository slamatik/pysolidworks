# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILight_members.html
class ILight:
	def __init__(self, parent=None):
		self._instance = parent

	def get_i_d(self):
		"""Gets the light ID for this light feature."""
		# return self._instance.GetID
		raise NotImplemented

