# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterferenceDetectionMgr_members.html
class IInterferenceDetectionMgr:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def create_fasteners_folder(self):
		"""Gets or sets whether to create the Fasteners folders to segregate interferences involving fasteners."""
		return self._instance.CreateFastenersFolder

	@create_fasteners_folder.setter
	def create_fasteners_folder(self, value):
		"""Gets or sets whether to create the Fasteners folders to segregate interferences involving fasteners."""
		self._instance.CreateFastenersFolder = value

	@property
	def ignore_hidden_bodies(self):
		"""Gets or sets whether to ignore hidden bodies during interference detection."""
		return self._instance.IgnoreHiddenBodies

	@ignore_hidden_bodies.setter
	def ignore_hidden_bodies(self, value):
		"""Gets or sets whether to ignore hidden bodies during interference detection."""
		self._instance.IgnoreHiddenBodies = value

	@property
	def include_multibody_part_interferences(self):
		"""Gets or sets whether to report interferences between bodies within multibody parts."""
		return self._instance.IncludeMultibodyPartInterferences

	@include_multibody_part_interferences.setter
	def include_multibody_part_interferences(self, value):
		"""Gets or sets whether to report interferences between bodies within multibody parts."""
		self._instance.IncludeMultibodyPartInterferences = value

	@property
	def make_interfering_parts_transparent(self):
		"""Gets or sets whether to display the components of the selected interference in transparent mode."""
		return self._instance.MakeInterferingPartsTransparent

	@make_interfering_parts_transparent.setter
	def make_interfering_parts_transparent(self, value):
		"""Gets or sets whether to display the components of the selected interference in transparent mode."""
		self._instance.MakeInterferingPartsTransparent = value

	@property
	def non_interfering_component_display(self):
		"""Gets or sets the mode to display non-interfering components."""
		return self._instance.NonInterferingComponentDisplay

	@non_interfering_component_display.setter
	def non_interfering_component_display(self, value):
		"""Gets or sets the mode to display non-interfering components."""
		self._instance.NonInterferingComponentDisplay = value

	@property
	def show_ignored_interferences(self):
		"""Gets or sets whether to show ignored interferences."""
		return self._instance.ShowIgnoredInterferences

	@show_ignored_interferences.setter
	def show_ignored_interferences(self, value):
		"""Gets or sets whether to show ignored interferences."""
		self._instance.ShowIgnoredInterferences = value

	@property
	def treat_coincidence_as_interference(self):
		"""Gets or sets whether to treat coincident entities as interference."""
		return self._instance.TreatCoincidenceAsInterference

	@treat_coincidence_as_interference.setter
	def treat_coincidence_as_interference(self, value):
		"""Gets or sets whether to treat coincident entities as interference."""
		self._instance.TreatCoincidenceAsInterference = value

	@property
	def treat_sub_assemblies_as_components(self):
		"""Gets or sets whether to treat subassemblies as single components so that interferences between a sub-assembly's components are not reported."""
		return self._instance.TreatSubAssembliesAsComponents

	@treat_sub_assemblies_as_components.setter
	def treat_sub_assemblies_as_components(self, value):
		"""Gets or sets whether to treat subassemblies as single components so that interferences between a sub-assembly's components are not reported."""
		self._instance.TreatSubAssembliesAsComponents = value

	@property
	def use_transform(self):
		"""Gets or sets whether to use transforms in interference detection."""
		return self._instance.UseTransform

	@use_transform.setter
	def use_transform(self, value):
		"""Gets or sets whether to use transforms in interference detection."""
		self._instance.UseTransform = value

	@property
	def done(self):
		"""Stops the interference detection."""
		return self._instance.Done

	@done.setter
	def done(self, value):
		"""Stops the interference detection."""
		self._instance.Done = value

	@property
	def export_results(self):
		"""Saves interference detection results to a file."""
		return self._instance.ExportResults

	@export_results.setter
	def export_results(self, value):
		"""Saves interference detection results to a file."""
		self._instance.ExportResults = value

	@property
	def get_components_and_transforms(self):
		"""Gets the interfering components and their transforms."""
		return self._instance.GetComponentsAndTransforms

	@get_components_and_transforms.setter
	def get_components_and_transforms(self, value):
		"""Gets the interfering components and their transforms."""
		self._instance.GetComponentsAndTransforms = value

	@property
	def get_components_transform_interference(self):
		"""Calculates and gets the interfering components for the specified components and math transform."""
		return self._instance.GetComponentsTransformInterference

	@get_components_transform_interference.setter
	def get_components_transform_interference(self, value):
		"""Calculates and gets the interfering components for the specified components and math transform."""
		self._instance.GetComponentsTransformInterference = value

	@property
	def get_components_transform_interference_count(self):
		"""Calculates and gets the number of interfering components for the specified components and math transform."""
		return self._instance.GetComponentsTransformInterferenceCount

	@get_components_transform_interference_count.setter
	def get_components_transform_interference_count(self, value):
		"""Calculates and gets the number of interfering components for the specified components and math transform."""
		self._instance.GetComponentsTransformInterferenceCount = value

	@property
	def get_interference_component_count(self):
		"""Calculates and gets the number of interfering components."""
		return self._instance.GetInterferenceComponentCount

	@get_interference_component_count.setter
	def get_interference_component_count(self, value):
		"""Calculates and gets the number of interfering components."""
		self._instance.GetInterferenceComponentCount = value

	@property
	def get_interference_components(self):
		"""Calculates and gets the interfering components."""
		return self._instance.GetInterferenceComponents

	@get_interference_components.setter
	def get_interference_components(self, value):
		"""Calculates and gets the interfering components."""
		self._instance.GetInterferenceComponents = value

	@property
	def get_interference_count(self):
		"""Calculates and gets the number of interferences."""
		return self._instance.GetInterferenceCount

	@get_interference_count.setter
	def get_interference_count(self, value):
		"""Calculates and gets the number of interferences."""
		self._instance.GetInterferenceCount = value

	@property
	def get_interferences(self):
		"""Calculates and gets the interferences."""
		return self._instance.GetInterferences

	@get_interferences.setter
	def get_interferences(self, value):
		"""Calculates and gets the interferences."""
		self._instance.GetInterferences = value

	@property
	def i_get_components_transform_interference(self):
		"""Calculates and gets the interfering components for the specified components and math transform."""
		return self._instance.IGetComponentsTransformInterference

	@i_get_components_transform_interference.setter
	def i_get_components_transform_interference(self, value):
		"""Calculates and gets the interfering components for the specified components and math transform."""
		self._instance.IGetComponentsTransformInterference = value

	@property
	def i_get_interference_components(self):
		"""Calculates and gets the interfering components."""
		return self._instance.IGetInterferenceComponents

	@i_get_interference_components.setter
	def i_get_interference_components(self, value):
		"""Calculates and gets the interfering components."""
		self._instance.IGetInterferenceComponents = value

	@property
	def i_get_interferences(self):
		"""Calculates and gets the interferences."""
		return self._instance.IGetInterferences

	@i_get_interferences.setter
	def i_get_interferences(self, value):
		"""Calculates and gets the interferences."""
		self._instance.IGetInterferences = value

	@property
	def set_components_and_transforms(self):
		"""Sets the interfering components and their transforms."""
		return self._instance.SetComponentsAndTransforms

	@set_components_and_transforms.setter
	def set_components_and_transforms(self, value):
		"""Sets the interfering components and their transforms."""
		self._instance.SetComponentsAndTransforms = value

