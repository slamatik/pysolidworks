# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.html
class IPrintSpecification:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def collate(self):
		"""Gets or sets whether to collate the pages in multiple copies of this document."""
		return self._instance.Collate

	@collate.setter
	def collate(self, value):
		"""Gets or sets whether to collate the pages in multiple copies of this document."""
		self._instance.Collate = value

	@property
	def convert_to_high_quality(self):
		"""Gets or sets whether to convert draft quality drawing views to high quality."""
		return self._instance.ConvertToHighQuality

	@convert_to_high_quality.setter
	def convert_to_high_quality(self, value):
		"""Gets or sets whether to convert draft quality drawing views to high quality."""
		self._instance.ConvertToHighQuality = value

	@property
	def current_sheet(self):
		"""Gets the index of the current sheet."""
		return self._instance.CurrentSheet

	@current_sheet.setter
	def current_sheet(self, value):
		"""Gets the index of the current sheet."""
		self._instance.CurrentSheet = value

	@property
	def from_scale(self):
		"""Gets or sets the custom "from" scale factor for the current drawing sheet."""
		return self._instance.FromScale

	@from_scale.setter
	def from_scale(self, value):
		"""Gets or sets the custom "from" scale factor for the current drawing sheet."""
		self._instance.FromScale = value

	@property
	def number_of_copies(self):
		"""Gets or sets the number of copies to print."""
		return self._instance.NumberOfCopies

	@number_of_copies.setter
	def number_of_copies(self, value):
		"""Gets or sets the number of copies to print."""
		self._instance.NumberOfCopies = value

	@property
	def print_background(self):
		"""Gets or sets whether to print the background."""
		return self._instance.PrintBackground

	@print_background.setter
	def print_background(self, value):
		"""Gets or sets whether to print the background."""
		self._instance.PrintBackground = value

	@property
	def print_cross_hatch_on_out_of_date_views(self):
		"""Gets or sets whether to print a cross hatch on out-of-date views."""
		return self._instance.PrintCrossHatchOnOutOfDateViews

	@print_cross_hatch_on_out_of_date_views.setter
	def print_cross_hatch_on_out_of_date_views(self, value):
		"""Gets or sets whether to print a cross hatch on out-of-date views."""
		self._instance.PrintCrossHatchOnOutOfDateViews = value

	@property
	def printer_queue(self):
		"""Gets or sets the printer to use."""
		return self._instance.PrinterQueue

	@printer_queue.setter
	def printer_queue(self, value):
		"""Gets or sets the printer to use."""
		self._instance.PrinterQueue = value

	@property
	def print_file(self):
		"""Gets or sets the path and file name to which to print the document."""
		return self._instance.PrintFile

	@print_file.setter
	def print_file(self, value):
		"""Gets or sets the path and file name to which to print the document."""
		self._instance.PrintFile = value

	@property
	def print_range(self):
		"""Gets or sets the range of pages to print."""
		return self._instance.PrintRange

	@print_range.setter
	def print_range(self, value):
		"""Gets or sets the range of pages to print."""
		self._instance.PrintRange = value

	@property
	def print_to_file(self):
		"""Gets or sets whether to print to a file."""
		return self._instance.PrintToFile

	@print_to_file.setter
	def print_to_file(self, value):
		"""Gets or sets whether to print to a file."""
		self._instance.PrintToFile = value

	@property
	def print_white_items_black(self):
		"""Gets or sets whether to print white lines and white text in black."""
		return self._instance.PrintWhiteItemsBlack

	@print_white_items_black.setter
	def print_white_items_black(self, value):
		"""Gets or sets whether to print white lines and white text in black."""
		self._instance.PrintWhiteItemsBlack = value

	@property
	def scale_method(self):
		"""Gets or sets the page selection option for printing."""
		return self._instance.ScaleMethod

	@scale_method.setter
	def scale_method(self, value):
		"""Gets or sets the page selection option for printing."""
		self._instance.ScaleMethod = value

	@property
	def sheet_count(self):
		"""Gets the number of sheets in this drawing."""
		return self._instance.SheetCount

	@sheet_count.setter
	def sheet_count(self, value):
		"""Gets the number of sheets in this drawing."""
		self._instance.SheetCount = value

	@property
	def to_scale(self):
		"""Gets or sets the custom "to" scale factor for the current drawing sheet."""
		return self._instance.ToScale

	@to_scale.setter
	def to_scale(self, value):
		"""Gets or sets the custom "to" scale factor for the current drawing sheet."""
		self._instance.ToScale = value

	@property
	def x_origin(self):
		"""Gets or sets the X-coordinate of the print window origin."""
		return self._instance.XOrigin

	@x_origin.setter
	def x_origin(self, value):
		"""Gets or sets the X-coordinate of the print window origin."""
		self._instance.XOrigin = value

	@property
	def y_origin(self):
		"""Gets or sets the Y-coordinate of the print window origin."""
		return self._instance.YOrigin

	@y_origin.setter
	def y_origin(self, value):
		"""Gets or sets the Y-coordinate of the print window origin."""
		self._instance.YOrigin = value

	@property
	def add_print_range(self):
		"""Adds a range of pages to print."""
		return self._instance.AddPrintRange

	@add_print_range.setter
	def add_print_range(self, value):
		"""Adds a range of pages to print."""
		self._instance.AddPrintRange = value

	@property
	def reset_print_range(self):
		"""Resets the print range to the default."""
		return self._instance.ResetPrintRange

	@reset_print_range.setter
	def reset_print_range(self, value):
		"""Resets the print range to the default."""
		self._instance.ResetPrintRange = value

	@property
	def restore_defaults(self):
		"""Restores the default printing options."""
		return self._instance.RestoreDefaults

	@restore_defaults.setter
	def restore_defaults(self, value):
		"""Restores the default printing options."""
		self._instance.RestoreDefaults = value

