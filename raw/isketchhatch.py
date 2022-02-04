# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html
class ISketchHatch:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the hatch angle."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the hatch angle."""
		self._instance.Angle = value

	@property
	def color(self):
		"""Gets or sets the sketch hatch line color."""
		return self._instance.Color

	@color.setter
	def color(self, value):
		"""Gets or sets the sketch hatch line color."""
		self._instance.Color = value

	@property
	def layer(self):
		"""Gets or sets the layer used by this sketch hatch."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""Gets or sets the layer used by this sketch hatch."""
		self._instance.Layer = value

	@property
	def layer_override(self):
		"""Gets or sets whether the sketch hatch has properties that override the default properties of the layer."""
		return self._instance.LayerOverride

	@layer_override.setter
	def layer_override(self, value):
		"""Gets or sets whether the sketch hatch has properties that override the default properties of the layer."""
		self._instance.LayerOverride = value

	@property
	def pattern(self):
		"""Gets or sets the hatch pattern (also called type or name) of the sketch hatch (for example, "Stars" or "Honeycomb"), which is a string from the sldwks.ptn file."""
		return self._instance.Pattern

	@pattern.setter
	def pattern(self, value):
		"""Gets or sets the hatch pattern (also called type or name) of the sketch hatch (for example, "Stars" or "Honeycomb"), which is a string from the sldwks.ptn file."""
		self._instance.Pattern = value

	@property
	def pattern_id(self):
		"""Gets the pattern ID for this sketch hatch."""
		return self._instance.PatternId

	@pattern_id.setter
	def pattern_id(self, value):
		"""Gets the pattern ID for this sketch hatch."""
		self._instance.PatternId = value

	@property
	def scale(self):
		"""Gets or sets the hatch pattern scale."""
		return self._instance.Scale2

	@scale.setter
	def scale(self, value):
		"""Gets or sets the hatch pattern scale."""
		self._instance.Scale2 = value

	@property
	def solid_fill(self):
		"""Gets or sets whether to enable solid fill for the sketch hatch."""
		return self._instance.SolidFill

	@solid_fill.setter
	def solid_fill(self, value):
		"""Gets or sets whether to enable solid fill for the sketch hatch."""
		self._instance.SolidFill = value

	@property
	def de_select(self):
		"""Deselects the sketch hatch."""
		return self._instance.DeSelect

	@de_select.setter
	def de_select(self, value):
		"""Deselects the sketch hatch."""
		self._instance.DeSelect = value

	@property
	def get_face(self):
		"""Gets the face associated with this sketch hatch."""
		return self._instance.GetFace

	@get_face.setter
	def get_face(self, value):
		"""Gets the face associated with this sketch hatch."""
		self._instance.GetFace = value

	@property
	def get_i_d(self):
		"""Gets the ID for this sketch hatch."""
		return self._instance.GetID

	@get_i_d.setter
	def get_i_d(self, value):
		"""Gets the ID for this sketch hatch."""
		self._instance.GetID = value

	@property
	def get_sketch(self):
		"""Gets the sketch for the current sketch hatch."""
		return self._instance.GetSketch

	@get_sketch.setter
	def get_sketch(self, value):
		"""Gets the sketch for the current sketch hatch."""
		self._instance.GetSketch = value

	@property
	def i_get_face(self):
		"""Gets the face associated with this sketch hatch."""
		return self._instance.IGetFace2

	@i_get_face.setter
	def i_get_face(self, value):
		"""Gets the face associated with this sketch hatch."""
		self._instance.IGetFace2 = value

	@property
	def i_get_i_d(self):
		"""Gets the ID for this sketch hatch."""
		return self._instance.IGetID

	@i_get_i_d.setter
	def i_get_i_d(self, value):
		"""Gets the ID for this sketch hatch."""
		self._instance.IGetID = value

	@property
	def select(self):
		"""Selects the sketch hatch and marks it."""
		return self._instance.Select4

	@select.setter
	def select(self, value):
		"""Selects the sketch hatch and marks it."""
		self._instance.Select4 = value

