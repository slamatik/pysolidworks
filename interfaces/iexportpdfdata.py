class IExportPdfData:
    def __init__(self, parent=None):
        self._instance = parent # tod
    
    @property
    def export_as_3d(self):
        return self._instance.ExportAs3D
    
    @export_as_3d.setter
    def export_as_3d(self, value):
        self._instance.ExportAs3D = value

    @property
    def view_pdf_after_saving(self):
        return self._instance.ViewPdfAfterSaving

    @view_pdf_after_saving.setter
    def view_pdf_after_saving(self, value):
        self._instance.ViewPdfAfterSaving = value

    def get_sheets(self):
        # todo Sheets
        return self._instance.GetSheets

    def get_which_sheets(self):
        return self._instance.GetWhichSheets

    def set_sheets(self, which, sheets):
        return self._instance.SetSheets(which, sheets)