# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorComponentFeatureData_members.html
class IMirrorComponentFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def alignment_references(self):
		"""Gets or sets the alignment references for components whose orientation axes align to them."""
		return self._instance.AlignmentReferences

	@alignment_references.setter
	def alignment_references(self, value):
		"""Gets or sets the alignment references for components whose orientation axes align to them."""
		self._instance.AlignmentReferences = value

	@property
	def break_links_to_original_part(self):
		"""Gets or sets whether to break links between opposite-hand components and original components."""
		return self._instance.BreakLinksToOriginalPart

	@break_links_to_original_part.setter
	def break_links_to_original_part(self, value):
		"""Gets or sets whether to break links between opposite-hand components and original components."""
		self._instance.BreakLinksToOriginalPart = value

	@property
	def component_orientations_align_to_component_origin(self):
		"""Gets or sets the array of orientations for the components whose axes align to origins."""
		return self._instance.ComponentOrientationsAlignToComponentOrigin

	@component_orientations_align_to_component_origin.setter
	def component_orientations_align_to_component_origin(self, value):
		"""Gets or sets the array of orientations for the components whose axes align to origins."""
		self._instance.ComponentOrientationsAlignToComponentOrigin = value

	@property
	def component_orientations_align_to_selection(self):
		"""Gets or sets the array of orientations for the components whose axes align to a selected reference."""
		return self._instance.ComponentOrientationsAlignToSelection

	@component_orientations_align_to_selection.setter
	def component_orientations_align_to_selection(self, value):
		"""Gets or sets the array of orientations for the components whose axes align to a selected reference."""
		self._instance.ComponentOrientationsAlignToSelection = value

	@property
	def components_to_instance_align_to_component_origin(self):
		"""Gets or sets the array of components whose orientation axes align to origins."""
		return self._instance.ComponentsToInstanceAlignToComponentOrigin

	@components_to_instance_align_to_component_origin.setter
	def components_to_instance_align_to_component_origin(self, value):
		"""Gets or sets the array of components whose orientation axes align to origins."""
		self._instance.ComponentsToInstanceAlignToComponentOrigin = value

	@property
	def components_to_instance_align_to_selection(self):
		"""Gets or sets the array of components whose orientation axes align to selected references."""
		return self._instance.ComponentsToInstanceAlignToSelection

	@components_to_instance_align_to_selection.setter
	def components_to_instance_align_to_selection(self, value):
		"""Gets or sets the array of components whose orientation axes align to selected references."""
		self._instance.ComponentsToInstanceAlignToSelection = value

	@property
	def create_derived_configurations(self):
		"""Gets or sets whether to create a derived configuration of the opposite-hand components in the original assembly."""
		return self._instance.CreateDerivedConfigurations

	@create_derived_configurations.setter
	def create_derived_configurations(self, value):
		"""Gets or sets whether to create a derived configuration of the opposite-hand components in the original assembly."""
		self._instance.CreateDerivedConfigurations = value

	@property
	def dim_xpert_scheme(self):
		"""Gets or sets whether to copy the DimXpert scheme of the original components to the opposite-hand versions."""
		return self._instance.DimXpertScheme

	@dim_xpert_scheme.setter
	def dim_xpert_scheme(self, value):
		"""Gets or sets whether to copy the DimXpert scheme of the original components to the opposite-hand versions."""
		self._instance.DimXpertScheme = value

	@property
	def flip_directions(self):
		"""Gets or sets whether to reverse the direction of alignment for selected alignment references."""
		return self._instance.FlipDirections

	@flip_directions.setter
	def flip_directions(self, value):
		"""Gets or sets whether to reverse the direction of alignment for selected alignment references."""
		self._instance.FlipDirections = value

	@property
	def force_use_seed_configuration(self):
		"""Gets or sets whether to synchronize the configuration of mirror components with the configuration of the mirrored component in this mirror component feature."""
		return self._instance.ForceUseSeedConfiguration

	@force_use_seed_configuration.setter
	def force_use_seed_configuration(self, value):
		"""Gets or sets whether to synchronize the configuration of mirror components with the configuration of the mirrored component in this mirror component feature."""
		self._instance.ForceUseSeedConfiguration = value

	@property
	def mirror_components_folder_location(self):
		"""Gets or sets the existing folder where all opposite-hand versions are saved."""
		return self._instance.MirrorComponentsFolderLocation

	@mirror_components_folder_location.setter
	def mirror_components_folder_location(self, value):
		"""Gets or sets the existing folder where all opposite-hand versions are saved."""
		self._instance.MirrorComponentsFolderLocation = value

	@property
	def mirrored_component_filenames(self):
		"""Gets or sets the file names of the opposite-hand component versions."""
		return self._instance.MirroredComponentFilenames

	@mirrored_component_filenames.setter
	def mirrored_component_filenames(self, value):
		"""Gets or sets the file names of the opposite-hand component versions."""
		self._instance.MirroredComponentFilenames = value

	@property
	def mirror_plane(self):
		"""Gets or sets the plane about which components are mirrored."""
		return self._instance.MirrorPlane

	@mirror_plane.setter
	def mirror_plane(self, value):
		"""Gets or sets the plane about which components are mirrored."""
		self._instance.MirrorPlane = value

	@property
	def mirror_transfer_options(self):
		"""Gets or sets the items to transfer to the opposite-hand versions."""
		return self._instance.MirrorTransferOptions

	@mirror_transfer_options.setter
	def mirror_transfer_options(self, value):
		"""Gets or sets the items to transfer to the opposite-hand versions."""
		self._instance.MirrorTransferOptions = value

	@property
	def mirror_type(self):
		"""Gets or sets the mirror position."""
		return self._instance.MirrorType

	@mirror_type.setter
	def mirror_type(self, value):
		"""Gets or sets the mirror position."""
		self._instance.MirrorType = value

	@property
	def name_modifier(self):
		"""Gets or sets the prefix or suffix to add to the file or configuration names of the components to be mirrored."""
		return self._instance.NameModifier

	@name_modifier.setter
	def name_modifier(self, value):
		"""Gets or sets the prefix or suffix to add to the file or configuration names of the components to be mirrored."""
		self._instance.NameModifier = value

	@property
	def name_modifier_type(self):
		"""Gets or sets the type of modifier to apply to the opposite-hand version file name."""
		return self._instance.NameModifierType

	@name_modifier_type.setter
	def name_modifier_type(self, value):
		"""Gets or sets the type of modifier to apply to the opposite-hand version file name."""
		self._instance.NameModifierType = value

	@property
	def opposite_hand_components(self):
		"""Gets or sets the array of components for which to create opposite-hand versions."""
		return self._instance.OppositeHandComponents

	@opposite_hand_components.setter
	def opposite_hand_components(self, value):
		"""Gets or sets the array of components for which to create opposite-hand versions."""
		self._instance.OppositeHandComponents = value

	@property
	def place_files_in_one_folder(self):
		"""Gets or sets whether to place the opposite-hand versions in one folder."""
		return self._instance.PlaceFilesInOneFolder

	@place_files_in_one_folder.setter
	def place_files_in_one_folder(self, value):
		"""Gets or sets whether to place the opposite-hand versions in one folder."""
		self._instance.PlaceFilesInOneFolder = value

	@property
	def preserve_z_axis(self):
		"""Gets or sets whether to preserve the orientation of the Z-axis in the opposite-hand versions."""
		return self._instance.PreserveZAxis

	@preserve_z_axis.setter
	def preserve_z_axis(self, value):
		"""Gets or sets whether to preserve the orientation of the Z-axis in the opposite-hand versions."""
		self._instance.PreserveZAxis = value

	@property
	def propagate_from_original_part(self):
		"""Gets or sets whether to propagate visual properties from the orginal part to the opposite-hand versions."""
		return self._instance.PropagateFromOriginalPart

	@propagate_from_original_part.setter
	def propagate_from_original_part(self, value):
		"""Gets or sets whether to propagate visual properties from the orginal part to the opposite-hand versions."""
		self._instance.PropagateFromOriginalPart = value

	@property
	def replace_file_locations(self):
		"""Gets or sets the file locations of existing files that are to be replaced with new opposite-hand versions."""
		return self._instance.ReplaceFileLocations

	@replace_file_locations.setter
	def replace_file_locations(self, value):
		"""Gets or sets the file locations of existing files that are to be replaced with new opposite-hand versions."""
		self._instance.ReplaceFileLocations = value

	@property
	def sync_flexible_sub_assemblies(self):
		"""Gets or sets whether to synchronize the movement of mirrored components with the movement of seed components in the flexible subassembly."""
		return self._instance.SyncFlexibleSubAssemblies

	@sync_flexible_sub_assemblies.setter
	def sync_flexible_sub_assemblies(self, value):
		"""Gets or sets whether to synchronize the movement of mirrored components with the movement of seed components in the flexible subassembly."""
		self._instance.SyncFlexibleSubAssemblies = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define the mirror component feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define the mirror component feature."""
		self._instance.AccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define this mirror component feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define this mirror component feature."""
		self._instance.ReleaseSelectionAccess = value

