# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html
class IDragOperator:
	def __init__(self, parent=None):
		self._instance = parent

	def apply_to_this_configuration(self):
		"""Gets or sets the configurations to which to apply the movement of the components."""
		# return self._instance.ApplyToThisConfiguration
		raise NotImplemented

	def clearance(self, n_index):
		"""
		Gets the clearance distance between the components.
		:param n_index: Index of the components
		"""
		# return self._instance.Clearance(n_index)
		raise NotImplemented

	def collision_detection_enabled(self):
		"""Gets or sets the collision detection setting."""
		# return self._instance.CollisionDetectionEnabled
		raise NotImplemented

	def drag_corrected(self):
		"""Gets whether or not the drag operation was corrected."""
		# return self._instance.DragCorrected
		raise NotImplemented

	def drag_mode(self):
		"""Gets or sets the drag mode for this drag operation."""
		# return self._instance.DragMode
		raise NotImplemented

	def dynamic_clearance_enabled(self):
		"""Gets or sets the dynamic clearance setting."""
		# return self._instance.DynamicClearanceEnabled
		raise NotImplemented

	def graphics_redraw_enabled(self):
		"""Gets or sets whether or not to update the graphics display after moving components."""
		# return self._instance.GraphicsRedrawEnabled
		raise NotImplemented

	def hear_clashes(self):
		"""Gets or sets whether sound is associated with entity clashes."""
		# return self._instance.HearClashes
		raise NotImplemented

	def highlight_clashes(self):
		"""Gets or sets whether to highlight clashes."""
		# return self._instance.HighlightClashes
		raise NotImplemented

	def ignore_complex_surfaces(self):
		"""Gets or sets whether complex surfaces are ignored."""
		# return self._instance.IgnoreComplexSurfaces
		raise NotImplemented

	def is_drag_by_ray(self):
		"""Gets or sets the drag-by-ray setting."""
		# return self._instance.IsDragByRay
		raise NotImplemented

	def is_drag_specific(self):
		"""Gets or sets the drag-specific setting."""
		# return self._instance.IsDragSpecific
		raise NotImplemented

	def is_relaxation_eval(self):
		"""Gets or sets the relaxation evaluation."""
		# return self._instance.IsRelaxationEval
		raise NotImplemented

	def smart_mating(self):
		"""Gets or sets SmartMates."""
		# return self._instance.SmartMating
		raise NotImplemented

	def transform_type(self):
		"""Gets or sets the type of transformation."""
		# return self._instance.TransformType
		raise NotImplemented

	def use_absolute_transform(self):
		"""Gets or sets whether the transforms to use with IDragOperator::Drag or IDragOperator::IDrag are absolute or relative."""
		# return self._instance.UseAbsoluteTransform
		raise NotImplemented

	def add_component(self, p_disp, append_flag):
		"""
		Adds a component to the list of components to drag.
		:param p_disp: Component to add to the list
		:param append_flag: True to append the component to the list, false to clear the list before adding the component
		"""
		# return self._instance.AddComponent(p_disp, append_flag)
		raise NotImplemented

	def add_dynamic_clearance(self, comp1, comp2, value, append_flag, show_dim):
		"""
		Adds a dynamic clearance detector.
		:param comp1: First component of the clearance pair
		:param comp2: Second component of the clearance pair
		:param value: Minimum clearance distance
		:param append_flag: True appends the component to the list, false overwrites the list
		:param show_dim: True displays a dynamic reference dimension of the minimum clearance distance
		"""
		# return self._instance.AddDynamicClearance(comp1, comp2, value, append_flag, show_dim)
		raise NotImplemented

	def begin_drag(self):
		"""Initiates the drag operation."""
		# return self._instance.BeginDrag
		raise NotImplemented

	def collision_detection(self, entity_array, part_only, stop_at):
		"""
		Sets the collision detection parameters.
		:param entity_array: Array of components for collision detection
		:param part_only: True checks for collisions with only the components that you selected to move, false check for collisions in all affected components
		:param stop_at: True stops the motion of the component when it touches any other entity, false does not
		"""
		# return self._instance.CollisionDetection(entity_array, part_only, stop_at)
		raise NotImplemented

	def drag(self, p_xform):
		"""
		Sets the transform matrix for this drag operation.
		:param p_xform: Math transform that specifies the desired motion for this step
		"""
		# return self._instance.Drag(p_xform)
		raise NotImplemented

	def drag_as_u_i(self, p_xform):
		"""
		Sets the transform matrix for this drag operation.
		:param p_xform: Pointer to IMathTransform that specifies the desired motion for this step
		"""
		# return self._instance.DragAsUI(p_xform)
		raise NotImplemented

	def end_drag(self):
		"""Terminates the drag operation."""
		# return self._instance.EndDrag
		raise NotImplemented

	def get_drag_point(self, point):
		"""
		Gets the drag point.
		:param point: Array containing the X, Y, Z coordinates of the drag point
		"""
		# return self._instance.GetDragPoint(point)
		raise NotImplemented

	def i_add_component(self, p_comp, append_flag):
		"""
		Adds a component to the list of components to drag.
		:param p_comp: Component to add to the list
		:param append_flag: True to append the component to the list, false to clear the list before adding the component
		"""
		# return self._instance.IAddComponent(p_comp, append_flag)
		raise NotImplemented

	def i_add_dynamic_clearance(self, comp1, comp2, value, append_flag, show_dim):
		"""
		Adds a dynamic clearance detector.
		:param comp1: First component of the clearance pair
		:param comp2: Second component of the clearance pair
		:param value: Minimum clearance distance
		:param append_flag: True appends the component to the list, false overwrites the list
		:param show_dim: True displays a dynamic reference dimension of the minimum clearance distance
		"""
		# return self._instance.IAddDynamicClearance(comp1, comp2, value, append_flag, show_dim)
		raise NotImplemented

	def i_collision_detection(self, count, component_array, part_only, stop_at):
		"""
		Sets the collision detection parameters.
		:param count: Number of components for collision detection
		:param component_array: Array of components for collision detection
		:param part_only: True checks for collisions with only the components that you selected to move, false check for collisions in all affected components
		:param stop_at: True stops the motion of the component when it touches any other entity, false does not
		"""
		# return self._instance.ICollisionDetection(count, component_array, part_only, stop_at)
		raise NotImplemented

	def i_drag(self, p_xform):
		"""
		Sets the transform matrix for this drag operation.
		:param p_xform: Pointer to an IMathTransform that specifies the desired motion for this step
		"""
		# return self._instance.IDrag(p_xform)
		raise NotImplemented

	def i_get_drag_point(self, point):
		"""
		Gets the drag point.
		:param point: Array containing the X, Y, Z coordinates of the drag point
		"""
		# return self._instance.IGetDragPoint(point)
		raise NotImplemented

	def i_set_drag_point(self, point):
		"""
		Sets the drag point.
		:param point: Array containing the X, Y, Z coordinate of the drag point
		"""
		# return self._instance.ISetDragPoint(point)
		raise NotImplemented

	def set_drag_point(self, point):
		"""
		Sets the drag point.
		:param point: Array of size 3 containing the X, Y, Z coordinate of the drag point
		"""
		# return self._instance.SetDragPoint(point)
		raise NotImplemented

