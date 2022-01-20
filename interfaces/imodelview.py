# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.html


class IModelView:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def camera(self):
        # todo ICamera
        return self._instance.Camera

    @camera.setter
    def camera(self, value):
        pass

    @property
    def display_mode(self):
        return self._instance.DisplayMode

    @display_mode.setter
    def display_mode(self, value):
        # todo
        self._instance.DisplayMode = value

