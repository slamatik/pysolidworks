# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint_members.html
class ISketchPoint:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def color(self):
		"""Gets or sets the color of this sketch point."""
		return self._instance.Color

	@color.setter
	def color(self, value):
		"""Gets or sets the color of this sketch point."""
		self._instance.Color = value

	@property
	def layer(self):
		"""Gets or sets the layer for this sketch point."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""Gets or sets the layer for this sketch point."""
		self._instance.Layer = value

	@property
	def layer_override(self):
		"""Gets or sets whether the sketch point has properties that override the default properties of the layer."""
		return self._instance.LayerOverride

	@layer_override.setter
	def layer_override(self, value):
		"""Gets or sets whether the sketch point has properties that override the default properties of the layer."""
		self._instance.LayerOverride = value

	@property
	def type(self):
		"""Gets or sets the type of sketch point."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of sketch point."""
		self._instance.Type = value

	@property
	def x(self):
		"""Gets or sets the x coordinate of the sketch point."""
		return self._instance.X

	@x.setter
	def x(self, value):
		"""Gets or sets the x coordinate of the sketch point."""
		self._instance.X = value

	@property
	def y(self):
		"""Gets or sets  the y coordinate of the sketch point."""
		return self._instance.Y

	@y.setter
	def y(self, value):
		"""Gets or sets  the y coordinate of the sketch point."""
		self._instance.Y = value

	@property
	def z(self):
		"""Gets or sets the z coordinate of the sketch point."""
		return self._instance.Z

	@z.setter
	def z(self, value):
		"""Gets or sets the z coordinate of the sketch point."""
		self._instance.Z = value

	@property
	def de_select(self):
		"""Deselects the sketch point."""
		return self._instance.DeSelect

	@de_select.setter
	def de_select(self, value):
		"""Deselects the sketch point."""
		self._instance.DeSelect = value

	@property
	def get_coords(self):
		"""Gets the x coordinate of the sketch point."""
		return self._instance.GetCoords

	@get_coords.setter
	def get_coords(self, value):
		"""Gets the x coordinate of the sketch point."""
		self._instance.GetCoords = value

	@property
	def get_i_d(self):
		"""Gets the sketch point ID for this sketch point."""
		return self._instance.GetID

	@get_i_d.setter
	def get_i_d(self, value):
		"""Gets the sketch point ID for this sketch point."""
		self._instance.GetID = value

	@property
	def get_relations(self):
		"""Gets the sketch relations for this sketch point."""
		return self._instance.GetRelations

	@get_relations.setter
	def get_relations(self, value):
		"""Gets the sketch relations for this sketch point."""
		self._instance.GetRelations = value

	@property
	def get_relations_count(self):
		"""Gets the number of sketch relations for this sketch point."""
		return self._instance.GetRelationsCount

	@get_relations_count.setter
	def get_relations_count(self, value):
		"""Gets the number of sketch relations for this sketch point."""
		self._instance.GetRelationsCount = value

	@property
	def get_sketch(self):
		"""Gets the sketch for the current sketch point."""
		return self._instance.GetSketch

	@get_sketch.setter
	def get_sketch(self, value):
		"""Gets the sketch for the current sketch point."""
		self._instance.GetSketch = value

	@property
	def get_sketch_slot(self):
		"""Gets sketch slot with which this sketch point is associated."""
		return self._instance.GetSketchSlot

	@get_sketch_slot.setter
	def get_sketch_slot(self, value):
		"""Gets sketch slot with which this sketch point is associated."""
		self._instance.GetSketchSlot = value

	@property
	def i_get_i_d(self):
		"""Gets the sketch point ID for this sketch point."""
		return self._instance.IGetID

	@i_get_i_d.setter
	def i_get_i_d(self, value):
		"""Gets the sketch point ID for this sketch point."""
		self._instance.IGetID = value

	@property
	def i_get_relations(self):
		"""Gets the sketch relations for this sketch point."""
		return self._instance.IGetRelations

	@i_get_relations.setter
	def i_get_relations(self, value):
		"""Gets the sketch relations for this sketch point."""
		self._instance.IGetRelations = value

	@property
	def select(self):
		"""Selects the sketch point and marks it."""
		return self._instance.Select4

	@select.setter
	def select(self, value):
		"""Selects the sketch point and marks it."""
		self._instance.Select4 = value

	@property
	def set_coords(self):
		"""Sets the location of this sketch point."""
		return self._instance.SetCoords

	@set_coords.setter
	def set_coords(self, value):
		"""Sets the location of this sketch point."""
		self._instance.SetCoords = value

