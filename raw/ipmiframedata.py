# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData_members.html
class IPMIFrameData:
	def __init__(self, parent=None):
		self._instance = parent

	def frame_number(self):
		"""Gets the index of this Gtol frame.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.FrameNumber
		raise NotImplemented

	def geometric_characteristic(self):
		"""Gets the geometric characteristic of this Gtol frame.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.GeometricCharacteristic
		raise NotImplemented

	def get_gtol_box_at_index(self, index):
		"""
		Gets the specified tolerance box in this Gtol frame.
		:param index: 0 <= Gtol frame box index <= 2
		"""
		# return self._instance.GetGtolBoxAtIndex(index)
		raise NotImplemented

	def get_gtol_box_count(self):
		"""Gets the number of tolerance boxes in this Gtol frame."""
		# return self._instance.GetGtolBoxCount
		raise NotImplemented

	def get_gtol_datum_at_index(self, index):
		"""
		Gets the specified datum box in this Gtol frame.
		:param index: 0 <= Gtol frame datum index <= 2
		"""
		# return self._instance.GetGtolDatumAtIndex(index)
		raise NotImplemented

	def get_gtol_datum_count(self):
		"""Gets the number of datum boxes in this Gtol frame."""
		# return self._instance.GetGtolDatumCount
		raise NotImplemented

