# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutVariable_members.html
class ICalloutVariable:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def fit_display_style(self):
		"""Gets or sets how fit tolerance is displayed in a hole callout."""
		return self._instance.FitDisplayStyle

	@fit_display_style.setter
	def fit_display_style(self, value):
		"""Gets or sets how fit tolerance is displayed in a hole callout."""
		self._instance.FitDisplayStyle = value

	@property
	def fit_text_height(self):
		"""Gets or sets the height of the fit tolerance font in a hole callout."""
		return self._instance.FitTextHeight

	@fit_text_height.setter
	def fit_text_height(self, value):
		"""Gets or sets the height of the fit tolerance font in a hole callout."""
		self._instance.FitTextHeight = value

	@property
	def fit_text_scale(self):
		"""Gets or sets the value with which to scale the fit tolerance font in a hole callout."""
		return self._instance.FitTextScale

	@fit_text_scale.setter
	def fit_text_scale(self, value):
		"""Gets or sets the value with which to scale the fit tolerance font in a hole callout."""
		self._instance.FitTextScale = value

	@property
	def fit_type(self):
		"""Gets or sets the fit type for this hole callout."""
		return self._instance.FitType

	@fit_type.setter
	def fit_type(self, value):
		"""Gets or sets the fit type for this hole callout."""
		self._instance.FitType = value

	@property
	def fit_use_text_scale(self):
		"""Gets or sets whether to use the fit tolerance font scale value in a hole callout."""
		return self._instance.FitUseTextScale

	@fit_use_text_scale.setter
	def fit_use_text_scale(self, value):
		"""Gets or sets whether to use the fit tolerance font scale value in a hole callout."""
		self._instance.FitUseTextScale = value

	@property
	def hole_fit(self):
		"""Gets or sets the fit tolerance in a hole callout."""
		return self._instance.HoleFit

	@hole_fit.setter
	def hole_fit(self, value):
		"""Gets or sets the fit tolerance in a hole callout."""
		self._instance.HoleFit = value

	@property
	def shaft_fit(self):
		"""Gets or sets the shaft fit tolerance in a hole callout."""
		return self._instance.ShaftFit

	@shaft_fit.setter
	def shaft_fit(self, value):
		"""Gets or sets the shaft fit tolerance in a hole callout."""
		self._instance.ShaftFit = value

	@property
	def show_parenthesis(self):
		"""Gets or sets whether to show parentheses around linear tolerance dimensions in a hole callout."""
		return self._instance.ShowParenthesis

	@show_parenthesis.setter
	def show_parenthesis(self, value):
		"""Gets or sets whether to show parentheses around linear tolerance dimensions in a hole callout."""
		self._instance.ShowParenthesis = value

	@property
	def text_height(self):
		"""Gets or sets the height of the tolerance text in a hole callout."""
		return self._instance.TextHeight

	@text_height.setter
	def text_height(self, value):
		"""Gets or sets the height of the tolerance text in a hole callout."""
		self._instance.TextHeight = value

	@property
	def text_scale(self):
		"""Gets or sets the value with which to scale the tolerance font for a hole callout."""
		return self._instance.TextScale

	@text_scale.setter
	def text_scale(self, value):
		"""Gets or sets the value with which to scale the tolerance font for a hole callout."""
		self._instance.TextScale = value

	@property
	def tolerance_max(self):
		"""Gets or sets the maximum tolerance for a hole callout."""
		return self._instance.ToleranceMax

	@tolerance_max.setter
	def tolerance_max(self, value):
		"""Gets or sets the maximum tolerance for a hole callout."""
		self._instance.ToleranceMax = value

	@property
	def tolerance_min(self):
		"""Gets or sets the minimum tolerance for a hole callout."""
		return self._instance.ToleranceMin

	@tolerance_min.setter
	def tolerance_min(self, value):
		"""Gets or sets the minimum tolerance for a hole callout."""
		self._instance.ToleranceMin = value

	@property
	def tolerance_type(self):
		"""Gets or sets the type of tolerance for a hole callout."""
		return self._instance.ToleranceType

	@tolerance_type.setter
	def tolerance_type(self, value):
		"""Gets or sets the type of tolerance for a hole callout."""
		self._instance.ToleranceType = value

	@property
	def type(self):
		"""Gets the type of general hole callout variable."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the type of general hole callout variable."""
		self._instance.Type = value

	@property
	def user_readable_variable_name(self):
		"""Gets the name of the hole callout variable as it appears in the Dimension PropertyManager page in the Callout value drop-down list box."""
		return self._instance.UserReadableVariableName

	@user_readable_variable_name.setter
	def user_readable_variable_name(self, value):
		"""Gets the name of the hole callout variable as it appears in the Dimension PropertyManager page in the Callout value drop-down list box."""
		self._instance.UserReadableVariableName = value

	@property
	def use_text_scale(self):
		"""Gets or sets whether to use the value with which to scale the tolerance text for a hole callout."""
		return self._instance.UseTextScale

	@use_text_scale.setter
	def use_text_scale(self, value):
		"""Gets or sets whether to use the value with which to scale the tolerance text for a hole callout."""
		self._instance.UseTextScale = value

	@property
	def variable_name(self):
		"""Gets the name of the hole callout variable as it appears in the Dimension PropertyManager page in the Dimension Text box."""
		return self._instance.VariableName

	@variable_name.setter
	def variable_name(self, value):
		"""Gets the name of the hole callout variable as it appears in the Dimension PropertyManager page in the Dimension Text box."""
		self._instance.VariableName = value

	@property
	def variable_type(self):
		"""Gets the type of specific hole callout variable."""
		return self._instance.VariableType

	@variable_type.setter
	def variable_type(self, value):
		"""Gets the type of specific hole callout variable."""
		self._instance.VariableType = value

