# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane_members.html
class IRefPlane:
	def __init__(self, parent=None):
		self._instance = parent

	def bounding_box(self):
		"""Gets the bounding box of the reference plane, the top-left and bottom-right points."""
		# return self._instance.BoundingBox
		raise NotImplemented

	def corner_points(self):
		"""Gets the corner points of this reference plane."""
		# return self._instance.CornerPoints
		raise NotImplemented

	def transform(self):
		"""Gets the plane transform with respect to the world."""
		# return self._instance.Transform
		raise NotImplemented

	def i_get_bounding_box(self):
		"""Gets the bounding box of the reference plane, the top-left and bottom-right points."""
		# return self._instance.IGetBoundingBox
		raise NotImplemented

	def i_get_corner_points(self):
		"""Gets the corner points of this reference plane."""
		# return self._instance.IGetCornerPoints
		raise NotImplemented

