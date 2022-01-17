# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup.html

class IPageSetup:
    # todo
    def __init__(self, parent=None):
        self._instance = parent.PageSetup

    def footer_text_format(self):
        return self._instance.FooterTextFormat

    def set_header(self, left, center, right):
        return self._instance.SetHeader(left, center, right)
