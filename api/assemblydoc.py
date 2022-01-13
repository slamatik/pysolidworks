from interfaces.iassemblydoc import IAssemblyDoc
from .modeldoc import ModelDoc


class AssemblyDoc(IAssemblyDoc, ModelDoc):
    def __init__(self, system_object):
        super().__init__(system_object)
