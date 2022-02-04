# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchArc_members.html
class ISketchArc:
	def __init__(self, parent=None):
		self._instance = parent

	def get_center_point(self):
		"""Gets the sketch point for the center point of the arc."""
		# return self._instance.GetCenterPoint2
		raise NotImplemented

	def get_end_point(self):
		"""Gets the sketch point for the end point of the arc."""
		# return self._instance.GetEndPoint2
		raise NotImplemented

	def get_normal_vector(self):
		"""Gets the normal to the arc."""
		# return self._instance.GetNormalVector
		raise NotImplemented

	def get_radius(self):
		"""Gets the radius of the arc."""
		# return self._instance.GetRadius
		raise NotImplemented

	def get_rotation_dir(self):
		"""Gets the rotation direction of this sketch arc."""
		# return self._instance.GetRotationDir
		raise NotImplemented

	def get_start_point(self):
		"""Gets the sketch point for the start point of this arc."""
		# return self._instance.GetStartPoint2
		raise NotImplemented

	def i_get_center_point(self):
		"""Gets the sketch point for the center point of the arc."""
		# return self._instance.IGetCenterPoint2
		raise NotImplemented

	def i_get_end_point(self):
		"""Gets the sketch point for the end point of the arc."""
		# return self._instance.IGetEndPoint2
		raise NotImplemented

	def i_get_normal_vector(self):
		"""Gets the normal to the arc."""
		# return self._instance.IGetNormalVector
		raise NotImplemented

	def i_get_start_point(self):
		"""Gets the sketch point for the start point of this arc."""
		# return self._instance.IGetStartPoint2
		raise NotImplemented

	def is_circle(self):
		"""Gets whether the sketch arc is a complete circle or a partial arc."""
		# return self._instance.IsCircle
		raise NotImplemented

	def set_radius(self, radius):
		"""
		Sets the radius of the arc.
		:param radius: Radius in meters of the arc
		"""
		# return self._instance.SetRadius(radius)
		raise NotImplemented

