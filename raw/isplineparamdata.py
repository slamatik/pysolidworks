# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineParamData_members.html
class ISplineParamData:
	def __init__(self, parent=None):
		self._instance = parent

	def color(self):
		"""Gets the color used to draw the spline."""
		# return self._instance.Color
		raise NotImplemented

	def control_points_count(self):
		"""Gets and sets the number of control points in the spline."""
		# return self._instance.ControlPointsCount
		raise NotImplemented

	def dimension(self):
		"""Gets and sets the dimension of the spline."""
		# return self._instance.Dimension
		raise NotImplemented

	def knot_points_count(self):
		"""Gets the number of knots in the spline."""
		# return self._instance.KnotPointsCount
		raise NotImplemented

	def layer(self):
		"""Gets the index of the layer in which this spline is drawn."""
		# return self._instance.Layer
		raise NotImplemented

	def layer_override(self):
		"""Gets the spline's properties that override the default properties of the layer."""
		# return self._instance.LayerOverride
		raise NotImplemented

	def line_style(self):
		"""Gets the line style used to draw the spline."""
		# return self._instance.LineStyle
		raise NotImplemented

	def line_width(self):
		"""Gets the line weight used to draw the spline."""
		# return self._instance.LineWidth
		raise NotImplemented

	def order(self):
		"""Gets and sets the number of nearby control points that influence any given point on the curve."""
		# return self._instance.Order
		raise NotImplemented

	def periodic(self):
		"""Gets and sets the periodicity of the spline."""
		# return self._instance.Periodic
		raise NotImplemented

	def reserved(self):
		"""Not used."""
		# return self._instance.Reserved
		raise NotImplemented

	def segment_count(self):
		"""Gets the number of segments in the spline."""
		# return self._instance.SegmentCount
		raise NotImplemented

	def get_control_points(self, control_points):
		"""
		Gets the coordinates of all of the control points of the spline.
		:param control_points: One-dimensional array of doubles (see Remarks)
		"""
		# return self._instance.GetControlPoints(control_points)
		raise NotImplemented

	def get_knot_points(self, knot_points):
		"""
		Gets the knot vector for the spline.
		:param knot_points: Array of double values between 0 and 1, inclusive (see Remarks)
		"""
		# return self._instance.GetKnotPoints(knot_points)
		raise NotImplemented

	def get_segments(self, segments):
		"""
		Gets the coefficients of all of the piecewise polynomials of a spline.
		:param segments: Array of doubles (see Remarks)
		"""
		# return self._instance.GetSegments(segments)
		raise NotImplemented

	def i_get_control_points(self, count, control_points):
		"""
		Gets the coordinates of all of the control points of the spline.
		:param count: Size of ControlPoints array
		:param control_points: 
in-process, unmanaged C++: Pointer to an array of doubles (see Remarks)
VBA, VB.NET, C#, and C++/CLI: Not supported 
 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IGetControlPoints(count, control_points)
		raise NotImplemented

	def i_get_knot_points(self, count, knot_points):
		"""
		Gets all of the knot points of the spline.
		:param count: Size of KnotPoints array
		:param knot_points: 
in-process, unmanaged C++: Pointer to an array of double values between 0 and 1, inclusive
VBA, VB.NET, C#, and C++/CLI: Not supported 
 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IGetKnotPoints(count, knot_points)
		raise NotImplemented

	def i_get_segments(self, count, segments):
		"""
		Gets the coefficients of all of the piecewise polynomials of a spline.
		:param count: Size of Segments array
		:param segments: 
in-process, unmanaged C++: Pointer to an array of doubles
VBA, VB.NET, C#, and C++/CLI: Not supported 
 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IGetSegments(count, segments)
		raise NotImplemented

	def set_control_points(self, control_points):
		"""
		Sets the coordinates of all of the control points of a spline.
		:param control_points: One-dimensional array of doubles (see Remarks)
		"""
		# return self._instance.SetControlPoints(control_points)
		raise NotImplemented

	def set_knot_points(self, knot_points):
		"""
		Sets the knot vector for a spline.
		:param knot_points: Array of doubles between 0 and 1, inclusive
		"""
		# return self._instance.SetKnotPoints(knot_points)
		raise NotImplemented

