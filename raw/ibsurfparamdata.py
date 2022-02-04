# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBSurfParamData_members.html
class IBSurfParamData:
	def __init__(self, parent=None):
		self._instance = parent

	def control_point_column_count(self):
		"""Gets the number of control point columns."""
		# return self._instance.ControlPointColumnCount
		raise NotImplemented

	def control_point_dimension(self):
		"""Gets the dimension of the control points."""
		# return self._instance.ControlPointDimension
		raise NotImplemented

	def control_point_row_count(self):
		"""Gets the number of control point rows."""
		# return self._instance.ControlPointRowCount
		raise NotImplemented

	def u_knots(self):
		"""Gets the knot vector in the U direction."""
		# return self._instance.UKnots
		raise NotImplemented

	def u_order(self):
		"""Gets the order of the surface in the U direction."""
		# return self._instance.UOrder
		raise NotImplemented

	def u_periodicity(self):
		"""Gets whether the surface is periodic in the U direction."""
		# return self._instance.UPeriodicity
		raise NotImplemented

	def v_knots(self):
		"""Gets the knot vector in the V direction."""
		# return self._instance.VKnots
		raise NotImplemented

	def v_order(self):
		"""Gets the order of the surface in the V direction."""
		# return self._instance.VOrder
		raise NotImplemented

	def v_periodicity(self):
		"""Gets whether the surface is periodic in the V direction."""
		# return self._instance.VPeriodicity
		raise NotImplemented

	def get_control_points(self, row, column):
		"""
		Gets the coordinates of a control point at a specific row and column of the control point matrix.
		:param row: 1 <= index of row <= ControlPointRowCount
		:param column: 1 <= index of column <= ControlPointColumnCount
		"""
		# return self._instance.GetControlPoints(row, column)
		raise NotImplemented

	def i_get_control_points(self, row, column, count):
		"""
		Gets the coordinates of a control point at a specific row and column of the control point matrix.
		:param row: 1 <= index of row <= ControlPointRowCount
		:param column: 1 <= index of column <= ControlPointColumnCount
		:param count: ControlPointDimension
		"""
		# return self._instance.IGetControlPoints(row, column, count)
		raise NotImplemented

