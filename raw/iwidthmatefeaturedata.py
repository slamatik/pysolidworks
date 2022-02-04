# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.html
class IWidthMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def constraint_type(self):
		"""Gets or sets the type of constraint for this width mate."""
		return self._instance.ConstraintType

	@constraint_type.setter
	def constraint_type(self, value):
		"""Gets or sets the type of constraint for this width mate."""
		self._instance.ConstraintType = value

	@property
	def distance_from_end(self):
		"""Gets or sets the distance from the end of this width mate."""
		return self._instance.DistanceFromEnd

	@distance_from_end.setter
	def distance_from_end(self, value):
		"""Gets or sets the distance from the end of this width mate."""
		self._instance.DistanceFromEnd = value

	@property
	def flip_dimension(self):
		"""Gets or sets whether to move entities to opposite sides of the dimension of this width mate."""
		return self._instance.FlipDimension

	@flip_dimension.setter
	def flip_dimension(self, value):
		"""Gets or sets whether to move entities to opposite sides of the dimension of this width mate."""
		self._instance.FlipDimension = value

	@property
	def percent_distance_from_end(self):
		"""Gets or sets the percentage of distance from the end of this width mate."""
		return self._instance.PercentDistanceFromEnd

	@percent_distance_from_end.setter
	def percent_distance_from_end(self, value):
		"""Gets or sets the percentage of distance from the end of this width mate."""
		self._instance.PercentDistanceFromEnd = value

	@property
	def tab_selection(self):
		"""Gets or sets the tab references for this width mate."""
		return self._instance.TabSelection

	@tab_selection.setter
	def tab_selection(self, value):
		"""Gets or sets the tab references for this width mate."""
		self._instance.TabSelection = value

	@property
	def width_selection(self):
		"""Gets or sets the width references for this width mate."""
		return self._instance.WidthSelection

	@width_selection.setter
	def width_selection(self, value):
		"""Gets or sets the width references for this width mate."""
		self._instance.WidthSelection = value

