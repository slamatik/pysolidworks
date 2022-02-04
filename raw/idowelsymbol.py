# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.html
class IDowelSymbol:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def flipped(self):
		"""Gets or sets whether to flip this dowel symbol."""
		return self._instance.Flipped

	@flipped.setter
	def flipped(self, value):
		"""Gets or sets whether to flip this dowel symbol."""
		self._instance.Flipped = value

	@property
	def get_annotation(self):
		"""Gets the IAnnotation object for this dowel symbol."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the IAnnotation object for this dowel symbol."""
		self._instance.GetAnnotation = value

	@property
	def get_arc_points(self):
		"""Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based."""
		return self._instance.GetArcPoints

	@get_arc_points.setter
	def get_arc_points(self, value):
		"""Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based."""
		self._instance.GetArcPoints = value

	@property
	def get_next(self):
		"""Gets the next dowel symbol in the current sheet, view, or model."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next dowel symbol in the current sheet, view, or model."""
		self._instance.GetNext = value

	@property
	def i_get_annotation(self):
		"""Gets the IAnnotation object for this dowel symbol."""
		return self._instance.IGetAnnotation

	@i_get_annotation.setter
	def i_get_annotation(self, value):
		"""Gets the IAnnotation object for this dowel symbol."""
		self._instance.IGetAnnotation = value

	@property
	def i_get_arc_points(self):
		"""Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based."""
		return self._instance.IGetArcPoints

	@i_get_arc_points.setter
	def i_get_arc_points(self, value):
		"""Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based."""
		self._instance.IGetArcPoints = value

	@property
	def i_get_next(self):
		"""Gets the next dowel symbol in the current sheet, view, or model."""
		return self._instance.IGetNext

	@i_get_next.setter
	def i_get_next(self, value):
		"""Gets the next dowel symbol in the current sheet, view, or model."""
		self._instance.IGetNext = value

