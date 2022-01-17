from interfaces.icustompropertymanager import ICustomPropertyManager
from enums import VisibilityState


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html


class IFeature:
    def __init__(self, parent=None):
        self._instance = parent.GetFeature

    @property
    def created_by(self):
        return self._instance.CreatedBy

    @property
    def custom_property_manager(self):
        raise NotImplemented

    @property
    def date_created(self):
        return self._instance.DateCreated

    @property
    def date_modified(self):
        return self._instance.DateModified

    @property
    def description(self):
        return self._instance.Description

    @description.setter
    def description(self, description):
        self._instance.Description = description

    @property
    def exclude_from_cut_list(self):
        return self._instance.ExcludeFromCutList

    @exclude_from_cut_list.setter
    def exclude_from_cut_list(self, state):
        self._instance.ExcludeFromCutList = state

    @property
    def name(self):
        return self._instance.Name

    @name.setter
    def name(self, name):
        self._instance.Name = name

    @property
    def visible(self):
        return VisibilityState(self._instance.Visible)
