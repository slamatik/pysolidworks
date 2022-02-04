# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimensionTolerance_members.html
class IDimensionTolerance:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def fit_display_style(self):
		"""Gets or sets how this dimension fit tolerance is displayed."""
		return self._instance.FitDisplayStyle

	@fit_display_style.setter
	def fit_display_style(self, value):
		"""Gets or sets how this dimension fit tolerance is displayed."""
		self._instance.FitDisplayStyle = value

	@property
	def fit_type(self):
		"""Gets or sets the fit type for this dimension fit tolerance."""
		return self._instance.FitType

	@fit_type.setter
	def fit_type(self, value):
		"""Gets or sets the fit type for this dimension fit tolerance."""
		self._instance.FitType = value

	@property
	def show_parenthesis(self):
		"""Indicates whether to show parentheses around linear tolerance dimensions."""
		return self._instance.ShowParenthesis

	@show_parenthesis.setter
	def show_parenthesis(self, value):
		"""Indicates whether to show parentheses around linear tolerance dimensions."""
		self._instance.ShowParenthesis = value

	@property
	def type(self):
		"""Gets or sets the type of tolerance."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of tolerance."""
		self._instance.Type = value

	@property
	def get_fit_font_height(self):
		"""Gets the height of the fit tolerance font."""
		return self._instance.GetFitFontHeight

	@get_fit_font_height.setter
	def get_fit_font_height(self, value):
		"""Gets the height of the fit tolerance font."""
		self._instance.GetFitFontHeight = value

	@property
	def get_fit_font_scale(self):
		"""Gets the ratio of the height of the fit tolerance font to the height of the dimension font."""
		return self._instance.GetFitFontScale

	@get_fit_font_scale.setter
	def get_fit_font_scale(self, value):
		"""Gets the ratio of the height of the fit tolerance font to the height of the dimension font."""
		self._instance.GetFitFontScale = value

	@property
	def get_fit_font_use_dimension(self):
		"""Gets whether the fit tolerance font is the same size as the dimension font."""
		return self._instance.GetFitFontUseDimension

	@get_fit_font_use_dimension.setter
	def get_fit_font_use_dimension(self, value):
		"""Gets whether the fit tolerance font is the same size as the dimension font."""
		self._instance.GetFitFontUseDimension = value

	@property
	def get_fit_font_use_scale(self):
		"""Gets whether the fit tolerance font size is scaled based on the dimension font size, or if it is an absolute height value."""
		return self._instance.GetFitFontUseScale

	@get_fit_font_use_scale.setter
	def get_fit_font_use_scale(self, value):
		"""Gets whether the fit tolerance font size is scaled based on the dimension font size, or if it is an absolute height value."""
		self._instance.GetFitFontUseScale = value

	@property
	def get_font_height(self):
		"""Gets the height of the tolerance font."""
		return self._instance.GetFontHeight

	@get_font_height.setter
	def get_font_height(self, value):
		"""Gets the height of the tolerance font."""
		self._instance.GetFontHeight = value

	@property
	def get_font_scale(self):
		"""Gets the ratio of the height of the tolerance font to the height of the dimension font."""
		return self._instance.GetFontScale

	@get_font_scale.setter
	def get_font_scale(self, value):
		"""Gets the ratio of the height of the tolerance font to the height of the dimension font."""
		self._instance.GetFontScale = value

	@property
	def get_font_use_dimension(self):
		"""Gets whether the tolerance font is the same size as the dimension font."""
		return self._instance.GetFontUseDimension

	@get_font_use_dimension.setter
	def get_font_use_dimension(self, value):
		"""Gets whether the tolerance font is the same size as the dimension font."""
		self._instance.GetFontUseDimension = value

	@property
	def get_font_use_scale(self):
		"""Gets whether the tolerance font size is scaled based on the dimension font size, or if it is an absolute height value."""
		return self._instance.GetFontUseScale

	@get_font_use_scale.setter
	def get_font_use_scale(self, value):
		"""Gets whether the tolerance font size is scaled based on the dimension font size, or if it is an absolute height value."""
		self._instance.GetFontUseScale = value

	@property
	def get_hole_fit_value(self):
		"""Gets the tolerance hole fit value."""
		return self._instance.GetHoleFitValue

	@get_hole_fit_value.setter
	def get_hole_fit_value(self, value):
		"""Gets the tolerance hole fit value."""
		self._instance.GetHoleFitValue = value

	@property
	def get_max_value(self):
		"""Gets the tolerance maximum value."""
		return self._instance.GetMaxValue2

	@get_max_value.setter
	def get_max_value(self, value):
		"""Gets the tolerance maximum value."""
		self._instance.GetMaxValue2 = value

	@property
	def get_min_value(self):
		"""Gets the tolerance minimum value."""
		return self._instance.GetMinValue2

	@get_min_value.setter
	def get_min_value(self, value):
		"""Gets the tolerance minimum value."""
		self._instance.GetMinValue2 = value

	@property
	def get_shaft_fit_value(self):
		"""Gets the tolerance shaft fit value."""
		return self._instance.GetShaftFitValue

	@get_shaft_fit_value.setter
	def get_shaft_fit_value(self, value):
		"""Gets the tolerance shaft fit value."""
		self._instance.GetShaftFitValue = value

	@property
	def set_fit_font(self):
		"""Sets the fit tolerance font values."""
		return self._instance.SetFitFont

	@set_fit_font.setter
	def set_fit_font(self, value):
		"""Sets the fit tolerance font values."""
		self._instance.SetFitFont = value

	@property
	def set_fit_values(self):
		"""Sets the tolerance hole fit and shaft fit values."""
		return self._instance.SetFitValues

	@set_fit_values.setter
	def set_fit_values(self, value):
		"""Sets the tolerance hole fit and shaft fit values."""
		self._instance.SetFitValues = value

	@property
	def set_font(self):
		"""Sets the tolerance font values."""
		return self._instance.SetFont

	@set_font.setter
	def set_font(self, value):
		"""Sets the tolerance font values."""
		self._instance.SetFont = value

	@property
	def set_values(self):
		"""Sets the tolerance minimum and maximum values of a dimension."""
		return self._instance.SetValues2

	@set_values.setter
	def set_values(self, value):
		"""Sets the tolerance minimum and maximum values of a dimension."""
		self._instance.SetValues2 = value

