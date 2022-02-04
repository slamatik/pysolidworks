# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html
class IAdvancedSaveAsOptions:
	def __init__(self, parent=None):
		self._instance = parent

	def configurations_to_save(self):
		"""Sets the subset of configurations to save."""
		# return self._instance.ConfigurationsToSave
		raise NotImplemented

	def description(self):
		"""Adds a desciption of the save."""
		# return self._instance.Description
		raise NotImplemented

	def geometry_to_save(self):
		"""Sets the geometry to save only when saving an assembly as a part."""
		# return self._instance.GeometryToSave
		raise NotImplemented

	def override_defaults(self):
		"""Sets whether to override defaults only when saving an assembly as a part."""
		# return self._instance.OverrideDefaults
		raise NotImplemented

	def preserve_geometry_references(self):
		"""Sets whether to preserve geometry references only when saving an assembly as a part."""
		# return self._instance.PreserveGeometryReferences
		raise NotImplemented

	def save_all_as_copy(self):
		"""Sets whether to save all component references as copies."""
		# return self._instance.SaveAllAsCopy
		raise NotImplemented

	def get_items_name_and_path(self, ids_list, names_list, paths_list):
		"""
		Gets all reference components' names and paths.
		:param ids_list: Array of component reference IDs
		:param names_list: Array of component reference names
		:param paths_list: Array of component reference paths
		"""
		# return self._instance.GetItemsNameAndPath(ids_list, names_list, paths_list)
		raise NotImplemented

	def modify_items_name_and_path(self, ids_list, names_list, paths_list):
		"""
		Modifies the specified reference components with the specified names and paths.
		:param ids_list: Array of reference component IDs (see Remarks)
		:param names_list: Array of new reference component names
		:param paths_list: Array of new reference component paths
		"""
		# return self._instance.ModifyItemsNameAndPath(ids_list, names_list, paths_list)
		raise NotImplemented

	def set_prefix_suffix_to_all(self, prefix_string, suffix_string):
		"""
		Sets a prefix and/or a suffix on all component reference names.
		:param prefix_string: Prefix
		:param suffix_string: Suffix
		"""
		# return self._instance.SetPrefixSuffixToAll(prefix_string, suffix_string)
		raise NotImplemented

