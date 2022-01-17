from com import Com
from .iconfigurationmanager import IConfigurationManager
from .imodeldocextension import IModelDocExtension
from .ifeaturemanager import IFeatureManager
import win32com.client as win32
import pythoncom


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html

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
        return IConfigurationManager(self._instance())

    @property
    def extension(self):
        return IModelDocExtension(self._instance())

    @property
    def feature_manager(self):
        return IFeatureManager(self._instance())

    @property
    def length_unit(self):
        return self._instance().LengthUnit

    def get_path_name(self):
        return self._instance().GetPathName

    def get_title(self):
        return self._instance().GetTitle

    def save(self, options=1):
        arg1 = win32.VARIANT(pythoncom.VT_I4, options)
        arg2 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        arg3 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        self._instance().Save3(arg1, arg2, arg3)
        return arg2.value, arg3.value