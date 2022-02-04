# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty_members.html
class ITextAndCustomProperty:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def custom_property_name(self):
		"""Gets or sets the name of the custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		return self._instance.CustomPropertyName

	@custom_property_name.setter
	def custom_property_name(self, value):
		"""Gets or sets the name of the custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		self._instance.CustomPropertyName = value

	@property
	def description(self):
		"""Gets the description of the text or custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		return self._instance.Description

	@description.setter
	def description(self, value):
		"""Gets the description of the text or custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		self._instance.Description = value

	@property
	def is_custom_property(self):
		"""Gets whether this is text or a custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		return self._instance.IsCustomProperty

	@is_custom_property.setter
	def is_custom_property(self, value):
		"""Gets whether this is text or a custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		self._instance.IsCustomProperty = value

	@property
	def name(self):
		"""Gets the name of the text or custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets the name of the text or custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		self._instance.Name = value

	@property
	def value(self):
		"""Gets or sets the value of the text or custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		return self._instance.Value

	@value.setter
	def value(self, value):
		"""Gets or sets the value of the text or custom property in a theme for a SOLIDWORKS MBD 3D PDF."""
		self._instance.Value = value

