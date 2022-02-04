# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences_members.html
class IRenamedDocumentReferences:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def completion_action(self):
		"""Gets or sets whether to update references to the renamed file in unopened documents."""
		return self._instance.CompletionAction

	@completion_action.setter
	def completion_action(self, value):
		"""Gets or sets whether to update references to the renamed file in unopened documents."""
		self._instance.CompletionAction = value

	@property
	def include_file_locations(self):
		"""Gets or sets whether to search the folders listed under Referenced Documents in Tools > Options > System Options > File Locations."""
		return self._instance.IncludeFileLocations

	@include_file_locations.setter
	def include_file_locations(self, value):
		"""Gets or sets whether to search the folders listed under Referenced Documents in Tools > Options > System Options > File Locations."""
		self._instance.IncludeFileLocations = value

	@property
	def update_where_used_references(self):
		"""Gets or sets whether to update the references to the new file name."""
		return self._instance.UpdateWhereUsedReferences

	@update_where_used_references.setter
	def update_where_used_references(self, value):
		"""Gets or sets whether to update the references to the new file name."""
		self._instance.UpdateWhereUsedReferences = value

	@property
	def add_search_folder(self):
		"""Adds the specified folder in which to search for documents whose references to update."""
		return self._instance.AddSearchFolder

	@add_search_folder.setter
	def add_search_folder(self, value):
		"""Adds the specified folder in which to search for documents whose references to update."""
		self._instance.AddSearchFolder = value

	@property
	def get_search_path(self):
		"""Gets the folders to search."""
		return self._instance.GetSearchPath

	@get_search_path.setter
	def get_search_path(self, value):
		"""Gets the folders to search."""
		self._instance.GetSearchPath = value

	@property
	def references_array(self):
		"""Gets the pathnames of the documents with references to this renamed document."""
		return self._instance.ReferencesArray

	@references_array.setter
	def references_array(self, value):
		"""Gets the pathnames of the documents with references to this renamed document."""
		self._instance.ReferencesArray = value

	@property
	def remove_reference(self):
		"""Removes the specified reference from the list of references to update."""
		return self._instance.RemoveReference

	@remove_reference.setter
	def remove_reference(self, value):
		"""Removes the specified reference from the list of references to update."""
		self._instance.RemoveReference = value

	@property
	def remove_search_folder(self):
		"""Removes the specified folder in which to search for documents whose references to update."""
		return self._instance.RemoveSearchFolder

	@remove_search_folder.setter
	def remove_search_folder(self, value):
		"""Removes the specified folder in which to search for documents whose references to update."""
		self._instance.RemoveSearchFolder = value

	@property
	def search(self):
		"""Searches for documents whose references to update."""
		return self._instance.Search

	@search.setter
	def search(self, value):
		"""Searches for documents whose references to update."""
		self._instance.Search = value

