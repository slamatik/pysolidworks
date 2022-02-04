# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBodyFolder_members.html
class IBodyFolder:
	def __init__(self, parent=None):
		self._instance = parent

	def type(self):
		"""Gets the type of body folder."""
		# return self._instance.Type
		raise NotImplemented

	def get_automatic_cut_list(self):
		"""Gets whether to automatically generate a cut list when the first weldment feature is inserted in a part."""
		# return self._instance.GetAutomaticCutList
		raise NotImplemented

	def get_automatic_update(self):
		"""Gets whether to automatically update cut lists."""
		# return self._instance.GetAutomaticUpdate
		raise NotImplemented

	def get_bodies(self):
		"""Gets the bodies in the folder."""
		# return self._instance.GetBodies
		raise NotImplemented

	def get_body_count(self):
		"""Gets the number of bodies in the folder."""
		# return self._instance.GetBodyCount
		raise NotImplemented

	def get_cut_list_sort_options(self):
		"""Gets the cut list sort options."""
		# return self._instance.GetCutListSortOptions
		raise NotImplemented

	def get_cut_list_type(self):
		"""Gets the type of cut list."""
		# return self._instance.GetCutListType
		raise NotImplemented

	def get_feature(self):
		"""Gets the feature for this body folder."""
		# return self._instance.GetFeature
		raise NotImplemented

	def i_get_bodies(self, count):
		"""
		Gets the bodies in the folder.
		:param count: Number of bodies in the folder
		"""
		# return self._instance.IGetBodies(count)
		raise NotImplemented

	def set_automatic_cut_list(self, cut_list):
		"""
		Sets whether to automatically generate a cut list when the first weldment feature is inserted in a part.
		:param cut_list: True to automatically generate a cut list, false to not
		"""
		# return self._instance.SetAutomaticCutList(cut_list)
		raise NotImplemented

	def set_automatic_update(self, update):
		"""
		Sets whether to automatically update cut lists.
		:param update: True to automatically update cut lists, false to update them manually
		"""
		# return self._instance.SetAutomaticUpdate(update)
		raise NotImplemented

	def sort_cut_list(self, cut_list_sort_options, ignore_invalid_faces_or_features):
		"""
		Sorts the cut list.
		:param cut_list_sort_options: ICutListSortOptions
		:param ignore_invalid_faces_or_features: True to sort bodies ignoring any invalid excluded faces/features, false to not sort the bodies if there are invalid excluded faces/features (see Remarks)
		"""
		# return self._instance.SortCutList(cut_list_sort_options, ignore_invalid_faces_or_features)
		raise NotImplemented

	def update_cut_list(self):
		"""Updates an automatically generated cut list."""
		# return self._instance.UpdateCutList
		raise NotImplemented

