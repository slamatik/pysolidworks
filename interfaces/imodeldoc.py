from com import Com
from .iconfigurationmanager import ConfigurationManager
from .imodeldocextension import IModelDocExtension


class IModelDoc:
    def __init__(self, parent=None):
        self.parent = parent

    def _instance(self):
        if self.parent is not None:
            return self.parent
        else:
            return Com('SldWorks.Application').ActiveDoc

    @property
    def configuration_manager(self):
        return ConfigurationManager(self._instance())

    @property
    def extension(self):
        return IModelDocExtension(self._instance())

    @property
    def feature_manager(self):
        # return FeatureManager(self._instance())
        pass

    @property
    def length_unit(self):
        return self._instance().LengthUnit

    def get_path_name(self):
        return self._instance().GetPathName

    def get_title(self):
        return self._instance().GetTitle
