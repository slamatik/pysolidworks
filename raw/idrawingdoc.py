# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html
class IDrawingDoc:
	def __init__(self, parent=None):
		self._instance = parent

	def active_drawing_view(self):
		"""Gets the currently active drawing view."""
		# return self._instance.ActiveDrawingView
		raise NotImplemented

	@property
	def automatic_view_update(self):
		"""Gets or sets whether the drawing views in this drawing are automatically updated if the underlying model in that drawing view changes."""
		return self._instance.AutomaticViewUpdate

	@automatic_view_update.setter
	def automatic_view_update(self, value):
		"""Gets or sets whether the drawing views in this drawing are automatically updated if the underlying model in that drawing view changes."""
		self._instance.AutomaticViewUpdate = value

	@property
	def background_processing_option(self):
		"""Gets or sets the background processing option for this drawing."""
		return self._instance.BackgroundProcessingOption

	@background_processing_option.setter
	def background_processing_option(self, value):
		"""Gets or sets the background processing option for this drawing."""
		self._instance.BackgroundProcessingOption = value

	@property
	def hidden_views_visible(self):
		"""Shows or hides all of the hidden drawing views."""
		return self._instance.HiddenViewsVisible

	@hidden_views_visible.setter
	def hidden_views_visible(self, value):
		"""Shows or hides all of the hidden drawing views."""
		self._instance.HiddenViewsVisible = value

	@property
	def i_active_drawing_view(self):
		"""Gets the currently active drawing view."""
		return self._instance.IActiveDrawingView

	@i_active_drawing_view.setter
	def i_active_drawing_view(self, value):
		"""Gets the currently active drawing view."""
		self._instance.IActiveDrawingView = value

	@property
	def sheet(self):
		"""Gets the specified sheet."""
		return self._instance.Sheet

	@sheet.setter
	def sheet(self, value):
		"""Gets the specified sheet."""
		self._instance.Sheet = value

	@property
	def activate_sheet(self):
		"""Activates the specified drawing sheet."""
		return self._instance.ActivateSheet

	@activate_sheet.setter
	def activate_sheet(self, value):
		"""Activates the specified drawing sheet."""
		self._instance.ActivateSheet = value

	@property
	def activate_view(self):
		"""Activates the specified drawing view."""
		return self._instance.ActivateView

	@activate_view.setter
	def activate_view(self, value):
		"""Activates the specified drawing view."""
		self._instance.ActivateView = value

	@property
	def add_chamfer_dim(self):
		"""Adds a chamfer dimension."""
		return self._instance.AddChamferDim

	@add_chamfer_dim.setter
	def add_chamfer_dim(self, value):
		"""Adds a chamfer dimension."""
		self._instance.AddChamferDim = value

	@property
	def add_hole_callout(self):
		"""Adds a hole callout at the specified position to the hole whose edge is selected."""
		return self._instance.AddHoleCallout2

	@add_hole_callout.setter
	def add_hole_callout(self, value):
		"""Adds a hole callout at the specified position to the hole whose edge is selected."""
		self._instance.AddHoleCallout2 = value

	@property
	def add_line_style(self):
		"""Adds a line style to the current drawing."""
		return self._instance.AddLineStyle

	@add_line_style.setter
	def add_line_style(self, value):
		"""Adds a line style to the current drawing."""
		self._instance.AddLineStyle = value

	@property
	def align_horz(self):
		"""Uses the selected edge to align the current drawing view."""
		return self._instance.AlignHorz

	@align_horz.setter
	def align_horz(self, value):
		"""Uses the selected edge to align the current drawing view."""
		self._instance.AlignHorz = value

	@property
	def align_ordinate(self):
		"""Aligns the ordinate dimension."""
		return self._instance.AlignOrdinate

	@align_ordinate.setter
	def align_ordinate(self, value):
		"""Aligns the ordinate dimension."""
		self._instance.AlignOrdinate = value

	@property
	def align_vert(self):
		"""Uses the selected edge to align the current drawing view."""
		return self._instance.AlignVert

	@align_vert.setter
	def align_vert(self, value):
		"""Uses the selected edge to align the current drawing view."""
		self._instance.AlignVert = value

	@property
	def attach_annotation(self):
		"""Attaches an existing annotation to a drawing sheet or view."""
		return self._instance.AttachAnnotation

	@attach_annotation.setter
	def attach_annotation(self, value):
		"""Attaches an existing annotation to a drawing sheet or view."""
		self._instance.AttachAnnotation = value

	@property
	def attach_dimensions(self):
		"""Attaches unattached dimensions."""
		return self._instance.AttachDimensions

	@attach_dimensions.setter
	def attach_dimensions(self, value):
		"""Attaches unattached dimensions."""
		self._instance.AttachDimensions = value

	@property
	def auto_balloon(self):
		"""Automatically inserts BOM balloons in selected drawing views."""
		return self._instance.AutoBalloon5

	@auto_balloon.setter
	def auto_balloon(self, value):
		"""Automatically inserts BOM balloons in selected drawing views."""
		self._instance.AutoBalloon5 = value

	@property
	def auto_dimension(self):
		"""Automatically dimensions the selected drawing view."""
		return self._instance.AutoDimension

	@auto_dimension.setter
	def auto_dimension(self, value):
		"""Automatically dimensions the selected drawing view."""
		self._instance.AutoDimension = value

	@property
	def break_view(self):
		"""Breaks the drawing view along the existing break lines."""
		return self._instance.BreakView

	@break_view.setter
	def break_view(self, value):
		"""Breaks the drawing view along the existing break lines."""
		self._instance.BreakView = value

	@property
	def change_component_layer(self):
		"""Puts the selected components on the specified layer."""
		return self._instance.ChangeComponentLayer

	@change_component_layer.setter
	def change_component_layer(self, value):
		"""Puts the selected components on the specified layer."""
		self._instance.ChangeComponentLayer = value

	@property
	def change_ord_dir(self):
		"""Changes the ordinate direction."""
		return self._instance.ChangeOrdDir

	@change_ord_dir.setter
	def change_ord_dir(self, value):
		"""Changes the ordinate direction."""
		self._instance.ChangeOrdDir = value

	@property
	def change_ref_configuration_of_flat_pattern_view(self):
		"""Changes the referenced configuration of the flat-pattern view."""
		return self._instance.ChangeRefConfigurationOfFlatPatternView

	@change_ref_configuration_of_flat_pattern_view.setter
	def change_ref_configuration_of_flat_pattern_view(self, value):
		"""Changes the referenced configuration of the flat-pattern view."""
		self._instance.ChangeRefConfigurationOfFlatPatternView = value

	@property
	def createst_angle_views(self):
		"""Creates standard three orthographic views (first angle projection) for the specified model."""
		return self._instance.Create1stAngleViews2

	@createst_angle_views.setter
	def createst_angle_views(self, value):
		"""Creates standard three orthographic views (first angle projection) for the specified model."""
		self._instance.Create1stAngleViews2 = value

	@property
	def createrd_angle_views(self):
		"""Creates standard three orthographic views (third angle projection) for the specified model."""
		return self._instance.Create3rdAngleViews2

	@createrd_angle_views.setter
	def createrd_angle_views(self, value):
		"""Creates standard three orthographic views (third angle projection) for the specified model."""
		self._instance.Create3rdAngleViews2 = value

	@property
	def create_ang_dim(self):
		"""Creates a non-associative angular dimension."""
		return self._instance.CreateAngDim4

	@create_ang_dim.setter
	def create_ang_dim(self, value):
		"""Creates a non-associative angular dimension."""
		self._instance.CreateAngDim4 = value

	@property
	def create_auto_balloon_options(self):
		"""Creates an object that stores auto balloon options."""
		return self._instance.CreateAutoBalloonOptions

	@create_auto_balloon_options.setter
	def create_auto_balloon_options(self, value):
		"""Creates an object that stores auto balloon options."""
		self._instance.CreateAutoBalloonOptions = value

	@property
	def create_auxiliary_view_at(self):
		"""Creates an auxiliary view based on a selected edge in a drawing view."""
		return self._instance.CreateAuxiliaryViewAt2

	@create_auxiliary_view_at.setter
	def create_auxiliary_view_at(self, value):
		"""Creates an auxiliary view based on a selected edge in a drawing view."""
		self._instance.CreateAuxiliaryViewAt2 = value

	@property
	def create_break_out_section(self):
		"""Creates a broken-out section in a drawing document."""
		return self._instance.CreateBreakOutSection

	@create_break_out_section.setter
	def create_break_out_section(self, value):
		"""Creates a broken-out section in a drawing document."""
		self._instance.CreateBreakOutSection = value

	@property
	def create_construction_geometry(self):
		"""Sets the selected sketch segments to be construction geometry instead of sketch geometry."""
		return self._instance.CreateConstructionGeometry

	@create_construction_geometry.setter
	def create_construction_geometry(self, value):
		"""Sets the selected sketch segments to be construction geometry instead of sketch geometry."""
		self._instance.CreateConstructionGeometry = value

	@property
	def create_detail_view_at(self):
		"""Creates a detail view in a drawing document."""
		return self._instance.CreateDetailViewAt4

	@create_detail_view_at.setter
	def create_detail_view_at(self, value):
		"""Creates a detail view in a drawing document."""
		self._instance.CreateDetailViewAt4 = value

	@property
	def create_diam_dim(self):
		"""Creates a non-associative diameter dimension."""
		return self._instance.CreateDiamDim4

	@create_diam_dim.setter
	def create_diam_dim(self, value):
		"""Creates a non-associative diameter dimension."""
		self._instance.CreateDiamDim4 = value

	@property
	def create_draw_view_from_model_view(self):
		"""Creates a drawing view on the current drawing sheet using the specified model view."""
		return self._instance.CreateDrawViewFromModelView3

	@create_draw_view_from_model_view.setter
	def create_draw_view_from_model_view(self, value):
		"""Creates a drawing view on the current drawing sheet using the specified model view."""
		self._instance.CreateDrawViewFromModelView3 = value

	@property
	def create_flat_pattern_view_from_model_view(self):
		"""Creates a flat-pattern view from a model view."""
		return self._instance.CreateFlatPatternViewFromModelView3

	@create_flat_pattern_view_from_model_view.setter
	def create_flat_pattern_view_from_model_view(self, value):
		"""Creates a flat-pattern view from a model view."""
		self._instance.CreateFlatPatternViewFromModelView3 = value

	@property
	def create_layer(self):
		"""Creates a layer for this document."""
		return self._instance.CreateLayer2

	@create_layer.setter
	def create_layer(self, value):
		"""Creates a layer for this document."""
		self._instance.CreateLayer2 = value

	@property
	def create_linear_dim(self):
		"""Creates a non-associative linear dimension."""
		return self._instance.CreateLinearDim4

	@create_linear_dim.setter
	def create_linear_dim(self, value):
		"""Creates a non-associative linear dimension."""
		self._instance.CreateLinearDim4 = value

	@property
	def create_ordinate_dim(self):
		"""Creates a non-associative ordinate dimension."""
		return self._instance.CreateOrdinateDim4

	@create_ordinate_dim.setter
	def create_ordinate_dim(self, value):
		"""Creates a non-associative ordinate dimension."""
		self._instance.CreateOrdinateDim4 = value

	@property
	def create_relative_view(self):
		"""Creates a relative drawing view."""
		return self._instance.CreateRelativeView

	@create_relative_view.setter
	def create_relative_view(self, value):
		"""Creates a relative drawing view."""
		self._instance.CreateRelativeView = value

	@property
	def create_section_view(self):
		"""Creates a section view in the drawing using the selected section line."""
		return self._instance.CreateSectionView

	@create_section_view.setter
	def create_section_view(self, value):
		"""Creates a section view in the drawing using the selected section line."""
		self._instance.CreateSectionView = value

	@property
	def create_section_view_at(self):
		"""Creates the specified section view."""
		return self._instance.CreateSectionViewAt5

	@create_section_view_at.setter
	def create_section_view_at(self, value):
		"""Creates the specified section view."""
		self._instance.CreateSectionViewAt5 = value

	@property
	def create_text(self):
		"""Creates a note containing the specified text at a given location."""
		return self._instance.CreateText2

	@create_text.setter
	def create_text(self, value):
		"""Creates a note containing the specified text at a given location."""
		self._instance.CreateText2 = value

	@property
	def create_unfolded_view_at(self):
		"""Creates an unfolded drawing view from the selected drawing view and places it in the drawing at the specified location."""
		return self._instance.CreateUnfoldedViewAt3

	@create_unfolded_view_at.setter
	def create_unfolded_view_at(self, value):
		"""Creates an unfolded drawing view from the selected drawing view and places it in the drawing at the specified location."""
		self._instance.CreateUnfoldedViewAt3 = value

	@property
	def create_viewport(self):
		"""Creates a an empty view in a drawing."""
		return self._instance.CreateViewport3

	@create_viewport.setter
	def create_viewport(self, value):
		"""Creates a an empty view in a drawing."""
		self._instance.CreateViewport3 = value

	@property
	def delete_all_cosmetic_threads(self):
		"""Deletes all cosmetic threads, which do not have callouts, in a drawing of an assembly only."""
		return self._instance.DeleteAllCosmeticThreads

	@delete_all_cosmetic_threads.setter
	def delete_all_cosmetic_threads(self, value):
		"""Deletes all cosmetic threads, which do not have callouts, in a drawing of an assembly only."""
		self._instance.DeleteAllCosmeticThreads = value

	@property
	def delete_line_style(self):
		"""Deletes the specified line style from the current drawing."""
		return self._instance.DeleteLineStyle

	@delete_line_style.setter
	def delete_line_style(self, value):
		"""Deletes the specified line style from the current drawing."""
		self._instance.DeleteLineStyle = value

	@property
	def dimensions(self):
		"""Adds dimensions to the drawing from model."""
		return self._instance.Dimensions

	@dimensions.setter
	def dimensions(self, value):
		"""Adds dimensions to the drawing from model."""
		self._instance.Dimensions = value

	@property
	def drag_model_dimension(self):
		"""Copies or moves dimensions to a different drawing view."""
		return self._instance.DragModelDimension

	@drag_model_dimension.setter
	def drag_model_dimension(self, value):
		"""Copies or moves dimensions to a different drawing view."""
		self._instance.DragModelDimension = value

	@property
	def drawing_view_rotate(self):
		"""Rotates the selected drawing view."""
		return self._instance.DrawingViewRotate

	@drawing_view_rotate.setter
	def drawing_view_rotate(self, value):
		"""Rotates the selected drawing view."""
		self._instance.DrawingViewRotate = value

	@property
	def drop_drawing_view_from_palette(self):
		"""Moves the specified drawing view from the View Palette to the current drawing sheet."""
		return self._instance.DropDrawingViewFromPalette2

	@drop_drawing_view_from_palette.setter
	def drop_drawing_view_from_palette(self, value):
		"""Moves the specified drawing view from the View Palette to the current drawing sheet."""
		self._instance.DropDrawingViewFromPalette2 = value

	@property
	def edit_center_mark_properties(self):
		"""Edits center mark properties."""
		return self._instance.EditCenterMarkProperties

	@edit_center_mark_properties.setter
	def edit_center_mark_properties(self, value):
		"""Edits center mark properties."""
		self._instance.EditCenterMarkProperties = value

	@property
	def edit_ordinate(self):
		"""Edits an ordinate dimension."""
		return self._instance.EditOrdinate

	@edit_ordinate.setter
	def edit_ordinate(self, value):
		"""Edits an ordinate dimension."""
		self._instance.EditOrdinate = value

	@property
	def edit_selected_gtol(self):
		"""Gets the selected GTol to edit."""
		return self._instance.EditSelectedGtol

	@edit_selected_gtol.setter
	def edit_selected_gtol(self, value):
		"""Gets the selected GTol to edit."""
		self._instance.EditSelectedGtol = value

	@property
	def edit_sheet(self):
		"""Puts the current drawing sheet in edit mode."""
		return self._instance.EditSheet

	@edit_sheet.setter
	def edit_sheet(self, value):
		"""Puts the current drawing sheet in edit mode."""
		self._instance.EditSheet = value

	@property
	def edit_sketch(self):
		"""Allows editing of a sketch in the selected drawing view or sheet."""
		return self._instance.EditSketch

	@edit_sketch.setter
	def edit_sketch(self, value):
		"""Allows editing of a sketch in the selected drawing view or sheet."""
		self._instance.EditSketch = value

	@property
	def edit_template(self):
		"""Puts the template of the current drawing sheet in edit mode."""
		return self._instance.EditTemplate

	@edit_template.setter
	def edit_template(self, value):
		"""Puts the template of the current drawing sheet in edit mode."""
		self._instance.EditTemplate = value

	@property
	def end_drawing(self):
		"""Provides faster creation of entities in a drawing when used with IDrawingDoc::StartDrawing."""
		return self._instance.EndDrawing

	@end_drawing.setter
	def end_drawing(self, value):
		"""Provides faster creation of entities in a drawing when used with IDrawingDoc::StartDrawing."""
		self._instance.EndDrawing = value

	@property
	def feature_by_name(self):
		"""Gets the specified feature in the drawing."""
		return self._instance.FeatureByName

	@feature_by_name.setter
	def feature_by_name(self, value):
		"""Gets the specified feature in the drawing."""
		self._instance.FeatureByName = value

	@property
	def flip_section_line(self):
		"""Flips the cut direction of the selected section line."""
		return self._instance.FlipSectionLine

	@flip_section_line.setter
	def flip_section_line(self, value):
		"""Flips the cut direction of the selected section line."""
		self._instance.FlipSectionLine = value

	@property
	def generate_view_palette_views(self):
		"""Adds the specified document's predefined drawing views to the View Palette."""
		return self._instance.GenerateViewPaletteViews

	@generate_view_palette_views.setter
	def generate_view_palette_views(self, value):
		"""Adds the specified document's predefined drawing views to the View Palette."""
		self._instance.GenerateViewPaletteViews = value

	@property
	def get_current_sheet(self):
		"""Gets the currently active drawing sheet."""
		return self._instance.GetCurrentSheet

	@get_current_sheet.setter
	def get_current_sheet(self, value):
		"""Gets the currently active drawing sheet."""
		self._instance.GetCurrentSheet = value

	@property
	def get_drawing_palette_view_names(self):
		"""Gets the names of drawing views in the View Palette for the active drawing sheet."""
		return self._instance.GetDrawingPaletteViewNames

	@get_drawing_palette_view_names.setter
	def get_drawing_palette_view_names(self, value):
		"""Gets the names of drawing views in the View Palette for the active drawing sheet."""
		self._instance.GetDrawingPaletteViewNames = value

	@property
	def get_edit_sheet(self):
		"""Gets whether the current drawing is in edit sheet mode or edit template mode."""
		return self._instance.GetEditSheet

	@get_edit_sheet.setter
	def get_edit_sheet(self, value):
		"""Gets whether the current drawing is in edit sheet mode or edit template mode."""
		self._instance.GetEditSheet = value

	@property
	def get_first_view(self):
		"""Gets the first drawing view on the current sheet."""
		return self._instance.GetFirstView

	@get_first_view.setter
	def get_first_view(self, value):
		"""Gets the first drawing view on the current sheet."""
		self._instance.GetFirstView = value

	@property
	def get_insertion_point(self):
		"""Gets the current insertion (pick) point in a drawing."""
		return self._instance.GetInsertionPoint

	@get_insertion_point.setter
	def get_insertion_point(self, value):
		"""Gets the current insertion (pick) point in a drawing."""
		self._instance.GetInsertionPoint = value

	@property
	def get_line_font_count(self):
		"""Gets the a number line fonts supported by this drawing."""
		return self._instance.GetLineFontCount2

	@get_line_font_count.setter
	def get_line_font_count(self, value):
		"""Gets the a number line fonts supported by this drawing."""
		self._instance.GetLineFontCount2 = value

	@property
	def get_line_font_id(self):
		"""Gets the associated line font ID."""
		return self._instance.GetLineFontId

	@get_line_font_id.setter
	def get_line_font_id(self, value):
		"""Gets the associated line font ID."""
		self._instance.GetLineFontId = value

	@property
	def get_line_font_info(self):
		"""Gets the detailed information about the specified line font."""
		return self._instance.GetLineFontInfo2

	@get_line_font_info.setter
	def get_line_font_info(self, value):
		"""Gets the detailed information about the specified line font."""
		self._instance.GetLineFontInfo2 = value

	@property
	def get_line_font_name(self):
		"""Gets the name of the specified line font."""
		return self._instance.GetLineFontName2

	@get_line_font_name.setter
	def get_line_font_name(self, value):
		"""Gets the name of the specified line font."""
		self._instance.GetLineFontName2 = value

	@property
	def get_line_styles(self):
		"""Gets all of the line styles used in the current document."""
		return self._instance.GetLineStyles

	@get_line_styles.setter
	def get_line_styles(self, value):
		"""Gets all of the line styles used in the current document."""
		self._instance.GetLineStyles = value

	@property
	def get_pen_count(self):
		"""Gets the number of pens currently defined in SOLIDWORKS."""
		return self._instance.GetPenCount

	@get_pen_count.setter
	def get_pen_count(self, value):
		"""Gets the number of pens currently defined in SOLIDWORKS."""
		self._instance.GetPenCount = value

	@property
	def get_pen_info(self):
		"""Gets information about the pens used in SOLIDWORKS."""
		return self._instance.GetPenInfo

	@get_pen_info.setter
	def get_pen_info(self, value):
		"""Gets information about the pens used in SOLIDWORKS."""
		self._instance.GetPenInfo = value

	@property
	def get_sheet_count(self):
		"""Gets the number of drawing sheets in this drawing."""
		return self._instance.GetSheetCount

	@get_sheet_count.setter
	def get_sheet_count(self, value):
		"""Gets the number of drawing sheets in this drawing."""
		self._instance.GetSheetCount = value

	@property
	def get_sheet_names(self):
		"""Gets a list of the names of the drawing sheets in this drawing."""
		return self._instance.GetSheetNames

	@get_sheet_names.setter
	def get_sheet_names(self, value):
		"""Gets a list of the names of the drawing sheets in this drawing."""
		self._instance.GetSheetNames = value

	@property
	def get_view_count(self):
		"""Gets all of the number of all of views, including the number of sheets, in this drawing document."""
		return self._instance.GetViewCount

	@get_view_count.setter
	def get_view_count(self, value):
		"""Gets all of the number of all of views, including the number of sheets, in this drawing document."""
		self._instance.GetViewCount = value

	@property
	def get_views(self):
		"""Gets the all of the views, including the sheets, in this drawing document."""
		return self._instance.GetViews

	@get_views.setter
	def get_views(self, value):
		"""Gets the all of the views, including the sheets, in this drawing document."""
		self._instance.GetViews = value

	@property
	def hide_edge(self):
		"""Hides selected visible edges in a drawing document."""
		return self._instance.HideEdge

	@hide_edge.setter
	def hide_edge(self, value):
		"""Hides selected visible edges in a drawing document."""
		self._instance.HideEdge = value

	@property
	def hide_show_dimensions(self):
		"""Sets whether to display suppressed dimensions as dimmed and hide them."""
		return self._instance.HideShowDimensions

	@hide_show_dimensions.setter
	def hide_show_dimensions(self, value):
		"""Sets whether to display suppressed dimensions as dimmed and hide them."""
		self._instance.HideShowDimensions = value

	@property
	def hide_show_drawing_views(self):
		"""Sets whether to hide or show hidden drawing views."""
		return self._instance.HideShowDrawingViews

	@hide_show_drawing_views.setter
	def hide_show_drawing_views(self, value):
		"""Sets whether to hide or show hidden drawing views."""
		self._instance.HideShowDrawingViews = value

	@property
	def i_add_chamfer_dim(self):
		"""Adds a chamfer dimension."""
		return self._instance.IAddChamferDim

	@i_add_chamfer_dim.setter
	def i_add_chamfer_dim(self, value):
		"""Adds a chamfer dimension."""
		self._instance.IAddChamferDim = value

	@property
	def i_add_hole_callout(self):
		"""Adds a hole callout at the specified position to the hole whose edge is selected."""
		return self._instance.IAddHoleCallout2

	@i_add_hole_callout.setter
	def i_add_hole_callout(self, value):
		"""Adds a hole callout at the specified position to the hole whose edge is selected."""
		self._instance.IAddHoleCallout2 = value

	@property
	def i_create_ang_dim(self):
		"""Creates a non-associative angular dimension."""
		return self._instance.ICreateAngDim4

	@i_create_ang_dim.setter
	def i_create_ang_dim(self, value):
		"""Creates a non-associative angular dimension."""
		self._instance.ICreateAngDim4 = value

	@property
	def i_create_auxiliary_view_at(self):
		"""Creates an auxiliary view based on a selected edge in a drawing view."""
		return self._instance.ICreateAuxiliaryViewAt2

	@i_create_auxiliary_view_at.setter
	def i_create_auxiliary_view_at(self, value):
		"""Creates an auxiliary view based on a selected edge in a drawing view."""
		self._instance.ICreateAuxiliaryViewAt2 = value

	@property
	def i_create_diam_dim(self):
		"""Creates a non-associative diameter dimension."""
		return self._instance.ICreateDiamDim4

	@i_create_diam_dim.setter
	def i_create_diam_dim(self, value):
		"""Creates a non-associative diameter dimension."""
		self._instance.ICreateDiamDim4 = value

	@property
	def i_create_linear_dim(self):
		"""Creates a non-associative linear dimension."""
		return self._instance.ICreateLinearDim4

	@i_create_linear_dim.setter
	def i_create_linear_dim(self, value):
		"""Creates a non-associative linear dimension."""
		self._instance.ICreateLinearDim4 = value

	@property
	def i_create_ordinate_dim(self):
		"""Creates a non-associative ordinate dimension."""
		return self._instance.ICreateOrdinateDim4

	@i_create_ordinate_dim.setter
	def i_create_ordinate_dim(self, value):
		"""Creates a non-associative ordinate dimension."""
		self._instance.ICreateOrdinateDim4 = value

	@property
	def i_create_section_view_at(self):
		"""Creates a section view from the section line up to the specified distance at the specified distance."""
		return self._instance.ICreateSectionViewAt5

	@i_create_section_view_at.setter
	def i_create_section_view_at(self, value):
		"""Creates a section view from the section line up to the specified distance at the specified distance."""
		self._instance.ICreateSectionViewAt5 = value

	@property
	def i_create_text(self):
		"""Creates a note containing the specified text at a given location."""
		return self._instance.ICreateText2

	@i_create_text.setter
	def i_create_text(self, value):
		"""Creates a note containing the specified text at a given location."""
		self._instance.ICreateText2 = value

	@property
	def i_edit_selected_gtol(self):
		"""Gets the selected GTol to edit."""
		return self._instance.IEditSelectedGtol

	@i_edit_selected_gtol.setter
	def i_edit_selected_gtol(self, value):
		"""Gets the selected GTol to edit."""
		self._instance.IEditSelectedGtol = value

	@property
	def i_feature_by_name(self):
		"""Gets the specified feature in the drawing."""
		return self._instance.IFeatureByName

	@i_feature_by_name.setter
	def i_feature_by_name(self, value):
		"""Gets the specified feature in the drawing."""
		self._instance.IFeatureByName = value

	@property
	def i_get_current_sheet(self):
		"""Gets the currently active drawing sheet."""
		return self._instance.IGetCurrentSheet

	@i_get_current_sheet.setter
	def i_get_current_sheet(self, value):
		"""Gets the currently active drawing sheet."""
		self._instance.IGetCurrentSheet = value

	@property
	def i_get_first_view(self):
		"""Gets the first drawing view on the current sheet."""
		return self._instance.IGetFirstView

	@i_get_first_view.setter
	def i_get_first_view(self, value):
		"""Gets the first drawing view on the current sheet."""
		self._instance.IGetFirstView = value

	@property
	def i_get_insertion_point(self):
		"""Gets the current insertion (pick) point in a drawing."""
		return self._instance.IGetInsertionPoint

	@i_get_insertion_point.setter
	def i_get_insertion_point(self, value):
		"""Gets the current insertion (pick) point in a drawing."""
		self._instance.IGetInsertionPoint = value

	@property
	def i_get_pen_info(self):
		"""Gets information about the pens used in SOLIDWORKS."""
		return self._instance.IGetPenInfo

	@i_get_pen_info.setter
	def i_get_pen_info(self, value):
		"""Gets information about the pens used in SOLIDWORKS."""
		self._instance.IGetPenInfo = value

	@property
	def i_get_sheet_names(self):
		"""Gets a list of the names of the drawing sheets in this drawing."""
		return self._instance.IGetSheetNames

	@i_get_sheet_names.setter
	def i_get_sheet_names(self, value):
		"""Gets a list of the names of the drawing sheets in this drawing."""
		self._instance.IGetSheetNames = value

	@property
	def i_insert_dowel_symbol(self):
		"""Inserts a dowel pin symbol on the currently selected edge or edges."""
		return self._instance.IInsertDowelSymbol

	@i_insert_dowel_symbol.setter
	def i_insert_dowel_symbol(self, value):
		"""Inserts a dowel pin symbol on the currently selected edge or edges."""
		self._instance.IInsertDowelSymbol = value

	@property
	def i_insert_multi_jog_leader(self):
		"""Inserts a multi-jog leader."""
		return self._instance.IInsertMultiJogLeader3

	@i_insert_multi_jog_leader.setter
	def i_insert_multi_jog_leader(self, value):
		"""Inserts a multi-jog leader."""
		self._instance.IInsertMultiJogLeader3 = value

	@property
	def i_insert_revision_cloud(self):
		"""Inserts a revision cloud annotation with the specified shape into a view or sheet."""
		return self._instance.IInsertRevisionCloud

	@i_insert_revision_cloud.setter
	def i_insert_revision_cloud(self, value):
		"""Inserts a revision cloud annotation with the specified shape into a view or sheet."""
		self._instance.IInsertRevisionCloud = value

	@property
	def i_new_gtol(self):
		"""Creates a new GTol."""
		return self._instance.INewGtol

	@i_new_gtol.setter
	def i_new_gtol(self, value):
		"""Creates a new GTol."""
		self._instance.INewGtol = value

	@property
	def insert_angular_running_dim(self):
		"""Inserts an angular running dimension into this drawing."""
		return self._instance.InsertAngularRunningDim

	@insert_angular_running_dim.setter
	def insert_angular_running_dim(self, value):
		"""Inserts an angular running dimension into this drawing."""
		self._instance.InsertAngularRunningDim = value

	@property
	def insert_base_dim(self):
		"""Inserts the base model dimensions into this drawing."""
		return self._instance.InsertBaseDim

	@insert_base_dim.setter
	def insert_base_dim(self, value):
		"""Inserts the base model dimensions into this drawing."""
		self._instance.InsertBaseDim = value

	@property
	def insert_break_horizontal(self):
		"""Inserts a horizontal break in the drawing view."""
		return self._instance.InsertBreakHorizontal

	@insert_break_horizontal.setter
	def insert_break_horizontal(self, value):
		"""Inserts a horizontal break in the drawing view."""
		self._instance.InsertBreakHorizontal = value

	@property
	def insert_break_vertical(self):
		"""Inserts a vertical break in this drawing."""
		return self._instance.InsertBreakVertical

	@insert_break_vertical.setter
	def insert_break_vertical(self, value):
		"""Inserts a vertical break in this drawing."""
		self._instance.InsertBreakVertical = value

	@property
	def insert_center_line(self):
		"""Inserts a centerline on the selected entities."""
		return self._instance.InsertCenterLine2

	@insert_center_line.setter
	def insert_center_line(self, value):
		"""Inserts a centerline on the selected entities."""
		self._instance.InsertCenterLine2 = value

	@property
	def insert_center_mark(self):
		"""Inserts a center mark in a drawing document."""
		return self._instance.InsertCenterMark3

	@insert_center_mark.setter
	def insert_center_mark(self, value):
		"""Inserts a center mark in a drawing document."""
		self._instance.InsertCenterMark3 = value

	@property
	def insert_circular_note_pattern(self):
		"""Inserts a circular note pattern using the selected note."""
		return self._instance.InsertCircularNotePattern

	@insert_circular_note_pattern.setter
	def insert_circular_note_pattern(self, value):
		"""Inserts a circular note pattern using the selected note."""
		self._instance.InsertCircularNotePattern = value

	@property
	def insert_dowel_symbol(self):
		"""Inserts a dowel pin symbol on the currently selected edge or edges in this drawing."""
		return self._instance.InsertDowelSymbol

	@insert_dowel_symbol.setter
	def insert_dowel_symbol(self, value):
		"""Inserts a dowel pin symbol on the currently selected edge or edges in this drawing."""
		self._instance.InsertDowelSymbol = value

	@property
	def insert_group(self):
		"""Inserts the currently selected items into a group (or view)."""
		return self._instance.InsertGroup

	@insert_group.setter
	def insert_group(self, value):
		"""Inserts the currently selected items into a group (or view)."""
		self._instance.InsertGroup = value

	@property
	def insert_horizontal_ordinate(self):
		"""Inserts a horizontal ordinate dimension into this drawing."""
		return self._instance.InsertHorizontalOrdinate

	@insert_horizontal_ordinate.setter
	def insert_horizontal_ordinate(self, value):
		"""Inserts a horizontal ordinate dimension into this drawing."""
		self._instance.InsertHorizontalOrdinate = value

	@property
	def insert_linear_note_pattern(self):
		"""Inserts a linear note pattern using the selected note."""
		return self._instance.InsertLinearNotePattern

	@insert_linear_note_pattern.setter
	def insert_linear_note_pattern(self, value):
		"""Inserts a linear note pattern using the selected note."""
		self._instance.InsertLinearNotePattern = value

	@property
	def insert_model_annotations(self):
		"""Inserts model annotations into this drawing document in the currently selected drawing view."""
		return self._instance.InsertModelAnnotations3

	@insert_model_annotations.setter
	def insert_model_annotations(self, value):
		"""Inserts model annotations into this drawing document in the currently selected drawing view."""
		self._instance.InsertModelAnnotations3 = value

	@property
	def insert_model_dimensions(self):
		"""Inserts model dimensions into the selected drawing view according to the option specified."""
		return self._instance.InsertModelDimensions

	@insert_model_dimensions.setter
	def insert_model_dimensions(self, value):
		"""Inserts model dimensions into the selected drawing view according to the option specified."""
		self._instance.InsertModelDimensions = value

	@property
	def insert_model_in_predefined_view(self):
		"""Inserts the model into the predefined drawing views in the active drawing sheet."""
		return self._instance.InsertModelInPredefinedView

	@insert_model_in_predefined_view.setter
	def insert_model_in_predefined_view(self, value):
		"""Inserts the model into the predefined drawing views in the active drawing sheet."""
		self._instance.InsertModelInPredefinedView = value

	@property
	def insert_multi_jog_leader(self):
		"""Inserts a multi-jog leader."""
		return self._instance.InsertMultiJogLeader3

	@insert_multi_jog_leader.setter
	def insert_multi_jog_leader(self, value):
		"""Inserts a multi-jog leader."""
		self._instance.InsertMultiJogLeader3 = value

	@property
	def insert_new_note(self):
		"""Creates a new note in this drawing."""
		return self._instance.InsertNewNote2

	@insert_new_note.setter
	def insert_new_note(self, value):
		"""Creates a new note in this drawing."""
		self._instance.InsertNewNote2 = value

	@property
	def insert_ordinate(self):
		"""Inserts an ordinate dimension into this drawing."""
		return self._instance.InsertOrdinate

	@insert_ordinate.setter
	def insert_ordinate(self, value):
		"""Inserts an ordinate dimension into this drawing."""
		self._instance.InsertOrdinate = value

	@property
	def insert_ref_dim(self):
		"""Inserts reference dimensions in this drawing."""
		return self._instance.InsertRefDim

	@insert_ref_dim.setter
	def insert_ref_dim(self, value):
		"""Inserts reference dimensions in this drawing."""
		self._instance.InsertRefDim = value

	@property
	def insert_revision_cloud(self):
		"""Inserts a revision cloud annotation with the specified shape into a view or sheet."""
		return self._instance.InsertRevisionCloud

	@insert_revision_cloud.setter
	def insert_revision_cloud(self, value):
		"""Inserts a revision cloud annotation with the specified shape into a view or sheet."""
		self._instance.InsertRevisionCloud = value

	@property
	def insert_revision_symbol(self):
		"""Inserts a revision symbol note in this drawing."""
		return self._instance.InsertRevisionSymbol

	@insert_revision_symbol.setter
	def insert_revision_symbol(self, value):
		"""Inserts a revision symbol note in this drawing."""
		self._instance.InsertRevisionSymbol = value

	@property
	def insert_table_annotation(self):
		"""Inserts a table annotation in this drawing."""
		return self._instance.InsertTableAnnotation2

	@insert_table_annotation.setter
	def insert_table_annotation(self, value):
		"""Inserts a table annotation in this drawing."""
		self._instance.InsertTableAnnotation2 = value

	@property
	def insert_thread_callout(self):
		"""Inserts a thread callout into this drawing."""
		return self._instance.InsertThreadCallout

	@insert_thread_callout.setter
	def insert_thread_callout(self, value):
		"""Inserts a thread callout into this drawing."""
		self._instance.InsertThreadCallout = value

	@property
	def insert_vertical_ordinate(self):
		"""Inserts a vertical ordinate dimension in this drawing."""
		return self._instance.InsertVerticalOrdinate

	@insert_vertical_ordinate.setter
	def insert_vertical_ordinate(self, value):
		"""Inserts a vertical ordinate dimension in this drawing."""
		self._instance.InsertVerticalOrdinate = value

	@property
	def insert_weld_symbol(self):
		"""Creates a weld symbol located at the last edge selection."""
		return self._instance.InsertWeldSymbol

	@insert_weld_symbol.setter
	def insert_weld_symbol(self, value):
		"""Creates a weld symbol located at the last edge selection."""
		self._instance.InsertWeldSymbol = value

	@property
	def i_reorder_sheets(self):
		"""Reorders the drawing sheets per their positions in the input array."""
		return self._instance.IReorderSheets

	@i_reorder_sheets.setter
	def i_reorder_sheets(self, value):
		"""Reorders the drawing sheets per their positions in the input array."""
		self._instance.IReorderSheets = value

	@property
	def is_detailing_mode(self):
		"""Gets whether this drawing is in detailing mode."""
		return self._instance.IsDetailingMode

	@is_detailing_mode.setter
	def is_detailing_mode(self, value):
		"""Gets whether this drawing is in detailing mode."""
		self._instance.IsDetailingMode = value

	@property
	def isolate_changed_dimensions(self):
		"""Isolates changed dimensions."""
		return self._instance.IsolateChangedDimensions

	@isolate_changed_dimensions.setter
	def isolate_changed_dimensions(self, value):
		"""Isolates changed dimensions."""
		self._instance.IsolateChangedDimensions = value

	@property
	def load_line_styles(self):
		"""Loads the specified line styles into the current drawing."""
		return self._instance.LoadLineStyles

	@load_line_styles.setter
	def load_line_styles(self, value):
		"""Loads the specified line styles into the current drawing."""
		self._instance.LoadLineStyles = value

	@property
	def make_section_line(self):
		"""Makes a section line from a set of connected sketch lines."""
		return self._instance.MakeSectionLine

	@make_section_line.setter
	def make_section_line(self, value):
		"""Makes a section line from a set of connected sketch lines."""
		self._instance.MakeSectionLine = value

	@property
	def modify_surface_finish_symbol(self):
		"""Modifies the selected surface finish symbol."""
		return self._instance.ModifySurfaceFinishSymbol

	@modify_surface_finish_symbol.setter
	def modify_surface_finish_symbol(self, value):
		"""Modifies the selected surface finish symbol."""
		self._instance.ModifySurfaceFinishSymbol = value

	@property
	def new_gtol(self):
		"""Creates a new GTol object and returns the pointer to that object."""
		return self._instance.NewGtol

	@new_gtol.setter
	def new_gtol(self, value):
		"""Creates a new GTol object and returns the pointer to that object."""
		self._instance.NewGtol = value

	@property
	def new_note(self):
		"""Creates a new note at the selected location."""
		return self._instance.NewNote

	@new_note.setter
	def new_note(self, value):
		"""Creates a new note at the selected location."""
		self._instance.NewNote = value

	@property
	def new_sheet(self):
		"""Creates a new drawing sheet in this drawing document."""
		return self._instance.NewSheet4

	@new_sheet.setter
	def new_sheet(self, value):
		"""Creates a new drawing sheet in this drawing document."""
		self._instance.NewSheet4 = value

	@property
	def on_component_properties(self):
		"""Displays the Component Properties dialog for the selected view."""
		return self._instance.OnComponentProperties

	@on_component_properties.setter
	def on_component_properties(self, value):
		"""Displays the Component Properties dialog for the selected view."""
		self._instance.OnComponentProperties = value

	@property
	def paste_sheet(self):
		"""Copies and pastes a drawing sheet to the specified location of the drawing document, optionally renaming whenever duplicate names occur."""
		return self._instance.PasteSheet

	@paste_sheet.setter
	def paste_sheet(self, value):
		"""Copies and pastes a drawing sheet to the specified location of the drawing document, optionally renaming whenever duplicate names occur."""
		self._instance.PasteSheet = value

	@property
	def reorder_sheets(self):
		"""Reorders the drawing sheets per their positions in the input array."""
		return self._instance.ReorderSheets

	@reorder_sheets.setter
	def reorder_sheets(self, value):
		"""Reorders the drawing sheets per their positions in the input array."""
		self._instance.ReorderSheets = value

	@property
	def replace_view_model(self):
		"""Replaces the specified instances of a model in the specified drawing views."""
		return self._instance.ReplaceViewModel

	@replace_view_model.setter
	def replace_view_model(self, value):
		"""Replaces the specified instances of a model in the specified drawing views."""
		self._instance.ReplaceViewModel = value

	@property
	def resolve_out_of_date_light_weight_components(self):
		"""Resolves out-of-date lightweight components in the selected drawing view or drawing sheet."""
		return self._instance.ResolveOutOfDateLightWeightComponents

	@resolve_out_of_date_light_weight_components.setter
	def resolve_out_of_date_light_weight_components(self, value):
		"""Resolves out-of-date lightweight components in the selected drawing view or drawing sheet."""
		self._instance.ResolveOutOfDateLightWeightComponents = value

	@property
	def restore_rotation(self):
		"""Restores rotation for the selected drawing view."""
		return self._instance.RestoreRotation

	@restore_rotation.setter
	def restore_rotation(self, value):
		"""Restores rotation for the selected drawing view."""
		self._instance.RestoreRotation = value

	@property
	def save_line_styles(self):
		"""Exports to a file the specified line styles in the current drawing."""
		return self._instance.SaveLineStyles

	@save_line_styles.setter
	def save_line_styles(self, value):
		"""Exports to a file the specified line styles in the current drawing."""
		self._instance.SaveLineStyles = value

	@property
	def set_current_layer(self):
		"""Sets the current layer used by this document."""
		return self._instance.SetCurrentLayer

	@set_current_layer.setter
	def set_current_layer(self, value):
		"""Sets the current layer used by this document."""
		self._instance.SetCurrentLayer = value

	@property
	def set_line_color(self):
		"""Sets the line color for a selected edge or sketch entity."""
		return self._instance.SetLineColor

	@set_line_color.setter
	def set_line_color(self, value):
		"""Sets the line color for a selected edge or sketch entity."""
		self._instance.SetLineColor = value

	@property
	def set_line_style(self):
		"""Sets the style or font for the line for a selected edge or sketch entity."""
		return self._instance.SetLineStyle

	@set_line_style.setter
	def set_line_style(self, value):
		"""Sets the style or font for the line for a selected edge or sketch entity."""
		self._instance.SetLineStyle = value

	@property
	def set_line_width(self):
		"""Sets the line thickness for a selected edge or sketch entity to a SOLIDWORKS-supplied weight (width)."""
		return self._instance.SetLineWidth

	@set_line_width.setter
	def set_line_width(self, value):
		"""Sets the line thickness for a selected edge or sketch entity to a SOLIDWORKS-supplied weight (width)."""
		self._instance.SetLineWidth = value

	@property
	def set_line_width_custom(self):
		"""Sets the line thickness to the specified custom width for a selected edge or sketch entity."""
		return self._instance.SetLineWidthCustom

	@set_line_width_custom.setter
	def set_line_width_custom(self, value):
		"""Sets the line thickness to the specified custom width for a selected edge or sketch entity."""
		self._instance.SetLineWidthCustom = value

	@property
	def set_sheets_selected(self):
		"""Sets the specified drawing sheets whose setups to modify."""
		return self._instance.SetSheetsSelected

	@set_sheets_selected.setter
	def set_sheets_selected(self, value):
		"""Sets the specified drawing sheets whose setups to modify."""
		self._instance.SetSheetsSelected = value

	@property
	def setup_sheet(self):
		"""Sets up the specified drawing sheet."""
		return self._instance.SetupSheet6

	@setup_sheet.setter
	def setup_sheet(self, value):
		"""Sets up the specified drawing sheet."""
		self._instance.SetupSheet6 = value

	@property
	def sheet_next(self):
		"""Moves to the next sheet in the drawing."""
		return self._instance.SheetNext

	@sheet_next.setter
	def sheet_next(self, value):
		"""Moves to the next sheet in the drawing."""
		self._instance.SheetNext = value

	@property
	def sheet_previous(self):
		"""Returns to the previous sheet in a drawing."""
		return self._instance.SheetPrevious

	@sheet_previous.setter
	def sheet_previous(self, value):
		"""Returns to the previous sheet in a drawing."""
		self._instance.SheetPrevious = value

	@property
	def show_edge(self):
		"""Shows the selected hidden edges in a drawing document."""
		return self._instance.ShowEdge

	@show_edge.setter
	def show_edge(self, value):
		"""Shows the selected hidden edges in a drawing document."""
		self._instance.ShowEdge = value

	@property
	def sketch_dim(self):
		"""Inserts a sketch dimension in this drawing."""
		return self._instance.SketchDim

	@sketch_dim.setter
	def sketch_dim(self, value):
		"""Inserts a sketch dimension in this drawing."""
		self._instance.SketchDim = value

	@property
	def start_drawing(self):
		"""Provides faster creation of entities within a drawing."""
		return self._instance.StartDrawing

	@start_drawing.setter
	def start_drawing(self, value):
		"""Provides faster creation of entities within a drawing."""
		self._instance.StartDrawing = value

	@property
	def suppress_view(self):
		"""Hides the selected drawing view."""
		return self._instance.SuppressView

	@suppress_view.setter
	def suppress_view(self, value):
		"""Hides the selected drawing view."""
		self._instance.SuppressView = value

	@property
	def translate_drawing(self):
		"""Translates the entire drawing."""
		return self._instance.TranslateDrawing

	@translate_drawing.setter
	def translate_drawing(self, value):
		"""Translates the entire drawing."""
		self._instance.TranslateDrawing = value

	@property
	def un_break_view(self):
		"""Removes a break in the selected drawing view."""
		return self._instance.UnBreakView

	@un_break_view.setter
	def un_break_view(self, value):
		"""Removes a break in the selected drawing view."""
		self._instance.UnBreakView = value

	@property
	def unsuppress_view(self):
		"""Hides the selected drawing view."""
		return self._instance.UnsuppressView

	@unsuppress_view.setter
	def unsuppress_view(self, value):
		"""Hides the selected drawing view."""
		self._instance.UnsuppressView = value

	@property
	def view_display_hidden(self):
		"""Sets the current display mode to Hidden Lines Removed."""
		return self._instance.ViewDisplayHidden

	@view_display_hidden.setter
	def view_display_hidden(self, value):
		"""Sets the current display mode to Hidden Lines Removed."""
		self._instance.ViewDisplayHidden = value

	@property
	def view_display_hiddengreyed(self):
		"""Sets the current display mode to Hidden Lines Visible."""
		return self._instance.ViewDisplayHiddengreyed

	@view_display_hiddengreyed.setter
	def view_display_hiddengreyed(self, value):
		"""Sets the current display mode to Hidden Lines Visible."""
		self._instance.ViewDisplayHiddengreyed = value

	@property
	def view_display_shaded(self):
		"""Sets the current display mode to Shaded."""
		return self._instance.ViewDisplayShaded

	@view_display_shaded.setter
	def view_display_shaded(self, value):
		"""Sets the current display mode to Shaded."""
		self._instance.ViewDisplayShaded = value

	@property
	def view_display_wireframe(self):
		"""Sets the current display mode to Wireframe."""
		return self._instance.ViewDisplayWireframe

	@view_display_wireframe.setter
	def view_display_wireframe(self, value):
		"""Sets the current display mode to Wireframe."""
		self._instance.ViewDisplayWireframe = value

	@property
	def view_full_page(self):
		"""Fits the drawing to the full page."""
		return self._instance.ViewFullPage

	@view_full_page.setter
	def view_full_page(self, value):
		"""Fits the drawing to the full page."""
		self._instance.ViewFullPage = value

	@property
	def view_hlr_quality(self):
		"""Toggles the Hidden Lines Removed mode for the drawing view."""
		return self._instance.ViewHlrQuality

	@view_hlr_quality.setter
	def view_hlr_quality(self, value):
		"""Toggles the Hidden Lines Removed mode for the drawing view."""
		self._instance.ViewHlrQuality = value

	@property
	def view_model_edges(self):
		"""Toggles the mode for viewing model edges when in shaded mode."""
		return self._instance.ViewModelEdges

	@view_model_edges.setter
	def view_model_edges(self, value):
		"""Toggles the mode for viewing model edges when in shaded mode."""
		self._instance.ViewModelEdges = value

	@property
	def view_tangent_edges(self):
		"""Toggles display of tangent edges in the selected drawing view."""
		return self._instance.ViewTangentEdges

	@view_tangent_edges.setter
	def view_tangent_edges(self, value):
		"""Toggles display of tangent edges in the selected drawing view."""
		self._instance.ViewTangentEdges = value

