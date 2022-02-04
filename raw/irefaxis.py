# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis_members.html
class IRefAxis:
	def __init__(self, parent=None):
		self._instance = parent

	def get_ref_axis_params(self):
		"""Gets information for a reference axis."""
		# return self._instance.GetRefAxisParams
		raise NotImplemented

	def get_temp_axis_reference_face(self):
		"""Gets the reference face for this temporary axis."""
		# return self._instance.GetTempAxisReferenceFace
		raise NotImplemented

	def i_get_ref_axis_params(self):
		"""Gets information for a reference axis."""
		# return self._instance.IGetRefAxisParams
		raise NotImplemented

	def is_temp_axis(self):
		"""Gets whether the reference axis is a temporary axis."""
		# return self._instance.IsTempAxis
		raise NotImplemented

