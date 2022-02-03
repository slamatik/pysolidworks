# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragArrowManipulator_members.html
class IDragArrowManipulator:
	def __init__(self, parent=None):
		self._instance = parent

	def allow_flip(self):
		"""Gets or sets whether the unidirectional handle can change direction when dragged past length = 0."""
		# return self._instance.AllowFlip
		raise NotImplemented

	def direction(self):
		"""Gets or sets the direction of the handle."""
		# return self._instance.Direction
		raise NotImplemented

	def fixed_length(self):
		"""Gets or sets whether the origin can be changed."""
		# return self._instance.FixedLength
		raise NotImplemented

	def length(self):
		"""Gets or sets the length of the handle."""
		# return self._instance.Length
		raise NotImplemented

	def length_opposite_direction(self):
		"""Gets or sets the length of the opposite handle."""
		# return self._instance.LengthOppositeDirection
		raise NotImplemented

	def origin(self):
		"""Gets or sets the origin of the handle."""
		# return self._instance.Origin
		raise NotImplemented

	def show_opposite_direction(self):
		"""Gets or sets whether to display the bidirectional handle."""
		# return self._instance.ShowOppositeDirection
		raise NotImplemented

	def show_ruler(self):
		"""Gets or sets whether to display a ruler when the handle moves."""
		# return self._instance.ShowRuler
		raise NotImplemented

	def update(self):
		"""Displays a handle after having modified the length of the handle."""
		# return self._instance.Update
		raise NotImplemented

