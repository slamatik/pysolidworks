# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html
class ISketch:
    def __init__(self, system_object=None):
        self._instance = system_object

    def model_to_sketch_transform(self):
        """Gets the model-to-sketch transform for this sketch.
        NOTE: This property is a get-only property. Set is not implemented."""
        # return self._instance.ModelToSketchTransform
        raise NotImplemented

    def relation_manager(self):
        """Gets the sketch relation manager.
        NOTE: This property is a get-only property. Set is not implemented."""
        # return self._instance.RelationManager
        raise NotImplemented

    def check_feature_use(self, feature_type, open_count, closed_count):
        """
        Checks to see if this sketch is valid for use in creating a specified feature.
        :param feature_type: Determine if this type of feature can be created as defined in swSketchCheckFeatureProfileUsage_e
        :param open_count: Number of open contours found in this sketch
        :param closed_count: Number of closed contours found in this sketch
        """
        # return self._instance.CheckFeatureUse(feature_type, open_count, closed_count)
        raise NotImplemented

    def constrain_all(self):
        """Attempts to solve all of the apparent relations in the sketch and returns the number of constraints that were
        added to the sketch."""
        # return self._instance.ConstrainAll
        raise NotImplemented

    def get_arc_count(self):
        """Gets the number of arcs in the sketch."""
        # return self._instance.GetArcCount
        raise NotImplemented

    def get_arcs(self):
        """Gets all of the arcs in the sketch."""
        # return self._instance.GetArcs2
        raise NotImplemented

    def get_automatic_solve(self):
        """Checks whether the computation to solve the sketch geometry of the part as modifications are automatically
        performed."""
        # return self._instance.GetAutomaticSolve
        raise NotImplemented

    def get_constrained_status(self):
        """Gets the current constrained status of the sketch."""
        # return self._instance.GetConstrainedStatus
        raise NotImplemented

    def get_contour_edge_count(self):
        """Gets the number of edges for this sketch contour."""
        # return self._instance.GetContourEdgeCount
        raise NotImplemented

    def get_contour_edges(self, xform):
        """
        Gets the edges for a sketch that has one contour.
        :param xform: Array of size 16 doubles representing the transform
        """
        # return self._instance.GetContourEdges(xform)
        raise NotImplemented

    def get_detach_segment_on_drag(self):
        """Gets the Detach Segment on Drag setting."""
        # return self._instance.GetDetachSegmentOnDrag
        raise NotImplemented

    def get_ellipse_count(self):
        """Gets the number of ellipses in the sketch."""
        # return self._instance.GetEllipseCount
        raise NotImplemented

    def get_ellipses(self):
        """Gets all of the ellipses in the sketch."""
        # return self._instance.GetEllipses3
        raise NotImplemented

    def get_line_count(self, cross_hatch_option):
        """
        Gets the number of lines in the sketch with an option to exclude or include crosshatch lines.
        :param cross_hatch_option: Crosshatch option as defined in swCrossHatchFilter_e
        """
        # return self._instance.GetLineCount2(cross_hatch_option)
        raise NotImplemented

    def get_lines(self, cross_hatch_option):
        """
        Gets all of the lines in the sketch with an option to include or exclude crosshatch lines.
        :param cross_hatch_option: Crosshatch option as defined in swCrossHatchFilter_e
        """
        # return self._instance.GetLines2(cross_hatch_option)
        raise NotImplemented

    def get_parabola_count(self):
        """Gets the number of parabolas in the sketch."""
        # return self._instance.GetParabolaCount
        raise NotImplemented

    def get_parabolas(self):
        """Gets all of the parabolas in the sketch."""
        # return self._instance.GetParabolas2
        raise NotImplemented

    def get_poly_line_count(self, point_count):
        """
        Not implemented.
        :param point_count: �
        """
        # return self._instance.GetPolyLineCount(point_count)
        raise NotImplemented

    def get_polylines(self):
        """Not implemented."""
        # return self._instance.GetPolylines
        raise NotImplemented

    def get_reference_entity(self, l_entity_type):
        """
        Gets the entity on which this sketch was created.
        :param l_entity_type: Entity type as defined in swSelectType_e (only swSelFACES and swSelDATUMPLANES are valid
        values for this method)
        """
        # return self._instance.GetReferenceEntity(l_entity_type)
        raise NotImplemented

    def get_sketch_block_instance_count(self):
        """Gets the number of block instances in this sketch (i.e., the sketch under which the block instances are
        displayed in the FeatureManager design tree)."""
        # return self._instance.GetSketchBlockInstanceCount
        raise NotImplemented

    def get_sketch_block_instances(self):
        """Gets the block instances in this sketch (i.e., the sketch under which the block instances are displayed in
        the FeatureManager design tree)."""
        # return self._instance.GetSketchBlockInstances
        raise NotImplemented

    def get_sketch_contour_count(self):
        """Gets the number of sketch contours in this sketch."""
        # return self._instance.GetSketchContourCount
        raise NotImplemented

    def get_sketch_contours(self):
        """Gets the sketch contours in this sketch."""
        # return self._instance.GetSketchContours
        raise NotImplemented

    def get_sketch_hatches(self):
        """Gets an array of sketch hatches that exist in this sketch."""
        # return self._instance.GetSketchHatches
        raise NotImplemented

    def get_sketch_path_count(self):
        """Gets the number of sketch paths in this sketch."""
        # return self._instance.GetSketchPathCount
        raise NotImplemented

    def get_sketch_paths(self):
        """Gets the sketch paths in this sketch."""
        # return self._instance.GetSketchPaths
        raise NotImplemented

    def get_sketch_picture_count(self):
        """Gets the number of pictures on this sketch."""
        # return self._instance.GetSketchPictureCount
        raise NotImplemented

    def get_sketch_pictures(self):
        """Gets the pictures on this sketch."""
        # return self._instance.GetSketchPictures
        raise NotImplemented

    def get_sketch_points(self):
        """Gets the sketch points in this sketch."""
        # return self._instance.GetSketchPoints2
        raise NotImplemented

    def get_sketch_points_count(self):
        """Gets the number of sketch points in this sketch."""
        # return self._instance.GetSketchPointsCount2
        raise NotImplemented

    def get_sketch_region_count(self):
        """Gets the number of sketch regions in this sketch."""
        # return self._instance.GetSketchRegionCount
        raise NotImplemented

    def get_sketch_regions(self):
        """Gets the sketch regions in this sketch."""
        # return self._instance.GetSketchRegions
        raise NotImplemented

    def get_sketch_segments(self):
        """Gets the sketch segments in this sketch, which include line, arc, spline, parabola, and ellipse entities."""
        # return self._instance.GetSketchSegments
        raise NotImplemented

    def get_sketch_slot_count(self):
        """Gets the number of sketch slots in this sketch."""
        # return self._instance.GetSketchSlotCount
        raise NotImplemented

    def get_sketch_slots(self):
        """Gets the sketch slots in this sketch."""
        # return self._instance.GetSketchSlots
        raise NotImplemented

    def get_sketch_text_segments(self):
        """Gets the sketch segments that represent the selected text in the sketch."""
        # return self._instance.GetSketchTextSegments
        raise NotImplemented

    def get_spline_count(self, point_count):
        """
        Gets the number of splines in this sketch.
        :param point_count: Number of points in this sketch
        """
        # return self._instance.GetSplineCount(point_count)
        raise NotImplemented

    def get_spline_interpolate_count(self, point_count):
        """
        Gets the number of points in the spline and number of splines in the sketch.
        :param point_count: Number of points in this sketch
        """
        # return self._instance.GetSplineInterpolateCount(point_count)
        raise NotImplemented

    def get_spline_params(self, force_non_periodic, index):
        """
        Gets the parameterization data of the specified spline in this sketch.
        :param force_non_periodic: True to attempt to convert a non-periodic�spline�to a periodic one, false to not
        :param index: 0-based index indicating the spline whose parameterization data to get
        """
        # return self._instance.GetSplineParams5(force_non_periodic, index)
        raise NotImplemented

    def get_spline_params_count(self, force_non_periodic, size):
        """
        Gets the number of splines in the sketch and the size of array required to hold the data for them.
        :param force_non_periodic: True to attempt to convert all non-periodic�splines�to periodic, false to not
        :param size: Size of array required for a call to�ISketch::IGetSplineParams3
        """
        # return self._instance.GetSplineParamsCount3(force_non_periodic, size)
        raise NotImplemented

    def get_splines(self):
        """Gets information for each spline by tessellation instead of by interpolation as is done by
        ISketch::GetSplinesInterpolate and ISketch::IGetSplinesInterpolate."""
        # return self._instance.GetSplines
        raise NotImplemented

    def get_splines_interpolate(self):
        """Gets the spline points by interpolation instead of by tessellation as is done by
        ISketch::GetSplines and ISketch::IGetSplines."""
        # return self._instance.GetSplinesInterpolate
        raise NotImplemented

    def get_user_points(self):
        """Gets all of the user points in this sketch."""
        # return self._instance.GetUserPoints2
        raise NotImplemented

    def get_user_points_count(self):
        """Gets the number of user points in the sketch."""
        # return self._instance.GetUserPointsCount
        raise NotImplemented

    def i_enum_sketch_hatches(self):
        """Gets the sketch hatches enumeration in this sketch."""
        # return self._instance.IEnumSketchHatches
        raise NotImplemented

    def i_enum_sketch_points(self):
        """Gets the sketch points enumeration in this sketch."""
        # return self._instance.IEnumSketchPoints
        raise NotImplemented

    def i_enum_sketch_segments(self):
        """Gets the sketch segments enumeration in this sketch."""
        # return self._instance.IEnumSketchSegments
        raise NotImplemented

    def i_enum_sketch_text_segments(self):
        """Gets the sketch segments enumeration for the selected text in this sketch."""
        # return self._instance.IEnumSketchTextSegments
        raise NotImplemented

    def i_get_arcs(self, array_size):
        """
        Gets all of the arcs in the sketch.
        :param array_size: Number of arcs in the sketch
        """
        # return self._instance.IGetArcs2(array_size)
        raise NotImplemented

    def i_get_contour_edges(self, xform, edge_count):
        """
        Gets the edges for a sketch that has one contour.
        :param xform: Sketch entities, edges
        :param edge_count: Number of edges
        """
        # return self._instance.IGetContourEdges(xform, edge_count)
        raise NotImplemented

    def i_get_ellipses(self, array_size):
        """
        Gets all of the ellipses in the sketch.
        :param array_size: Number of ellipses in the sketch
        """
        # return self._instance.IGetEllipses3(array_size)
        raise NotImplemented

    def i_get_lines(self, cross_hatch_option, array_size):
        """
        Gets all of the lines in the sketch with an option to include or exclude crosshatch lines.
        :param cross_hatch_option: Crosshatch option as defined in swCrossHatchFilter_e
        :param array_size: Number of lines in the sketch
        """
        # return self._instance.IGetLines2(cross_hatch_option, array_size)
        raise NotImplemented

    def i_get_parabolas(self, array_size):
        """
        Gets all of the parabolas in the sketch.
        :param array_size: Number of parabolas in the sketch
        """
        # return self._instance.IGetParabolas2(array_size)
        raise NotImplemented

    def i_get_polylines(self):
        """Not implemented."""
        # return self._instance.IGetPolylines
        raise NotImplemented

    def i_get_sketch_block_instances(self, count):
        """
        Gets the block instances in this sketch (i.e., the sketch under which the block instances are displayed in the
        FeatureManager design tree).
        :param count: Number of block instances in this sketch
        """
        # return self._instance.IGetSketchBlockInstances(count)
        raise NotImplemented

    def i_get_sketch_contours(self, count):
        """
        Gets the sketch contours in this sketch.
        :param count: Number of sketch contours
        """
        # return self._instance.IGetSketchContours(count)
        raise NotImplemented

    def i_get_sketch_paths(self, count):
        """
        Gets the sketch paths in this sketch.
        :param count: Number of sketch paths
        """
        # return self._instance.IGetSketchPaths(count)
        raise NotImplemented

    def i_get_sketch_pictures(self, count):
        """
        Gets the pictures on this sketch.
        :param count: Number of pictures on this sketch
        """
        # return self._instance.IGetSketchPictures(count)
        raise NotImplemented

    def i_get_sketch_points(self, count):
        """
        Gets the sketch points in this sketch.
        :param count: Number of sketch points in this sketch
        """
        # return self._instance.IGetSketchPoints2(count)
        raise NotImplemented

    def i_get_sketch_regions(self, count):
        """
        Gets the sketch regions in this sketch.
        :param count: Number of sketch regions
        """
        # return self._instance.IGetSketchRegions(count)
        raise NotImplemented

    def i_get_sketch_slots(self, count):
        """
        Gets the sketch slots in this sketch.
        :param count: Number of sketch slots in this sketch
        """
        # return self._instance.IGetSketchSlots(count)
        raise NotImplemented

    def i_get_splines(self):
        """Gets information for each spline by tessellation instead of by interpolation as is done by
        ISketch::GetSplinesInterpolate and ISketch::IGetSplinesInterpolate."""
        # return self._instance.IGetSplines
        raise NotImplemented

    def i_get_splines_interpolate(self):
        """Gets the spline points by interpolation instead of by tessellation as is done by ISketch::GetSplines and
        ISketch::IGetSplines."""
        # return self._instance.IGetSplinesInterpolate
        raise NotImplemented

    def i_get_user_points(self, array_size):
        """
        Gets all of the user points in this sketch.
        :param array_size: Number of user points in the sketch
        """
        # return self._instance.IGetUserPoints2(array_size)
        raise NotImplemented

    def insert_route_line(self, items_to_connect, reverse, alternate_path, along_x_y_z):
        """
        Inserts a route line in an explode line sketch or a 3D sketch to indicate component relationships.
        :param items_to_connect: Array of faces, edges,�and vertices to which to�connect the route line
        :param reverse: Array of Booleans indicating whether to reverse the route line at the corresponding item to
        connect; true to reverse the direction of the route line, false to not
        :param alternate_path: Array of Booleans indicating whether to display an alternate path at the corresponding
        item to connect; true to display another possible path for the route line, false to not
        :param along_x_y_z: Array of Booleans indicating whether to create a path parallel to the X, Y, and Z directions
        from the corresponding item to connect; true to use the X, Y, and Z directions,�false�to use the shortest route
        """
        # return self._instance.InsertRouteLine(items_to_connect, reverse, alternate_path, along_x_y_z)
        raise NotImplemented

    def is_d(self):
        """Gets whether this sketch is 2D or 3D."""
        # return self._instance.Is3D
        raise NotImplemented

    def is_boundary_box_sketch(self):
        """Determines whether the sketch is a boundary box."""
        # return self._instance.IsBoundaryBoxSketch
        raise NotImplemented

    def is_derived(self):
        """Gets whether a sketch is derived."""
        # return self._instance.IsDerived
        raise NotImplemented

    def is_shared(self):
        """Gets whether this sketch is used by more than one feature."""
        # return self._instance.IsShared
        raise NotImplemented

    def is_sketch_editable(self):
        """Gets whether this sketch is editable."""
        # return self._instance.IsSketchEditable
        raise NotImplemented

    def merge_points(self, distance):
        """
        Merges sketch points within a specified distance.
        :param distance: Distance at which points are considered coincident
        """
        # return self._instance.MergePoints(distance)
        raise NotImplemented

    def set_automatic_solve(self, solve_flag):
        """
        Controls whether the computation to solve the sketch geometry of the part as modifications are automatically
        performed.
        :param solve_flag: True if solving is on, false if it is off
        """
        # return self._instance.SetAutomaticSolve(solve_flag)
        raise NotImplemented

    def set_detach_segment_on_drag(self, detach):
        """
        Sets the Detach Segment on Drag setting.
        :param detach: True to select Detach Segment on Drag, false to not
        """
        # return self._instance.SetDetachSegmentOnDrag(detach)
        raise NotImplemented

    def set_sketch_editable(self, editable):
        """
        Sets whether this sketch is editable.
        :param editable: True to make this sketch editable, false to make it read only
        """
        # return self._instance.SetSketchEditable(editable)
        raise NotImplemented

    def set_working_plane_orientation(self, origin_x, origin_y, origin_z, x_axis_x, x_axis_y, x_axis_z, y_axis_x,
                                      y_axis_y, y_axis_z, normal_x, normal_y, normal_z):
        """
        Sets the orientation for sketching geometry in a 3D sketch. It sets the planar location for new 2D and 3D
        geometry in a 3D sketch.
        :param origin_x: x coordinate of the origin of the axis
        :param origin_y: y coordinate of the origin of the axis
        :param origin_z: z coordinate of the origin of the axis
        :param x_axis_x: x coordinate of the x vector direction
        :param x_axis_y: y coordinate of the x vector direction
        :param x_axis_z: z coordinate of the x vector direction
        :param y_axis_x: x coordinate of the y vector direction
        :param y_axis_y: y coordinate of the y vector direction
        :param y_axis_z: z coordinate of the y vector direction
        :param normal_x: x coordinate of the normal to the planar direction
        :param normal_y: y coordinate of the normal to the planar direction
        :param normal_z: z coordinate of the normal to the planar direction
        """
        # return self._instance.SetWorkingPlaneOrientation(origin_x, origin_y, origin_z, x_axis_x, x_axis_y, x_axis_z,
        # y_axis_x, y_axis_y, y_axis_z, normal_x, normal_y, normal_z)
        raise NotImplemented
