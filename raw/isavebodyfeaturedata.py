# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveBodyFeatureData_members.html
class ISaveBodyFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def assembly_path(self):
		"""Gets or sets the path and filename of the assembly (*.sldasm) of save bodies."""
		return self._instance.AssemblyPath

	@assembly_path.setter
	def assembly_path(self, value):
		"""Gets or sets the path and filename of the assembly (*.sldasm) of save bodies."""
		self._instance.AssemblyPath = value

	@property
	def consume_body(self):
		"""Gets or sets whether to consume all bodies in the original part."""
		return self._instance.ConsumeBody

	@consume_body.setter
	def consume_body(self, value):
		"""Gets or sets whether to consume all bodies in the original part."""
		self._instance.ConsumeBody = value

	@property
	def copy_custom_properties(self):
		"""Gets or sets whether to copy custom properties to the new parts."""
		return self._instance.CopyCustomProperties

	@copy_custom_properties.setter
	def copy_custom_properties(self, value):
		"""Gets or sets whether to copy custom properties to the new parts."""
		self._instance.CopyCustomProperties = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this Save Bodies feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this Save Bodies feature."""
		self._instance.AccessSelections = value

	@property
	def add_save_bodies(self):
		"""Adds the specified bodies to the Save Bodies feature and saves them as part documents on disk."""
		return self._instance.AddSaveBodies

	@add_save_bodies.setter
	def add_save_bodies(self, value):
		"""Adds the specified bodies to the Save Bodies feature and saves them as part documents on disk."""
		self._instance.AddSaveBodies = value

	@property
	def get_save_bodies(self):
		"""Gets the save bodies in this Save Bodies feature."""
		return self._instance.GetSaveBodies

	@get_save_bodies.setter
	def get_save_bodies(self, value):
		"""Gets the save bodies in this Save Bodies feature."""
		self._instance.GetSaveBodies = value

	@property
	def get_save_bodies_count(self):
		"""Gets the number of save bodies in this Save Bodies feature."""
		return self._instance.GetSaveBodiesCount

	@get_save_bodies_count.setter
	def get_save_bodies_count(self, value):
		"""Gets the number of save bodies in this Save Bodies feature."""
		self._instance.GetSaveBodiesCount = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this Save Bodies feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this Save Bodies feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def remove_save_bodies(self):
		"""Removes the specified bodies from this Save Bodies feature."""
		return self._instance.RemoveSaveBodies

	@remove_save_bodies.setter
	def remove_save_bodies(self, value):
		"""Removes the specified bodies from this Save Bodies feature."""
		self._instance.RemoveSaveBodies = value

