# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html
class IFillSurfaceFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def merge(self):
		"""Gets or sets whether or not to merge results."""
		return self._instance.Merge

	@merge.setter
	def merge(self, value):
		"""Gets or sets whether or not to merge results."""
		self._instance.Merge = value

	@property
	def optimize_surface(self):
		"""Gets or sets whether or not to optimize the patch."""
		return self._instance.OptimizeSurface

	@optimize_surface.setter
	def optimize_surface(self, value):
		"""Gets or sets whether or not to optimize the patch."""
		self._instance.OptimizeSurface = value

	@property
	def resolution_control(self):
		"""Gets and sets the quality of the resolution of the fill-surface feature."""
		return self._instance.ResolutionControl

	@resolution_control.setter
	def resolution_control(self, value):
		"""Gets and sets the quality of the resolution of the fill-surface feature."""
		self._instance.ResolutionControl = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether or not to reverse direction while merging results."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether or not to reverse direction while merging results."""
		self._instance.ReverseDirection = value

	@property
	def reverse_surface(self):
		"""Gets or sets direction of the surface patch."""
		return self._instance.ReverseSurface

	@reverse_surface.setter
	def reverse_surface(self, value):
		"""Gets or sets direction of the surface patch."""
		self._instance.ReverseSurface = value

	@property
	def try_to_form_solid(self):
		"""Gets or sets whether to form a solid."""
		return self._instance.TryToFormSolid

	@try_to_form_solid.setter
	def try_to_form_solid(self, value):
		"""Gets or sets whether to form a solid."""
		self._instance.TryToFormSolid = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this fill-surface feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this fill-surface feature."""
		self._instance.AccessSelections = value

	@property
	def get_alternate_face(self):
		"""Gets an alternate face to use as the boundary face for the curvature control of the patch."""
		return self._instance.GetAlternateFace

	@get_alternate_face.setter
	def get_alternate_face(self, value):
		"""Gets an alternate face to use as the boundary face for the curvature control of the patch."""
		self._instance.GetAlternateFace = value

	@property
	def get_constraint_curves(self):
		"""Gets the constraint curves for this fill-surface feature."""
		return self._instance.GetConstraintCurves

	@get_constraint_curves.setter
	def get_constraint_curves(self, value):
		"""Gets the constraint curves for this fill-surface feature."""
		self._instance.GetConstraintCurves = value

	@property
	def get_constraint_curves_count(self):
		"""Gets the number of entities used to create the constraint curves for this fill-surface feature."""
		return self._instance.GetConstraintCurvesCount

	@get_constraint_curves_count.setter
	def get_constraint_curves_count(self, value):
		"""Gets the number of entities used to create the constraint curves for this fill-surface feature."""
		self._instance.GetConstraintCurvesCount = value

	@property
	def get_curvature_control(self):
		"""Gets the contact type for the input boundary."""
		return self._instance.GetCurvatureControl

	@get_curvature_control.setter
	def get_curvature_control(self, value):
		"""Gets the contact type for the input boundary."""
		self._instance.GetCurvatureControl = value

	@property
	def get_patch_boundary(self):
		"""Gets the entities used to define the patch boundary for this fill-surface feature."""
		return self._instance.GetPatchBoundary

	@get_patch_boundary.setter
	def get_patch_boundary(self, value):
		"""Gets the entities used to define the patch boundary for this fill-surface feature."""
		self._instance.GetPatchBoundary = value

	@property
	def get_patch_boundary_count(self):
		"""Gets the number of entities used to define the patch boundary for this fill-surface feature."""
		return self._instance.GetPatchBoundaryCount

	@get_patch_boundary_count.setter
	def get_patch_boundary_count(self, value):
		"""Gets the number of entities used to define the patch boundary for this fill-surface feature."""
		self._instance.GetPatchBoundaryCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this fill-surface feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this fill-surface feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_constraint_curves(self):
		"""Gets the constraint curves for this fill-surface feature."""
		return self._instance.IGetConstraintCurves

	@i_get_constraint_curves.setter
	def i_get_constraint_curves(self, value):
		"""Gets the constraint curves for this fill-surface feature."""
		self._instance.IGetConstraintCurves = value

	@property
	def i_get_patch_boundary(self):
		"""Gets the entities used to define the patch boundary for this fill-surface feature."""
		return self._instance.IGetPatchBoundary

	@i_get_patch_boundary.setter
	def i_get_patch_boundary(self, value):
		"""Gets the entities used to define the patch boundary for this fill-surface feature."""
		self._instance.IGetPatchBoundary = value

	@property
	def i_set_constraint_curves(self):
		"""Sets the entities for the constraint curves."""
		return self._instance.ISetConstraintCurves

	@i_set_constraint_curves.setter
	def i_set_constraint_curves(self, value):
		"""Sets the entities for the constraint curves."""
		self._instance.ISetConstraintCurves = value

	@property
	def i_set_patch_boundary(self):
		"""Sets the patch boundary for this fill-surface feature."""
		return self._instance.ISetPatchBoundary

	@i_set_patch_boundary.setter
	def i_set_patch_boundary(self, value):
		"""Sets the patch boundary for this fill-surface feature."""
		self._instance.ISetPatchBoundary = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that define this fill-surface feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that define this fill-surface feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_constraint_curves(self):
		"""Sets the entities for the constraint curves."""
		return self._instance.SetConstraintCurves

	@set_constraint_curves.setter
	def set_constraint_curves(self, value):
		"""Sets the entities for the constraint curves."""
		self._instance.SetConstraintCurves = value

	@property
	def set_curvature_control(self):
		"""Sets the contact type for this fill-surface feature."""
		return self._instance.SetCurvatureControl

	@set_curvature_control.setter
	def set_curvature_control(self, value):
		"""Sets the contact type for this fill-surface feature."""
		self._instance.SetCurvatureControl = value

	@property
	def set_patch_boundary(self):
		"""Sets the patch boundary for this fill-surface feature."""
		return self._instance.SetPatchBoundary

	@set_patch_boundary.setter
	def set_patch_boundary(self, value):
		"""Sets the patch boundary for this fill-surface feature."""
		self._instance.SetPatchBoundary = value

	@property
	def toggle_alternate_face(self):
		"""Switches the boundary face of the curvature control of the patch."""
		return self._instance.ToggleAlternateFace

	@toggle_alternate_face.setter
	def toggle_alternate_face(self, value):
		"""Switches the boundary face of the curvature control of the patch."""
		self._instance.ToggleAlternateFace = value

