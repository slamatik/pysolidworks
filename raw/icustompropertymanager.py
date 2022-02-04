# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html
class ICustomPropertyManager:
	def __init__(self, parent=None):
		self._instance = parent

	def count(self):
		"""Gets the number of custom properties."""
		# return self._instance.Count
		raise NotImplemented

	@property
	def link_all(self):
		"""Gets or sets whether to link or unlink all custom properties to or from their parent parts."""
		return self._instance.LinkAll

	@link_all.setter
	def link_all(self, value):
		"""Gets or sets whether to link or unlink all custom properties to or from their parent parts."""
		self._instance.LinkAll = value

	@property
	def owner(self):
		"""Gets the owner of this custom property."""
		return self._instance.Owner

	@owner.setter
	def owner(self, value):
		"""Gets the owner of this custom property."""
		self._instance.Owner = value

	@property
	def add(self):
		"""Adds a custom property to a configuration or model document."""
		return self._instance.Add3

	@add.setter
	def add(self, value):
		"""Adds a custom property to a configuration or model document."""
		self._instance.Add3 = value

	@property
	def delete(self):
		"""Deletes the specified custom property."""
		return self._instance.Delete2

	@delete.setter
	def delete(self, value):
		"""Deletes the specified custom property."""
		self._instance.Delete2 = value

	@property
	def get(self):
		"""Gets the value and the evaluated value of the specified custom property."""
		return self._instance.Get6

	@get.setter
	def get(self, value):
		"""Gets the value and the evaluated value of the specified custom property."""
		self._instance.Get6 = value

	@property
	def get_all(self):
		"""Gets all of the custom properties for this configuration."""
		return self._instance.GetAll3

	@get_all.setter
	def get_all(self, value):
		"""Gets all of the custom properties for this configuration."""
		self._instance.GetAll3 = value

	@property
	def get_names(self):
		"""Gets the names of the custom properties."""
		return self._instance.GetNames

	@get_names.setter
	def get_names(self, value):
		"""Gets the names of the custom properties."""
		self._instance.GetNames = value

	@property
	def get_type(self):
		"""Gets the type of the specified custom property for a configuration or model document."""
		return self._instance.GetType2

	@get_type.setter
	def get_type(self, value):
		"""Gets the type of the specified custom property for a configuration or model document."""
		self._instance.GetType2 = value

	@property
	def i_get_all(self):
		"""Gets all of the custom properties for this configuration."""
		return self._instance.IGetAll

	@i_get_all.setter
	def i_get_all(self, value):
		"""Gets all of the custom properties for this configuration."""
		self._instance.IGetAll = value

	@property
	def i_get_names(self):
		"""Gets the names of the custom properties."""
		return self._instance.IGetNames

	@i_get_names.setter
	def i_get_names(self, value):
		"""Gets the names of the custom properties."""
		self._instance.IGetNames = value

	@property
	def is_custom_property_editable(self):
		"""Gets whether the specified custom property is editable in the specified configuration."""
		return self._instance.IsCustomPropertyEditable

	@is_custom_property_editable.setter
	def is_custom_property_editable(self, value):
		"""Gets whether the specified custom property is editable in the specified configuration."""
		self._instance.IsCustomPropertyEditable = value

	@property
	def link_property(self):
		"""Sets whether to link or unlink the specified custom property to or from its parent part."""
		return self._instance.LinkProperty

	@link_property.setter
	def link_property(self, value):
		"""Sets whether to link or unlink the specified custom property to or from its parent part."""
		self._instance.LinkProperty = value

	@property
	def set(self):
		"""Sets the value for the specified custom property."""
		return self._instance.Set2

	@set.setter
	def set(self, value):
		"""Sets the value for the specified custom property."""
		self._instance.Set2 = value

