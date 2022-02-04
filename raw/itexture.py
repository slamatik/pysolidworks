# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITexture_members.html
class ITexture:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the rotation angle of the texture."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the rotation angle of the texture."""
		self._instance.Angle = value

	@property
	def blend_color(self):
		"""Gets or sets whether to blend the part color with the texture color."""
		return self._instance.BlendColor

	@blend_color.setter
	def blend_color(self, value):
		"""Gets or sets whether to blend the part color with the texture color."""
		self._instance.BlendColor = value

	@property
	def decal_type(self):
		"""Gets whether the texture is a decal."""
		return self._instance.DecalType

	@decal_type.setter
	def decal_type(self, value):
		"""Gets whether the texture is a decal."""
		self._instance.DecalType = value

	@property
	def ignore_color_material(self):
		"""Gets whether to ignore the color texture-based appearance."""
		return self._instance.IgnoreColorMaterial

	@ignore_color_material.setter
	def ignore_color_material(self, value):
		"""Gets whether to ignore the color texture-based appearance."""
		self._instance.IgnoreColorMaterial = value

	@property
	def material_name(self):
		"""Gets or sets the path and file name of the texture material."""
		return self._instance.MaterialName

	@material_name.setter
	def material_name(self, value):
		"""Gets or sets the path and file name of the texture material."""
		self._instance.MaterialName = value

	@property
	def scale_factor(self):
		"""Gets or sets the granularity of the texture."""
		return self._instance.ScaleFactor

	@scale_factor.setter
	def scale_factor(self, value):
		"""Gets or sets the granularity of the texture."""
		self._instance.ScaleFactor = value

	@property
	def trans_x(self):
		"""Gets the x coordinate for the translation point of the texture-based appearance."""
		return self._instance.TransX

	@trans_x.setter
	def trans_x(self, value):
		"""Gets the x coordinate for the translation point of the texture-based appearance."""
		self._instance.TransX = value

	@property
	def trans_y(self):
		"""Gets the y coordinate for the translation point of the texture-based appearance."""
		return self._instance.TransY

	@trans_y.setter
	def trans_y(self, value):
		"""Gets the y coordinate for the translation point of the texture-based appearance."""
		self._instance.TransY = value

	@property
	def u_dir(self):
		"""Gets the U direction of the texture-based appearance."""
		return self._instance.UDir

	@u_dir.setter
	def u_dir(self, value):
		"""Gets the U direction of the texture-based appearance."""
		self._instance.UDir = value

	@property
	def v_dir(self):
		"""Gets the V direction of the texture-based appearance."""
		return self._instance.VDir

	@v_dir.setter
	def v_dir(self, value):
		"""Gets the V direction of the texture-based appearance."""
		self._instance.VDir = value

	@property
	def v_scale(self):
		"""Gets the scale for this texture-based appearance or decal."""
		return self._instance.VScale

	@v_scale.setter
	def v_scale(self, value):
		"""Gets the scale for this texture-based appearance or decal."""
		self._instance.VScale = value

	@property
	def get_system_texture_name(self):
		"""Gets the name of the texture that appears in the Texture PropertyManager."""
		return self._instance.GetSystemTextureName

	@get_system_texture_name.setter
	def get_system_texture_name(self, value):
		"""Gets the name of the texture that appears in the Texture PropertyManager."""
		self._instance.GetSystemTextureName = value

