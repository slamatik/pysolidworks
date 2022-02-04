# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.html
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

	@property
	def get_sheets(self):
		"""Gets the drawing sheets to export."""
		return self._instance.GetSheets

	@get_sheets.setter
	def get_sheets(self, value):
		"""Gets the drawing sheets to export."""
		self._instance.GetSheets = value

	@property
	def get_which_sheets(self):
		"""Gets the drawing sheets to export to PDF."""
		return self._instance.GetWhichSheets

	@get_which_sheets.setter
	def get_which_sheets(self, value):
		"""Gets the drawing sheets to export to PDF."""
		self._instance.GetWhichSheets = value

	@property
	def set_sheets(self):
		"""Sets the drawing sheets to export."""
		return self._instance.SetSheets

	@set_sheets.setter
	def set_sheets(self, value):
		"""Sets the drawing sheets to export."""
		self._instance.SetSheets = value

