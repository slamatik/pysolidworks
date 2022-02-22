class IExportPdfData:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def export_as_d(self):
        """Gets or sets whether to export this part or drawing document to 3D PDF."""
        return self._instance.ExportAs3D

    @export_as_d.setter
    def export_as_d(self, value):
        """Gets or sets whether to export this part or drawing document to 3D PDF."""
        self._instance.ExportAs3D = value

    @property
    def view_pdf_after_saving(self):
        """Gets or sets whether to view the PDF file to which a part or drawing is saved."""
        return self._instance.ViewPdfAfterSaving

    @view_pdf_after_saving.setter
    def view_pdf_after_saving(self, value):
        """Gets or sets whether to view the PDF file to which a part or drawing is saved."""
        self._instance.ViewPdfAfterSaving = value

    def get_sheets(self):
        """Gets the drawing sheets to export."""
        # return self._instance.GetSheets todo ISheets
        raise NotImplemented

    def get_which_sheets(self):
        """Gets the drawing sheets to export to PDF."""
        # return self._instance.GetWhichSheets
        raise NotImplemented

    def set_sheets(self, which, sheets):
        """
        Sets the drawing sheets to export.
        :param which: Drawing sheets to export to PDF as defined in swExportDataSheetsToExport_e
        :param sheets: Array of the names of the drawing sheets to export
        """
        # return self._instance.SetSheets(which, sheets)
        raise NotImplemented