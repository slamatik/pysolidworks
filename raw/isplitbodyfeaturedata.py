# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData_members.html
class ISplitBodyFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def consume(self):
		"""Gets or sets whether the bodies in this Split feature are consumed."""
		return self._instance.Consume

	@consume.setter
	def consume(self, value):
		"""Gets or sets whether the bodies in this Split feature are consumed."""
		self._instance.Consume = value

	@property
	def override_default_template_settings(self):
		"""Gets or sets whether to use an alternate template to apply to all new part or assembly files created during the split operation."""
		return self._instance.OverrideDefaultTemplateSettings

	@override_default_template_settings.setter
	def override_default_template_settings(self, value):
		"""Gets or sets whether to use an alternate template to apply to all new part or assembly files created during the split operation."""
		self._instance.OverrideDefaultTemplateSettings = value

	@property
	def template_path(self):
		"""Gets or sets the template to use to make this Split feature."""
		return self._instance.TemplatePath

	@template_path.setter
	def template_path(self, value):
		"""Gets or sets the template to use to make this Split feature."""
		self._instance.TemplatePath = value

	@property
	def trim_tools(self):
		"""Gets the trimming surfaces used as trim tools in this Split feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.TrimTools

	@trim_tools.setter
	def trim_tools(self, value):
		"""Gets the trimming surfaces used as trim tools in this Split feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.TrimTools = value

	@property
	def access_selections(self):
		"""Gains access to a Split feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to a Split feature."""
		self._instance.AccessSelections = value

	@property
	def get_split_bodies(self):
		"""Gets the split bodies in this Split feature."""
		return self._instance.GetSplitBodies

	@get_split_bodies.setter
	def get_split_bodies(self, value):
		"""Gets the split bodies in this Split feature."""
		self._instance.GetSplitBodies = value

	@property
	def get_split_bodies_count(self):
		"""Gets the number of split bodies in this Split feature."""
		return self._instance.GetSplitBodiesCount

	@get_split_bodies_count.setter
	def get_split_bodies_count(self, value):
		"""Gets the number of split bodies in this Split feature."""
		self._instance.GetSplitBodiesCount = value

	@property
	def get_trim_tools_count(self):
		"""Gets the number of trimming surfaces used as trim tools in this Split feature."""
		return self._instance.GetTrimToolsCount

	@get_trim_tools_count.setter
	def get_trim_tools_count(self, value):
		"""Gets the number of trimming surfaces used as trim tools in this Split feature."""
		self._instance.GetTrimToolsCount = value

	@property
	def i_get_split_bodies(self):
		"""Gets the split bodies for this Split feature."""
		return self._instance.IGetSplitBodies

	@i_get_split_bodies.setter
	def i_get_split_bodies(self, value):
		"""Gets the split bodies for this Split feature."""
		self._instance.IGetSplitBodies = value

	@property
	def i_get_trim_tools(self):
		"""Gets the trimming surfaces used as trim tools in this Split feature."""
		return self._instance.IGetTrimTools

	@i_get_trim_tools.setter
	def i_get_trim_tools(self, value):
		"""Gets the trimming surfaces used as trim tools in this Split feature."""
		self._instance.IGetTrimTools = value

	@property
	def i_set_trim_tools(self):
		"""Gets the trimming surfaces used as trim tools in this Split feature."""
		return self._instance.ISetTrimTools

	@i_set_trim_tools.setter
	def i_set_trim_tools(self, value):
		"""Gets the trimming surfaces used as trim tools in this Split feature."""
		self._instance.ISetTrimTools = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this Split feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this Split feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_split_bodies(self):
		"""Edits the current split bodies in this Split feature."""
		return self._instance.SetSplitBodies2

	@set_split_bodies.setter
	def set_split_bodies(self, value):
		"""Edits the current split bodies in this Split feature."""
		self._instance.SetSplitBodies2 = value

