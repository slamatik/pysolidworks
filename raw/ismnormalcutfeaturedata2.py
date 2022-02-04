# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2_members.html
class ISMNormalCutFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_propagation(self):
		"""Gets or sets whether to automatically add tangent faces to the cut-extrude face group."""
		return self._instance.AutoPropagation

	@auto_propagation.setter
	def auto_propagation(self, value):
		"""Gets or sets whether to automatically add tangent faces to the cut-extrude face group."""
		self._instance.AutoPropagation = value

	@property
	def cut_direction(self):
		"""Gets or sets the edge, linear curve, or planar face that defines the direction of the Normal Cut."""
		return self._instance.CutDirection

	@cut_direction.setter
	def cut_direction(self, value):
		"""Gets or sets the edge, linear curve, or planar face that defines the direction of the Normal Cut."""
		self._instance.CutDirection = value

	@property
	def layer_adjustment_value(self):
		"""Gets or sets the offset plane adjustment value."""
		return self._instance.LayerAdjustmentValue

	@layer_adjustment_value.setter
	def layer_adjustment_value(self, value):
		"""Gets or sets the offset plane adjustment value."""
		self._instance.LayerAdjustmentValue = value

	@property
	def link_to_k_factor(self):
		"""Gets or sets whether to link to a K-Factor when adjusting the offset plane of this Normal Cut."""
		return self._instance.LinkToKFactor

	@link_to_k_factor.setter
	def link_to_k_factor(self, value):
		"""Gets or sets whether to link to a K-Factor when adjusting the offset plane of this Normal Cut."""
		self._instance.LinkToKFactor = value

	@property
	def normal_cut_parameters(self):
		"""Gets or sets the Normal Cut parameters."""
		return self._instance.NormalCutParameters

	@normal_cut_parameters.setter
	def normal_cut_parameters(self, value):
		"""Gets or sets the Normal Cut parameters."""
		self._instance.NormalCutParameters = value

	@property
	def offset_plane_reference(self):
		"""Gets or sets the offset plane reference for the Normal Cut."""
		return self._instance.OffsetPlaneReference

	@offset_plane_reference.setter
	def offset_plane_reference(self, value):
		"""Gets or sets the offset plane reference for the Normal Cut."""
		self._instance.OffsetPlaneReference = value

	@property
	def optimize_geometry(self):
		"""Gets or sets whether to optimize the geometry of the Normal Cut."""
		return self._instance.OptimizeGeometry

	@optimize_geometry.setter
	def optimize_geometry(self, value):
		"""Gets or sets whether to optimize the geometry of the Normal Cut."""
		self._instance.OptimizeGeometry = value

	@property
	def access_selections(self):
		"""Gains access to the selections defining this sheet metal Normal Cut feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections defining this sheet metal Normal Cut feature."""
		self._instance.AccessSelections = value

	@property
	def create_group(self):
		"""Creates a group of connected faces to cut."""
		return self._instance.CreateGroup

	@create_group.setter
	def create_group(self, value):
		"""Creates a group of connected faces to cut."""
		self._instance.CreateGroup = value

	@property
	def delete_group_by_name(self):
		"""Deletes the specified face group."""
		return self._instance.DeleteGroupByName

	@delete_group_by_name.setter
	def delete_group_by_name(self, value):
		"""Deletes the specified face group."""
		self._instance.DeleteGroupByName = value

	@property
	def get_group_by_name(self):
		"""Gets the specified face group."""
		return self._instance.GetGroupByName

	@get_group_by_name.setter
	def get_group_by_name(self, value):
		"""Gets the specified face group."""
		self._instance.GetGroupByName = value

	@property
	def get_group_names(self):
		"""Gets an array of face group names."""
		return self._instance.GetGroupNames

	@get_group_names.setter
	def get_group_names(self, value):
		"""Gets an array of face group names."""
		self._instance.GetGroupNames = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this sheet metal Normal Cut feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this sheet metal Normal Cut feature."""
		self._instance.ReleaseSelectionAccess = value

