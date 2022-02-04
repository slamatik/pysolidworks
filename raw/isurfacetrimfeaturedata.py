# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceTrimFeatureData_members.html
class ISurfaceTrimFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def pieces_to_keep(self):
		"""Gets the pieces to keep for this surface trim feature.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.PiecesToKeep
		raise NotImplemented

	def trim_tools(self):
		"""Gets the trim tools for surface trim feature.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.TrimTools
		raise NotImplemented

	def access_selections(self, top_doc, component):
		"""
		Accesses the selections that define this surface trim feature.
		:param top_doc: Top-level document
		:param component: Component in which the feature is to be modified
		"""
		# return self._instance.AccessSelections(top_doc, component)
		raise NotImplemented

	def get_pieces_to_keep_count(self):
		"""Gets the number of pieces to keep for this surface trim feature."""
		# return self._instance.GetPiecesToKeepCount
		raise NotImplemented

	def get_trim_tools_count(self):
		"""Gets the number of trim tools for this surface trim feature."""
		# return self._instance.GetTrimToolsCount
		raise NotImplemented

	def get_type(self):
		"""Gets the type of this surface trim feature."""
		# return self._instance.GetType
		raise NotImplemented

	def i_access_selections(self, top_doc, component):
		"""
		Accesses the selections that define this surface trim feature.
		:param top_doc: Top-level document
		:param component: Component in which the feature is to be modified
		"""
		# return self._instance.IAccessSelections(top_doc, component)
		raise NotImplemented

	def i_get_pieces_to_keep(self, count):
		"""
		Gets the pieces to keep for this surface trim feature.
		:param count: Number of pieces to keep
		"""
		# return self._instance.IGetPiecesToKeep(count)
		raise NotImplemented

	def i_get_trim_tools(self, count):
		"""
		Gets the trim tools for this surface trim feature.
		:param count: Number of trim tools
		"""
		# return self._instance.IGetTrimTools(count)
		raise NotImplemented

	def i_set_pieces_to_keep(self, count, body_arr):
		"""
		Sets the pieces to keep for this surface trim feature.
		:param count: Number of pieces to keep
		:param body_arr: 

in-process, unmanaged C++: Pointer to an array of pieces to keep of size Count
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method. 
		"""
		# return self._instance.ISetPiecesToKeep(count, body_arr)
		raise NotImplemented

	def i_set_trim_tools(self, count, disp_arr):
		"""
		Sets the trim tools for this surface trim feature.
		:param count: Number of trim tools
		:param disp_arr: 

in-process, unmanaged C++: Pointer to an array of trim tools of size Count
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.ISetTrimTools(count, disp_arr)
		raise NotImplemented

	def release_selection_access(self):
		"""Releases access to the selections that created this surface trim feature."""
		# return self._instance.ReleaseSelectionAccess
		raise NotImplemented

