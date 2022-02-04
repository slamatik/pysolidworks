# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPointFeatureData_members.html
class IRefPointFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def along_curve_option(self):
		"""Gets or sets whether to enable or disable the option to create the reference point along a curve or to create multiple reference points."""
		return self._instance.AlongCurveOption

	@along_curve_option.setter
	def along_curve_option(self, value):
		"""Gets or sets whether to enable or disable the option to create the reference point along a curve or to create multiple reference points."""
		self._instance.AlongCurveOption = value

	@property
	def distance(self):
		"""Gets the distance at which the reference point was created or sets the distance at which to create the reference point."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets the distance at which the reference point was created or sets the distance at which to create the reference point."""
		self._instance.Distance = value

	@property
	def selections(self):
		"""Gets the entities selected to create the reference point or sets the entities to create the reference point."""
		return self._instance.Selections

	@selections.setter
	def selections(self, value):
		"""Gets the entities selected to create the reference point or sets the entities to create the reference point."""
		self._instance.Selections = value

	@property
	def type(self):
		"""Gets or sets the type of reference point."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of reference point."""
		self._instance.Type = value

	@property
	def access_selections(self):
		"""Accesses the selections used to create the reference point feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections used to create the reference point feature."""
		self._instance.AccessSelections = value

	@property
	def get_selections_count(self):
		"""Gets the number of entities selected to use to create the reference point."""
		return self._instance.GetSelectionsCount

	@get_selections_count.setter
	def get_selections_count(self, value):
		"""Gets the number of entities selected to use to create the reference point."""
		self._instance.GetSelectionsCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections used to create the reference point feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections used to create the reference point feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_selections(self):
		"""Gets the selected entities to use to create the reference points."""
		return self._instance.IGetSelections

	@i_get_selections.setter
	def i_get_selections(self, value):
		"""Gets the selected entities to use to create the reference points."""
		self._instance.IGetSelections = value

	@property
	def i_set_selections(self):
		"""Sets the number of entities to use to create the reference points."""
		return self._instance.ISetSelections

	@i_set_selections.setter
	def i_set_selections(self, value):
		"""Sets the number of entities to use to create the reference points."""
		self._instance.ISetSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created this reference point feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created this reference point feature."""
		self._instance.ReleaseSelectionAccess = value

