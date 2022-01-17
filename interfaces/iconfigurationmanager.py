from interfaces.iconfiguration import IConfiguration


# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfigurationManager.html

class IConfigurationManager:
    def __init__(self, parent):
        self._instance = parent.ConfigurationManager

    @property
    def show_configuration_names(self):
        return self._instance.ShowConfigurationNames

    @show_configuration_names.setter
    def show_configuration_names(self, state):
        self._instance.ShowConfigurationNames = state

    @property
    def show_configuration_description(self):
        return self._instance.ShowConfigurationDescriptions

    @show_configuration_description.setter
    def show_configuration_description(self, state):
        self._instance.ShowConfigurationDescriptions = state

    @property
    def active_configuration(self):
        return IConfiguration(self._instance)

    def add_configuration(self):
        pass

    def add_rebuild_save_mark(self, which_configuration, config_name=None):
        # http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~AddRebuildSaveMark.html
        self._instance.AddRebuildSaveMark(which_configuration, config_name)

    def get_configuration_params_count(self, config_name):
        return self._instance.GetConfigurationParamsCount(config_name)

    def remove_mark_for_all_configuration(self):
        return self._instance.RemoveMarkForAllConfigurations

    def sort_configuration_tree(self, order):
        # http://help.solidworks.com/2021/english/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigTreeSortType_e.html
        self._instance.SortConfigurationTree(order)
