from interfaces.idrawingdoc import IDrawingDoc
from .modeldoc import ModelDoc


class DrawingDoc(IDrawingDoc, ModelDoc):
    def __init__(self, system_object):
        super().__init__(system_object)
