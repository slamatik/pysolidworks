# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlaneFeatureData_members.html
class IRefPlaneFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the angle of the reference plane feature."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle of the reference plane feature."""
		self._instance.Angle = value

	@property
	def angle_or_distance(self):
		"""Gets or sets the angle or distance of the specified reference for this reference plane feature."""
		return self._instance.AngleOrDistance

	@angle_or_distance.setter
	def angle_or_distance(self, value):
		"""Gets or sets the angle or distance of the specified reference for this reference plane feature."""
		self._instance.AngleOrDistance = value

	@property
	def auto_size(self):
		"""Gets or sets whether to automatically size the reference plane feature to either the geometry on which it is created or to the bounding box of the model geometry."""
		return self._instance.AutoSize

	@auto_size.setter
	def auto_size(self, value):
		"""Gets or sets whether to automatically size the reference plane feature to either the geometry on which it is created or to the bounding box of the model geometry."""
		self._instance.AutoSize = value

	@property
	def constraint(self):
		"""Gets or sets the constraint for the specified reference for this reference plane feature."""
		return self._instance.Constraint

	@constraint.setter
	def constraint(self, value):
		"""Gets or sets the constraint for the specified reference for this reference plane feature."""
		self._instance.Constraint = value

	@property
	def distance(self):
		"""Gets or sets the distance, in meters, to offset the reference plane feature."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the distance, in meters, to offset the reference plane feature."""
		self._instance.Distance = value

	@property
	def origin_on_curve(self):
		"""Gets or sets whether to place the origin on the curve for this reference plane feature."""
		return self._instance.OriginOnCurve

	@origin_on_curve.setter
	def origin_on_curve(self, value):
		"""Gets or sets whether to place the origin on the curve for this reference plane feature."""
		self._instance.OriginOnCurve = value

	@property
	def projection_type(self):
		"""Gets or sets the projection type for this on-surface reference plane feature."""
		return self._instance.ProjectionType

	@projection_type.setter
	def projection_type(self, value):
		"""Gets or sets the projection type for this on-surface reference plane feature."""
		self._instance.ProjectionType = value

	@property
	def reference(self):
		"""Gets or sets the reference entity for the specified reference for this reference plane feature."""
		return self._instance.Reference

	@reference.setter
	def reference(self, value):
		"""Gets or sets the reference entity for the specified reference for this reference plane feature."""
		self._instance.Reference = value

	@property
	def reversed_reference_direction(self):
		"""Gets or sets whether to reverse the direction of the specified reference for this reference plane feature."""
		return self._instance.ReversedReferenceDirection

	@reversed_reference_direction.setter
	def reversed_reference_direction(self, value):
		"""Gets or sets whether to reverse the direction of the specified reference for this reference plane feature."""
		self._instance.ReversedReferenceDirection = value

	@property
	def selections(self):
		"""Gets or sets the selected entities used to create the reference plane feature or sets the entities to use to create the reference plane feature."""
		return self._instance.Selections

	@selections.setter
	def selections(self, value):
		"""Gets or sets the selected entities used to create the reference plane feature or sets the entities to use to create the reference plane feature."""
		self._instance.Selections = value

	@property
	def solution_index(self):
		"""Gets or sets the intended plane when there are multiple planes from which to select for an on-surface reference plane feature."""
		return self._instance.SolutionIndex

	@solution_index.setter
	def solution_index(self, value):
		"""Gets or sets the intended plane when there are multiple planes from which to select for an on-surface reference plane feature."""
		self._instance.SolutionIndex = value

	@property
	def type(self):
		"""Gets the type of reference plane created in SOLIDWORKS 2009 or earlier. Can also get whether a constraint-based reference plane created in SOLIDWORKS 2010 or has angle or offset distance references. NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the type of reference plane created in SOLIDWORKS 2009 or earlier. Can also get whether a constraint-based reference plane created in SOLIDWORKS 2010 or has angle or offset distance references. NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Type = value

	@property
	def type(self):
		"""Gets whether the reference plane is constraint based; thus, created in SOLIDWORKS 2010 and later.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Type2

	@type.setter
	def type(self, value):
		"""Gets whether the reference plane is constraint based; thus, created in SOLIDWORKS 2010 and later.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Type2 = value

	@property
	def update_plane(self):
		"""Gets or sets whether to update this reference plane so that it is parallel to the screen."""
		return self._instance.UpdatePlane

	@update_plane.setter
	def update_plane(self, value):
		"""Gets or sets whether to update this reference plane so that it is parallel to the screen."""
		self._instance.UpdatePlane = value

	@property
	def use_normal_plane(self):
		"""Gets or sets whether to: 


Use the plane normal to the selected plane

Automatically size the plane to either the geometry on which it is created or to the bounding box of the model geometry"""
		return self._instance.UseNormalPlane

	@use_normal_plane.setter
	def use_normal_plane(self, value):
		"""Gets or sets whether to: 


Use the plane normal to the selected plane

Automatically size the plane to either the geometry on which it is created or to the bounding box of the model geometry"""
		self._instance.UseNormalPlane = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define a reference plane feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define a reference plane feature."""
		self._instance.AccessSelections = value

	@property
	def get_selections_count(self):
		"""Gets the number of entities selected to create this reference plane feature."""
		return self._instance.GetSelectionsCount

	@get_selections_count.setter
	def get_selections_count(self, value):
		"""Gets the number of entities selected to create this reference plane feature."""
		self._instance.GetSelectionsCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define a reference plane feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define a reference plane feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_selections(self):
		"""Gets the selected entities used to create this reference plane feature."""
		return self._instance.IGetSelections

	@i_get_selections.setter
	def i_get_selections(self, value):
		"""Gets the selected entities used to create this reference plane feature."""
		self._instance.IGetSelections = value

	@property
	def i_set_selections(self):
		"""Sets the entities to use to create the reference plane feature."""
		return self._instance.ISetSelections

	@i_set_selections.setter
	def i_set_selections(self, value):
		"""Sets the entities to use to create the reference plane feature."""
		self._instance.ISetSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created the reference plane feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created the reference plane feature."""
		self._instance.ReleaseSelectionAccess = value

