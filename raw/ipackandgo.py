# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html
class IPackAndGo:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def add_prefix(self):
		"""Gets or sets a prefix for all filenames for Pack and Go."""
		return self._instance.AddPrefix

	@add_prefix.setter
	def add_prefix(self, value):
		"""Gets or sets a prefix for all filenames for Pack and Go."""
		self._instance.AddPrefix = value

	@property
	def add_suffix(self):
		"""Gets or sets a suffix for all filenames for Pack and Go."""
		return self._instance.AddSuffix

	@add_suffix.setter
	def add_suffix(self, value):
		"""Gets or sets a suffix for all filenames for Pack and Go."""
		self._instance.AddSuffix = value

	@property
	def flatten_to_single_folder(self):
		"""Gets or sets whether to save all files to the root directory of the Pack and Go destination folder."""
		return self._instance.FlattenToSingleFolder

	@flatten_to_single_folder.setter
	def flatten_to_single_folder(self, value):
		"""Gets or sets whether to save all files to the root directory of the Pack and Go destination folder."""
		self._instance.FlattenToSingleFolder = value

	@property
	def include_drawings(self):
		"""Gets or sets whether to add the model's drawing documents to Pack and Go."""
		return self._instance.IncludeDrawings

	@include_drawings.setter
	def include_drawings(self, value):
		"""Gets or sets whether to add the model's drawing documents to Pack and Go."""
		self._instance.IncludeDrawings = value

	@property
	def include_simulation_results(self):
		"""Gets or sets whether to add the model's SOLIDWORKS Simulation results to Pack and Go."""
		return self._instance.IncludeSimulationResults

	@include_simulation_results.setter
	def include_simulation_results(self, value):
		"""Gets or sets whether to add the model's SOLIDWORKS Simulation results to Pack and Go."""
		self._instance.IncludeSimulationResults = value

	@property
	def include_suppressed(self):
		"""Gets or sets whether to included suppressed components in Pack and Go."""
		return self._instance.IncludeSuppressed

	@include_suppressed.setter
	def include_suppressed(self, value):
		"""Gets or sets whether to included suppressed components in Pack and Go."""
		self._instance.IncludeSuppressed = value

	@property
	def include_toolbox_components(self):
		"""Gets or sets whether to include SOLIDWORKS Toolbox components in Pack and Go."""
		return self._instance.IncludeToolboxComponents

	@include_toolbox_components.setter
	def include_toolbox_components(self, value):
		"""Gets or sets whether to include SOLIDWORKS Toolbox components in Pack and Go."""
		self._instance.IncludeToolboxComponents = value

	@property
	def add_external_documents(self):
		"""Adds non-SOLIDWORKS files to Pack and Go."""
		return self._instance.AddExternalDocuments

	@add_external_documents.setter
	def add_external_documents(self, value):
		"""Adds non-SOLIDWORKS files to Pack and Go."""
		self._instance.AddExternalDocuments = value

	@property
	def get_document_names(self):
		"""Gets the original paths and filenames of all of the model's documents for Pack and Go."""
		return self._instance.GetDocumentNames

	@get_document_names.setter
	def get_document_names(self, value):
		"""Gets the original paths and filenames of all of the model's documents for Pack and Go."""
		self._instance.GetDocumentNames = value

	@property
	def get_document_names_count(self):
		"""Gets the number of documents comprising the model for Pack and Go."""
		return self._instance.GetDocumentNamesCount

	@get_document_names_count.setter
	def get_document_names_count(self, value):
		"""Gets the number of documents comprising the model for Pack and Go."""
		self._instance.GetDocumentNamesCount = value

	@property
	def get_document_save_to_names(self):
		"""Gets the paths and filenames to which to save the model's documents for Pack and Go set by IPackAndGo::SetDocumentSaveToNames."""
		return self._instance.GetDocumentSaveToNames

	@get_document_save_to_names.setter
	def get_document_save_to_names(self, value):
		"""Gets the paths and filenames to which to save the model's documents for Pack and Go set by IPackAndGo::SetDocumentSaveToNames."""
		self._instance.GetDocumentSaveToNames = value

	@property
	def get_external_documents(self):
		"""Gets the paths and filenames of the non-SOLIDWORKS files added to Pack And Go."""
		return self._instance.GetExternalDocuments

	@get_external_documents.setter
	def get_external_documents(self, value):
		"""Gets the paths and filenames of the non-SOLIDWORKS files added to Pack And Go."""
		self._instance.GetExternalDocuments = value

	@property
	def get_save_to_name(self):
		"""Gets the path or the path and filename of the Zip file for Pack and Go set by IPackAndGo::SetSaveToName."""
		return self._instance.GetSaveToName

	@get_save_to_name.setter
	def get_save_to_name(self, value):
		"""Gets the path or the path and filename of the Zip file for Pack and Go set by IPackAndGo::SetSaveToName."""
		self._instance.GetSaveToName = value

	@property
	def i_get_document_names(self):
		"""Gets the original paths and filenames of all of the model's documents for Pack and Go."""
		return self._instance.IGetDocumentNames

	@i_get_document_names.setter
	def i_get_document_names(self, value):
		"""Gets the original paths and filenames of all of the model's documents for Pack and Go."""
		self._instance.IGetDocumentNames = value

	@property
	def i_get_document_save_to_names(self):
		"""Gets the paths and filenames to which to save the model's documents for Pack and Go set by IPackAndGo::ISetDocumentSaveToNames."""
		return self._instance.IGetDocumentSaveToNames

	@i_get_document_save_to_names.setter
	def i_get_document_save_to_names(self, value):
		"""Gets the paths and filenames to which to save the model's documents for Pack and Go set by IPackAndGo::ISetDocumentSaveToNames."""
		self._instance.IGetDocumentSaveToNames = value

	@property
	def i_set_document_save_to_names(self):
		"""Sets the paths and filenames of the documents to save in Pack and Go."""
		return self._instance.ISetDocumentSaveToNames

	@i_set_document_save_to_names.setter
	def i_set_document_save_to_names(self, value):
		"""Sets the paths and filenames of the documents to save in Pack and Go."""
		self._instance.ISetDocumentSaveToNames = value

	@property
	def remove_external_documents(self):
		"""Removes the specified non-SOLIDWORKS files from Pack and Go."""
		return self._instance.RemoveExternalDocuments

	@remove_external_documents.setter
	def remove_external_documents(self, value):
		"""Removes the specified non-SOLIDWORKS files from Pack and Go."""
		self._instance.RemoveExternalDocuments = value

	@property
	def set_document_save_to_names(self):
		"""Sets the paths and filenames of the documents for Pack and Go."""
		return self._instance.SetDocumentSaveToNames

	@set_document_save_to_names.setter
	def set_document_save_to_names(self, value):
		"""Sets the paths and filenames of the documents for Pack and Go."""
		self._instance.SetDocumentSaveToNames = value

	@property
	def set_save_to_name(self):
		"""Overrides the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames with the specified path or the path and name of the Zip file."""
		return self._instance.SetSaveToName

	@set_save_to_name.setter
	def set_save_to_name(self, value):
		"""Overrides the paths and filenames of the documents set by IPackAndGo::SetDocumentSaveToNames or IPackAndGo::ISetDocumentSaveToNames with the specified path or the path and name of the Zip file."""
		self._instance.SetSaveToName = value

