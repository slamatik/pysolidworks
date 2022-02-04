# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleDataTable_members.html
class IHoleDataTable:
	def __init__(self, parent=None):
		self._instance = parent

	def fastener_i_d(self):
		"""Gets the ID of the fastener associated with this Hole Wizard fastener table."""
		# return self._instance.FastenerID
		raise NotImplemented

	def standard_name(self):
		"""Gets the name of the Hole Wizard standard associated with this Hole Wizard fastener table."""
		# return self._instance.StandardName
		raise NotImplemented

	def table_type_i_d(self):
		"""Gets the fastener table type ID associated with this Hole Wizard fastener table."""
		# return self._instance.TableTypeID
		raise NotImplemented

	def get_cell_data(self, column_name, row_index, cell_data):
		"""
		Gets data from the specified table cell of this Hole Wizard fastener table.
		:param column_name: Column name (see Remarks)
		:param row_index: 0-based row index
		:param cell_data: Cell data
		"""
		# return self._instance.GetCellData(column_name, row_index, cell_data)
		raise NotImplemented

	def get_column_names(self, column_names):
		"""
		Gets the names of all the columns in this Hole Wizard fastener table.
		:param column_names: Array of column names
		"""
		# return self._instance.GetColumnNames(column_names)
		raise NotImplemented

	def get_row_count(self, row_count):
		"""
		Gets the number of rows in this Hole Wizard fastener table.
		:param row_count: Number of rows
		"""
		# return self._instance.GetRowCount(row_count)
		raise NotImplemented

	def get_row_data(self, row_index, row_data):
		"""
		Gets data for the specified row of this Hole Wizard fastener table.
		:param row_index: 0-based index of row
		:param row_data: Row data
		"""
		# return self._instance.GetRowData(row_index, row_data)
		raise NotImplemented

