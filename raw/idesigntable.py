# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDesignTable_members.html
class IDesignTable:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_add_new_configs(self):
		"""Gets or sets whether to automatically add rows or columns to the design table when new configurations are added to the model."""
		return self._instance.AutoAddNewConfigs

	@auto_add_new_configs.setter
	def auto_add_new_configs(self, value):
		"""Gets or sets whether to automatically add rows or columns to the design table when new configurations are added to the model."""
		self._instance.AutoAddNewConfigs = value

	@property
	def auto_add_new_params(self):
		"""Gets or sets whether or not to automatically add rows or columns to the design table when new parameters are added to the model."""
		return self._instance.AutoAddNewParams

	@auto_add_new_params.setter
	def auto_add_new_params(self, value):
		"""Gets or sets whether or not to automatically add rows or columns to the design table when new parameters are added to the model."""
		self._instance.AutoAddNewParams = value

	@property
	def column_hidden(self):
		"""Gets the visibility state of the specified column."""
		return self._instance.ColumnHidden

	@column_hidden.setter
	def column_hidden(self, value):
		"""Gets the visibility state of the specified column."""
		self._instance.ColumnHidden = value

	@property
	def enable_cell_dropdown_lists(self):
		"""Gets or sets whether to enable cell drop-down lists in the design table."""
		return self._instance.EnableCellDropdownLists

	@enable_cell_dropdown_lists.setter
	def enable_cell_dropdown_lists(self, value):
		"""Gets or sets whether to enable cell drop-down lists in the design table."""
		self._instance.EnableCellDropdownLists = value

	@property
	def file_name(self):
		"""Gets or sets the Microsoft Excel file for this design table."""
		return self._instance.FileName

	@file_name.setter
	def file_name(self, value):
		"""Gets or sets the Microsoft Excel file for this design table."""
		self._instance.FileName = value

	@property
	def last_error(self):
		"""Gets or sets the last error that occurred in this design table."""
		return self._instance.LastError

	@last_error.setter
	def last_error(self, value):
		"""Gets or sets the last error that occurred in this design table."""
		self._instance.LastError = value

	@property
	def link_to_file(self):
		"""Gets or sets whether to link the design table to the model."""
		return self._instance.LinkToFile

	@link_to_file.setter
	def link_to_file(self, value):
		"""Gets or sets whether to link the design table to the model."""
		self._instance.LinkToFile = value

	@property
	def row_hidden(self):
		"""Gets the visibility state of the specified row."""
		return self._instance.RowHidden

	@row_hidden.setter
	def row_hidden(self, value):
		"""Gets the visibility state of the specified row."""
		self._instance.RowHidden = value

	@property
	def source_type(self):
		"""Gets or sets the type of source file for this design table."""
		return self._instance.SourceType

	@source_type.setter
	def source_type(self, value):
		"""Gets or sets the type of source file for this design table."""
		self._instance.SourceType = value

	@property
	def updatable(self):
		"""Gets or sets whether edits to the model update the design table."""
		return self._instance.Updatable

	@updatable.setter
	def updatable(self, value):
		"""Gets or sets whether edits to the model update the design table."""
		self._instance.Updatable = value

	@property
	def warn(self):
		"""Gets or sets whether to display a warning when invalid information is encountered in the design table when updating the design table."""
		return self._instance.Warn

	@warn.setter
	def warn(self, value):
		"""Gets or sets whether to display a warning when invalid information is encountered in the design table when updating the design table."""
		self._instance.Warn = value

	@property
	def worksheet(self):
		"""Gets the Microsoft Excel worksheet for this design table."""
		return self._instance.Worksheet

	@worksheet.setter
	def worksheet(self, value):
		"""Gets the Microsoft Excel worksheet for this design table."""
		self._instance.Worksheet = value

	@property
	def add_row(self):
		"""Adds a row to the design table."""
		return self._instance.AddRow

	@add_row.setter
	def add_row(self, value):
		"""Adds a row to the design table."""
		self._instance.AddRow = value

	@property
	def attach(self):
		"""Activates the design table within the part or assembly document."""
		return self._instance.Attach

	@attach.setter
	def attach(self, value):
		"""Activates the design table within the part or assembly document."""
		self._instance.Attach = value

	@property
	def detach(self):
		"""Detaches the design table from the Microsoft Excel sheet."""
		return self._instance.Detach

	@detach.setter
	def detach(self, value):
		"""Detaches the design table from the Microsoft Excel sheet."""
		self._instance.Detach = value

	@property
	def edit_feature(self):
		"""Lets you change the characteristics of the design table."""
		return self._instance.EditFeature

	@edit_feature.setter
	def edit_feature(self, value):
		"""Lets you change the characteristics of the design table."""
		self._instance.EditFeature = value

	@property
	def edit_table(self):
		"""Lets you edit the design table."""
		return self._instance.EditTable2

	@edit_table.setter
	def edit_table(self, value):
		"""Lets you edit the design table."""
		self._instance.EditTable2 = value

	@property
	def get_column_count(self):
		"""Gets the number of columns in the design table that are currently visible in the model view."""
		return self._instance.GetColumnCount

	@get_column_count.setter
	def get_column_count(self, value):
		"""Gets the number of columns in the design table that are currently visible in the model view."""
		self._instance.GetColumnCount = value

	@property
	def get_entry_text(self):
		"""Gets the contents of the specified cell as a string regardless of the cell's data type."""
		return self._instance.GetEntryText

	@get_entry_text.setter
	def get_entry_text(self, value):
		"""Gets the contents of the specified cell as a string regardless of the cell's data type."""
		self._instance.GetEntryText = value

	@property
	def get_entry_value(self):
		"""Gets the contents of the specified cell."""
		return self._instance.GetEntryValue

	@get_entry_value.setter
	def get_entry_value(self, value):
		"""Gets the contents of the specified cell."""
		self._instance.GetEntryValue = value

	@property
	def get_header_text(self):
		"""Gets the header text for the specified column."""
		return self._instance.GetHeaderText

	@get_header_text.setter
	def get_header_text(self, value):
		"""Gets the header text for the specified column."""
		self._instance.GetHeaderText = value

	@property
	def get_row_count(self):
		"""Gets the number of rows in the design table that are currently visible in the model view."""
		return self._instance.GetRowCount

	@get_row_count.setter
	def get_row_count(self, value):
		"""Gets the number of rows in the design table that are currently visible in the model view."""
		self._instance.GetRowCount = value

	@property
	def get_start_column_number(self):
		"""Gets the number of the first column in which a dimension is displayed."""
		return self._instance.GetStartColumnNumber

	@get_start_column_number.setter
	def get_start_column_number(self, value):
		"""Gets the number of the first column in which a dimension is displayed."""
		self._instance.GetStartColumnNumber = value

	@property
	def get_start_row_number(self):
		"""Gets the number of the first row in which dimensions are displayed."""
		return self._instance.GetStartRowNumber

	@get_start_row_number.setter
	def get_start_row_number(self, value):
		"""Gets the number of the first row in which dimensions are displayed."""
		self._instance.GetStartRowNumber = value

	@property
	def get_title(self):
		"""Gets the design table title."""
		return self._instance.GetTitle

	@get_title.setter
	def get_title(self, value):
		"""Gets the design table title."""
		self._instance.GetTitle = value

	@property
	def get_total_column_count(self):
		"""Gets the number of columns in the design table."""
		return self._instance.GetTotalColumnCount

	@get_total_column_count.setter
	def get_total_column_count(self, value):
		"""Gets the number of columns in the design table."""
		self._instance.GetTotalColumnCount = value

	@property
	def get_total_row_count(self):
		"""Gets the number of rows in the design table."""
		return self._instance.GetTotalRowCount

	@get_total_row_count.setter
	def get_total_row_count(self, value):
		"""Gets the number of rows in the design table."""
		self._instance.GetTotalRowCount = value

	@property
	def get_visible_column_count(self):
		"""Gets the number of columns visible in this design table."""
		return self._instance.GetVisibleColumnCount

	@get_visible_column_count.setter
	def get_visible_column_count(self, value):
		"""Gets the number of columns visible in this design table."""
		self._instance.GetVisibleColumnCount = value

	@property
	def get_visible_left_column_number(self):
		"""Gets the number of the leftmost visible column."""
		return self._instance.GetVisibleLeftColumnNumber

	@get_visible_left_column_number.setter
	def get_visible_left_column_number(self, value):
		"""Gets the number of the leftmost visible column."""
		self._instance.GetVisibleLeftColumnNumber = value

	@property
	def get_visible_row_count(self):
		"""Gets the number of rows visible in the design table."""
		return self._instance.GetVisibleRowCount

	@get_visible_row_count.setter
	def get_visible_row_count(self, value):
		"""Gets the number of rows visible in the design table."""
		self._instance.GetVisibleRowCount = value

	@property
	def get_visible_top_row_number(self):
		"""Gets the number of the topmost visible row."""
		return self._instance.GetVisibleTopRowNumber

	@get_visible_top_row_number.setter
	def get_visible_top_row_number(self, value):
		"""Gets the number of the topmost visible row."""
		self._instance.GetVisibleTopRowNumber = value

	@property
	def is_active(self):
		"""Gets whether the design table is currently being edited."""
		return self._instance.IsActive

	@is_active.setter
	def is_active(self, value):
		"""Gets whether the design table is currently being edited."""
		self._instance.IsActive = value

	@property
	def save_as_excel_file(self):
		"""Saves the design table to a Microsoft Excel file."""
		return self._instance.SaveAsExcelFile

	@save_as_excel_file.setter
	def save_as_excel_file(self, value):
		"""Saves the design table to a Microsoft Excel file."""
		self._instance.SaveAsExcelFile = value

	@property
	def set_entry_text(self):
		"""Sets the text value of the specified entry."""
		return self._instance.SetEntryText

	@set_entry_text.setter
	def set_entry_text(self, value):
		"""Sets the text value of the specified entry."""
		self._instance.SetEntryText = value

	@property
	def set_entry_value(self):
		"""Sets the data type and value in the specified cell."""
		return self._instance.SetEntryValue

	@set_entry_value.setter
	def set_entry_value(self, value):
		"""Sets the data type and value in the specified cell."""
		self._instance.SetEntryValue = value

	@property
	def set_row_changed(self):
		"""Sets the number of the row that was changed."""
		return self._instance.SetRowChanged

	@set_row_changed.setter
	def set_row_changed(self, value):
		"""Sets the number of the row that was changed."""
		self._instance.SetRowChanged = value

	@property
	def update_feature(self):
		"""Updates the characteristics of the design table."""
		return self._instance.UpdateFeature

	@update_feature.setter
	def update_feature(self, value):
		"""Updates the characteristics of the design table."""
		self._instance.UpdateFeature = value

	@property
	def update_model(self):
		"""Applies the edits to the design table to the model."""
		return self._instance.UpdateModel

	@update_model.setter
	def update_model(self, value):
		"""Applies the edits to the design table to the model."""
		self._instance.UpdateModel = value

	@property
	def update_table(self):
		"""Applies the changes made to the design table to the model."""
		return self._instance.UpdateTable

	@update_table.setter
	def update_table(self, value):
		"""Applies the changes made to the design table to the model."""
		self._instance.UpdateTable = value

