from interfaces.irevisiontableannotation import IRevisionTableAnnotation
from interfaces.ititleblock import ITitleBlock
from interfaces.itableanchor import ITableAnchor
from interfaces.ipagesetup import IPageSetup
from interfaces.isketch import ISketch
from interfaces.iview import IView
from enums import TableAnnotation
import win32com.client as win32
import pythoncom


# http://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html

class ISheet:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def custom_property_view(self):
        return self._instance.CustomPropertyView

    @custom_property_view.setter
    def custom_property_view(self, value):
        self._instance.CustomPropertyView = value

    @property
    def page_setup(self):
        return IPageSetup(self._instance)

    @property
    def revision_table(self):
        return IRevisionTableAnnotation(self._instance.RevisionTable)

    @property
    def table_anchor(self, table_type):
        return ITableAnchor(self._instance, table_type)

    @property
    def title_block(self):
        return ITitleBlock(self._instance)

    def get_drawing_zone(self, x, y):
        return self._instance.GetDrawingZone(x, y)

    def get_id(self):
        return self._instance.GetID

    def get_magnetic_lines(self):
        return self._instance.GetMagneticLines

    def get_magnetic_lines_count(self):
        return self._instance.GetMagneticLinesCount

    def get_name(self):
        return self._instance.GetName

    def get_properties(self):
        # paperSize, templateIn, scale1, scale2, firstAngle, width, height, sameCustomProp
        return self._instance.GetProperties2

    def get_sheet_format_name(self):
        return self._instance.GetSheetFormatName

    def get_size(self):
        width = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        height = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        self._instance.GetSize(width, height)
        return width.value, height.value

    def get_template_name(self):
        return self._instance.GetTemplateName

    def get_template_sketch(self):
        return ISketch(self._instance.GetTemplateSketch)

    def get_views(self):
        return [IView(i) for i in self._instance.GetViews]

    def insert_revision_table(self, use_anchor_point=True, x=0.01, y=0.01, anchor_type=3,
                              table_template=r"M:\DESIGN\Solidworks Templates\revision table template 2021.sldrevtbt",
                              shape=1, auto_update_zone_cells=False):
        # todo
        return IRevisionTableAnnotation(self._instance.InsertRevisionTable2(use_anchor_point, x, y, anchor_type,
                                                                            table_template, shape,
                                                                            auto_update_zone_cells))

    def reload_template(self, keep_note_changes=True):
        return self._instance.ReloadTemplate(keep_note_changes)

    def save_format(self, file_name):
        # return self._instance.SaveFormat(file_name)
        pass

    # def get_zone_margin(self, zone_margin):
    #     pass
    #     # zone_margin = win32.VARIANT(pythoncom.VT_I4, zone_margin)
    #     # self._instance.GetZoneMargin(zone_margin)
    #     # return zone_margin
    #     # 2022

    # def get_zone_size_distribution(self):
    #     pass
    #     # row = win32.VARIANT(pythoncom.VT_I4, 0)
    #     # col = win32.VARIANT(pythoncom.VT_I4, 0)
    #     # self._instance.GetZoneSizeDistribution(row, col)
    #     # return row, col
    #     # 2022
    def set_name(self, name):
        self._instance.SetName(name)

    def set_properties(self, paper_size, template, s1, s2, first_angle, width, height, same=True):
        self._instance.SetProperties2(paper_size, template, s1, s2, first_angle, width, height, same)

    def set_scale(self, numerator, denominator, scale_anno_position, scale_anno_text_height):
        return self._instance.SetScale(numerator, denominator, scale_anno_position, scale_anno_text_height)

    def set_sheet_format_name(self, name):
        return self._instance.SetSheetFormatName(name)

    def set_size(self, size=6, width=0.5, height=0.25):
        # todo needs looking at
        return self._instance.SetSize(size, width, height)

    def set_template_name(self, name_in):
        self._instance.SetTemplateName(name_in)
