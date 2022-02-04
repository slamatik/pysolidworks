import win32com.client as win32
import pythoncom
from interfaces.inote import INote
from interfaces.ifeature import IFeature


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlock_members.html


class ITitleBlock:
    def __init__(self, parent=None):
        self._instance = parent.TitleBlock

    def get_extents(self):
        """Gets the coordinates on the drawing sheet format that define the extents of the title block."""
        x_upper_left = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        y_upper_left = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        x_lower_right = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        y_lower_right = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        self._instance.GetExtents(x_upper_left, y_upper_left, x_lower_right, y_lower_right)
        return x_upper_left.value, y_upper_left.value, x_lower_right.value, y_lower_right.value

    def get_feature(self):
        """Gets the feature for this title block."""
        return IFeature(self._instance)

    def get_note_count(self):
        """Gets the number of notes in this title block."""
        return self._instance.GetNoteCount

    def get_notes(self):
        """Gets the notes in this title block."""
        notes = self._instance.GetNotes
        notes = [INote(note) for note in notes]
        return notes

    def i_get_notes(self, count):
        """
        Gets the notes in this title block.
        :param count: Number of notes in this title block
        """
        # return self._instance.IGetNotes(count)
        raise NotImplemented

    def set_extents(self, x_upper_left, y_upper_left, x_lower_right, y_lower_right):
        """
        Sets the coordinates on the drawing sheet format that define the extens of the title blcok.
        :param x_upper_left: X upper-left coordinate
        :param y_upper_left: Y upper-left coordinate
        :param x_lower_right: X lower-right coordinate
        :param y_lower_right: Y lower-right coordinate
        """
        current_coords = self.get_extents()
        x0 = x_upper_left if x_upper_left else current_coords[0]
        y0 = y_upper_left if y_upper_left else current_coords[1]
        x1 = x_lower_right if x_lower_right else current_coords[2]
        y1 = y_lower_right if y_lower_right else current_coords[3]
        x0 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, x0)
        y0 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, y0)
        x1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, x1)
        y1 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, y1)
        self._instance.SetExtents(x0, y0, x1, y1)
