# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumData_members.html
class IPMIDatumData:
	def __init__(self, parent=None):
		self._instance = parent

	def get_datum_feature(self):
		"""Gets the PMI datum feature."""
		# return self._instance.GetDatumFeature
		raise NotImplemented

	def get_datum_target(self):
		"""Gets the PMI datum target."""
		# return self._instance.GetDatumTarget
		raise NotImplemented

	def get_datum_type(self):
		"""Gets the PMI datum type."""
		# return self._instance.GetDatumType
		raise NotImplemented

