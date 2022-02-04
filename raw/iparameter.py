# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.html
class IParameter:
	def __init__(self, parent=None):
		self._instance = parent

	def get_double_value(self):
		"""Gets an attribute value of type double."""
		# return self._instance.GetDoubleValue
		raise NotImplemented

	def get_name(self):
		"""Gets the name of this parameter."""
		# return self._instance.GetName
		raise NotImplemented

	def get_string_value(self):
		"""Gets an attribute value of type string."""
		# return self._instance.GetStringValue
		raise NotImplemented

	def get_type(self):
		"""Gets the type of data stored on the parameter."""
		# return self._instance.GetType
		raise NotImplemented

	def get_vector(self, x, y, z):
		"""
		Extracts information of type vector from a parameter.
		:param x: x vector value stored on the parameter
		:param y: y vector value stored on the parameter
		:param z: z vector value stored on the parameter
		"""
		# return self._instance.GetVector(x, y, z)
		raise NotImplemented

	def get_vector_v_b(self):
		"""Extracts information of type vector from a parameter."""
		# return self._instance.GetVectorVB
		raise NotImplemented

	def set_double_value(self, value, configuration_option, configuration_name):
		"""
		Sets the double or integer value of a named configuration option parameter.
		:param value: Value to store for the named configuration option
		:param configuration_option: Configuration option as defined in swSetValueInConfiguration_e
		:param configuration_name: Name of the configuration
		"""
		# return self._instance.SetDoubleValue2(value, configuration_option, configuration_name)
		raise NotImplemented

	def set_string_value(self, string_value, configuration_option, configuration_name):
		"""
		Sets the double or integer value of a named configuration option parameter.
		:param string_value: Value to store for the named configuration option
		:param configuration_option: Configuration option as defined in swInConfigurationOpts_e
		:param configuration_name: Name of the configuration
		"""
		# return self._instance.SetStringValue2(string_value, configuration_option, configuration_name)
		raise NotImplemented

	def set_vector(self, x, y, z, configuration_option, configuration_name):
		"""
		Sets the vector values of a named configuration option parameter.
		:param x: x value to store for the named configuration option
		:param y: y value to store for the named configuration option
		:param z: z value to store for the named configuration option
		:param configuration_option: Configuration option as defined in swInConfigurationOpts_e
		:param configuration_name: Name of the configuration
		"""
		# return self._instance.SetVector2(x, y, z, configuration_option, configuration_name)
		raise NotImplemented

