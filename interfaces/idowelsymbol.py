# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDowelSymbol_members.html
class IDowelSymbol:
	def __init__(self, parent=None):
		self._instance = parent

	def flipped(self):
		"""Gets or sets whether to flip this dowel symbol."""
		# return self._instance.Flipped
		raise NotImplemented

	def get_annotation(self):
		"""Gets the IAnnotation object for this dowel symbol."""
		# return self._instance.GetAnnotation
		raise NotImplemented

	def get_arc_points(self):
		"""Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based."""
		# return self._instance.GetArcPoints
		raise NotImplemented

	def get_next(self):
		"""Gets the next dowel symbol in the current sheet, view, or model."""
		# return self._instance.GetNext
		raise NotImplemented

	def i_get_annotation(self):
		"""Gets the IAnnotation object for this dowel symbol."""
		# return self._instance.IGetAnnotation
		raise NotImplemented

	def i_get_arc_points(self):
		"""Gets the start, mid, and end points (in 2D only) of the arc segment on which this dowel symbol is based."""
		# return self._instance.IGetArcPoints
		raise NotImplemented

	def i_get_next(self):
		"""Gets the next dowel symbol in the current sheet, view, or model."""
		# return self._instance.IGetNext
		raise NotImplemented

