# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchEllipse_members.html
class ISketchEllipse:
	def __init__(self, parent=None):
		self._instance = parent

	def get_center_point(self):
		"""Gets the sketch point for the center point of the ellipse."""
		# return self._instance.GetCenterPoint2
		raise NotImplemented

	def get_end_point(self):
		"""Gets the sketch point for the end point of the ellipse."""
		# return self._instance.GetEndPoint2
		raise NotImplemented

	def get_major_point(self):
		"""Gets the sketch point for the major point of the ellipse."""
		# return self._instance.GetMajorPoint2
		raise NotImplemented

	def get_minor_point(self):
		"""Gets the sketch point for the minor point of the ellipse."""
		# return self._instance.GetMinorPoint2
		raise NotImplemented

	def get_rotation_dir(self):
		"""Gets the rotation direction for this sketch ellipse segment."""
		# return self._instance.GetRotationDir
		raise NotImplemented

	def get_start_point(self):
		"""Gets the sketch point for the start point of the ellipse."""
		# return self._instance.GetStartPoint2
		raise NotImplemented

	def i_get_center_point(self):
		"""Gets the sketch point for the center point of the ellipse."""
		# return self._instance.IGetCenterPoint2
		raise NotImplemented

	def i_get_end_point(self):
		"""Gets the sketch point for the end point of the ellipse."""
		# return self._instance.IGetEndPoint2
		raise NotImplemented

	def i_get_major_point(self):
		"""Gets the sketch point for the major point of the ellipse."""
		# return self._instance.IGetMajorPoint2
		raise NotImplemented

	def i_get_minor_point(self):
		"""Gets the sketch point for the minor point of the ellipse."""
		# return self._instance.IGetMinorPoint2
		raise NotImplemented

	def i_get_start_point(self):
		"""Gets the sketch point for the start point of the ellipse."""
		# return self._instance.IGetStartPoint2
		raise NotImplemented

