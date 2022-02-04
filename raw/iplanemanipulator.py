# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPlaneManipulator_members.html
class IPlaneManipulator:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def color(self):
		"""Gets or sets the color of a plane."""
		return self._instance.Color

	@color.setter
	def color(self, value):
		"""Gets or sets the color of a plane."""
		self._instance.Color = value

	@property
	def distance(self):
		"""Gets or sets the distance to move a plane that has a manipulator."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the distance to move a plane that has a manipulator."""
		self._instance.Distance = value

	@property
	def height(self):
		"""Gets or sets the height of a plane that has a manipulator."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of a plane that has a manipulator."""
		self._instance.Height = value

	@property
	def normal(self):
		"""Gets or sets the normal-to vector for a plane that has a manipulator."""
		return self._instance.Normal

	@normal.setter
	def normal(self, value):
		"""Gets or sets the normal-to vector for a plane that has a manipulator."""
		self._instance.Normal = value

	@property
	def origin(self):
		"""Gets or sets the origin of the plane."""
		return self._instance.Origin

	@origin.setter
	def origin(self, value):
		"""Gets or sets the origin of the plane."""
		self._instance.Origin = value

	@property
	def width(self):
		"""Gets or sets the width of a plane that has a manipulator."""
		return self._instance.Width

	@width.setter
	def width(self, value):
		"""Gets or sets the width of a plane that has a manipulator."""
		self._instance.Width = value

	@property
	def x_angle(self):
		"""Gets or sets the x coordinate of the angle to use to rotate a plane that has a manipulator."""
		return self._instance.XAngle

	@x_angle.setter
	def x_angle(self, value):
		"""Gets or sets the x coordinate of the angle to use to rotate a plane that has a manipulator."""
		self._instance.XAngle = value

	@property
	def y_angle(self):
		"""Gets or sets the y coordinate of the angle to use to rotate a plane that has a manipulator."""
		return self._instance.YAngle

	@y_angle.setter
	def y_angle(self, value):
		"""Gets or sets the y coordinate of the angle to use to rotate a plane that has a manipulator."""
		self._instance.YAngle = value

	@property
	def update(self):
		"""Updates a plane that has a manipulator after modifying it."""
		return self._instance.Update

	@update.setter
	def update(self, value):
		"""Updates a plane that has a manipulator after modifying it."""
		self._instance.Update = value

