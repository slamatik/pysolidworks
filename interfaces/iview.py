# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html
# todo
class IView:
    def __init__(self, system_object=None):
        self._instance = system_object

    def get_name(self):
        return self._instance.GetName2