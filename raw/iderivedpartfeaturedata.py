# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPartFeatureData_members.html
class IDerivedPartFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def import_absorbed_sketches(self):
		"""Gets or sets whether to import absorbed sketches with the derived part feature."""
		return self._instance.ImportAbsorbedSketches

	@import_absorbed_sketches.setter
	def import_absorbed_sketches(self, value):
		"""Gets or sets whether to import absorbed sketches with the derived part feature."""
		self._instance.ImportAbsorbedSketches = value

	@property
	def import_axis(self):
		"""Gets or sets whether to import the axis with the derived part feature."""
		return self._instance.ImportAxis

	@import_axis.setter
	def import_axis(self, value):
		"""Gets or sets whether to import the axis with the derived part feature."""
		self._instance.ImportAxis = value

	@property
	def import_coordinate_systems(self):
		"""Gets or sets whether to import coordinate systems with the derived part feature."""
		return self._instance.ImportCoordinateSystems

	@import_coordinate_systems.setter
	def import_coordinate_systems(self, value):
		"""Gets or sets whether to import coordinate systems with the derived part feature."""
		self._instance.ImportCoordinateSystems = value

	@property
	def import_c_thread(self):
		"""Gets or sets whether to import cosmetic threads with the derived part feature."""
		return self._instance.ImportCThread

	@import_c_thread.setter
	def import_c_thread(self, value):
		"""Gets or sets whether to import cosmetic threads with the derived part feature."""
		self._instance.ImportCThread = value

	@property
	def import_custom_properties(self):
		"""Gets or sets which custom properties to import with the derived part feature."""
		return self._instance.ImportCustomProperties

	@import_custom_properties.setter
	def import_custom_properties(self, value):
		"""Gets or sets which custom properties to import with the derived part feature."""
		self._instance.ImportCustomProperties = value

	@property
	def import_cut_list_properties(self):
		"""Gets or sets whether to import cut list properties with the derived part feature."""
		return self._instance.ImportCutListProperties

	@import_cut_list_properties.setter
	def import_cut_list_properties(self, value):
		"""Gets or sets whether to import cut list properties with the derived part feature."""
		self._instance.ImportCutListProperties = value

	@property
	def import_hole_wizard_data(self):
		"""Gets or sets whether to import Hole Wizard data with the derived part feature."""
		return self._instance.ImportHoleWizardData

	@import_hole_wizard_data.setter
	def import_hole_wizard_data(self, value):
		"""Gets or sets whether to import Hole Wizard data with the derived part feature."""
		self._instance.ImportHoleWizardData = value

	@property
	def import_material(self):
		"""Gets or sets whether to import material with the derived part feature."""
		return self._instance.ImportMaterial

	@import_material.setter
	def import_material(self, value):
		"""Gets or sets whether to import material with the derived part feature."""
		self._instance.ImportMaterial = value

	@property
	def import_model_dimensions(self):
		"""Gets or sets whether to import model dimensions with the derived part feature."""
		return self._instance.ImportModelDimensions

	@import_model_dimensions.setter
	def import_model_dimensions(self, value):
		"""Gets or sets whether to import model dimensions with the derived part feature."""
		self._instance.ImportModelDimensions = value

	@property
	def import_plane(self):
		"""Gets or sets whether to import planes with the derived part feature."""
		return self._instance.ImportPlane

	@import_plane.setter
	def import_plane(self, value):
		"""Gets or sets whether to import planes with the derived part feature."""
		self._instance.ImportPlane = value

	@property
	def import_sheet_metal_information(self):
		"""Gets or sets how to import sheet metal information with the derived part feature."""
		return self._instance.ImportSheetMetalInformation

	@import_sheet_metal_information.setter
	def import_sheet_metal_information(self, value):
		"""Gets or sets how to import sheet metal information with the derived part feature."""
		self._instance.ImportSheetMetalInformation = value

	@property
	def import_solid_bodies(self):
		"""Gets or sets whether to import solid bodies with the derived part feature."""
		return self._instance.ImportSolidBodies

	@import_solid_bodies.setter
	def import_solid_bodies(self, value):
		"""Gets or sets whether to import solid bodies with the derived part feature."""
		self._instance.ImportSolidBodies = value

	@property
	def import_surf(self):
		"""Gets or sets whether to import surface bodies with the derived part feature."""
		return self._instance.ImportSurf

	@import_surf.setter
	def import_surf(self, value):
		"""Gets or sets whether to import surface bodies with the derived part feature."""
		self._instance.ImportSurf = value

	@property
	def import_un_absorbed_sketches(self):
		"""Gets or sets whether to import unabsorbed sketches with the derived part feature."""
		return self._instance.ImportUnAbsorbedSketches

	@import_un_absorbed_sketches.setter
	def import_un_absorbed_sketches(self, value):
		"""Gets or sets whether to import unabsorbed sketches with the derived part feature."""
		self._instance.ImportUnAbsorbedSketches = value

	@property
	def part_configuration(self):
		"""Gets or sets the part configuration to use to create the derived part feature."""
		return self._instance.PartConfiguration

	@part_configuration.setter
	def part_configuration(self, value):
		"""Gets or sets the part configuration to use to create the derived part feature."""
		self._instance.PartConfiguration = value

	@property
	def path_name(self):
		"""Gets the path for the derived part feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.PathName

	@path_name.setter
	def path_name(self, value):
		"""Gets the path for the derived part feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.PathName = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define this derived part feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define this derived part feature."""
		self._instance.AccessSelections = value

	@property
	def get_model_doc(self):
		"""Gets the model document from which this part was derived (i.e., the base model document)."""
		return self._instance.GetModelDoc

	@get_model_doc.setter
	def get_model_doc(self, value):
		"""Gets the model document from which this part was derived (i.e., the base model document)."""
		self._instance.GetModelDoc = value

	@property
	def get_move_feature(self):
		"""Gets the move/copy feature belonging to this derived part feature."""
		return self._instance.GetMoveFeature

	@get_move_feature.setter
	def get_move_feature(self, value):
		"""Gets the move/copy feature belonging to this derived part feature."""
		self._instance.GetMoveFeature = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections used to define this derived part feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections used to define this derived part feature."""
		self._instance.IAccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe this derived part feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe this derived part feature."""
		self._instance.ReleaseSelectionAccess = value

