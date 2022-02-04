# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchText_members.html
class ISketchText:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def text(self):
		"""Gets or sets the text that makes up this sketch text."""
		return self._instance.Text

	@text.setter
	def text(self, value):
		"""Gets or sets the text that makes up this sketch text."""
		self._instance.Text = value

	@property
	def enum_edges(self):
		"""Gets the edges in this sketch text."""
		return self._instance.EnumEdges

	@enum_edges.setter
	def enum_edges(self, value):
		"""Gets the edges in this sketch text."""
		self._instance.EnumEdges = value

	@property
	def get_coordinates(self):
		"""Gets the position of this sketch text."""
		return self._instance.GetCoordinates

	@get_coordinates.setter
	def get_coordinates(self, value):
		"""Gets the position of this sketch text."""
		self._instance.GetCoordinates = value

	@property
	def get_edges(self):
		"""Gets the edges for this sketch text."""
		return self._instance.GetEdges2

	@get_edges.setter
	def get_edges(self, value):
		"""Gets the edges for this sketch text."""
		self._instance.GetEdges2 = value

	@property
	def get_text_format(self):
		"""Gets the text format for this sketch text."""
		return self._instance.GetTextFormat

	@get_text_format.setter
	def get_text_format(self, value):
		"""Gets the text format for this sketch text."""
		self._instance.GetTextFormat = value

	@property
	def get_use_doc_text_format(self):
		"""Gets whether default model text format is in use in this sketch text."""
		return self._instance.GetUseDocTextFormat

	@get_use_doc_text_format.setter
	def get_use_doc_text_format(self, value):
		"""Gets whether default model text format is in use in this sketch text."""
		self._instance.GetUseDocTextFormat = value

	@property
	def i_get_coordinates(self):
		"""Gets the position of this sketch text."""
		return self._instance.IGetCoordinates

	@i_get_coordinates.setter
	def i_get_coordinates(self, value):
		"""Gets the position of this sketch text."""
		self._instance.IGetCoordinates = value

	@property
	def i_get_text_format(self):
		"""Gets the text format for this sketch text."""
		return self._instance.IGetTextFormat

	@i_get_text_format.setter
	def i_get_text_format(self, value):
		"""Gets the text format for this sketch text."""
		self._instance.IGetTextFormat = value

	@property
	def i_set_text_format(self):
		"""Sets the text format for this sketch text."""
		return self._instance.ISetTextFormat

	@i_set_text_format.setter
	def i_set_text_format(self, value):
		"""Sets the text format for this sketch text."""
		self._instance.ISetTextFormat = value

	@property
	def set_coordinates(self):
		"""Sets the position of this sketch text."""
		return self._instance.SetCoordinates

	@set_coordinates.setter
	def set_coordinates(self, value):
		"""Sets the position of this sketch text."""
		self._instance.SetCoordinates = value

	@property
	def set_text_format(self):
		"""Sets the text format for this sketch text."""
		return self._instance.SetTextFormat

	@set_text_format.setter
	def set_text_format(self, value):
		"""Sets the text format for this sketch text."""
		self._instance.SetTextFormat = value

