from interfaces.isheet import ISheet


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html

class IDrawingDoc:
    def __init__(self, system_object):
        self.system_object = system_object

    @property
    def _instance(self):
        return self.system_object

    @property
    def active_drawing_view(self):
        return self._instance.ActiveDrawingView

    def get_current_sheet(self):
        return ISheet(self._instance)

    def activate_view(self, view_name):
        return self._instance.ActivateView(view_name)

    def create_text(self, text, x, y, z, height, angle):
        return self._instance.CreateText2(text, x, y, z, height, angle)

    def feature_by_name(self, name):
        return self._instance.FeatureByName(name)
