# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMaterialVisualPropertiesData_members.html
class IMaterialVisualPropertiesData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the angle of the texture."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle of the texture."""
		self._instance.Angle = value

	@property
	def apply_appearance(self):
		"""Gets or sets whether to apply the appearance of material."""
		return self._instance.ApplyAppearance

	@apply_appearance.setter
	def apply_appearance(self, value):
		"""Gets or sets whether to apply the appearance of material."""
		self._instance.ApplyAppearance = value

	@property
	def apply_material_color_to_part(self):
		"""Gets or sets whether the part color matches the material color."""
		return self._instance.ApplyMaterialColorToPart

	@apply_material_color_to_part.setter
	def apply_material_color_to_part(self, value):
		"""Gets or sets whether the part color matches the material color."""
		self._instance.ApplyMaterialColorToPart = value

	@property
	def apply_material_hatch_to_section(self):
		"""Gets or sets whether the drawing section views use the material hatch."""
		return self._instance.ApplyMaterialHatchToSection

	@apply_material_hatch_to_section.setter
	def apply_material_hatch_to_section(self, value):
		"""Gets or sets whether the drawing section views use the material hatch."""
		self._instance.ApplyMaterialHatchToSection = value

	@property
	def blend_color(self):
		"""Gets or sets whether to blend the part color with the texture."""
		return self._instance.BlendColor

	@blend_color.setter
	def blend_color(self, value):
		"""Gets or sets whether to blend the part color with the texture."""
		self._instance.BlendColor = value

	@property
	def real_view(self):
		"""Gets or sets whether textures are displayed in RealView or Standard graphics."""
		return self._instance.RealView

	@real_view.setter
	def real_view(self, value):
		"""Gets or sets whether textures are displayed in RealView or Standard graphics."""
		self._instance.RealView = value

	@property
	def scale(self):
		"""Gets or sets the scale factor for the standard texture."""
		return self._instance.Scale2

	@scale.setter
	def scale(self, value):
		"""Gets or sets the scale factor for the standard texture."""
		self._instance.Scale2 = value

