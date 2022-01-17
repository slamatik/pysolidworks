# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html


class IFeatureManager:
    def __init__(self, parent=None):
        self._instance = parent.FeatureManager

