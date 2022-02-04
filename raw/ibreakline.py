# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html
class IBreakLine:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def break_sketch_blocks(self):
		"""Gets or sets whether to break sketch blocks."""
		return self._instance.BreakSketchBlocks

	@break_sketch_blocks.setter
	def break_sketch_blocks(self, value):
		"""Gets or sets whether to break sketch blocks."""
		self._instance.BreakSketchBlocks = value

	@property
	def layer(self):
		"""Gets or sets the layer for this break line in the drawing view."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""Gets or sets the layer for this break line in the drawing view."""
		self._instance.Layer = value

	@property
	def orientation(self):
		"""Gets the orientation of this break line in the drawing view."""
		return self._instance.Orientation

	@orientation.setter
	def orientation(self, value):
		"""Gets the orientation of this break line in the drawing view."""
		self._instance.Orientation = value

	@property
	def shape_intensity(self):
		"""Gets or sets the shape intensity of a jagged cut break line."""
		return self._instance.ShapeIntensity

	@shape_intensity.setter
	def shape_intensity(self, value):
		"""Gets or sets the shape intensity of a jagged cut break line."""
		self._instance.ShapeIntensity = value

	@property
	def style(self):
		"""Gets or sets the style of the break line in the drawing view."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets the style of the break line in the drawing view."""
		self._instance.Style = value

	@property
	def get_position(self):
		"""Gets the location of this break line in the drawing view."""
		return self._instance.GetPosition

	@get_position.setter
	def get_position(self, value):
		"""Gets the location of this break line in the drawing view."""
		self._instance.GetPosition = value

	@property
	def get_view(self):
		"""Gets the drawing view for this break line."""
		return self._instance.GetView

	@get_view.setter
	def get_view(self, value):
		"""Gets the drawing view for this break line."""
		self._instance.GetView = value

	@property
	def select(self):
		"""Selects the break line and marks it."""
		return self._instance.Select

	@select.setter
	def select(self, value):
		"""Selects the break line and marks it."""
		self._instance.Select = value

	@property
	def set_position(self):
		"""Sets the locations of the break lines in the drawing view."""
		return self._instance.SetPosition

	@set_position.setter
	def set_position(self, value):
		"""Sets the locations of the break lines in the drawing view."""
		self._instance.SetPosition = value

