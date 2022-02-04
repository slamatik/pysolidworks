# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHingeMateFeatureData_members.html
class IHingeMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the nominal angle between two selected faces."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the nominal angle between two selected faces."""
		self._instance.Angle = value

	@property
	def angle_selection(self):
		"""Gets or sets whether to specify angle limits."""
		return self._instance.AngleSelection

	@angle_selection.setter
	def angle_selection(self, value):
		"""Gets or sets whether to specify angle limits."""
		self._instance.AngleSelection = value

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this hinge mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this hinge mate."""
		self._instance.EntitiesToMate = value

	@property
	def mate_alignment(self):
		"""Gets or sets the mate alignment of this hinge mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the mate alignment of this hinge mate."""
		self._instance.MateAlignment = value

	@property
	def max_val(self):
		"""Gets or sets the maximum angular rotation between the two components."""
		return self._instance.MaxVal

	@max_val.setter
	def max_val(self, value):
		"""Gets or sets the maximum angular rotation between the two components."""
		self._instance.MaxVal = value

	@property
	def min_val(self):
		"""Gets or sets the minimum angular rotation between the two components."""
		return self._instance.MinVal

	@min_val.setter
	def min_val(self, value):
		"""Gets or sets the minimum angular rotation between the two components."""
		self._instance.MinVal = value

