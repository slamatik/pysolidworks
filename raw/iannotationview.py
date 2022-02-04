# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView_members.html
class IAnnotationView:
	def __init__(self, parent=None):
		self._instance = parent

	def always_d(self):
		"""Gets whether to display annotations in 2D or 3D."""
		# return self._instance.Always2D
		raise NotImplemented

	def angle_made_with_view_horizontal(self):
		"""Gets the angle used to make the annotation view horizontal."""
		# return self._instance.AngleMadeWithViewHorizontal
		raise NotImplemented

	def annotation_count(self):
		"""Gets the number of annotations in this annotation view."""
		# return self._instance.AnnotationCount
		raise NotImplemented

	def flat_pattern_view(self):
		"""Gets whether this annotation view is a flat-pattern view."""
		# return self._instance.FlatPatternView
		raise NotImplemented

	def unassigned_view(self):
		"""Gets whether this annotation view is assigned to a 3D View."""
		# return self._instance.UnassignedView
		raise NotImplemented

	def activate(self):
		"""Activates this annotation view."""
		# return self._instance.Activate
		raise NotImplemented

	def activate_and_reorient(self):
		"""Activates and reorients this annotation view."""
		# return self._instance.ActivateAndReorient
		raise NotImplemented

	def get_annotations(self, dim_xpert_only, unassigned_in_plane):
		"""
		Gets the annotations in this annotation view.
		:param dim_xpert_only: True to get only DimXpert annotations, false to get all annotations
		:param unassigned_in_plane: True to get only DimXpert annotations, false to get all annotations
		"""
		# return self._instance.GetAnnotations2(dim_xpert_only, unassigned_in_plane)
		raise NotImplemented

	def get_view_rotation(self):
		"""Gets the rotation matrix of the annotation view relative to the X-Y plane of the model."""
		# return self._instance.GetViewRotation
		raise NotImplemented

	def hide(self):
		"""Hides the annotations in an annotation view that is not activated."""
		# return self._instance.Hide
		raise NotImplemented

	def i_get_view_rotation(self):
		"""Gets the rotation matrix of the annotation view relative to the X-Y plane of the model."""
		# return self._instance.IGetViewRotation
		raise NotImplemented

	def is_shown(self):
		"""Gets whether the annotations in this annotation view are shown."""
		# return self._instance.IsShown
		raise NotImplemented

	def move_annotations(self, annotations_to_move):
		"""
		Moves the specified annotations to this annotation view.
		:param annotations_to_move: Annotations to move
		"""
		# return self._instance.MoveAnnotations(annotations_to_move)
		raise NotImplemented

	def orient(self):
		"""Orients this annotation view."""
		# return self._instance.Orient
		raise NotImplemented

	def show(self):
		"""Shows the annotations in an annotation view that is not activated."""
		# return self._instance.Show
		raise NotImplemented

