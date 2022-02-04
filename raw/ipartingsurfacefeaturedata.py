# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.html
class IPartingSurfaceFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def knit(self):
		"""Gets or sets whether to knit all surfaces."""
		return self._instance.Knit

	@knit.setter
	def knit(self, value):
		"""Gets or sets whether to knit all surfaces."""
		self._instance.Knit = value

	@property
	def offset_angle(self):
		"""Gets or sets the angle for this parting surface feature."""
		return self._instance.OffsetAngle

	@offset_angle.setter
	def offset_angle(self, value):
		"""Gets or sets the angle for this parting surface feature."""
		self._instance.OffsetAngle = value

	@property
	def offset_distance(self):
		"""Gets or sets the distance that this parting surface feature extends."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the distance that this parting surface feature extends."""
		self._instance.OffsetDistance = value

	@property
	def parting_lines(self):
		"""Gets or sets the entities for the parting lines for this parting surface feature."""
		return self._instance.PartingLines

	@parting_lines.setter
	def parting_lines(self, value):
		"""Gets or sets the entities for the parting lines for this parting surface feature."""
		self._instance.PartingLines = value

	@property
	def parting_type(self):
		"""Gets or sets the type of parting surface."""
		return self._instance.PartingType

	@parting_type.setter
	def parting_type(self, value):
		"""Gets or sets the type of parting surface."""
		self._instance.PartingType = value

	@property
	def pull_direction_base(self):
		"""Gets or sets the entity that defines the direction of pull for this parting surface feature."""
		return self._instance.PullDirectionBase

	@pull_direction_base.setter
	def pull_direction_base(self, value):
		"""Gets or sets the entity that defines the direction of pull for this parting surface feature."""
		self._instance.PullDirectionBase = value

	@property
	def pull_direction_type(self):
		"""Gets the type of entity that specifies the direction of pull for this parting surface feature."""
		return self._instance.PullDirectionType

	@pull_direction_type.setter
	def pull_direction_type(self, value):
		"""Gets the type of entity that specifies the direction of pull for this parting surface feature."""
		self._instance.PullDirectionType = value

	@property
	def reverse_alignment(self):
		"""Gets or sets whether to reverse alignment of this parting surface feature."""
		return self._instance.ReverseAlignment

	@reverse_alignment.setter
	def reverse_alignment(self, value):
		"""Gets or sets whether to reverse alignment of this parting surface feature."""
		self._instance.ReverseAlignment = value

	@property
	def reverse_offset_direction(self):
		"""Gets or sets whether to reverse the direction of this parting surface feature."""
		return self._instance.ReverseOffsetDirection

	@reverse_offset_direction.setter
	def reverse_offset_direction(self, value):
		"""Gets or sets whether to reverse the direction of this parting surface feature."""
		self._instance.ReverseOffsetDirection = value

	@property
	def transition_distance(self):
		"""Gets or sets the distance to set between adjacent edges for this parting surface feature."""
		return self._instance.TransitionDistance

	@transition_distance.setter
	def transition_distance(self, value):
		"""Gets or sets the distance to set between adjacent edges for this parting surface feature."""
		self._instance.TransitionDistance = value

	@property
	def transition_type(self):
		"""Gets or sets the type of transition between adjacent edges for this parting surface feature."""
		return self._instance.TransitionType

	@transition_type.setter
	def transition_type(self, value):
		"""Gets or sets the type of transition between adjacent edges for this parting surface feature."""
		self._instance.TransitionType = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this parting surface feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this parting surface feature."""
		self._instance.AccessSelections = value

	@property
	def get_parting_lines_count(self):
		"""Gets the number of parting lines for this parting surface feature."""
		return self._instance.GetPartingLinesCount

	@get_parting_lines_count.setter
	def get_parting_lines_count(self, value):
		"""Gets the number of parting lines for this parting surface feature."""
		self._instance.GetPartingLinesCount = value

	@property
	def get_parting_lines_type(self):
		"""Gets the type of entity to use for parting lines for this parting surface feature."""
		return self._instance.GetPartingLinesType

	@get_parting_lines_type.setter
	def get_parting_lines_type(self, value):
		"""Gets the type of entity to use for parting lines for this parting surface feature."""
		self._instance.GetPartingLinesType = value

	@property
	def i_get_parting_lines(self):
		"""Gets the parting lines for this parting surface feature."""
		return self._instance.IGetPartingLines

	@i_get_parting_lines.setter
	def i_get_parting_lines(self, value):
		"""Gets the parting lines for this parting surface feature."""
		self._instance.IGetPartingLines = value

	@property
	def i_set_parting_lines(self):
		"""Sets the parting lines for this parting surface feature."""
		return self._instance.ISetPartingLines

	@i_set_parting_lines.setter
	def i_set_parting_lines(self, value):
		"""Sets the parting lines for this parting surface feature."""
		self._instance.ISetPartingLines = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this parting surface feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this parting surface feature."""
		self._instance.ReleaseSelectionAccess = value

