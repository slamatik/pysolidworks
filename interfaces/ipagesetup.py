# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPageSetup_members.html
class IPageSetup:
    def __init__(self, parent=None):
        self._instance = parent.PageSetup

    @property
    def center_footer(self):
        """Gets or sets the page footer in the center of the page."""
        return self._instance.CenterFooter

    @center_footer.setter
    def center_footer(self, value):
        """Gets or sets the page footer in the center of the page."""
        self._instance.CenterFooter = value

    @property
    def center_header(self):
        """Gets or sets the page header in the center of the page."""
        return self._instance.CenterHeader

    @center_header.setter
    def center_header(self, value):
        """Gets or sets the page header in the center of the page."""
        self._instance.CenterHeader = value

    def drawing_color(self, value):
        """Sets the color of the drawing for printing."""
        return self._instance.DrawingColor(value)

    @property
    def footer_text_format(self):
        """Gets or sets the text format for the page footer."""
        return self._instance.FooterTextFormat

    @footer_text_format.setter
    def footer_text_format(self, value):
        """Gets or sets the text format for the page footer."""
        self._instance.FooterTextFormat = value

    def header_text_format(self):
        """Gets or sets the text format for the page header."""
        # return self._instance.HeaderTextFormat
        raise NotImplemented

    def high_quality(self):
        """Gets or sets whether to print a drawing in high quality."""
        # return self._instance.HighQuality
        raise NotImplemented

    def left_footer(self):
        """Gets or sets the page footer on the left side of the page."""
        # return self._instance.LeftFooter
        raise NotImplemented

    def left_header(self):
        """Gets or sets the page header on the left side of the page."""
        # return self._instance.LeftHeader
        raise NotImplemented

    def orientation(self):
        """Gets or sets the page orientation."""
        # return self._instance.Orientation
        raise NotImplemented

    def printer_paper_length(self):
        """Gets or sets the user-defined printer paper length for this document or sheet."""
        # return self._instance.PrinterPaperLength
        raise NotImplemented

    def printer_paper_size(self):
        """Gets or sets the printer paper size for this document or sheet."""
        # return self._instance.PrinterPaperSize
        raise NotImplemented

    def printer_paper_source(self):
        """Gets or sets the printer paper source for this document or sheet."""
        # return self._instance.PrinterPaperSource
        raise NotImplemented

    def printer_paper_width(self):
        """Gets or sets the user-defined printer paper width for this document or sheet."""
        # return self._instance.PrinterPaperWidth
        raise NotImplemented

    def right_footer(self):
        """Gets or sets the page footer on the right side of the page."""
        # return self._instance.RightFooter
        raise NotImplemented

    def right_header(self):
        """Gets or sets the page header on the right side of the page."""
        # return self._instance.RightHeader
        raise NotImplemented

    def scale(self):
        """Gets or sets the scale for printing the page."""
        # return self._instance.Scale2
        raise NotImplemented

    def scale_draft_edges(self):
        """Gets or sets whether to scale draft edges when printing a drawing in high quality."""
        # return self._instance.ScaleDraftEdges
        raise NotImplemented

    def scale_to_fit(self):
        """Enables or disables scaling the page to fit the printer."""
        # return self._instance.ScaleToFit
        raise NotImplemented

    def get_header_footer_string(self, which_one):
        """
        Gets the specified standard string that can be used in headers and footers.
        :param which_one: Type of string as defined in swStandardHeaderFooterPageSetupTexts_e
        """
        # return self._instance.GetHeaderFooterString(which_one)
        raise NotImplemented

    def get_resolution(self):
        """Gets the current printer resolution on documents and drawing sheets."""
        # return self._instance.GetResolution
        raise NotImplemented

    def get_use_default_resolution(self):
        """Gets whether the printer default resolution is in use on documents and drawing sheets."""
        # return self._instance.GetUseDefaultResolution
        raise NotImplemented

    def set_footer(self, left, center, right):
        """
        Sets the entire page footer.
        :param left: Left-footer text
        :param center: Center-footer text
        :param right: Right-footer text
        """
        # return self._instance.SetFooter(left, center, right)
        raise NotImplemented

    def set_header(self, left, center, right):
        """
        Sets the entire page header.
        :param left: Left-header text
        :param center: Center-header text
        :param right: Right-header text
        """
        return self._instance.SetHeader(left, center, right)

    def set_resolution(self, use_default, d_p_i):
        """
        Sets the current printer resolution on documents and drawing sheets.
        :param use_default: True to use the default printer resolution, false to set the printer resolution
        :param d_p_i: Dots per inch
        """
        # return self._instance.SetResolution(use_default, d_p_i)
        raise NotImplemented
