# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportDxfDwgData_members.html
class IImportDxfDwgData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def add_sketch_constraints(self):
		"""Gets or sets whether constraints are added to the geometry in the part sketch after importing the entities."""
		return self._instance.AddSketchConstraints

	@add_sketch_constraints.setter
	def add_sketch_constraints(self, value):
		"""Gets or sets whether constraints are added to the geometry in the part sketch after importing the entities."""
		self._instance.AddSketchConstraints = value

	@property
	def document_template(self):
		"""Gets or sets the filename of the document template."""
		return self._instance.DocumentTemplate

	@document_template.setter
	def document_template(self, value):
		"""Gets or sets the filename of the document template."""
		self._instance.DocumentTemplate = value

	@property
	def ignore_polyline_width(self):
		"""Gets or sets whether to convert width polylines to solid fill hatches when importing to the part sketch."""
		return self._instance.IgnorePolylineWidth

	@ignore_polyline_width.setter
	def ignore_polyline_width(self, value):
		"""Gets or sets whether to convert width polylines to solid fill hatches when importing to the part sketch."""
		self._instance.IgnorePolylineWidth = value

	@property
	def import_dimensions(self):
		"""Gets or sets whether to import dimension into the part sketch."""
		return self._instance.ImportDimensions

	@import_dimensions.setter
	def import_dimensions(self, value):
		"""Gets or sets whether to import dimension into the part sketch."""
		self._instance.ImportDimensions = value

	@property
	def import_hatch(self):
		"""Gets or sets whether to import hatch into this part sketch."""
		return self._instance.ImportHatch

	@import_hatch.setter
	def import_hatch(self, value):
		"""Gets or sets whether to import hatch into this part sketch."""
		self._instance.ImportHatch = value

	@property
	def import_method(self):
		"""Gets or sets whether to import this sheet (layout)."""
		return self._instance.ImportMethod

	@import_method.setter
	def import_method(self, value):
		"""Gets or sets whether to import this sheet (layout)."""
		self._instance.ImportMethod = value

	@property
	def length_unit(self):
		"""Gets or sets the length units for the drawing."""
		return self._instance.LengthUnit

	@length_unit.setter
	def length_unit(self, value):
		"""Gets or sets the length units for the drawing."""
		self._instance.LengthUnit = value

	@property
	def sheet_name(self):
		"""Gets or sets the name of the sheet for the drawing."""
		return self._instance.SheetName

	@sheet_name.setter
	def sheet_name(self, value):
		"""Gets or sets the name of the sheet for the drawing."""
		self._instance.SheetName = value

	@property
	def get_import_layer_to_sheet_format(self):
		"""Gets whether the specified visible layer is imported to the drawing sheet or sheet format."""
		return self._instance.GetImportLayerToSheetFormat

	@get_import_layer_to_sheet_format.setter
	def get_import_layer_to_sheet_format(self, value):
		"""Gets whether the specified visible layer is imported to the drawing sheet or sheet format."""
		self._instance.GetImportLayerToSheetFormat = value

	@property
	def get_import_layer_visibility(self):
		"""Gets whether the specified layer is imported hidden or visible."""
		return self._instance.GetImportLayerVisibility

	@get_import_layer_visibility.setter
	def get_import_layer_visibility(self, value):
		"""Gets whether the specified layer is imported hidden or visible."""
		self._instance.GetImportLayerVisibility = value

	@property
	def get_merge_distance(self):
		"""Gets whether points that are within the specified distance are merged in the part sketch after entities are imported."""
		return self._instance.GetMergeDistance

	@get_merge_distance.setter
	def get_merge_distance(self, value):
		"""Gets whether points that are within the specified distance are merged in the part sketch after entities are imported."""
		self._instance.GetMergeDistance = value

	@property
	def get_merge_points(self):
		"""Gets whether near-identical points are merged in the part sketch after entities are imported."""
		return self._instance.GetMergePoints

	@get_merge_points.setter
	def get_merge_points(self, value):
		"""Gets whether near-identical points are merged in the part sketch after entities are imported."""
		self._instance.GetMergePoints = value

	@property
	def get_paper_size(self):
		"""Gets the size of the paper for the drawing."""
		return self._instance.GetPaperSize

	@get_paper_size.setter
	def get_paper_size(self, value):
		"""Gets the size of the paper for the drawing."""
		self._instance.GetPaperSize = value

	@property
	def get_position(self):
		"""Gets the position of the entities created in the drawing."""
		return self._instance.GetPosition

	@get_position.setter
	def get_position(self, value):
		"""Gets the position of the entities created in the drawing."""
		self._instance.GetPosition = value

	@property
	def get_sheet_scale(self):
		"""Gets the sheet scale for the drawing."""
		return self._instance.GetSheetScale

	@get_sheet_scale.setter
	def get_sheet_scale(self, value):
		"""Gets the sheet scale for the drawing."""
		self._instance.GetSheetScale = value

	@property
	def set_import_layer_to_sheet_format(self):
		"""Sets whether the specified visible layers are imported to the sheet format or drawing sheet."""
		return self._instance.SetImportLayerToSheetFormat

	@set_import_layer_to_sheet_format.setter
	def set_import_layer_to_sheet_format(self, value):
		"""Sets whether the specified visible layers are imported to the sheet format or drawing sheet."""
		self._instance.SetImportLayerToSheetFormat = value

	@property
	def set_import_layer_visibility(self):
		"""Sets whether the specified layers are imported hidden or visible."""
		return self._instance.SetImportLayerVisibility

	@set_import_layer_visibility.setter
	def set_import_layer_visibility(self, value):
		"""Sets whether the specified layers are imported hidden or visible."""
		self._instance.SetImportLayerVisibility = value

	@property
	def set_merge_points(self):
		"""Sets whether near-identical points within the specified distance are merged in the part sketch after entities are imported."""
		return self._instance.SetMergePoints

	@set_merge_points.setter
	def set_merge_points(self, value):
		"""Sets whether near-identical points within the specified distance are merged in the part sketch after entities are imported."""
		self._instance.SetMergePoints = value

	@property
	def set_paper_size(self):
		"""Sets the size of the paper in the drawing."""
		return self._instance.SetPaperSize

	@set_paper_size.setter
	def set_paper_size(self, value):
		"""Sets the size of the paper in the drawing."""
		self._instance.SetPaperSize = value

	@property
	def set_position(self):
		"""Sets the position of the entities created in the drawing."""
		return self._instance.SetPosition

	@set_position.setter
	def set_position(self, value):
		"""Sets the position of the entities created in the drawing."""
		self._instance.SetPosition = value

	@property
	def set_sheet_scale(self):
		"""Sets the sheet scale for the drawing."""
		return self._instance.SetSheetScale

	@set_sheet_scale.setter
	def set_sheet_scale(self, value):
		"""Sets the sheet scale for the drawing."""
		self._instance.SetSheetScale = value

