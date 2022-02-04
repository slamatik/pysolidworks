# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRoutingSettings_members.html
class IRoutingSettings:
	def __init__(self, parent=None):
		self._instance = parent

	def get_from_to_list_header_definitions(self, wire_name_hdr, from_ref_hdr, from_pin_hdr, from_partno_hdr, to_ref_hdr, to_pin_hdr, to_partno_hdr, cable_name_hdr, core_name_hdr, colour_hdr, wire_spec_hdr, other_attrib_hdr):
		"""
		Gets the headers from a routing from-to list.
		:param wire_name_hdr: Wire name header
		:param from_ref_hdr: "From" reference header
		:param from_pin_hdr: "From" pin header
		:param from_partno_hdr: "From" part number header
		:param to_ref_hdr: "To" reference header
		:param to_pin_hdr: "To" pin header
		:param to_partno_hdr: "To" part number header
		:param cable_name_hdr: Cable name header
		:param core_name_hdr: Core name header
		:param colour_hdr: Color header
		:param wire_spec_hdr: Wire specification header
		:param other_attrib_hdr: Miscellaneous header
		"""
		# return self._instance.GetFromToListHeaderDefinitions(wire_name_hdr, from_ref_hdr, from_pin_hdr, from_partno_hdr, to_ref_hdr, to_pin_hdr, to_partno_hdr, cable_name_hdr, core_name_hdr, colour_hdr, wire_spec_hdr, other_attrib_hdr)
		raise NotImplemented

	def get_routing_user_preference_double_value(self, user_preference_value):
		"""
		Gets the double value of the specified routing user preference.
		:param user_preference_value: User preference as defined in swUserPreferenceRoutingDouble_e
		"""
		# return self._instance.GetRoutingUserPreferenceDoubleValue(user_preference_value)
		raise NotImplemented

	def get_routing_user_preference_integer_value(self, user_preference_value):
		"""
		Gets the integer value of the specified routing user preference.
		:param user_preference_value: User preference as defined in swUserPreferenceRoutingInteger_e
		"""
		# return self._instance.GetRoutingUserPreferenceIntegerValue(user_preference_value)
		raise NotImplemented

	def get_routing_user_preference_string_value(self, user_preference, use_default_val):
		"""
		Gets the string value of the specified routing user preference.
		:param user_preference: User preference as defined in swUserPreferenceRoutingFileLocations_e
		:param use_default_val: True to use the default, false to not
		"""
		# return self._instance.GetRoutingUserPreferenceStringValue(user_preference, use_default_val)
		raise NotImplemented

	def get_routing_user_preference_toggle(self, user_preference_toggle):
		"""
		Gets whether the specified routing user preference is turned on.
		:param user_preference_toggle: User preference as defined in swUserPreferenceRoutingToggle_e
		"""
		# return self._instance.GetRoutingUserPreferenceToggle(user_preference_toggle)
		raise NotImplemented

	def load_default_routing_settings(self):
		"""Loads the default routing settings."""
		# return self._instance.LoadDefaultRoutingSettings
		raise NotImplemented

	def load_routing_settings_from_file(self, routing_settings_filename):
		"""
		Loads routing settings from the specified file.
		:param routing_settings_filename: 
Full path name of the .sqy file from which to load the routing settings
		"""
		# return self._instance.LoadRoutingSettingsFromFile(routing_settings_filename)
		raise NotImplemented

	def save_routing_settings_to_file(self, routing_settings_filename):
		"""
		Saves routing settings to the specified file.
		:param routing_settings_filename: Full path name of file to which to save routing settings; file name must have an extension of .sqy
		"""
		# return self._instance.SaveRoutingSettingsToFile(routing_settings_filename)
		raise NotImplemented

	def set_from_to_list_header_definitions(self, wire_name_hdr, from_ref_hdr, from_pin_hdr, from_partno_hdr, to_ref_hdr, to_pin_hdr, to_partno_hdr, cable_name_hdr, core_name_hdr, colour_hdr, wire_spec_hdr, other_attrib_hdr):
		"""
		Sets the headers in a routing from-to list.
		:param wire_name_hdr: Wire name header
		:param from_ref_hdr: "From" reference header
		:param from_pin_hdr: "From" pin header
		:param from_partno_hdr: "From" part number header
		:param to_ref_hdr: "To" reference header
		:param to_pin_hdr: "To" pin header
		:param to_partno_hdr: "To" part number header
		:param cable_name_hdr: Cable name header
		:param core_name_hdr: Core name header
		:param colour_hdr: Color header
		:param wire_spec_hdr: Wire specification header
		:param other_attrib_hdr: Miscellaneous header
		"""
		# return self._instance.SetFromToListHeaderDefinitions(wire_name_hdr, from_ref_hdr, from_pin_hdr, from_partno_hdr, to_ref_hdr, to_pin_hdr, to_partno_hdr, cable_name_hdr, core_name_hdr, colour_hdr, wire_spec_hdr, other_attrib_hdr)
		raise NotImplemented

	def set_routing_user_preference_double_value(self, user_preference_value, value):
		"""
		Sets a double value for the specified routing user preference.
		:param user_preference_value: User preference as defined in swUserPreferenceRoutingDouble_e
		:param value: Double value of the specified user preference
		"""
		# return self._instance.SetRoutingUserPreferenceDoubleValue(user_preference_value, value)
		raise NotImplemented

	def set_routing_user_preference_integer_value(self, user_preference_value, value):
		"""
		Sets an integer value for the specified routing user preference.
		:param user_preference_value: User preference as defined in swUserPreferenceRoutingInteger_e
		:param value: Integer value of the specified user preference
		"""
		# return self._instance.SetRoutingUserPreferenceIntegerValue(user_preference_value, value)
		raise NotImplemented

	def set_routing_user_preference_string_value(self, user_preference, value):
		"""
		Sets a string value for the specified routing user preference.
		:param user_preference: User preference as defined in swUserPreferenceRoutingFileLocations_e
		:param value: String value of the specified user preference
		"""
		# return self._instance.SetRoutingUserPreferenceStringValue(user_preference, value)
		raise NotImplemented

	def set_routing_user_preference_toggle(self, user_preference_value, on_flag):
		"""
		Sets whether the specified routing user preference is turned on or off.
		:param user_preference_value: User preference as defined in swUserPreferenceRoutingToggle_e
		:param on_flag: True to turn on, false to turn off
		"""
		# return self._instance.SetRoutingUserPreferenceToggle(user_preference_value, on_flag)
		raise NotImplemented

