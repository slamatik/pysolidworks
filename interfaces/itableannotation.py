import interfaces.itextformat
import win32com.client as win32
import pythoncom
from com import Com


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html
class ITableAnnotation:
    def __init__(self, parent=None):
        self._instance = parent

    def anchored(self):
        """Gets or sets whether this table is attached to its anchor."""
        # return self._instance.Anchored
        raise NotImplemented

    def anchor_type(self):
        """Gets or sets the anchor point for this table annotation."""
        # return self._instance.AnchorType
        raise NotImplemented

    def border_line_weight(self):
        """Gets or sets the line weight of the border lines to the specified SOLIDWORKS-supplied weight for this
        table."""
        # return self._instance.BorderLineWeight
        raise NotImplemented

    def border_line_weight_custom(self):
        """Gets or sets the line weight of the border lines to the specified custom weight for this table."""
        # return self._instance.BorderLineWeightCustom
        raise NotImplemented

    def cell_text_horizontal_justification(self, row, column):
        """
        Gets or sets the horizontal justification for the text in the specified cell.
        :param row: Index of the row in which the cell resides
        :param column: Index of the column in which the cell resides
        """
        # return self._instance.CellTextHorizontalJustification(row, column)
        raise NotImplemented

    def cell_text_vertical_justification(self, row, column):
        """
        Gets or sets the vertical justification for the text in the specified cell.
        :param row: Index of the row in which this cell resides
        :param column: Index of the column in which this cell resides
        """
        # return self._instance.CellTextVerticalJustification(row, column)
        raise NotImplemented

    def column_count(self):
        """Gets the number of columns in this table."""
        # return self._instance.ColumnCount
        raise NotImplemented

    def column_hidden(self, index):
        """
        Hides or shows the specified column in this table annotation.
        :param index: Index of column to show or hide
        """
        # return self._instance.ColumnHidden(index)
        raise NotImplemented

    def displayed_text(self, row, column, include_hidden):
        """
        Gets the actual text displayed in the specified cell in this table.
        :param row: Index of the row
        :param column: Index of the column
        :param include_hidden: True to get the text displayed in the hidden cell, false to not
        """
        # return self._instance.DisplayedText2(row, column, include_hidden)
        raise NotImplemented

    def general_table_feature(self):
        """Gets the general table feature for this general table annotation."""
        # return self._instance.GeneralTableFeature
        raise NotImplemented

    def grid_line_weight(self):
        """Gets or sets the line weight of the inner lines to the SOLIDWORKS-supplied weight for this table."""
        # return self._instance.GridLineWeight
        raise NotImplemented

    def grid_line_weight_custom(self):
        """Gets or sets the line weight of the inner lines to the specified custom weight for this table."""
        # return self._instance.GridLineWeightCustom
        raise NotImplemented

    def row_count(self):
        """Gets the number of rows in this table."""
        # return self._instance.RowCount
        raise NotImplemented

    def row_hidden(self, index):
        """
        Gets or sets whether the specified row is hidden in this table.
        :param index: Index of row
        """
        # return self._instance.RowHidden(index)
        raise NotImplemented

    def stop_auto_splitting(self):
        """Stops the automatic horizontal splitting of this table."""
        # return self._instance.StopAutoSplitting
        raise NotImplemented

    def text(self, row, column, include_hidden):
        """
        Gets or sets the parametrized string of text for the specified cell of this table.
        :param row: Index of the row
        :param column: Index of the column
        :param include_hidden: True to get or set text in the hidden cell, false to not
        """
        # return self._instance.Text2(row, column, include_hidden)
        raise NotImplemented

    def text_horizontal_justification(self):
        """Gets or sets the horizontal justification setting for the text in this table."""
        # return self._instance.TextHorizontalJustification
        raise NotImplemented

    def text_vertical_justification(self):
        """Gets or sets the vertical justification for the text in this table."""
        # return self._instance.TextVerticalJustification
        raise NotImplemented

    def title(self):
        """Gets or sets the title for this table."""
        return self._instance.Title

    def title_visible(self):
        """Gets or sets whether the title of the table is visible."""
        # return self._instance.TitleVisible
        raise NotImplemented

    def total_column_count(self):
        """Gets the total number of visible and hidden columns in this table."""
        # return self._instance.TotalColumnCount
        raise NotImplemented

    def total_row_count(self):
        """Gets the total number of visible and hidden rows in this table."""
        # return self._instance.TotalRowCount
        raise NotImplemented

    def type(self):
        """Gets the type of table."""
        # return self._instance.Type
        raise NotImplemented

    def upper_case(self):
        """Gets or sets whether text in the table is all upper case."""
        # return self._instance.UpperCase
        raise NotImplemented

    def delete_column(self, index, include_hidden):
        """
        Deletes the specified column in this table.
        :param index: Index of the column you want to delete
        :param include_hidden: True to delete the hidden column, false to not
        """
        # return self._instance.DeleteColumn2(index, include_hidden)
        raise NotImplemented

    def delete_row(self, index, include_hidden):
        """
        Deletes the specified row from this table.
        :param index: Index of the row you want to delete
        :param include_hidden: True to delete the hidden row, false to not
        """
        # return self._instance.DeleteRow2(index, include_hidden)
        raise NotImplemented

    def evaluate_cell_equation(self, row, column, include_hidden, equation, solved_value):
        """
        Solves the specified equation in the specified cell of this BOM table.
        :param row: 0-based index of the row
        :param column: 0-based index of the column
        :param include_hidden: True to include hidden rows and columns in the Row and Column indexes, false to not
        :param equation: Equation to solve; empty string to remove an equation
        :param solved_value: Value of solved Equation
        """
        # return self._instance.EvaluateCellEquation(row, column, include_hidden, equation, solved_value)
        raise NotImplemented

    def get_annotation(self):
        """Gets the annotation for this table annotation."""
        # return self._instance.GetAnnotation
        raise NotImplemented

    def get_cell_equation(self, row, column, include_hidden, solved_value, status):
        """
        Gets the equation and its solved value for the specified row and column of this BOM table.
        :param row: 0-based index of the row, -1 to get the column equation
        :param column: 0-based index of the column
        :param include_hidden: True to include hidden rows and columns in the Row and Column indexes, false to not
        :param solved_value: Evaluated equation
        :param status: Return code as defined in swCellEquationStatus_e
        """
        # return self._instance.GetCellEquation(row, column, include_hidden, solved_value, status)
        raise NotImplemented

    def get_cell_range(self, first_row, last_row, first_column, last_column):
        """
        Gets the selected table cells' row and column index ranges.
        :param first_row: Index of row of first selected cell
        :param last_row: Index of row of last selected cell
        :param first_column: Index of column of first selected cell
        :param last_column: Index of column of last selected cell
        """
        # return self._instance.GetCellRange(first_row, last_row, first_column, last_column)
        raise NotImplemented

    def get_cell_text_format(self, row, column):
        """
        Gets the text format for the specified cell in this table.
        :param row: Index of the row in which the cell is located
        :param column: Index of the column in which the cell is located
        """
        return interfaces.itextformat.ITextFormat(self._instance.GetCellTextFormat(row, column))

    def get_cell_text_orientation(self, row, column, include_hidden, all_cells):
        """
        Gets the text orientation in the specified cell of this table.
        :param row: 0-based index of the cell row; valid only if AllCells is set to false
        :param column: 0-based index of the cell column; valid only if AllCells is set to false
        :param include_hidden: True to include hidden rows and columns in Row and Column indexes, false to not
        :param all_cells: True to get the orientation in all cells, false to not; if false, set Row and Column (see Remarks)
        """
        # return self._instance.GetCellTextOrientation(row, column, include_hidden, all_cells)
        raise NotImplemented

    def get_cell_use_doc_text_format(self, row, column):
        """
        Gets whether this cell uses the document setting for its text format.
        :param row: Index of the row in which the cell resides
        :param column: Index of the column in which the cell resides
        """
        # return self._instance.GetCellUseDocTextFormat(row, column)
        raise NotImplemented

    def get_column_title(self, index, include_hidden):
        """
        Gets the title of the specified column.
        :param index: 0-based index indicating the column
        :param include_hidden: True to get the title of the hidden column, false to not
        """
        # return self._instance.GetColumnTitle2(index, include_hidden)
        raise NotImplemented

    def get_column_type(self, index, include_hidden, property_data, status):
        """
        Gets the type and property data for the specified BOM table column.
        :param index: 0-based index of the column whose type to get
        :param include_hidden: True to include hidden columns in Index, false to not
        :param property_data: Property data specific to the type of column (see Remarks)
        :param status: Return code as defined in swColumnTypeStatus_e
        """
        # return self._instance.GetColumnType3(index, include_hidden, property_data, status)
        raise NotImplemented

    def get_column_width(self, index):
        """
        Gets the width of the specified column of this table annotation.
        :param index: Index of column for which to get the width
        """
        # return self._instance.GetColumnWidth(index)
        raise NotImplemented

    def get_header_count(self):
        """Gets the number of rows or columns in the header of this table."""
        # return self._instance.GetHeaderCount
        raise NotImplemented

    def get_header_style(self):
        """Gets the header style of this table."""
        # return self._instance.GetHeaderStyle
        raise NotImplemented

    def get_lock_column_width(self, index):
        """
        Gets whether the width of the specified column is locked in this table annotation.
        :param index: 0-based index of the column (see Remarks)
        """
        # return self._instance.GetLockColumnWidth(index)
        raise NotImplemented

    def get_lock_row_height(self, index):
        """
        Gets whether the height of the specified row is locked in this table annotation.
        :param index: 0-based index of the row (see Remarks)
        """
        # return self._instance.GetLockRowHeight(index)
        raise NotImplemented

    def get_next(self):
        """Gets the next table annotation in this drawing view."""
        # return self._instance.GetNext
        raise NotImplemented

    def get_row_height(self, index):
        """
        Gets the height of the specified row of this table.
        :param index: Index of row for which to get the height
        """
        # return self._instance.GetRowHeight(index)
        raise NotImplemented

    def get_row_vertical_gap(self, index):
        """
        Gets the gap between the text and the top or bottom of the specified row of this table.
        :param index: Index of row for which to get the height
        """
        # return self._instance.GetRowVerticalGap(index)
        raise NotImplemented

    def get_split_information(self, index, count, range_start, range_end):
        """
        Gets information about any splits in this table.
        :param index: Piece of the table that this is
        :param count: Piece of the table that this is
        :param range_start: Beginning row for this piece of the table
        :param range_end: Ending row for this piece of the table
        """
        # return self._instance.GetSplitInformation(index, count, range_start, range_end)
        raise NotImplemented

    def get_text_format(self):
        """Gets the text format for this table."""
        # return self._instance.GetTextFormat
        raise NotImplemented

    def get_use_doc_text_format(self):
        """Gets whether this table uses the document setting for text formatting."""
        # return self._instance.GetUseDocTextFormat
        raise NotImplemented

    def horizontal_auto_split(self, max_number_of_rows, apply, placement_of_new_split_tables):
        """
        Starts the automatic horizontal splitting of this table using the specified options.
        :param max_number_of_rows: Maximum number of rows in the split portions
        :param apply: How often to horizontally split the table as defined in swHorizontalAutoSplitApply_e
        :param placement_of_new_split_tables: Where to place the horizontally split table as defined in swHorizontalAutoSplitPlacementOfSplitTable_e
        """
        # return self._instance.HorizontalAutoSplit(max_number_of_rows, apply, placement_of_new_split_tables)
        raise NotImplemented

    def insert_column(self, where, index, name, width_style):
        """
        Inserts a column into this table.
        :param where: Where to insert the column as specified in swTableItemInsertPosition_e
        :param index: Index of the column where to insert the new column
        :param name: Column name
        :param width_style: Style of the width of the column as defined in swInsertTableColumnWidthStyle_e
        """
        # return self._instance.InsertColumn2(where, index, name, width_style)
        raise NotImplemented

    def insert_row(self, where, index):
        """
        Inserts a row into this table.
        :param where: Where to insert the new row as defined in swTableItemInsertPosition_e
        :param index: Index of row where to insert new row (see Remarks)
        """
        # return self._instance.InsertRow(where, index)
        raise NotImplemented

    def is_cell_merged(self, row, column, with_row, with_column):
        """
        Gets whether the specified cell is merged with other cells.
        :param row: Index of the row of the first cell to see if it's merged
        :param column: Index of the column of the first cell to see if it's merged
        :param with_row: Index of the row of the second cell with which the first cell is merged
        :param with_column: Index of the column of the second cell with which the first cell is merged
        """
        # return self._instance.IsCellMerged(row, column, with_row, with_column)
        raise NotImplemented

    def is_cell_text_editable(self, row, column):
        """
        Gets whether the text in this cell can be edited.
        :param row: Index of row in which cell resides
        :param column: Index of column in which cell resides
        """
        # return self._instance.IsCellTextEditable(row, column)
        raise NotImplemented

    def merge(self, where):
        """
        Merges the display of this table.
        :param where: Merge the display of this table as defined in swTableMergeLocations_e
        """
        # return self._instance.Merge(where)
        raise NotImplemented

    def merge_cells(self, row_start, column_start, row_end, column_end):
        """
        Merges the cells in the specified range.
        :param row_start: Index of row at which start the merge
        :param column_start: Index of column at which to start the merge
        :param row_end: Index of row at which to end the merge
        :param column_end: Index of column at which to end the merge
        """
        # return self._instance.MergeCells(row_start, column_start, row_end, column_end)
        raise NotImplemented

    def move_column(self, source, where, destination):
        """
        Moves a column in this table annotation.
        :param source: Index of column to move
        :param where: Position where to move Source relative to Destination as defined by swTableItemInsertPosition_e
        :param destination: Index of column where to move Source
        """
        # return self._instance.MoveColumn(source, where, destination)
        raise NotImplemented

    def move_row(self, source, where, destination):
        """
        Moves a row in this table either up one row or down one row.
        :param source: Index of row to move
        :param where: Position where to move Source relative to Destination as defined by swTableItemInsertPosition_e
        :param destination: Index of row where to move Source, which is either 1 greater than the Source or 1 less than Source
        """
        # return self._instance.MoveRow(source, where, destination)
        raise NotImplemented

    def save_as_p_d_f(self, file_name):
        """
        Saves this table to a PDF file.
        :param file_name: Full path and filename of the PDF File (see Remarks)
        """
        # return self._instance.SaveAsPDF(file_name)
        raise NotImplemented

    def save_as_template(self, file_name):
        """
        Saves the format of this table as a template file, which you can then use to create other tables of the same type and that look the same.
        :param file_name: Full path and filename to which to save the table template file (see Remarks)
        """
        # return self._instance.SaveAsTemplate(file_name)
        raise NotImplemented

    def save_as_text(self, file_name, separator, include_hidden):
        """
        Saves this table to a text data file.
        :param file_name: Full path and filename of text data file (see Remarks)
        :param separator: Character or string to use to separate each of the text within each of the cells in the table in the text file (see Remarks)
        :param include_hidden: True to include text in hidden cells, false to not
        """
        # return self._instance.SaveAsText2(file_name, separator, include_hidden)
        raise NotImplemented

    def set_cell_equation(self, row, column, include_hidden, equation):
        """
        Sets the specified equation for the specified row and column of this BOM table.
        :param row: 0-based index of the row, -1 to set a column equation
        :param column: 0-based index of the column
        :param include_hidden: True to include hidden rows and columns in the Row and Column indexes, false to not
        :param equation: Equation
        """
        # return self._instance.SetCellEquation(row, column, include_hidden, equation)
        raise NotImplemented

    def set_cell_range(self, first_row, last_row, first_column, last_column):
        """
        Sets the current range of cells.
        :param first_row: First row in the range
        :param last_row: Last row in the range
        :param first_column: First column in the range
        :param last_column: Last column in the range
        """
        # return self._instance.SetCellRange(first_row, last_row, first_column, last_column)
        raise NotImplemented

    def set_cell_text_format(self, row, column, use_doc, text_format):
        """
        Sets the text format for the text in the specified cell.
        :param row: Index of row in which cell resides
        :param column: Index of column in which cell resides
        :param use_doc: True to use the document setting for the text format, false to not
        :param text_format: ITextFormat object
        """
        arg1 = win32.VARIANT(pythoncom.VT_I4, row)
        arg2 = win32.VARIANT(pythoncom.VT_I4, column)
        arg3 = win32.VARIANT(pythoncom.VT_BOOL, use_doc)
        # arg4 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_DISPATCH, win32.Dispatch(text_format))
        # arg4 = win32.VARIANT(pythoncom.VT_RECORD, text_format)
        return self._instance.SetCellTextFormat(row, column, use_doc, Com(text_format))

    def set_cell_text_orientation(self, row, column, include_hidden, all_cells, orientation):
        """
        Sets the text orientation in the specified table cell.
        :param row: 0-based index of row; valid only if AllCells is set to false
        :param column: 0-based index of column; valid only if AllCells is set to false
        :param include_hidden: True to include hidden rows and columns in the Row and Column indexes, false to not
        :param all_cells: True for all cells, false if not; if false, set Row and Column
        :param orientation: Text orientation as defined in swTableCellOrientation_e (see Remarks)
        """
        # return self._instance.SetCellTextOrientation(row, column, include_hidden, all_cells, orientation)
        raise NotImplemented

    def set_column_title(self, index, title, include_hidden):
        """
        Sets the title of the specified column.
        :param index: Index of the column whose title to set
        :param title: Column title
        :param include_hidden: True to set the hidden column title, false to not
        """
        # return self._instance.SetColumnTitle2(index, title, include_hidden)
        raise NotImplemented

    def set_column_type(self, index, column_type, include_hidden, property_data):
        """
        Sets the type and property data for the specified BOM table column.
        :param index: 0-based index of the column whose type to set
        :param column_type: Type of column as defined in swTableColumnTypes_e (see Remarks)
        :param include_hidden: True to include hidden columns in Index, false to not
        :param property_data: Property data specific to ColumnType (see Remarks)
        """
        # return self._instance.SetColumnType3(index, column_type, include_hidden, property_data)
        raise NotImplemented

    def set_column_width(self, index, width, options):
        """
        Sets the width of the specified column in this table.
        :param index: Index of column for which to set the width
        :param width: Width at which to set specified column, in system units
        :param options: Table's behavior after changing column width as defined by swTableRowColSizeChangeBehavior_e (see Remarks)
        """
        # return self._instance.SetColumnWidth(index, width, options)
        raise NotImplemented

    def set_header(self, style, count):
        """
        Sets the header for this table.
        :param style: Header style as defined in swTableHeaderPosition_e
        :param count: Number of lines in the header
        """
        # return self._instance.SetHeader(style, count)
        raise NotImplemented

    def set_lock_column_width(self, index, lock_column_width):
        """
        Sets whether to lock the width of the specified column in this table annotation.
        :param index: 0-based index of the column (see Remarks)
        :param lock_column_width: True to lock this column's width, false to not
        """
        # return self._instance.SetLockColumnWidth(index, lock_column_width)
        raise NotImplemented

    def set_lock_row_height(self, index, lock_row_height):
        """
        Sets whether to lock the height of the specified row in this table annotation.
        :param index: 0-based index of the row (see Remarks)
        :param lock_row_height: True to lock this row's height, false to not
        """
        # return self._instance.SetLockRowHeight(index, lock_row_height)
        raise NotImplemented

    def set_row_height(self, index, height, options):
        """
        Sets the height of the specified row in this table.
        :param index: Index of row for which to set height
        :param height: Height at which to set specified row, in system units
        :param options: Table's behavior after changing row as defined by swTableRowColSizeChangeBehavior_e (see Remarks)
        """
        # return self._instance.SetRowHeight(index, height, options)
        raise NotImplemented

    def set_row_vertical_gap(self, index, gap):
        """
        Sets the gap between the text and the top or bottom of the specified row of this table.
        :param index: Index of row for which to get the height
        :param gap: Gap in system units
        """
        # return self._instance.SetRowVerticalGap(index, gap)
        raise NotImplemented

    def set_text_format(self, use_doc, text_format):
        """
        Sets the text format for this table.
        :param use_doc: True to use the document setting, false to not
        :param text_format: ITextFormat object
        """
        # return self._instance.SetTextFormat(use_doc, text_format)
        raise NotImplemented

    def split(self, where, index):
        """
        Splits the table at the specified location.
        :param where: Where to split the table as defined in swTableSplitLocations_e
        :param index: Index of the row or column as specified in Where to split the table (see Remarks)
        """
        # return self._instance.Split(where, index)
        raise NotImplemented

    def unmerge_cells(self, row, column):
        """
        Splits the specified previously merged cell in this table.
        :param row: Index of the row of the cell
        :param column: Index of the column of the cell
        """
        # return self._instance.UnmergeCells(row, column)
        raise NotImplemented
