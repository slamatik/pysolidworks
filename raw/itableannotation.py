# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html
class ITableAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def anchored(self):
		"""Gets or sets whether this table is attached to its anchor."""
		return self._instance.Anchored

	@anchored.setter
	def anchored(self, value):
		"""Gets or sets whether this table is attached to its anchor."""
		self._instance.Anchored = value

	@property
	def anchor_type(self):
		"""Gets or sets the anchor point for this table annotation."""
		return self._instance.AnchorType

	@anchor_type.setter
	def anchor_type(self, value):
		"""Gets or sets the anchor point for this table annotation."""
		self._instance.AnchorType = value

	@property
	def border_line_weight(self):
		"""Gets or sets the line weight of the border lines to the specified SOLIDWORKS-supplied weight for this table."""
		return self._instance.BorderLineWeight

	@border_line_weight.setter
	def border_line_weight(self, value):
		"""Gets or sets the line weight of the border lines to the specified SOLIDWORKS-supplied weight for this table."""
		self._instance.BorderLineWeight = value

	@property
	def border_line_weight_custom(self):
		"""Gets or sets the line weight of the border lines to the specified custom weight for this table."""
		return self._instance.BorderLineWeightCustom

	@border_line_weight_custom.setter
	def border_line_weight_custom(self, value):
		"""Gets or sets the line weight of the border lines to the specified custom weight for this table."""
		self._instance.BorderLineWeightCustom = value

	@property
	def cell_text_horizontal_justification(self):
		"""Gets or sets the horizontal justification for the text in the specified cell."""
		return self._instance.CellTextHorizontalJustification

	@cell_text_horizontal_justification.setter
	def cell_text_horizontal_justification(self, value):
		"""Gets or sets the horizontal justification for the text in the specified cell."""
		self._instance.CellTextHorizontalJustification = value

	@property
	def cell_text_vertical_justification(self):
		"""Gets or sets the vertical justification for the text in the specified cell."""
		return self._instance.CellTextVerticalJustification

	@cell_text_vertical_justification.setter
	def cell_text_vertical_justification(self, value):
		"""Gets or sets the vertical justification for the text in the specified cell."""
		self._instance.CellTextVerticalJustification = value

	@property
	def column_count(self):
		"""Gets the number of columns in this table."""
		return self._instance.ColumnCount

	@column_count.setter
	def column_count(self, value):
		"""Gets the number of columns in this table."""
		self._instance.ColumnCount = value

	@property
	def column_hidden(self):
		"""Hides or shows the specified column in this table annotation."""
		return self._instance.ColumnHidden

	@column_hidden.setter
	def column_hidden(self, value):
		"""Hides or shows the specified column in this table annotation."""
		self._instance.ColumnHidden = value

	@property
	def displayed_text(self):
		"""Gets the actual text displayed in the specified cell in this table."""
		return self._instance.DisplayedText2

	@displayed_text.setter
	def displayed_text(self, value):
		"""Gets the actual text displayed in the specified cell in this table."""
		self._instance.DisplayedText2 = value

	@property
	def general_table_feature(self):
		"""Gets the general table feature for this general table annotation."""
		return self._instance.GeneralTableFeature

	@general_table_feature.setter
	def general_table_feature(self, value):
		"""Gets the general table feature for this general table annotation."""
		self._instance.GeneralTableFeature = value

	@property
	def grid_line_weight(self):
		"""Gets or sets the line weight of the inner lines to the SOLIDWORKS-supplied weight for this table."""
		return self._instance.GridLineWeight

	@grid_line_weight.setter
	def grid_line_weight(self, value):
		"""Gets or sets the line weight of the inner lines to the SOLIDWORKS-supplied weight for this table."""
		self._instance.GridLineWeight = value

	@property
	def grid_line_weight_custom(self):
		"""Gets or sets the line weight of the inner lines to the specified custom weight for this table."""
		return self._instance.GridLineWeightCustom

	@grid_line_weight_custom.setter
	def grid_line_weight_custom(self, value):
		"""Gets or sets the line weight of the inner lines to the specified custom weight for this table."""
		self._instance.GridLineWeightCustom = value

	@property
	def row_count(self):
		"""Gets the number of rows in this table."""
		return self._instance.RowCount

	@row_count.setter
	def row_count(self, value):
		"""Gets the number of rows in this table."""
		self._instance.RowCount = value

	@property
	def row_hidden(self):
		"""Gets or sets whether the specified row is hidden in this table."""
		return self._instance.RowHidden

	@row_hidden.setter
	def row_hidden(self, value):
		"""Gets or sets whether the specified row is hidden in this table."""
		self._instance.RowHidden = value

	@property
	def stop_auto_splitting(self):
		"""Stops the automatic horizontal splitting of this table."""
		return self._instance.StopAutoSplitting

	@stop_auto_splitting.setter
	def stop_auto_splitting(self, value):
		"""Stops the automatic horizontal splitting of this table."""
		self._instance.StopAutoSplitting = value

	@property
	def text(self):
		"""Gets or sets the parametrized string of text for the specified cell of this table."""
		return self._instance.Text2

	@text.setter
	def text(self, value):
		"""Gets or sets the parametrized string of text for the specified cell of this table."""
		self._instance.Text2 = value

	@property
	def text_horizontal_justification(self):
		"""Gets or sets the horizontal justification setting for the text in this table."""
		return self._instance.TextHorizontalJustification

	@text_horizontal_justification.setter
	def text_horizontal_justification(self, value):
		"""Gets or sets the horizontal justification setting for the text in this table."""
		self._instance.TextHorizontalJustification = value

	@property
	def text_vertical_justification(self):
		"""Gets or sets the vertical justification for the text in this table."""
		return self._instance.TextVerticalJustification

	@text_vertical_justification.setter
	def text_vertical_justification(self, value):
		"""Gets or sets the vertical justification for the text in this table."""
		self._instance.TextVerticalJustification = value

	@property
	def title(self):
		"""Gets or sets the title for this table."""
		return self._instance.Title

	@title.setter
	def title(self, value):
		"""Gets or sets the title for this table."""
		self._instance.Title = value

	@property
	def title_visible(self):
		"""Gets or sets whether the title of the table is visible."""
		return self._instance.TitleVisible

	@title_visible.setter
	def title_visible(self, value):
		"""Gets or sets whether the title of the table is visible."""
		self._instance.TitleVisible = value

	@property
	def total_column_count(self):
		"""Gets the total number of visible and hidden columns in this table."""
		return self._instance.TotalColumnCount

	@total_column_count.setter
	def total_column_count(self, value):
		"""Gets the total number of visible and hidden columns in this table."""
		self._instance.TotalColumnCount = value

	@property
	def total_row_count(self):
		"""Gets the total number of visible and hidden rows in this table."""
		return self._instance.TotalRowCount

	@total_row_count.setter
	def total_row_count(self, value):
		"""Gets the total number of visible and hidden rows in this table."""
		self._instance.TotalRowCount = value

	@property
	def type(self):
		"""Gets the type of table."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the type of table."""
		self._instance.Type = value

	@property
	def upper_case(self):
		"""Gets or sets whether text in the table is all upper case."""
		return self._instance.UpperCase

	@upper_case.setter
	def upper_case(self, value):
		"""Gets or sets whether text in the table is all upper case."""
		self._instance.UpperCase = value

	@property
	def delete_column(self):
		"""Deletes the specified column in this table."""
		return self._instance.DeleteColumn2

	@delete_column.setter
	def delete_column(self, value):
		"""Deletes the specified column in this table."""
		self._instance.DeleteColumn2 = value

	@property
	def delete_row(self):
		"""Deletes the specified row from this table."""
		return self._instance.DeleteRow2

	@delete_row.setter
	def delete_row(self, value):
		"""Deletes the specified row from this table."""
		self._instance.DeleteRow2 = value

	@property
	def evaluate_cell_equation(self):
		"""Solves the specified equation in the specified cell of this BOM table."""
		return self._instance.EvaluateCellEquation

	@evaluate_cell_equation.setter
	def evaluate_cell_equation(self, value):
		"""Solves the specified equation in the specified cell of this BOM table."""
		self._instance.EvaluateCellEquation = value

	@property
	def get_annotation(self):
		"""Gets the annotation for this table annotation."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the annotation for this table annotation."""
		self._instance.GetAnnotation = value

	@property
	def get_cell_equation(self):
		"""Gets the equation and its solved value for the specified row and column of this BOM table."""
		return self._instance.GetCellEquation

	@get_cell_equation.setter
	def get_cell_equation(self, value):
		"""Gets the equation and its solved value for the specified row and column of this BOM table."""
		self._instance.GetCellEquation = value

	@property
	def get_cell_range(self):
		"""Gets the selected table cells' row and column index ranges."""
		return self._instance.GetCellRange

	@get_cell_range.setter
	def get_cell_range(self, value):
		"""Gets the selected table cells' row and column index ranges."""
		self._instance.GetCellRange = value

	@property
	def get_cell_text_format(self):
		"""Gets the text format for the specified cell in this table."""
		return self._instance.GetCellTextFormat

	@get_cell_text_format.setter
	def get_cell_text_format(self, value):
		"""Gets the text format for the specified cell in this table."""
		self._instance.GetCellTextFormat = value

	@property
	def get_cell_text_orientation(self):
		"""Gets the text orientation in the specified cell of this table."""
		return self._instance.GetCellTextOrientation

	@get_cell_text_orientation.setter
	def get_cell_text_orientation(self, value):
		"""Gets the text orientation in the specified cell of this table."""
		self._instance.GetCellTextOrientation = value

	@property
	def get_cell_use_doc_text_format(self):
		"""Gets whether this cell uses the document setting for its text format."""
		return self._instance.GetCellUseDocTextFormat

	@get_cell_use_doc_text_format.setter
	def get_cell_use_doc_text_format(self, value):
		"""Gets whether this cell uses the document setting for its text format."""
		self._instance.GetCellUseDocTextFormat = value

	@property
	def get_column_title(self):
		"""Gets the title of the specified column."""
		return self._instance.GetColumnTitle2

	@get_column_title.setter
	def get_column_title(self, value):
		"""Gets the title of the specified column."""
		self._instance.GetColumnTitle2 = value

	@property
	def get_column_type(self):
		"""Gets the type and property data for the specified BOM table column."""
		return self._instance.GetColumnType3

	@get_column_type.setter
	def get_column_type(self, value):
		"""Gets the type and property data for the specified BOM table column."""
		self._instance.GetColumnType3 = value

	@property
	def get_column_width(self):
		"""Gets the width of the specified column of this table annotation."""
		return self._instance.GetColumnWidth

	@get_column_width.setter
	def get_column_width(self, value):
		"""Gets the width of the specified column of this table annotation."""
		self._instance.GetColumnWidth = value

	@property
	def get_header_count(self):
		"""Gets the number of rows or columns in the header of this table."""
		return self._instance.GetHeaderCount

	@get_header_count.setter
	def get_header_count(self, value):
		"""Gets the number of rows or columns in the header of this table."""
		self._instance.GetHeaderCount = value

	@property
	def get_header_style(self):
		"""Gets the header style of this table."""
		return self._instance.GetHeaderStyle

	@get_header_style.setter
	def get_header_style(self, value):
		"""Gets the header style of this table."""
		self._instance.GetHeaderStyle = value

	@property
	def get_lock_column_width(self):
		"""Gets whether the width of the specified column is locked in this table annotation."""
		return self._instance.GetLockColumnWidth

	@get_lock_column_width.setter
	def get_lock_column_width(self, value):
		"""Gets whether the width of the specified column is locked in this table annotation."""
		self._instance.GetLockColumnWidth = value

	@property
	def get_lock_row_height(self):
		"""Gets whether the height of the specified row is locked in this table annotation."""
		return self._instance.GetLockRowHeight

	@get_lock_row_height.setter
	def get_lock_row_height(self, value):
		"""Gets whether the height of the specified row is locked in this table annotation."""
		self._instance.GetLockRowHeight = value

	@property
	def get_next(self):
		"""Gets the next table annotation in this drawing view."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next table annotation in this drawing view."""
		self._instance.GetNext = value

	@property
	def get_row_height(self):
		"""Gets the height of the specified row of this table."""
		return self._instance.GetRowHeight

	@get_row_height.setter
	def get_row_height(self, value):
		"""Gets the height of the specified row of this table."""
		self._instance.GetRowHeight = value

	@property
	def get_row_vertical_gap(self):
		"""Gets the gap between the text and the top or bottom of the specified row of this table."""
		return self._instance.GetRowVerticalGap

	@get_row_vertical_gap.setter
	def get_row_vertical_gap(self, value):
		"""Gets the gap between the text and the top or bottom of the specified row of this table."""
		self._instance.GetRowVerticalGap = value

	@property
	def get_split_information(self):
		"""Gets information about any splits in this table."""
		return self._instance.GetSplitInformation

	@get_split_information.setter
	def get_split_information(self, value):
		"""Gets information about any splits in this table."""
		self._instance.GetSplitInformation = value

	@property
	def get_text_format(self):
		"""Gets the text format for this table."""
		return self._instance.GetTextFormat

	@get_text_format.setter
	def get_text_format(self, value):
		"""Gets the text format for this table."""
		self._instance.GetTextFormat = value

	@property
	def get_use_doc_text_format(self):
		"""Gets whether this table uses the document setting for text formatting."""
		return self._instance.GetUseDocTextFormat

	@get_use_doc_text_format.setter
	def get_use_doc_text_format(self, value):
		"""Gets whether this table uses the document setting for text formatting."""
		self._instance.GetUseDocTextFormat = value

	@property
	def horizontal_auto_split(self):
		"""Starts the automatic horizontal splitting of this table using the specified options."""
		return self._instance.HorizontalAutoSplit

	@horizontal_auto_split.setter
	def horizontal_auto_split(self, value):
		"""Starts the automatic horizontal splitting of this table using the specified options."""
		self._instance.HorizontalAutoSplit = value

	@property
	def insert_column(self):
		"""Inserts a column into this table."""
		return self._instance.InsertColumn2

	@insert_column.setter
	def insert_column(self, value):
		"""Inserts a column into this table."""
		self._instance.InsertColumn2 = value

	@property
	def insert_row(self):
		"""Inserts a row into this table."""
		return self._instance.InsertRow

	@insert_row.setter
	def insert_row(self, value):
		"""Inserts a row into this table."""
		self._instance.InsertRow = value

	@property
	def is_cell_merged(self):
		"""Gets whether the specified cell is merged with other cells."""
		return self._instance.IsCellMerged

	@is_cell_merged.setter
	def is_cell_merged(self, value):
		"""Gets whether the specified cell is merged with other cells."""
		self._instance.IsCellMerged = value

	@property
	def is_cell_text_editable(self):
		"""Gets whether the text in this cell can be edited."""
		return self._instance.IsCellTextEditable

	@is_cell_text_editable.setter
	def is_cell_text_editable(self, value):
		"""Gets whether the text in this cell can be edited."""
		self._instance.IsCellTextEditable = value

	@property
	def merge(self):
		"""Merges the display of this table."""
		return self._instance.Merge

	@merge.setter
	def merge(self, value):
		"""Merges the display of this table."""
		self._instance.Merge = value

	@property
	def merge_cells(self):
		"""Merges the cells in the specified range."""
		return self._instance.MergeCells

	@merge_cells.setter
	def merge_cells(self, value):
		"""Merges the cells in the specified range."""
		self._instance.MergeCells = value

	@property
	def move_column(self):
		"""Moves a column in this table annotation."""
		return self._instance.MoveColumn

	@move_column.setter
	def move_column(self, value):
		"""Moves a column in this table annotation."""
		self._instance.MoveColumn = value

	@property
	def move_row(self):
		"""Moves a row in this table either up one row or down one row."""
		return self._instance.MoveRow

	@move_row.setter
	def move_row(self, value):
		"""Moves a row in this table either up one row or down one row."""
		self._instance.MoveRow = value

	@property
	def save_as_p_d_f(self):
		"""Saves this table to a PDF file."""
		return self._instance.SaveAsPDF

	@save_as_p_d_f.setter
	def save_as_p_d_f(self, value):
		"""Saves this table to a PDF file."""
		self._instance.SaveAsPDF = value

	@property
	def save_as_template(self):
		"""Saves the format of this table as a template file, which you can then use to create other tables of the same type and that look the same."""
		return self._instance.SaveAsTemplate

	@save_as_template.setter
	def save_as_template(self, value):
		"""Saves the format of this table as a template file, which you can then use to create other tables of the same type and that look the same."""
		self._instance.SaveAsTemplate = value

	@property
	def save_as_text(self):
		"""Saves this table to a text data file."""
		return self._instance.SaveAsText2

	@save_as_text.setter
	def save_as_text(self, value):
		"""Saves this table to a text data file."""
		self._instance.SaveAsText2 = value

	@property
	def set_cell_equation(self):
		"""Sets the specified equation for the specified row and column of this BOM table."""
		return self._instance.SetCellEquation

	@set_cell_equation.setter
	def set_cell_equation(self, value):
		"""Sets the specified equation for the specified row and column of this BOM table."""
		self._instance.SetCellEquation = value

	@property
	def set_cell_range(self):
		"""Sets the current range of cells."""
		return self._instance.SetCellRange

	@set_cell_range.setter
	def set_cell_range(self, value):
		"""Sets the current range of cells."""
		self._instance.SetCellRange = value

	@property
	def set_cell_text_format(self):
		"""Sets the text format for the text in the specified cell."""
		return self._instance.SetCellTextFormat

	@set_cell_text_format.setter
	def set_cell_text_format(self, value):
		"""Sets the text format for the text in the specified cell."""
		self._instance.SetCellTextFormat = value

	@property
	def set_cell_text_orientation(self):
		"""Sets the text orientation in the specified table cell."""
		return self._instance.SetCellTextOrientation

	@set_cell_text_orientation.setter
	def set_cell_text_orientation(self, value):
		"""Sets the text orientation in the specified table cell."""
		self._instance.SetCellTextOrientation = value

	@property
	def set_column_title(self):
		"""Sets the title of the specified column."""
		return self._instance.SetColumnTitle2

	@set_column_title.setter
	def set_column_title(self, value):
		"""Sets the title of the specified column."""
		self._instance.SetColumnTitle2 = value

	@property
	def set_column_type(self):
		"""Sets the type and property data for the specified BOM table column."""
		return self._instance.SetColumnType3

	@set_column_type.setter
	def set_column_type(self, value):
		"""Sets the type and property data for the specified BOM table column."""
		self._instance.SetColumnType3 = value

	@property
	def set_column_width(self):
		"""Sets the width of the specified column in this table."""
		return self._instance.SetColumnWidth

	@set_column_width.setter
	def set_column_width(self, value):
		"""Sets the width of the specified column in this table."""
		self._instance.SetColumnWidth = value

	@property
	def set_header(self):
		"""Sets the header for this table."""
		return self._instance.SetHeader

	@set_header.setter
	def set_header(self, value):
		"""Sets the header for this table."""
		self._instance.SetHeader = value

	@property
	def set_lock_column_width(self):
		"""Sets whether to lock the width of the specified column in this table annotation."""
		return self._instance.SetLockColumnWidth

	@set_lock_column_width.setter
	def set_lock_column_width(self, value):
		"""Sets whether to lock the width of the specified column in this table annotation."""
		self._instance.SetLockColumnWidth = value

	@property
	def set_lock_row_height(self):
		"""Sets whether to lock the height of the specified row in this table annotation."""
		return self._instance.SetLockRowHeight

	@set_lock_row_height.setter
	def set_lock_row_height(self, value):
		"""Sets whether to lock the height of the specified row in this table annotation."""
		self._instance.SetLockRowHeight = value

	@property
	def set_row_height(self):
		"""Sets the height of the specified row in this table."""
		return self._instance.SetRowHeight

	@set_row_height.setter
	def set_row_height(self, value):
		"""Sets the height of the specified row in this table."""
		self._instance.SetRowHeight = value

	@property
	def set_row_vertical_gap(self):
		"""Sets the gap between the text and the top or bottom of the specified row of this table."""
		return self._instance.SetRowVerticalGap

	@set_row_vertical_gap.setter
	def set_row_vertical_gap(self, value):
		"""Sets the gap between the text and the top or bottom of the specified row of this table."""
		self._instance.SetRowVerticalGap = value

	@property
	def set_text_format(self):
		"""Sets the text format for this table."""
		return self._instance.SetTextFormat

	@set_text_format.setter
	def set_text_format(self, value):
		"""Sets the text format for this table."""
		self._instance.SetTextFormat = value

	@property
	def split(self):
		"""Splits the table at the specified location."""
		return self._instance.Split

	@split.setter
	def split(self, value):
		"""Splits the table at the specified location."""
		self._instance.Split = value

	@property
	def unmerge_cells(self):
		"""Splits the specified previously merged cell in this table."""
		return self._instance.UnmergeCells

	@unmerge_cells.setter
	def unmerge_cells(self, value):
		"""Splits the specified previously merged cell in this table."""
		self._instance.UnmergeCells = value

