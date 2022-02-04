# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager_members.html
class IConfigurationManager:
	def __init__(self, parent=None):
		self._instance = parent

	def active_configuration(self):
		"""Gets the active configuration."""
		# return self._instance.ActiveConfiguration
		raise NotImplemented

	def document(self):
		"""Gets the related model document."""
		# return self._instance.Document
		raise NotImplemented

	@property
	def enable_configuration_tree(self):
		"""Gets or sets whether to update the ConfigurationManager tree."""
		return self._instance.EnableConfigurationTree

	@enable_configuration_tree.setter
	def enable_configuration_tree(self, value):
		"""Gets or sets whether to update the ConfigurationManager tree."""
		self._instance.EnableConfigurationTree = value

	@property
	def link_display_states_to_configurations(self):
		"""Gets or sets whether to link or unlink display states to or from the active configuration."""
		return self._instance.LinkDisplayStatesToConfigurations

	@link_display_states_to_configurations.setter
	def link_display_states_to_configurations(self, value):
		"""Gets or sets whether to link or unlink display states to or from the active configuration."""
		self._instance.LinkDisplayStatesToConfigurations = value

	@property
	def show_configuration_descriptions(self):
		"""Gets or sets whether to display configuration descriptions in ConfigurationManager."""
		return self._instance.ShowConfigurationDescriptions

	@show_configuration_descriptions.setter
	def show_configuration_descriptions(self, value):
		"""Gets or sets whether to display configuration descriptions in ConfigurationManager."""
		self._instance.ShowConfigurationDescriptions = value

	@property
	def show_configuration_names(self):
		"""Gets or sets whether to display configuration names in ConfigurationManager."""
		return self._instance.ShowConfigurationNames

	@show_configuration_names.setter
	def show_configuration_names(self, value):
		"""Gets or sets whether to display configuration names in ConfigurationManager."""
		self._instance.ShowConfigurationNames = value

	@property
	def show_preview(self):
		"""Gets or sets whether to display the preview of a selected configuration."""
		return self._instance.ShowPreview

	@show_preview.setter
	def show_preview(self, value):
		"""Gets or sets whether to display the preview of a selected configuration."""
		self._instance.ShowPreview = value

	@property
	def add_configuration(self):
		"""Creates a new configuration."""
		return self._instance.AddConfiguration2

	@add_configuration.setter
	def add_configuration(self, value):
		"""Creates a new configuration."""
		self._instance.AddConfiguration2 = value

	@property
	def add_rebuild_save_mark(self):
		"""Adds marks indicating whether the specified configurations need to be rebuilt and their configuration data saved every time the model document is saved."""
		return self._instance.AddRebuildSaveMark

	@add_rebuild_save_mark.setter
	def add_rebuild_save_mark(self, value):
		"""Adds marks indicating whether the specified configurations need to be rebuilt and their configuration data saved every time the model document is saved."""
		self._instance.AddRebuildSaveMark = value

	@property
	def add_speed_pak(self):
		"""Creates a SpeedPak configuration that includes all faces and the specified threshold of parts or bodies for the active assembly configuration."""
		return self._instance.AddSpeedPak2

	@add_speed_pak.setter
	def add_speed_pak(self, value):
		"""Creates a SpeedPak configuration that includes all faces and the specified threshold of parts or bodies for the active assembly configuration."""
		self._instance.AddSpeedPak2 = value

	@property
	def get_configuration_params(self):
		"""Gets the parameters for this configuration."""
		return self._instance.GetConfigurationParams

	@get_configuration_params.setter
	def get_configuration_params(self, value):
		"""Gets the parameters for this configuration."""
		self._instance.GetConfigurationParams = value

	@property
	def get_configuration_params_count(self):
		"""Gets the number of parameters for this configuration."""
		return self._instance.GetConfigurationParamsCount

	@get_configuration_params_count.setter
	def get_configuration_params_count(self, value):
		"""Gets the number of parameters for this configuration."""
		self._instance.GetConfigurationParamsCount = value

	@property
	def i_get_configuration_params(self):
		"""Gets the parameters for this configuration."""
		return self._instance.IGetConfigurationParams

	@i_get_configuration_params.setter
	def i_get_configuration_params(self, value):
		"""Gets the parameters for this configuration."""
		self._instance.IGetConfigurationParams = value

	@property
	def i_set_configuration_params(self):
		"""Sets the parameters for this configuration."""
		return self._instance.ISetConfigurationParams

	@i_set_configuration_params.setter
	def i_set_configuration_params(self, value):
		"""Sets the parameters for this configuration."""
		self._instance.ISetConfigurationParams = value

	@property
	def remove_mark_for_all_configurations(self):
		"""Remove all marks indicating whether configurations need to be rebuilt and their configuration data saved every time the model document is saved."""
		return self._instance.RemoveMarkForAllConfigurations

	@remove_mark_for_all_configurations.setter
	def remove_mark_for_all_configurations(self, value):
		"""Remove all marks indicating whether configurations need to be rebuilt and their configuration data saved every time the model document is saved."""
		self._instance.RemoveMarkForAllConfigurations = value

	@property
	def set_configuration_params(self):
		"""Sets the parameters for this configuration."""
		return self._instance.SetConfigurationParams

	@set_configuration_params.setter
	def set_configuration_params(self, value):
		"""Sets the parameters for this configuration."""
		self._instance.SetConfigurationParams = value

	@property
	def set_expanded(self):
		"""Sets whether to display and expand all of the configuration nodes in the specified pane of the ConfigurationManager."""
		return self._instance.SetExpanded

	@set_expanded.setter
	def set_expanded(self, value):
		"""Sets whether to display and expand all of the configuration nodes in the specified pane of the ConfigurationManager."""
		self._instance.SetExpanded = value

	@property
	def sort_configuration_tree(self):
		"""Specifies the order in which to list configurations in the ConfigurationManager."""
		return self._instance.SortConfigurationTree

	@sort_configuration_tree.setter
	def sort_configuration_tree(self, value):
		"""Specifies the order in which to list configurations in the ConfigurationManager."""
		self._instance.SortConfigurationTree = value

