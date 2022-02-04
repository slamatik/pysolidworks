# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICombineBodiesFeatureData_members.html
class ICombineBodiesFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bodies_to_combine(self):
		"""Gets or sets the bodies to combine."""
		return self._instance.BodiesToCombine

	@bodies_to_combine.setter
	def bodies_to_combine(self, value):
		"""Gets or sets the bodies to combine."""
		self._instance.BodiesToCombine = value

	@property
	def main_body(self):
		"""Gets or sets the main body to keep when subtracting bodies from this combine feature."""
		return self._instance.MainBody

	@main_body.setter
	def main_body(self, value):
		"""Gets or sets the main body to keep when subtracting bodies from this combine feature."""
		self._instance.MainBody = value

	@property
	def operation_type(self):
		"""Gets or sets how to combine multiple solid bodies for a combine feature."""
		return self._instance.OperationType

	@operation_type.setter
	def operation_type(self, value):
		"""Gets or sets how to combine multiple solid bodies for a combine feature."""
		self._instance.OperationType = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this combine feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this combine feature."""
		self._instance.AccessSelections = value

	@property
	def get_bodies_to_combine_count(self):
		"""Gets the number of bodies to combine."""
		return self._instance.GetBodiesToCombineCount

	@get_bodies_to_combine_count.setter
	def get_bodies_to_combine_count(self, value):
		"""Gets the number of bodies to combine."""
		self._instance.GetBodiesToCombineCount = value

	@property
	def i_get_bodies_to_combine(self):
		"""Gets the bodies to combine."""
		return self._instance.IGetBodiesToCombine

	@i_get_bodies_to_combine.setter
	def i_get_bodies_to_combine(self, value):
		"""Gets the bodies to combine."""
		self._instance.IGetBodiesToCombine = value

	@property
	def i_set_bodies_to_combine(self):
		"""Sets the bodies to combine."""
		return self._instance.ISetBodiesToCombine

	@i_set_bodies_to_combine.setter
	def i_set_bodies_to_combine(self, value):
		"""Sets the bodies to combine."""
		self._instance.ISetBodiesToCombine = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this combine feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this combine feature."""
		self._instance.ReleaseSelectionAccess = value

