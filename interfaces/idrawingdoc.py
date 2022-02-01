from interfaces.isheet import ISheet


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html

class IDrawingDoc:
    def __init__(self, system_object):
        self.system_object = system_object

    @property
    def _instance(self):
        return self.system_object

    @property
    def active_drawing_view(self):
        return self._instance.ActiveDrawingView

    def sheet(self, name='Sheet1'):
        return ISheet(self._instance.Sheet(name))

    def activate_sheet(self, name):
        """
        Activates the specified drawing sheet.
        :param name: Name of the sheet
        """
        # return self._instance.ActivateSheet(name)
        raise NotImplemented

    def activate_view(self, view_name):
        """
        Activates the specified drawing view.
        :param view_name: Name of the drawing view
        """
        # return self._instance.ActivateView(view_name)
        raise NotImplemented

    def add_chamfer_dim(self, x, y, z):
        """
        Adds a chamfer dimension.
        :param x: X dimension
        :param y: Y dimension
        :param z: Z dimension
        """
        # return self._instance.AddChamferDim(x, y, z)
        raise NotImplemented

    def add_hole_callout(self, x, y, z):
        """
        Adds a hole callout at the specified position to the hole whose edge is selected.
        :param x: X position of hole callout in meters
        :param y: Y position of hole callout in meters
        :param z: Z position of hole callout in meters
        """
        # return self._instance.AddHoleCallout2(x, y, z)
        raise NotImplemented

    def add_line_style(self, style_name, style_definition):
        """
        Adds a line style to the current drawing.
        :param style_name: Name of line style
        :param style_definition: Comma-delimited string of line lengths and spacing values for the line style
        """
        # return self._instance.AddLineStyle(style_name, style_definition)
        raise NotImplemented

    def align_horz(self):
        """Uses the selected edge to align the current drawing view."""
        # return self._instance.AlignHorz
        raise NotImplemented

    def align_ordinate(self):
        """Aligns the ordinate dimension."""
        # return self._instance.AlignOrdinate
        raise NotImplemented

    def align_vert(self):
        """Uses the selected edge to align the current drawing view."""
        # return self._instance.AlignVert
        raise NotImplemented

    def attach_annotation(self, option):
        """
        Attaches an existing annotation to a drawing sheet or view.
        :param option: Annotation attachment option as defined in swAttachAnnotationOption_e
        """
        # return self._instance.AttachAnnotation(option)
        raise NotImplemented

    def attach_dimensions(self):
        """Attaches unattached dimensions."""
        # return self._instance.AttachDimensions
        raise NotImplemented

    def auto_balloon(self, balloon_options):
        """
        Automatically inserts BOM balloons in selected drawing views.
        :param balloon_options: IAutoBalloonOptions
        """
        # return self._instance.AutoBalloon5(balloon_options)
        raise NotImplemented

    def auto_dimension(self, entities_to_dimension, horizontal_scheme, horizontal_placement, vertical_scheme,
                       vertical_placement):
        """
        Automatically dimensions the selected drawing view.
        :param entities_to_dimension: Entities to dimension as defined in swAutodimEntities_e
        :param horizontal_scheme: Horizontal dimensioning scheme as defined in swAutodimScheme_e
        :param horizontal_placement: Placement relative to the drawing view as defined in swAutodimHorizontalPlacement_e
        :param vertical_scheme: Vertical dimensioning scheme as defined in swAutodimScheme_e
        :param vertical_placement: Placement relative to the drawing view as defined in swAutodimVerticalPlacement_e
        """
        # return self._instance.AutoDimension(entities_to_dimension, horizontal_scheme, horizontal_placement,
        # vertical_scheme, vertical_placement)
        raise NotImplemented

    def break_view(self):
        """Breaks the drawing view along the existing break lines."""
        # return self._instance.BreakView
        raise NotImplemented

    def change_component_layer(self, layername, all_views):
        """
        Puts the selected components on the specified layer.
        :param layername: Name of layer for components
        :param all_views: True changes the component layer for all views in the drawing, false changes only the selected
        view
        """
        # return self._instance.ChangeComponentLayer(layername, all_views)
        raise NotImplemented

    def change_ord_dir(self):
        """Changes the ordinate direction."""
        # return self._instance.ChangeOrdDir
        raise NotImplemented

    def change_ref_configuration_of_flat_pattern_view(self, model_name, config_name):
        """
        Changes the referenced configuration of the flat-pattern view.
        :param model_name: Name of the model in the flat-pattern view
        :param config_name: Name of the configuration
        """
        # return self._instance.ChangeRefConfigurationOfFlatPatternView(model_name, config_name)
        raise NotImplemented

    def createst_angle_views(self, model_name):
        """
        Creates standard three orthographic views (first angle projection) for the specified model.
        :param model_name: Name of the document from which to create views
        """
        # return self._instance.Create1stAngleViews2(model_name)
        raise NotImplemented

    def createrd_angle_views(self, model_name):
        """
        Creates standard three orthographic views (third angle projection) for the specified model.
        :param model_name: Name of the document from which to create views
        """
        # return self._instance.Create3rdAngleViews2(model_name)
        raise NotImplemented

    def create_ang_dim(self, p0, p1, p2, p3, p4, p5, p6, text_point, text_height):
        """
        Creates a non-associative angular dimension.
        :param p0: Array of 3 doubles (x,y,z); dimension end point
        :param p1: Array of 3 doubles (x,y,z); dimension point
        :param p2: Array of 3 doubles (x,y,z); extension1 start point
        :param p3: Array of 3 doubles (x,y,z); extension1 end point
        :param p4: Array of 3 doubles (x,y,z); extension2 start point
        :param p5: Array of 3 doubles (x,y,z); extension2 end point
        :param p6: Array of 3 doubles (x,y,z); plane normal
        :param text_point: Array�of 3 doubles (x,y,z); position of text
        :param text_height: Text height in meters
        """
        # return self._instance.CreateAngDim4(p0, p1, p2, p3, p4, p5, p6, text_point, text_height)
        raise NotImplemented

    def create_auto_balloon_options(self):
        """Creates an object that stores auto balloon options."""
        # return self._instance.CreateAutoBalloonOptions
        raise NotImplemented

    def create_auxiliary_view_at(self, x, y, z, not_aligned, label, showarrow, flip):
        """
        Creates an auxiliary view based on a selected edge in a drawing view.
        :param x: X position for the auxiliary view
        :param y: Y position for the auxiliary view
        :param z: Z position for the auxiliary view
        :param not_aligned: True aligns the view from its owner, false does not
        :param label: String that holds label of the auxiliary view
        :param showarrow: True shows the arrow, false hides the arrow
        :param flip: True flips the side shown in the auxiliary view, false does not
        """
        # return self._instance.CreateAuxiliaryViewAt2(x, y, z, not_aligned, label, showarrow, flip)
        raise NotImplemented

    def create_break_out_section(self, depth):
        """
        Creates a broken-out section in a drawing document.
        :param depth: Depth of the broken-out section
        """
        # return self._instance.CreateBreakOutSection(depth)
        raise NotImplemented

    def create_construction_geometry(self):
        """Sets the selected sketch segments to be construction geometry instead of sketch geometry."""
        # return self._instance.CreateConstructionGeometry
        raise NotImplemented

    def create_detail_view_at(self, x, y, z, style, scale1, scale2, label_in, showtype, full_outline, jagged_outline,
                              no_outline, shape_intensity):
        """
        Creates a detail view in a drawing document.
        :param x: X position for the detail view
        :param y: Y position for the detail view
        :param z: Z position for the detail view
        :param style: Style for the detail view as defined in swDetViewStyle_e
        :param scale1: Scale numerator
        :param scale2: Scale denominator
        :param label_in: Detail view label
        :param showtype: Type of sketch for the detail view�as defined in swDetCircleShowType_e
        :param full_outline: True to�show a full outline, false to not; valid only if NoOutline is false
        :param jagged_outline: True to show a jagged outline, false to not; only valid if NoOutline is false
        :param no_outline: True to not show an outline, false to show an outline
        :param shape_intensity: Intensity of jagged outline; valid range is 1 (most) to 5 (least) and only valid if
        JaggedOutline is true and NoOutline is false
        """
        # return self._instance.CreateDetailViewAt4(x, y, z, style, scale1, scale2, label_in, showtype, full_outline,
        # jagged_outline, no_outline, shape_intensity)
        raise NotImplemented

    def create_diam_dim(self, p0, p1, p2, p3, text_point, val, text_height):
        """
        Creates a non-associative diameter dimension.
        :param p0: Array of�3 doubles (x,y,z); location of dimension point
        :param p1: Array of 3 doubles (x,y,z); nearest point on circle
        :param p2: Array of 3 doubles (x,y,z); farthest point on circle diametrically opposite to P1
        :param p3: Array of 3 doubles (x,y,z); plane normal
        :param text_point: Array of 3 doubles (x,y,z); position of text
        :param val: Dimension value in meters
        :param text_height: Text height in meters
        """
        # return self._instance.CreateDiamDim4(p0, p1, p2, p3, text_point, val, text_height)
        raise NotImplemented

    def create_draw_view_from_model_view(self, model_name, view_name, loc_x, loc_y, loc_z):
        """
        Creates a drawing view on the current drawing sheet using the specified model view.
        :param model_name: Full pathname of the model document for which to create the drawing view (see Remarks)
        :param view_name: Name of the model view from which to create the drawing view (see Remarks)
        :param loc_x: x location of drawing view center in meters
        :param loc_y: y location of drawing view center in meters
        :param loc_z: z location of drawing view center in meters
        """
        # return self._instance.CreateDrawViewFromModelView3(model_name, view_name, loc_x, loc_y, loc_z)
        raise NotImplemented

    def create_flat_pattern_view_from_model_view(self, model_name, config_name, loc_x, loc_y, loc_z, hide_bend_lines,
                                                 flip_view):
        """
        Creates a flat-pattern view from a model view.
        :param model_name: Name of model
        :param config_name: Name of configuration
        :param loc_x: X coordinate
        :param loc_y: Y coordinate
        :param loc_z: Z coordinate
        :param hide_bend_lines: True hides bend lines,�false does not
        :param flip_view: True flips the view,�false does not
        """
        # return self._instance.CreateFlatPatternViewFromModelView3(model_name, config_name, loc_x, loc_y, loc_z,
        # hide_bend_lines, flip_view)
        raise NotImplemented

    def create_layer(self, layername, layer_desc, layer_color, layer_style, layer_width, b_on, b_print):
        """
        Creates a layer for this document.
        :param layername: Layer name (see Remarks)
        :param layer_desc: Description for the new layer
        :param layer_color: COLORREF value specifying the color of items in this layer
        :param layer_style: Line style as defined in swLineStyles_e
        :param layer_width: Line width as defined in swLineWeights_e
        :param b_on: True makes this layer visible, false makes it invisible
        :param b_print: True to print this layer when printing the document, false to not
        """
        # return self._instance.CreateLayer2(layername, layer_desc, layer_color, layer_style, layer_width, b_on,
        # b_print)
        raise NotImplemented

    def create_linear_dim(self, p0, p1, p2, p3, p4, text_point, val, angle, text_height):
        """
        Creates a non-associative linear dimension.
        :param p0: Array�of 3 doubles (x,y,z), dimension point
        :param p1: Array of 3 doubles (x,y,z), dimension end
        :param p2: Array of 3 doubles (x,y,z), normal to the plane of sketch
        :param p3: Array of 3 doubles (x,y,z), extension line 1 reference point
        :param p4: Array of 3 doubles (x,y,z), extension line 2 reference point
        :param text_point: Array of 3 doubles (x,y,z), position of text
        :param val: Value for the non-associative linear dimension
        :param angle: Inclination angle of the text in radians
        :param text_height: Text height in meters
        """
        # return self._instance.CreateLinearDim4(p0, p1, p2, p3, p4, text_point, val, angle, text_height)
        raise NotImplemented

    def create_ordinate_dim(self, p0, p1, p2, p3, p4, p5, val, angle, text_height):
        """
        Creates a non-associative ordinate dimension.
        :param p0: Array�of 3 doubles (x,y,z); dimension point
        :param p1: Array�of 3 doubles (x,y,z); unit vector that specifies the direction of the ordinate dimension
        :param p2: Array�of 3 doubles (x,y,z); extension line start point
        :param p3: Array�of 3 doubles (x,y,z); extension line end point
        :param p4: Array of 3 doubles (x,y,z); unit vector and specifies the orientation of the text; for example,
        (1, 0, 0) results in horizontal text read from left to right
        :param p5: Array of 3 doubles (x,y,z); position of text
        :param val: Value for the ordinate dimension
        :param angle: Inclination angle of the text in radians (character slant)
        :param text_height: Text height in meters
        """
        # return self._instance.CreateOrdinateDim4(p0, p1, p2, p3, p4, p5, val, angle, text_height)
        raise NotImplemented

    def create_relative_view(self, model_name, x_pos, y_pos, view_dir_front, view_dir_right):
        """
        Creates a relative drawing view.
        :param model_name: Path and filename of the model for which to create a relative drawing view
        :param x_pos: x coordinate where to create the relative drawing view
        :param y_pos: y coordinate where to create a relative drawing view
        :param view_dir_front: Orientation as defined by swRelativeViewCreationDirection_e
        :param view_dir_right: Orientation as defined by swRelativeViewCreationDirection_e
        """
        # return self._instance.CreateRelativeView(model_name, x_pos, y_pos, view_dir_front, view_dir_right)
        raise NotImplemented

    def create_section_view(self):
        """Creates a section view in the drawing using the selected section line."""
        # return self._instance.CreateSectionView
        raise NotImplemented

    def create_section_view_at(self, x, y, z, section_label, options, excluded_components, section_depth):
        """
        Creates the specified section view.
        :param x: x�position on the drawing sheet for the center of the section view
        :param y: y position on the drawing sheet for the center of the section view
        :param z: z position on the drawing sheet for the center of the section view
        :param section_label: Letter for the label for the section view
        :param options: Options that affect the section view as defined in swCreateSectionViewAtOptions_e
        :param excluded_components: Array of components to exclude from the section view
        :param section_depth: Distance from the selected section line (see Remarks)
        """
        # return self._instance.CreateSectionViewAt5(x, y, z, section_label, options, excluded_components,
        # section_depth)
        raise NotImplemented

    def create_text(self, text_string, text_x, text_y, text_z, text_height, text_angle):
        """
        Creates a note containing the specified text at a given location.
        :param text_string: User input text
        :param text_x: X text location in meters (see Remarks)
        :param text_y: Y text location in meters (see Remarks)
        :param text_z: Z text location in meters (see Remarks)
        :param text_height: Text height in meters
        :param text_angle: Text angle for rotated text in radians
        """
        return self._instance.CreateText2(text_string, text_x, text_y, text_z, text_height, text_angle)

    def create_unfolded_view_at(self, x, y, z, not_aligned):
        """
        Creates an unfolded drawing view from the selected drawing view and places it in the drawing at the specified
        location.
        :param x: x position in the drawing sheet space for the center of the drawing view
        :param y: y position in the drawing sheet space for the center of the drawing view
        :param z: z position in the drawing sheet space for the center of the drawing view
        :param not_aligned: True if you want to break the alignment with the parent view, false if you want to keep the
        view aligned with the parent view
        """
        # return self._instance.CreateUnfoldedViewAt3(x, y, z, not_aligned)
        raise NotImplemented

    def create_viewport(self, lower_left_x, lower_left_y, sketch_size, scale):
        """
        Creates a an empty view in a drawing.
        :param lower_left_x: x value for lower-left coordinate for the view
        :param lower_left_y: y value for lower-left coordinate for the view
        :param sketch_size: Approximate number of entries
        :param scale: Scale to use for the view
        """
        # return self._instance.CreateViewport3(lower_left_x, lower_left_y, sketch_size, scale)
        raise NotImplemented

    def delete_all_cosmetic_threads(self):
        """Deletes all cosmetic threads, which do not have callouts, in a drawing of an assembly only."""
        # return self._instance.DeleteAllCosmeticThreads
        raise NotImplemented

    def delete_line_style(self, style_name, replace_name):
        """
        Deletes the specified line style from the current drawing.
        :param style_name: Name of line style to delete
        :param replace_name: Name of line style to replace deleted StyleName
        """
        # return self._instance.DeleteLineStyle(style_name, replace_name)
        raise NotImplemented

    def dimensions(self):
        """Adds dimensions to the drawing from model."""
        # return self._instance.Dimensions
        raise NotImplemented

    def drag_model_dimension(self, view_name, drop_effect, x, y, z):
        """
        Copies or moves dimensions to a different drawing view.
        :param view_name: Name of the drawing view to which you want to copy or move the selected model dimension
        :param drop_effect:
    Copy = 1

    Move = 2
        :param x: X location in sheet space for the newly copied or moved dimension
        :param y: Y location in sheet space for the newly copied or moved dimension
        :param z: Z location in sheet space for the newly copied or moved dimension; set to� 0
        """
        # return self._instance.DragModelDimension(view_name, drop_effect, x, y, z)
        raise NotImplemented

    def drawing_view_rotate(self, new_angle):
        """
        Rotates the selected drawing view.
        :param new_angle: New angle value for the drawing view
        """
        # return self._instance.DrawingViewRotate(new_angle)
        raise NotImplemented

    def drop_drawing_view_from_palette(self, palette_view_name, x, y, z):
        """
        Moves the specified drawing view from the View Palette to the current drawing sheet.
        :param palette_view_name: Name of the drawing view to move to the drawing sheet
        :param x: x coordinate where to drop the drawing view
        :param y: y coordinate where to drop the drawing view
        :param z: z coordinate where to drop the drawing view; this coordinate is always 0
        """
        # return self._instance.DropDrawingViewFromPalette2(palette_view_name, x, y, z)
        raise NotImplemented

    def edit_center_mark_properties(self, angle, size, lines, doc_settings):
        """
        Edits center mark properties.
        :param angle: New angle of the center mark
        :param size: New size of the center mark
        :param lines: True displays the center mark lines, false displays the plus sign (+) at the circlecenter
        :param doc_settings: True uses the default settings for this document, false does not
        """
        # return self._instance.EditCenterMarkProperties(angle, size, lines, doc_settings)
        raise NotImplemented

    def edit_ordinate(self):
        """Edits an ordinate dimension."""
        # return self._instance.EditOrdinate
        raise NotImplemented

    def edit_selected_gtol(self):
        """Gets the selected GTol to edit."""
        # return self._instance.EditSelectedGtol
        raise NotImplemented

    def edit_sheet(self):
        """Puts the current drawing sheet in edit mode."""
        # return self._instance.EditSheet
        raise NotImplemented

    def edit_sketch(self):
        """Allows editing of a sketch in the selected drawing view or sheet."""
        # return self._instance.EditSketch
        raise NotImplemented

    def edit_template(self):
        """Puts the template of the current drawing sheet in edit mode."""
        # return self._instance.EditTemplate
        raise NotImplemented

    def end_drawing(self):
        """Provides faster creation of entities in a drawing when used with IDrawingDoc::StartDrawing."""
        # return self._instance.EndDrawing
        raise NotImplemented

    def feature_by_name(self, name):
        """
        Gets the specified feature in the drawing.
        :param name: Name of the feature
        """
        return self._instance.FeatureByName(name)

    def flip_section_line(self):
        """Flips the cut direction of the selected section line."""
        # return self._instance.FlipSectionLine
        raise NotImplemented

    def generate_view_palette_views(self, file_name):
        """
        Adds the specified document's predefined drawing views to the View Palette.
        :param file_name: Path and file name of the document from which to add the predefined drawing views to the View
        Palette
        """
        # return self._instance.GenerateViewPaletteViews(file_name)
        raise NotImplemented

    def get_current_sheet(self):
        """Gets the currently active drawing sheet."""
        return ISheet(self._instance.GetCurrentSheet)

    def get_drawing_palette_view_names(self):
        """Gets the names of drawing views in the View Palette for the active drawing sheet."""
        # return self._instance.GetDrawingPaletteViewNames
        raise NotImplemented

    def get_edit_sheet(self):
        """Gets whether the current drawing is in edit sheet mode or edit template mode."""
        # return self._instance.GetEditSheet
        raise NotImplemented

    def get_first_view(self):
        """Gets the first drawing view on the current sheet."""
        # return self._instance.GetFirstView
        raise NotImplemented

    def get_insertion_point(self):
        """Gets the current insertion (pick) point in a drawing."""
        # return self._instance.GetInsertionPoint
        raise NotImplemented

    def get_line_font_count(self):
        """Gets the a number line fonts supported by this drawing."""
        # return self._instance.GetLineFontCount2
        raise NotImplemented

    def get_line_font_id(self, index):
        """
        Gets the associated line font ID.
        :param index: Index position of the line font which is within the index range returned by
        IDrawingDoc::GetLineFontCount2
        """
        # return self._instance.GetLineFontId(index)
        raise NotImplemented

    def get_line_font_info(self, index):
        """
        Gets the detailed information about the specified line font.
        :param index: Index position of the line font which is within the index range returned by
        IDrawingDoc::GetLineFontCount2
        """
        # return self._instance.GetLineFontInfo2(index)
        raise NotImplemented

    def get_line_font_name(self, index):
        """
        Gets the name of the specified line font.
        :param index: Index position of the line font which is within the index range returned by
        IDrawingDoc::GetLineFontCount2
        """
        # return self._instance.GetLineFontName2(index)
        raise NotImplemented

    def get_line_styles(self, style_name_list, style_list):
        """
        Gets all of the line styles used in the current document.
        :param style_name_list: Array of strings containing style names
        :param style_list: Array of strings containing style types
        """
        # return self._instance.GetLineStyles(style_name_list, style_list)
        raise NotImplemented

    def get_pen_count(self):
        """Gets the number of pens currently defined in SOLIDWORKS."""
        # return self._instance.GetPenCount
        raise NotImplemented

    def get_pen_info(self):
        """Gets information about the pens used in SOLIDWORKS."""
        # return self._instance.GetPenInfo
        raise NotImplemented

    def get_sheet_count(self):
        """Gets the number of drawing sheets in this drawing."""
        # return self._instance.GetSheetCount
        raise NotImplemented

    def get_sheet_names(self):
        """Gets a list of the names of the drawing sheets in this drawing."""
        # return self._instance.GetSheetNames
        raise NotImplemented

    def get_view_count(self):
        """Gets all of the number of all of views, including the number of sheets, in this drawing document."""
        # return self._instance.GetViewCount
        raise NotImplemented

    def get_views(self):
        """Gets the all of the views, including the sheets, in this drawing document."""
        # return self._instance.GetViews
        raise NotImplemented

    def hide_edge(self):
        """Hides selected visible edges in a drawing document."""
        # return self._instance.HideEdge
        raise NotImplemented

    def hide_show_dimensions(self):
        """Sets whether to display suppressed dimensions as dimmed and hide them."""
        # return self._instance.HideShowDimensions
        raise NotImplemented

    def hide_show_drawing_views(self):
        """Sets whether to hide or show hidden drawing views."""
        # return self._instance.HideShowDrawingViews
        raise NotImplemented

    def i_add_chamfer_dim(self, x, y, z):
        """
        Adds a chamfer dimension.
        :param x: X dimension
        :param y: Y dimension
        :param z: Z dimension
        """
        # return self._instance.IAddChamferDim(x, y, z)
        raise NotImplemented

    def i_add_hole_callout(self, x, y, z):
        """
        Adds a hole callout at the specified position to the hole whose edge is selected.
        :param x: X position of hole callout in meters
        :param y: Y position of hole callout in meters
        :param z: Z position of hole callout in meters
        """
        # return self._instance.IAddHoleCallout2(x, y, z)
        raise NotImplemented

    def i_create_ang_dim(self, p0, p1, p2, p3, p4, p5, p6, text_point, text_height):
        """
        Creates a non-associative angular dimension.
        :param p0: Pointer to an array of 3 doubles (x,y,z); dimension end point
        :param p1: Pointer to an array of 3 doubles (x,y,z); dimension point
        :param p2: Pointer to an array of 3 doubles (x,y,z); extension1 start point
        :param p3: Pointer to an array of 3 doubles (x,y,z); extension1 end point
        :param p4: Pointer to an array of 3 doubles (x,y,z); extension2 start point
        :param p5: Pointer to an array of 3 doubles (x,y,z); extension2 end point
        :param p6: Pointer to an array of 3 doubles (x,y,z); plane normal
        :param text_point: Pointer to an array of 3 doubles (x,y,z); position of text
        :param text_height: Text height in meters
        """
        # return self._instance.ICreateAngDim4(p0, p1, p2, p3, p4, p5, p6, text_point, text_height)
        raise NotImplemented

    def i_create_auxiliary_view_at(self, x, y, z, not_aligned, label, showarrow, flip):
        """
        Creates an auxiliary view based on a selected edge in a drawing view.
        :param x: X position for the auxiliary view
        :param y: Y position for the auxiliary view
        :param z: Z position for the auxiliary view
        :param not_aligned: True aligns the view from its owner, false does not
        :param label: String that holds label of the auxiliary view
        :param showarrow: True shows the arrow, false hides the arrow
        :param flip: True flips the side shown in the auxiliary view, false does not
        """
        # return self._instance.ICreateAuxiliaryViewAt2(x, y, z, not_aligned, label, showarrow, flip)
        raise NotImplemented

    def i_create_diam_dim(self, p0, p1, p2, p3, text_point, val, text_height):
        """
        Creates a non-associative diameter dimension.
        :param p0: Pointer to an array of 3 doubles (x,y,z); location of dimension point
        :param p1: Pointer to an array of 3 doubles (x,y,z); nearest point on circle
        :param p2: Pointer to an array of 3 doubles (x,y,z); farthest point on circle diametrically opposite to P1
        :param p3: Pointer to an array of 3 doubles (x,y,z); plane normal
        :param text_point: Pointer to an array of 3 doubles (x,y,z); position of text
        :param val: Dimension value in meters
        :param text_height: Text height in meters
        """
        # return self._instance.ICreateDiamDim4(p0, p1, p2, p3, text_point, val, text_height)
        raise NotImplemented

    def i_create_linear_dim(self, p0, p1, p2, p3, p4, text_point, val, angle, text_height):
        """
        Creates a non-associative linear dimension.
        :param p0: Pointer to an array of 3 doubles (x,y,z), �dimension point
        :param p1: Pointer to an array of 3 doubles (x,y,z), dimension end
        :param p2: Pointer to an array of 3 doubles (x,y,z), normal to the plane of sketch
        :param p3: Pointer to an array of 3 doubles (x,y,z), extension line 1 reference point
        :param p4: Pointer to an array of 3 doubles (x,y,z), extension line 2 reference point
        :param text_point: Pointer to an array of 3 doubles (x,y,z), position of text
        :param val: Value for the non-associative linear dimension
        :param angle: Inclination angle of the text in radians
        :param text_height: Text height in meters
        """
        # return self._instance.ICreateLinearDim4(p0, p1, p2, p3, p4, text_point, val, angle, text_height)
        raise NotImplemented

    def i_create_ordinate_dim(self, p0, p1, p2, p3, p4, p5, val, angle, text_height):
        """
        Creates a non-associative ordinate dimension.
        :param p0: Pointer to an array of 3 doubles (x,y,z); dimension point
        :param p1: Pointer to an array of 3 doubles (x,y,z); unit vector that specifies the direction of the ordinate
        dimension
        :param p2: Pointer to an array of 3 doubles (x,y,z); extension line start point
        :param p3: Pointer to an array of 3 doubles (x,y,z); extension line end point
        :param p4: Pointer to an array of 3 doubles (x,y,z); unit vector and specifies the orientation of the text; for
        example, (1, 0, 0) results in horizontal text read from left to right
        :param p5: Pointer to an array of 3 doubles (x,y,z); position of text
        :param val: Value for the ordinate dimension
        :param angle: Inclination angle of the text in radians (character slant)
        :param text_height: Text height in meters
        """
        # return self._instance.ICreateOrdinateDim4(p0, p1, p2, p3, p4, p5, val, angle, text_height)
        raise NotImplemented

    def i_create_section_view_at(self, x, y, z, section_label, options, num_excluded_components, excluded_components,
                                 section_depth):
        """
        Creates a section view from the section line up to the specified distance at the specified distance.
        :param x: x position on the drawing sheet for the center of the section view
        :param y: y position on the drawing sheet for the center of the section view
        :param z: z position on the drawing sheet for the center of the section view
        :param section_label: Letter for the label for the section view
        :param options: Options that affect the section view as defined in swCreateSectionViewAtOptions_e
        :param num_excluded_components: Number of components to exclude from the section view
        :param excluded_components: Array of components to exclude from the section view
        :param section_depth: Distance from the section line to�create the section view
        """
        # return self._instance.ICreateSectionViewAt5(x, y, z, section_label, options, num_excluded_components, excluded
        # components, section_depth)
        raise NotImplemented

    def i_create_text(self, text_string, text_x, text_y, text_z, text_height, text_angle):
        """
        Creates a note containing the specified text at a given location.
        :param text_string: User input text
        :param text_x: X text location in meters (see Remarks)
        :param text_y: Y text location in meters (see Remarks)
        :param text_z: Z text location in meters (see Remarks)
        :param text_height: Text height in meters
        :param text_angle: Text angle for rotated text in radians
        """
        # return self._instance.ICreateText2(text_string, text_x, text_y, text_z, text_height, text_angle)
        raise NotImplemented

    def i_edit_selected_gtol(self):
        """Gets the selected GTol to edit."""
        # return self._instance.IEditSelectedGtol
        raise NotImplemented

    def i_feature_by_name(self, name):
        """
        Gets the specified feature in the drawing.
        :param name: Name of the feature
        """
        # return self._instance.IFeatureByName(name)
        raise NotImplemented

    def i_get_current_sheet(self):
        """Gets the currently active drawing sheet."""
        # return self._instance.IGetCurrentSheet
        raise NotImplemented

    def i_get_first_view(self):
        """Gets the first drawing view on the current sheet."""
        # return self._instance.IGetFirstView
        raise NotImplemented

    def i_get_insertion_point(self):
        """Gets the current insertion (pick) point in a drawing."""
        # return self._instance.IGetInsertionPoint
        raise NotImplemented

    def i_get_pen_info(self):
        """Gets information about the pens used in SOLIDWORKS."""
        # return self._instance.IGetPenInfo
        raise NotImplemented

    def i_get_sheet_names(self, count):
        """
        Gets a list of the names of the drawing sheets in this drawing.
        :param count: Number of drawing sheets in this drawing (see Remarks)
        """
        # return self._instance.IGetSheetNames(count)
        raise NotImplemented

    def i_insert_dowel_symbol(self):
        """Inserts a dowel pin symbol on the currently selected edge or edges."""
        # return self._instance.IInsertDowelSymbol
        raise NotImplemented

    def i_insert_multi_jog_leader(self, points_count, points, start_point_arrow_style, end_point_arrow_style):
        """
        Inserts a multi-jog leader.
        :param points_count: Number of points
        :param points: Array of points of size PointsCount
        :param start_point_arrow_style: Starting point's arrowhead style as defined in swArrowStyle_e
        :param end_point_arrow_style: Ending point's arrowhead style as defined in� swArrowStyle_e
        """
        # return self._instance.IInsertMultiJogLeader3(points_count, points, start_point_arrow_style,
        # end_point_arrow_style)
        raise NotImplemented

    def i_insert_revision_cloud(self, cloud_shape):
        """
        Inserts a revision cloud annotation with the specified shape into a view or sheet.
        :param cloud_shape: Revision cloud annotation shape as defined in swRevisionCloudShape_e
        """
        # return self._instance.IInsertRevisionCloud(cloud_shape)
        raise NotImplemented

    def i_new_gtol(self):
        """Creates a new GTol."""
        # return self._instance.INewGtol
        raise NotImplemented

    def insert_angular_running_dim(self):
        """Inserts an angular running dimension into this drawing."""
        # return self._instance.InsertAngularRunningDim
        raise NotImplemented

    def insert_base_dim(self):
        """Inserts the base model dimensions into this drawing."""
        # return self._instance.InsertBaseDim
        raise NotImplemented

    def insert_break_horizontal(self):
        """Inserts a horizontal break in the drawing view."""
        # return self._instance.InsertBreakHorizontal
        raise NotImplemented

    def insert_break_vertical(self):
        """Inserts a vertical break in this drawing."""
        # return self._instance.InsertBreakVertical
        raise NotImplemented

    def insert_center_line(self):
        """Inserts a centerline on the selected entities."""
        # return self._instance.InsertCenterLine2
        raise NotImplemented

    def insert_center_mark(self, style, propagate, slot):
        """
        Inserts a center mark in a drawing document.
        :param style: Style as defined in swCenterMarkStyle_e
        :param propagate: True if the center mark should propagate throughout the pattern, false if not
        :param slot: True if this is slot-style center mark, false if not
        """
        # return self._instance.InsertCenterMark3(style, propagate, slot)
        raise NotImplemented

    def insert_circular_note_pattern(self, arc_radius, arc_angle, pattern_num, pattern_spacing, pattern_rotate,
                                     delete_instances):
        """
        Inserts a circular note pattern using the selected note.
        :param arc_radius: Radius for the circular note pattern
        :param arc_angle: Angle relative to the notes being patterned
        :param pattern_num: Total number of pattern instances, including the seed geometry
        :param pattern_spacing: Spacing between pattern instances in radians
        :param pattern_rotate: True to rotate the pattern, false to not
        :param delete_instances: Number of instances�to delete, passed as a string formatted as "(a) (b) (c) "
        """
        # return self._instance.InsertCircularNotePattern(arc_radius, arc_angle, pattern_num, pattern_spacing,
        # pattern_rotate, delete_instances)
        raise NotImplemented

    def insert_dowel_symbol(self):
        """Inserts a dowel pin symbol on the currently selected edge or edges in this drawing."""
        # return self._instance.InsertDowelSymbol
        raise NotImplemented

    def insert_group(self):
        """Inserts the currently selected items into a group (or view)."""
        # return self._instance.InsertGroup
        raise NotImplemented

    def insert_horizontal_ordinate(self):
        """Inserts a horizontal ordinate dimension into this drawing."""
        # return self._instance.InsertHorizontalOrdinate
        raise NotImplemented

    def insert_linear_note_pattern(self, num_x, num_y, spacing_x, spacing_y, angle_x, angle_y, delete_instances):
        """
        Inserts a linear note pattern using the selected note.
        :param num_x: Total number of instances along the x axis, including the seed
        :param num_y: Total number of instances along the y axis, including the seed
        :param spacing_x: Spacing between pattern instances along the x axis
        :param spacing_y: Spacing between pattern instances along the y axis
        :param angle_x: Angle for direction 1 relative to the x axis
        :param angle_y: Angle for direction�2 relative to the�y axis
        :param delete_instances: Number of instances to delete, passed as a string in the format "(a) (b) (c) "
        """
        # return self._instance.InsertLinearNotePattern(num_x, num_y, spacing_x, spacing_y, angle_x, angle_y,
        # delete_instances)
        raise NotImplemented

    def insert_model_annotations(self, option, types, all_views, duplicate_dims, hidden_feature_dims,
                                 use_placement_in_sketch):
        """
        Inserts model annotations into this drawing document in the currently selected drawing view.
        :param option: Source of dimensions as defined by swImportModelItemsSource_e (see Remarks)
        :param types: Bitwise OR of annotation types as defined in swInsertAnnotation_e
        :param all_views: True to insert the annotations in all views in the drawing, false to insert annotations only
        in the selected view
        :param duplicate_dims: True to eliminate duplicate dimensions, false to allow duplicate dimensions
        :param hidden_feature_dims: True to insert dimensions from features that are hidden, false to not insert
        dimensions from features that are hidden
        :param use_placement_in_sketch: True to insert dimensions as they were placed in sketch, false to not
        """
        # return self._instance.InsertModelAnnotations3(option, types, all_views, duplicate_dims, hidden_feature_dims,
        # use_placement_in_sketch)
        raise NotImplemented

    def insert_model_dimensions(self, option):
        """
        Inserts model dimensions into the selected drawing view according to the option specified.
        :param option:
    0 - All dimensions in the view

    1 - All dimensions of the currently selected component (for assembly drawings)

    2 - All dimensions of the currently selected feature

    3 - All dimensions of the assembly
        """
        # return self._instance.InsertModelDimensions(option)
        raise NotImplemented

    def insert_model_in_predefined_view(self, model_name):
        """
        Inserts the model into the predefined drawing views in the active drawing sheet.
        :param model_name: Name of the model to insert into the predefined drawing views in the active drawing sheet
        """
        # return self._instance.InsertModelInPredefinedView(model_name)
        raise NotImplemented

    def insert_multi_jog_leader(self, points, start_point_arrow_style, end_point_arrow_style):
        """
        Inserts a multi-jog leader.
        :param points: Array�of points of size PointsCount
        :param start_point_arrow_style: Starting point's arrowhead style as defined in swArrowStyle_e
        :param end_point_arrow_style: Ending point's arrowhead style as defined in� swArrowStyle_e
        """
        # return self._instance.InsertMultiJogLeader3(points, start_point_arrow_style, end_point_arrow_style)
        raise NotImplemented

    def insert_new_note(self, upper_text, lower_text, no_leader, bent_leader, arrow_style, leader_side, angle,
                        balloon_style, balloon_fit, upper_note_content, lower_note_content):
        """
        Creates a new note in this drawing.
        :param upper_text: Upper text string to be put in the note
        :param lower_text: Unused; pass an empty string
        :param no_leader: True does not add a leader line, false does
        :param bent_leader: True adds a bent leader line, false does not
        :param arrow_style: Arrowhead type as defined in swArrowStyle_e
        :param leader_side: Leader line side as defined in swLeaderSide_e
        :param angle: Text angle
        :param balloon_style: Balloon style type as defined in swBalloonStyle_e
        :param balloon_fit: Balloon fit type as defined in swBalloonFit_e
        :param upper_note_content: Unused; set to 0
        :param lower_note_content: Unused; set to 0
        """
        # return self._instance.InsertNewNote2(upper_text, lower_text, no_leader, bent_leader, arrow_style, leader_side,
        # angle, balloon_style, balloon_fit, upper_note_content, lower_note_content)
        raise NotImplemented

    def insert_ordinate(self):
        """Inserts an ordinate dimension into this drawing."""
        # return self._instance.InsertOrdinate
        raise NotImplemented

    def insert_ref_dim(self):
        """Inserts reference dimensions in this drawing."""
        # return self._instance.InsertRefDim
        raise NotImplemented

    def insert_revision_cloud(self, cloud_shape):
        """
        Inserts a revision cloud annotation with the specified shape into a view or sheet.
        :param cloud_shape: Revision cloud annotation shape as defined in swRevisionCloudShape_e
        """
        # return self._instance.InsertRevisionCloud(cloud_shape)
        raise NotImplemented

    def insert_revision_symbol(self, x, y):
        """
        Inserts a revision symbol note in this drawing.
        :param x: X coordinate �at which to insert revision symbol note
        :param y: Y coordinate at which to insert revision symbol note
        """
        # return self._instance.InsertRevisionSymbol(x, y)
        raise NotImplemented

    def insert_table_annotation(self, use_anchor_point, x, y, anchor_type, table_template, rows, columns):
        """
        Inserts a table annotation in this drawing.
        :param use_anchor_point: True to anchor the table to the general table anchor point and ignore any coordinates
        specified for X and Y, or false to use the coordinates specified for X and Y
        :param x: X coordinate to insert this table annotation
        :param y: Y coordinate to insert this table annotation
        :param anchor_type: Type of anchor as defined in swBOMConfigurationAnchorType_e (see Remarks)
        :param table_template: Path and filename of the general table template to use �(see Remarks)
        :param rows: Number of rows in the table annotation
        :param columns: Number of columns in the table annotation
        """
        # return self._instance.InsertTableAnnotation2(use_anchor_point, x, y, anchor_type, table_template, rows,
        # columns)
        raise NotImplemented

    def insert_thread_callout(self):
        """Inserts a thread callout into this drawing."""
        # return self._instance.InsertThreadCallout
        raise NotImplemented

    def insert_vertical_ordinate(self):
        """Inserts a vertical ordinate dimension in this drawing."""
        # return self._instance.InsertVerticalOrdinate
        raise NotImplemented

    def insert_weld_symbol(self, dim1, symbol, dim2, symmetric, field_weld, show_other_side, dash_on_top, peripheral,
                           has_process, process_value):
        """
        Creates a weld symbol located at the last edge selection.
        :param dim1: First text value to the left of the symbol
        :param symbol: Weld symbol name (see Remarks)
        :param dim2: Text value to the right of the symbol
        :param symmetric: True puts the symbol above and below the horizontal line
        :param field_weld: True puts a flag for field welding
        :param show_other_side: True puts Dim1, Symbol, and Dim2 on the other side of the horizontal line
        :param dash_on_top: True puts the dash line on top
        :param peripheral: True puts a peripheral symbol
        :param has_process: True uses ProcessValue
        :param process_value: Process value if HasProcess is set to True
        """
        # return self._instance.InsertWeldSymbol(dim1, symbol, dim2, symmetric, field_weld, show_other_side,
        # dash_on_top, peripheral, has_process, process_value)
        raise NotImplemented

    def i_reorder_sheets(self, sheet_count, new_sheet_list):
        """
        Reorders the drawing sheets per their positions in the input array.
        :param sheet_count: Number of sheets to reorder
        :param new_sheet_list: Array of the names of the sheets to reorder
        """
        # return self._instance.IReorderSheets(sheet_count, new_sheet_list)
        raise NotImplemented

    def is_detailing_mode(self):
        """Gets whether this drawing is in detailing mode."""
        # return self._instance.IsDetailingMode
        raise NotImplemented

    def isolate_changed_dimensions(self):
        """Isolates changed dimensions."""
        # return self._instance.IsolateChangedDimensions
        raise NotImplemented

    def load_line_styles(self, style_files, style_name_list, replace_existing):
        """
        Loads the specified line styles into the current drawing.
        :param style_files: Full pathname of file containing line styles to import
        :param style_name_list: Array of strings containing style names
        :param replace_existing: True to replace existing styles, false to not
        """
        # return self._instance.LoadLineStyles(style_files, style_name_list, replace_existing)
        raise NotImplemented

    def make_section_line(self):
        """Makes a section line from a set of connected sketch lines."""
        # return self._instance.MakeSectionLine
        raise NotImplemented

    def modify_surface_finish_symbol(self, sym_type, leader_type, loc_x, loc_y, loc_z, lay_symbol, arrow_type,
                                     mach_allowance, other_vals, prod_method, sample_len, max_roughness, min_roughness,
                                     roughness_spacing):
        """
        Modifies the selected surface finish symbol.
        :param sym_type: Symbol type as defined in swSFSymType_e
        :param leader_type: Leader type as defined in swLeaderStyle_e
        :param loc_x: X location for symbol
        :param loc_y: Y location for symbol
        :param loc_z: Z location for symbol
        :param lay_symbol: Direction of lay as defined in swSFLaySym_e
        :param arrow_type: Arrowhead type as defined in swArrowStyle_e
        :param mach_allowance: Material removal allowance
        :param other_vals: Other roughness values
        :param prod_method: Production method/treatment
        :param sample_len: Sampling length
        :param max_roughness: Maximum roughness
        :param min_roughness: Minimum roughness
        :param roughness_spacing: Roughness spacing
        """
        # return self._instance.ModifySurfaceFinishSymbol(sym_type, leader_type, loc_x, loc_y, loc_z, lay_symbol,
        # arrow_type, mach_allowance, other_vals, prod_method, sample_len, max_roughness, min_roughness,
        # roughness_spacing)
        raise NotImplemented

    def new_gtol(self):
        """Creates a new GTol object and returns the pointer to that object."""
        # return self._instance.NewGtol
        raise NotImplemented

    def new_note(self, text, height):
        """
        Creates a new note at the selected location.
        :param text: Text string for the note
        :param height: Height of the note in meters
        """
        # return self._instance.NewNote(text, height)
        raise NotImplemented

    def new_sheet(self, name, paper_size, template_in, scale1, scale2, first_angle, template_name, width, height,
                  property_view_name, zone_left_margin, zone_right_margin, zone_top_margin, zone_bottom_margin,
                  zone_row, zone_col):
        """
        Creates a new drawing sheet in this drawing document.
        :param name: Name to be given to the new drawing sheet
        :param paper_size: Size of paper as defined in swDwgPaperSizes_e; valid only if TemplateIn is
        swDwgTemplates_e.swDwgTemplateNone
        :param template_in: Template as defined in swDwgTemplates_e
        :param scale1: Scale numerator
        :param scale2: Scale denominator
        :param first_angle: True for first angle projection, false for third angle projection
        :param template_name: Name of custom template with full directory path; valid only�if TemplateIn is set to
        swDwgTemplates_e.swDwgTemplateCustom
        :param width: Paper width; valid only if TemplateIn is set to swDwgTemplates_e.swDwgTemplateNone or PaperSize is
        set to swDwgPaperSizes_e.swDwgPapersUserDefined
        :param height: Paper height; valid only�if TemplateIn is set to swDwgTemplates_e.swDwgTemplateNone or PaperSize
        is set to swDwgPaperSizes_e.swDwgPapersUserDefined
        :param property_view_name: Name of view containing the model from which to get custom property values
        :param zone_left_margin: Zone area left margin; distance from drawing sheet's left edge
        :param zone_right_margin: Zone area right margin; distance from drawing sheet's right edge
        :param zone_top_margin: Zone area top margin; distance from drawing sheet's top edge
        :param zone_bottom_margin: Zone area bottom margin; distance from drawing sheet's bottom edge
        :param zone_row: Number of zone rows in the zone area of this sheet (see Remarks)
        :param zone_col: Number of zone columns in the zone area of this sheet (see Remarks)
        """
        # return self._instance.NewSheet4(name, paper_size, template_in, scale1, scale2, first_angle, template_name,
        # width, height, property_view_name, zone_left_margin, zone_right_margin, zone_top_margin, zone_bottom_margin,
        # zone_row, zone_col)
        raise NotImplemented

    def on_component_properties(self):
        """Displays the Component Properties dialog for the selected view."""
        # return self._instance.OnComponentProperties
        raise NotImplemented

    def paste_sheet(self, insert_option, rename_option):
        """
        Copies and pastes a drawing sheet to the specified location of the drawing document, optionally renaming
        whenever duplicate names occur.
        :param insert_option: Option as defined in swInsertOptions_e
        :param rename_option: Option as defined in swRenameOptions_e;�1 to rename duplicate section, detail or
        auxiliary view names;�2 to not rename
        """
        # return self._instance.PasteSheet(insert_option, rename_option)
        raise NotImplemented

    def reorder_sheets(self, new_sheet_list):
        """
        Reorders the drawing sheets per their positions in the input array.
        :param new_sheet_list: Array of the names of the sheets to reorder
        """
        # return self._instance.ReorderSheets(new_sheet_list)
        raise NotImplemented

    def replace_view_model(self, new_model_path_name, views, instances):
        """
        Replaces the specified instances of a model in the specified drawing views.
        :param new_model_path_name: Full path and filename of the replacement model
        :param views: Array of IViews in which to replace the model
        :param instances: Array of IComponent2s that are specific instances of�the model to replace in the drawing
        """
        # return self._instance.ReplaceViewModel(new_model_path_name, views, instances)
        raise NotImplemented

    def resolve_out_of_date_light_weight_components(self):
        """Resolves out-of-date lightweight components in the selected drawing view or drawing sheet."""
        # return self._instance.ResolveOutOfDateLightWeightComponents
        raise NotImplemented

    def restore_rotation(self):
        """Restores rotation for the selected drawing view."""
        # return self._instance.RestoreRotation
        raise NotImplemented

    def save_line_styles(self, style_files, style_name_list, replace_existing):
        """
        Exports to a file the specified line styles in the current drawing.
        :param style_files: Full pathname of file to save line styles to
        :param style_name_list: Array of strings containing line style names to save
        :param replace_existing: True to replace existing styles in the file, false to not
        """
        # return self._instance.SaveLineStyles(style_files, style_name_list, replace_existing)
        raise NotImplemented

    def set_current_layer(self, layername):
        """
        Sets the current layer used by this document.
        :param layername: Name of the layer
        """
        # return self._instance.SetCurrentLayer(layername)
        raise NotImplemented

    def set_line_color(self, color):
        """
        Sets the line color for a selected edge or sketch entity.
        :param color: Color definition as a COLORREF
        """
        # return self._instance.SetLineColor(color)
        raise NotImplemented

    def set_line_style(self, style_name):
        """
        Sets the style or font for the line for a selected edge or sketch entity.
        :param style_name: Style or font for the selected edge or sketch entity as defined in swLineStyles_e
        """
        # return self._instance.SetLineStyle(style_name)
        raise NotImplemented

    def set_line_width(self, width):
        """
        Sets the line thickness for a selected edge or sketch entity to a SOLIDWORKS-supplied weight (width).
        :param width: Weight for the line as defined in swLineWeights_e
        """
        # return self._instance.SetLineWidth(width)
        raise NotImplemented

    def set_line_width_custom(self, width):
        """
        Sets the line thickness to the specified custom width for a selected edge or sketch entity.
        :param width: Custom width for the�line in meters
        """
        # return self._instance.SetLineWidthCustom(width)
        raise NotImplemented

    def set_sheets_selected(self, new_sheet_list):
        """
        Sets the specified drawing sheets whose setups to modify.
        :param new_sheet_list: Names of the drawing sheets whose setups to modify (see Remarks)
        """
        # return self._instance.SetSheetsSelected(new_sheet_list)
        raise NotImplemented

    def setup_sheet(self, name, paper_size, template_in, scale1, scale2, first_angle, template_name, width, height,
                    property_view_name, remove_modified_notes, zone_left_margin, zone_right_margin, zone_top_margin,
                    zone_bottom_margin, zone_row, zone_col):
        """
        Sets up the specified drawing sheet.
        :param name: Name of the sheet to set up
        :param paper_size: Size of paper as defined in swDwgPaperSizes_e; valid only if�TemplateIn is set to
        swDwgTemplates_e.swDwgTemplateNone
        :param template_in: Template as defined in swDwgTemplates_e
        :param scale1: Scale numerator
        :param scale2: Scale denominator
        :param first_angle: True for first angle projection, false for third angle projection
        :param template_name: Name of custom template with full directory path; valid only�if TemplateIn is set to
        swDwgTemplates_e.swDwgTemplateCustom
        :param width: Paper width; valid only if TemplateIn is set to swDwgTemplates_e.swDwgTemplateNone or PaperSize is
        set to swDwgPaperSizes_e.swDwgPapersUserDefined
        :param height: Paper height; valid only�if TemplateIn is set to swDwgTemplates_e.swDwgTemplateNone or PaperSize
        is set to swDwgPaperSizes_e.swDwgPapersUserDefined
        :param property_view_name: Name of view containing the model from which to get custom property values
        :param remove_modified_notes: True to delete modified notes, false to not
        :param zone_left_margin: Zone area left margin; distance from drawing sheet's left edge
        :param zone_right_margin: Zone area right margin; distance from drawing sheet's right edge
        :param zone_top_margin: Zone area top margin; distance from drawing sheet's top edge
        :param zone_bottom_margin: Zone area bottom margin; distance from drawing sheet's bottom edge
        :param zone_row: Number of zone rows�in the zone area�of this sheet (see Remarks)
        :param zone_col: Number of zone columns�in the zone area�of this sheet (see Remarks)
        """
        # return self._instance.SetupSheet6(name, paper_size, template_in, scale1, scale2, first_angle, template_name,
        # width, height, property_view_name, remove_modified_notes, zone_left_margin, zone_right_margin,
        # zone_top_margin, zone_bottom_margin, zone_row, zone_col)
        raise NotImplemented

    def sheet_next(self):
        """Moves to the next sheet in the drawing."""
        # return self._instance.SheetNext
        raise NotImplemented

    def sheet_previous(self):
        """Returns to the previous sheet in a drawing."""
        # return self._instance.SheetPrevious
        raise NotImplemented

    def show_edge(self):
        """Shows the selected hidden edges in a drawing document."""
        # return self._instance.ShowEdge
        raise NotImplemented

    def sketch_dim(self):
        """Inserts a sketch dimension in this drawing."""
        # return self._instance.SketchDim
        raise NotImplemented

    def start_drawing(self):
        """Provides faster creation of entities within a drawing."""
        # return self._instance.StartDrawing
        raise NotImplemented

    def suppress_view(self):
        """Hides the selected drawing view."""
        # return self._instance.SuppressView
        raise NotImplemented

    def translate_drawing(self, delta_x, delta_y):
        """
        Translates the entire drawing.
        :param delta_x: Delta X value for the translation operation
        :param delta_y: Delta Y value for the translation operation
        """
        # return self._instance.TranslateDrawing(delta_x, delta_y)
        raise NotImplemented

    def un_break_view(self):
        """Removes a break in the selected drawing view."""
        # return self._instance.UnBreakView
        raise NotImplemented

    def unsuppress_view(self):
        """Hides the selected drawing view."""
        # return self._instance.UnsuppressView
        raise NotImplemented

    def view_display_hidden(self):
        """Sets the current display mode to Hidden Lines Removed."""
        # return self._instance.ViewDisplayHidden
        raise NotImplemented

    def view_display_hiddengreyed(self):
        """Sets the current display mode to Hidden Lines Visible."""
        # return self._instance.ViewDisplayHiddengreyed
        raise NotImplemented

    def view_display_shaded(self):
        """Sets the current display mode to Shaded."""
        # return self._instance.ViewDisplayShaded
        raise NotImplemented

    def view_display_wireframe(self):
        """Sets the current display mode to Wireframe."""
        # return self._instance.ViewDisplayWireframe
        raise NotImplemented

    def view_full_page(self):
        """Fits the drawing to the full page."""
        # return self._instance.ViewFullPage
        raise NotImplemented

    def view_hlr_quality(self):
        """Toggles the Hidden Lines Removed mode for the drawing view."""
        # return self._instance.ViewHlrQuality
        raise NotImplemented

    def view_model_edges(self):
        """Toggles the mode for viewing model edges when in shaded mode."""
        # return self._instance.ViewModelEdges
        raise NotImplemented

    def view_tangent_edges(self):
        """Toggles display of tangent edges in the selected drawing view."""
        # return self._instance.ViewTangentEdges
        raise NotImplemented
