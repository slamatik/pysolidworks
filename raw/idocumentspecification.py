# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html
class IDocumentSpecification:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_repair(self):
		"""Gets or sets whether to automatically repair non-critical custom properties errors in the file to be opened."""
		return self._instance.AutoRepair

	@auto_repair.setter
	def auto_repair(self, value):
		"""Gets or sets whether to automatically repair non-critical custom properties errors in the file to be opened."""
		self._instance.AutoRepair = value

	@property
	def component_list(self):
		"""Gets or sets the selected components to load when opening an assembly document."""
		return self._instance.ComponentList

	@component_list.setter
	def component_list(self, value):
		"""Gets or sets the selected components to load when opening an assembly document."""
		self._instance.ComponentList = value

	@property
	def configuration_name(self):
		"""Gets or sets the name of the configuration to load when opening a model document."""
		return self._instance.ConfigurationName

	@configuration_name.setter
	def configuration_name(self, value):
		"""Gets or sets the name of the configuration to load when opening a model document."""
		self._instance.ConfigurationName = value

	@property
	def critical_data_repair(self):
		"""Gets or sets whether to automatically repair critical data errors in the file to be opened."""
		return self._instance.CriticalDataRepair

	@critical_data_repair.setter
	def critical_data_repair(self, value):
		"""Gets or sets whether to automatically repair critical data errors in the file to be opened."""
		self._instance.CriticalDataRepair = value

	@property
	def detailing_mode(self):
		"""Gets or sets whether this drawing document is in detailing mode."""
		return self._instance.DetailingMode

	@detailing_mode.setter
	def detailing_mode(self, value):
		"""Gets or sets whether this drawing document is in detailing mode."""
		self._instance.DetailingMode = value

	@property
	def display_state(self):
		"""Gets or sets the name of the display state to use when opening a model document."""
		return self._instance.DisplayState

	@display_state.setter
	def display_state(self, value):
		"""Gets or sets the name of the display state to use when opening a model document."""
		self._instance.DisplayState = value

	@property
	def document_type(self):
		"""Gets or sets the type of model document to open."""
		return self._instance.DocumentType

	@document_type.setter
	def document_type(self, value):
		"""Gets or sets the type of model document to open."""
		self._instance.DocumentType = value

	@property
	def error(self):
		"""Gets or sets the file load errors when opening a model document."""
		return self._instance.Error

	@error.setter
	def error(self, value):
		"""Gets or sets the file load errors when opening a model document."""
		self._instance.Error = value

	@property
	def file_name(self):
		"""Gets or sets the path and filename of the model document to open."""
		return self._instance.FileName

	@file_name.setter
	def file_name(self, value):
		"""Gets or sets the path and filename of the model document to open."""
		self._instance.FileName = value

	@property
	def ignore_hidden_components(self):
		"""Gets or sets whether to load hidden components when opening an assembly or drawing document."""
		return self._instance.IgnoreHiddenComponents

	@ignore_hidden_components.setter
	def ignore_hidden_components(self, value):
		"""Gets or sets whether to load hidden components when opening an assembly or drawing document."""
		self._instance.IgnoreHiddenComponents = value

	@property
	def interactive_advanced_open(self):
		"""Gets whether to display an intermediate dialog, which allows the interactive user to set options before opening a document."""
		return self._instance.InteractiveAdvancedOpen

	@interactive_advanced_open.setter
	def interactive_advanced_open(self, value):
		"""Gets whether to display an intermediate dialog, which allows the interactive user to set options before opening a document."""
		self._instance.InteractiveAdvancedOpen = value

	@property
	def interactive_component_selection(self):
		"""Gets whether to display the Selective Open dialog, which allows the interactive user to either select and open specific components or open all of the
displayed components."""
		return self._instance.InteractiveComponentSelection

	@interactive_component_selection.setter
	def interactive_component_selection(self, value):
		"""Gets whether to display the Selective Open dialog, which allows the interactive user to either select and open specific components or open all of the
displayed components."""
		self._instance.InteractiveComponentSelection = value

	@property
	def light_weight(self):
		"""Gets or sets whether to open an assembly or drawing document with lightweight parts."""
		return self._instance.LightWeight

	@light_weight.setter
	def light_weight(self, value):
		"""Gets or sets whether to open an assembly or drawing document with lightweight parts."""
		self._instance.LightWeight = value

	@property
	def load_external_references_in_memory(self):
		"""Gets or sets whether to load external references in memory when opening a document."""
		return self._instance.LoadExternalReferencesInMemory

	@load_external_references_in_memory.setter
	def load_external_references_in_memory(self, value):
		"""Gets or sets whether to load external references in memory when opening a document."""
		self._instance.LoadExternalReferencesInMemory = value

	@property
	def load_model(self):
		"""Gets or sets whether to load the model if the document is a detached drawing."""
		return self._instance.LoadModel

	@load_model.setter
	def load_model(self, value):
		"""Gets or sets whether to load the model if the document is a detached drawing."""
		self._instance.LoadModel = value

	@property
	def p_l_m_object_specification(self):
		"""Gets the specification of this SOLIDWORKS Connected document."""
		return self._instance.PLMObjectSpecification

	@p_l_m_object_specification.setter
	def p_l_m_object_specification(self, value):
		"""Gets the specification of this SOLIDWORKS Connected document."""
		self._instance.PLMObjectSpecification = value

	@property
	def query(self):
		"""Gets or sets whether the options passed during a document's open, load, and save can be retrieved by this API."""
		return self._instance.Query

	@query.setter
	def query(self, value):
		"""Gets or sets whether the options passed during a document's open, load, and save can be retrieved by this API."""
		self._instance.Query = value

	@property
	def read_only(self):
		"""Gets or sets whether the model document is opened read-only or read-write."""
		return self._instance.ReadOnly

	@read_only.setter
	def read_only(self, value):
		"""Gets or sets whether the model document is opened read-only or read-write."""
		self._instance.ReadOnly = value

	@property
	def selective(self):
		"""Gets or sets whether to open a document in Quick view (parts and drawings) or Quick view / Selective (assemblies) mode."""
		return self._instance.Selective

	@selective.setter
	def selective(self, value):
		"""Gets or sets whether to open a document in Quick view (parts and drawings) or Quick view / Selective (assemblies) mode."""
		self._instance.Selective = value

	@property
	def sheet_name(self):
		"""Gets or sets the name of the sheet in a drawing document to open."""
		return self._instance.SheetName

	@sheet_name.setter
	def sheet_name(self, value):
		"""Gets or sets the name of the sheet in a drawing document to open."""
		self._instance.SheetName = value

	@property
	def silent(self):
		"""Gets or sets whether to open the model document silently."""
		return self._instance.Silent

	@silent.setter
	def silent(self, value):
		"""Gets or sets whether to open the model document silently."""
		self._instance.Silent = value

	@property
	def use_light_weight_default(self):
		"""Gets or sets whether to use the system default lightweight setting."""
		return self._instance.UseLightWeightDefault

	@use_light_weight_default.setter
	def use_light_weight_default(self, value):
		"""Gets or sets whether to use the system default lightweight setting."""
		self._instance.UseLightWeightDefault = value

	@property
	def use_speed_pak(self):
		"""Gets or sets whether to open an assembly document using the SpeedPak option."""
		return self._instance.UseSpeedPak

	@use_speed_pak.setter
	def use_speed_pak(self, value):
		"""Gets or sets whether to open an assembly document using the SpeedPak option."""
		self._instance.UseSpeedPak = value

	@property
	def view_only(self):
		"""Gets or sets whether to open the assembly document in Large Design Review mode."""
		return self._instance.ViewOnly

	@view_only.setter
	def view_only(self, value):
		"""Gets or sets whether to open the assembly document in Large Design Review mode."""
		self._instance.ViewOnly = value

	@property
	def warning(self):
		"""Gets or sets any file load warnings when opening a model document."""
		return self._instance.Warning

	@warning.setter
	def warning(self, value):
		"""Gets or sets any file load warnings when opening a model document."""
		self._instance.Warning = value

