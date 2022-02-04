# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.html
class IMoveCopyBodyFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bodies(self):
		"""Gets or sets the bodies to move or rotate and copy."""
		return self._instance.Bodies

	@bodies.setter
	def bodies(self, value):
		"""Gets or sets the bodies to move or rotate and copy."""
		self._instance.Bodies = value

	@property
	def copy(self):
		"""Gets or sets whether to copy the selected bodies."""
		return self._instance.Copy

	@copy.setter
	def copy(self, value):
		"""Gets or sets whether to copy the selected bodies."""
		self._instance.Copy = value

	@property
	def number_of_copies(self):
		"""Gets or sets the number of copies."""
		return self._instance.NumberOfCopies

	@number_of_copies.setter
	def number_of_copies(self, value):
		"""Gets or sets the number of copies."""
		self._instance.NumberOfCopies = value

	@property
	def rotation_origin_x(self):
		"""Gets or sets the x coordinate for the origin about which to rotate the selected bodies."""
		return self._instance.RotationOriginX

	@rotation_origin_x.setter
	def rotation_origin_x(self, value):
		"""Gets or sets the x coordinate for the origin about which to rotate the selected bodies."""
		self._instance.RotationOriginX = value

	@property
	def rotation_origin_y(self):
		"""Gets or sets the y coordinate for the origin about which to rotate the selected bodies."""
		return self._instance.RotationOriginY

	@rotation_origin_y.setter
	def rotation_origin_y(self, value):
		"""Gets or sets the y coordinate for the origin about which to rotate the selected bodies."""
		self._instance.RotationOriginY = value

	@property
	def rotation_origin_z(self):
		"""Gets or sets the z coordinate for the origin about which to rotate the selected bodies."""
		return self._instance.RotationOriginZ

	@rotation_origin_z.setter
	def rotation_origin_z(self, value):
		"""Gets or sets the z coordinate for the origin about which to rotate the selected bodies."""
		self._instance.RotationOriginZ = value

	@property
	def transform_reference_entity(self):
		"""Gets or sets the entity to reference when moving or rotating the selected bodies."""
		return self._instance.TransformReferenceEntity

	@transform_reference_entity.setter
	def transform_reference_entity(self, value):
		"""Gets or sets the entity to reference when moving or rotating the selected bodies."""
		self._instance.TransformReferenceEntity = value

	@property
	def transform_type(self):
		"""Gets or sets whether to move or rotate the selected bodies."""
		return self._instance.TransformType

	@transform_type.setter
	def transform_type(self, value):
		"""Gets or sets whether to move or rotate the selected bodies."""
		self._instance.TransformType = value

	@property
	def transform_value(self):
		"""Gets or sets the distance or angle by which to move or rotate the selected bodies based on the selected edge."""
		return self._instance.TransformValue

	@transform_value.setter
	def transform_value(self, value):
		"""Gets or sets the distance or angle by which to move or rotate the selected bodies based on the selected edge."""
		self._instance.TransformValue = value

	@property
	def transform_x(self):
		"""Gets or sets the x coordinate for either moving or rotating the selected bodies."""
		return self._instance.TransformX

	@transform_x.setter
	def transform_x(self, value):
		"""Gets or sets the x coordinate for either moving or rotating the selected bodies."""
		self._instance.TransformX = value

	@property
	def transform_y(self):
		"""Gets or sets the y coordinate for either moving or rotating the selected bodies."""
		return self._instance.TransformY

	@transform_y.setter
	def transform_y(self, value):
		"""Gets or sets the y coordinate for either moving or rotating the selected bodies."""
		self._instance.TransformY = value

	@property
	def transform_z(self):
		"""Gets the z coordinate for either moving or rotating the selected bodies."""
		return self._instance.TransformZ

	@transform_z.setter
	def transform_z(self, value):
		"""Gets the z coordinate for either moving or rotating the selected bodies."""
		self._instance.TransformZ = value

	@property
	def translate_to_vertex(self):
		"""Gets or sets the entity to which to move the selected bodies."""
		return self._instance.TranslateToVertex

	@translate_to_vertex.setter
	def translate_to_vertex(self, value):
		"""Gets or sets the entity to which to move the selected bodies."""
		self._instance.TranslateToVertex = value

	@property
	def access_selections(self):
		"""Gains access to selections that define this feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections that define this feature."""
		self._instance.AccessSelections = value

	@property
	def add_mate(self):
		"""Adds a mate to the feature."""
		return self._instance.AddMate

	@add_mate.setter
	def add_mate(self, value):
		"""Adds a mate to the feature."""
		self._instance.AddMate = value

	@property
	def get_bodies_count(self):
		"""Gets the number of bodies to move or rotate and copy."""
		return self._instance.GetBodiesCount

	@get_bodies_count.setter
	def get_bodies_count(self, value):
		"""Gets the number of bodies to move or rotate and copy."""
		self._instance.GetBodiesCount = value

	@property
	def i_add_mate(self):
		"""Adds a mate to the feature."""
		return self._instance.IAddMate

	@i_add_mate.setter
	def i_add_mate(self, value):
		"""Adds a mate to the feature."""
		self._instance.IAddMate = value

	@property
	def i_get_bodies(self):
		"""Gets the bodies to move or rotate and copy."""
		return self._instance.IGetBodies

	@i_get_bodies.setter
	def i_get_bodies(self, value):
		"""Gets the bodies to move or rotate and copy."""
		self._instance.IGetBodies = value

	@property
	def i_set_bodies(self):
		"""Sets the bodies to move or rotate and copy."""
		return self._instance.ISetBodies

	@i_set_bodies.setter
	def i_set_bodies(self, value):
		"""Sets the bodies to move or rotate and copy."""
		self._instance.ISetBodies = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this move/copy body feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this move/copy body feature."""
		self._instance.ReleaseSelectionAccess = value

