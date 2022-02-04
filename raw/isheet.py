# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html
class ISheet:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def custom_property_view(self):
		"""Gets or sets the drawing view to use to set the custom information for this drawing sheet."""
		return self._instance.CustomPropertyView

	@custom_property_view.setter
	def custom_property_view(self, value):
		"""Gets or sets the drawing view to use to set the custom information for this drawing sheet."""
		self._instance.CustomPropertyView = value

	@property
	def focus_locked(self):
		"""Gets or sets whether focus is locked on this sheet."""
		return self._instance.FocusLocked

	@focus_locked.setter
	def focus_locked(self, value):
		"""Gets or sets whether focus is locked on this sheet."""
		self._instance.FocusLocked = value

	@property
	def i_page_setup(self):
		"""Gets the page setup for this sheet."""
		return self._instance.IPageSetup

	@i_page_setup.setter
	def i_page_setup(self, value):
		"""Gets the page setup for this sheet."""
		self._instance.IPageSetup = value

	@property
	def page_setup(self):
		"""Gets the page setup for this sheet."""
		return self._instance.PageSetup

	@page_setup.setter
	def page_setup(self, value):
		"""Gets the page setup for this sheet."""
		self._instance.PageSetup = value

	@property
	def revision_table(self):
		"""Gets the revision table annotation for this drawing sheet."""
		return self._instance.RevisionTable

	@revision_table.setter
	def revision_table(self, value):
		"""Gets the revision table annotation for this drawing sheet."""
		self._instance.RevisionTable = value

	@property
	def sheet_format_visible(self):
		"""Gets or sets whether the sheet format is currently visible in this drawing sheet."""
		return self._instance.SheetFormatVisible

	@sheet_format_visible.setter
	def sheet_format_visible(self, value):
		"""Gets or sets whether the sheet format is currently visible in this drawing sheet."""
		self._instance.SheetFormatVisible = value

	@property
	def table_anchor(self):
		"""Gets the specified table anchor."""
		return self._instance.TableAnchor

	@table_anchor.setter
	def table_anchor(self, value):
		"""Gets the specified table anchor."""
		self._instance.TableAnchor = value

	@property
	def title_block(self):
		"""Gets the title block in this sheet."""
		return self._instance.TitleBlock

	@title_block.setter
	def title_block(self, value):
		"""Gets the title block in this sheet."""
		self._instance.TitleBlock = value

	@property
	def get_drawing_zone(self):
		"""Gets the name of the drawing zone for the specified x and y coordinates on the sheet."""
		return self._instance.GetDrawingZone

	@get_drawing_zone.setter
	def get_drawing_zone(self, value):
		"""Gets the name of the drawing zone for the specified x and y coordinates on the sheet."""
		self._instance.GetDrawingZone = value

	@property
	def get_i_d(self):
		"""Gets the ID of this drawing sheet."""
		return self._instance.GetID

	@get_i_d.setter
	def get_i_d(self, value):
		"""Gets the ID of this drawing sheet."""
		self._instance.GetID = value

	@property
	def get_magnetic_lines(self):
		"""Gets the magnetic lines on this drawing sheet."""
		return self._instance.GetMagneticLines

	@get_magnetic_lines.setter
	def get_magnetic_lines(self, value):
		"""Gets the magnetic lines on this drawing sheet."""
		self._instance.GetMagneticLines = value

	@property
	def get_magnetic_lines_count(self):
		"""Gets the number of magnetic lines on this drawing sheet."""
		return self._instance.GetMagneticLinesCount

	@get_magnetic_lines_count.setter
	def get_magnetic_lines_count(self, value):
		"""Gets the number of magnetic lines on this drawing sheet."""
		self._instance.GetMagneticLinesCount = value

	@property
	def get_name(self):
		"""Gets the name of the sheet."""
		return self._instance.GetName

	@get_name.setter
	def get_name(self, value):
		"""Gets the name of the sheet."""
		self._instance.GetName = value

	@property
	def get_properties(self):
		"""Gets the properties for this sheet."""
		return self._instance.GetProperties2

	@get_properties.setter
	def get_properties(self, value):
		"""Gets the properties for this sheet."""
		self._instance.GetProperties2 = value

	@property
	def get_sheet_format_name(self):
		"""Gets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree."""
		return self._instance.GetSheetFormatName

	@get_sheet_format_name.setter
	def get_sheet_format_name(self, value):
		"""Gets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree."""
		self._instance.GetSheetFormatName = value

	@property
	def get_size(self):
		"""Gets the size of the sheet and the corresponding standard sheet size."""
		return self._instance.GetSize

	@get_size.setter
	def get_size(self, value):
		"""Gets the size of the sheet and the corresponding standard sheet size."""
		self._instance.GetSize = value

	@property
	def get_template_name(self):
		"""Gets the name of the template used by this sheet."""
		return self._instance.GetTemplateName

	@get_template_name.setter
	def get_template_name(self, value):
		"""Gets the name of the template used by this sheet."""
		self._instance.GetTemplateName = value

	@property
	def get_template_sketch(self):
		"""Gets the sheet format sketch for this drawing sheet."""
		return self._instance.GetTemplateSketch

	@get_template_sketch.setter
	def get_template_sketch(self, value):
		"""Gets the sheet format sketch for this drawing sheet."""
		self._instance.GetTemplateSketch = value

	@property
	def get_views(self):
		"""Gets the drawing views on this sheet."""
		return self._instance.GetViews

	@get_views.setter
	def get_views(self, value):
		"""Gets the drawing views on this sheet."""
		self._instance.GetViews = value

	@property
	def i_get_magnetic_lines(self):
		"""Gets the magnetic lines on this drawing sheet."""
		return self._instance.IGetMagneticLines

	@i_get_magnetic_lines.setter
	def i_get_magnetic_lines(self, value):
		"""Gets the magnetic lines on this drawing sheet."""
		self._instance.IGetMagneticLines = value

	@property
	def insert_magnetic_line(self):
		"""Inserts a magnetic line at the specified start and end points on this drawing sheet."""
		return self._instance.InsertMagneticLine

	@insert_magnetic_line.setter
	def insert_magnetic_line(self, value):
		"""Inserts a magnetic line at the specified start and end points on this drawing sheet."""
		self._instance.InsertMagneticLine = value

	@property
	def insert_revision_table(self):
		"""Inserts a revision table in this drawing sheet."""
		return self._instance.InsertRevisionTable2

	@insert_revision_table.setter
	def insert_revision_table(self, value):
		"""Inserts a revision table in this drawing sheet."""
		self._instance.InsertRevisionTable2 = value

	@property
	def insert_title_block(self):
		"""Inserts a title block into this drawing sheet."""
		return self._instance.InsertTitleBlock

	@insert_title_block.setter
	def insert_title_block(self, value):
		"""Inserts a title block into this drawing sheet."""
		self._instance.InsertTitleBlock = value

	@property
	def is_loaded(self):
		"""Gets whether this sheet is loaded."""
		return self._instance.IsLoaded

	@is_loaded.setter
	def is_loaded(self, value):
		"""Gets whether this sheet is loaded."""
		self._instance.IsLoaded = value

	@property
	def reload_template(self):
		"""Reloads the sheet format from the original sheet format template."""
		return self._instance.ReloadTemplate

	@reload_template.setter
	def reload_template(self, value):
		"""Reloads the sheet format from the original sheet format template."""
		self._instance.ReloadTemplate = value

	@property
	def save_format(self):
		"""Saves the sheet format in the specified file."""
		return self._instance.SaveFormat

	@save_format.setter
	def save_format(self, value):
		"""Saves the sheet format in the specified file."""
		self._instance.SaveFormat = value

	@property
	def set_as_table_anchor(self):
		"""Sets the anchor for the specified table at a selected point in the sheet format."""
		return self._instance.SetAsTableAnchor

	@set_as_table_anchor.setter
	def set_as_table_anchor(self, value):
		"""Sets the anchor for the specified table at a selected point in the sheet format."""
		self._instance.SetAsTableAnchor = value

	@property
	def set_name(self):
		"""Sets the sheet name."""
		return self._instance.SetName

	@set_name.setter
	def set_name(self, value):
		"""Sets the sheet name."""
		self._instance.SetName = value

	@property
	def set_properties(self):
		"""Sets the properties for this sheet."""
		return self._instance.SetProperties2

	@set_properties.setter
	def set_properties(self, value):
		"""Sets the properties for this sheet."""
		self._instance.SetProperties2 = value

	@property
	def set_scale(self):
		"""Sets the scale for this drawing sheet."""
		return self._instance.SetScale

	@set_scale.setter
	def set_scale(self, value):
		"""Sets the scale for this drawing sheet."""
		self._instance.SetScale = value

	@property
	def set_sheet_format_name(self):
		"""Sets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree."""
		return self._instance.SetSheetFormatName

	@set_sheet_format_name.setter
	def set_sheet_format_name(self, value):
		"""Sets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree."""
		self._instance.SetSheetFormatName = value

	@property
	def set_size(self):
		"""Sets the standard sheet size and the size of the sheet so that the drawing looks correct."""
		return self._instance.SetSize

	@set_size.setter
	def set_size(self, value):
		"""Sets the standard sheet size and the size of the sheet so that the drawing looks correct."""
		self._instance.SetSize = value

	@property
	def set_template_name(self):
		"""Sets the template name for the sheet format."""
		return self._instance.SetTemplateName

	@set_template_name.setter
	def set_template_name(self, value):
		"""Sets the template name for the sheet format."""
		self._instance.SetTemplateName = value

