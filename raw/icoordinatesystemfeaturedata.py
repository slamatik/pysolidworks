# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoordinateSystemFeatureData_members.html
class ICoordinateSystemFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def origin_entity(self):
		"""Gets or sets the entity for the origin of this coordinate system feature."""
		return self._instance.OriginEntity

	@origin_entity.setter
	def origin_entity(self, value):
		"""Gets or sets the entity for the origin of this coordinate system feature."""
		self._instance.OriginEntity = value

	@property
	def transform(self):
		"""Gets the math transform for this coordinate system feature."""
		return self._instance.Transform

	@transform.setter
	def transform(self, value):
		"""Gets the math transform for this coordinate system feature."""
		self._instance.Transform = value

	@property
	def x_axis_entities(self):
		"""Gets or sets the entities for the x axis of this coordinate system feature."""
		return self._instance.XAxisEntities

	@x_axis_entities.setter
	def x_axis_entities(self, value):
		"""Gets or sets the entities for the x axis of this coordinate system feature."""
		self._instance.XAxisEntities = value

	@property
	def x_flipped(self):
		"""Gets or sets whether to flip the x axis of this coordinate system feature."""
		return self._instance.XFlipped

	@x_flipped.setter
	def x_flipped(self, value):
		"""Gets or sets whether to flip the x axis of this coordinate system feature."""
		self._instance.XFlipped = value

	@property
	def y_axis_entities(self):
		"""Gets or sets the entities for the y axis of this coordinate system."""
		return self._instance.YAxisEntities

	@y_axis_entities.setter
	def y_axis_entities(self, value):
		"""Gets or sets the entities for the y axis of this coordinate system."""
		self._instance.YAxisEntities = value

	@property
	def y_flipped(self):
		"""Gets or sets whether to flip the y axis of this coordinate system feature."""
		return self._instance.YFlipped

	@y_flipped.setter
	def y_flipped(self, value):
		"""Gets or sets whether to flip the y axis of this coordinate system feature."""
		self._instance.YFlipped = value

	@property
	def z_axis_entities(self):
		"""Gets or sets the entities for the z axis of this coordinate system feature."""
		return self._instance.ZAxisEntities

	@z_axis_entities.setter
	def z_axis_entities(self, value):
		"""Gets or sets the entities for the z axis of this coordinate system feature."""
		self._instance.ZAxisEntities = value

	@property
	def z_flipped(self):
		"""Gets or sets whether to flip the z axis of this coordinate system feature."""
		return self._instance.ZFlipped

	@z_flipped.setter
	def z_flipped(self, value):
		"""Gets or sets whether to flip the z axis of this coordinate system feature."""
		self._instance.ZFlipped = value

	@property
	def access_selections(self):
		"""Allows access to the selections that describe this coordinate system feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Allows access to the selections that describe this coordinate system feature."""
		self._instance.AccessSelections = value

	@property
	def get_origin_entity_type(self):
		"""Gets the type of entity of the origin."""
		return self._instance.GetOriginEntityType

	@get_origin_entity_type.setter
	def get_origin_entity_type(self, value):
		"""Gets the type of entity of the origin."""
		self._instance.GetOriginEntityType = value

	@property
	def get_x_axis_entities_count(self):
		"""Gets the number of entities for the x axis of this coordinate system feature."""
		return self._instance.GetXAxisEntitiesCount

	@get_x_axis_entities_count.setter
	def get_x_axis_entities_count(self, value):
		"""Gets the number of entities for the x axis of this coordinate system feature."""
		self._instance.GetXAxisEntitiesCount = value

	@property
	def get_x_axis_entities_types(self):
		"""Gets the x-axis type of entities."""
		return self._instance.GetXAxisEntitiesTypes

	@get_x_axis_entities_types.setter
	def get_x_axis_entities_types(self, value):
		"""Gets the x-axis type of entities."""
		self._instance.GetXAxisEntitiesTypes = value

	@property
	def get_y_axis_entities_count(self):
		"""Gets the number of entities for the y axis of this coordinate system feature."""
		return self._instance.GetYAxisEntitiesCount

	@get_y_axis_entities_count.setter
	def get_y_axis_entities_count(self, value):
		"""Gets the number of entities for the y axis of this coordinate system feature."""
		self._instance.GetYAxisEntitiesCount = value

	@property
	def get_y_axis_entities_types(self):
		"""Gets the y-axis type of entities."""
		return self._instance.GetYAxisEntitiesTypes

	@get_y_axis_entities_types.setter
	def get_y_axis_entities_types(self, value):
		"""Gets the y-axis type of entities."""
		self._instance.GetYAxisEntitiesTypes = value

	@property
	def get_z_axis_entities_count(self):
		"""Gets the number of entities for the z axis for this coordinate system feature."""
		return self._instance.GetZAxisEntitiesCount

	@get_z_axis_entities_count.setter
	def get_z_axis_entities_count(self, value):
		"""Gets the number of entities for the z axis for this coordinate system feature."""
		self._instance.GetZAxisEntitiesCount = value

	@property
	def get_z_axis_entities_types(self):
		"""Gets the z-axis type of entities."""
		return self._instance.GetZAxisEntitiesTypes

	@get_z_axis_entities_types.setter
	def get_z_axis_entities_types(self, value):
		"""Gets the z-axis type of entities."""
		self._instance.GetZAxisEntitiesTypes = value

	@property
	def i_access_selections(self):
		"""Allows access to the selections that describe this coordinate system feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Allows access to the selections that describe this coordinate system feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_origin_entity(self):
		"""Gets the entity for the origin of this coordinate system feature."""
		return self._instance.IGetOriginEntity

	@i_get_origin_entity.setter
	def i_get_origin_entity(self, value):
		"""Gets the entity for the origin of this coordinate system feature."""
		self._instance.IGetOriginEntity = value

	@property
	def i_get_origin_entity_type(self):
		"""Gets the type of entity of the origin."""
		return self._instance.IGetOriginEntityType

	@i_get_origin_entity_type.setter
	def i_get_origin_entity_type(self, value):
		"""Gets the type of entity of the origin."""
		self._instance.IGetOriginEntityType = value

	@property
	def i_get_x_axis_entities(self):
		"""Gets the entities for the x axis of this coordinate system feature."""
		return self._instance.IGetXAxisEntities

	@i_get_x_axis_entities.setter
	def i_get_x_axis_entities(self, value):
		"""Gets the entities for the x axis of this coordinate system feature."""
		self._instance.IGetXAxisEntities = value

	@property
	def i_get_x_axis_entities_types(self):
		"""Gets the x-axis type of entities."""
		return self._instance.IGetXAxisEntitiesTypes

	@i_get_x_axis_entities_types.setter
	def i_get_x_axis_entities_types(self, value):
		"""Gets the x-axis type of entities."""
		self._instance.IGetXAxisEntitiesTypes = value

	@property
	def i_get_y_axis_entities(self):
		"""Gets the entities for the y axis of this coordinate system feature."""
		return self._instance.IGetYAxisEntities

	@i_get_y_axis_entities.setter
	def i_get_y_axis_entities(self, value):
		"""Gets the entities for the y axis of this coordinate system feature."""
		self._instance.IGetYAxisEntities = value

	@property
	def i_get_y_axis_entities_types(self):
		"""Gets the y-axis type of entities."""
		return self._instance.IGetYAxisEntitiesTypes

	@i_get_y_axis_entities_types.setter
	def i_get_y_axis_entities_types(self, value):
		"""Gets the y-axis type of entities."""
		self._instance.IGetYAxisEntitiesTypes = value

	@property
	def i_get_z_axis_entities(self):
		"""Gets the entities for the z axis for this coordinate system feature."""
		return self._instance.IGetZAxisEntities

	@i_get_z_axis_entities.setter
	def i_get_z_axis_entities(self, value):
		"""Gets the entities for the z axis for this coordinate system feature."""
		self._instance.IGetZAxisEntities = value

	@property
	def i_get_z_axis_entities_types(self):
		"""Gets the z-axis type of entities."""
		return self._instance.IGetZAxisEntitiesTypes

	@i_get_z_axis_entities_types.setter
	def i_get_z_axis_entities_types(self, value):
		"""Gets the z-axis type of entities."""
		self._instance.IGetZAxisEntitiesTypes = value

	@property
	def i_set_origin_entity(self):
		"""Sets the entity for the origin of this coordinate feature data."""
		return self._instance.ISetOriginEntity

	@i_set_origin_entity.setter
	def i_set_origin_entity(self, value):
		"""Sets the entity for the origin of this coordinate feature data."""
		self._instance.ISetOriginEntity = value

	@property
	def i_set_x_axis_entities(self):
		"""Sets the entities for the x axis of this coordinate system feature."""
		return self._instance.ISetXAxisEntities

	@i_set_x_axis_entities.setter
	def i_set_x_axis_entities(self, value):
		"""Sets the entities for the x axis of this coordinate system feature."""
		self._instance.ISetXAxisEntities = value

	@property
	def i_set_y_axis_entities(self):
		"""Sets the entities for the y axis of this coordinate system feature."""
		return self._instance.ISetYAxisEntities

	@i_set_y_axis_entities.setter
	def i_set_y_axis_entities(self, value):
		"""Sets the entities for the y axis of this coordinate system feature."""
		self._instance.ISetYAxisEntities = value

	@property
	def i_set_z_axis_entities(self):
		"""Sets the entities for the z axis of this coordinate system feature."""
		return self._instance.ISetZAxisEntities

	@i_set_z_axis_entities.setter
	def i_set_z_axis_entities(self, value):
		"""Sets the entities for the z axis of this coordinate system feature."""
		self._instance.ISetZAxisEntities = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe this coordinate system feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe this coordinate system feature."""
		self._instance.ReleaseSelectionAccess = value

