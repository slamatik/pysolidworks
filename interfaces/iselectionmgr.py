# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.html
class ISelectionMgr:
    def __init__(self, parent=None):
        self._instance = parent

    def enable_contour_selection(self):
        """Enables and disables contour selection."""
        # return self._instance.EnableContourSelection
        raise NotImplemented

    def enable_selection(self):
        """Enables or disables selection."""
        # return self._instance.EnableSelection
        raise NotImplemented

    def selection_color(self, mark):
        """
        Gets or sets the selection color.
        :param mark: Mark value (see Remarks)
        """
        # return self._instance.SelectionColor(mark)
        raise NotImplemented

    def add_selection_list_object(self, object, select_data):
        """
        Adds the specified object to the selection list.
        :param object: Object to add to the selection list (see Remarks)
        :param select_data: ISelectData
        """
        # return self._instance.AddSelectionListObject(object, select_data)
        raise NotImplemented

    def add_selection_list_objects(self, objects, select_data):
        """
        Adds the specified objects to the selection list.
        :param objects: Array of objects to add to the selection list (see Remarks)
        :param select_data: ISelectData
        """
        # return self._instance.AddSelectionListObjects(objects, select_data)
        raise NotImplemented

    def clear_selection_colors(self):
        """Clears all of selection color settings."""
        # return self._instance.ClearSelectionColors
        raise NotImplemented

    def create_callout(self, number_of_rows, lp_handler):
        """
        Creates a callout for the selection.
        :param number_of_rows: Number of rows in the callout
        :param lp_handler: Pointer to the event handler for the callout (ISwCalloutHandler)
        """
        # return self._instance.CreateCallout2(number_of_rows, lp_handler)
        raise NotImplemented

    def create_select_data(self):
        """Creates a ISelectData object to use as argument with Select methods."""
        # return self._instance.CreateSelectData
        raise NotImplemented

    def de_select(self, at_index, mark):
        """
        Deselects the specified entity.
        :param at_index: Index position within the current list of selected items where index ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.DeSelect2(at_index, mark)
        raise NotImplemented

    def get_pre_selected_object(self):
        """Gets the preselected object when the preselection notify event is fired."""
        # return self._instance.GetPreSelectedObject
        raise NotImplemented

    def get_select_by_id_specification(self, object, select_by_string, object_type, type):
        """
        Gets the selection specification for the specified object.
        :param object: Object for which to get the selection specification
        :param select_by_string: Feature name of Object; "" if Object is not a feature
        :param object_type: Type of Object
        :param type: Type of Object as defined in swSelectType_e
        """
        # return self._instance.GetSelectByIdSpecification(object, select_by_string, object_type, type)
        raise NotImplemented

    def get_selected_object(self, index, mark):
        """
        Gets the selected object.
        :param index: Index position within the current list of selected items, where Index ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks
        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.GetSelectedObject6(index, mark)
        raise NotImplemented

    def get_selected_object_count(self, mark):
        """
        Gets the number of selected objects.
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.GetSelectedObjectCount2(mark)
        raise NotImplemented

    def get_selected_object_loop(self, index, mark):
        """
        Gets the loop, if selected, for the selected edge.
        :param index: Index position within the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.GetSelectedObjectLoop2(index, mark)
        raise NotImplemented

    def get_selected_object_mark(self, at_index):
        """
        Gets the value of the mark for the specified selection.
        :param at_index: Index position within the current list of selected items where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2
        """
        # return self._instance.GetSelectedObjectMark(at_index)
        raise NotImplemented

    def get_selected_objects_component(self, index, mark):
        """
        Gets the selected component in an assembly or drawing.
        :param index: Index position within the current list of selected items, where the index ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = Only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.GetSelectedObjectsComponent4(index, mark)
        raise NotImplemented

    def get_selected_objects_drawing_view(self, index, mark):
        """
        Gets the drawing view for the selected object.
        :param index: Index position with in the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.GetSelectedObjectsDrawingView2(index, mark)
        raise NotImplemented

    def get_selected_objects_face(self, at_index, mark):
        """
        Gets the face of the specified selection if the specified selection is a silhouette edge.
        :param at_index: Index position within the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2
        :param mark:
        1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.GetSelectedObjectsFace(at_index, mark)
        raise NotImplemented

    def get_selected_object_type(self, index, mark):
        """
        Gets the type of object selected.
        :param index: Index position with in the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.GetSelectedObjectType3(index, mark)
        raise NotImplemented

    def get_selection_point(self, index, mark):
        """
        Gets the selected point in model space coordinates from the currently selected object.
        :param index: Index position with in the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.GetSelectionPoint2(index, mark)
        raise NotImplemented

    def get_selection_point_in_sketch_space(self, index, mark):
        """
        Gets the selection point projected on to the active sketch and returned in sketch space.
        :param index: Index position with in the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks
        0 = only the selections without marks
        Any other value that was used to mark and select an object
        """
        # return self._instance.GetSelectionPointInSketchSpace2(index, mark)
        raise NotImplemented

    def get_selection_specification(self, index, select_by_string, object_type, type, x, y, z):
        """
        Gets the selection specification at the specified index of the current selection list.
        :param index: 1 <= Index in the current list of selected items <= ISelectionMgr::GetSelectedObjectCount2
        :param select_by_string: Feature name of object at Index; "" if object is not a feature
        :param object_type: Type of object at Index
        :param type: Type of object at Index as defined in swSelectType_e
        :param x: X coordinate of object at Index; 0 if SelectByString is not ""
        :param y: Y coordinate of object at Index; 0 if SelectByString is not ""
        :param z: Z coordinate of object at Index; 0 if SelectByString is not ""
        """
        # return self._instance.GetSelectionSpecification(index, select_by_string, object_type, type, x, y, z)
        raise NotImplemented

    def i_de_select(self, count, at_index, mark):
        """
        Deselects the specified entity.
        :param count: Number of objects to deselect
        :param at_index: Index position within the current list of selected items where index ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.IDeSelect2(count, at_index, mark)
        raise NotImplemented

    def i_get_selection_point(self, index, mark):
        """
        Gets the selected point in model space coordinates from the currently selected object.
        :param index: Index position with in the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.IGetSelectionPoint2(index, mark)
        raise NotImplemented

    def i_get_selection_point_in_sketch_space(self, index, mark):
        """
        Gets the selection point projected on to the active sketch and returned in sketch space.
        :param index: Index position with in the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks
        0 = only the selections without marks
        Any other value that was used to mark and select an object
        """
        # return self._instance.IGetSelectionPointInSketchSpace2(index, mark)
        raise NotImplemented

    def is_in_edit_target(self, index, mark):
        """
        Gets whether the selected object is in the edit target.
        :param index: Index position with in the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        """
        # return self._instance.IsInEditTarget2(index, mark)
        raise NotImplemented

    def resume_selection_list(self, append):
        """
        Reinstates the previously suspended selection list.
        :param append: True to append the new selection list to the suspended selection list and resume the combined
        selection list, false to just resume the suspended selection list
        """
        # return self._instance.ResumeSelectionList2(append)
        raise NotImplemented

    def set_callout(self, index, p_callout):
        """
        Adds a callout to the currently selected object.
        :param index: Index number of the selected object
        :param p_callout: Callout (see Remarks)
        """
        # return self._instance.SetCallout(index, p_callout)
        raise NotImplemented

    def set_selected_object_mark(self, at_index, mark, action):
        """
        Sets the mark value for the specified selection.
        :param at_index: 1 <= Index position within the current list of selected items <= ISelectionMgr::GetSelectedObjectCount2
        :param mark: Number to use as a mark for the selected item; this number is used by certain API functions that
        require ordered entity selection
        :param action: Action to take as defined in swSelectionMarkAction_e
        """
        # return self._instance.SetSelectedObjectMark(at_index, mark, action)
        raise NotImplemented

    def set_selection_point(self, index, mark, x, y, z):
        """
        Sets the selection point in model space.
        :param index: Index position with in the current list of selected items, where AtIndex ranges from 1 to
        ISelectionMgr::GetSelectedObjectCount2 (see Remarks)
        :param mark:
        -1 = All selections regardless of marks

        0 = only the selections without marks

        Any other value = Value that was used to mark and select an object
        :param x: x coordinate of the selection point
        :param y: y coordinate of the selection point
        :param z: z coordinate of the selection point
        """
        # return self._instance.SetSelectionPoint2(index, mark, x, y, z)
        raise NotImplemented

    def suspend_selection_list(self):
        """Suspends the current selection list."""
        # return self._instance.SuspendSelectionList
        raise NotImplemented
