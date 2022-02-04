# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveParamData_members.html
class ICurveParamData:
	def __init__(self, parent=None):
		self._instance = parent

	def curve_tag(self):
		"""Gets the ID for this curve."""
		# return self._instance.CurveTag
		raise NotImplemented

	def curve_type(self):
		"""Gets the type of curve."""
		# return self._instance.CurveType
		raise NotImplemented

	def end_point(self):
		"""Gets the x, y, and z coordinates for the end point of this curve."""
		# return self._instance.EndPoint
		raise NotImplemented

	def sense(self):
		"""Gets whether the curve and edge are in the same direction."""
		# return self._instance.Sense
		raise NotImplemented

	def start_point(self):
		"""Gets the x, y, and z coordinates for the start point of the curve."""
		# return self._instance.StartPoint
		raise NotImplemented

	def u_max_value(self):
		"""Gets the maximum U parameter value."""
		# return self._instance.UMaxValue
		raise NotImplemented

	def u_min_value(self):
		"""Gets the minimum U parameter value."""
		# return self._instance.UMinValue
		raise NotImplemented

