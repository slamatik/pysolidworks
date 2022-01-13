from interfaces.irevisiontableannotation import IRevisionTableAnnotation
from interfaces.ititleblock import ITitleBlock
from interfaces.itableanchor import ITableAnchor
from interfaces.ipagesetup import IPageSetup
from enums import TableAnnotation
import win32com.client as win32
import pythoncom


class ISheet:
    def __init__(self, parent=None):
        self._instance = parent.GetCurrentSheet

    def page_setup(self):
        return IPageSetup(self._instance)
        # pass  # todo IPageSetup
        # return self._instance.PageSetup

    def revision_table(self):
        return IRevisionTableAnnotation(self._instance)

    def table_anchor(self, table_type):
        # todo
        return ITableAnchor(self._instance, table_type)

    def title_block(self):
        return ITitleBlock(self._instance)

    def get_drawing_zone(self, x, y):
        return self._instance.GetDrawingZone(x, y)

    @property
    def get_id(self):
        return self._instance.GetID

    @property
    def get_name(self):
        return self._instance.GetName

    @property
    def get_properties(self):
        # paperSize, templateIn, scale1, scale2, firstAngle, width, height, sameCustomProp
        return self._instance.GetProperties2

    @property
    def get_sheet_format_name(self):
        return self._instance.GetSheetFormatName

    @property
    def get_size(self):
        # todo
        x, y = float(), float()
        # x = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I8, None)
        # y = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I8, None)
        data = self._instance.GetSize(x, y)
        return data

    @property
    def get_template_name(self):
        return self._instance.GetTemplateName

    @property
    def get_template_sketch(self):
        # todo ISketch
        return self._instance.GetTemplateSketch

    def get_views(self):
        # todo [IView]
        return self._instance.GetViews

    def set_name(self, name):
        self._instance.SetName(name)
