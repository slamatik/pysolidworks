# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html
class IColorTable:
	def __init__(self, parent=None):
		self._instance = parent

	def get_basic_color_count(self):
		"""Gets the number of basic colors defined in the color table."""
		# return self._instance.GetBasicColorCount
		raise NotImplemented

	def get_basic_colors(self):
		"""Gets the basic colors in the color table."""
		# return self._instance.GetBasicColors
		raise NotImplemented

	def get_color_ref_at_index(self, index):
		"""
		Gets the COLORREF at the specified index position of the color table.
		:param index: Index position of the desired color
		"""
		# return self._instance.GetColorRefAtIndex(index)
		raise NotImplemented

	def get_count(self):
		"""Gets the total number of colors in the color table, including standard and custom colors."""
		# return self._instance.GetCount
		raise NotImplemented

	def get_custom_color_count(self):
		"""Gets the number of custom colors in the color table."""
		# return self._instance.GetCustomColorCount
		raise NotImplemented

	def get_custom_colors(self):
		"""Gets the number of custom colors in the color table."""
		# return self._instance.GetCustomColors
		raise NotImplemented

	def get_name_at_index(self, index):
		"""
		Gets the name of the color at the specified index position in the color table.
		:param index: Index position of the desired color
		"""
		# return self._instance.GetNameAtIndex(index)
		raise NotImplemented

	def get_standard_count(self):
		"""Gets the number of basic or standard colors defined in the color table."""
		# return self._instance.GetStandardCount
		raise NotImplemented

	def i_get_basic_colors(self, color_count):
		"""
		Gets the basic colors in the color table.
		:param color_count: Number of basic colors
		"""
		# return self._instance.IGetBasicColors(color_count)
		raise NotImplemented

	def i_get_custom_colors(self, color_count):
		"""
		Gets the number of custom colors in the color table.
		:param color_count: Number of custom colors
		"""
		# return self._instance.IGetCustomColors(color_count)
		raise NotImplemented

	def set_color_ref_at_index(self, index, color_ref, apply_to):
		"""
		Sets the specified color value within the color table.
		:param index: Index value within the color table you want to modify
		:param color_ref: COLORREF value 
		:param apply_to: Not used; specify 0
		"""
		# return self._instance.SetColorRefAtIndex(index, color_ref, apply_to)
		raise NotImplemented

	def set_custom_color(self, index, color_ref):
		"""
		Sets a custom color.
		:param index: Index of the custom color to set
		:param color_ref: COLORREF value
		"""
		# return self._instance.SetCustomColor(index, color_ref)
		raise NotImplemented

