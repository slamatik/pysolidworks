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

	@property
	def selection_color(self):
		"""Gets or sets the selection color."""
		return self._instance.SelectionColor

	@selection_color.setter
	def selection_color(self, value):
		"""Gets or sets the selection color."""
		self._instance.SelectionColor = value

	@property
	def add_selection_list_object(self):
		"""Adds the specified object to the selection list."""
		return self._instance.AddSelectionListObject

	@add_selection_list_object.setter
	def add_selection_list_object(self, value):
		"""Adds the specified object to the selection list."""
		self._instance.AddSelectionListObject = value

	@property
	def add_selection_list_objects(self):
		"""Adds the specified objects to the selection list."""
		return self._instance.AddSelectionListObjects

	@add_selection_list_objects.setter
	def add_selection_list_objects(self, value):
		"""Adds the specified objects to the selection list."""
		self._instance.AddSelectionListObjects = value

	@property
	def clear_selection_colors(self):
		"""Clears all of selection color settings."""
		return self._instance.ClearSelectionColors

	@clear_selection_colors.setter
	def clear_selection_colors(self, value):
		"""Clears all of selection color settings."""
		self._instance.ClearSelectionColors = value

	@property
	def create_callout(self):
		"""Creates a callout for the selection."""
		return self._instance.CreateCallout2

	@create_callout.setter
	def create_callout(self, value):
		"""Creates a callout for the selection."""
		self._instance.CreateCallout2 = value

	@property
	def create_select_data(self):
		"""Creates a ISelectData object to use as argument with Select methods."""
		return self._instance.CreateSelectData

	@create_select_data.setter
	def create_select_data(self, value):
		"""Creates a ISelectData object to use as argument with Select methods."""
		self._instance.CreateSelectData = value

	@property
	def de_select(self):
		"""Deselects the specified entity."""
		return self._instance.DeSelect2

	@de_select.setter
	def de_select(self, value):
		"""Deselects the specified entity."""
		self._instance.DeSelect2 = value

	@property
	def get_pre_selected_object(self):
		"""Gets the preselected object when the preselection notify event is fired."""
		return self._instance.GetPreSelectedObject

	@get_pre_selected_object.setter
	def get_pre_selected_object(self, value):
		"""Gets the preselected object when the preselection notify event is fired."""
		self._instance.GetPreSelectedObject = value

	@property
	def get_select_by_id_specification(self):
		"""Gets the selection specification for the specified object."""
		return self._instance.GetSelectByIdSpecification

	@get_select_by_id_specification.setter
	def get_select_by_id_specification(self, value):
		"""Gets the selection specification for the specified object."""
		self._instance.GetSelectByIdSpecification = value

	@property
	def get_selected_object(self):
		"""Gets the selected object."""
		return self._instance.GetSelectedObject6

	@get_selected_object.setter
	def get_selected_object(self, value):
		"""Gets the selected object."""
		self._instance.GetSelectedObject6 = value

	@property
	def get_selected_object_count(self):
		"""Gets the number of selected objects."""
		return self._instance.GetSelectedObjectCount2

	@get_selected_object_count.setter
	def get_selected_object_count(self, value):
		"""Gets the number of selected objects."""
		self._instance.GetSelectedObjectCount2 = value

	@property
	def get_selected_object_loop(self):
		"""Gets the loop, if selected, for the selected edge."""
		return self._instance.GetSelectedObjectLoop2

	@get_selected_object_loop.setter
	def get_selected_object_loop(self, value):
		"""Gets the loop, if selected, for the selected edge."""
		self._instance.GetSelectedObjectLoop2 = value

	@property
	def get_selected_object_mark(self):
		"""Gets the value of the mark for the specified selection."""
		return self._instance.GetSelectedObjectMark

	@get_selected_object_mark.setter
	def get_selected_object_mark(self, value):
		"""Gets the value of the mark for the specified selection."""
		self._instance.GetSelectedObjectMark = value

	@property
	def get_selected_objects_component(self):
		"""Gets the selected component in an assembly or drawing."""
		return self._instance.GetSelectedObjectsComponent4

	@get_selected_objects_component.setter
	def get_selected_objects_component(self, value):
		"""Gets the selected component in an assembly or drawing."""
		self._instance.GetSelectedObjectsComponent4 = value

	@property
	def get_selected_objects_drawing_view(self):
		"""Gets the drawing view for the selected object."""
		return self._instance.GetSelectedObjectsDrawingView2

	@get_selected_objects_drawing_view.setter
	def get_selected_objects_drawing_view(self, value):
		"""Gets the drawing view for the selected object."""
		self._instance.GetSelectedObjectsDrawingView2 = value

	@property
	def get_selected_objects_face(self):
		"""Gets the face of the specified selection if the specified selection is a silhouette edge."""
		return self._instance.GetSelectedObjectsFace

	@get_selected_objects_face.setter
	def get_selected_objects_face(self, value):
		"""Gets the face of the specified selection if the specified selection is a silhouette edge."""
		self._instance.GetSelectedObjectsFace = value

	@property
	def get_selected_object_type(self):
		"""Gets the type of object selected."""
		return self._instance.GetSelectedObjectType3

	@get_selected_object_type.setter
	def get_selected_object_type(self, value):
		"""Gets the type of object selected."""
		self._instance.GetSelectedObjectType3 = value

	@property
	def get_selection_point(self):
		"""Gets the selected point in model space coordinates from the currently selected object."""
		return self._instance.GetSelectionPoint2

	@get_selection_point.setter
	def get_selection_point(self, value):
		"""Gets the selected point in model space coordinates from the currently selected object."""
		self._instance.GetSelectionPoint2 = value

	@property
	def get_selection_point_in_sketch_space(self):
		"""Gets the selection point projected on to the active sketch and returned in sketch space."""
		return self._instance.GetSelectionPointInSketchSpace2

	@get_selection_point_in_sketch_space.setter
	def get_selection_point_in_sketch_space(self, value):
		"""Gets the selection point projected on to the active sketch and returned in sketch space."""
		self._instance.GetSelectionPointInSketchSpace2 = value

	@property
	def get_selection_specification(self):
		"""Gets the selection specification at the specified index of the current selection list."""
		return self._instance.GetSelectionSpecification

	@get_selection_specification.setter
	def get_selection_specification(self, value):
		"""Gets the selection specification at the specified index of the current selection list."""
		self._instance.GetSelectionSpecification = value

	@property
	def i_de_select(self):
		"""Deselects the specified entity."""
		return self._instance.IDeSelect2

	@i_de_select.setter
	def i_de_select(self, value):
		"""Deselects the specified entity."""
		self._instance.IDeSelect2 = value

	@property
	def i_get_selection_point(self):
		"""Gets the selected point in model space coordinates from the currently selected object."""
		return self._instance.IGetSelectionPoint2

	@i_get_selection_point.setter
	def i_get_selection_point(self, value):
		"""Gets the selected point in model space coordinates from the currently selected object."""
		self._instance.IGetSelectionPoint2 = value

	@property
	def i_get_selection_point_in_sketch_space(self):
		"""Gets the selection point projected on to the active sketch and returned in sketch space."""
		return self._instance.IGetSelectionPointInSketchSpace2

	@i_get_selection_point_in_sketch_space.setter
	def i_get_selection_point_in_sketch_space(self, value):
		"""Gets the selection point projected on to the active sketch and returned in sketch space."""
		self._instance.IGetSelectionPointInSketchSpace2 = value

	@property
	def is_in_edit_target(self):
		"""Gets whether the selected object is in the edit target."""
		return self._instance.IsInEditTarget2

	@is_in_edit_target.setter
	def is_in_edit_target(self, value):
		"""Gets whether the selected object is in the edit target."""
		self._instance.IsInEditTarget2 = value

	@property
	def resume_selection_list(self):
		"""Reinstates the previously suspended selection list."""
		return self._instance.ResumeSelectionList2

	@resume_selection_list.setter
	def resume_selection_list(self, value):
		"""Reinstates the previously suspended selection list."""
		self._instance.ResumeSelectionList2 = value

	@property
	def set_callout(self):
		"""Adds a callout to the currently selected object."""
		return self._instance.SetCallout

	@set_callout.setter
	def set_callout(self, value):
		"""Adds a callout to the currently selected object."""
		self._instance.SetCallout = value

	@property
	def set_selected_object_mark(self):
		"""Sets the mark value for the specified selection."""
		return self._instance.SetSelectedObjectMark

	@set_selected_object_mark.setter
	def set_selected_object_mark(self, value):
		"""Sets the mark value for the specified selection."""
		self._instance.SetSelectedObjectMark = value

	@property
	def set_selection_point(self):
		"""Sets the selection point in model space."""
		return self._instance.SetSelectionPoint2

	@set_selection_point.setter
	def set_selection_point(self, value):
		"""Sets the selection point in model space."""
		self._instance.SetSelectionPoint2 = value

	@property
	def suspend_selection_list(self):
		"""Suspends the current selection list."""
		return self._instance.SuspendSelectionList

	@suspend_selection_list.setter
	def suspend_selection_list(self, value):
		"""Suspends the current selection list."""
		self._instance.SuspendSelectionList = value

