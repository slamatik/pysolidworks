# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFeatureData_members.html
class ILibraryFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def configuration_name(self):
		"""Gets or sets the name of the active library feature configuration."""
		return self._instance.ConfigurationName

	@configuration_name.setter
	def configuration_name(self, value):
		"""Gets or sets the name of the active library feature configuration."""
		self._instance.ConfigurationName = value

	@property
	def library_part(self):
		"""Gets the path and filename of the library feature."""
		return self._instance.LibraryPart

	@library_part.setter
	def library_part(self, value):
		"""Gets the path and filename of the library feature."""
		self._instance.LibraryPart = value

	@property
	def link_to_library_part(self):
		"""Gets or sets whether to the link the library feature to its parent library feature document."""
		return self._instance.LinkToLibraryPart

	@link_to_library_part.setter
	def link_to_library_part(self, value):
		"""Gets or sets whether to the link the library feature to its parent library feature document."""
		self._instance.LinkToLibraryPart = value

	@property
	def override_dimension(self):
		"""Gets or sets whether to override the existing size dimension values of the library feature."""
		return self._instance.OverrideDimension

	@override_dimension.setter
	def override_dimension(self, value):
		"""Gets or sets whether to override the existing size dimension values of the library feature."""
		self._instance.OverrideDimension = value

	@property
	def access_selections(self):
		"""Gains access to selections that define this library feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections that define this library feature."""
		self._instance.AccessSelections = value

	@property
	def get_all_configuration_names(self):
		"""Gets the names of the library feature configurations."""
		return self._instance.GetAllConfigurationNames

	@get_all_configuration_names.setter
	def get_all_configuration_names(self, value):
		"""Gets the names of the library feature configurations."""
		self._instance.GetAllConfigurationNames = value

	@property
	def get_configuration_count(self):
		"""Gets the number of library feature configurations."""
		return self._instance.GetConfigurationCount

	@get_configuration_count.setter
	def get_configuration_count(self, value):
		"""Gets the number of library feature configurations."""
		self._instance.GetConfigurationCount = value

	@property
	def get_dimensions(self):
		"""Gets the names and values of the specified type of dimension for this library feature."""
		return self._instance.GetDimensions

	@get_dimensions.setter
	def get_dimensions(self, value):
		"""Gets the names and values of the specified type of dimension for this library feature."""
		self._instance.GetDimensions = value

	@property
	def get_dimensions_count(self):
		"""Gets the number of dimensions of the specified type for this library feature."""
		return self._instance.GetDimensionsCount

	@get_dimensions_count.setter
	def get_dimensions_count(self, value):
		"""Gets the number of dimensions of the specified type for this library feature."""
		self._instance.GetDimensionsCount = value

	@property
	def get_placement_plane(self):
		"""Gets the face or plane on which the library feature was placed."""
		return self._instance.GetPlacementPlane2

	@get_placement_plane.setter
	def get_placement_plane(self, value):
		"""Gets the face or plane on which the library feature was placed."""
		self._instance.GetPlacementPlane2 = value

	@property
	def get_references(self):
		"""Gets the references with respect to the specified scope."""
		return self._instance.GetReferences3

	@get_references.setter
	def get_references(self, value):
		"""Gets the references with respect to the specified scope."""
		self._instance.GetReferences3 = value

	@property
	def get_references_count(self):
		"""Gets the number of references for the library feature."""
		return self._instance.GetReferencesCount

	@get_references_count.setter
	def get_references_count(self, value):
		"""Gets the number of references for the library feature."""
		self._instance.GetReferencesCount = value

	@property
	def i_get_all_configuration_names(self):
		"""Gets the names of the library feature configurations."""
		return self._instance.IGetAllConfigurationNames

	@i_get_all_configuration_names.setter
	def i_get_all_configuration_names(self, value):
		"""Gets the names of the library feature configurations."""
		self._instance.IGetAllConfigurationNames = value

	@property
	def i_get_dimensions(self):
		"""Gets the names and values of the specified type of dimension for this library feature."""
		return self._instance.IGetDimensions

	@i_get_dimensions.setter
	def i_get_dimensions(self, value):
		"""Gets the names and values of the specified type of dimension for this library feature."""
		self._instance.IGetDimensions = value

	@property
	def i_get_references(self):
		"""Gets the references with respect to the specified scope."""
		return self._instance.IGetReferences3

	@i_get_references.setter
	def i_get_references(self, value):
		"""Gets the references with respect to the specified scope."""
		self._instance.IGetReferences3 = value

	@property
	def initialize(self):
		"""Initializes a newly created library feature using the specified library part."""
		return self._instance.Initialize

	@initialize.setter
	def initialize(self, value):
		"""Initializes a newly created library feature using the specified library part."""
		self._instance.Initialize = value

	@property
	def i_set_references(self):
		"""Sets the references for the library feature."""
		return self._instance.ISetReferences

	@i_set_references.setter
	def i_set_references(self, value):
		"""Sets the references for the library feature."""
		self._instance.ISetReferences = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created this library feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created this library feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_dimension(self):
		"""Sets a dimension's type, name, and value for the library feature."""
		return self._instance.SetDimension

	@set_dimension.setter
	def set_dimension(self, value):
		"""Sets a dimension's type, name, and value for the library feature."""
		self._instance.SetDimension = value

	@property
	def set_placement_plane(self):
		"""Sets the face or plane on which to place the library feature."""
		return self._instance.SetPlacementPlane

	@set_placement_plane.setter
	def set_placement_plane(self, value):
		"""Sets the face or plane on which to place the library feature."""
		self._instance.SetPlacementPlane = value

	@property
	def set_references(self):
		"""Sets the references for the library feature."""
		return self._instance.SetReferences

	@set_references.setter
	def set_references(self, value):
		"""Sets the references for the library feature."""
		self._instance.SetReferences = value

