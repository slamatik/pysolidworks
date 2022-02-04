# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.html
class IPMIGtolFrameDatum:
	def __init__(self, parent=None):
		self._instance = parent

	def datum(self):
		"""Gets the Gtol frame datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Datum
		raise NotImplemented

	def datum_linked(self):
		"""Gets the first linked datum of this Gtol frame datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DatumLinked1
		raise NotImplemented

	def datum_linked(self):
		"""Gets the second linked datum of this Gtol frame datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DatumLinked2
		raise NotImplemented

	def datum_linked_modifier(self):
		"""Gets the modifier of the first linked datum of this Gtol frame datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DatumLinkedModifier1
		raise NotImplemented

	def datum_linked_modifier(self):
		"""Gets the modifier of the second linked datum of this Gtol frame datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DatumLinkedModifier2
		raise NotImplemented

	def datum_linked_modifier_value(self):
		"""Gets the value of the modifier of the first linked datum of this Gtol frame datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DatumLinkedModifierValue1
		raise NotImplemented

	def datum_linked_modifier_value(self):
		"""Gets the value of the modifier of the second linked datum of this Gtol frame datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DatumLinkedModifierValue2
		raise NotImplemented

	def datum_modifier(self):
		"""Gets the material modifier of this Gtol frame datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DatumModifier
		raise NotImplemented

	def datum_modifier_value(self):
		"""Gets the value of the material modifier of this Gtol frame datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DatumModifierValue
		raise NotImplemented

