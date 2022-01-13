class IPageSetup:
    # No ideas
    def __init__(self, parent=None):
        self._instance = parent.PageSetup

    def footer_text_format(self):
        return self._instance.FooterTextFormat

    def set_header(self, left, center, right):
        return self._instance.SetHeader(left, center, right)