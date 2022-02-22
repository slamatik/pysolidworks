import win32com.client as win32


# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextFormat_members.html


class ITextFormat:
    def __init__(self, parent=None):
        self._instance = parent

    @property
    def backwards(self):
        """Gets or sets whether the text is displayed backwards."""
        return self._instance.BackWards

    @backwards.setter
    def backwards(self, value: bool):
        """Gets or sets whether the text is displayed backwards."""
        self._instance.BackWards = value

    @property
    def bold(self):
        """Gets or sets the whether the text format is bold."""
        return self._instance.Bold

    @bold.setter
    def bold(self, value: bool):
        """Gets or sets the whether the text format is bold."""
        self._instance.Bold = value

    @property
    def char_height(self):
        """Gets or sets the height of the font in meters."""
        return self._instance.CharHeight

    @char_height.setter
    def char_height(self, value: int):
        """Gets or sets the height of the font in meters."""
        self._instance.CharHeight = value

    @property
    def char_height_in_pts(self):
        """Gets or sets the height of the font in points."""
        return self._instance.CharHeightInPts

    @char_height_in_pts.setter
    def char_height_in_pts(self, value):
        """Gets or sets the height of the font in points."""
        self._instance.CharHeightInPts = value

    @property
    def char_spacing_factor(self):
        """Gets or sets the factor that controls the spacing between characters."""
        return self._instance.CharSpacingFactor

    @char_spacing_factor.setter
    def char_spacing_factor(self, value: int):
        """Gets or sets the factor that controls the spacing between characters."""
        self._instance.CharSpacingFactor = value

    @property
    def escapement(self):
        """Gets or sets the text angle in radians. """
        return self._instance.Escapement

    @escapement.setter
    def escapement(self, value: int):
        """Gets or sets the text angle in radians. """
        self._instance.Escapement = value

    @property
    def italic(self):
        """Gets or sets the whether the text format is italic."""
        return self._instance.Italic

    @italic.setter
    def italic(self, value: bool):
        """Gets or sets the whether the text format is italic."""
        self._instance.Italic = value

    @property
    def line_length(self):
        """Gets or sets the text line length in meters."""
        return self._instance.LineSpacing

    @line_length.setter
    def line_length(self, value: int):
        """Gets or sets the text line length in meters."""
        self._instance.LineSpacing = value

    @property
    def line_spacing(self):
        """Gets or sets the text line spacing."""
        return self._instance.LineSpacing

    @line_spacing.setter
    def line_spacing(self, value: int):
        """Gets or sets the text line spacing."""
        self._instance.LineSpacing = value

    @property
    def oblique_angle(self):
        """Gets or sets the text slant."""
        return self._instance.ObliqueAngle

    @oblique_angle.setter
    def oblique_angle(self, value: int):
        """Gets or sets the text slant."""
        self._instance.ObliqueAngle = value

    @property
    def strikeout(self):
        """Gets or sets the whether the text format is strikeout."""
        return self._instance.Strikeout

    @strikeout.setter
    def strikeout(self, value: bool):
        """Gets or sets the whether the text format is strikeout."""
        self._instance.Strikeout = value

    @property
    def type_face_name(self):
        """Gets or sets the name of the font."""
        return self._instance.TypeFaceName

    @type_face_name.setter
    def type_face_name(self, value: str):
        """Gets or sets the name of the font."""
        self._instance.TypeFaceName = value

    @property
    def underline(self):
        """Gets or sets the whether the text format is underlined."""
        return self._instance.Underline

    @underline.setter
    def underline(self, value: int):
        """Gets or sets the whether the text format is underlined."""
        self._instance.Underline = value

    @property
    def upside_down(self):
        """Gets or sets whether the whole text string is upside down."""
        return self._instance.UpsideDown

    @upside_down.setter
    def upside_down(self, value: bool):
        """Gets or sets whether the whole text string is upside down."""
        self._instance.UpsideDown = value

    @property
    def vertical(self):
        """Gets or sets the individual characters as vertical."""
        return self._instance.Vertical

    @vertical.setter
    def vertical(self, value: int):
        """Gets or sets the individual characters as vertical."""
        self._instance.Vertical = value

    def width_factor(self, value: int):
        """Stretches the text by the specified factor."""
        self._instance.WidthFactor = value

    def is_height_specified_in_pts(self):
        """Gets whether the character height is in points or system units."""
        return self._instance.IsHeightSpecifiedInPts
