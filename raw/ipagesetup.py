# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html
class IPageSetup:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def center_footer(self):
		"""Gets or sets the page footer in the center of the page."""
		return self._instance.CenterFooter

	@center_footer.setter
	def center_footer(self, value):
		"""Gets or sets the page footer in the center of the page."""
		self._instance.CenterFooter = value

	@property
	def center_header(self):
		"""Gets or sets the page header in the center of the page."""
		return self._instance.CenterHeader

	@center_header.setter
	def center_header(self, value):
		"""Gets or sets the page header in the center of the page."""
		self._instance.CenterHeader = value

	@property
	def drawing_color(self):
		"""Sets the color of the drawing for printing."""
		return self._instance.DrawingColor

	@drawing_color.setter
	def drawing_color(self, value):
		"""Sets the color of the drawing for printing."""
		self._instance.DrawingColor = value

	@property
	def footer_text_format(self):
		"""Gets or sets the text format for the page footer."""
		return self._instance.FooterTextFormat

	@footer_text_format.setter
	def footer_text_format(self, value):
		"""Gets or sets the text format for the page footer."""
		self._instance.FooterTextFormat = value

	@property
	def header_text_format(self):
		"""Gets or sets the text format for the page header."""
		return self._instance.HeaderTextFormat

	@header_text_format.setter
	def header_text_format(self, value):
		"""Gets or sets the text format for the page header."""
		self._instance.HeaderTextFormat = value

	@property
	def high_quality(self):
		"""Gets or sets whether to print a drawing in high quality."""
		return self._instance.HighQuality

	@high_quality.setter
	def high_quality(self, value):
		"""Gets or sets whether to print a drawing in high quality."""
		self._instance.HighQuality = value

	@property
	def left_footer(self):
		"""Gets or sets the page footer on the left side of the page."""
		return self._instance.LeftFooter

	@left_footer.setter
	def left_footer(self, value):
		"""Gets or sets the page footer on the left side of the page."""
		self._instance.LeftFooter = value

	@property
	def left_header(self):
		"""Gets or sets the page header on the left side of the page."""
		return self._instance.LeftHeader

	@left_header.setter
	def left_header(self, value):
		"""Gets or sets the page header on the left side of the page."""
		self._instance.LeftHeader = value

	@property
	def orientation(self):
		"""Gets or sets the page orientation."""
		return self._instance.Orientation

	@orientation.setter
	def orientation(self, value):
		"""Gets or sets the page orientation."""
		self._instance.Orientation = value

	@property
	def printer_paper_length(self):
		"""Gets or sets the user-defined printer paper length for this document or sheet."""
		return self._instance.PrinterPaperLength

	@printer_paper_length.setter
	def printer_paper_length(self, value):
		"""Gets or sets the user-defined printer paper length for this document or sheet."""
		self._instance.PrinterPaperLength = value

	@property
	def printer_paper_size(self):
		"""Gets or sets the printer paper size for this document or sheet."""
		return self._instance.PrinterPaperSize

	@printer_paper_size.setter
	def printer_paper_size(self, value):
		"""Gets or sets the printer paper size for this document or sheet."""
		self._instance.PrinterPaperSize = value

	@property
	def printer_paper_source(self):
		"""Gets or sets the printer paper source for this document or sheet."""
		return self._instance.PrinterPaperSource

	@printer_paper_source.setter
	def printer_paper_source(self, value):
		"""Gets or sets the printer paper source for this document or sheet."""
		self._instance.PrinterPaperSource = value

	@property
	def printer_paper_width(self):
		"""Gets or sets the user-defined printer paper width for this document or sheet."""
		return self._instance.PrinterPaperWidth

	@printer_paper_width.setter
	def printer_paper_width(self, value):
		"""Gets or sets the user-defined printer paper width for this document or sheet."""
		self._instance.PrinterPaperWidth = value

	@property
	def right_footer(self):
		"""Gets or sets the page footer on the right side of the page."""
		return self._instance.RightFooter

	@right_footer.setter
	def right_footer(self, value):
		"""Gets or sets the page footer on the right side of the page."""
		self._instance.RightFooter = value

	@property
	def right_header(self):
		"""Gets or sets the page header on the right side of the page."""
		return self._instance.RightHeader

	@right_header.setter
	def right_header(self, value):
		"""Gets or sets the page header on the right side of the page."""
		self._instance.RightHeader = value

	@property
	def scale(self):
		"""Gets or sets the scale for printing the page."""
		return self._instance.Scale2

	@scale.setter
	def scale(self, value):
		"""Gets or sets the scale for printing the page."""
		self._instance.Scale2 = value

	@property
	def scale_draft_edges(self):
		"""Gets or sets whether to scale draft edges when printing a drawing in high quality."""
		return self._instance.ScaleDraftEdges

	@scale_draft_edges.setter
	def scale_draft_edges(self, value):
		"""Gets or sets whether to scale draft edges when printing a drawing in high quality."""
		self._instance.ScaleDraftEdges = value

	@property
	def scale_to_fit(self):
		"""Enables or disables scaling the page to fit the printer."""
		return self._instance.ScaleToFit

	@scale_to_fit.setter
	def scale_to_fit(self, value):
		"""Enables or disables scaling the page to fit the printer."""
		self._instance.ScaleToFit = value

	@property
	def get_header_footer_string(self):
		"""Gets the specified standard string that can be used in headers and footers."""
		return self._instance.GetHeaderFooterString

	@get_header_footer_string.setter
	def get_header_footer_string(self, value):
		"""Gets the specified standard string that can be used in headers and footers."""
		self._instance.GetHeaderFooterString = value

	@property
	def get_resolution(self):
		"""Gets the current printer resolution on documents and drawing sheets."""
		return self._instance.GetResolution

	@get_resolution.setter
	def get_resolution(self, value):
		"""Gets the current printer resolution on documents and drawing sheets."""
		self._instance.GetResolution = value

	@property
	def get_use_default_resolution(self):
		"""Gets whether the printer default resolution is in use on documents and drawing sheets."""
		return self._instance.GetUseDefaultResolution

	@get_use_default_resolution.setter
	def get_use_default_resolution(self, value):
		"""Gets whether the printer default resolution is in use on documents and drawing sheets."""
		self._instance.GetUseDefaultResolution = value

	@property
	def set_footer(self):
		"""Sets the entire page footer."""
		return self._instance.SetFooter

	@set_footer.setter
	def set_footer(self, value):
		"""Sets the entire page footer."""
		self._instance.SetFooter = value

	@property
	def set_header(self):
		"""Sets the entire page header."""
		return self._instance.SetHeader

	@set_header.setter
	def set_header(self, value):
		"""Sets the entire page header."""
		self._instance.SetHeader = value

	@property
	def set_resolution(self):
		"""Sets the current printer resolution on documents and drawing sheets."""
		return self._instance.SetResolution

	@set_resolution.setter
	def set_resolution(self, value):
		"""Sets the current printer resolution on documents and drawing sheets."""
		self._instance.SetResolution = value

