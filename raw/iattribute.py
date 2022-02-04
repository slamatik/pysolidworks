# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.html
class IAttribute:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def include_in_library_feature(self):
		"""Gets or sets whether this attribute is included in the library feature."""
		return self._instance.IncludeInLibraryFeature

	@include_in_library_feature.setter
	def include_in_library_feature(self, value):
		"""Gets or sets whether this attribute is included in the library feature."""
		self._instance.IncludeInLibraryFeature = value

	@property
	def delete(self):
		"""Deletes an attribute and lets you indicate whether or not to update the FeatureManager design tree if the deleted attribute appears in it."""
		return self._instance.Delete

	@delete.setter
	def delete(self, value):
		"""Deletes an attribute and lets you indicate whether or not to update the FeatureManager design tree if the deleted attribute appears in it."""
		self._instance.Delete = value

	@property
	def get_body(self):
		"""Gets the body to which this attribute is attached, if any."""
		return self._instance.GetBody

	@get_body.setter
	def get_body(self, value):
		"""Gets the body to which this attribute is attached, if any."""
		self._instance.GetBody = value

	@property
	def get_component(self):
		"""Returns the component to which this attribute is attached."""
		return self._instance.GetComponent

	@get_component.setter
	def get_component(self, value):
		"""Returns the component to which this attribute is attached."""
		self._instance.GetComponent = value

	@property
	def get_definition(self):
		"""Gets the definition of this attribute."""
		return self._instance.GetDefinition

	@get_definition.setter
	def get_definition(self, value):
		"""Gets the definition of this attribute."""
		self._instance.GetDefinition = value

	@property
	def get_entity(self):
		"""Gets the entity to which this attribute was originally associated."""
		return self._instance.GetEntity

	@get_entity.setter
	def get_entity(self, value):
		"""Gets the entity to which this attribute was originally associated."""
		self._instance.GetEntity = value

	@property
	def get_entity_state(self):
		"""Returns the state of the associated entity."""
		return self._instance.GetEntityState

	@get_entity_state.setter
	def get_entity_state(self, value):
		"""Returns the state of the associated entity."""
		self._instance.GetEntityState = value

	@property
	def get_name(self):
		"""Gets the name of the attribute."""
		return self._instance.GetName

	@get_name.setter
	def get_name(self, value):
		"""Gets the name of the attribute."""
		self._instance.GetName = value

	@property
	def get_parameter(self):
		"""Gets the specified parameter on this attribute."""
		return self._instance.GetParameter

	@get_parameter.setter
	def get_parameter(self, value):
		"""Gets the specified parameter on this attribute."""
		self._instance.GetParameter = value

	@property
	def i_get_component(self):
		"""Returns the component to which this attribute is attached."""
		return self._instance.IGetComponent2

	@i_get_component.setter
	def i_get_component(self, value):
		"""Returns the component to which this attribute is attached."""
		self._instance.IGetComponent2 = value

	@property
	def i_get_definition(self):
		"""Gets the definition of this attribute."""
		return self._instance.IGetDefinition

	@i_get_definition.setter
	def i_get_definition(self, value):
		"""Gets the definition of this attribute."""
		self._instance.IGetDefinition = value

	@property
	def i_get_entity(self):
		"""Gets the entity to which this attribute was originally associated."""
		return self._instance.IGetEntity2

	@i_get_entity.setter
	def i_get_entity(self, value):
		"""Gets the entity to which this attribute was originally associated."""
		self._instance.IGetEntity2 = value

	@property
	def i_get_parameter(self):
		"""Gets the specified parameter on this attribute."""
		return self._instance.IGetParameter

	@i_get_parameter.setter
	def i_get_parameter(self, value):
		"""Gets the specified parameter on this attribute."""
		self._instance.IGetParameter = value

