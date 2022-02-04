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
        """Gets or sets the drawing view to use to set the custom information for this drawing sheet."""
        return self._instance.CustomPropertyView

    @custom_property_view.setter
    def custom_property_view(self, value):
        """Gets or sets the drawing view to use to set the custom information for this drawing sheet."""
        self._instance.CustomPropertyView = value

    @property
    def focus_locked(self):
        """Gets or sets whether focus is locked on this sheet."""
        return self._instance.FocusLocked

    @focus_locked.setter
    def focus_locked(self, value):
        self._instance.FocusLocked = value

    @property
    def i_page_setup(self):
        """Gets the page setup for this sheet."""
        # return self._instance.IPageSetup
        raise NotImplemented

    @property
    def page_setup(self):
        return IPageSetup(self._instance)

    @property
    def revision_table(self):
        return IRevisionTableAnnotation(self._instance.RevisionTable)

    @property
    def sheet_format_visible(self):
        """Gets or sets whether the sheet format is currently visible in this drawing sheet."""
        return self._instance.SheetFormatVisible

    @sheet_format_visible.setter
    def sheet_format_visible(self, value):
        """Gets or sets whether the sheet format is currently visible in this drawing sheet."""
        self._instance.SheetFormatVisible = value

    def table_anchor(self, table_type):
        """
        Gets the specified table anchor.
        :param table_type: Table type as defined in swTableAnnotationType_e
        """
        return ITableAnchor(self._instance, table_type)

    @property
    def title_block(self):
        return ITitleBlock(self._instance)

    def get_drawing_zone(self, x, y):
        """
        Gets the name of the drawing zone for the specified x and y coordinates on the sheet.
        :param x: x coordinate
        :param y: y coordinate
        """
        return self._instance.GetDrawingZone(x, y)

    def get_id(self):
        """Gets the ID of this drawing sheet."""
        return self._instance.GetID

    def get_magnetic_lines(self):
        """Gets the magnetic lines on this drawing sheet."""
        return self._instance.GetMagneticLines

    def get_magnetic_lines_count(self):
        """Gets the number of magnetic lines on this drawing sheet."""
        return self._instance.GetMagneticLinesCount

    def get_name(self):
        """Gets the name of the sheet."""
        return self._instance.GetName

    def get_properties(self):
        """
        Gets the properties for this sheet.
        paperSize, templateIn, scale1, scale2, firstAngle, width, height, sameCustomProp
        """
        return self._instance.GetProperties2

    def get_sheet_format_name(self):
        """Gets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree."""
        return self._instance.GetSheetFormatName

    # def get_size(self, width, height):
    #     """ todo
    #     Gets the size of the sheet and the corresponding standard sheet size.
    #     :param width: Width of sheet
    #     :param height: Height of sheet
    #     """
    #     # return self._instance.GetSize(width, height)
    #     raise NotImplemented

    def get_size(self):
        width = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        height = win32.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_R8, None)
        self._instance.GetSize(width, height)
        return width.value, height.value

    def get_template_name(self):
        """Gets the name of the template used by this sheet."""
        return self._instance.GetTemplateName

    def get_template_sketch(self):
        """Gets the sheet format sketch for this drawing sheet."""
        return ISketch(self._instance.GetTemplateSketch)

    def get_views(self):
        """Gets the drawing views on this sheet."""
        return [IView(i) for i in self._instance.GetViews]

    def i_get_magnetic_lines(self, count):
        """
        Gets the magnetic lines on this drawing sheet.
        :param count: Number of magnetic lines returned by this method
        """
        # return self._instance.IGetMagneticLines(count)
        raise NotImplemented

    def insert_magnetic_line(self, start_point, end_point):
        """
        Inserts a magnetic line at the specified start and end points on this drawing sheet.
        :param start_point: IMathPoint
        :param end_point: IMathPoint
        """
        # return self._instance.InsertMagneticLine(start_point, end_point)
        raise NotImplemented

    def insert_revision_table(self, use_anchor_point=True, x=0.01, y=0.01, anchor_type=3,
                              table_template=r"M:\DESIGN\Solidworks Templates\revision table template 2021.sldrevtbt",
                              shape=1, auto_update_zone_cells=False):
        """
        Inserts a revision table in this drawing sheet.
        :param use_anchor_point: True to insert the revision table at the existing revision table anchor point, false to
        anchor the table at the point specified by X and Y
        :param x: X coordinate for the placement of the revision table annotation
        :param y: Y coordinate for the placement of this revision table annotation
        :param anchor_type: Anchor type as defined by swBOMConfigurationAnchorType_e
        :param table_template: Path and filename of the template that corresponds to this type of table (see Remarks)
        :param shape: Revision symbol shape as defined in swRevisionTableSymbolShape_e
        :param auto_update_zone_cells: True to automatically update zone cells, false to not
        """
        return IRevisionTableAnnotation(self._instance.InsertRevisionTable2(use_anchor_point, x, y, anchor_type,
                                                                            table_template, shape,
                                                                            auto_update_zone_cells))

    def insert_title_block(self, notes):
        """
        Inserts a title block into this drawing sheet.
        :param notes: Array of notes or nothing (see Remarks)
        """
        # return self._instance.InsertTitleBlock(notes)
        raise NotImplemented

    def is_loaded(self):
        """Gets whether this sheet is loaded."""
        # return self._instance.IsLoaded
        raise NotImplemented

    def reload_template(self, keep_note_changes=True):
        """
        Reloads the sheet format from the original sheet format template.
        :param keep_note_changes: True to keep note modifications made to the sheet format and reload all other elements
        from the original sheet format template, false to reload all elements from the original sheet format template
        and discard any note modifications made to the sheet format
        """
        return self._instance.ReloadTemplate(keep_note_changes)

    def save_format(self, file_name):
        """
        Saves the sheet format in the specified file.
        :param file_name: Path and file name to which to save the sheet format (see Remarks)
        """
        # return self._instance.SaveFormat(file_name)
        raise NotImplemented

    def set_as_table_anchor(self, table_type):
        """
        Sets the anchor for the specified table at a selected point in the sheet format.
        :param table_type: Table for which an anchor is required as defined in swTableAnnotationType_e
        """
        # return self._instance.SetAsTableAnchor(table_type)
        raise NotImplemented

    def set_name(self, name):
        """
        Sets the sheet name.
        :param name: Name for the sheet
        """
        self._instance.SetName(name)

    def set_properties(self, paper_size, template, s1, s2, first_angle, width, height, same=True):
        """
        Sets the properties for this sheet.
        :param paper_size: Paper size as defined in swDwgPaperSizes_e (see Remarks)
        :param template: Template as defined in swDwgTemplates_e (see Remarks)
        :param s1: Scale numerator (see Remarks)
        :param s2: Scale denominator (see Remarks)
        :param first_angle: True if you want first angle projection, false if not
        :param width: Custom paper width if PaperSz = swDwgPaperSizes_e.swDwgPaperUserDefined (see Remarks)
        :param height: Custom paper height if PaperSz = swDwgPaperSizes_e.swDwgPaperUserDefined (see Remarks)
        :param same: True to select the Same as sheet specified in Document Properties check box in the Sheet Properties
        dialog, false to not (see Remarks)
        """
        self._instance.SetProperties2(paper_size, template, s1, s2, first_angle, width, height, same)

    def set_scale(self, numerator, denominator, scale_anno_position, scale_anno_text_height):
        """
        Sets the scale for this drawing sheet.
        :param numerator: First value in the scale ratio (n : n)
        :param denominator: Second value in the scale ratio (n : n)
        :param scale_anno_position: True if the position of the annotations is scaled, false if not
        :param scale_anno_text_height: True if the text height of the annotations is scaled, false if not
        """
        return self._instance.SetScale(numerator, denominator, scale_anno_position, scale_anno_text_height)

    def set_sheet_format_name(self, name):
        """
        Sets the name of the sheet format of this drawing sheet, as displayed in the FeatureManager design tree.
        :param name: Name of the sheet format
        """
        return self._instance.SetSheetFormatName(name)

    def set_size(self, size=6, width=0.5, height=0.25):
        """
        Sets the standard sheet size and the size of the sheet so that the drawing looks correct.
        :param size: Paper size as defined in swDwgPaperSizes_e
        :param width: Width of sheet
        :param height: Height of sheet
        """
        # todo needs looking at
        return self._instance.SetSize(size, width, height)

    def set_template_name(self, name_in):
        """
        Sets the template name for the sheet format.
        :param name_in: Path name of the sheet format template
        """
        self._instance.SetTemplateName(name_in)
