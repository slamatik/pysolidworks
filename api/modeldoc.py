from interfaces.imodeldoc2 import IModelDoc


class ModelDoc(IModelDoc):
    def __init__(self, system_object=None):
        super().__init__(system_object)
