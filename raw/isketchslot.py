# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSlot_members.html
class ISketchSlot:
	def __init__(self, parent=None):
		self._instance = parent

	def center_arc_direction(self):
		"""Gets the direction of the slot."""
		# return self._instance.CenterArcDirection
		raise NotImplemented

	def creation_type(self):
		"""Gets the type of slot."""
		# return self._instance.CreationType
		raise NotImplemented

	def length(self):
		"""Gets the length of the sketch slot."""
		# return self._instance.Length
		raise NotImplemented

	@property
	def length_type(self):
		"""Gets or sets the type of length of this sketch slot."""
		return self._instance.LengthType

	@length_type.setter
	def length_type(self, value):
		"""Gets or sets the type of length of this sketch slot."""
		self._instance.LengthType = value

	@property
	def width(self):
		"""Gets or sets the width of this sketch slot."""
		return self._instance.Width

	@width.setter
	def width(self, value):
		"""Gets or sets the width of this sketch slot."""
		self._instance.Width = value

	@property
	def get_center_point(self):
		"""Gets the centerpoint in this sketch slot."""
		return self._instance.GetCenterPoint

	@get_center_point.setter
	def get_center_point(self, value):
		"""Gets the centerpoint in this sketch slot."""
		self._instance.GetCenterPoint = value

	@property
	def get_center_point_handle(self):
		"""Gets the sketch point representing the centerpoint of the sketch slot."""
		return self._instance.GetCenterPointHandle

	@get_center_point_handle.setter
	def get_center_point_handle(self, value):
		"""Gets the sketch point representing the centerpoint of the sketch slot."""
		self._instance.GetCenterPointHandle = value

	@property
	def get_slot_points(self):
		"""Gets the points for this slot."""
		return self._instance.GetSlotPoints

	@get_slot_points.setter
	def get_slot_points(self, value):
		"""Gets the points for this slot."""
		self._instance.GetSlotPoints = value

