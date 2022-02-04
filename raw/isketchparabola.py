# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchParabola_members.html
class ISketchParabola:
	def __init__(self, parent=None):
		self._instance = parent

	def get_apex_point(self):
		"""Gets the sketch point for the apex point of the parabola."""
		# return self._instance.GetApexPoint2
		raise NotImplemented

	def get_end_point(self):
		"""Gets the sketch point for the end point of the parabola."""
		# return self._instance.GetEndPoint2
		raise NotImplemented

	def get_focal_point(self):
		"""Gets the sketch point for the focal point of the parabola."""
		# return self._instance.GetFocalPoint2
		raise NotImplemented

	def get_start_point(self):
		"""Gets the sketch point for the start point of the parabola."""
		# return self._instance.GetStartPoint2
		raise NotImplemented

	def i_get_apex_point(self):
		"""Gets the sketch point for the apex point of the parabola."""
		# return self._instance.IGetApexPoint2
		raise NotImplemented

	def i_get_end_point(self):
		"""Gets the sketch point for the end point of the parabola."""
		# return self._instance.IGetEndPoint2
		raise NotImplemented

	def i_get_focal_point(self):
		"""Gets the sketch point for the focal point of the parabola."""
		# return self._instance.IGetFocalPoint2
		raise NotImplemented

	def i_get_start_point(self):
		"""Gets the sketch point for the start point of the parabola."""
		# return self._instance.IGetStartPoint2
		raise NotImplemented

	def set_points(self, center_x, center_y, center_z, apex_x, apex_y, apex_z, start_x, start_y, start_z, end_x, end_y, end_z):
		"""
		Sets all four sketch points for a parabola.
		:param center_x: x coordinate of center (focal) sketch point
		:param center_y: y coordinate of center (focal) sketch point
		:param center_z: z coordinate of center (focal) sketch point
		:param apex_x: x coordinate of apex sketch point
		:param apex_y: y coordinate of apex sketch point
		:param apex_z: z coordinate of apex sketch point
		:param start_x: x coordinate of start sketch point
		:param start_y: y coordinate of start sketch point
		:param start_z: z coordinate of start sketch point
		:param end_x: x coordinate of end sketch point
		:param end_y: y coordinate of end sketch point
		:param end_z: z coordinate of end sketch point
		"""
		# return self._instance.SetPoints(center_x, center_y, center_z, apex_x, apex_y, apex_z, start_x, start_y, start_z, end_x, end_y, end_z)
		raise NotImplemented

