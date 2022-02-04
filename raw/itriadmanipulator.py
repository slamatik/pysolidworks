# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITriadManipulator_members.html
class ITriadManipulator:
	def __init__(self, parent=None):
		self._instance = parent

	def cursor(self):
		"""Sets the cursor to use when the pointer is over the triad manipulator."""
		# return self._instance.Cursor
		raise NotImplemented

	def do_not_show(self):
		"""Specifies which triad manipulator's control points to not show."""
		# return self._instance.DoNotShow
		raise NotImplemented

	@property
	def origin(self):
		"""Gets or sets the origin for this triad manipulator."""
		return self._instance.Origin

	@origin.setter
	def origin(self, value):
		"""Gets or sets the origin for this triad manipulator."""
		self._instance.Origin = value

	@property
	def previous_drag_point(self):
		"""Gets the previous drag position of the triad manipulator."""
		return self._instance.PreviousDragPoint

	@previous_drag_point.setter
	def previous_drag_point(self, value):
		"""Gets the previous drag position of the triad manipulator."""
		self._instance.PreviousDragPoint = value

	@property
	def x_axis(self):
		"""Gets or sets the x axis for this triad manipulator."""
		return self._instance.XAxis

	@x_axis.setter
	def x_axis(self, value):
		"""Gets or sets the x axis for this triad manipulator."""
		self._instance.XAxis = value

	@property
	def y_axis(self):
		"""Gets or sets the y axis for this triad manipulator."""
		return self._instance.YAxis

	@y_axis.setter
	def y_axis(self, value):
		"""Gets or sets the y axis for this triad manipulator."""
		self._instance.YAxis = value

	@property
	def z_axis(self):
		"""Gets or sets the z axis for this triad manipulator."""
		return self._instance.ZAxis

	@z_axis.setter
	def z_axis(self, value):
		"""Gets or sets the z axis for this triad manipulator."""
		self._instance.ZAxis = value

	@property
	def set_color_ref_at_index(self):
		"""Sets the colors of the controls of a triad manipulator."""
		return self._instance.SetColorRefAtIndex

	@set_color_ref_at_index.setter
	def set_color_ref_at_index(self, value):
		"""Sets the colors of the controls of a triad manipulator."""
		self._instance.SetColorRefAtIndex = value

	@property
	def update_position(self):
		"""Updates the position of this triad manipulator."""
		return self._instance.UpdatePosition

	@update_position.setter
	def update_position(self, value):
		"""Updates the position of this triad manipulator."""
		self._instance.UpdatePosition = value

	@property
	def update_scale(self):
		"""Sets scale for the triad manipulator's x,y,z axes."""
		return self._instance.UpdateScale

	@update_scale.setter
	def update_scale(self, value):
		"""Sets scale for the triad manipulator's x,y,z axes."""
		self._instance.UpdateScale = value

