import interfaces.itextformat
import win32com.client as win32
import pythoncom


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html


class ITableAnnotation:
    def __init__(self, parent):
        self._instance = parent

    def text(self, row, column, include_hidden=True, value=None):
        if value:
            self._instance.Text2(row, column, include_hidden, win32.VARIANT(pythoncom.VT_BSTR, value))
        else:
            return self._instance.Text2(row, column)

    @property
    def title(self):
        return self._instance.Title

    def get_cell_text_format(self, row, column):
        return interfaces.itextformat.ITextFormat(self._instance.GetCellTextFormat(row, column))

    def set_cell_text_format(self, row, column, use_doc, text_format):
        arg1 = win32.VARIANT(pythoncom.VT_I4, row)
        arg2 = win32.VARIANT(pythoncom.VT_I4, column)
        arg3 = win32.VARIANT(pythoncom.VT_BOOL, use_doc)
        # arg4 = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_DISPATCH, win32.Dispatch(text_format))
        arg4 = win32.VARIANT(pythoncom.VT_RECORD, text_format)
        # return self._instance.SetCellTextFormat(row, column, use_doc, text_format)
        print(arg1, arg2, arg3, arg4)
        self._instance.SetCellTextFormat(arg1, arg2, arg3, arg4)
        return # todo

    def get_text_format(self):
        return interfaces.itextformat.ITextFormat(self._instance.GetTextFormat)
