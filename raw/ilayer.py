# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayer_members.html
class ILayer:
	def __init__(self, parent=None):
		self._instance = parent

	def color(self):
		"""Gets and sets the line color for this layer."""
		# return self._instance.Color
		raise NotImplemented

	def description(self):
		"""Gets and sets this layer description."""
		# return self._instance.Description
		raise NotImplemented

	def name(self):
		"""Gets and sets the name of this layer."""
		# return self._instance.Name
		raise NotImplemented

	def printable(self):
		"""Gets and sets whether this layer is printed when the drawing document is printed."""
		# return self._instance.Printable
		raise NotImplemented

	def style(self):
		"""Gets and sets the line style for this layer."""
		# return self._instance.Style
		raise NotImplemented

	@property
	def visible(self):
		"""Gets or sets the visibility of this layer."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets the visibility of this layer."""
		self._instance.Visible = value

	@property
	def width(self):
		"""Gets and sets the line width for this layer."""
		return self._instance.Width

	@width.setter
	def width(self, value):
		"""Gets and sets the line width for this layer."""
		self._instance.Width = value

	@property
	def get_i_d(self):
		"""Gets the layer ID for this layer."""
		return self._instance.GetID

	@get_i_d.setter
	def get_i_d(self, value):
		"""Gets the layer ID for this layer."""
		self._instance.GetID = value

	@property
	def get_items(self):
		"""Gets the items on this layer."""
		return self._instance.GetItems

	@get_items.setter
	def get_items(self, value):
		"""Gets the items on this layer."""
		self._instance.GetItems = value

