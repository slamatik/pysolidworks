# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html
class IPMIDimensionItem:
	def __init__(self, parent=None):
		self._instance = parent

	def additional_symbol(self):
		"""Gets the tolerance zone modifier for this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.AdditionalSymbol
		raise NotImplemented

	def callout_text(self):
		"""Gets the callout value for this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.CalloutText
		raise NotImplemented

	def instance_count(self):
		"""Gets the instance count of this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.InstanceCount
		raise NotImplemented

	def max_variation(self):
		"""Gets the maximum variation of tolerance for this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.MaxVariation
		raise NotImplemented

	def min_variation(self):
		"""Gets the minimum variation of tolerance for this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.MinVariation
		raise NotImplemented

	def prefix(self):
		"""Gets the prefix of this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Prefix
		raise NotImplemented

	def suffix(self):
		"""Gets the suffix of this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Suffix
		raise NotImplemented

	def symbol(self):
		"""Gets the dimension symbols for this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Symbol
		raise NotImplemented

	def tolerance_precision(self):
		"""Gets the tolerance precision of this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.TolerancePrecision
		raise NotImplemented

	def tol_type(self):
		"""Gets the tolerance type of this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.TolType
		raise NotImplemented

	def unit(self):
		"""Gets the units of this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Unit
		raise NotImplemented

	def value(self):
		"""Gets the primary value of this PMI dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Value
		raise NotImplemented

	def value_precision(self):
		"""Gets the value precision of this dimension item.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.ValuePrecision
		raise NotImplemented

	def is_reference_only(self):
		"""Gets whether this PMI dimension is reference only.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.IsReferenceOnly
		raise NotImplemented

