class ITextFormat:
    def __init__(self, parent):
        self._instance = parent

    @property
    def backwards(self):
        return self._instance.BackWards

    @backwards.setter
    def backwards(self, value):
        self._instance.BackWards = value

    @property
    def bold(self):
        return self._instance.Bold

    @bold.setter
    def bold(self, value):
        self._instance.Bold = value

    @property
    def type_face_name(self):
        return self._instance.TypeFaceName

    @type_face_name.setter
    def type_face_name(self, value):
        self._instance.TypeFaceName = value