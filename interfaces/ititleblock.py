import win32com.client as win32
import pythoncom
from interfaces.inote import INote
from interfaces.ifeature import IFeature


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock.html


class ITitleBlock:
    def __init__(self, parent=None):
        self._instance = parent.TitleBlock

    def get_extents(self):
        x0 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        y0 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        x1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        y1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        self._instance.GetExtents(x0, y0, x1, y1)
        return x0.value, y0.value, x1.value, y1.value

    def get_feature(self):
        return IFeature(self._instance)

    def get_note_count(self):
        return self._instance.GetNoteCount

    def get_notes(self):
        notes = self._instance.GetNotes
        notes = [INote(note) for note in notes]
        return notes

    def set_extents(self, x0, y0, x1=None, y1=None):
        current_coords = self.get_extents()
        x0 = x0 if x0 else current_coords[0]
        y0 = y0 if y0 else current_coords[1]
        x1 = x1 if x1 else current_coords[2]
        y1 = y1 if y1 else current_coords[3]
        x0 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, x0)
        y0 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, y0)
        x1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, x1)
        y1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, y1)
        self._instance.SetExtents(x0, y0, x1, y1)
