# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html
class IMirrorPartFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def absorbed_sketches(self):
		"""Gets or sets whether to import absorbed sketches."""
		return self._instance.AbsorbedSketches

	@absorbed_sketches.setter
	def absorbed_sketches(self, value):
		"""Gets or sets whether to import absorbed sketches."""
		self._instance.AbsorbedSketches = value

	@property
	def axes(self):
		"""Gets or sets whether to import axes."""
		return self._instance.Axes

	@axes.setter
	def axes(self, value):
		"""Gets or sets whether to import axes."""
		self._instance.Axes = value

	@property
	def coordinate_systems(self):
		"""Gets or sets whether to import coordinate systems."""
		return self._instance.CoordinateSystems

	@coordinate_systems.setter
	def coordinate_systems(self, value):
		"""Gets or sets whether to import coordinate systems."""
		self._instance.CoordinateSystems = value

	@property
	def cosmetic_threads(self):
		"""Gets or sets whether to import cosmetic threads."""
		return self._instance.CosmeticThreads

	@cosmetic_threads.setter
	def cosmetic_threads(self, value):
		"""Gets or sets whether to import cosmetic threads."""
		self._instance.CosmeticThreads = value

	@property
	def custom_properties(self):
		"""Gets or sets whether to import custom properties."""
		return self._instance.CustomProperties

	@custom_properties.setter
	def custom_properties(self, value):
		"""Gets or sets whether to import custom properties."""
		self._instance.CustomProperties = value

	@property
	def cut_list_properties(self):
		"""Gets or sets whether to import cut-list properties."""
		return self._instance.CutListProperties

	@cut_list_properties.setter
	def cut_list_properties(self, value):
		"""Gets or sets whether to import cut-list properties."""
		self._instance.CutListProperties = value

	@property
	def dim_xpert_annotations(self):
		"""Gets or sets whether to import DimXpert annotations."""
		return self._instance.DimXpertAnnotations

	@dim_xpert_annotations.setter
	def dim_xpert_annotations(self, value):
		"""Gets or sets whether to import DimXpert annotations."""
		self._instance.DimXpertAnnotations = value

	@property
	def hole_wizard_data(self):
		"""Gets or sets whether to import hole wizard data."""
		return self._instance.HoleWizardData

	@hole_wizard_data.setter
	def hole_wizard_data(self, value):
		"""Gets or sets whether to import hole wizard data."""
		self._instance.HoleWizardData = value

	@property
	def model_dimensions(self):
		"""Gets or sets whether to import model dimensions."""
		return self._instance.ModelDimensions

	@model_dimensions.setter
	def model_dimensions(self, value):
		"""Gets or sets whether to import model dimensions."""
		self._instance.ModelDimensions = value

	@property
	def path_name(self):
		"""Gets the path and file name of the derived mirror part feature."""
		return self._instance.PathName

	@path_name.setter
	def path_name(self, value):
		"""Gets the path and file name of the derived mirror part feature."""
		self._instance.PathName = value

	@property
	def planes(self):
		"""Gets or sets whether to import planes."""
		return self._instance.Planes

	@planes.setter
	def planes(self, value):
		"""Gets or sets whether to import planes."""
		self._instance.Planes = value

	@property
	def sheet_metal_information(self):
		"""Gets or sets whether to transfer the sheet-metal and flat-pattern information from the original sheet-metal part to the mirrored part."""
		return self._instance.SheetMetalInformation

	@sheet_metal_information.setter
	def sheet_metal_information(self, value):
		"""Gets or sets whether to transfer the sheet-metal and flat-pattern information from the original sheet-metal part to the mirrored part."""
		self._instance.SheetMetalInformation = value

	@property
	def solid_bodies(self):
		"""Gets or sets whether to import solid bodies."""
		return self._instance.SolidBodies

	@solid_bodies.setter
	def solid_bodies(self, value):
		"""Gets or sets whether to import solid bodies."""
		self._instance.SolidBodies = value

	@property
	def surface_bodies(self):
		"""Gets or sets whether to import surface bodies."""
		return self._instance.SurfaceBodies

	@surface_bodies.setter
	def surface_bodies(self, value):
		"""Gets or sets whether to import surface bodies."""
		self._instance.SurfaceBodies = value

	@property
	def unabsorbed_sketches(self):
		"""Gets or sets whether to import unabsorbed sketches."""
		return self._instance.UnabsorbedSketches

	@unabsorbed_sketches.setter
	def unabsorbed_sketches(self, value):
		"""Gets or sets whether to import unabsorbed sketches."""
		self._instance.UnabsorbedSketches = value

	@property
	def unlocked_properties(self):
		"""Gets or sets whether to enable editing of the sheet-metal definition in this mirrored sheet-metal part."""
		return self._instance.UnlockedProperties

	@unlocked_properties.setter
	def unlocked_properties(self, value):
		"""Gets or sets whether to enable editing of the sheet-metal definition in this mirrored sheet-metal part."""
		self._instance.UnlockedProperties = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define the mirror part feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define the mirror part feature."""
		self._instance.AccessSelections = value

	@property
	def get_mirror_plane(self):
		"""Gets the plane about which this part is mirrored."""
		return self._instance.GetMirrorPlane

	@get_mirror_plane.setter
	def get_mirror_plane(self, value):
		"""Gets the plane about which this part is mirrored."""
		self._instance.GetMirrorPlane = value

	@property
	def get_mirror_plane_type(self):
		"""Gets whether the mirror plane is a face or a reference plane."""
		return self._instance.GetMirrorPlaneType

	@get_mirror_plane_type.setter
	def get_mirror_plane_type(self, value):
		"""Gets whether the mirror plane is a face or a reference plane."""
		self._instance.GetMirrorPlaneType = value

	@property
	def get_model_doc(self):
		"""Gets the base model document of this mirror part feature."""
		return self._instance.GetModelDoc

	@get_model_doc.setter
	def get_model_doc(self, value):
		"""Gets the base model document of this mirror part feature."""
		self._instance.GetModelDoc = value

	@property
	def get_transform(self):
		"""Gets the transform of this mirror part feature."""
		return self._instance.GetTransform

	@get_transform.setter
	def get_transform(self, value):
		"""Gets the transform of this mirror part feature."""
		self._instance.GetTransform = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the mirror part feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the mirror part feature."""
		self._instance.ReleaseSelectionAccess = value

