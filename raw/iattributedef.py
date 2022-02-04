# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.html
class IAttributeDef:
	def __init__(self, parent=None):
		self._instance = parent

	def add_parameter(self, name_in, type, default_value, options):
		"""
		Adds a parameter to the attribute definition using the specified name and default value.
		:param name_in: Name to be given to the parameter (see Remarks)
		:param type: Parameter type as defined in swParamType_e
		:param default_value: Default value (see Remarks)
		:param options: Not used
		"""
		# return self._instance.AddParameter(name_in, type, default_value, options)
		raise NotImplemented

	def create_instance(self, owner_doc, owner_obj, name_in, options, configuration_option):
		"""
		Creates an instance of this attribute on the specified object with the specified options.
		:param owner_doc: Document whose FeatureManager design tree to which to add this attribute
		:param owner_obj: Component or entity to which to add this attribute:

IBODY2
ICOMPONENT2
IENTITY, which can be a face, loop, edge, vertex, or feature 
MODELDOC2 if NULL
		:param name_in: Name to assign to this attribute instance (see Remarks)
		:param options: Creation control options (see Remarks)
		:param configuration_option: Configuration options as defined in swInConfigurationOpts_e
		"""
		# return self._instance.CreateInstance5(owner_doc, owner_obj, name_in, options, configuration_option)
		raise NotImplemented

	def register(self):
		"""Registers an AttributeDef object as the final part of its creation."""
		# return self._instance.Register
		raise NotImplemented

