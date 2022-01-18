from interfaces.isheet import ISheet


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html

class IDrawingDoc:
    def __init__(self, system_object):
        self.system_object = system_object

    @property
    def _instance(self):
        return self.system_object

    @property
    def active_drawing_view(self):
        return self._instance.ActiveDrawingView

    def sheet(self, name):
        return ISheet(self._instance.Sheet(name))

    def get_current_sheet(self):
        return ISheet(self._instance.GetCurrentSheet)

    def activate_view(self, view_name):
        return self._instance.ActivateView(view_name)

    def create_text(self, text, x, y, z, height, angle):
        return self._instance.CreateText2(text, x, y, z, height, angle)

    def feature_by_name(self, name):
        return self._instance.FeatureByName(name)

    def setup_sheet(self, name, paper_size, template_in, scale1, scale2, first_angle, template_name, width, height,
                    property_view_name, remove_modified_notes, zone_left_margin, zone_right_margin, zone_top_margin,
                    zone_bottom_margin, zone_row, zone_col):
        """

        :param name:
        :param paper_size:
        :param template_in:
        :param scale1:
        :param scale2:
        :param first_angle:
        :param template_name:
        :param width:
        :param height:
        :param property_view_name:
        :param remove_modified_notes:
        :param zone_left_margin:
        :param zone_right_margin:
        :param zone_top_margin:
        :param zone_bottom_margin:
        :param zone_row:
        :param zone_col:
        :return:
        """
        return self._instance.SetupSheet6(name, paper_size, template_in, scale1, scale2, first_angle, template_name,
                                          width,
                                          height, property_view_name, remove_modified_notes, zone_left_margin,
                                          zone_right_margin, zone_top_margin, zone_bottom_margin, zone_row, zone_col)
