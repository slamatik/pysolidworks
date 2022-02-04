# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.html
class IView:
    def __init__(self, parent=None):
        self._instance = parent

    def angle(self):
        """Gets or sets the rotation angle of the view."""
        # return self._instance.Angle
        raise NotImplemented

    def bodies(self):
        """Gets or sets the bodies of a multibody part to show in the drawing view."""
        # return self._instance.Bodies
        raise NotImplemented

    def break_line_gap(self):
        """Gets or sets the width of the gap for a break line."""
        # return self._instance.BreakLineGap
        raise NotImplemented

    def crop_view_jagged_outline(self):
        """Gets or sets whether to use a jagged outline in this cropped drawing view."""
        # return self._instance.CropViewJaggedOutline
        raise NotImplemented

    def crop_view_jagged_shape_intensity(self):
        """Gets or sets the shape intensity of the jagged outline in this cropped drawing view."""
        # return self._instance.CropViewJaggedShapeIntensity
        raise NotImplemented

    def crop_view_no_outline(self):
        """Gets or sets whether to show an outline in this cropped drawing view."""
        # return self._instance.CropViewNoOutline
        raise NotImplemented

    def disable_auto_update(self):
        """Gets or sets whether to disable the automatic update of this view."""
        # return self._instance.DisableAutoUpdate
        raise NotImplemented

    def display_state(self):
        """Gets or sets the name of the display state for this drawing view."""
        # return self._instance.DisplayState
        raise NotImplemented

    def emphasize_outline(self):
        """Gets or sets whether the outlines of section views are emphasized in this drawing view."""
        # return self._instance.EmphasizeOutline
        raise NotImplemented

    def flip_view(self):
        """Gets or sets whether to flip a flat-pattern view of a sheet metal part."""
        # return self._instance.FlipView
        raise NotImplemented

    def focus_locked(self):
        """Gets or sets whether or not focus is locked on this view."""
        # return self._instance.FocusLocked
        raise NotImplemented

    def hidden_edges(self):
        """Gets the hidden edges in the drawing view or sets the hidden edges in the drawing view to be visible."""
        # return self._instance.HiddenEdges
        raise NotImplemented

    def i_position(self):
        """Gets or sets the X and Y location of the model view's geometric center, relative to the drawing sheet origin."""
        # return self._instance.IPosition
        raise NotImplemented

    def i_scale_ratio(self):
        """Gets or sets the scale of the drawing view, returning the results in ratio format (n:n)."""
        # return self._instance.IScaleRatio
        raise NotImplemented

    def link_parent_configuration(self):
        """Gets or sets whether to link a projected or auxiliary view with the parent configuration."""
        # return self._instance.LinkParentConfiguration
        raise NotImplemented

    def model_to_view_transform(self):
        """Gets the math transform to go from model to drawing view space.
NOTE: This property is a get-only property. Set is not implemented."""
        # return self._instance.ModelToViewTransform
        raise NotImplemented

    def position(self):
        """Gets or sets the X and Y location of the model view's geometric center, relative to the drawing sheet origin."""
        # return self._instance.Position
        raise NotImplemented

    def position_locked(self):
        """Gets or sets whether this drawing view's position is locked."""
        # return self._instance.PositionLocked
        raise NotImplemented

    def projected_dimensions(self):
        """Gets or sets whether dimensions in this view are true or projected."""
        # return self._instance.ProjectedDimensions
        raise NotImplemented

    def referenced_configuration(self):
        """Gets or sets the configuration referenced by this drawing view."""
        # return self._instance.ReferencedConfiguration
        raise NotImplemented

    def referenced_configuration_i_d(self):
        """Gets the persistent reference ID of the configuration referenced in this drawing view."""
        # return self._instance.ReferencedConfigurationID
        raise NotImplemented

    def referenced_document(self):
        """Gets the document referenced by this drawing view."""
        # return self._instance.ReferencedDocument
        raise NotImplemented

    def root_drawing_component(self):
        """Gets the root component for this drawing view."""
        # return self._instance.RootDrawingComponent
        raise NotImplemented

    def scale_decimal(self):
        """Gets or sets the scale of the drawing view, returning the results in decimal format."""
        # return self._instance.ScaleDecimal
        raise NotImplemented

    def scale_hatch_pattern(self):
        """Gets or sets whether to scale the hatch pattern to the drawing view."""
        # return self._instance.ScaleHatchPattern
        raise NotImplemented

    def scale_ratio(self):
        """Gets or sets the scale of the drawing view, returning the results in ratio format (n:n)."""
        # return self._instance.ScaleRatio
        raise NotImplemented

    def sheet(self):
        """Gets the sheet on which this drawing view exists."""
        # return self._instance.Sheet
        raise NotImplemented

    def show_sheet_metal_bend_notes(self):
        """Gets or sets whether to show sheet metal bend notes."""
        # return self._instance.ShowSheetMetalBendNotes
        raise NotImplemented

    def suppress_state(self):
        """Gets or sets the view suppress state."""
        # return self._instance.SuppressState
        raise NotImplemented

    def type(self):
        """Gets the drawing view type."""
        # return self._instance.Type
        raise NotImplemented

    def use_parent_scale(self):
        """Gets or sets the drawing view's scale to match the parent drawing view's scale."""
        # return self._instance.UseParentScale
        raise NotImplemented

    def use_sheet_scale(self):
        """Gets or sets whether the scale of the drawing view is the same as the scale of the drawing sheet on which this view is located."""
        # return self._instance.UseSheetScale
        raise NotImplemented

    def align_drawing_view(self, align_view_type):
        """
        Specifies the alignment of this auxiliary drawing view.
        :param align_view_type: Type of alignment as defined by swAlignDrawingViewTypes_e
        """
        # return self._instance.AlignDrawingView(align_view_type)
        raise NotImplemented

    def align_with_view(self, align_type, base_view):
        """
        Sets view alignment.
        :param align_type: Type of alignment to set as defined by swAlignViewTypes_e
        :param base_view: View with which to align, if aligning with another view
        """
        # return self._instance.AlignWithView(align_type, base_view)
        raise NotImplemented

    def auto_insert_center_marks(self, insert_type, insert_option, linear_slot_center, arc_slot_center,
                                 use_document_defaults, size, gap, extended_lines, center_line_font, angle):
        """
        Automatically inserts the specified center marks in this view.
        :param insert_type: Features for which to insert center marks as defined in swAutoInsertCenterMarkTypes_e
        :param insert_option: Center mark options as defined in swCenterMarkConnectionLine_e
        :param linear_slot_center: True to add center marks to slot centers, false to add them to slot ends
        :param arc_slot_center: True to add center marks to arc centers, false to add them to arc ends
        :param use_document_defaults: True to use the display settings specified in Tools > Options > Document Properties > Centerlines/Center Marks, false to use the display settings set by this method
        :param size: Size of center mark; valid only if UseDocumentDefaults is false
        :param gap: Size of gap between the center mark and extension line; valid only if UseDocumentDefaults is false and the Tools > Options > Document Properties > Centerlines/Center Marks > Scale by view scale check box is clear (see Remarks)
        :param extended_lines: True to extend lines from center mark points, false to not; valid only if UseDocumentDefaults is false
        :param center_line_font: True to use the centerline font, false to not; valid only if UseDocumentDefaults is false
        :param angle: Rotation angle for the center mark; a positive angle rotates the center mark counterclockwise
        """
        # return self._instance.AutoInsertCenterMarks2(insert_type, insert_option, linear_slot_center, arc_slot_center, use_document_defaults, size, gap, extended_lines, center_line_font, angle)
        raise NotImplemented

    def crop(self, jagged_outline, no_outline, shape_intensity):
        """
        Crops this view using the selected closed sketch profile.
        :param jagged_outline: True to use a jagged outline, false to not; only valid if NoOutline is false
        :param no_outline: True to not show an outline, false to show an outline
        :param shape_intensity: Shape intensity of the jagged outline; valid range is 1 (most) to 5 (least); only valid if JaggedOutline is true
        """
        # return self._instance.Crop2(jagged_outline, no_outline, shape_intensity)
        raise NotImplemented

    def enum_hidden_components(self):
        """Gets the hidden components enumeration in this drawing view."""
        # return self._instance.EnumHiddenComponents2
        raise NotImplemented

    def enum_section_lines(self):
        """Gets the section lines enumeration in the view."""
        # return self._instance.EnumSectionLines
        raise NotImplemented

    def get_alignment(self):
        """Gets the alignment information of this view."""
        # return self._instance.GetAlignment
        raise NotImplemented

    def get_annotation_count(self):
        """Gets the number of annotations in this view."""
        # return self._instance.GetAnnotationCount
        raise NotImplemented

    def get_annotations(self):
        """Gets the annotations in this view."""
        # return self._instance.GetAnnotations
        raise NotImplemented

    def get_arc_count(self):
        """Gets the number of arcs in this view."""
        # return self._instance.GetArcCount
        raise NotImplemented

    def get_arcs(self):
        """Gets all of the information for all of the arcs added by a user in this drawing view."""
        # return self._instance.GetArcs4
        raise NotImplemented

    def get_base_view(self):
        """Gets the base (parent) view used to create this view."""
        # return self._instance.GetBaseView
        raise NotImplemented

    def get_bend_line_count(self):
        """Gets the number of bendlines in a flat-pattern drawing view."""
        # return self._instance.GetBendLineCount
        raise NotImplemented

    def get_bend_lines(self):
        """Gets the bendlines in a flat-pattern drawing view."""
        # return self._instance.GetBendLines
        raise NotImplemented

    def get_bend_note_attribute_string(self, attribute):
        """
        Gets the internal string that is used to format the text of the specified bend note attribute in this drawing view of a sheet metal part.
        :param attribute: Bend note attribute as defined in swBendNoteAttribute_e
        """
        # return self._instance.GetBendNoteAttributeString(attribute)
        raise NotImplemented

    def get_bend_note_text_format(self):
        """Gets the text format of all bend notes in this drawing view of a sheet metal part."""
        # return self._instance.GetBendNoteTextFormat
        raise NotImplemented

    def get_bodies_count(self):
        """Gets the number of bodies of a multibody part in the drawing view."""
        # return self._instance.GetBodiesCount
        raise NotImplemented

    def get_bom_table(self):
        """Gets the BOM table found in this drawing view."""
        # return self._instance.GetBomTable
        raise NotImplemented

    def get_break_line_count(self, size):
        """
        Gets the number of breaks lines and breaks in this view.
        :param size: Size of an array of doubles to allocate in IView::GetBreakLineInfo2 and IView::IGetBreakLineInfo2
        """
        # return self._instance.GetBreakLineCount2(size)
        raise NotImplemented

    def get_break_line_info(self):
        """Gets information for all of the break lines in this view."""
        # return self._instance.GetBreakLineInfo2
        raise NotImplemented

    def get_break_lines(self):
        """Gets the all of the breaks in this view."""
        # return self._instance.GetBreakLines
        raise NotImplemented

    def get_break_out_section_count(self):
        """Gets the number of broken-out sections in this view."""
        # return self._instance.GetBreakOutSectionCount
        raise NotImplemented

    def get_break_out_sections(self):
        """Gets all of the broken-out sections in this view."""
        # return self._instance.GetBreakOutSections
        raise NotImplemented

    def get_center_line_count(self):
        """Gets the number of centerlines on this drawing view."""
        # return self._instance.GetCenterLineCount
        raise NotImplemented

    def get_center_lines(self):
        """Gets all of the centerline annotations on this drawing view."""
        # return self._instance.GetCenterLines
        raise NotImplemented

    def get_center_line_sketch(self):
        """Gets the sketch that contains all of the centerline information for this view."""
        # return self._instance.GetCenterLineSketch
        raise NotImplemented

    def get_center_mark_count(self, size):
        """
        Gets the number of center marks that are features in the view.
        :param size: Not used
        """
        # return self._instance.GetCenterMarkCount2(size)
        raise NotImplemented

    def get_center_mark_info(self):
        """Gets information about each center mark that is a feature in the view."""
        # return self._instance.GetCenterMarkInfo
        raise NotImplemented

    def get_center_marks(self):
        """Gets all of the center marks that are features in the view."""
        # return self._instance.GetCenterMarks
        raise NotImplemented

    def get_corresponding(self, input_object):
        """
        Gets the object in this drawing view that corresponds to the specified part or assembly object.
        :param input_object: Pointer to the Dispatch object in a part or assembly (see Remarks)
        """
        # return self._instance.GetCorresponding(input_object)
        raise NotImplemented

    def get_corresponding_entity(self, entity):
        """
        Gets the entity in this drawing view that corresponds to the specified part or assembly entity.
        :param entity: Dispatch pointer to a vertex, face, or edge entity in the part or assembly
        """
        # return self._instance.GetCorrespondingEntity(entity)
        raise NotImplemented

    def get_c_thread_count(self):
        """Gets the number of cosmetic threads in this drawing view."""
        # return self._instance.GetCThreadCount
        raise NotImplemented

    def get_c_thread_quality(self):
        """Gets the cosmetic thread display quality in this view."""
        # return self._instance.GetCThreadQuality
        raise NotImplemented

    def get_c_threads(self):
        """Gets all of the cosmetic threads on this drawing view."""
        # return self._instance.GetCThreads
        raise NotImplemented

    def get_datum_origin_count(self):
        """Gets the number of datum origins on this drawing view."""
        # return self._instance.GetDatumOriginCount
        raise NotImplemented

    def get_datum_origins(self):
        """Gets all of the datum origins on this drawing view."""
        # return self._instance.GetDatumOrigins
        raise NotImplemented

    def get_datum_points(self):
        """Gets all of the information about all the datum points in this view."""
        # return self._instance.GetDatumPoints2
        raise NotImplemented

    def get_datum_points_count(self):
        """Gets the number of datum points in this view."""
        # return self._instance.GetDatumPointsCount
        raise NotImplemented

    def get_datum_tag_count(self):
        """Gets the number of datum tags on this drawing view."""
        # return self._instance.GetDatumTagCount
        raise NotImplemented

    def get_datum_tags(self):
        """Gets all of the datum tags on this drawing view."""
        # return self._instance.GetDatumTags
        raise NotImplemented

    def get_datum_target_sym_count(self):
        """Gets the number of datum target symbols on this drawing view."""
        # return self._instance.GetDatumTargetSymCount
        raise NotImplemented

    def get_datum_target_syms(self):
        """Gets all of the datum target symbols on this drawing view."""
        # return self._instance.GetDatumTargetSyms
        raise NotImplemented

    def get_dependent_view_count(self, all_views, specific_view_type):
        """
        Gets the number of all, or only the specified, dependent views (i.e., alternate position, detail, section, etc.) in this view.
        :param all_views: True to get the number of all of the dependent views in this view, false to get the number of SpecificViewType views in this view
        :param specific_view_type: Type of dependent view as defined in swDrawingViewTypes_e
        """
        # return self._instance.GetDependentViewCount(all_views, specific_view_type)
        raise NotImplemented

    def get_dependent_views(self, all_views, specific_view_type):
        """
        Gets either all, or only the specified, dependent views in this view.
        :param all_views: True to get all of the dependent views in this view, false to get only the SpecificViewType views in this view
        :param specific_view_type: Type of dependent view as defined in swDrawingViewTypes_e
        """
        # return self._instance.GetDependentViews(all_views, specific_view_type)
        raise NotImplemented

    def get_design_table_extent(self):
        """Gets the size and location of the design table associated with this drawing view."""
        # return self._instance.GetDesignTableExtent
        raise NotImplemented

    def get_detail(self):
        """Gets the detail circle for this detail view."""
        # return self._instance.GetDetail
        raise NotImplemented

    def get_detail_circle_count(self, size):
        """
        Gets the number of detail circles in the drawing view.
        :param size: Size, which includes a double for each detail circle; this new double contains the layer ID for the detail circle
        """
        # return self._instance.GetDetailCircleCount2(size)
        raise NotImplemented

    def get_detail_circle_info(self):
        """Gets all of the information about each detail circle in the view."""
        # return self._instance.GetDetailCircleInfo2
        raise NotImplemented

    def get_detail_circles(self):
        """Gets the detail circles in this view."""
        # return self._instance.GetDetailCircles
        raise NotImplemented

    def get_detail_circle_strings(self):
        """Gets an array of strings; each string represents the text label for a detail circle in this view."""
        # return self._instance.GetDetailCircleStrings
        raise NotImplemented

    def get_dimension_count(self):
        """Gets the number of display dimensions in the current drawing sheet or the current drawing view."""
        # return self._instance.GetDimensionCount4
        raise NotImplemented

    def get_dimension_display_info(self):
        """Gets the display dimension information for the current drawing sheet or the current drawing view."""
        # return self._instance.GetDimensionDisplayInfo5
        raise NotImplemented

    def get_dimension_display_info_size(self):
        """Gets the number of  the dimension lines n the current drawing sheet or the current drawing view."""
        # return self._instance.GetDimensionDisplayInfoSize2
        raise NotImplemented

    def get_dimension_display_string(self):
        """Gets all of the dimension text in the current drawing sheet or the current drawing view."""
        # return self._instance.GetDimensionDisplayString4
        raise NotImplemented

    def get_dimension_ids(self):
        """Gets the dimension names from the current drawing sheet or the current drawing view."""
        # return self._instance.GetDimensionIds4
        raise NotImplemented

    def get_dimension_info(self):
        """Gets all of the dimension information in the current drawing sheet or the current drawing view."""
        # return self._instance.GetDimensionInfo6
        raise NotImplemented

    def get_dimension_string(self):
        """Gets the strings containing the text associated with each dimension in the current drawing sheet or the current drawing view."""
        # return self._instance.GetDimensionString4
        raise NotImplemented

    def get_display_data(self):
        """Gets the the IDisplayData object for this drawing view containing only those model items that are visible in the view."""
        # return self._instance.GetDisplayData4
        raise NotImplemented

    def get_display_dimension_count(self):
        """Gets the number of display dimensions in this drawing view."""
        # return self._instance.GetDisplayDimensionCount
        raise NotImplemented

    def get_display_dimensions(self):
        """Gets all of the display dimension on this drawing view."""
        # return self._instance.GetDisplayDimensions
        raise NotImplemented

    def get_display_edges_in_shaded_mode(self):
        """Gets whether to display the edges in this when the drawing view is in shaded mode."""
        # return self._instance.GetDisplayEdgesInShadedMode
        raise NotImplemented

    def get_display_mode(self):
        """Gets the current display mode of the view."""
        # return self._instance.GetDisplayMode2
        raise NotImplemented

    def get_display_tangent_edges(self):
        """Gets the current tangent edge display mode of the drawing view."""
        # return self._instance.GetDisplayTangentEdges2
        raise NotImplemented

    def get_dowel_symbol_count(self):
        """Gets the number of dowel symbols in this drawing view."""
        # return self._instance.GetDowelSymbolCount
        raise NotImplemented

    def get_dowel_symbols(self):
        """Gets all of the dowel symbols on this drawing view."""
        # return self._instance.GetDowelSymbols
        raise NotImplemented

    def get_ellipse_count(self):
        """Gets the number of ellipses in the view."""
        # return self._instance.GetEllipseCount
        raise NotImplemented

    def get_ellipses(self):
        """Gets all of the ellipses added by a user in this drawing view."""
        # return self._instance.GetEllipses5
        raise NotImplemented

    def get_face_hatch_count(self):
        """Gets the number of face hatches in the view."""
        # return self._instance.GetFaceHatchCount
        raise NotImplemented

    def get_face_hatches(self):
        """Gets the face hatches in the view."""
        # return self._instance.GetFaceHatches
        raise NotImplemented

    def get_facetted_hlr_display(self):
        """Gets whether HLR/HLV (Hidden Lines Removed/Hidden Lines Visible) edges should be displayed faceted in the view."""
        # return self._instance.GetFacettedHlrDisplay
        raise NotImplemented

    def get_first_annotation(self):
        """Gets the first annotation in this drawing view."""
        # return self._instance.GetFirstAnnotation3
        raise NotImplemented

    def get_first_center_line(self):
        """Gets the first centerline in this view."""
        # return self._instance.GetFirstCenterLine
        raise NotImplemented

    def get_first_center_mark(self):
        """Gets the first center mark in the view."""
        # return self._instance.GetFirstCenterMark
        raise NotImplemented

    def get_first_center_of_mass(self):
        """Gets the first center of mass in this view."""
        # return self._instance.GetFirstCenterOfMass
        raise NotImplemented

    def get_first_c_thread(self):
        """Gets the first cosmetic thread in the view."""
        # return self._instance.GetFirstCThread
        raise NotImplemented

    def get_first_datum_origin(self):
        """Gets the first datum origin in this drawing view."""
        # return self._instance.GetFirstDatumOrigin
        raise NotImplemented

    def get_first_datum_tag(self):
        """Gets the first datum tag in the view."""
        # return self._instance.GetFirstDatumTag
        raise NotImplemented

    def get_first_datum_target_sym(self):
        """Gets the first datum target symbol in the view."""
        # return self._instance.GetFirstDatumTargetSym
        raise NotImplemented

    def get_first_display_dimension(self):
        """Gets the first display dimension in this drawing view."""
        # return self._instance.GetFirstDisplayDimension5
        raise NotImplemented

    def get_first_dowel_symbol(self):
        """Gets the first dowel symbol in the view."""
        # return self._instance.GetFirstDowelSymbol
        raise NotImplemented

    def get_first_g_t_o_l(self):
        """Gets the first geometric tolerance in this view."""
        # return self._instance.GetFirstGTOL
        raise NotImplemented

    def get_first_multi_jog_leader(self):
        """Gets the first multi-jog leader in the view."""
        # return self._instance.GetFirstMultiJogLeader
        raise NotImplemented

    def get_first_note(self):
        """Gets the first note in the view."""
        # return self._instance.GetFirstNote
        raise NotImplemented

    def get_first_revision_cloud(self):
        """Gets the first revision cloud annotation in this view."""
        # return self._instance.GetFirstRevisionCloud
        raise NotImplemented

    def get_first_s_f_symbol(self):
        """Gets the first surface-finish symbols in the view."""
        # return self._instance.GetFirstSFSymbol
        raise NotImplemented

    def get_first_table_annotation(self):
        """Gets the first table annotation in this view."""
        # return self._instance.GetFirstTableAnnotation
        raise NotImplemented

    def get_first_weld_bead(self):
        """Gets the first weld bead annotation in this view."""
        # return self._instance.GetFirstWeldBead
        raise NotImplemented

    def get_first_weld_symbol(self):
        """Gets the first weld symbol in the view."""
        # return self._instance.GetFirstWeldSymbol
        raise NotImplemented

    def get_g_tol_count(self):
        """Gets the number of geometric tolerances in this drawing view."""
        # return self._instance.GetGTolCount
        raise NotImplemented

    def get_g_tols(self):
        """Gets all of the geometric tolerances on this drawing view."""
        # return self._instance.GetGTols
        raise NotImplemented

    def get_hidden_components(self):
        """Gets the hidden components in this drawing view."""
        # return self._instance.GetHiddenComponents
        raise NotImplemented

    def get_keep_linked_to_b_o_m(self):
        """Gets whether this drawing view is linked to a BOM or weldment cut-list table."""
        # return self._instance.GetKeepLinkedToBOM
        raise NotImplemented

    def get_keep_linked_to_b_o_m_name(self):
        """Gets the name of the BOM or weldment cut-list table feature to which this drawing view is linked."""
        # return self._instance.GetKeepLinkedToBOMName
        raise NotImplemented

    def get_line_count(self, cross_hatch_option):
        """
        Gets the number of lines in this view with an option to include or exclude crosshatch lines.
        :param cross_hatch_option: Crosshatch option as defined in swCrossHatchFilter_e
        """
        # return self._instance.GetLineCount2(cross_hatch_option)
        raise NotImplemented

    def get_lines(self, cross_hatch_option):
        """
        Gets all of the lines in the view with an option to include or exclude crosshatch lines.
        :param cross_hatch_option: Crosshatch option as defined in swCrossHatchFilter_e
        """
        # return self._instance.GetLines4(cross_hatch_option)
        raise NotImplemented

    def get_mirror_view_orientation(self, b_is_mirror_view, l_mirror_view_orientation):
        """
        Gets whether this view is mirrored.
        :param b_is_mirror_view: True if the view is mirrored, false if not
        :param l_mirror_view_orientation: Orientation of the mirror view as defined in swMirrorViewPositions_e
        """
        # return self._instance.GetMirrorViewOrientation(b_is_mirror_view, l_mirror_view_orientation)
        raise NotImplemented

    def get_multi_jog_leader_count(self):
        """Gets the number of multi-jog leaders on this drawing view."""
        # return self._instance.GetMultiJogLeaderCount
        raise NotImplemented

    def get_multi_jog_leaders(self):
        """Gets all of the multi-jog leaders in this drawing view."""
        # return self._instance.GetMultiJogLeaders
        raise NotImplemented

    def get_name(self):
        """Gets the name of this drawing view displayed in the FeatureManager design tree."""
        return self._instance.GetName2

    def get_next_view(self):
        """Gets the next drawing view in the drawing."""
        # return self._instance.GetNextView
        raise NotImplemented

    def get_note_count(self):
        """Gets the number notes in this drawing view."""
        # return self._instance.GetNoteCount
        raise NotImplemented

    def get_notes(self):
        """Gets the notes in this drawing view."""
        # return self._instance.GetNotes
        raise NotImplemented

    def get_orientation_name(self):
        """Gets the predefined name of this view."""
        # return self._instance.GetOrientationName
        raise NotImplemented

    def get_outline(self):
        """Gets the bounding box for a view (sheet or drawing) in meters on the drawing page."""
        # return self._instance.GetOutline
        raise NotImplemented

    def get_parabola_count(self):
        """Gets the number of parabolas in the view."""
        # return self._instance.GetParabolaCount
        raise NotImplemented

    def get_parabolas(self):
        """Gets all of the information about all of the parabolas in this view."""
        # return self._instance.GetParabolas2
        raise NotImplemented

    def get_poly_line_count(self, cross_hatch_option, point_count):
        """
        Gets the number of polylines in this view with an option to include or exclude crosshatch lines.
        :param cross_hatch_option: Crosshatch option as defined in swCrossHatchFilter_e
        :param point_count: Size of array needed to allocate in doubles for IView::IGetPolylines6
        """
        # return self._instance.GetPolyLineCount5(cross_hatch_option, point_count)
        raise NotImplemented

    def get_polylines(self, cross_hatch_option, polylines):
        """
        Gets all of the polylines in the view with an option to include or exclude crosshatch lines.
        :param cross_hatch_option:
0 = include crosshatch lines

1 = exclude crosshatch lines

2 = include only crosshatch lines
        :param polylines: Array of doubles of the lines in the view
        """
        # return self._instance.GetPolylines7(cross_hatch_option, polylines)
        raise NotImplemented

    def get_poly_lines_and_curves(self, cross_hatch_option):
        """
        Gets the arcs, ellipses, splines, and polylines in the view with an option to include or exclude crosshatch lines.
        :param cross_hatch_option:
0 = include crosshatch lines

1 = exclude crosshatch lines

2 = include only crosshatch lines
        """
        # return self._instance.GetPolyLinesAndCurves(cross_hatch_option)
        raise NotImplemented

    def get_poly_lines_and_curves_count(self, cross_hatch_option, point_count):
        """
        Gets the number of lines, including arcs, ellipses, splines, and polylines, in the view with the option to include or exclude cross hatch  lines.
        :param cross_hatch_option: Crosshatch option as defined in swCrossHatchFilter_e
        :param point_count: Size of array to allocate in doubles for IView::IGetPolyLinesAndCurves
        """
        # return self._instance.GetPolyLinesAndCurvesCount(cross_hatch_option, point_count)
        raise NotImplemented

    def get_projection_arrow(self):
        """Gets the projection arrow for this projected view."""
        # return self._instance.GetProjectionArrow
        raise NotImplemented

    def get_projection_line_count(self):
        """Gets the number of projection lines (arrows) in this drawing view."""
        # return self._instance.GetProjectionLineCount
        raise NotImplemented

    def get_projection_lines(self):
        """Gets the projection lines (arrows) in this drawing view."""
        # return self._instance.GetProjectionLines
        raise NotImplemented

    def get_referenced_model_name(self):
        """Gets the name of the model that is referenced in the drawing view."""
        # return self._instance.GetReferencedModelName
        raise NotImplemented

    def get_related_tangent_edge_count(self, bend_line):
        """
        Gets the number of visible tangent edges for the specified bendline in a flat-pattern drawing view.
        :param bend_line: Bendline whose visible tangent edges you want (see Remarks)
        """
        # return self._instance.GetRelatedTangentEdgeCount(bend_line)
        raise NotImplemented

    def get_related_tangent_edges(self, bend_line):
        """
        Gets the visible tangent edges for the specified bendline in a flat-pattern drawing view.
        :param bend_line: Bendline whose visible tangent edges you want (see Remarks)
        """
        # return self._instance.GetRelatedTangentEdges(bend_line)
        raise NotImplemented

    def get_revision_cloud_count(self):
        """Gets the number of revision cloud annotations in this view."""
        # return self._instance.GetRevisionCloudCount
        raise NotImplemented

    def get_revision_clouds(self):
        """Gets all of the revision cloud annotations in this view."""
        # return self._instance.GetRevisionClouds
        raise NotImplemented

    def get_section(self):
        """Gets the section for this section view."""
        # return self._instance.GetSection
        raise NotImplemented

    def get_section_line_count(self, size):
        """
        Gets the number of section lines in the view.
        :param size: Size, which includes an extra double per section line containing the layer ID for the section line
        """
        # return self._instance.GetSectionLineCount2(size)
        raise NotImplemented

    def get_section_line_info(self):
        """Gets all of the information about the section lines in the view."""
        # return self._instance.GetSectionLineInfo2
        raise NotImplemented

    def get_section_lines(self):
        """Gets the section lines in the view."""
        # return self._instance.GetSectionLines
        raise NotImplemented

    def get_section_line_strings(self):
        """Gets an array of strings; each string represents the text label for a section line in this view."""
        # return self._instance.GetSectionLineStrings
        raise NotImplemented

    def get_s_f_symbol_count(self):
        """Gets the number of surface finish symbols on this drawing view."""
        # return self._instance.GetSFSymbolCount
        raise NotImplemented

    def get_s_f_symbols(self):
        """Gets all of the surface finish symbols in this drawing view."""
        # return self._instance.GetSFSymbols
        raise NotImplemented

    def get_sketch(self):
        """Gets the sketch used by this view."""
        # return self._instance.GetSketch
        raise NotImplemented

    def get_sketch_picture_count(self):
        """Gets the number of sketch pictures imported to this view when a drawing is created from a part."""
        # return self._instance.GetSketchPictureCount
        raise NotImplemented

    def get_sketch_pictures(self):
        """Gets all of the sketch pictures imported to this view when a drawing is created from a part."""
        # return self._instance.GetSketchPictures
        raise NotImplemented

    def get_s_m_boundary_box_display_data(self):
        """Gets the boundary-box sketch display data of a flat-pattern drawing view."""
        # return self._instance.GetSMBoundaryBoxDisplayData2
        raise NotImplemented

    def get_solid_hatch_count(self, array_size):
        """
        Gets the number of visible solid-fill hatches in a detail, break, or crop view and the size of the array for their boundary data.
        :param array_size: Number of solid-fill hatches
        """
        # return self._instance.GetSolidHatchCount(array_size)
        raise NotImplemented

    def get_solid_hatch_info(self):
        """Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view."""
        # return self._instance.GetSolidHatchInfo
        raise NotImplemented

    def get_spline_count(self, point_count):
        """
        Gets the number of splines in the view.
        :param point_count: Number of doubles (see IView::GetSplines3 or IView::IGetSplines3 Remarks)
        """
        # return self._instance.GetSplineCount(point_count)
        raise NotImplemented

    def get_splines(self):
        """Gets all of the splines added by a user in the drawing view."""
        # return self._instance.GetSplines3
        raise NotImplemented

    def get_table_annotation_count(self):
        """Gets the number of table annotations in this drawing view."""
        # return self._instance.GetTableAnnotationCount
        raise NotImplemented

    def get_table_annotations(self):
        """Gets all of the table annotations on this drawing view."""
        # return self._instance.GetTableAnnotations
        raise NotImplemented

    def get_temporary_axes(self):
        """Gets the information of the temporary axes displayed in this view."""
        # return self._instance.GetTemporaryAxes
        raise NotImplemented

    def get_temporary_axes_count(self):
        """Gets the number of temporary axes in this view."""
        # return self._instance.GetTemporaryAxesCount
        raise NotImplemented

    def get_unique_name(self):
        """Gets the unique name of this section view."""
        # return self._instance.GetUniqueName
        raise NotImplemented

    def get_use_parent_display_mode(self):
        """Gets whether the view is using its parent settings or if it is using its own local settings."""
        # return self._instance.GetUseParentDisplayMode
        raise NotImplemented

    def get_user_points(self):
        """Gets all of the information about all of the user points in this view."""
        # return self._instance.GetUserPoints2
        raise NotImplemented

    def get_user_points_count(self):
        """Gets the number of user points in the view."""
        # return self._instance.GetUserPointsCount
        raise NotImplemented

    def get_view_xform(self):
        """Gets the transform from model space origin to drawing space origin."""
        # return self._instance.GetViewXform
        raise NotImplemented

    def get_visible(self):
        """Gets the visibility of this drawing view."""
        # return self._instance.GetVisible
        raise NotImplemented

    def get_visible_component_count(self):
        """Gets the number of visible components in this drawing view."""
        # return self._instance.GetVisibleComponentCount
        raise NotImplemented

    def get_visible_components(self):
        """Gets the visible components in this drawing view."""
        # return self._instance.GetVisibleComponents
        raise NotImplemented

    def get_visible_drawing_components(self):
        """Gets all of the unobscured drawing components in this drawing view of an assembly drawing."""
        # return self._instance.GetVisibleDrawingComponents
        raise NotImplemented

    def get_visible_entities(self, lp_view_component, entity_type):
        """
        Gets the visible entities of the specified type for the specified component in this drawing view.
        :param lp_view_component: Component from which to get EntityType
        :param entity_type: Type of entity as defined in swViewEntityType_e
        """
        # return self._instance.GetVisibleEntities2(lp_view_component, entity_type)
        raise NotImplemented

    def get_visible_entity_count(self, lp_view_component, entity_type):
        """
        Gets the number of visible entities of the specified type for the specified component in this drawing view.
        :param lp_view_component: Component from which to get the visible EntityType
        :param entity_type: Type of entity as defined in swViewEntityType_e
        """
        # return self._instance.GetVisibleEntityCount2(lp_view_component, entity_type)
        raise NotImplemented

    def get_weld_bead_count(self):
        """Gets the number of weld beads on this drawing view."""
        # return self._instance.GetWeldBeadCount
        raise NotImplemented

    def get_weld_beads(self):
        """Gets all of the weld beads on this drawing view."""
        # return self._instance.GetWeldBeads
        raise NotImplemented

    def get_weld_symbol_count(self):
        """Gets the number of weld symbols on this drawing view."""
        # return self._instance.GetWeldSymbolCount
        raise NotImplemented

    def get_weld_symbols(self):
        """Gets all of the weld symbols on this drawing view."""
        # return self._instance.GetWeldSymbols
        raise NotImplemented

    def get_witness_entities_count(self, size):
        """
        Gets the number of virtual sharp witness lines in this drawing view.
        :param size: Size of the virtual sharp witness line data array (see Remarks)
        """
        # return self._instance.GetWitnessEntitiesCount(size)
        raise NotImplemented

    def get_witness_geom_info(self):
        """Gets the geometry data for all of the virtual sharp witness lines in this drawing view."""
        # return self._instance.GetWitnessGeomInfo
        raise NotImplemented

    def get_xform(self):
        """Gets the matrix used for displaying this drawing view."""
        # return self._instance.GetXform
        raise NotImplemented

    def has_design_table(self):
        """Gets whether this drawing view has a design table associated with it."""
        # return self._instance.HasDesignTable
        raise NotImplemented

    def i_get_annotations(self, num_annotations):
        """
        Gets the annotations in this view.
        :param num_annotations: Number of annotations
        """
        # return self._instance.IGetAnnotations(num_annotations)
        raise NotImplemented

    def i_get_arcs(self):
        """Gets all of the information for all of the arcs added by a user in this drawing view."""
        # return self._instance.IGetArcs4
        raise NotImplemented

    def i_get_base_view(self):
        """Gets the base (parent) view used to create this view."""
        # return self._instance.IGetBaseView
        raise NotImplemented

    def i_get_bend_lines(self, number_of_bend_line):
        """
        Gets the bendlines in a flat-pattern drawing view.
        :param number_of_bend_line: Number of bendlines in a flat-pattern drawing view
        """
        # return self._instance.IGetBendLines(number_of_bend_line)
        raise NotImplemented

    def i_get_bodies(self, count):
        """
        Gets the bodies of a multibody part in the drawing view.
        :param count: Number of bodies of a multibody part in the drawing view
        """
        # return self._instance.IGetBodies(count)
        raise NotImplemented

    def i_get_bom_table(self):
        """Gets the BOM table found in this drawing view."""
        # return self._instance.IGetBomTable
        raise NotImplemented

    def i_get_break_line_info(self, array_size):
        """
        Gets information for all of the break lines in this view.
        :param array_size: Number of break lines
        """
        # return self._instance.IGetBreakLineInfo2(array_size)
        raise NotImplemented

    def i_get_break_lines(self, count):
        """
        Gets the all of the breaks in this view.
        :param count: Number of breaks in the view
        """
        # return self._instance.IGetBreakLines(count)
        raise NotImplemented

    def i_get_break_out_sections(self, count):
        """
        Gets all of the broken-out sections in this view.
        :param count: Number of broken-out sections in this view
        """
        # return self._instance.IGetBreakOutSections(count)
        raise NotImplemented

    def i_get_center_lines(self, num_center_line):
        """
        Gets all of the centerlines on this drawing view.
        :param num_center_line: Total number of centerlines on this drawing view
        """
        # return self._instance.IGetCenterLines(num_center_line)
        raise NotImplemented

    def i_get_center_mark_info(self):
        """Gets information about each center mark that is a feature in the view."""
        # return self._instance.IGetCenterMarkInfo
        raise NotImplemented

    def i_get_center_marks(self, count):
        """
        Gets all of the center marks that are features in the view.
        :param count: Number of center marks that are features in the view
        """
        # return self._instance.IGetCenterMarks(count)
        raise NotImplemented

    def i_get_c_threads(self, num_c_thread):
        """
        Gets all of the cosmetic threads on this drawing view.
        :param num_c_thread: Total number of cosmetic threads on the drawing view
        """
        # return self._instance.IGetCThreads(num_c_thread)
        raise NotImplemented

    def i_get_datum_origins(self, num_datum_origin):
        """
        Gets all of the datum origins on this drawing view.
        :param num_datum_origin: Total number of datum origins on the drawing view
        """
        # return self._instance.IGetDatumOrigins(num_datum_origin)
        raise NotImplemented

    def i_get_datum_points(self):
        """Gets all of the information about all the datum points in this view."""
        # return self._instance.IGetDatumPoints2
        raise NotImplemented

    def i_get_datum_tags(self, num_datum_tag):
        """
        Gets all the datum tags on this drawing view.
        :param num_datum_tag: Total number of datum tags on the drawing view
        """
        # return self._instance.IGetDatumTags(num_datum_tag)
        raise NotImplemented

    def i_get_datum_target_syms(self, num_datum_target_sym):
        """
        Gets all of the datum target symbols on this drawing view.
        :param num_datum_target_sym: Total number of datum target symbols on the drawing view
        """
        # return self._instance.IGetDatumTargetSyms(num_datum_target_sym)
        raise NotImplemented

    def i_get_dependent_views(self, all_views, specific_view_type, dependent_view_count):
        """
        Gets either all, or only the specified, dependent views in this view.
        :param all_views: True to get all of the dependent views in this view, false to get only the SpecificViewType views in this view
        :param specific_view_type: Type of dependent view as defined in swDrawingViewTypes_e
        :param dependent_view_count: Number of dependent views
        """
        # return self._instance.IGetDependentViews(all_views, specific_view_type, dependent_view_count)
        raise NotImplemented

    def i_get_design_table_extent(self):
        """Gets the size and location of the design table associated with this drawing view."""
        # return self._instance.IGetDesignTableExtent
        raise NotImplemented

    def i_get_detail(self):
        """Gets the detail circle for this detail view."""
        # return self._instance.IGetDetail
        raise NotImplemented

    def i_get_detail_circle_info(self, array_size):
        """
        Gets all of the information about each detail circle in the view.
        :param array_size: Extra double for each detail circle; this array entity contains the layer ID for the detail circle, and it is the first entity in the array for each detail circle (see Remarks)
        """
        # return self._instance.IGetDetailCircleInfo2(array_size)
        raise NotImplemented

    def i_get_detail_circles(self, num_detail_circles):
        """
        Gets the detail circles in this view.
        :param num_detail_circles: Number of detail circles in the view
        """
        # return self._instance.IGetDetailCircles(num_detail_circles)
        raise NotImplemented

    def i_get_detail_circle_strings(self):
        """Gets an array of strings; each string represents the text label for a detail circle in this view."""
        # return self._instance.IGetDetailCircleStrings
        raise NotImplemented

    def i_get_dimension_display_info(self, array_size):
        """
        Gets the display dimension information for the current drawing sheet or the current drawing view.
        :param array_size: Number of items in the array
        """
        # return self._instance.IGetDimensionDisplayInfo5(array_size)
        raise NotImplemented

    def i_get_dimension_display_string(self):
        """Gets all of the dimension text in the current drawing sheet or the current drawing view."""
        # return self._instance.IGetDimensionDisplayString4
        raise NotImplemented

    def i_get_dimension_ids(self):
        """Gets the dimension names from the current drawing sheet or the current drawing view."""
        # return self._instance.IGetDimensionIds4
        raise NotImplemented

    def i_get_dimension_info(self):
        """Gets all of the dimension information in the current drawing sheet or the current drawing view."""
        # return self._instance.IGetDimensionInfo6
        raise NotImplemented

    def i_get_dimension_string(self):
        """Gets the strings containing the text associated with each dimension in the current drawing sheet or the current drawing view."""
        # return self._instance.IGetDimensionString4
        raise NotImplemented

    def i_get_display_data(self):
        """Gets the the IDisplayData object for this drawing view containing only those model items that are visible in the view."""
        # return self._instance.IGetDisplayData3
        raise NotImplemented

    def i_get_display_dimensions(self, num_display_dim):
        """
        Gets all of the display dimensions on this drawing view.
        :param num_display_dim: Total number of display dimensions on this drawing view
        """
        # return self._instance.IGetDisplayDimensions(num_display_dim)
        raise NotImplemented

    def i_get_dowel_symbols(self, num_dowel_symbol):
        """
        Gets all of the dowel symbols on this drawing view.
        :param num_dowel_symbol: Total number of dowel symbols on this drawing view
        """
        # return self._instance.IGetDowelSymbols(num_dowel_symbol)
        raise NotImplemented

    def i_get_ellipses(self):
        """Gets all of the ellipses added by a user in this drawing view."""
        # return self._instance.IGetEllipses5
        raise NotImplemented

    def i_get_face_hatches(self, num_faces_hatches):
        """
        Gets the face hatches in the view.
        :param num_faces_hatches: Number of face hatches in the view
        """
        # return self._instance.IGetFaceHatches(num_faces_hatches)
        raise NotImplemented

    def i_get_first_center_of_mass(self):
        """Gets the first center of mass in this view."""
        # return self._instance.IGetFirstCenterOfMass
        raise NotImplemented

    def i_get_first_c_thread(self):
        """Gets the first cosmetic thread in the view."""
        # return self._instance.IGetFirstCThread
        raise NotImplemented

    def i_get_first_datum_tag(self):
        """Gets the first datum tag in the view."""
        # return self._instance.IGetFirstDatumTag
        raise NotImplemented

    def i_get_first_datum_target_sym(self):
        """Gets the first datum target symbol in the view."""
        # return self._instance.IGetFirstDatumTargetSym
        raise NotImplemented

    def i_get_first_dowel_symbol(self):
        """Gets the first dowel symbol in the view."""
        # return self._instance.IGetFirstDowelSymbol
        raise NotImplemented

    def i_get_first_g_t_o_l(self):
        """Gets the first geometric tolerance in this view."""
        # return self._instance.IGetFirstGTOL
        raise NotImplemented

    def i_get_first_multi_jog_leader(self):
        """Gets the first multi-jog leader in the view."""
        # return self._instance.IGetFirstMultiJogLeader
        raise NotImplemented

    def i_get_first_note(self):
        """Gets the first note in the view."""
        # return self._instance.IGetFirstNote
        raise NotImplemented

    def i_get_first_revision_cloud(self):
        """Gets the first revision cloud annotation in this view."""
        # return self._instance.IGetFirstRevisionCloud
        raise NotImplemented

    def i_get_first_s_f_symbol(self):
        """Gets the first surface-finish symbols in the view."""
        # return self._instance.IGetFirstSFSymbol
        raise NotImplemented

    def i_get_first_weld_symbol(self):
        """Gets the first weld symbol in the view."""
        # return self._instance.IGetFirstWeldSymbol
        raise NotImplemented

    def i_get_g_tols(self, num_g_tol):
        """
        Gets all of the geometric tolerances on this drawing view.
        :param num_g_tol: Total number of geometric tolerances on this drawing view.
        """
        # return self._instance.IGetGTols(num_g_tol)
        raise NotImplemented

    def i_get_lines(self, cross_hatch_option, array_size):
        """
        Gets all of the lines in the view with an option to include or exclude crosshatch lines.
        :param cross_hatch_option: Crosshatch option as defined in swCrossHatchFilter_e
        :param array_size: Number of lines in the view
        """
        # return self._instance.IGetLines4(cross_hatch_option, array_size)
        raise NotImplemented

    def i_get_multi_jog_leaders(self, num_multi_jog_leader):
        """
        Gets all of the multi-jog leaders in this drawing view.
        :param num_multi_jog_leader: Number of multi-jog leaders in this drawing view.
        """
        # return self._instance.IGetMultiJogLeaders(num_multi_jog_leader)
        raise NotImplemented

    def i_get_next_view(self):
        """Gets the next drawing view in the drawing."""
        # return self._instance.IGetNextView
        raise NotImplemented

    def i_get_notes(self, number_of_notes):
        """
        Gets the notes in this drawing view.
        :param number_of_notes: Number of notes in this drawing view
        """
        # return self._instance.IGetNotes(number_of_notes)
        raise NotImplemented

    def i_get_outline(self):
        """Gets the bounding box for a view (sheet or drawing) in meters on the drawing page."""
        # return self._instance.IGetOutline
        raise NotImplemented

    def i_get_parabolas(self):
        """Gets all of the information about all of the parabolas in this view."""
        # return self._instance.IGetParabolas2
        raise NotImplemented

    def i_get_polylines(self, cross_hatch_option, array_size, polylines, edge_array_size):
        """
        Gets all of the polylines in the view with an option to include or exclude crosshatch lines
        :param cross_hatch_option:
0 = include crosshatch lines

1 = exclude crosshatch lines

2 = include only crosshatch lines
        :param array_size: Number of lines in the view
        :param polylines: Array of doubles of the lines in the view of size ArraySize
        :param edge_array_size: Size of array of modeling edges
        """
        # return self._instance.IGetPolylines7(cross_hatch_option, array_size, polylines, edge_array_size)
        raise NotImplemented

    def i_get_poly_lines_and_curves(self, cross_hatch_option, array_size):
        """
        Gets the arcs, ellipses, splines, and polylines in the view with an option to include or exclude crosshatch lines.
        :param cross_hatch_option:
0 = include crosshatch lines

1 = exclude crosshatch lines

2 = include only crosshatch lines
        :param array_size: Size of the array of lines and parameters in the view
        """
        # return self._instance.IGetPolyLinesAndCurves(cross_hatch_option, array_size)
        raise NotImplemented

    def i_get_projection_arrow(self):
        """Gets the projection arrow for this projected view."""
        # return self._instance.IGetProjectionArrow
        raise NotImplemented

    def i_get_projection_lines(self, count):
        """
        Gets the projection lines (arrows) in this drawing view.
        :param count: Number of projection lines
        """
        # return self._instance.IGetProjectionLines(count)
        raise NotImplemented

    def i_get_related_tangent_edges(self, bend_line, num_of_tangent_edges):
        """
        Gets the visible tangent edges for the specified bendline in a flat-pattern drawing view.
        :param bend_line: Bendline whose visible tangent edges you want (see Remarks)
        :param num_of_tangent_edges: Number of visible tangent edges for the specified bendline
        """
        # return self._instance.IGetRelatedTangentEdges(bend_line, num_of_tangent_edges)
        raise NotImplemented

    def i_get_revision_clouds(self, num_rev_clouds):
        """
        Gets all of the revision cloud annotations in this view.
        :param num_rev_clouds: Number of revision cloud annotations in this view (see Remarks)
        """
        # return self._instance.IGetRevisionClouds(num_rev_clouds)
        raise NotImplemented

    def i_get_section(self):
        """Gets the section for this section view."""
        # return self._instance.IGetSection
        raise NotImplemented

    def i_get_section_line_info(self, array_size):
        """
        Gets all of the information about the section lines in the view.
        :param array_size: Number of section lines
        """
        # return self._instance.IGetSectionLineInfo2(array_size)
        raise NotImplemented

    def i_get_section_lines(self):
        """Gets the section lines in the view."""
        # return self._instance.IGetSectionLines
        raise NotImplemented

    def i_get_section_line_strings(self):
        """Gets an array of strings; each string represents the text label for a section line in this view."""
        # return self._instance.IGetSectionLineStrings
        raise NotImplemented

    def i_get_s_f_symbols(self, num_s_f_symbol):
        """
        Gets all of the surface finish symbols in this drawing view.
        :param num_s_f_symbol: Total number of surface finish symbols this drawing view
        """
        # return self._instance.IGetSFSymbols(num_s_f_symbol)
        raise NotImplemented

    def i_get_sketch(self):
        """Gets the sketch used by this view."""
        # return self._instance.IGetSketch
        raise NotImplemented

    def i_get_sketch_pictures(self, count):
        """
        Gets all of the sketch pictures imported to this view when a drawing is created from a part.
        :param count: Number of sketch pictures in this view
        """
        # return self._instance.IGetSketchPictures(count)
        raise NotImplemented

    def i_get_s_m_boundary_box_display_data(self):
        """Gets the boundary-box sketch display data of a flat-pattern drawing view."""
        # return self._instance.IGetSMBoundaryBoxDisplayData
        raise NotImplemented

    def i_get_solid_hatch_info(self, array_size):
        """
        Gets the boundary data for all visible solid-fill hatches in a detail, break, or crop view.
        :param array_size: Size of array to allocate for the boundary data as determined by IView::GetSolidHatchCount
        """
        # return self._instance.IGetSolidHatchInfo(array_size)
        raise NotImplemented

    def i_get_splines(self):
        """Gets all of the splines added by a user in the drawing view."""
        # return self._instance.IGetSplines3
        raise NotImplemented

    def i_get_table_annotations(self, num_table_annotation):
        """
        Gets all of the table annotations in this drawing view.
        :param num_table_annotation: Total number of table annotations in this drawing view
        """
        # return self._instance.IGetTableAnnotations(num_table_annotation)
        raise NotImplemented

    def i_get_temporary_axes(self, temp_axes_count):
        """
        Gets the information of the temporary axes displayed in this view.
        :param temp_axes_count: Number of temporary axes
\
        """
        # return self._instance.IGetTemporaryAxes(temp_axes_count)
        raise NotImplemented

    def i_get_user_points(self):
        """Gets all of the information about all of the user points in this view."""
        # return self._instance.IGetUserPoints2
        raise NotImplemented

    def i_get_view_xform(self):
        """Gets the transform from model space origin to drawing space origin."""
        # return self._instance.IGetViewXform
        raise NotImplemented

    def i_get_visible_components(self, view_component_count):
        """
        Gets the visible components in this drawing view.
        :param view_component_count: Number of visible components
        """
        # return self._instance.IGetVisibleComponents(view_component_count)
        raise NotImplemented

    def i_get_visible_entities(self, lp_view_component, entity_type, view_entity_count):
        """
        Gets the visible entities of the specified type for the specified component in this drawing view.
        :param lp_view_component: Component from which to get EntityType
        :param entity_type: Type of entity as defined in swViewEntityType_e
        :param view_entity_count: Number of visible entities of EntityType in LpViewComponent
        """
        # return self._instance.IGetVisibleEntities2(lp_view_component, entity_type, view_entity_count)
        raise NotImplemented

    def i_get_weld_beads(self, num_weld_bead):
        """
        Gets all of the weld beads on this drawing view.
        :param num_weld_bead: Total number of weld beads on this drawing view
        """
        # return self._instance.IGetWeldBeads(num_weld_bead)
        raise NotImplemented

    def i_get_weld_symbols(self, num_weld_symbol):
        """
        Gets all of the weld symbols on this drawing view.
        :param num_weld_symbol: Total number of weld symbols on this drawing view
        """
        # return self._instance.IGetWeldSymbols(num_weld_symbol)
        raise NotImplemented

    def i_get_witness_geom_info(self, array_size):
        """
        Gets the geometry data for all of the virtual sharp witness lines in this drawing view.
        :param array_size: Size of the virtual sharp witness line geometry data array (see Remarks)
        """
        # return self._instance.IGetWitnessGeomInfo(array_size)
        raise NotImplemented

    def i_get_xform(self):
        """Gets the matrix used for displaying this drawing view."""
        # return self._instance.IGetXform
        raise NotImplemented

    def i_insert_bom_table(self, template, xloc, yloc, errors):
        """
        Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel.
        :param template: File name of the template to use to create this BOM
        :param xloc: X coordinate of the location of the BOM
        :param yloc: Y coordinate of the location of the BOM
        :param errors: Status of the BOM creation operation as defined in swBOMConfigurationCreationErrors_e
        """
        # return self._instance.IInsertBomTable(template, xloc, yloc, errors)
        raise NotImplemented

    def insert_alternate_view(self, configuration_name):
        """
        Inserts an Alternate Position View of the currently selected drawing view.
        :param configuration_name: Name of the configuration (see Remarks)
        """
        # return self._instance.InsertAlternateView(configuration_name)
        raise NotImplemented

    def insert_bend_table(self, use_anchor_point, x, y, anchor_type, start_value, table_template):
        """
        Inserts a bend table for this drawing view.
        :param use_anchor_point: True to insert the bend table at the sheet format anchor point, false to insert it at the point specified by the X and Y parameters of this method
        :param x: X-coordinate for placement of the bend table; valid only when UseAnchorPoint is false
        :param y: Y-coordinate for placement of the bend table; valid only when UseAnchorPoint is false
        :param anchor_type: Anchor type as defined in swBomConfigurationAnchorType_e
        :param start_value: Starting datum tag; a value from A to Z for letter tags; a positive integer for number tags
        :param table_template: Full pathname of the template (e.g., install_dir\lang\language\bendtable-standard.sldbndtbt)
        """
        # return self._instance.InsertBendTable(use_anchor_point, x, y, anchor_type, start_value, table_template)
        raise NotImplemented

    def insert_bom_table(self, template, xloc, yloc, errors):
        """
        Inserts a Bill of Materials (BOM) table for this drawing view using Microsoft Excel.
        :param template: File name of the template to use to create this BOM
        :param xloc: X coordinate of the location of the BOM
        :param yloc: Y coordinate of the location of the BOM
        :param errors: Status of the BOM creation operation as defined in swBOMConfigurationCreationErrors_e
        """
        # return self._instance.InsertBomTable(template, xloc, yloc, errors)
        raise NotImplemented

    def insert_bom_table(self, use_anchor_point, x, y, anchor_type, bom_type, configuration, table_template, hidden,
                         indented_numbering_type, detailed_cut_list):
        """
        Inserts a bill of materials (BOM) table for this drawing view using SOLIDWORKS table functionality.
        :param use_anchor_point: If true and the appropriate sheet format anchor point exists, then insert table at this point; if false, then use the values
specified for the X and Y arguments as the insertion point
        :param x: X coordinate for the placement of the BOM table
        :param y: Y coordinate for the placement of the BOM table
        :param anchor_type: Anchor type as defined by swBomConfigurationAnchorType_e
        :param bom_type: Type of BOM table as defined by swBomType_e
        :param configuration: Name of the configuration for this BOM table (see Remarks)
        :param table_template: Path and filename of the template that you want to use that corresponds to this type of table (see Remarks)
        :param hidden: True to hide the BOM table, false to show it
        :param indented_numbering_type: Type of numbering as defined by swNumberingType_e; valid only for BomType = swBomType_e.swBomType_Indented
        :param detailed_cut_list: True to show the detailed cut list, false to not; valid only for BomType = swBomType_e.swBomType_Indented
        """
        # return self._instance.InsertBomTable4(use_anchor_point, x, y, anchor_type, bom_type, configuration, table_template, hidden, indented_numbering_type, detailed_cut_list)
        raise NotImplemented

    def insert_break(self, orientation, position1, position2, style, shape_intensity, break_sketch_blocks):
        """
        Inserts the specified type of break at the specified location in this drawing view.
        :param orientation: Horizontal or vertical cut as defined in swBreakLineOrientation_e
        :param position1: Location of the first line in the break (see Remarks)
        :param position2: Location of the second line in the break (see Remarks)
        :param style: Break line style as defined in swBreakLineStyle_e
        :param shape_intensity: Shape intensity for jagged cut break lines only; valid range is 1 (most) through 5 (least)
        :param break_sketch_blocks: True to break sketch blocks, false to not
        """
        # return self._instance.InsertBreak3(orientation, position1, position2, style, shape_intensity, break_sketch_blocks)
        raise NotImplemented

    def insert_cut_list_property_note(self, x, y, z):
        """
        Inserts a note that contains all of the cut list item properties of a sheet metal part.
        :param x: x coordinate of the note
        :param y: y coordinate of the note
        :param z: z coordinate of the note
        """
        # return self._instance.InsertCutListPropertyNote(x, y, z)
        raise NotImplemented

    def insert_hole_table(self, use_anchor_point, x, y, anchor_type, start_value, template, tag_order, tag_type,
                          manual_tags):
        """
        Inserts a hole table in this drawing view.
        :param use_anchor_point: If true, and the sheet format anchor point exists, then insert table at the anchor point; if false, then insert the table at the location specified by the X and Y parameters
        :param x: X coordinate in meters for the anchor of this hole table
        :param y: Y coordinate in meters for the anchor of this hole table
        :param anchor_type: Anchor type as defined by swBomConfigurationAnchorType_e
        :param start_value: Starting value for the specified TagType
        :param template: Path and filename of the hole table template that corresponds to the hole table you want to create (see Remarks)
        :param tag_order: Tag numbering as defined in swHoleTableTagOrder_e
        :param tag_type: Tag type as defined in swHoleTableTagStyle_e
        :param manual_tags: Array of custom tags; valid only if TagType is swHoleTableTagStyle_e.swHoleTable_ManualTags
        """
        # return self._instance.InsertHoleTable3(use_anchor_point, x, y, anchor_type, start_value, template, tag_order, tag_type, manual_tags)
        raise NotImplemented

    def insert_punch_table(self, use_anchor_point, x, y, anchor_type, start_value, table_template):
        """
        Inserts a punch table in the flat pattern drawing view of a sheet metal part.
        :param use_anchor_point: If true, and the sheet format anchor point exists, then insert table at the anchor point; if false, then insert the table at the location specified by the X and Y parameters
        :param x: X coordinate for the anchor of this punch table
        :param y: Y coordinate for the anchor of this punch table
        :param anchor_type: Anchor type as defined by swBomConfigurationAnchorType_e
        :param start_value: Starting value for datum tags; a letter from A to Z, if TableTemplate uses letter tags; a positive integer, if TableTemplate uses number tags (see Remarks)
        :param table_template: Path and filename of the table template that corresponds to the type of table you want to use (see Remarks)
        """
        # return self._instance.InsertPunchTable(use_anchor_point, x, y, anchor_type, start_value, table_template)
        raise NotImplemented

    def insert_view_as_block(self, insertion_point, position):
        """
        Creates a sketch block from this view and aligns the specified manipulator point with the specified sketch block position on the drawing sheet.
        :param insertion_point: IMathPoint in this view where the manipulator of the new sketch block is located
        :param position: IMathPoint on the drawing sheet where the new sketch block manipulator is positioned
        """
        # return self._instance.InsertViewAsBlock(insertion_point, position)
        raise NotImplemented

    def insert_weldment_table(self, use_anchor_point, x, y, anchor_type, configuration, table_template):
        """
        Inserts a weldment cut-list table into this drawing view.
        :param use_anchor_point: If true and the appropriate sheet format anchor point exists, then insert table at this point; if false, then use the values specified for the X and Y arguments as the insertion point
        :param x: X coordinate for the placement of the weldment cut-list table; valid only if UserAnchorPoint = False 
        :param y: Y coordinate for the placement of the weldment cut-list table; valid only if UseAnchorPoint = False
        :param anchor_type: Anchor type as defined by swBomConfigurationAnchorType_e
        :param configuration: Name of the "As Welded" configuration for the weldment cut-list table
        :param table_template: Path and filename of the template that corresponds to this type of table (see Remarks)
        """
        # return self._instance.InsertWeldmentTable(use_anchor_point, x, y, anchor_type, configuration, table_template)
        raise NotImplemented

    def insert_weld_table(self, use_anchor_point, include_annotations, combine_same_type, x, y, anchor_type,
                          configuration, table_template):
        """
        Inserts a weld table into this drawing view.
        :param use_anchor_point: If true and the appropriate sheet format anchor point exists, then insert the table at the anchor point; if false, then use the values specified for the X and Y arguments as the insertion point
        :param include_annotations: True to include weld symbols not attached to cosmetic weld features, false to not
        :param combine_same_type: True to group welds having the same weld symbol and weld size, false to not
        :param x: X coordinate in meters for the placement of the weld table; valid only if UseAnchorPoint = False
        :param y: Y coordinate in meters for the placement of the weld table; valid only if UseAnchorPoint = False
        :param anchor_type: Anchor type as defined by swBomConfigurationAnchorType_e
        :param configuration: Name of the part configuration for which to insert the weld table
        :param table_template: Path and filename of the template that corresponds to this type of table (see Remarks)
        """
        # return self._instance.InsertWeldTable(use_anchor_point, include_annotations, combine_same_type, x, y, anchor_type, configuration, table_template)
        raise NotImplemented

    def is_broken(self):
        """Gets whether the drawing view is displayed with a break."""
        # return self._instance.IsBroken
        raise NotImplemented

    def is_cropped(self):
        """Get whether this drawing view is cropped."""
        # return self._instance.IsCropped
        raise NotImplemented

    def i_select_entity(self, entity, append_flag):
        """
        Selects an entity in this drawing view.
        :param entity: Entity
        :param append_flag: True appends the entity to the selection list, false replaces the selection list with the entity
        """
        # return self._instance.ISelectEntity(entity, append_flag)
        raise NotImplemented

    def i_set_bodies(self, count, body_array):
        """
        Sets the bodies of a multibody part to include in the view.
        :param count: Number of bodies in a multibody part
        :param body_array:
in-process, unmanaged C++: Pointer to an array of bodies
VBA, VB.NET, C#, and C++/CLI: Not supported

See In-process Methods for details about this type of method.
        """
        # return self._instance.ISetBodies(count, body_array)
        raise NotImplemented

    def i_set_xform(self, transform):
        """
        Sets the matrix used for display of this drawing view.
        :param transform: Array of 3 doubles (see Remarks)
        """
        # return self._instance.ISetXform(transform)
        raise NotImplemented

    def is_exploded(self):
        """Gets whether the drawing view is currently showing the assembly as exploded or collasped."""
        # return self._instance.IsExploded
        raise NotImplemented

    def is_flat_pattern_view(self):
        """Gets whether a drawing view is a flat-pattern drawing view."""
        # return self._instance.IsFlatPatternView
        raise NotImplemented

    def is_lightweight(self):
        """Gets whether the drawing view is lightweight."""
        # return self._instance.IsLightweight
        raise NotImplemented

    def is_model_break_state(self):
        """Gets whether this drawing view is a Model Break View."""
        # return self._instance.IsModelBreakState
        raise NotImplemented

    def is_model_loaded(self):
        """Gets whether the model is loaded in this drawing view."""
        # return self._instance.IsModelLoaded
        raise NotImplemented

    def is_model_out_of_date(self):
        """Gets whether the model in this drawing view is up-to-date with the current model."""
        # return self._instance.IsModelOutOfDate
        raise NotImplemented

    def is_perspective_view(self):
        """Gets whether this drawing view is showing a perspective view of the model."""
        # return self._instance.IsPerspectiveView
        raise NotImplemented

    def load_model(self):
        """Loads the model if the model has not already been loaded for this drawing view."""
        # return self._instance.LoadModel
        raise NotImplemented

    def merge_bend_tags(self, merge, bend_notes):
        """
        Merges or unmerges bend tags in drawings of sheet metal parts.
        :param merge: True to merge bend tags, false to unmerge a merged bend tag
        :param bend_notes: Array of two or more bend tags to merge or an array of one merged bend tag to unmerge
        """
        # return self._instance.MergeBendTags(merge, bend_notes)
        raise NotImplemented

    def remove_alignment(self):
        """Removes the alignment from this drawing view."""
        # return self._instance.RemoveAlignment
        raise NotImplemented

    def replace_view_with_block(self, insertion_point):
        """
        Converts this view into a sketch block with the specified manipulator location.
        :param insertion_point: IMathPoint in this view where the manipulator of the new sketch block is located
        """
        # return self._instance.ReplaceViewWithBlock(insertion_point)
        raise NotImplemented

    def replace_view_with_sketch(self):
        """Converts this view into a sketch."""
        # return self._instance.ReplaceViewWithSketch
        raise NotImplemented

    def reset_sketch_visibility(self):
        """Resets the visibility of the sketches in the drawing view so that the drawing view reflects the model."""
        # return self._instance.ResetSketchVisibility
        raise NotImplemented

    def select_entity(self, entity, append_flag):
        """
        Selects an entity in this drawing view.
        :param entity: Entity
        :param append_flag: True appends the entity to the selection list, false replaces the selection list with the entity
        """
        # return self._instance.SelectEntity(entity, append_flag)
        raise NotImplemented

    def set_bend_note_text_format(self, format):
        """
        Sets the text format of all bend notes in this drawing view of a sheet metal part.
        :param format: Format in which to display all bend notes in this drawing view of a sheet metal part (see Remarks)
        """
        # return self._instance.SetBendNoteTextFormat(format)
        raise NotImplemented

    def set_display_mode(self, use_parent, mode, faceted, edges, c_thread_high_quality):
        """
        Sets the display mode of this drawing view.
        :param use_parent: True to use the parent's settings, false to use this drawing view's local settings (see Remarks)
        :param mode: Display mode of the drawing view as defined in swDisplayMode_e (see Remarks)
        :param faceted: True for draft quality, false for precision quality (see Remarks)
        :param edges: True if edges are displayed when this view is in shaded mode, false if not
        :param c_thread_high_quality: True for precision quality cosmetic threads, false for draft quality
        """
        # return self._instance.SetDisplayMode4(use_parent, mode, faceted, edges, c_thread_high_quality)
        raise NotImplemented

    def set_display_tangent_edges(self, display_in):
        """
        Sets the tangent edge display mode of the drawing view.
        :param display_in: Tangent edge display mode as defined in swDisplayTangentEdges_e
        """
        # return self._instance.SetDisplayTangentEdges2(display_in)
        raise NotImplemented

    def set_keep_linked_to_b_o_m(self, linked, name):
        """
        Sets whether this drawing view is linked to the specified BOM or weldment cut-list table.
        :param linked: True to set a drawing view to the specified BOM or weldment cut-list table, false to not
        :param name: Name of the BOM or weldment cut-list table to which to link this drawing view
        """
        # return self._instance.SetKeepLinkedToBOM(linked, name)
        raise NotImplemented

    def set_lightweight_to_resolved(self):
        """Changes the drawing view from lightweight to resolved."""
        # return self._instance.SetLightweightToResolved
        raise NotImplemented

    def set_mirror_view_orientation(self, b_set_is_mirror_view, b_mirror_vieworientation):
        """
        Sets whether to mirror this view.
        :param b_set_is_mirror_view: True to mirror the view, false to not
        :param b_mirror_vieworientation: Orientation of the mirror view as defined in swMirrorViewPositions_e
        """
        # return self._instance.SetMirrorViewOrientation(b_set_is_mirror_view, b_mirror_vieworientation)
        raise NotImplemented

    def set_name(self, name):
        """
        Sets the name of this drawing view, as displayed in the FeatureManager design tree.
        :param name: Name of drawing view
        """
        # return self._instance.SetName2(name)
        raise NotImplemented

    def set_resolved_to_lightweight(self):
        """Changes the drawing view from resolved to lightweight."""
        # return self._instance.SetResolvedToLightweight
        raise NotImplemented

    def set_visible(self, visible, dependents_too):
        """
        Sets the visibility of this drawing view.
        :param visible: True to set the view to visible, false to not
        :param dependents_too: True to set the dependents of this view to visible, false to not
        """
        # return self._instance.SetVisible(visible, dependents_too)
        raise NotImplemented

    def set_xform(self, transform):
        """
        Sets the matrix used for display of this drawing view.
        :param transform: Array of 3 doubles (see Remarks)
        """
        # return self._instance.SetXform(transform)
        raise NotImplemented

    def show_exploded(self, show_it):
        """
        Shows an exploded assembly in this drawing view.
        :param show_it: True if you want this drawing view to display the exploded state of the current assembly configuration, false if you want this drawing view to display the collapsed state
        """
        # return self._instance.ShowExploded(show_it)
        raise NotImplemented

    def show_model_break_state(self, show_it, break_name):
        """
        Sets whether to display the specified Model Break View.
        :param show_it: True to display the Model Break View specified in BreakName, false to not
        :param break_name: Name of Model Break View to display
        """
        # return self._instance.ShowModelBreakState(show_it, break_name)
        raise NotImplemented

    def update_view_display_geometry(self):
        """Updates the displayed geometry for a drawing view."""
        # return self._instance.UpdateViewDisplayGeometry
        raise NotImplemented

    def use_default_alignment(self):
        """Restores the default alignment for this drawing view."""
        # return self._instance.UseDefaultAlignment
        raise NotImplemented
