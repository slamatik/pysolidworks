# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferencePointCurveFeatureData_members.html
class IReferencePointCurveFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def closed_curve(self):
		"""Gets or sets whether the curve is closed or not."""
		return self._instance.ClosedCurve

	@closed_curve.setter
	def closed_curve(self, value):
		"""Gets or sets whether the curve is closed or not."""
		self._instance.ClosedCurve = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define a reference-point curve feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define a reference-point curve feature."""
		self._instance.AccessSelections = value

	@property
	def get_through_point_count(self):
		"""Gets the number of points through which this curve passes."""
		return self._instance.GetThroughPointCount

	@get_through_point_count.setter
	def get_through_point_count(self, value):
		"""Gets the number of points through which this curve passes."""
		self._instance.GetThroughPointCount = value

	@property
	def get_through_points(self):
		"""Gets the points through which this curve passes."""
		return self._instance.GetThroughPoints

	@get_through_points.setter
	def get_through_points(self, value):
		"""Gets the points through which this curve passes."""
		self._instance.GetThroughPoints = value

	@property
	def i_get_through_points(self):
		"""Gets the points through which this curve passes."""
		return self._instance.IGetThroughPoints

	@i_get_through_points.setter
	def i_get_through_points(self, value):
		"""Gets the points through which this curve passes."""
		self._instance.IGetThroughPoints = value

	@property
	def i_set_through_points(self):
		"""Sets the points through which this curve passes."""
		return self._instance.ISetThroughPoints

	@i_set_through_points.setter
	def i_set_through_points(self, value):
		"""Sets the points through which this curve passes."""
		self._instance.ISetThroughPoints = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this reference-point curve feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this reference-point curve feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_through_points(self):
		"""Sets the points through which this curve passes."""
		return self._instance.SetThroughPoints

	@set_through_points.setter
	def set_through_points(self, value):
		"""Sets the points through which this curve passes."""
		self._instance.SetThroughPoints = value

