# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch.html
# todo
class ISketch:
    def __init__(self, system_object=None):
        self._instance = system_object

    def is3d(self):
        return self._instance.Is3D