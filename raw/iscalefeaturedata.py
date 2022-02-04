# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.html
class IScaleFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bodies(self):
		"""Gets or sets whether the bodies are scaled in a multibody part."""
		return self._instance.Bodies

	@bodies.setter
	def bodies(self, value):
		"""Gets or sets whether the bodies are scaled in a multibody part."""
		self._instance.Bodies = value

	@property
	def coordinate_system(self):
		"""Gets or sets the coordinate system of the scale feature."""
		return self._instance.CoordinateSystem

	@coordinate_system.setter
	def coordinate_system(self, value):
		"""Gets or sets the coordinate system of the scale feature."""
		self._instance.CoordinateSystem = value

	@property
	def is_uniform(self):
		"""Gets or sets uniform scaling for this scale feature."""
		return self._instance.IsUniform

	@is_uniform.setter
	def is_uniform(self, value):
		"""Gets or sets uniform scaling for this scale feature."""
		self._instance.IsUniform = value

	@property
	def scale_uniform(self):
		"""Gets or sets the uniform scaling factor for this scale feature when uniform scaling is enabled."""
		return self._instance.ScaleUniform

	@scale_uniform.setter
	def scale_uniform(self, value):
		"""Gets or sets the uniform scaling factor for this scale feature when uniform scaling is enabled."""
		self._instance.ScaleUniform = value

	@property
	def scale_x(self):
		"""Gets or sets the scaling factor in the X direction when uniform scaling is disabled."""
		return self._instance.ScaleX

	@scale_x.setter
	def scale_x(self, value):
		"""Gets or sets the scaling factor in the X direction when uniform scaling is disabled."""
		self._instance.ScaleX = value

	@property
	def scale_y(self):
		"""Gets or sets the scaling factor in the Y direction when uniform scaling is disabled."""
		return self._instance.ScaleY

	@scale_y.setter
	def scale_y(self, value):
		"""Gets or sets the scaling factor in the Y direction when uniform scaling is disabled."""
		self._instance.ScaleY = value

	@property
	def scale_z(self):
		"""Gets or sets the scaling factor in the Z direction when uniform scaling is disabled."""
		return self._instance.ScaleZ

	@scale_z.setter
	def scale_z(self, value):
		"""Gets or sets the scaling factor in the Z direction when uniform scaling is disabled."""
		self._instance.ScaleZ = value

	@property
	def type(self):
		"""Gets or sets the scale type."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the scale type."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this scale feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this scale feature."""
		self._instance.AccessSelections = value

	@property
	def get_bodies_count(self):
		"""Gets the number of scaled bodies for this scale feature."""
		return self._instance.GetBodiesCount

	@get_bodies_count.setter
	def get_bodies_count(self, value):
		"""Gets the number of scaled bodies for this scale feature."""
		self._instance.GetBodiesCount = value

	@property
	def get_scale(self):
		"""Gets the scale factor for this scale feature in x, y,and z directions."""
		return self._instance.GetScale

	@get_scale.setter
	def get_scale(self, value):
		"""Gets the scale factor for this scale feature in x, y,and z directions."""
		self._instance.GetScale = value

	@property
	def i_access_selections(self):
		"""Allows access to a scale feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Allows access to a scale feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_bodies(self):
		"""Gets the bodies that are scaled in a multibody part."""
		return self._instance.IGetBodies

	@i_get_bodies.setter
	def i_get_bodies(self, value):
		"""Gets the bodies that are scaled in a multibody part."""
		self._instance.IGetBodies = value

	@property
	def i_set_bodies(self):
		"""Sets the bodies that are scaled in a multibody part."""
		return self._instance.ISetBodies

	@i_set_bodies.setter
	def i_set_bodies(self, value):
		"""Sets the bodies that are scaled in a multibody part."""
		self._instance.ISetBodies = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the scale feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the scale feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_scale(self):
		"""Sets the scale factor for this scale feature in the x, y,and z directions."""
		return self._instance.SetScale

	@set_scale.setter
	def set_scale(self, value):
		"""Sets the scale factor for this scale feature in the x, y,and z directions."""
		self._instance.SetScale = value

