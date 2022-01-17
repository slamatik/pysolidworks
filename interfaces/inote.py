# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.html


class INote:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def all_upper_case(self):
        return self._instance.AllUpperCase

    @all_upper_case.setter
    def all_upper_case(self, state):
        self._instance.AllUpperCase = state

    @property
    def angle(self):
        return self._instance.Angle

    @angle.setter
    def angle(self, value):
        self._instance.Angle = value

    @property
    def prompt_text(self):
        return self._instance.PromptText

    @prompt_text.setter
    def prompt_text(self, value):
        self._instance.PromptText = value

    @property
    def property_linked_text(self):
        return self._instance.PropertyLinkedText

    @property
    def tag_name(self):
        return self._instance.TagName

    def get_annotation(self):
        pass  # todo IAnnotation

    def get_text(self):
        return self._instance.GetText

    def get_name(self):
        return self._instance.GetName
