# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html
class IDragArrowManipulator:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def allow_flip(self):
		"""Gets or sets whether the unidirectional handle can change direction when dragged past length = 0."""
		return self._instance.AllowFlip

	@allow_flip.setter
	def allow_flip(self, value):
		"""Gets or sets whether the unidirectional handle can change direction when dragged past length = 0."""
		self._instance.AllowFlip = value

	@property
	def direction(self):
		"""Gets or sets the direction of the handle."""
		return self._instance.Direction

	@direction.setter
	def direction(self, value):
		"""Gets or sets the direction of the handle."""
		self._instance.Direction = value

	@property
	def fixed_length(self):
		"""Gets or sets whether the origin can be changed."""
		return self._instance.FixedLength

	@fixed_length.setter
	def fixed_length(self, value):
		"""Gets or sets whether the origin can be changed."""
		self._instance.FixedLength = value

	@property
	def length(self):
		"""Gets or sets the length of the handle."""
		return self._instance.Length

	@length.setter
	def length(self, value):
		"""Gets or sets the length of the handle."""
		self._instance.Length = value

	@property
	def length_opposite_direction(self):
		"""Gets or sets the length of the opposite handle."""
		return self._instance.LengthOppositeDirection

	@length_opposite_direction.setter
	def length_opposite_direction(self, value):
		"""Gets or sets the length of the opposite handle."""
		self._instance.LengthOppositeDirection = value

	@property
	def origin(self):
		"""Gets or sets the origin of the handle."""
		return self._instance.Origin

	@origin.setter
	def origin(self, value):
		"""Gets or sets the origin of the handle."""
		self._instance.Origin = value

	@property
	def show_opposite_direction(self):
		"""Gets or sets whether to display the bidirectional handle."""
		return self._instance.ShowOppositeDirection

	@show_opposite_direction.setter
	def show_opposite_direction(self, value):
		"""Gets or sets whether to display the bidirectional handle."""
		self._instance.ShowOppositeDirection = value

	@property
	def show_ruler(self):
		"""Gets or sets whether to display a ruler when the handle moves."""
		return self._instance.ShowRuler

	@show_ruler.setter
	def show_ruler(self, value):
		"""Gets or sets whether to display a ruler when the handle moves."""
		self._instance.ShowRuler = value

	@property
	def update(self):
		"""Displays a handle after having modified the length of the handle."""
		return self._instance.Update

	@update.setter
	def update(self, value):
		"""Displays a handle after having modified the length of the handle."""
		self._instance.Update = value

