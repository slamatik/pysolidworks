# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevisionCloud_members.html
class IRevisionCloud:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the rotation angle of this revision cloud annotation."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the rotation angle of this revision cloud annotation."""
		self._instance.Angle = value

	@property
	def arc_radius(self):
		"""Gets or sets the maximum arc radius of this revision cloud annotation."""
		return self._instance.ArcRadius

	@arc_radius.setter
	def arc_radius(self, value):
		"""Gets or sets the maximum arc radius of this revision cloud annotation."""
		self._instance.ArcRadius = value

	@property
	def shape(self):
		"""Gets the shape of this revision cloud annotation."""
		return self._instance.Shape

	@shape.setter
	def shape(self, value):
		"""Gets the shape of this revision cloud annotation."""
		self._instance.Shape = value

	@property
	def finalize(self):
		"""Finalizes the creation of this revision cloud annotation."""
		return self._instance.Finalize

	@finalize.setter
	def finalize(self, value):
		"""Finalizes the creation of this revision cloud annotation."""
		self._instance.Finalize = value

	@property
	def get_annotation(self):
		"""Gets the annotation object for this revision cloud."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the annotation object for this revision cloud."""
		self._instance.GetAnnotation = value

	@property
	def get_next(self):
		"""Gets the next revision cloud in a drawing view or sheet."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next revision cloud in a drawing view or sheet."""
		self._instance.GetNext = value

	@property
	def get_path_point_at_index(self):
		"""Gets the coordinates of a point with the specified index on the path of this revision cloud annotation."""
		return self._instance.GetPathPointAtIndex

	@get_path_point_at_index.setter
	def get_path_point_at_index(self, value):
		"""Gets the coordinates of a point with the specified index on the path of this revision cloud annotation."""
		self._instance.GetPathPointAtIndex = value

	@property
	def get_path_point_count(self):
		"""Gets the number of points on the path of this revision cloud annotation."""
		return self._instance.GetPathPointCount

	@get_path_point_count.setter
	def get_path_point_count(self, value):
		"""Gets the number of points on the path of this revision cloud annotation."""
		self._instance.GetPathPointCount = value

	@property
	def i_get_annotation(self):
		"""Gets the annotation object for this revision cloud."""
		return self._instance.IGetAnnotation

	@i_get_annotation.setter
	def i_get_annotation(self, value):
		"""Gets the annotation object for this revision cloud."""
		self._instance.IGetAnnotation = value

	@property
	def i_get_next(self):
		"""Gets the next revision cloud in a drawing view or sheet."""
		return self._instance.IGetNext

	@i_get_next.setter
	def i_get_next(self, value):
		"""Gets the next revision cloud in a drawing view or sheet."""
		self._instance.IGetNext = value

	@property
	def i_get_path_point_at_index(self):
		"""Gets the coordinates of a point with the specified index on the path of this revision cloud annotation."""
		return self._instance.IGetPathPointAtIndex

	@i_get_path_point_at_index.setter
	def i_get_path_point_at_index(self, value):
		"""Gets the coordinates of a point with the specified index on the path of this revision cloud annotation."""
		self._instance.IGetPathPointAtIndex = value

	@property
	def set_path_point_at_index(self):
		"""Sets the specified coordinates of a point at the specified index on the path of this revision cloud annotation."""
		return self._instance.SetPathPointAtIndex

	@set_path_point_at_index.setter
	def set_path_point_at_index(self, value):
		"""Sets the specified coordinates of a point at the specified index on the path of this revision cloud annotation."""
		self._instance.SetPathPointAtIndex = value

