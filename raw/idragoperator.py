# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html
class IDragOperator:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def apply_to_this_configuration(self):
		"""Gets or sets the configurations to which to apply the movement of the components."""
		return self._instance.ApplyToThisConfiguration

	@apply_to_this_configuration.setter
	def apply_to_this_configuration(self, value):
		"""Gets or sets the configurations to which to apply the movement of the components."""
		self._instance.ApplyToThisConfiguration = value

	@property
	def clearance(self):
		"""Gets the clearance distance between the components."""
		return self._instance.Clearance

	@clearance.setter
	def clearance(self, value):
		"""Gets the clearance distance between the components."""
		self._instance.Clearance = value

	@property
	def collision_detection_enabled(self):
		"""Gets or sets the collision detection setting."""
		return self._instance.CollisionDetectionEnabled

	@collision_detection_enabled.setter
	def collision_detection_enabled(self, value):
		"""Gets or sets the collision detection setting."""
		self._instance.CollisionDetectionEnabled = value

	@property
	def drag_corrected(self):
		"""Gets whether or not the drag operation was corrected."""
		return self._instance.DragCorrected

	@drag_corrected.setter
	def drag_corrected(self, value):
		"""Gets whether or not the drag operation was corrected."""
		self._instance.DragCorrected = value

	@property
	def drag_mode(self):
		"""Gets or sets the drag mode for this drag operation."""
		return self._instance.DragMode

	@drag_mode.setter
	def drag_mode(self, value):
		"""Gets or sets the drag mode for this drag operation."""
		self._instance.DragMode = value

	@property
	def dynamic_clearance_enabled(self):
		"""Gets or sets the dynamic clearance setting."""
		return self._instance.DynamicClearanceEnabled

	@dynamic_clearance_enabled.setter
	def dynamic_clearance_enabled(self, value):
		"""Gets or sets the dynamic clearance setting."""
		self._instance.DynamicClearanceEnabled = value

	@property
	def graphics_redraw_enabled(self):
		"""Gets or sets whether or not to update the graphics display after moving components."""
		return self._instance.GraphicsRedrawEnabled

	@graphics_redraw_enabled.setter
	def graphics_redraw_enabled(self, value):
		"""Gets or sets whether or not to update the graphics display after moving components."""
		self._instance.GraphicsRedrawEnabled = value

	@property
	def hear_clashes(self):
		"""Gets or sets whether sound is associated with entity clashes."""
		return self._instance.HearClashes

	@hear_clashes.setter
	def hear_clashes(self, value):
		"""Gets or sets whether sound is associated with entity clashes."""
		self._instance.HearClashes = value

	@property
	def highlight_clashes(self):
		"""Gets or sets whether to highlight clashes."""
		return self._instance.HighlightClashes

	@highlight_clashes.setter
	def highlight_clashes(self, value):
		"""Gets or sets whether to highlight clashes."""
		self._instance.HighlightClashes = value

	@property
	def ignore_complex_surfaces(self):
		"""Gets or sets whether complex surfaces are ignored."""
		return self._instance.IgnoreComplexSurfaces

	@ignore_complex_surfaces.setter
	def ignore_complex_surfaces(self, value):
		"""Gets or sets whether complex surfaces are ignored."""
		self._instance.IgnoreComplexSurfaces = value

	@property
	def is_drag_by_ray(self):
		"""Gets or sets the drag-by-ray setting."""
		return self._instance.IsDragByRay

	@is_drag_by_ray.setter
	def is_drag_by_ray(self, value):
		"""Gets or sets the drag-by-ray setting."""
		self._instance.IsDragByRay = value

	@property
	def is_drag_specific(self):
		"""Gets or sets the drag-specific setting."""
		return self._instance.IsDragSpecific

	@is_drag_specific.setter
	def is_drag_specific(self, value):
		"""Gets or sets the drag-specific setting."""
		self._instance.IsDragSpecific = value

	@property
	def is_relaxation_eval(self):
		"""Gets or sets the relaxation evaluation."""
		return self._instance.IsRelaxationEval

	@is_relaxation_eval.setter
	def is_relaxation_eval(self, value):
		"""Gets or sets the relaxation evaluation."""
		self._instance.IsRelaxationEval = value

	@property
	def smart_mating(self):
		"""Gets or sets SmartMates."""
		return self._instance.SmartMating

	@smart_mating.setter
	def smart_mating(self, value):
		"""Gets or sets SmartMates."""
		self._instance.SmartMating = value

	@property
	def transform_type(self):
		"""Gets or sets the type of transformation."""
		return self._instance.TransformType

	@transform_type.setter
	def transform_type(self, value):
		"""Gets or sets the type of transformation."""
		self._instance.TransformType = value

	@property
	def use_absolute_transform(self):
		"""Gets or sets whether the transforms to use with IDragOperator::Drag or IDragOperator::IDrag are absolute or relative."""
		return self._instance.UseAbsoluteTransform

	@use_absolute_transform.setter
	def use_absolute_transform(self, value):
		"""Gets or sets whether the transforms to use with IDragOperator::Drag or IDragOperator::IDrag are absolute or relative."""
		self._instance.UseAbsoluteTransform = value

	@property
	def add_component(self):
		"""Adds a component to the list of components to drag."""
		return self._instance.AddComponent

	@add_component.setter
	def add_component(self, value):
		"""Adds a component to the list of components to drag."""
		self._instance.AddComponent = value

	@property
	def add_dynamic_clearance(self):
		"""Adds a dynamic clearance detector."""
		return self._instance.AddDynamicClearance

	@add_dynamic_clearance.setter
	def add_dynamic_clearance(self, value):
		"""Adds a dynamic clearance detector."""
		self._instance.AddDynamicClearance = value

	@property
	def begin_drag(self):
		"""Initiates the drag operation."""
		return self._instance.BeginDrag

	@begin_drag.setter
	def begin_drag(self, value):
		"""Initiates the drag operation."""
		self._instance.BeginDrag = value

	@property
	def collision_detection(self):
		"""Sets the collision detection parameters."""
		return self._instance.CollisionDetection

	@collision_detection.setter
	def collision_detection(self, value):
		"""Sets the collision detection parameters."""
		self._instance.CollisionDetection = value

	@property
	def drag(self):
		"""Sets the transform matrix for this drag operation."""
		return self._instance.Drag

	@drag.setter
	def drag(self, value):
		"""Sets the transform matrix for this drag operation."""
		self._instance.Drag = value

	@property
	def drag_as_u_i(self):
		"""Sets the transform matrix for this drag operation."""
		return self._instance.DragAsUI

	@drag_as_u_i.setter
	def drag_as_u_i(self, value):
		"""Sets the transform matrix for this drag operation."""
		self._instance.DragAsUI = value

	@property
	def end_drag(self):
		"""Terminates the drag operation."""
		return self._instance.EndDrag

	@end_drag.setter
	def end_drag(self, value):
		"""Terminates the drag operation."""
		self._instance.EndDrag = value

	@property
	def get_drag_point(self):
		"""Gets the drag point."""
		return self._instance.GetDragPoint

	@get_drag_point.setter
	def get_drag_point(self, value):
		"""Gets the drag point."""
		self._instance.GetDragPoint = value

	@property
	def i_add_component(self):
		"""Adds a component to the list of components to drag."""
		return self._instance.IAddComponent

	@i_add_component.setter
	def i_add_component(self, value):
		"""Adds a component to the list of components to drag."""
		self._instance.IAddComponent = value

	@property
	def i_add_dynamic_clearance(self):
		"""Adds a dynamic clearance detector."""
		return self._instance.IAddDynamicClearance

	@i_add_dynamic_clearance.setter
	def i_add_dynamic_clearance(self, value):
		"""Adds a dynamic clearance detector."""
		self._instance.IAddDynamicClearance = value

	@property
	def i_collision_detection(self):
		"""Sets the collision detection parameters."""
		return self._instance.ICollisionDetection

	@i_collision_detection.setter
	def i_collision_detection(self, value):
		"""Sets the collision detection parameters."""
		self._instance.ICollisionDetection = value

	@property
	def i_drag(self):
		"""Sets the transform matrix for this drag operation."""
		return self._instance.IDrag

	@i_drag.setter
	def i_drag(self, value):
		"""Sets the transform matrix for this drag operation."""
		self._instance.IDrag = value

	@property
	def i_get_drag_point(self):
		"""Gets the drag point."""
		return self._instance.IGetDragPoint

	@i_get_drag_point.setter
	def i_get_drag_point(self, value):
		"""Gets the drag point."""
		self._instance.IGetDragPoint = value

	@property
	def i_set_drag_point(self):
		"""Sets the drag point."""
		return self._instance.ISetDragPoint

	@i_set_drag_point.setter
	def i_set_drag_point(self, value):
		"""Sets the drag point."""
		self._instance.ISetDragPoint = value

	@property
	def set_drag_point(self):
		"""Sets the drag point."""
		return self._instance.SetDragPoint

	@set_drag_point.setter
	def set_drag_point(self, value):
		"""Sets the drag point."""
		self._instance.SetDragPoint = value

