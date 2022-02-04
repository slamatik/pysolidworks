# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.html
class IUserUnit:
	def __init__(self, parent=None):
		self._instance = parent

	def display_leading_zero(self):
		"""Gets whether to display leading zeroes."""
		# return self._instance.DisplayLeadingZero
		raise NotImplemented

	def fraction_base(self):
		"""Gets the fraction base."""
		# return self._instance.FractionBase
		raise NotImplemented

	def fraction_value(self):
		"""Gets the denominator value of the fraction."""
		# return self._instance.FractionValue
		raise NotImplemented

	def pad_zero(self):
		"""Gets whether to pad with zeroes."""
		# return self._instance.PadZero
		raise NotImplemented

	def round_to_fraction(self):
		"""Gets whether to round to a fraction."""
		# return self._instance.RoundToFraction
		raise NotImplemented

	def separator_character(self):
		"""Gets the decimal separator character."""
		# return self._instance.SeparatorCharacter
		raise NotImplemented

	def significant_digits(self):
		"""Gets the number of significant digits."""
		# return self._instance.SignificantDigits
		raise NotImplemented

	def specific_unit_type(self):
		"""Gets the specific unit type for this user unit."""
		# return self._instance.SpecificUnitType
		raise NotImplemented

	def unit_type(self):
		"""Gets the user unit type."""
		# return self._instance.UnitType
		raise NotImplemented

	def convert_double_to_system_value(self, user_value):
		"""
		Converts a double value to a document unit value.
		:param user_value: Value to convert
		"""
		# return self._instance.ConvertDoubleToSystemValue(user_value)
		raise NotImplemented

	def convert_to_system_value(self, unit_text, computed_value):
		"""
		Converts a text string to a document unit value.
		:param unit_text: Value to convert
		:param computed_value: Converted value in document units
		"""
		# return self._instance.ConvertToSystemValue(unit_text, computed_value)
		raise NotImplemented

	def convert_to_user_unit(self, value_in, show_usernames, name_in_english):
		"""
		Converts the input value to document units.
		:param value_in: Value to convert
		:param show_usernames: True to show the user names, false to not
		:param name_in_english: True to return the name in English, false to not
		"""
		# return self._instance.ConvertToUserUnit(value_in, show_usernames, name_in_english)
		raise NotImplemented

	def get_conversion_factor(self):
		"""Gets the conversion factor."""
		# return self._instance.GetConversionFactor
		raise NotImplemented

	def get_full_unit_name(self, plural):
		"""
		Gets the full name of the unit.
		:param plural: True if the name of the unit is plural, false if not
		"""
		# return self._instance.GetFullUnitName(plural)
		raise NotImplemented

	def get_units_string(self, in_english):
		"""
		Gets the string that describes the unit.
		:param in_english: True to return the string in English, false to not
		"""
		# return self._instance.GetUnitsString(in_english)
		raise NotImplemented

	def get_user_angle_tolerance(self):
		"""Gets the value of the angle tolerance for an angle unit."""
		# return self._instance.GetUserAngleTolerance
		raise NotImplemented

	def is_metric(self):
		"""Gets whether the unit is metric."""
		# return self._instance.IsMetric
		raise NotImplemented

