# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTable_members.html
class IBomTable:
	def __init__(self, parent=None):
		self._instance = parent

	def attach(self):
		"""Activates the BOM."""
		# return self._instance.Attach3
		raise NotImplemented

	def de_select(self):
		"""Deselects this BOM table."""
		# return self._instance.DeSelect
		raise NotImplemented

	def detach(self):
		"""Deactivates the BOM."""
		# return self._instance.Detach
		raise NotImplemented

	def get_column_width(self, col):
		"""
		Gets the specified column width in meters.
		:param col: Column number; this is a 0-based index
		"""
		# return self._instance.GetColumnWidth(col)
		raise NotImplemented

	def get_display_data(self):
		"""Returns the IDisplayData object for this BOM table."""
		# return self._instance.GetDisplayData
		raise NotImplemented

	def get_entry_text(self, row, col):
		"""
		Retrieves the contents of the specified cell as a string regardless of the cell's data type.
		:param row: Row number of the desired cell; this is a 0-based index
		:param col: Column number of the desired cell; this is a 0-based index
		"""
		# return self._instance.GetEntryText(row, col)
		raise NotImplemented

	def get_entry_value(self, row, col):
		"""
		Gets the contents of the specified cell.
		:param row: Row number of the desired cell; this is a 0-based index
		:param col: Column number of the desired cell; this is a 0-based index
		"""
		# return self._instance.GetEntryValue(row, col)
		raise NotImplemented

	def get_extent(self):
		"""Gets the lower-left and upper-right extents of the BOM on the drawing sheet."""
		# return self._instance.GetExtent
		raise NotImplemented

	def get_header_text(self, col):
		"""
		Gets the header text for the specified column.
		:param col: Column number with the desired header text; this is a 0-based index
		"""
		# return self._instance.GetHeaderText(col)
		raise NotImplemented

	def get_row_height(self, row):
		"""
		Gets the specified row height in meters.
		:param row: Row number; this is a 0-based index
		"""
		# return self._instance.GetRowHeight(row)
		raise NotImplemented

	def get_total_column_count(self):
		"""Gets the total number of columns in the BOM table."""
		# return self._instance.GetTotalColumnCount
		raise NotImplemented

	def get_total_row_count(self):
		"""Gets the total number of rows in the BOM table."""
		# return self._instance.GetTotalRowCount
		raise NotImplemented

	def i_get_display_data(self):
		"""Returns the IDisplayData object for this BOM table."""
		# return self._instance.IGetDisplayData
		raise NotImplemented

	def i_get_extent(self):
		"""Gets the lower-left and upper-right extents of the BOM on the drawing sheet."""
		# return self._instance.IGetExtent
		raise NotImplemented

	def is_visible(self):
		"""Gets whether this BOM is visible."""
		# return self._instance.IsVisible
		raise NotImplemented

	def select(self, append, mark):
		"""
		Selects this BOM table and marks it.
		:param append: True appends the selection list, false replaces the selection list
		:param mark: Value you want to use as a mark
		"""
		# return self._instance.Select(append, mark)
		raise NotImplemented

