class ConfigurationManager:
    def __init__(self, parent):
        self._instance = parent.ConfigurationManager

    @property
    def active_configuration(self):
        # return self._instance.ActiveConfiguration todo neew interface IConiguration
        pass

    def add_configuration(self):
        pass
