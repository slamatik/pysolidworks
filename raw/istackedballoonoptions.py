# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.html
class IStackedBalloonOptions:
	def __init__(self, parent=None):
		self._instance = parent

	def balloons_per_line(self):
		"""Gets and sets the number of stacked balloons per line."""
		# return self._instance.BalloonsPerLine
		raise NotImplemented

	def custom_size(self):
		"""Gets and sets the user-defined size of the balloons."""
		# return self._instance.CustomSize
		raise NotImplemented

	def item_number_increment(self):
		"""Gets and sets the item number increment."""
		# return self._instance.ItemNumberIncrement
		raise NotImplemented

	def item_number_start(self):
		"""Gets and sets the starting item number."""
		# return self._instance.ItemNumberStart
		raise NotImplemented

	def item_order(self):
		"""Gets and sets item ordering."""
		# return self._instance.ItemOrder
		raise NotImplemented

	def layername(self):
		"""Gets and sets the name of the layer on which to create the balloon stack."""
		# return self._instance.Layername
		raise NotImplemented

	def lower_text(self):
		"""Gets and sets the lower text of the balloons."""
		# return self._instance.LowerText
		raise NotImplemented

	def lower_text_content(self):
		"""Gets and sets the style of the lower text of the balloons."""
		# return self._instance.LowerTextContent
		raise NotImplemented

	def quantity_denotation_text(self):
		"""Gets and sets the label of BOM item quantities."""
		# return self._instance.QuantityDenotationText
		raise NotImplemented

	def quantity_override(self):
		"""Gets and sets whether to override the BOM item quantities."""
		# return self._instance.QuantityOverride
		raise NotImplemented

	def quantity_override_value(self):
		"""Gets and sets the override value for BOM item quantities."""
		# return self._instance.QuantityOverrideValue
		raise NotImplemented

	def quantity_placement(self):
		"""Gets and sets the placement of a BOM item quantity with respect to its balloon."""
		# return self._instance.QuantityPlacement
		raise NotImplemented

	def show_quantity(self):
		"""Gets and sets whether to display the BOM item quantities."""
		# return self._instance.ShowQuantity
		raise NotImplemented

	def size(self):
		"""Gets and sets the size of the balloons."""
		# return self._instance.Size
		raise NotImplemented

	def stack_direction(self):
		"""Gets and sets the direction in which to stack balloons."""
		# return self._instance.StackDirection
		raise NotImplemented

	def style(self):
		"""Gets and sets the style of the balloons."""
		# return self._instance.Style
		raise NotImplemented

	def upper_text(self):
		"""Gets and sets the upper text of the balloons."""
		# return self._instance.UpperText
		raise NotImplemented

	def upper_text_content(self):
		"""Gets and sets the style of the upper text of the balloons."""
		# return self._instance.UpperTextContent
		raise NotImplemented

