# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWrapSketchFeatureData_members.html
class IWrapSketchFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def face(self):
		"""Gets where this face was applied for this wrap feature or sets the face where to apply this wrap feature."""
		# return self._instance.Face
		raise NotImplemented

	@property
	def pull_direction(self):
		"""Gets or sets the pull direction for this wrap feature."""
		return self._instance.PullDirection

	@pull_direction.setter
	def pull_direction(self, value):
		"""Gets or sets the pull direction for this wrap feature."""
		self._instance.PullDirection = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether or not to reverse the direction of the wrap feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether or not to reverse the direction of the wrap feature."""
		self._instance.ReverseDirection = value

	@property
	def source_sketch(self):
		"""Gets or sets the sketch for this wrap feature."""
		return self._instance.SourceSketch

	@source_sketch.setter
	def source_sketch(self, value):
		"""Gets or sets the sketch for this wrap feature."""
		self._instance.SourceSketch = value

	@property
	def thickness(self):
		"""Gets or sets the thickness of this wrap feature."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or sets the thickness of this wrap feature."""
		self._instance.Thickness = value

	@property
	def type(self):
		"""Gets or sets the type of wrap for this wrap feature."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of wrap for this wrap feature."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this wrap feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this wrap feature."""
		self._instance.AccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this wrap feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this wrap feature."""
		self._instance.ReleaseSelectionAccess = value

