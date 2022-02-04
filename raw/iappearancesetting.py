# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAppearanceSetting_members.html
class IAppearanceSetting:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def blurry_reflection(self):
		"""Gets or sets whether to blur the reflections of surfaces."""
		return self._instance.BlurryReflection

	@blurry_reflection.setter
	def blurry_reflection(self, value):
		"""Gets or sets whether to blur the reflections of surfaces."""
		self._instance.BlurryReflection = value

	@property
	def color(self):
		"""Gets or sets the color."""
		return self._instance.Color

	@color.setter
	def color(self, value):
		"""Gets or sets the color."""
		self._instance.Color = value

	@property
	def diffuse(self):
		"""Gets or sets the intensity of light on a surface."""
		return self._instance.Diffuse

	@diffuse.setter
	def diffuse(self, value):
		"""Gets or sets the intensity of light on a surface."""
		self._instance.Diffuse = value

	@property
	def double_sided(self):
		"""Gets or sets whether to enable shading from both sides of a surface when rendering a model with PhotoView 360."""
		return self._instance.DoubleSided

	@double_sided.setter
	def double_sided(self, value):
		"""Gets or sets whether to enable shading from both sides of a surface when rendering a model with PhotoView 360."""
		self._instance.DoubleSided = value

	@property
	def luminous(self):
		"""Gets or sets the brightness emitted from the surface."""
		return self._instance.Luminous

	@luminous.setter
	def luminous(self, value):
		"""Gets or sets the brightness emitted from the surface."""
		self._instance.Luminous = value

	@property
	def reflection(self):
		"""Gets or sets the reflectivity of a surface."""
		return self._instance.Reflection

	@reflection.setter
	def reflection(self, value):
		"""Gets or sets the reflectivity of a surface."""
		self._instance.Reflection = value

	@property
	def round_sharp_edges(self):
		"""Gets or sets the value by which to round sharp edges when rendering a model with PhotoView 360."""
		return self._instance.RoundSharpEdges

	@round_sharp_edges.setter
	def round_sharp_edges(self, value):
		"""Gets or sets the value by which to round sharp edges when rendering a model with PhotoView 360."""
		self._instance.RoundSharpEdges = value

	@property
	def specular(self):
		"""Gets or sets the intensity of highlights on surfaces."""
		return self._instance.Specular

	@specular.setter
	def specular(self, value):
		"""Gets or sets the intensity of highlights on surfaces."""
		self._instance.Specular = value

	@property
	def specular_color(self):
		"""Gets or sets the color of reflected highlights for a specular component."""
		return self._instance.SpecularColor

	@specular_color.setter
	def specular_color(self, value):
		"""Gets or sets the color of reflected highlights for a specular component."""
		self._instance.SpecularColor = value

	@property
	def specular_spread(self):
		"""Gets or sets the blurriness of reflections on a surface."""
		return self._instance.SpecularSpread

	@specular_spread.setter
	def specular_spread(self, value):
		"""Gets or sets the blurriness of reflections on a surface."""
		self._instance.SpecularSpread = value

	@property
	def transparent(self):
		"""Gets or sets the degree to which light can pass through a surface."""
		return self._instance.Transparent

	@transparent.setter
	def transparent(self, value):
		"""Gets or sets the degree to which light can pass through a surface."""
		self._instance.Transparent = value

