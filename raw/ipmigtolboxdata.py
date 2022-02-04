# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.html
class IPMIGtolBoxData:
	def __init__(self, parent=None):
		self._instance = parent

	def material_modifier(self):
		"""Gets the material condition for this PMI Gtol frame box.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.MaterialModifier
		raise NotImplemented

	def tolerance_per_unit_type(self):
		"""Gets the tolerance per unit area type in this PMI Gtol frame box.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.TolerancePerUnitType
		raise NotImplemented

	def tolerance_per_unit_value(self):
		"""Gets the tolerance 1 per unit area value in this PMI Gtol frame box.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.TolerancePerUnitValue1
		raise NotImplemented

	def tolerance_per_unit_value(self):
		"""Gets the tolerance 2 per unit area in this PMI Gtol frame box.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.TolerancePerUnitValue2
		raise NotImplemented

	def tolerance_zone_modifier(self):
		"""Gets the tolerance zone modifier in this PMI Gtol frame box.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.ToleranceZoneModifier
		raise NotImplemented

	def tol_value(self):
		"""Gets the tolerance value in this PMI Gtol frame box.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.TolValue
		raise NotImplemented

	def unit(self):
		"""Gets the units of tolerance for this PMI Gtol frame box.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Unit
		raise NotImplemented

	def get_additional_symbols(self):
		"""Gets additional material conditions in this PMI Gtol frame box."""
		# return self._instance.GetAdditionalSymbols
		raise NotImplemented

	def get_tol_types(self):
		"""Gets the tolerance zone types in this PMI Gtol frame box."""
		# return self._instance.GetTolTypes
		raise NotImplemented

	def get_tol_type_values(self):
		"""Gets the tolerance zone values in this PMI Gtol frame box."""
		# return self._instance.GetTolTypeValues
		raise NotImplemented

