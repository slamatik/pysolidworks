# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine_members.html
class ISketchLine:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the angle of the line."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle of the line."""
		self._instance.Angle = value

	@property
	def infinite(self):
		"""Gets whether the line is infinite or finite.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Infinite

	@infinite.setter
	def infinite(self, value):
		"""Gets whether the line is infinite or finite.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Infinite = value

	@property
	def get_bend_line_direction(self):
		"""Gets whether the sketch line is a bendline, and, if it is, the direction of the bendline."""
		return self._instance.GetBendLineDirection

	@get_bend_line_direction.setter
	def get_bend_line_direction(self, value):
		"""Gets whether the sketch line is a bendline, and, if it is, the direction of the bendline."""
		self._instance.GetBendLineDirection = value

	@property
	def get_end_point(self):
		"""Gets the sketch point for the end point of the line."""
		return self._instance.GetEndPoint2

	@get_end_point.setter
	def get_end_point(self, value):
		"""Gets the sketch point for the end point of the line."""
		self._instance.GetEndPoint2 = value

	@property
	def get_start_point(self):
		"""Gets the sketch point for the start point of the line."""
		return self._instance.GetStartPoint2

	@get_start_point.setter
	def get_start_point(self, value):
		"""Gets the sketch point for the start point of the line."""
		self._instance.GetStartPoint2 = value

	@property
	def i_get_end_point(self):
		"""Gets the sketch point for the end point of the line."""
		return self._instance.IGetEndPoint2

	@i_get_end_point.setter
	def i_get_end_point(self, value):
		"""Gets the sketch point for the end point of the line."""
		self._instance.IGetEndPoint2 = value

	@property
	def i_get_start_point(self):
		"""Gets the sketch point for the start point of the line."""
		return self._instance.IGetStartPoint2

	@i_get_start_point.setter
	def i_get_start_point(self, value):
		"""Gets the sketch point for the start point of the line."""
		self._instance.IGetStartPoint2 = value

	@property
	def make_infinite(self):
		"""Makes a line infinite."""
		return self._instance.MakeInfinite

	@make_infinite.setter
	def make_infinite(self, value):
		"""Makes a line infinite."""
		self._instance.MakeInfinite = value

