# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget_members.html
class IPMIDatumTarget:
	def __init__(self, parent=None):
		self._instance = parent

	def area_style(self):
		"""Gets the area style of this PMI datum target.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.AreaStyle
		raise NotImplemented

	def diameter(self):
		"""Gets the PMI datum target diameter.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Diameter
		raise NotImplemented

	def height(self):
		"""Gets the PMI datum target height.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Height
		raise NotImplemented

	def movable_style(self):
		"""Gets the movable style of this PMI datum target.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.MovableStyle
		raise NotImplemented

	def symbol_style(self):
		"""Gets the symbol style of this PMI datum target.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.SymbolStyle
		raise NotImplemented

	def unit(self):
		"""Gets the units for the values of this PMI datum target.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Unit
		raise NotImplemented

	def width(self):
		"""Gets the PMI datum target width.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Width
		raise NotImplemented

	def get_datum_target_references(self):
		"""Gets the datum references for this PMI datum target."""
		# return self._instance.GetDatumTargetReferences
		raise NotImplemented

