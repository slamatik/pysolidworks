# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html
class IView:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the rotation angle of the view."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the rotation angle of the view."""
		self._instance.Angle = value

	@property
	def bodies(self):
		"""Gets or sets the bodies of a multibody part to show in the drawing view."""
		return self._instance.Bodies

	@bodies.setter
	def bodies(self, value):
		"""Gets or sets the bodies of a multibody part to show in the drawing view."""
		self._instance.Bodies = value

	@property
	def break_line_gap(self):
		"""Gets or sets the width of the gap for a break line."""
		return self._instance.BreakLineGap

	@break_line_gap.setter
	def break_line_gap(self, value):
		"""Gets or sets the width of the gap for a break line."""
		self._instance.BreakLineGap = value

	@property
	def crop_view_jagged_outline(self):
		"""Gets or sets whether to use a jagged outline in this cropped drawing view."""
		return self._instance.CropViewJaggedOutline

	@crop_view_jagged_outline.setter
	def crop_view_jagged_outline(self, value):
		"""Gets or sets whether to use a jagged outline in this cropped drawing view."""
		self._instance.CropViewJaggedOutline = value

	@property
	def crop_view_jagged_shape_intensity(self):
		"""Gets or sets the shape intensity of the jagged outline in this cropped drawing view."""
		return self._instance.CropViewJaggedShapeIntensity

	@crop_view_jagged_shape_intensity.setter
	def crop_view_jagged_shape_intensity(self, value):
		"""Gets or sets the shape intensity of the jagged outline in this cropped drawing view."""
		self._instance.CropViewJaggedShapeIntensity = value

	@property
	def crop_view_no_outline(self):
		"""Gets or sets whether to show an outline in this cropped drawing view."""
		return self._instance.CropViewNoOutline

	@crop_view_no_outline.setter
	def crop_view_no_outline(self, value):
		"""Gets or sets whether to show an outline in this cropped drawing view."""
		self._instance.CropViewNoOutline = value

	@property
	def disable_auto_update(self):
		"""Gets or sets whether to disable the automatic update of this view."""
		return self._instance.DisableAutoUpdate

	@disable_auto_update.setter
	def disable_auto_update(self, value):
		"""Gets or sets whether to disable the automatic update of this view."""
		self._instance.DisableAutoUpdate = value

	@property
	def display_state(self):
		"""Gets or sets the name of the display state for this drawing view."""
		return self._instance.DisplayState

	@display_state.setter
	def display_state(self, value):
		"""Gets or sets the name of the display state for this drawing view."""
		self._instance.DisplayState = value

	@property
	def emphasize_outline(self):
		"""Gets or sets whether the outlines of section views are emphasized in this drawing view."""
		return self._instance.EmphasizeOutline

	@emphasize_outline.setter
	def emphasize_outline(self, value):
		"""Gets or sets whether the outlines of section views are emphasized in this drawing view."""
		self._instance.EmphasizeOutline = value

	@property
	def flip_view(self):
		"""Gets or sets whether to flip a flat-pattern view of a sheet metal part."""
		return self._instance.FlipView

	@flip_view.setter
	def flip_view(self, value):
		"""Gets or sets whether to flip a flat-pattern view of a sheet metal part."""
		self._instance.FlipView = value

	@property
	def focus_locked(self):
		"""Gets or sets whether or not focus is locked on this view."""
		return self._instance.FocusLocked

	@focus_locked.setter
	def focus_locked(self, value):
		"""Gets or sets whether or not focus is locked on this view."""
		self._instance.FocusLocked = value

	@property
	def hidden_edges(self):
		"""Gets the hidden edges in the drawing view or sets the hidden edges in the drawing view to be visible."""
		return self._instance.HiddenEdges

	@hidden_edges.setter
	def hidden_edges(self, value):
		"""Gets the hidden edges in the drawing view or sets the hidden edges in the drawing view to be visible."""
		self._instance.HiddenEdges = value

	@property
	def i_position(self):
		"""Gets or sets the X and Y location of the model view's geometric center, relative to the drawing sheet origin."""
		return self._instance.IPosition

	@i_position.setter
	def i_position(self, value):
		"""Gets or sets the X and Y location of the model view's geometric center, relative to the drawing sheet origin."""
		self._instance.IPosition = value

	@property
	def i_scale_ratio(self):
		"""Gets or sets the scale of the drawing view, returning the results in ratio format (n:n)."""
		return self._instance.IScaleRatio

	@i_scale_ratio.setter
	def i_scale_ratio(self, value):
		"""Gets or sets the scale of the drawing view, returning the results in ratio format (n:n)."""
		self._instance.IScaleRatio = value

	@property
	def link_parent_configuration(self):
		"""Gets or sets whether to link a projected or auxiliary view with the parent configuration."""
		return self._instance.LinkParentConfiguration

	@link_parent_configuration.setter
	def link_parent_configuration(self, value):
		"""Gets or sets whether to link a projected or auxiliary view with the parent configuration."""
		self._instance.LinkParentConfiguration = value

	@property
	def model_to_view_transform(self):
		"""Gets the math transform to go from model to drawing view space.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.ModelToViewTransform

	@model_to_view_transform.setter
	def model_to_view_transform(self, value):
		"""Gets the math transform to go from model to drawing view space.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.ModelToViewTransform = value

	@property
	def position(self):
		"""Gets or sets the X and Y location of the model view's geometric center, relative to the drawing sheet origin."""
		return self._instance.Position

	@position.setter
	def position(self, value):
		"""Gets or sets the X and Y location of the model view's geometric center, relative to the drawing sheet origin."""
		self._instance.Position = value

	@property
	def position_locked(self):
		"""Gets or sets whether this drawing view's position is locked."""
		return self._instance.PositionLocked

	@position_locked.setter
	def position_locked(self, value):
		"""Gets or sets whether this drawing view's position is locked."""
		self._instance.PositionLocked = value

	@property
	def projected_dimensions(self):
		"""Gets or sets whether dimensions in this view are true or projected."""
		return self._instance.ProjectedDimensions

	@projected_dimensions.setter
	def projected_dimensions(self, value):
		"""Gets or sets whether dimensions in this view are true or projected."""
		self._instance.ProjectedDimensions = value

	@property
	def referenced_configuration(self):
		"""Gets or sets the configuration referenced by this drawing view."""
		return self._instance.ReferencedConfiguration

	@referenced_configuration.setter
	def referenced_configuration(self, value):
		"""Gets or sets the configuration referenced by this drawing view."""
		self._instance.ReferencedConfiguration = value

	@property
	def referenced_configuration_i_d(self):
		"""Gets the persistent reference ID of the configuration referenced in this drawing view."""
		return self._instance.ReferencedConfigurationID

	@referenced_configuration_i_d.setter
	def referenced_configuration_i_d(self, value):
		"""Gets the persistent reference ID of the configuration referenced in this drawing view."""
		self._instance.ReferencedConfigurationID = value

	@property
	def referenced_document(self):
		"""Gets the document referenced by this drawing view."""
		return self._instance.ReferencedDocument

	@referenced_document.setter
	def referenced_document(self, value):
		"""Gets the document referenced by this drawing view."""
		self._instance.ReferencedDocument = value

	@property
	def root_drawing_component(self):
		"""Gets the root component for this drawing view."""
		return self._instance.RootDrawingComponent

	@root_drawing_component.setter
	def root_drawing_component(self, value):
		"""Gets the root component for this drawing view."""
		self._instance.RootDrawingComponent = value

	@property
	def scale_decimal(self):
		"""Gets or sets the scale of the drawing view, returning the results in decimal format."""
		return self._instance.ScaleDecimal

	@scale_decimal.setter
	def scale_decimal(self, value):
		"""Gets or sets the scale of the drawing view, returning the results in decimal format."""
		self._instance.ScaleDecimal = value

	@property
	def scale_hatch_pattern(self):
		"""Gets or sets whether to scale the hatch pattern to the drawing view."""
		return self._instance.ScaleHatchPattern

	@scale_hatch_pattern.setter
	def scale_hatch_pattern(self, value):
		"""Gets or sets whether to scale the hatch pattern to the drawing view."""
		self._instance.ScaleHatchPattern = value

	@property
	def scale_ratio(self):
		"""Gets or sets the scale of the drawing view, returning the results in ratio format (n:n)."""
		return self._instance.ScaleRatio

	@scale_ratio.setter
	def scale_ratio(self, value):
		"""Gets or sets the scale of the drawing view, returning the results in ratio format (n:n)."""
		self._instance.ScaleRatio = value

	@property
	def sheet(self):
		"""Gets the sheet on which this drawing view exists."""
		return self._instance.Sheet

	@sheet.setter
	def sheet(self, value):
		"""Gets the sheet on which this drawing view exists."""
		self._instance.Sheet = value

	@property
	def show_sheet_metal_bend_notes(self):
		"""Gets or sets whether to show sheet metal bend notes."""
		return self._instance.ShowSheetMetalBendNotes

	@show_sheet_metal_bend_notes.setter
	def show_sheet_metal_bend_notes(self, value):
		"""Gets or sets whether to show sheet metal bend notes."""
		self._instance.ShowSheetMetalBendNotes = value

	@property
	def suppress_state(self):
		"""Gets or sets the view suppress state."""
		return self._instance.SuppressState

	@suppress_state.setter
	def suppress_state(self, value):
		"""Gets or sets the view suppress state."""
		self._instance.SuppressState = value

	@property
	def type(self):
		"""Gets the drawing view type."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the drawing view type."""
		self._instance.Type = value

	@property
	def use_parent_scale(self):
		"""Gets or sets the drawing view's scale to match the parent drawing view's scale."""
		return self._instance.UseParentScale

	@use_parent_scale.setter
	def use_parent_scale(self, value):
		"""Gets or sets the drawing view's scale to match the parent drawing view's scale."""
		self._instance.UseParentScale = value

	@property
	def use_sheet_scale(self):
		"""Gets or sets whether the scale of the drawing view is the same as the scale of the drawing sheet on which this view is located."""
		return self._instance.UseSheetScale

	@use_sheet_scale.setter
	def use_sheet_scale(self, value):
		"""Gets or sets whether the scale of the drawing view is the same as the scale of the drawing sheet on which this view is located."""
		self._instance.UseSheetScale = value

	@property
	def align_drawing_view(self):
		"""Specifies the alignment of this auxiliary drawing view."""
		return self._instance.AlignDrawingView

	@align_drawing_view.setter
	def align_drawing_view(self, value):
		"""Specifies the alignment of this auxiliary drawing view."""
		self._instance.AlignDrawingView = value

	@property
	def align_with_view(self):
		"""Sets view alignment."""
		return self._instance.AlignWithView

	@align_with_view.setter
	def align_with_view(self, value):
		"""Sets view alignment."""
		self._instance.AlignWithView = value

	@property
	def auto_insert_center_marks(self):
		"""Automatically inserts the specified center marks in this view."""
		return self._instance.AutoInsertCenterMarks2

	@auto_insert_center_marks.setter
	def auto_insert_center_marks(self, value):
		"""Automatically inserts the specified center marks in this view."""
		self._instance.AutoInsertCenterMarks2 = value

	@property
	def crop(self):
		"""Crops this view using the selected closed sketch profile."""
		return self._instance.Crop2

	@crop.setter
	def crop(self, value):
		"""Crops this view using the selected closed sketch profile."""
		self._instance.Crop2 = value

	@property
	def enum_hidden_components(self):
		"""Gets the hidden components enumeration in this drawing view."""
		return self._instance.EnumHiddenComponents2

	@enum_hidden_components.setter
	def enum_hidden_components(self, value):
		"""Gets the hidden components enumeration in this drawing view."""
		self._instance.EnumHiddenComponents2 = value

	@property
	def enum_section_lines(self):
		"""Gets the section lines enumeration in the view."""
		return self._instance.EnumSectionLines

	@enum_section_lines.setter
	def enum_section_lines(self, value):
		"""Gets the section lines enumeration in the view."""
		self._instance.EnumSectionLines = value

	@property
	def get_alignment(self):
		"""Gets the alignment information of this view."""
		return self._instance.GetAlignment

	@get_alignment.setter
	def get_alignment(self, value):
		"""Gets the alignment information of this view."""
		self._instance.GetAlignment = value

	@property
	def get_annotation_count(self):
		"""Gets the number of annotations in this view."""
		return self._instance.GetAnnotationCount

	@get_annotation_count.setter
	def get_annotation_count(self, value):
		"""Gets the number of annotations in this view."""
		self._instance.GetAnnotationCount = value

	@property
	def get_annotations(self):
		"""Gets the annotations in this view."""
		return self._instance.GetAnnotations

	@get_annotations.setter
	def get_annotations(self, value):
		"""Gets the annotations in this view."""
		self._instance.GetAnnotations = value

	@property
	def get_arc_count(self):
		"""Gets the number of arcs in this view."""
		return self._instance.GetArcCount

	@get_arc_count.setter
	def get_arc_count(self, value):
		"""Gets the number of arcs in this view."""
		self._instance.GetArcCount = value

	@property
	def get_arcs(self):
		"""Gets all of the information for all of the arcs added by a user in this drawing view."""
		return self._instance.GetArcs4

	@get_arcs.setter
	def get_arcs(self, value):
		"""Gets all of the information for all of the arcs added by a user in this drawing view."""
		self._instance.GetArcs4 = value

	@property
	def get_base_view(self):
		"""Gets the base (parent) view used to create this view."""
		return self._instance.GetBaseView

	@get_base_view.setter
	def get_base_view(self, value):
		"""Gets the base (parent) view used to create this view."""
		self._instance.GetBaseView = value

	@property
	def get_bend_line_count(self):
		"""Gets the number of bendlines in a flat-pattern drawing view."""
		return self._instance.GetBendLineCount

	@get_bend_line_count.setter
	def get_bend_line_count(self, value):
		"""Gets the number of bendlines in a flat-pattern drawing view."""
		self._instance.GetBendLineCount = value

	@property
	def get_bend_lines(self):
		"""Gets the bendlines in a flat-pattern drawing view."""
		return self._instance.GetBendLines

	@get_bend_lines.setter
	def get_bend_lines(self, value):
		"""Gets the bendlines in a flat-pattern drawing view."""
		self._instance.GetBendLines = value

	@property
	def get_bend_note_attribute_string(self):
		"""Gets the internal string that is used to format the text of the specified bend note attribute in this drawing view of a sheet metal part."""
		return self._instance.GetBendNoteAttributeString

	@get_bend_note_attribute_string.setter
	def get_bend_note_attribute_string(self, value):
		"""Gets the internal string that is used to format the text of the specified bend note attribute in this drawing view of a sheet metal part."""
		self._instance.GetBendNoteAttributeString = value

	@property
	def get_bend_note_text_format(self):
		"""Gets the text format of all bend notes in this drawing view of a sheet metal part."""
		return self._instance.GetBendNoteTextFormat

	@get_bend_note_text_format.setter
	def get_bend_note_text_format(self, value):
		"""Gets the text format of all bend notes in this drawing view of a sheet metal part."""
		self._instance.GetBendNoteTextFormat = value

	@property
	def get_bodies_count(self):
		"""Gets the number of bodies of a multibody part in the drawing view."""
		return self._instance.GetBodiesCount

	@get_bodies_count.setter
	def get_bodies_count(self, value):
		"""Gets the number of bodies of a multibody part in the drawing view."""
		self._instance.GetBodiesCount = value

	@property
	def get_bom_table(self):
		"""Gets the BOM table found in this drawing view."""
		return self._instance.GetBomTable

	@get_bom_table.setter
	def get_bom_table(self, value):
		"""Gets the BOM table found in this drawing view."""
		self._instance.GetBomTable = value

	@property
	def get_break_line_count(self):
		"""Gets the number of breaks lines and breaks in this view."""
		return self._instance.GetBreakLineCount2

	@get_break_line_count.setter
	def get_break_line_count(self, value):
		"""Gets the number of breaks lines and breaks in this view."""
		self._instance.GetBreakLineCount2 = value

	@property
	def get_break_line_info(self):
		"""Gets information for all of the break lines in this view."""
		return self._instance.GetBreakLineInfo2

	@get_break_line_info.setter
	def get_break_line_info(self, value):
		"""Gets information for all of the break lines in this view."""
		self._instance.GetBreakLineInfo2 = value

	@property
	def get_break_lines(self):
		"""Gets the all of the breaks in this view."""
		return self._instance.GetBreakLines

	@get_break_lines.setter
	def get_break_lines(self, value):
		"""Gets the all of the breaks in this view."""
		self._instance.GetBreakLines = value

	@property
	def get_break_out_section_count(self):
		"""Gets the number of broken-out sections in this view."""
		return self._instance.GetBreakOutSectionCount

	@get_break_out_section_count.setter
	def get_break_out_section_count(self, value):
		"""Gets the number of broken-out sections in this view."""
		self._instance.GetBreakOutSectionCount = value

	@property
	def get_break_out_sections(self):
		"""Gets all of the broken-out sections in this view."""
		return self._instance.GetBreakOutSections

	@get_break_out_sections.setter
	def get_break_out_sections(self, value):
		"""Gets all of the broken-out sections in this view."""
		self._instance.GetBreakOutSections = value

	@property
	def get_center_line_count(self):
		"""Gets the number of centerlines on this drawing view."""
		return self._instance.GetCenterLineCount

	@get_center_line_count.setter
	def get_center_line_count(self, value):
		"""Gets the number of centerlines on this drawing view."""
		self._instance.GetCenterLineCount = value

	@property
	def get_center_lines(self):
		"""Gets all of the centerline annotations on this drawing view."""
		return self._instance.GetCenterLines

	@get_center_lines.setter
	def get_center_lines(self, value):
		"""Gets all of the centerline annotations on this drawing view."""
		self._instance.GetCenterLines = value

	@property
	def get_center_line_sketch(self):
		"""Gets the sketch that contains all of the centerline information for this view."""
		return self._instance.GetCenterLineSketch

	@get_center_line_sketch.setter
	def get_center_line_sketch(self, value):
		"""Gets the sketch that contains all of the centerline information for this view."""
		self._instance.GetCenterLineSketch = value

	@property
	def get_center_mark_count(self):
		"""Gets the number of center marks that are features in the view."""
		return self._instance.GetCenterMarkCount2

	@get_center_mark_count.setter
	def get_center_mark_count(self, value):
		"""Gets the number of center marks that are features in the view."""
		self._instance.GetCenterMarkCount2 = value

	@property
	def get_center_mark_info(self):
		"""Gets information about each center mark that is a feature in the view."""
		return self._instance.GetCenterMarkInfo

	@get_center_mark_info.setter
	def get_center_mark_info(self, value):
		"""Gets information about each center mark that is a feature in the view."""
		self._instance.GetCenterMarkInfo = value

	@property
	def get_center_marks(self):
		"""Gets all of the center marks that are features in the view."""
		return self._instance.GetCenterMarks

	@get_center_marks.setter
	def get_center_marks(self, value):
		"""Gets all of the center marks that are features in the view."""
		self._instance.GetCenterMarks = value

	@property
	def get_corresponding(self):
		"""Gets the object in this drawing view that corresponds to the specified part or assembly object."""
		return self._instance.GetCorresponding

	@get_corresponding.setter
	def get_corresponding(self, value):
		"""Gets the object in this drawing view that corresponds to the specified part or assembly object."""
		self._instance.GetCorresponding = value

	@property
	def get_corresponding_entity(self):
		"""Gets the entity in this drawing view that corresponds to the specified part or assembly entity."""
		return self._instance.GetCorrespondingEntity

	@get_corresponding_entity.setter
	def get_corresponding_entity(self, value):
		"""Gets the entity in this drawing view that corresponds to the specified part or assembly entity."""
		self._instance.GetCorrespondingEntity = value

	@property
	def get_c_thread_count(self):
		"""Gets the number of cosmetic threads in this drawing view."""
		return self._instance.GetCThreadCount

	@get_c_thread_count.setter
	def get_c_thread_count(self, value):
		"""Gets the number of cosmetic threads in this drawing view."""
		self._instance.GetCThreadCount = value

	@property
	def get_c_thread_quality(self):
		"""Gets the cosmetic thread display quality in this view."""
		return self._instance.GetCThreadQuality

	@get_c_thread_quality.setter
	def get_c_thread_quality(self, value):
		"""Gets the cosmetic thread display quality in this view."""
		self._instance.GetCThreadQuality = value

	@property
	def get_c_threads(self):
		"""Gets all of the cosmetic threads on this drawing view."""
		return self._instance.GetCThreads

	@get_c_threads.setter
	def get_c_threads(self, value):
		"""Gets all of the cosmetic threads on this drawing view."""
		self._instance.GetCThreads = value

	@property
	def get_datum_origin_count(self):
		"""Gets the number of datum origins on this drawing view."""
		return self._instance.GetDatumOriginCount

	@get_datum_origin_count.setter
	def get_datum_origin_count(self, value):
		"""Gets the number of datum origins on this drawing view."""
		self._instance.GetDatumOriginCount = value

	@property
	def get_datum_origins(self):
		"""Gets all of the datum origins on this drawing view."""
		return self._instance.GetDatumOrigins

	@get_datum_origins.setter
	def get_datum_origins(self, value):
		"""Gets all of the datum origins on this drawing view."""
		self._instance.GetDatumOrigins = value

	@property
	def get_datum_points(self):
		"""Gets all of the information about all the datum points in this view."""
		return self._instance.GetDatumPoints2

	@get_datum_points.setter
	def get_datum_points(self, value):
		"""Gets all of the information about all the datum points in this view."""
		self._instance.GetDatumPoints2 = value

	@property
	def get_datum_points_count(self):
		"""Gets the number of datum points in this view."""
		return self._instance.GetDatumPointsCount

	@get_datum_points_count.setter
	def get_datum_points_count(self, value):
		"""Gets the number of datum points in this view."""
		self._instance.GetDatumPointsCount = value

	@property
	def get_datum_tag_count(self):
		"""Gets the number of datum tags on this drawing view."""
		return self._instance.GetDatumTagCount

	@get_datum_tag_count.setter
	def get_datum_tag_count(self, value):
		"""Gets the number of datum tags on this drawing view."""
		self._instance.GetDatumTagCount = value

	@property
	def get_datum_tags(self):
		"""Gets all of the datum tags on this drawing view."""
		return self._instance.GetDatumTags

	@get_datum_tags.setter
	def get_datum_tags(self, value):
		"""Gets all of the datum tags on this drawing view."""
		self._instance.GetDatumTags = value

	@property
	def get_datum_target_sym_count(self):
		"""Gets the number of datum target symbols on this drawing view."""
		return self._instance.GetDatumTargetSymCount

	@get_datum_target_sym_count.setter
	def get_datum_target_sym_count(self, value):
		"""Gets the number of datum target symbols on this drawing view."""
		self._instance.GetDatumTargetSymCount = value

	@property
	def get_datum_target_syms(self):
		"""Gets all of the datum target symbols on this drawing view."""
		return self._instance.GetDatumTargetSyms

	@get_datum_target_syms.setter
	def get_datum_target_syms(self, value):
		"""Gets all of the datum target symbols on this drawing view."""
		self._instance.GetDatumTargetSyms = value

	@property
	def get_dependent_view_count(self):
		"""Gets the number of all, or only the specified, dependent views (i.e., alternate position, detail, section, etc.) in this view."""
		return self._instance.GetDependentViewCount

	@get_dependent_view_count.setter
	def get_dependent_view_count(self, value):
		"""Gets the number of all, or only the specified, dependent views (i.e., alternate position, detail, section, etc.) in this view."""
		self._instance.GetDependentViewCount = value

	@property
	def get_dependent_views(self):
		"""Gets either all, or only the specified, dependent views in this view."""
		return self._instance.GetDependentViews

	@get_dependent_views.setter
	def get_dependent_views(self, value):
		"""Gets either all, or only the specified, dependent views in this view."""
		self._instance.GetDependentViews = value

	@property
	def get_design_table_extent(self):
		"""Gets the size and location of the design table associated with this drawing view."""
		return self._instance.GetDesignTableExtent

	@get_design_table_extent.setter
	def get_design_table_extent(self, value):
		"""Gets the size and location of the design table associated with this drawing view."""
		self._instance.GetDesignTableExtent = value

	@property
	def get_detail(self):
		"""Gets the detail circle for this detail view."""
		return self._instance.GetDetail

	@get_detail.setter
	def get_detail(self, value):
		"""Gets the detail circle for this detail view."""
		self._instance.GetDetail = value

	@property
	def get_detail_circle_count(self):
		"""Gets the number of detail circles in the drawing view."""
		return self._instance.GetDetailCircleCount2

	@get_detail_circle_count.setter
	def get_detail_circle_count(self, value):
		"""Gets the number of detail circles in the drawing view."""
		self._instance.GetDetailCircleCount2 = value

	@property
	def get_detail_circle_info(self):
		"""Gets all of the information about each detail circle in the view."""
		return self._instance.GetDetailCircleInfo2

	@get_detail_circle_info.setter
	def get_detail_circle_info(self, value):
		"""Gets all of the information about each detail circle in the view."""
		self._instance.GetDetailCircleInfo2 = value

	@property
	def get_detail_circles(self):
		"""Gets the detail circles in this view."""
		return self._instance.GetDetailCircles

	@get_detail_circles.setter
	def get_detail_circles(self, value):
		"""Gets the detail circles in this view."""
		self._instance.GetDetailCircles = value

	@property
	def get_detail_circle_strings(self):
		"""Gets an array of strings; each string represents the text label for a detail circle in this view."""
		return self._instance.GetDetailCircleStrings

	@get_detail_circle_strings.setter
	def get_detail_circle_strings(self, value):
		"""Gets an array of strings; each string represents the text label for a detail circle in this view."""
		self._instance.GetDetailCircleStrings = value

	@property
	def get_dimension_count(self):
		"""Gets the number of display dimensions in the current drawing sheet or the current drawing view."""
		return self._instance.GetDimensionCount4

	@get_dimension_count.setter
	def get_dimension_count(self, value):
		"""Gets the number of display dimensions in the current drawing sheet or the current drawing view."""
		self._instance.GetDimensionCount4 = value

	@property
	def get_dimension_display_info(self):
		"""Gets the display dimension information for the current drawing sheet or the current drawing view."""
		return self._instance.GetDimensionDisplayInfo5

	@get_dimension_display_info.setter
	def get_dimension_display_info(self, value):
		"""Gets the display dimension information for the current drawing sheet or the current drawing view."""
		self._instance.GetDimensionDisplayInfo5 = value

	@property
	def get_dimension_display_info_size(self):
		"""Gets the number of  the dimension lines n the current drawing sheet or the current drawing view."""
		return self._instance.GetDimensionDisplayInfoSize2

	@get_dimension_display_info_size.setter
	def get_dimension_display_info_size(self, value):
		"""Gets the number of  the dimension lines n the current drawing sheet or the current drawing view."""
		self._instance.GetDimensionDisplayInfoSize2 = value

	@property
	def get_dimension_display_string(self):
		"""Gets all of the dimension text in the current drawing sheet or the current drawing view."""
		return self._instance.GetDimensionDisplayString4

	@get_dimension_display_string.setter
	def get_dimension_display_string(self, value):
		"""Gets all of the dimension text in the current drawing sheet or the current drawing view."""
		self._instance.GetDimensionDisplayString4 = value

	@property
	def get_dimension_ids(self):
		"""Gets the dimension names from the current drawing sheet or the current drawing view."""
		return self._instance.GetDimensionIds4

	@get_dimension_ids.setter
	def get_dimension_ids(self, value):
		"""Gets the dimension names from the current drawing sheet or the current drawing view."""
		self._instance.GetDimensionIds4 = value

	@property
	def get_dimension_info(self):
		"""Gets all of the dimension information in the current drawing sheet or the current drawing view."""
		return self._instance.GetDimensionInfo6

	@get_dimension_info.setter
	def get_dimension_info(self, value):
		"""Gets all of the dimension information in the current drawing sheet or the current drawing view."""
		self._instance.GetDimensionInfo6 = value

	@property
	def get_dimension_string(self):
		"""Gets the strings containing the text associated with each dimension in the current drawing sheet or the current drawing view."""
		return self._instance.GetDimensionString4

	@get_dimension_string.setter
	def get_dimension_string(self, value):
		"""Gets the strings containing the text associated with each dimension in the current drawing sheet or the current drawing view."""
		self._instance.GetDimensionString4 = value

	@property
	def get_display_data(self):
		"""Gets the the IDisplayData object for this drawing view containing only those model items that are visible in the view."""
		return self._instance.GetDisplayData4

	@get_display_data.setter
	def get_display_data(self, value):
		"""Gets the the IDisplayData object for this drawing view containing only those model items that are visible in the view."""
		self._instance.GetDisplayData4 = value

	@property
	def get_display_dimension_count(self):
		"""Gets the number of display dimensions in this drawing view."""
		return self._instance.GetDisplayDimensionCount

	@get_display_dimension_count.setter
	def get_display_dimension_count(self, value):
		"""Gets the number of display dimensions in this drawing view."""
		self._instance.GetDisplayDimensionCount = value

	@property
	def get_display_dimensions(self):
		"""Gets all of the display dimension on this drawing view."""
		return self._instance.GetDisplayDimensions

	@get_display_dimensions.setter
	def get_display_dimensions(self, value):
		"""Gets all of the display dimension on this drawing view."""
		self._instance.GetDisplayDimensions = value

	@property
	def get_display_edges_in_shaded_mode(self):
		"""Gets whether to display the edges in this when the drawing view is in shaded mode."""
		return self._instance.GetDisplayEdgesInShadedMode

	@get_display_edges_in_shaded_mode.setter
	def get_display_edges_in_shaded_mode(self, value):
		"""Gets whether to display the edges in this when the drawing view is in shaded mode."""
		self._instance.GetDisplayEdgesInShadedMode = value

	@property
	def get_display_mode(self):
		"""Gets the current display mode of the view."""
		return self._instance.GetDisplayMode2

	@get_display_mode.setter
	def get_display_mode(self, value):
		"""Gets the current display mode of the view."""
		self._instance.GetDisplayMode2 = value

	@property
	def get_display_tangent_edges(self):
		"""Gets the current tangent edge display mode of the drawing view."""
		return self._instance.GetDisplayTangentEdges2

	@get_display_tangent_edges.setter
	def get_display_tangent_edges(self, value):
		"""Gets the current tangent edge display mode of the drawing view."""
		self._instance.GetDisplayTangentEdges2 = value

	@property
	def get_dowel_symbol_count(self):
		"""Gets the number of dowel symbols in this drawing view."""
		return self._instance.GetDowelSymbolCount

	@get_dowel_symbol_count.setter
	def get_dowel_symbol_count(self, value):
		"""Gets the number of dowel symbols in this drawing view."""
		self._instance.GetDowelSymbolCount = value

	@property
	def get_dowel_symbols(self):
		"""Gets all of the dowel symbols on this drawing view."""
		return self._instance.GetDowelSymbols

	@get_dowel_symbols.setter
	def get_dowel_symbols(self, value):
		"""Gets all of the dowel symbols on this drawing view."""
		self._instance.GetDowelSymbols = value

	@property
	def get_ellipse_count(self):
		"""Gets the number of ellipses in the view."""
		return self._instance.GetEllipseCount

	@get_ellipse_count.setter
	def get_ellipse_count(self, value):
		"""Gets the number of ellipses in the view."""
		self._instance.GetEllipseCount = value

	@property
	def get_ellipses(self):
		"""Gets all of the ellipses added by a user in this drawing view."""
		return self._instance.GetEllipses5

	@get_ellipses.setter
	def get_ellipses(self, value):
		"""Gets all of the ellipses added by a user in this drawing view."""
		self._instance.GetEllipses5 = value

	@property
	def get_face_hatch_count(self):
		"""Gets the number of face hatches in the view."""
		return self._instance.GetFaceHatchCount

	@get_face_hatch_count.setter
	def get_face_hatch_count(self, value):
		"""Gets the number of face hatches in the view."""
		self._instance.GetFaceHatchCount = value

	@property
	def get_face_hatches(self):
		"""Gets the face hatches in the view."""
		return self._instance.GetFaceHatches

	@get_face_hatches.setter
	def get_face_hatches(self, value):
		"""Gets the face hatches in the view."""
		self._instance.GetFaceHatches = value

	@property
	def get_facetted_hlr_display(self):
		"""Gets whether HLR/HLV (Hidden Lines Removed/Hidden Lines Visible) edges should be displayed faceted in the view."""
		return self._instance.GetFacettedHlrDisplay

	@get_facetted_hlr_display.setter
	def get_facetted_hlr_display(self, value):
		"""Gets whether HLR/HLV (Hidden Lines Removed/Hidden Lines Visible) edges should be displayed faceted in the view."""
		self._instance.GetFacettedHlrDisplay = value

	@property
	def get_first_annotation(self):
		"""Gets the first annotation in this drawing view."""
		return self._instance.GetFirstAnnotation3

	@get_first_annotation.setter
	def get_first_annotation(self, value):
		"""Gets the first annotation in this drawing view."""
		self._instance.GetFirstAnnotation3 = value

	@property
	def get_first_center_line(self):
		"""Gets the first centerline in this view."""
		return self._instance.GetFirstCenterLine

	@get_first_center_line.setter
	def get_first_center_line(self, value):
		"""Gets the first centerline in this view."""
		self._instance.GetFirstCenterLine = value

	@property
	def get_first_center_mark(self):
		"""Gets the first center mark in the view."""
		return self._instance.GetFirstCenterMark

	@get_first_center_mark.setter
	def get_first_center_mark(self, value):
		"""Gets the first center mark in the view."""
		self._instance.GetFirstCenterMark = value

	@property
	def get_first_center_of_mass(self):
		"""Gets the first center of mass in this view."""
		return self._instance.GetFirstCenterOfMass

	@get_first_center_of_mass.setter
	def get_first_center_of_mass(self, value):
		"""Gets the first center of mass in this view."""
		self._instance.GetFirstCenterOfMass = value

	@property
	def get_first_c_thread(self):
		"""Gets the first cosmetic thread in the view."""
		return self._instance.GetFirstCThread

	@get_first_c_thread.setter
	def get_first_c_thread(self, value):
		"""Gets the first cosmetic thread in the view."""
		self._instance.GetFirstCThread = value

	@property
	def get_first_datum_origin(self):
		"""Gets the first datum origin in this drawing view."""
		return self._instance.GetFirstDatumOrigin

	@get_first_datum_origin.setter
	def get_first_datum_origin(self, value):
		"""Gets the first datum origin in this drawing view."""
		self._instance.GetFirstDatumOrigin = value

	@property
	def get_first_datum_tag(self):
		"""Gets the first datum tag in the view."""
		return self._instance.GetFirstDatumTag

	@get_first_datum_tag.setter
	def get_first_datum_tag(self, value):
		"""Gets the first datum tag in the view."""
		self._instance.GetFirstDatumTag = value

	@property
	def get_first_datum_target_sym(self):
		"""Gets the first datum target symbol in the view."""
		return self._instance.GetFirstDatumTargetSym

	@get_first_datum_target_sym.setter
	def get_first_datum_target_sym(self, value):
		"""Gets the first datum target symbol in the view."""
		self._instance.GetFirstDatumTargetSym = value

	@property
	def get_first_display_dimension(self):
		"""Gets the first display dimension in this drawing view."""
		return self._instance.GetFirstDisplayDimension5

	@get_first_display_dimension.setter
	def get_first_display_dimension(self, value):
		"""Gets the first display dimension in this drawing view."""
		self._instance.GetFirstDisplayDimension5 = value

	@property
	def get_first_dowel_symbol(self):
		"""Gets the first dowel symbol in the view."""
		return self._instance.GetFirstDowelSymbol

	@get_first_dowel_symbol.setter
	def get_first_dowel_symbol(self, value):
		"""Gets the first dowel symbol in the view."""
		self._instance.GetFirstDowelSymbol = value

	@property
	def get_first_g_t_o_l(self):
		"""Gets the first geometric tolerance in this view."""
		return self._instance.GetFirstGTOL

	@get_first_g_t_o_l.setter
	def get_first_g_t_o_l(self, value):
		"""Gets the first geometric tolerance in this view."""
		self._instance.GetFirstGTOL = value

	@property
	def get_first_multi_jog_leader(self):
		"""Gets the first multi-jog leader in the view."""
		return self._instance.GetFirstMultiJogLeader

	@get_first_multi_jog_leader.setter
	def get_first_multi_jog_leader(self, value):
		"""Gets the first multi-jog leader in the view."""
		self._instance.GetFirstMultiJogLeader = value

	@property
	def get_first_note(self):
		"""Gets the first note in the view."""
		return self._instance.GetFirstNote

	@get_first_note.setter
	def get_first_note(self, value):
		"""Gets the first note in the view."""
		self._instance.GetFirstNote = value

	@property
	def get_first_revision_cloud(self):
		"""Gets the first revision cloud annotation in this view."""
		return self._instance.GetFirstRevisionCloud

	@get_first_revision_cloud.setter
	def get_first_revision_cloud(self, value):
		"""Gets the first revision cloud annotation in this view."""
		self._instance.GetFirstRevisionCloud = value

	@property
	def get_first_s_f_symbol(self):
		"""Gets the first surface-finish symbols in the view."""
		return self._instance.GetFirstSFSymbol

	@get_first_s_f_symbol.setter
	def get_first_s_f_symbol(self, value):
		"""Gets the first surface-finish symbols in the view."""
		self._instance.GetFirstSFSymbol = value

	@property
	def get_first_table_annotation(self):
		"""Gets the first table annotation in this view."""
		return self._instance.GetFirstTableAnnotation

	@get_first_table_annotation.setter
	def get_first_table_annotation(self, value):
		"""Gets the first table annotation in this view."""
		self._instance.GetFirstTableAnnotation = value

	@property
	def get_first_weld_bead(self):
		"""Gets the first weld bead annotation in this view."""
		return self._instance.GetFirstWeldBead

	@get_first_weld_bead.setter
	def get_first_weld_bead(self, value):
		"""Gets the first weld bead annotation in this view."""
		self._instance.GetFirstWeldBead = value

	@property
	def get_first_weld_symbol(self):
		"""Gets the first weld symbol in the view."""
		return self._instance.GetFirstWeldSymbol

	@get_first_weld_symbol.setter
	def get_first_weld_symbol(self, value):
		"""Gets the first weld symbol in the view."""
		self._instance.GetFirstWeldSymbol = value

	@property
	def get_g_tol_count(self):
		"""Gets the number of geometric tolerances in this drawing view."""
		return self._instance.GetGTolCount

	@get_g_tol_count.setter
	def get_g_tol_count(self, value):
		"""Gets the number of geometric tolerances in this drawing view."""
		self._instance.GetGTolCount = value

	@property
	def get_g_tols(self):
		"""Gets all of the geometric tolerances on this drawing view."""
		return self._instance.GetGTols

	@get_g_tols.setter
	def get_g_tols(self, value):
		"""Gets all of the geometric tolerances on this drawing view."""
		self._instance.GetGTols = value

	@property
	def get_hidden_components(self):
		"""Gets the hidden components in this drawing view."""
		return self._instance.GetHiddenComponents

	@get_hidden_components.setter
	def get_hidden_components(self, value):
		"""Gets the hidden components in this drawing view."""
		self._instance.GetHiddenComponents = value

	@property
	def get_keep_linked_to_b_o_m(self):
		"""Gets whether this drawing view is linked to a BOM or weldment cut-list table."""
		return self._instance.GetKeepLinkedToBOM

	@get_keep_linked_to_b_o_m.setter
	def get_keep_linked_to_b_o_m(self, value):
		"""Gets whether this drawing view is linked to a BOM or weldment cut-list table."""
		self._instance.GetKeepLinkedToBOM = value

	@property
	def get_keep_linked_to_b_o_m_name(self):
		"""Gets the name of the BOM or weldment cut-list table feature to which this drawing view is linked."""
		return self._instance.GetKeepLinkedToBOMName

	@get_keep_linked_to_b_o_m_name.setter
	def get_keep_linked_to_b_o_m_name(self, value):
		"""Gets the name of the BOM or weldment cut-list table feature to which this drawing view is linked."""
		self._instance.GetKeepLinkedToBOMName = value

	@property
	def get_line_count(self):
		"""Gets the number of lines in this view with an option to include or exclude crosshatch lines."""
		return self._instance.GetLineCount2

	@get_line_count.setter
	def get_line_count(self, value):
		"""Gets the number of lines in this view with an option to include or exclude crosshatch lines."""
		self._instance.GetLineCount2 = value

	@property
	def get_lines(self):
		"""Gets all of the lines in the view with an option to include or exclude crosshatch lines."""
		return self._instance.GetLines4

	@get_lines.setter
	def get_lines(self, value):
		"""Gets all of the lines in the view with an option to include or exclude crosshatch lines."""
		self._instance.GetLines4 = value

	@property
	def get_mirror_view_orientation(self):
		"""Gets whether this view is mirrored."""
		return self._instance.GetMirrorViewOrientation

	@get_mirror_view_orientation.setter
	def get_mirror_view_orientation(self, value):
		"""Gets whether this view is mirrored."""
		self._instance.GetMirrorViewOrientation = value

	@property
	def get_multi_jog_leader_count(self):
		"""Gets the number of multi-jog leaders on this drawing view."""
		return self._instance.GetMultiJogLeaderCount

	@get_multi_jog_leader_count.setter
	def get_multi_jog_leader_count(self, value):
		"""Gets the number of multi-jog leaders on this drawing view."""
		self._instance.GetMultiJogLeaderCount = value

	@property
	def get_multi_jog_leaders(self):
		"""Gets all of the multi-jog leaders in this drawing view."""
		return self._instance.GetMultiJogLeaders

	@get_multi_jog_leaders.setter
	def get_multi_jog_leaders(self, value):
		"""Gets all of the multi-jog leaders in this drawing view."""
		self._instance.GetMultiJogLeaders = value

	@property
	def get_name(self):
		"""Gets the name of this drawing view displayed in the FeatureManager design tree."""
		return self._instance.GetName2

	@get_name.setter
	def get_name(self, value):
		"""Gets the name of this drawing view displayed in the FeatureManager design tree."""
		self._instance.GetName2 = value

	@property
	def get_next_view(self):
		"""Gets the next drawing view in the drawing."""
		return self._instance.GetNextView

	@get_next_view.setter
	def get_next_view(self, value):
		"""Gets the next drawing view in the drawing."""
		self._instance.GetNextView = value

	@property
	def get_note_count(self):
		"""Gets the number notes in this drawing view."""
		return self._instance.GetNoteCount

	@get_note_count.setter
	def get_note_count(self, value):
		"""Gets the number notes in this drawing view."""
		self._instance.GetNoteCount = value

	@property
	def get_notes(self):
		"""Gets the notes in this drawing view."""
		return self._instance.GetNotes

	@get_notes.setter
	def get_notes(self, value):
		"""Gets the notes in this drawing view."""
		self._instance.GetNotes = value

	@property
	def get_orientation_name(self):
		"""Gets the predefined name of this view."""
		return self._instance.GetOrientationName

	@get_orientation_name.setter
	def get_orientation_name(self, value):
		"""Gets the predefined name of this view."""
		self._instance.GetOrientationName = value

	@property
	def get_outline(self):
		"""Gets the bounding box for a view (sheet or drawing) in meters on the drawing page."""
		return self._instance.GetOutline

	@get_outline.setter
	def get_outline(self, value):
		"""Gets the bounding box for a view (sheet or drawing) in meters on the drawing page."""
		self._instance.GetOutline = value

	@property
	def get_parabola_count(self):
		"""Gets the number of parabolas in the view."""
		return self._instance.GetParabolaCount

	@get_parabola_count.setter
	def get_parabola_count(self, value):
		"""Gets the number of parabolas in the view."""
		self._instance.GetParabolaCount = value

	@property
	def get_parabolas(self):
		"""Gets all of the information about all of the parabolas in this view."""
		return self._instance.GetParabolas2

	@get_parabolas.setter
	def get_parabolas(self, value):
		"""Gets all of the information about all of the parabolas in this view."""
		self._instance.GetParabolas2 = value

	@property
	def get_poly_line_count(self):
		"""Gets the number of polylines in this view with an option to include or exclude crosshatch lines."""
		return self._instance.GetPolyLineCount5

	@get_poly_line_count.setter
	def get_poly_line_count(self, value):
		"""Gets the number of polylines in this view with an option to include or exclude crosshatch lines."""
		self._instance.GetPolyLineCount5 = value

	@property
	def get_polylines(self):
		"""Gets all of the polylines in the view with an option to include or exclude crosshatch lines."""
		return self._instance.GetPolylines7

	@get_polylines.setter
	def get_polylines(self, value):
		"""Gets all of the polylines in the view with an option to include or exclude crosshatch lines."""
		self._instance.GetPolylines7 = value

	@property
	def get_poly_lines_and_curves(self):
		"""Gets the arcs, ellipses, splines, and polylines in the view with an option to include or exclude crosshatch lines."""
		return self._instance.GetPolyLinesAndCurves

	@get_poly_lines_and_curves.setter
	def get_poly_lines_and_curves(self, value):
		"""Gets the arcs, ellipses, splines, and polylines in the view with an option to include or exclude crosshatch lines."""
		self._instance.GetPolyLinesAndCurves = value

	@property
	def get_poly_lines_and_curves_count(self):
		"""Gets the number of lines, including arcs, ellipses, splines, and polylines, in the view with the option to include or exclude cross hatch  lines."""
		return self._instance.GetPolyLinesAndCurvesCount

	@get_poly_lines_and_curves_count.setter
	def get_poly_lines_and_curves_count(self, value):
		"""Gets the number of lines, including arcs, ellipses, splines, and polylines, in the view with the option to include or exclude cross hatch  lines."""
		self._instance.GetPolyLinesAndCurvesCount = value

	@property
	def get_projection_arrow(self):
		"""Gets the projection arrow for this projected view."""
		return self._instance.GetProjectionArrow

	@get_projection_arrow.setter
	def get_projection_arrow(self, value):
		"""Gets the projection arrow for this projected view."""
		self._instance.GetProjectionArrow = value

	@property
	def get_projection_line_count(self):
		"""Gets the number of projection lines (arrows) in this drawing view."""
		return self._instance.GetProjectionLineCount

	@get_projection_line_count.setter
	def get_projection_line_count(self, value):
		"""Gets the number of projection lines (arrows) in this drawing view."""
		self._instance.GetProjectionLineCount = value

	@property
	def get_projection_lines(self):
		"""Gets the projection lines (arrows) in this drawing view."""
		return self._instance.GetProjectionLines

	@get_projection_lines.setter
	def get_projection_lines(self, value):
		"""Gets the projection lines (arrows) in this drawing view."""
		self._instance.GetProjectionLines = value

	@property
	def get_referenced_model_name(self):
		"""Gets the name of the model that is referenced in the drawing view."""
		return self._instance.GetReferencedModelName

	@get_referenced_model_name.setter
	def get_referenced_model_name(self, value):
		"""Gets the name of the model that is referenced in the drawing view."""
		self._instance.GetReferencedModelName = value

	@property
	def get_related_tangent_edge_count(self):
		"""Gets the number of visible tangent edges for the specified bendline in a flat-pattern drawing view."""
		return self._instance.GetRelatedTangentEdgeCount

	@get_related_tangent_edge_count.setter
	def get_related_tangent_edge_count(self, value):
		"""Gets the number of visible tangent edges for the specified bendline in a flat-pattern drawing view."""
		self._instance.GetRelatedTangentEdgeCount = value

	@property
	def get_related_tangent_edges(self):
		"""Gets the visible tangent edges for the specified bendline in a flat-pattern drawing view."""
		return self._instance.GetRelatedTangentEdges

	@get_related_tangent_edges.setter
	def get_related_tangent_edges(self, value):
		"""Gets the visible tangent edges for the specified bendline in a flat-pattern drawing view."""
		self._instance.GetRelatedTangentEdges = value

	@property
	def get_revision_cloud_count(self):
		"""Gets the number of revision cloud annotations in this view."""
		return self._instance.GetRevisionCloudCount

	@get_revision_cloud_count.setter
	def get_revision_cloud_count(self, value):
		"""Gets the number of revision cloud annotations in this view."""
		self._instance.GetRevisionCloudCount = value

	@property
	def get_revision_clouds(self):
		"""Gets all of the revision cloud annotations in this view."""
		return self._instance.GetRevisionClouds

	@get_revision_clouds.setter
	def get_revision_clouds(self, value):
		"""Gets all of the revision cloud annotations in this view."""
		self._instance.GetRevisionClouds = value

	@property
	def get_section(self):
		"""Gets the section for this section view."""
		return self._instance.GetSection

	@get_section.setter
	def get_section(self, value):
		"""Gets the section for this section view."""
		self._instance.GetSection = value

	@property
	def get_section_line_count(self):
		"""Gets the number of section lines in the view."""
		return self._instance.GetSectionLineCount2

	@get_section_line_count.setter
	def get_section_line_count(self, value):
		"""Gets the number of section lines in the view."""
		self._instance.GetSectionLineCount2 = value

	@property
	def get_section_line_info(self):
		"""Gets all of the information about the section lines in the view."""
		return self._instance.GetSectionLineInfo2

	@get_section_line_info.setter
	def get_section_line_info(self, value):
		"""Gets all of the information about the section lines in the view."""
		self._instance.GetSectionLineInfo2 = value

	@property
	def get_section_lines(self):
		"""Gets the section lines in the view."""
		return self._instance.GetSectionLines

	@get_section_lines.setter
	def get_section_lines(self, value):
		"""Gets the section lines in the view."""
		self._instance.GetSectionLines = value

	@property
	def get_section_line_strings(self):
		"""Gets an array of strings; each string represents the text label for a section line in this view."""
		return self._instance.GetSectionLineStrings

	@get_section_line_strings.setter
	def get_section_line_strings(self, value):
		"""Gets an array of strings; each string represents the text label for a section line in this view."""
		self._instance.GetSectionLineStrings = value

	@property
	def get_s_f_symbol_count(self):
		"""Gets the number of surface finish symbols on this drawing view."""
		return self._instance.GetSFSymbolCount

	@get_s_f_symbol_count.setter
	def get_s_f_symbol_count(self, value):
		"""Gets the number of surface finish symbols on this drawing view."""
		self._instance.GetSFSymbolCount = value

	@property
	def get_s_f_symbols(self):
		"""Gets all of the surface finish symbols in this drawing view."""
		return self._instance.GetSFSymbols

	@get_s_f_symbols.setter
	def get_s_f_symbols(self, value):
		"""Gets all of the surface finish symbols in this drawing view."""
		self._instance.GetSFSymbols = value

	@property
	def get_sketch(self):
		"""Gets the sketch used by this view."""
		return self._instance.GetSketch

	@get_sketch.setter
	def get_sketch(self, value):
		"""Gets the sketch used by this view."""
		self._instance.GetSketch = value

	@property
	def get_sketch_picture_count(self):
		"""Gets the number of sketch pictures imported to this view when a drawing is created from a part."""
		return self._instance.GetSketchPictureCount

	@get_sketch_picture_count.setter
	def get_sketch_picture_count(self, value):
		"""Gets the number of sketch pictures imported to this view when a drawing is created from a part."""
		self._instance.GetSketchPictureCount = value

	@property
	def get_sketch_pictures(self):
		"""Gets all of the sketch pictures imported to this view when a drawing is created from a part."""
		return self._instance.GetSketchPictures

	@get_sketch_pictures.setter
	def get_sketch_pictures(self, value):
		"""Gets all of the sketch pictures imported to this view when a drawing is created from a part."""
		self._instance.GetSketchPictures = value

	@property
	def get_s_m_boundary_box_display_data(self):
		"""Gets the boundary-box sketch display data of a flat-pattern drawing view."""
		return self._instance.GetSMBoundaryBoxDisplayData2

	@get_s_m_boundary_box_display_data.setter
	def get_s_m_boundary_box_display_data(self, value):
		"""Gets the boundary-box sketch display data of a flat-pattern drawing view."""
		self._instance.GetSMBoundaryBoxDisplayData2 = value

	@property
	def get_solid_hatch_count(self):
		"""Gets the number of visible solid-fill hatches in a detail, break, or crop view and the size of the array for their boundary data."""
		return self._instance.GetSolidHatchCount

	@get_solid_hatch_count.setter
	def get_solid_hatch_count(self, value):
		"""Gets the number of visible solid-fill hatches in a detail, break, or crop view and the size of the array for their boundary data."""
		self._instance.GetSolidHatchCount = value

	@property
	def get_solid_hatch_info(self):
		"""Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view."""
		return self._instance.GetSolidHatchInfo

	@get_solid_hatch_info.setter
	def get_solid_hatch_info(self, value):
		"""Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view."""
		self._instance.GetSolidHatchInfo = value

	@property
	def get_spline_count(self):
		"""Gets the number of splines in the view."""
		return self._instance.GetSplineCount

	@get_spline_count.setter
	def get_spline_count(self, value):
		"""Gets the number of splines in the view."""
		self._instance.GetSplineCount = value

	@property
	def get_splines(self):
		"""Gets all of the splines added by a user in the drawing view."""
		return self._instance.GetSplines3

	@get_splines.setter
	def get_splines(self, value):
		"""Gets all of the splines added by a user in the drawing view."""
		self._instance.GetSplines3 = value

	@property
	def get_table_annotation_count(self):
		"""Gets the number of table annotations in this drawing view."""
		return self._instance.GetTableAnnotationCount

	@get_table_annotation_count.setter
	def get_table_annotation_count(self, value):
		"""Gets the number of table annotations in this drawing view."""
		self._instance.GetTableAnnotationCount = value

	@property
	def get_table_annotations(self):
		"""Gets all of the table annotations on this drawing view."""
		return self._instance.GetTableAnnotations

	@get_table_annotations.setter
	def get_table_annotations(self, value):
		"""Gets all of the table annotations on this drawing view."""
		self._instance.GetTableAnnotations = value

	@property
	def get_temporary_axes(self):
		"""Gets the information of the temporary axes displayed in this view."""
		return self._instance.GetTemporaryAxes

	@get_temporary_axes.setter
	def get_temporary_axes(self, value):
		"""Gets the information of the temporary axes displayed in this view."""
		self._instance.GetTemporaryAxes = value

	@property
	def get_temporary_axes_count(self):
		"""Gets the number of temporary axes in this view."""
		return self._instance.GetTemporaryAxesCount

	@get_temporary_axes_count.setter
	def get_temporary_axes_count(self, value):
		"""Gets the number of temporary axes in this view."""
		self._instance.GetTemporaryAxesCount = value

	@property
	def get_unique_name(self):
		"""Gets the unique name of this section view."""
		return self._instance.GetUniqueName

	@get_unique_name.setter
	def get_unique_name(self, value):
		"""Gets the unique name of this section view."""
		self._instance.GetUniqueName = value

	@property
	def get_use_parent_display_mode(self):
		"""Gets whether the view is using its parent settings or if it is using its own local settings."""
		return self._instance.GetUseParentDisplayMode

	@get_use_parent_display_mode.setter
	def get_use_parent_display_mode(self, value):
		"""Gets whether the view is using its parent settings or if it is using its own local settings."""
		self._instance.GetUseParentDisplayMode = value

	@property
	def get_user_points(self):
		"""Gets all of the information about all of the user points in this view."""
		return self._instance.GetUserPoints2

	@get_user_points.setter
	def get_user_points(self, value):
		"""Gets all of the information about all of the user points in this view."""
		self._instance.GetUserPoints2 = value

	@property
	def get_user_points_count(self):
		"""Gets the number of user points in the view."""
		return self._instance.GetUserPointsCount

	@get_user_points_count.setter
	def get_user_points_count(self, value):
		"""Gets the number of user points in the view."""
		self._instance.GetUserPointsCount = value

	@property
	def get_view_xform(self):
		"""Gets the transform from model space origin to drawing space origin."""
		return self._instance.GetViewXform

	@get_view_xform.setter
	def get_view_xform(self, value):
		"""Gets the transform from model space origin to drawing space origin."""
		self._instance.GetViewXform = value

	@property
	def get_visible(self):
		"""Gets the visibility of this drawing view."""
		return self._instance.GetVisible

	@get_visible.setter
	def get_visible(self, value):
		"""Gets the visibility of this drawing view."""
		self._instance.GetVisible = value

	@property
	def get_visible_component_count(self):
		"""Gets the number of visible components in this drawing view."""
		return self._instance.GetVisibleComponentCount

	@get_visible_component_count.setter
	def get_visible_component_count(self, value):
		"""Gets the number of visible components in this drawing view."""
		self._instance.GetVisibleComponentCount = value

	@property
	def get_visible_components(self):
		"""Gets the visible components in this drawing view."""
		return self._instance.GetVisibleComponents

	@get_visible_components.setter
	def get_visible_components(self, value):
		"""Gets the visible components in this drawing view."""
		self._instance.GetVisibleComponents = value

	@property
	def get_visible_drawing_components(self):
		"""Gets all of the unobscured drawing components in this drawing view of an assembly drawing."""
		return self._instance.GetVisibleDrawingComponents

	@get_visible_drawing_components.setter
	def get_visible_drawing_components(self, value):
		"""Gets all of the unobscured drawing components in this drawing view of an assembly drawing."""
		self._instance.GetVisibleDrawingComponents = value

	@property
	def get_visible_entities(self):
		"""Gets the visible entities of the specified type for the specified component in this drawing view."""
		return self._instance.GetVisibleEntities2

	@get_visible_entities.setter
	def get_visible_entities(self, value):
		"""Gets the visible entities of the specified type for the specified component in this drawing view."""
		self._instance.GetVisibleEntities2 = value

	@property
	def get_visible_entity_count(self):
		"""Gets the number of visible entities of the specified type for the specified component in this drawing view."""
		return self._instance.GetVisibleEntityCount2

	@get_visible_entity_count.setter
	def get_visible_entity_count(self, value):
		"""Gets the number of visible entities of the specified type for the specified component in this drawing view."""
		self._instance.GetVisibleEntityCount2 = value

	@property
	def get_weld_bead_count(self):
		"""Gets the number of weld beads on this drawing view."""
		return self._instance.GetWeldBeadCount

	@get_weld_bead_count.setter
	def get_weld_bead_count(self, value):
		"""Gets the number of weld beads on this drawing view."""
		self._instance.GetWeldBeadCount = value

	@property
	def get_weld_beads(self):
		"""Gets all of the weld beads on this drawing view."""
		return self._instance.GetWeldBeads

	@get_weld_beads.setter
	def get_weld_beads(self, value):
		"""Gets all of the weld beads on this drawing view."""
		self._instance.GetWeldBeads = value

	@property
	def get_weld_symbol_count(self):
		"""Gets the number of weld symbols on this drawing view."""
		return self._instance.GetWeldSymbolCount

	@get_weld_symbol_count.setter
	def get_weld_symbol_count(self, value):
		"""Gets the number of weld symbols on this drawing view."""
		self._instance.GetWeldSymbolCount = value

	@property
	def get_weld_symbols(self):
		"""Gets all of the weld symbols on this drawing view."""
		return self._instance.GetWeldSymbols

	@get_weld_symbols.setter
	def get_weld_symbols(self, value):
		"""Gets all of the weld symbols on this drawing view."""
		self._instance.GetWeldSymbols = value

	@property
	def get_witness_entities_count(self):
		"""Gets the number of virtual sharp witness lines in this drawing view."""
		return self._instance.GetWitnessEntitiesCount

	@get_witness_entities_count.setter
	def get_witness_entities_count(self, value):
		"""Gets the number of virtual sharp witness lines in this drawing view."""
		self._instance.GetWitnessEntitiesCount = value

	@property
	def get_witness_geom_info(self):
		"""Gets the geometry data for all of the virtual sharp witness lines in this drawing view."""
		return self._instance.GetWitnessGeomInfo

	@get_witness_geom_info.setter
	def get_witness_geom_info(self, value):
		"""Gets the geometry data for all of the virtual sharp witness lines in this drawing view."""
		self._instance.GetWitnessGeomInfo = value

	@property
	def get_xform(self):
		"""Gets the matrix used for displaying this drawing view."""
		return self._instance.GetXform

	@get_xform.setter
	def get_xform(self, value):
		"""Gets the matrix used for displaying this drawing view."""
		self._instance.GetXform = value

	@property
	def has_design_table(self):
		"""Gets whether this drawing view has a design table associated with it."""
		return self._instance.HasDesignTable

	@has_design_table.setter
	def has_design_table(self, value):
		"""Gets whether this drawing view has a design table associated with it."""
		self._instance.HasDesignTable = value

	@property
	def i_get_annotations(self):
		"""Gets the annotations in this view."""
		return self._instance.IGetAnnotations

	@i_get_annotations.setter
	def i_get_annotations(self, value):
		"""Gets the annotations in this view."""
		self._instance.IGetAnnotations = value

	@property
	def i_get_arcs(self):
		"""Gets all of the information for all of the arcs added by a user in this drawing view."""
		return self._instance.IGetArcs4

	@i_get_arcs.setter
	def i_get_arcs(self, value):
		"""Gets all of the information for all of the arcs added by a user in this drawing view."""
		self._instance.IGetArcs4 = value

	@property
	def i_get_base_view(self):
		"""Gets the base (parent) view used to create this view."""
		return self._instance.IGetBaseView

	@i_get_base_view.setter
	def i_get_base_view(self, value):
		"""Gets the base (parent) view used to create this view."""
		self._instance.IGetBaseView = value

	@property
	def i_get_bend_lines(self):
		"""Gets the bendlines in a flat-pattern drawing view."""
		return self._instance.IGetBendLines

	@i_get_bend_lines.setter
	def i_get_bend_lines(self, value):
		"""Gets the bendlines in a flat-pattern drawing view."""
		self._instance.IGetBendLines = value

	@property
	def i_get_bodies(self):
		"""Gets the bodies of a multibody part in the drawing view."""
		return self._instance.IGetBodies

	@i_get_bodies.setter
	def i_get_bodies(self, value):
		"""Gets the bodies of a multibody part in the drawing view."""
		self._instance.IGetBodies = value

	@property
	def i_get_bom_table(self):
		"""Gets the BOM table found in this drawing view."""
		return self._instance.IGetBomTable

	@i_get_bom_table.setter
	def i_get_bom_table(self, value):
		"""Gets the BOM table found in this drawing view."""
		self._instance.IGetBomTable = value

	@property
	def i_get_break_line_info(self):
		"""Gets information for all of the break lines in this view."""
		return self._instance.IGetBreakLineInfo2

	@i_get_break_line_info.setter
	def i_get_break_line_info(self, value):
		"""Gets information for all of the break lines in this view."""
		self._instance.IGetBreakLineInfo2 = value

	@property
	def i_get_break_lines(self):
		"""Gets the all of the breaks in this view."""
		return self._instance.IGetBreakLines

	@i_get_break_lines.setter
	def i_get_break_lines(self, value):
		"""Gets the all of the breaks in this view."""
		self._instance.IGetBreakLines = value

	@property
	def i_get_break_out_sections(self):
		"""Gets all of the broken-out sections in this view."""
		return self._instance.IGetBreakOutSections

	@i_get_break_out_sections.setter
	def i_get_break_out_sections(self, value):
		"""Gets all of the broken-out sections in this view."""
		self._instance.IGetBreakOutSections = value

	@property
	def i_get_center_lines(self):
		"""Gets all of the centerlines on this drawing view."""
		return self._instance.IGetCenterLines

	@i_get_center_lines.setter
	def i_get_center_lines(self, value):
		"""Gets all of the centerlines on this drawing view."""
		self._instance.IGetCenterLines = value

	@property
	def i_get_center_mark_info(self):
		"""Gets information about each center mark that is a feature in the view."""
		return self._instance.IGetCenterMarkInfo

	@i_get_center_mark_info.setter
	def i_get_center_mark_info(self, value):
		"""Gets information about each center mark that is a feature in the view."""
		self._instance.IGetCenterMarkInfo = value

	@property
	def i_get_center_marks(self):
		"""Gets all of the center marks that are features in the view."""
		return self._instance.IGetCenterMarks

	@i_get_center_marks.setter
	def i_get_center_marks(self, value):
		"""Gets all of the center marks that are features in the view."""
		self._instance.IGetCenterMarks = value

	@property
	def i_get_c_threads(self):
		"""Gets all of the cosmetic threads on this drawing view."""
		return self._instance.IGetCThreads

	@i_get_c_threads.setter
	def i_get_c_threads(self, value):
		"""Gets all of the cosmetic threads on this drawing view."""
		self._instance.IGetCThreads = value

	@property
	def i_get_datum_origins(self):
		"""Gets all of the datum origins on this drawing view."""
		return self._instance.IGetDatumOrigins

	@i_get_datum_origins.setter
	def i_get_datum_origins(self, value):
		"""Gets all of the datum origins on this drawing view."""
		self._instance.IGetDatumOrigins = value

	@property
	def i_get_datum_points(self):
		"""Gets all of the information about all the datum points in this view."""
		return self._instance.IGetDatumPoints2

	@i_get_datum_points.setter
	def i_get_datum_points(self, value):
		"""Gets all of the information about all the datum points in this view."""
		self._instance.IGetDatumPoints2 = value

	@property
	def i_get_datum_tags(self):
		"""Gets all the datum tags on this drawing view."""
		return self._instance.IGetDatumTags

	@i_get_datum_tags.setter
	def i_get_datum_tags(self, value):
		"""Gets all the datum tags on this drawing view."""
		self._instance.IGetDatumTags = value

	@property
	def i_get_datum_target_syms(self):
		"""Gets all of the datum target symbols on this drawing view."""
		return self._instance.IGetDatumTargetSyms

	@i_get_datum_target_syms.setter
	def i_get_datum_target_syms(self, value):
		"""Gets all of the datum target symbols on this drawing view."""
		self._instance.IGetDatumTargetSyms = value

	@property
	def i_get_dependent_views(self):
		"""Gets either all, or only the specified, dependent views in this view."""
		return self._instance.IGetDependentViews

	@i_get_dependent_views.setter
	def i_get_dependent_views(self, value):
		"""Gets either all, or only the specified, dependent views in this view."""
		self._instance.IGetDependentViews = value

	@property
	def i_get_design_table_extent(self):
		"""Gets the size and location of the design table associated with this drawing view."""
		return self._instance.IGetDesignTableExtent

	@i_get_design_table_extent.setter
	def i_get_design_table_extent(self, value):
		"""Gets the size and location of the design table associated with this drawing view."""
		self._instance.IGetDesignTableExtent = value

	@property
	def i_get_detail(self):
		"""Gets the detail circle for this detail view."""
		return self._instance.IGetDetail

	@i_get_detail.setter
	def i_get_detail(self, value):
		"""Gets the detail circle for this detail view."""
		self._instance.IGetDetail = value

	@property
	def i_get_detail_circle_info(self):
		"""Gets all of the information about each detail circle in the view."""
		return self._instance.IGetDetailCircleInfo2

	@i_get_detail_circle_info.setter
	def i_get_detail_circle_info(self, value):
		"""Gets all of the information about each detail circle in the view."""
		self._instance.IGetDetailCircleInfo2 = value

	@property
	def i_get_detail_circles(self):
		"""Gets the detail circles in this view."""
		return self._instance.IGetDetailCircles

	@i_get_detail_circles.setter
	def i_get_detail_circles(self, value):
		"""Gets the detail circles in this view."""
		self._instance.IGetDetailCircles = value

	@property
	def i_get_detail_circle_strings(self):
		"""Gets an array of strings; each string represents the text label for a detail circle in this view."""
		return self._instance.IGetDetailCircleStrings

	@i_get_detail_circle_strings.setter
	def i_get_detail_circle_strings(self, value):
		"""Gets an array of strings; each string represents the text label for a detail circle in this view."""
		self._instance.IGetDetailCircleStrings = value

	@property
	def i_get_dimension_display_info(self):
		"""Gets the display dimension information for the current drawing sheet or the current drawing view."""
		return self._instance.IGetDimensionDisplayInfo5

	@i_get_dimension_display_info.setter
	def i_get_dimension_display_info(self, value):
		"""Gets the display dimension information for the current drawing sheet or the current drawing view."""
		self._instance.IGetDimensionDisplayInfo5 = value

	@property
	def i_get_dimension_display_string(self):
		"""Gets all of the dimension text in the current drawing sheet or the current drawing view."""
		return self._instance.IGetDimensionDisplayString4

	@i_get_dimension_display_string.setter
	def i_get_dimension_display_string(self, value):
		"""Gets all of the dimension text in the current drawing sheet or the current drawing view."""
		self._instance.IGetDimensionDisplayString4 = value

	@property
	def i_get_dimension_ids(self):
		"""Gets the dimension names from the current drawing sheet or the current drawing view."""
		return self._instance.IGetDimensionIds4

	@i_get_dimension_ids.setter
	def i_get_dimension_ids(self, value):
		"""Gets the dimension names from the current drawing sheet or the current drawing view."""
		self._instance.IGetDimensionIds4 = value

	@property
	def i_get_dimension_info(self):
		"""Gets all of the dimension information in the current drawing sheet or the current drawing view."""
		return self._instance.IGetDimensionInfo6

	@i_get_dimension_info.setter
	def i_get_dimension_info(self, value):
		"""Gets all of the dimension information in the current drawing sheet or the current drawing view."""
		self._instance.IGetDimensionInfo6 = value

	@property
	def i_get_dimension_string(self):
		"""Gets the strings containing the text associated with each dimension in the current drawing sheet or the current drawing view."""
		return self._instance.IGetDimensionString4

	@i_get_dimension_string.setter
	def i_get_dimension_string(self, value):
		"""Gets the strings containing the text associated with each dimension in the current drawing sheet or the current drawing view."""
		self._instance.IGetDimensionString4 = value

	@property
	def i_get_display_data(self):
		"""Gets the the IDisplayData object for this drawing view containing only those model items that are visible in the view."""
		return self._instance.IGetDisplayData3

	@i_get_display_data.setter
	def i_get_display_data(self, value):
		"""Gets the the IDisplayData object for this drawing view containing only those model items that are visible in the view."""
		self._instance.IGetDisplayData3 = value

	@property
	def i_get_display_dimensions(self):
		"""Gets all of the display dimensions on this drawing view."""
		return self._instance.IGetDisplayDimensions

	@i_get_display_dimensions.setter
	def i_get_display_dimensions(self, value):
		"""Gets all of the display dimensions on this drawing view."""
		self._instance.IGetDisplayDimensions = value

	@property
	def i_get_dowel_symbols(self):
		"""Gets all of the dowel symbols on this drawing view."""
		return self._instance.IGetDowelSymbols

	@i_get_dowel_symbols.setter
	def i_get_dowel_symbols(self, value):
		"""Gets all of the dowel symbols on this drawing view."""
		self._instance.IGetDowelSymbols = value

	@property
	def i_get_ellipses(self):
		"""Gets all of the ellipses added by a user in this drawing view."""
		return self._instance.IGetEllipses5

	@i_get_ellipses.setter
	def i_get_ellipses(self, value):
		"""Gets all of the ellipses added by a user in this drawing view."""
		self._instance.IGetEllipses5 = value

	@property
	def i_get_face_hatches(self):
		"""Gets the face hatches in the view."""
		return self._instance.IGetFaceHatches

	@i_get_face_hatches.setter
	def i_get_face_hatches(self, value):
		"""Gets the face hatches in the view."""
		self._instance.IGetFaceHatches = value

	@property
	def i_get_first_center_of_mass(self):
		"""Gets the first center of mass in this view."""
		return self._instance.IGetFirstCenterOfMass

	@i_get_first_center_of_mass.setter
	def i_get_first_center_of_mass(self, value):
		"""Gets the first center of mass in this view."""
		self._instance.IGetFirstCenterOfMass = value

	@property
	def i_get_first_c_thread(self):
		"""Gets the first cosmetic thread in the view."""
		return self._instance.IGetFirstCThread

	@i_get_first_c_thread.setter
	def i_get_first_c_thread(self, value):
		"""Gets the first cosmetic thread in the view."""
		self._instance.IGetFirstCThread = value

	@property
	def i_get_first_datum_tag(self):
		"""Gets the first datum tag in the view."""
		return self._instance.IGetFirstDatumTag

	@i_get_first_datum_tag.setter
	def i_get_first_datum_tag(self, value):
		"""Gets the first datum tag in the view."""
		self._instance.IGetFirstDatumTag = value

	@property
	def i_get_first_datum_target_sym(self):
		"""Gets the first datum target symbol in the view."""
		return self._instance.IGetFirstDatumTargetSym

	@i_get_first_datum_target_sym.setter
	def i_get_first_datum_target_sym(self, value):
		"""Gets the first datum target symbol in the view."""
		self._instance.IGetFirstDatumTargetSym = value

	@property
	def i_get_first_dowel_symbol(self):
		"""Gets the first dowel symbol in the view."""
		return self._instance.IGetFirstDowelSymbol

	@i_get_first_dowel_symbol.setter
	def i_get_first_dowel_symbol(self, value):
		"""Gets the first dowel symbol in the view."""
		self._instance.IGetFirstDowelSymbol = value

	@property
	def i_get_first_g_t_o_l(self):
		"""Gets the first geometric tolerance in this view."""
		return self._instance.IGetFirstGTOL

	@i_get_first_g_t_o_l.setter
	def i_get_first_g_t_o_l(self, value):
		"""Gets the first geometric tolerance in this view."""
		self._instance.IGetFirstGTOL = value

	@property
	def i_get_first_multi_jog_leader(self):
		"""Gets the first multi-jog leader in the view."""
		return self._instance.IGetFirstMultiJogLeader

	@i_get_first_multi_jog_leader.setter
	def i_get_first_multi_jog_leader(self, value):
		"""Gets the first multi-jog leader in the view."""
		self._instance.IGetFirstMultiJogLeader = value

	@property
	def i_get_first_note(self):
		"""Gets the first note in the view."""
		return self._instance.IGetFirstNote

	@i_get_first_note.setter
	def i_get_first_note(self, value):
		"""Gets the first note in the view."""
		self._instance.IGetFirstNote = value

	@property
	def i_get_first_revision_cloud(self):
		"""Gets the first revision cloud annotation in this view."""
		return self._instance.IGetFirstRevisionCloud

	@i_get_first_revision_cloud.setter
	def i_get_first_revision_cloud(self, value):
		"""Gets the first revision cloud annotation in this view."""
		self._instance.IGetFirstRevisionCloud = value

	@property
	def i_get_first_s_f_symbol(self):
		"""Gets the first surface-finish symbols in the view."""
		return self._instance.IGetFirstSFSymbol

	@i_get_first_s_f_symbol.setter
	def i_get_first_s_f_symbol(self, value):
		"""Gets the first surface-finish symbols in the view."""
		self._instance.IGetFirstSFSymbol = value

	@property
	def i_get_first_weld_symbol(self):
		"""Gets the first weld symbol in the view."""
		return self._instance.IGetFirstWeldSymbol

	@i_get_first_weld_symbol.setter
	def i_get_first_weld_symbol(self, value):
		"""Gets the first weld symbol in the view."""
		self._instance.IGetFirstWeldSymbol = value

	@property
	def i_get_g_tols(self):
		"""Gets all of the geometric tolerances on this drawing view."""
		return self._instance.IGetGTols

	@i_get_g_tols.setter
	def i_get_g_tols(self, value):
		"""Gets all of the geometric tolerances on this drawing view."""
		self._instance.IGetGTols = value

	@property
	def i_get_lines(self):
		"""Gets all of the lines in the view with an option to include or exclude crosshatch lines."""
		return self._instance.IGetLines4

	@i_get_lines.setter
	def i_get_lines(self, value):
		"""Gets all of the lines in the view with an option to include or exclude crosshatch lines."""
		self._instance.IGetLines4 = value

	@property
	def i_get_multi_jog_leaders(self):
		"""Gets all of the multi-jog leaders in this drawing view."""
		return self._instance.IGetMultiJogLeaders

	@i_get_multi_jog_leaders.setter
	def i_get_multi_jog_leaders(self, value):
		"""Gets all of the multi-jog leaders in this drawing view."""
		self._instance.IGetMultiJogLeaders = value

	@property
	def i_get_next_view(self):
		"""Gets the next drawing view in the drawing."""
		return self._instance.IGetNextView

	@i_get_next_view.setter
	def i_get_next_view(self, value):
		"""Gets the next drawing view in the drawing."""
		self._instance.IGetNextView = value

	@property
	def i_get_notes(self):
		"""Gets the notes in this drawing view."""
		return self._instance.IGetNotes

	@i_get_notes.setter
	def i_get_notes(self, value):
		"""Gets the notes in this drawing view."""
		self._instance.IGetNotes = value

	@property
	def i_get_outline(self):
		"""Gets the bounding box for a view (sheet or drawing) in meters on the drawing page."""
		return self._instance.IGetOutline

	@i_get_outline.setter
	def i_get_outline(self, value):
		"""Gets the bounding box for a view (sheet or drawing) in meters on the drawing page."""
		self._instance.IGetOutline = value

	@property
	def i_get_parabolas(self):
		"""Gets all of the information about all of the parabolas in this view."""
		return self._instance.IGetParabolas2

	@i_get_parabolas.setter
	def i_get_parabolas(self, value):
		"""Gets all of the information about all of the parabolas in this view."""
		self._instance.IGetParabolas2 = value

	@property
	def i_get_polylines(self):
		"""Gets all of the polylines in the view with an option to include or exclude crosshatch lines"""
		return self._instance.IGetPolylines7

	@i_get_polylines.setter
	def i_get_polylines(self, value):
		"""Gets all of the polylines in the view with an option to include or exclude crosshatch lines"""
		self._instance.IGetPolylines7 = value

	@property
	def i_get_poly_lines_and_curves(self):
		"""Gets the arcs, ellipses, splines, and polylines in the view with an option to include or exclude crosshatch lines."""
		return self._instance.IGetPolyLinesAndCurves

	@i_get_poly_lines_and_curves.setter
	def i_get_poly_lines_and_curves(self, value):
		"""Gets the arcs, ellipses, splines, and polylines in the view with an option to include or exclude crosshatch lines."""
		self._instance.IGetPolyLinesAndCurves = value

	@property
	def i_get_projection_arrow(self):
		"""Gets the projection arrow for this projected view."""
		return self._instance.IGetProjectionArrow

	@i_get_projection_arrow.setter
	def i_get_projection_arrow(self, value):
		"""Gets the projection arrow for this projected view."""
		self._instance.IGetProjectionArrow = value

	@property
	def i_get_projection_lines(self):
		"""Gets the projection lines (arrows) in this drawing view."""
		return self._instance.IGetProjectionLines

	@i_get_projection_lines.setter
	def i_get_projection_lines(self, value):
		"""Gets the projection lines (arrows) in this drawing view."""
		self._instance.IGetProjectionLines = value

	@property
	def i_get_related_tangent_edges(self):
		"""Gets the visible tangent edges for the specified bendline in a flat-pattern drawing view."""
		return self._instance.IGetRelatedTangentEdges

	@i_get_related_tangent_edges.setter
	def i_get_related_tangent_edges(self, value):
		"""Gets the visible tangent edges for the specified bendline in a flat-pattern drawing view."""
		self._instance.IGetRelatedTangentEdges = value

	@property
	def i_get_revision_clouds(self):
		"""Gets all of the revision cloud annotations in this view."""
		return self._instance.IGetRevisionClouds

	@i_get_revision_clouds.setter
	def i_get_revision_clouds(self, value):
		"""Gets all of the revision cloud annotations in this view."""
		self._instance.IGetRevisionClouds = value

	@property
	def i_get_section(self):
		"""Gets the section for this section view."""
		return self._instance.IGetSection

	@i_get_section.setter
	def i_get_section(self, value):
		"""Gets the section for this section view."""
		self._instance.IGetSection = value

	@property
	def i_get_section_line_info(self):
		"""Gets all of the information about the section lines in the view."""
		return self._instance.IGetSectionLineInfo2

	@i_get_section_line_info.setter
	def i_get_section_line_info(self, value):
		"""Gets all of the information about the section lines in the view."""
		self._instance.IGetSectionLineInfo2 = value

	@property
	def i_get_section_lines(self):
		"""Gets the section lines in the view."""
		return self._instance.IGetSectionLines

	@i_get_section_lines.setter
	def i_get_section_lines(self, value):
		"""Gets the section lines in the view."""
		self._instance.IGetSectionLines = value

	@property
	def i_get_section_line_strings(self):
		"""Gets an array of strings; each string represents the text label for a section line in this view."""
		return self._instance.IGetSectionLineStrings

	@i_get_section_line_strings.setter
	def i_get_section_line_strings(self, value):
		"""Gets an array of strings; each string represents the text label for a section line in this view."""
		self._instance.IGetSectionLineStrings = value

	@property
	def i_get_s_f_symbols(self):
		"""Gets all of the surface finish symbols in this drawing view."""
		return self._instance.IGetSFSymbols

	@i_get_s_f_symbols.setter
	def i_get_s_f_symbols(self, value):
		"""Gets all of the surface finish symbols in this drawing view."""
		self._instance.IGetSFSymbols = value

	@property
	def i_get_sketch(self):
		"""Gets the sketch used by this view."""
		return self._instance.IGetSketch

	@i_get_sketch.setter
	def i_get_sketch(self, value):
		"""Gets the sketch used by this view."""
		self._instance.IGetSketch = value

	@property
	def i_get_sketch_pictures(self):
		"""Gets all of the sketch pictures imported to this view when a drawing is created from a part."""
		return self._instance.IGetSketchPictures

	@i_get_sketch_pictures.setter
	def i_get_sketch_pictures(self, value):
		"""Gets all of the sketch pictures imported to this view when a drawing is created from a part."""
		self._instance.IGetSketchPictures = value

	@property
	def i_get_s_m_boundary_box_display_data(self):
		"""Gets the boundary-box sketch display data of a flat-pattern drawing view."""
		return self._instance.IGetSMBoundaryBoxDisplayData

	@i_get_s_m_boundary_box_display_data.setter
	def i_get_s_m_boundary_box_display_data(self, value):
		"""Gets the boundary-box sketch display data of a flat-pattern drawing view."""
		self._instance.IGetSMBoundaryBoxDisplayData = value

	@property
	def i_get_solid_hatch_info(self):
		"""Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view."""
		return self._instance.IGetSolidHatchInfo

	@i_get_solid_hatch_info.setter
	def i_get_solid_hatch_info(self, value):
		"""Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view."""
		self._instance.IGetSolidHatchInfo = value

	@property
	def i_get_splines(self):
		"""Gets all of the splines added by a user in the drawing view."""
		return self._instance.IGetSplines3

	@i_get_splines.setter
	def i_get_splines(self, value):
		"""Gets all of the splines added by a user in the drawing view."""
		self._instance.IGetSplines3 = value

	@property
	def i_get_table_annotations(self):
		"""Gets all of the table annotations in this drawing view."""
		return self._instance.IGetTableAnnotations

	@i_get_table_annotations.setter
	def i_get_table_annotations(self, value):
		"""Gets all of the table annotations in this drawing view."""
		self._instance.IGetTableAnnotations = value

	@property
	def i_get_temporary_axes(self):
		"""Gets the information of the temporary axes displayed in this view."""
		return self._instance.IGetTemporaryAxes

	@i_get_temporary_axes.setter
	def i_get_temporary_axes(self, value):
		"""Gets the information of the temporary axes displayed in this view."""
		self._instance.IGetTemporaryAxes = value

	@property
	def i_get_user_points(self):
		"""Gets all of the information about all of the user points in this view."""
		return self._instance.IGetUserPoints2

	@i_get_user_points.setter
	def i_get_user_points(self, value):
		"""Gets all of the information about all of the user points in this view."""
		self._instance.IGetUserPoints2 = value

	@property
	def i_get_view_xform(self):
		"""Gets the transform from model space origin to drawing space origin."""
		return self._instance.IGetViewXform

	@i_get_view_xform.setter
	def i_get_view_xform(self, value):
		"""Gets the transform from model space origin to drawing space origin."""
		self._instance.IGetViewXform = value

	@property
	def i_get_visible_components(self):
		"""Gets the visible components in this drawing view."""
		return self._instance.IGetVisibleComponents

	@i_get_visible_components.setter
	def i_get_visible_components(self, value):
		"""Gets the visible components in this drawing view."""
		self._instance.IGetVisibleComponents = value

	@property
	def i_get_visible_entities(self):
		"""Gets the visible entities of the specified type for the specified component in this drawing view."""
		return self._instance.IGetVisibleEntities2

	@i_get_visible_entities.setter
	def i_get_visible_entities(self, value):
		"""Gets the visible entities of the specified type for the specified component in this drawing view."""
		self._instance.IGetVisibleEntities2 = value

	@property
	def i_get_weld_beads(self):
		"""Gets all of the weld beads on this drawing view."""
		return self._instance.IGetWeldBeads

	@i_get_weld_beads.setter
	def i_get_weld_beads(self, value):
		"""Gets all of the weld beads on this drawing view."""
		self._instance.IGetWeldBeads = value

	@property
	def i_get_weld_symbols(self):
		"""Gets all of the weld symbols on this drawing view."""
		return self._instance.IGetWeldSymbols

	@i_get_weld_symbols.setter
	def i_get_weld_symbols(self, value):
		"""Gets all of the weld symbols on this drawing view."""
		self._instance.IGetWeldSymbols = value

	@property
	def i_get_witness_geom_info(self):
		"""Gets the geometry data for all of the virtual sharp witness lines in this drawing view."""
		return self._instance.IGetWitnessGeomInfo

	@i_get_witness_geom_info.setter
	def i_get_witness_geom_info(self, value):
		"""Gets the geometry data for all of the virtual sharp witness lines in this drawing view."""
		self._instance.IGetWitnessGeomInfo = value

	@property
	def i_get_xform(self):
		"""Gets the matrix used for displaying this drawing view."""
		return self._instance.IGetXform

	@i_get_xform.setter
	def i_get_xform(self, value):
		"""Gets the matrix used for displaying this drawing view."""
		self._instance.IGetXform = value

	@property
	def i_insert_bom_table(self):
		"""Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel."""
		return self._instance.IInsertBomTable

	@i_insert_bom_table.setter
	def i_insert_bom_table(self, value):
		"""Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel."""
		self._instance.IInsertBomTable = value

	@property
	def insert_alternate_view(self):
		"""Inserts an Alternate Position View of the currently selected drawing view."""
		return self._instance.InsertAlternateView

	@insert_alternate_view.setter
	def insert_alternate_view(self, value):
		"""Inserts an Alternate Position View of the currently selected drawing view."""
		self._instance.InsertAlternateView = value

	@property
	def insert_bend_table(self):
		"""Inserts a bend table for this drawing view."""
		return self._instance.InsertBendTable

	@insert_bend_table.setter
	def insert_bend_table(self, value):
		"""Inserts a bend table for this drawing view."""
		self._instance.InsertBendTable = value

	@property
	def insert_bom_table(self):
		"""Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel."""
		return self._instance.InsertBomTable

	@insert_bom_table.setter
	def insert_bom_table(self, value):
		"""Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel."""
		self._instance.InsertBomTable = value

	@property
	def insert_bom_table(self):
		"""Inserts a bill of materials (BOM) table for this drawing view using SOLIDWORKS table functionality."""
		return self._instance.InsertBomTable4

	@insert_bom_table.setter
	def insert_bom_table(self, value):
		"""Inserts a bill of materials (BOM) table for this drawing view using SOLIDWORKS table functionality."""
		self._instance.InsertBomTable4 = value

	@property
	def insert_break(self):
		"""Inserts the specified type of break at the specified location in this drawing view."""
		return self._instance.InsertBreak3

	@insert_break.setter
	def insert_break(self, value):
		"""Inserts the specified type of break at the specified location in this drawing view."""
		self._instance.InsertBreak3 = value

	@property
	def insert_cut_list_property_note(self):
		"""Inserts a note that contains all of the cut list item properties of a sheet metal part."""
		return self._instance.InsertCutListPropertyNote

	@insert_cut_list_property_note.setter
	def insert_cut_list_property_note(self, value):
		"""Inserts a note that contains all of the cut list item properties of a sheet metal part."""
		self._instance.InsertCutListPropertyNote = value

	@property
	def insert_hole_table(self):
		"""Inserts a hole table in this drawing view."""
		return self._instance.InsertHoleTable3

	@insert_hole_table.setter
	def insert_hole_table(self, value):
		"""Inserts a hole table in this drawing view."""
		self._instance.InsertHoleTable3 = value

	@property
	def insert_punch_table(self):
		"""Inserts a punch table in the flat pattern drawing view of a sheet metal part."""
		return self._instance.InsertPunchTable

	@insert_punch_table.setter
	def insert_punch_table(self, value):
		"""Inserts a punch table in the flat pattern drawing view of a sheet metal part."""
		self._instance.InsertPunchTable = value

	@property
	def insert_view_as_block(self):
		"""Creates a sketch block from this view and aligns the specified manipulator point with the specified sketch block position on the drawing sheet."""
		return self._instance.InsertViewAsBlock

	@insert_view_as_block.setter
	def insert_view_as_block(self, value):
		"""Creates a sketch block from this view and aligns the specified manipulator point with the specified sketch block position on the drawing sheet."""
		self._instance.InsertViewAsBlock = value

	@property
	def insert_weldment_table(self):
		"""Inserts a weldment cut-list table into this drawing view."""
		return self._instance.InsertWeldmentTable

	@insert_weldment_table.setter
	def insert_weldment_table(self, value):
		"""Inserts a weldment cut-list table into this drawing view."""
		self._instance.InsertWeldmentTable = value

	@property
	def insert_weld_table(self):
		"""Inserts a weld table into this drawing view."""
		return self._instance.InsertWeldTable

	@insert_weld_table.setter
	def insert_weld_table(self, value):
		"""Inserts a weld table into this drawing view."""
		self._instance.InsertWeldTable = value

	@property
	def is_broken(self):
		"""Gets whether the drawing view is displayed with a break."""
		return self._instance.IsBroken

	@is_broken.setter
	def is_broken(self, value):
		"""Gets whether the drawing view is displayed with a break."""
		self._instance.IsBroken = value

	@property
	def is_cropped(self):
		"""Get whether this drawing view is cropped."""
		return self._instance.IsCropped

	@is_cropped.setter
	def is_cropped(self, value):
		"""Get whether this drawing view is cropped."""
		self._instance.IsCropped = value

	@property
	def i_select_entity(self):
		"""Selects an entity in this drawing view."""
		return self._instance.ISelectEntity

	@i_select_entity.setter
	def i_select_entity(self, value):
		"""Selects an entity in this drawing view."""
		self._instance.ISelectEntity = value

	@property
	def i_set_bodies(self):
		"""Sets the bodies of a multibody part to include in the view."""
		return self._instance.ISetBodies

	@i_set_bodies.setter
	def i_set_bodies(self, value):
		"""Sets the bodies of a multibody part to include in the view."""
		self._instance.ISetBodies = value

	@property
	def i_set_xform(self):
		"""Sets the matrix used for display of this drawing view."""
		return self._instance.ISetXform

	@i_set_xform.setter
	def i_set_xform(self, value):
		"""Sets the matrix used for display of this drawing view."""
		self._instance.ISetXform = value

	@property
	def is_exploded(self):
		"""Gets whether the drawing view is currently showing the assembly as exploded or collasped."""
		return self._instance.IsExploded

	@is_exploded.setter
	def is_exploded(self, value):
		"""Gets whether the drawing view is currently showing the assembly as exploded or collasped."""
		self._instance.IsExploded = value

	@property
	def is_flat_pattern_view(self):
		"""Gets whether a drawing view is a flat-pattern drawing view."""
		return self._instance.IsFlatPatternView

	@is_flat_pattern_view.setter
	def is_flat_pattern_view(self, value):
		"""Gets whether a drawing view is a flat-pattern drawing view."""
		self._instance.IsFlatPatternView = value

	@property
	def is_lightweight(self):
		"""Gets whether the drawing view is lightweight."""
		return self._instance.IsLightweight

	@is_lightweight.setter
	def is_lightweight(self, value):
		"""Gets whether the drawing view is lightweight."""
		self._instance.IsLightweight = value

	@property
	def is_model_break_state(self):
		"""Gets whether this drawing view is a Model Break View."""
		return self._instance.IsModelBreakState

	@is_model_break_state.setter
	def is_model_break_state(self, value):
		"""Gets whether this drawing view is a Model Break View."""
		self._instance.IsModelBreakState = value

	@property
	def is_model_loaded(self):
		"""Gets whether the model is loaded in this drawing view."""
		return self._instance.IsModelLoaded

	@is_model_loaded.setter
	def is_model_loaded(self, value):
		"""Gets whether the model is loaded in this drawing view."""
		self._instance.IsModelLoaded = value

	@property
	def is_model_out_of_date(self):
		"""Gets whether the model in this drawing view is up-to-date with the current model."""
		return self._instance.IsModelOutOfDate

	@is_model_out_of_date.setter
	def is_model_out_of_date(self, value):
		"""Gets whether the model in this drawing view is up-to-date with the current model."""
		self._instance.IsModelOutOfDate = value

	@property
	def is_perspective_view(self):
		"""Gets whether this drawing view is showing a perspective view of the model."""
		return self._instance.IsPerspectiveView

	@is_perspective_view.setter
	def is_perspective_view(self, value):
		"""Gets whether this drawing view is showing a perspective view of the model."""
		self._instance.IsPerspectiveView = value

	@property
	def load_model(self):
		"""Loads the model if the model has not already been loaded for this drawing view."""
		return self._instance.LoadModel

	@load_model.setter
	def load_model(self, value):
		"""Loads the model if the model has not already been loaded for this drawing view."""
		self._instance.LoadModel = value

	@property
	def merge_bend_tags(self):
		"""Merges or unmerges bend tags in drawings of sheet metal parts."""
		return self._instance.MergeBendTags

	@merge_bend_tags.setter
	def merge_bend_tags(self, value):
		"""Merges or unmerges bend tags in drawings of sheet metal parts."""
		self._instance.MergeBendTags = value

	@property
	def remove_alignment(self):
		"""Removes the alignment from this drawing view."""
		return self._instance.RemoveAlignment

	@remove_alignment.setter
	def remove_alignment(self, value):
		"""Removes the alignment from this drawing view."""
		self._instance.RemoveAlignment = value

	@property
	def replace_view_with_block(self):
		"""Converts this view into a sketch block with the specified manipulator location."""
		return self._instance.ReplaceViewWithBlock

	@replace_view_with_block.setter
	def replace_view_with_block(self, value):
		"""Converts this view into a sketch block with the specified manipulator location."""
		self._instance.ReplaceViewWithBlock = value

	@property
	def replace_view_with_sketch(self):
		"""Converts this view into a sketch."""
		return self._instance.ReplaceViewWithSketch

	@replace_view_with_sketch.setter
	def replace_view_with_sketch(self, value):
		"""Converts this view into a sketch."""
		self._instance.ReplaceViewWithSketch = value

	@property
	def reset_sketch_visibility(self):
		"""Resets the visibility of the sketches in the drawing view so that the drawing view reflects the model."""
		return self._instance.ResetSketchVisibility

	@reset_sketch_visibility.setter
	def reset_sketch_visibility(self, value):
		"""Resets the visibility of the sketches in the drawing view so that the drawing view reflects the model."""
		self._instance.ResetSketchVisibility = value

	@property
	def select_entity(self):
		"""Selects an entity in this drawing view."""
		return self._instance.SelectEntity

	@select_entity.setter
	def select_entity(self, value):
		"""Selects an entity in this drawing view."""
		self._instance.SelectEntity = value

	@property
	def set_bend_note_text_format(self):
		"""Sets the text format of all bend notes in this drawing view of a sheet metal part."""
		return self._instance.SetBendNoteTextFormat

	@set_bend_note_text_format.setter
	def set_bend_note_text_format(self, value):
		"""Sets the text format of all bend notes in this drawing view of a sheet metal part."""
		self._instance.SetBendNoteTextFormat = value

	@property
	def set_display_mode(self):
		"""Sets the display mode of this drawing view."""
		return self._instance.SetDisplayMode4

	@set_display_mode.setter
	def set_display_mode(self, value):
		"""Sets the display mode of this drawing view."""
		self._instance.SetDisplayMode4 = value

	@property
	def set_display_tangent_edges(self):
		"""Sets the tangent edge display mode of the drawing view."""
		return self._instance.SetDisplayTangentEdges2

	@set_display_tangent_edges.setter
	def set_display_tangent_edges(self, value):
		"""Sets the tangent edge display mode of the drawing view."""
		self._instance.SetDisplayTangentEdges2 = value

	@property
	def set_keep_linked_to_b_o_m(self):
		"""Sets whether this drawing view is linked to the specified BOM or weldment cut-list table."""
		return self._instance.SetKeepLinkedToBOM

	@set_keep_linked_to_b_o_m.setter
	def set_keep_linked_to_b_o_m(self, value):
		"""Sets whether this drawing view is linked to the specified BOM or weldment cut-list table."""
		self._instance.SetKeepLinkedToBOM = value

	@property
	def set_lightweight_to_resolved(self):
		"""Changes the drawing view from lightweight to resolved."""
		return self._instance.SetLightweightToResolved

	@set_lightweight_to_resolved.setter
	def set_lightweight_to_resolved(self, value):
		"""Changes the drawing view from lightweight to resolved."""
		self._instance.SetLightweightToResolved = value

	@property
	def set_mirror_view_orientation(self):
		"""Sets whether to mirror this view."""
		return self._instance.SetMirrorViewOrientation

	@set_mirror_view_orientation.setter
	def set_mirror_view_orientation(self, value):
		"""Sets whether to mirror this view."""
		self._instance.SetMirrorViewOrientation = value

	@property
	def set_name(self):
		"""Sets the name of this drawing view, as displayed in the FeatureManager design tree."""
		return self._instance.SetName2

	@set_name.setter
	def set_name(self, value):
		"""Sets the name of this drawing view, as displayed in the FeatureManager design tree."""
		self._instance.SetName2 = value

	@property
	def set_resolved_to_lightweight(self):
		"""Changes the drawing view from resolved to lightweight."""
		return self._instance.SetResolvedToLightweight

	@set_resolved_to_lightweight.setter
	def set_resolved_to_lightweight(self, value):
		"""Changes the drawing view from resolved to lightweight."""
		self._instance.SetResolvedToLightweight = value

	@property
	def set_visible(self):
		"""Sets the visibility of this drawing view."""
		return self._instance.SetVisible

	@set_visible.setter
	def set_visible(self, value):
		"""Sets the visibility of this drawing view."""
		self._instance.SetVisible = value

	@property
	def set_xform(self):
		"""Sets the matrix used for display of this drawing view."""
		return self._instance.SetXform

	@set_xform.setter
	def set_xform(self, value):
		"""Sets the matrix used for display of this drawing view."""
		self._instance.SetXform = value

	@property
	def show_exploded(self):
		"""Shows an exploded assembly in this drawing view."""
		return self._instance.ShowExploded

	@show_exploded.setter
	def show_exploded(self, value):
		"""Shows an exploded assembly in this drawing view."""
		self._instance.ShowExploded = value

	@property
	def show_model_break_state(self):
		"""Sets whether to display the specified Model Break View."""
		return self._instance.ShowModelBreakState

	@show_model_break_state.setter
	def show_model_break_state(self, value):
		"""Sets whether to display the specified Model Break View."""
		self._instance.ShowModelBreakState = value

	@property
	def update_view_display_geometry(self):
		"""Updates the displayed geometry for a drawing view."""
		return self._instance.UpdateViewDisplayGeometry

	@update_view_display_geometry.setter
	def update_view_display_geometry(self, value):
		"""Updates the displayed geometry for a drawing view."""
		self._instance.UpdateViewDisplayGeometry = value

	@property
	def use_default_alignment(self):
		"""Restores the default alignment for this drawing view."""
		return self._instance.UseDefaultAlignment

	@use_default_alignment.setter
	def use_default_alignment(self, value):
		"""Restores the default alignment for this drawing view."""
		self._instance.UseDefaultAlignment = value

