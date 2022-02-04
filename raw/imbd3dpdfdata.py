# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.html
class IMBD3DPdfData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def accuracy(self):
		"""Gets or sets the level of accuracy for lossy compression when publishing to SOLIDWORKS MBD 3D PDF."""
		return self._instance.Accuracy

	@accuracy.setter
	def accuracy(self, value):
		"""Gets or sets the level of accuracy for lossy compression when publishing to SOLIDWORKS MBD 3D PDF."""
		self._instance.Accuracy = value

	@property
	def compress_lossy_tessellation(self):
		"""Gets or sets whether to apply lossy compression to polygons in the model when publishing to SOLIDWORKS MBD 3D PDF."""
		return self._instance.CompressLossyTessellation

	@compress_lossy_tessellation.setter
	def compress_lossy_tessellation(self, value):
		"""Gets or sets whether to apply lossy compression to polygons in the model when publishing to SOLIDWORKS MBD 3D PDF."""
		self._instance.CompressLossyTessellation = value

	@property
	def create_attach_s_t_e_p(self):
		"""Gets or sets whether to export SOLIDWORKS parts and assemblies to STEP 242 format and attach the STEP 242 file to the SOLIDWORKS MBD 3D PDF."""
		return self._instance.CreateAttachSTEP242

	@create_attach_s_t_e_p.setter
	def create_attach_s_t_e_p(self, value):
		"""Gets or sets whether to export SOLIDWORKS parts and assemblies to STEP 242 format and attach the STEP 242 file to the SOLIDWORKS MBD 3D PDF."""
		self._instance.CreateAttachSTEP242 = value

	@property
	def exclude_from_annotation_view(self):
		"""Gets or sets whether to exclude BOM tables from annotation views for this SOLIDWORKS MBD 3D PDF."""
		return self._instance.ExcludeFromAnnotationView

	@exclude_from_annotation_view.setter
	def exclude_from_annotation_view(self, value):
		"""Gets or sets whether to exclude BOM tables from annotation views for this SOLIDWORKS MBD 3D PDF."""
		self._instance.ExcludeFromAnnotationView = value

	@property
	def file_path(self):
		"""Gets or sets the path and file name to which to save this SOLIDWORKS MBD 3D PDF."""
		return self._instance.FilePath

	@file_path.setter
	def file_path(self, value):
		"""Gets or sets the path and file name to which to save this SOLIDWORKS MBD 3D PDF."""
		self._instance.FilePath = value

	@property
	def theme_name(self):
		"""Gets or sets the path and file name of the theme for this SOLIDWORKS MBD 3D PDF."""
		return self._instance.ThemeName

	@theme_name.setter
	def theme_name(self, value):
		"""Gets or sets the path and file name of the theme for this SOLIDWORKS MBD 3D PDF."""
		self._instance.ThemeName = value

	@property
	def view_pdf_after_saving(self):
		"""Gets or sets whether to display this SOLIDWORKS MBD 3D PDF after publishing it."""
		return self._instance.ViewPdfAfterSaving

	@view_pdf_after_saving.setter
	def view_pdf_after_saving(self, value):
		"""Gets or sets whether to display this SOLIDWORKS MBD 3D PDF after publishing it."""
		self._instance.ViewPdfAfterSaving = value

	@property
	def get_attachments(self):
		"""Gets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF."""
		return self._instance.GetAttachments

	@get_attachments.setter
	def get_attachments(self, value):
		"""Gets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF."""
		self._instance.GetAttachments = value

	@property
	def get_bom_area_count(self):
		"""Gets the number of BOM Table Areas defined in the theme for this SOLIDWORKS MBD 3D PDF."""
		return self._instance.GetBomAreaCount

	@get_bom_area_count.setter
	def get_bom_area_count(self, value):
		"""Gets the number of BOM Table Areas defined in the theme for this SOLIDWORKS MBD 3D PDF."""
		self._instance.GetBomAreaCount = value

	@property
	def get_imported_notes(self):
		"""Gets the imported note names from the theme of this MBD3DPdfData."""
		return self._instance.GetImportedNotes

	@get_imported_notes.setter
	def get_imported_notes(self, value):
		"""Gets the imported note names from the theme of this MBD3DPdfData."""
		self._instance.GetImportedNotes = value

	@property
	def get_more_views(self):
		"""Gets the names of the custom views (i.e., named views and 3D views) in the model for this SOLIDWORKS MBD 3D PDF."""
		return self._instance.GetMoreViews

	@get_more_views.setter
	def get_more_views(self, value):
		"""Gets the names of the custom views (i.e., named views and 3D views) in the model for this SOLIDWORKS MBD 3D PDF."""
		self._instance.GetMoreViews = value

	@property
	def get_standard_views(self):
		"""Gets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF."""
		return self._instance.GetStandardViews

	@get_standard_views.setter
	def get_standard_views(self, value):
		"""Gets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF."""
		self._instance.GetStandardViews = value

	@property
	def get_text_and_custom_properties(self):
		"""Gets the text and custom properties in the theme for this SOLIDWORKS MBD 3D PDF."""
		return self._instance.GetTextAndCustomProperties

	@get_text_and_custom_properties.setter
	def get_text_and_custom_properties(self, value):
		"""Gets the text and custom properties in the theme for this SOLIDWORKS MBD 3D PDF."""
		self._instance.GetTextAndCustomProperties = value

	@property
	def set_attachments(self):
		"""Sets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF."""
		return self._instance.SetAttachments

	@set_attachments.setter
	def set_attachments(self, value):
		"""Sets the fully qualified paths of the files to include as attachments when publishing to SOLIDWORKS MBD 3D PDF."""
		self._instance.SetAttachments = value

	@property
	def set_bom_table(self):
		"""Maps a BOM Table Area in the theme with a BOM table in the model and sets the columns in the BOM table to export to the BOM Table Area in a SOLIDWORKS MBD 3D PDF."""
		return self._instance.SetBomTable

	@set_bom_table.setter
	def set_bom_table(self, value):
		"""Maps a BOM Table Area in the theme with a BOM table in the model and sets the columns in the BOM table to export to the BOM Table Area in a SOLIDWORKS MBD 3D PDF."""
		self._instance.SetBomTable = value

	@property
	def set_imported_note(self):
		"""Sets the specified imported note."""
		return self._instance.SetImportedNote

	@set_imported_note.setter
	def set_imported_note(self, value):
		"""Sets the specified imported note."""
		self._instance.SetImportedNote = value

	@property
	def set_independent_view_port(self):
		"""Sets the specified view for an independent viewport for the SOLIDWORKS MBD 3D PDF."""
		return self._instance.SetIndependentViewPort

	@set_independent_view_port.setter
	def set_independent_view_port(self, value):
		"""Sets the specified view for an independent viewport for the SOLIDWORKS MBD 3D PDF."""
		self._instance.SetIndependentViewPort = value

	@property
	def set_more_views(self):
		"""Sets the names of the custom views (i.e., named views and 3D views) in the model for this SOLIDWORKS MBD 3D PDF."""
		return self._instance.SetMoreViews

	@set_more_views.setter
	def set_more_views(self, value):
		"""Sets the names of the custom views (i.e., named views and 3D views) in the model for this SOLIDWORKS MBD 3D PDF."""
		self._instance.SetMoreViews = value

	@property
	def set_standard_views(self):
		"""Sets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF."""
		return self._instance.SetStandardViews

	@set_standard_views.setter
	def set_standard_views(self, value):
		"""Sets the types of standard views in the model for this SOLIDWORKS MBD 3D PDF."""
		self._instance.SetStandardViews = value

