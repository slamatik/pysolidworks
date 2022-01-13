import win32com.client as win32
import pythoncom
from interfaces.inote import INote


class ITitleBlock:
    def __init__(self, parent=None):
        self._instance = parent.TitleBlock

    def get_extents(self):
        x0 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        y0 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        x1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        y1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, None)
        # x0 = win32.VARIANT(pythoncom.VT_INT_PTR, None) todo IDK
        # y0 = win32.VARIANT(pythoncom.VT_INT_PTR, None)
        # x1 = win32.VARIANT(pythoncom.VT_INT_PTR, None)
        # y1 = win32.VARIANT(pythoncom.VT_INT_PTR, None)
        asd = self._instance.GetExtents(x0, y0, x1, y1)
        return x0, y0, x1, y1

    def get_feature(self):
        # todo IFeature
        return self._instance.GetFeature

    def get_note_count(self):
        return self._instance.GetNoteCount

    def get_notes(self):
        notes = self._instance.GetNotes
        # notes = [INote(note) for note in notes] #todo needs looking at
        return notes

    def set_extents(self):
        pass
