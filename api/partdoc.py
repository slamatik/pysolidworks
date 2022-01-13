from interfaces.ipartdoc import IPartDoc
from .modeldoc import ModelDoc


class PartDoc(IPartDoc, ModelDoc):
    def __init__(self, system_object):
        super().__init__(system_object)
