from interfaces.iconfiguration import IConfiguration


# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager.html

class IConfigurationManager:
    def __init__(self, parent):
        self._instance = parent.ConfigurationManager

    @property
    def active_configuration(self):
        """Gets the active configuration."""
        return self._instance.ActiveConfiguration

    # @property
    # def active_configuration(self):
    #     return IConfiguration(self._instance)

    @property
    def document(self):
        """Gets the related model document."""
        return self._instance.Document

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

    def add_configuration(self, name, comment, alternate_name, options, parent_config_name, description, rebuild):
        """
        Creates a new configuration.
        :param name: Name of the configuration
        :param comment: Comment displayed in Configuration Properties
        :param alternate_name: Alternate configuration name (i.e., user-specified name); used if Options is set to
        swConfigurationOptions2_e_UseAlternateName
        :param options: Combination of one or more configuration options as defined in swConfigurationOptions2_e (see Remarks)
        :param parent_config_name: Name of parent configuration
        :param description: Text that identifies the configuration
        :param rebuild: True to rebuild the model after adding this configuration, false to not
        """
        # return self._instance.AddConfiguration2(name, comment, alternate_name, options, parent_config_name, description, rebuild)
        raise NotImplemented

    def add_rebuild_save_mark(self, which_configurations, config_names):
        """
        Adds marks indicating whether the specified configurations need to be rebuilt and their configuration data saved
        every time the model document is saved.
        :param which_configurations: One of the following options in swInConfigurationOpts_e:
            swAllConfiguration
            swSpecifyConfiguration
            swThisConfiguration
            swSpeedpakConfiguration
        :param config_names: Array of configuration names to which to apply the mark; valid only if WhichConfigurations
        is set to swInConfigurationOpts_e.swSpecifyConfiguration
		"""
        # return self._instance.AddRebuildSaveMark(which_configurations, config_names)
        raise NotImplemented

    def add_speed_pak(self, type, part_threshold):
        """
        Creates a SpeedPak configuration that includes all faces and the specified threshold of parts or bodies for the
        active assembly configuration.
        :param type: Selection type:
            1 = Geometry
            2 = Graphics
        :param part_threshold:  1.0 >= Double value for part or body selection threshold >= 0.0; 1.0 selects nothing,
        and 0.0 selects all (see Remarks)
        """
        # return self._instance.AddSpeedPak2(type, part_threshold)
        raise NotImplemented

    def get_configuration_params(self, config_name, params, values):
        """
        Gets the parameters for this configuration.
        :param config_name: Name of the configuration
        :param params: Array of the names of the parameters for this configuration
        :param values: Array of values of the parameters for this configuration
        """
        # return self._instance.GetConfigurationParams(config_name, params, values)
        raise NotImplemented

    def get_configuration_params_count(self, config_name):
        """
        Gets the number of parameters for this configuration.
        :param config_name: Name of the configuration
        """
        # return self._instance.GetConfigurationParamsCount(config_name)
        raise NotImplemented

    def i_get_configuration_params(self, config_name, param_count, param_names, param_values):
        """
        Gets the parameters for this configuration.
        :param config_name: Name of the configuration
        :param param_count: Number of parameters for this configuration
        :param param_names: in-process, unmanaged C++: Pointer to an array of the names of the parameters for this
        configuration of size ParamCount
        VBA, VB.NET, C#, and C++/CLI: Not supported
        See In-process Methods for details about this type of method.
        :param param_values: in-process, unmanaged C++: Pointer to an array of values of the parameters for this
        configuration of size ParamCount
        VBA, VB.NET, C#, and C++/CLI: Not supported
        See In-process Methods for details about this type of method.
        """
        # return self._instance.IGetConfigurationParams(config_name, param_count, param_names, param_values)
        raise NotImplemented

    def i_set_configuration_params(self, config_name, param_count, param_names, param_values):
        """
        Sets the parameters for this configuration.
        :param config_name: Name of the configuration
        :param param_count: Number of parameters
        :param param_names: in-process, unmanaged C++: Pointer to an array of the names of the parameters for this
        configuration of size ParamCount
        VBA, VB.NET, C#, and C++/CLI: Not supported
        See In-process Methods for details about this type of method.
        :param param_values: in-process, unmanaged C++: Pointer to an array of values for the parameters for this
        configuration of size ParamCount
        VBA, VB.NET, C#, and C++/CLI: Not supported
        See In-process Methods for details about this type of method.
        """
        # return self._instance.ISetConfigurationParams(config_name, param_count, param_names, param_values)
        raise NotImplemented

    def remove_mark_for_all_configurations(self):
        """Remove all marks indicating whether configurations need to be rebuilt and their configuration data saved
        every time the model document is saved."""
        # return self._instance.RemoveMarkForAllConfigurations
        raise NotImplemented

    def set_configuration_params(self, config_name, param_names, param_values):
        """
        Sets the parameters for this configuration.
        :param config_name: Name of the configuration
        :param param_names: Array of the names of the parameters for this configuration
        :param param_values: Array of values for the parameters for this configuration
        """
        # return self._instance.SetConfigurationParams(config_name, param_names, param_values)
        raise NotImplemented

    def set_expanded(self, which_pane, expand):
        """
        Sets whether to display and expand all of the configuration nodes in the specified pane of the ConfigurationManager.
        :param which_pane: Display pane as defined in swFeatMgrPane_e:
        swFeatMgrPaneTop
        swFeatMgrPaneBottom
        :param expand: True to expand all of the nodes, false to collapse them
        """
        # return self._instance.SetExpanded(which_pane, expand)
        raise NotImplemented

    def sort_configuration_tree(self, in_sel_type):
        """
        Specifies the order in which to list configurations in the ConfigurationManager.
        :param in_sel_type: Order in which to list configurations in the ConfigurationManager as defined in
        swConfigTreeSortType_e
        """
        # return self._instance.SortConfigurationTree(in_sel_type)
        raise NotImplemented
