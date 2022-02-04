# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html
class IEdgeFlangeFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle_reference(self):
		"""Gets or sets the reference face used to define the bend angle of this edge flange."""
		return self._instance.AngleReference

	@angle_reference.setter
	def angle_reference(self, value):
		"""Gets or sets the reference face used to define the bend angle of this edge flange."""
		self._instance.AngleReference = value

	@property
	def auto_relief_type(self):
		"""Gets or sets the auto-relief type for this edge flange."""
		return self._instance.AutoReliefType

	@auto_relief_type.setter
	def auto_relief_type(self, value):
		"""Gets or sets the auto-relief type for this edge flange."""
		self._instance.AutoReliefType = value

	@property
	def bend_angle(self):
		"""Gets or sets the bend angle of the edge flange."""
		return self._instance.BendAngle

	@bend_angle.setter
	def bend_angle(self, value):
		"""Gets or sets the bend angle of the edge flange."""
		self._instance.BendAngle = value

	@property
	def bend_radius(self):
		"""Gets or sets the bend radius of the edge flange."""
		return self._instance.BendRadius

	@bend_radius.setter
	def bend_radius(self, value):
		"""Gets or sets the bend radius of the edge flange."""
		self._instance.BendRadius = value

	@property
	def edges(self):
		"""Gets the edges for this edge flange. 
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Edges

	@edges.setter
	def edges(self, value):
		"""Gets the edges for this edge flange. 
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Edges = value

	@property
	def gap_distance(self):
		"""Gets or sets the gap distance of the tear for this edge flange."""
		return self._instance.GapDistance

	@gap_distance.setter
	def gap_distance(self, value):
		"""Gets or sets the gap distance of the tear for this edge flange."""
		self._instance.GapDistance = value

	@property
	def lock_angle(self):
		"""Gets or sets whether to lock the flange angle for the Up To Edge and Merge option of this edge flange."""
		return self._instance.LockAngle

	@lock_angle.setter
	def lock_angle(self, value):
		"""Gets or sets whether to lock the flange angle for the Up To Edge and Merge option of this edge flange."""
		self._instance.LockAngle = value

	@property
	def normal_to_flange_plane(self):
		"""Gets or sets whether the Up To Vertex is on a plane that is normal to the end face of this edge flange."""
		return self._instance.NormalToFlangePlane

	@normal_to_flange_plane.setter
	def normal_to_flange_plane(self, value):
		"""Gets or sets whether the Up To Vertex is on a plane that is normal to the end face of this edge flange."""
		self._instance.NormalToFlangePlane = value

	@property
	def offset_dim_type(self):
		"""Gets or sets the flange length origin type for dimensioning this edge flange."""
		return self._instance.OffsetDimType

	@offset_dim_type.setter
	def offset_dim_type(self, value):
		"""Gets or sets the flange length origin type for dimensioning this edge flange."""
		self._instance.OffsetDimType = value

	@property
	def offset_distance(self):
		"""Gets or sets the flange length for this edge flange."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the flange length for this edge flange."""
		self._instance.OffsetDistance = value

	@property
	def offset_reference(self):
		"""Gets or sets the flange length reference for this edge flange."""
		return self._instance.OffsetReference

	@offset_reference.setter
	def offset_reference(self, value):
		"""Gets or sets the flange length reference for this edge flange."""
		self._instance.OffsetReference = value

	@property
	def offset_type(self):
		"""Gets or sets the flange length end condition for this edge flange."""
		return self._instance.OffsetType

	@offset_type.setter
	def offset_type(self, value):
		"""Gets or sets the flange length end condition for this edge flange."""
		self._instance.OffsetType = value

	@property
	def perpendicular_to_face(self):
		"""Gets or sets whether to set this edge flange perpendicular to the angle reference face."""
		return self._instance.PerpendicularToFace

	@perpendicular_to_face.setter
	def perpendicular_to_face(self, value):
		"""Gets or sets whether to set this edge flange perpendicular to the angle reference face."""
		self._instance.PerpendicularToFace = value

	@property
	def position_offset_distance(self):
		"""Gets or sets the flange position offset for this edge flange."""
		return self._instance.PositionOffsetDistance

	@position_offset_distance.setter
	def position_offset_distance(self, value):
		"""Gets or sets the flange position offset for this edge flange."""
		self._instance.PositionOffsetDistance = value

	@property
	def position_offset_reference(self):
		"""Gets or sets the flange position offset reference for this edge flange."""
		return self._instance.PositionOffsetReference

	@position_offset_reference.setter
	def position_offset_reference(self, value):
		"""Gets or sets the flange position offset reference for this edge flange."""
		self._instance.PositionOffsetReference = value

	@property
	def position_offset_type(self):
		"""Gets or sets the flange position offset end condition of this edge flange."""
		return self._instance.PositionOffsetType

	@position_offset_type.setter
	def position_offset_type(self, value):
		"""Gets or sets the flange position offset end condition of this edge flange."""
		self._instance.PositionOffsetType = value

	@property
	def position_type(self):
		"""Gets or sets the flange position of this edge flange."""
		return self._instance.PositionType

	@position_type.setter
	def position_type(self, value):
		"""Gets or sets the flange position of this edge flange."""
		self._instance.PositionType = value

	@property
	def relief_depth(self):
		"""Gets or sets the relief depth of the edge flange."""
		return self._instance.ReliefDepth

	@relief_depth.setter
	def relief_depth(self, value):
		"""Gets or sets the relief depth of the edge flange."""
		self._instance.ReliefDepth = value

	@property
	def relief_ratio(self):
		"""Gets or sets the relief ratio for this edge flange."""
		return self._instance.ReliefRatio

	@relief_ratio.setter
	def relief_ratio(self, value):
		"""Gets or sets the relief ratio for this edge flange."""
		self._instance.ReliefRatio = value

	@property
	def relief_tear_type(self):
		"""Gets or sets the type of relief tear for this edge flange."""
		return self._instance.ReliefTearType

	@relief_tear_type.setter
	def relief_tear_type(self, value):
		"""Gets or sets the type of relief tear for this edge flange."""
		self._instance.ReliefTearType = value

	@property
	def relief_width(self):
		"""Gets or sets the width of the relief for this edge flange."""
		return self._instance.ReliefWidth

	@relief_width.setter
	def relief_width(self, value):
		"""Gets or sets the width of the relief for this edge flange."""
		self._instance.ReliefWidth = value

	@property
	def reverse_offset(self):
		"""Gets or sets whether to flip the flange length for this edge flange."""
		return self._instance.ReverseOffset

	@reverse_offset.setter
	def reverse_offset(self, value):
		"""Gets or sets whether to flip the flange length for this edge flange."""
		self._instance.ReverseOffset = value

	@property
	def reverse_position_offset(self):
		"""Gets or sets whether to reverse the flange position offset for this edge flange."""
		return self._instance.ReversePositionOffset

	@reverse_position_offset.setter
	def reverse_position_offset(self, value):
		"""Gets or sets whether to reverse the flange position offset for this edge flange."""
		self._instance.ReversePositionOffset = value

	@property
	def use_default_bend_allowance(self):
		"""Gets or sets whether to use the default bend allowance for this edge flange."""
		return self._instance.UseDefaultBendAllowance

	@use_default_bend_allowance.setter
	def use_default_bend_allowance(self, value):
		"""Gets or sets whether to use the default bend allowance for this edge flange."""
		self._instance.UseDefaultBendAllowance = value

	@property
	def use_default_bend_radius(self):
		"""Gets or sets whether to use the default sheet metal bend radius for this edge flange."""
		return self._instance.UseDefaultBendRadius

	@use_default_bend_radius.setter
	def use_default_bend_radius(self, value):
		"""Gets or sets whether to use the default sheet metal bend radius for this edge flange."""
		self._instance.UseDefaultBendRadius = value

	@property
	def use_default_bend_relief(self):
		"""Gets or sets whether to use the default bend relief for this edge flange."""
		return self._instance.UseDefaultBendRelief

	@use_default_bend_relief.setter
	def use_default_bend_relief(self, value):
		"""Gets or sets whether to use the default bend relief for this edge flange."""
		self._instance.UseDefaultBendRelief = value

	@property
	def use_position_offset(self):
		"""Gets or sets whether to offset this edge flange from the sheet metal body."""
		return self._instance.UsePositionOffset

	@use_position_offset.setter
	def use_position_offset(self, value):
		"""Gets or sets whether to offset this edge flange from the sheet metal body."""
		self._instance.UsePositionOffset = value

	@property
	def use_position_trim_side_bends(self):
		"""Gets or sets whether to trim side bends for this edge flange."""
		return self._instance.UsePositionTrimSideBends

	@use_position_trim_side_bends.setter
	def use_position_trim_side_bends(self, value):
		"""Gets or sets whether to trim side bends for this edge flange."""
		self._instance.UsePositionTrimSideBends = value

	@property
	def use_relief_ratio(self):
		"""Gets or sets whether to use the relief ratio for this edge flange."""
		return self._instance.UseReliefRatio

	@use_relief_ratio.setter
	def use_relief_ratio(self, value):
		"""Gets or sets whether to use the relief ratio for this edge flange."""
		self._instance.UseReliefRatio = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe this edge flange."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe this edge flange."""
		self._instance.AccessSelections = value

	@property
	def add_edges(self):
		"""Adds edges to this edge flange."""
		return self._instance.AddEdges

	@add_edges.setter
	def add_edges(self, value):
		"""Adds edges to this edge flange."""
		self._instance.AddEdges = value

	@property
	def get_custom_bend_allowance(self):
		"""Gets the custom bend allowance for this edge flange."""
		return self._instance.GetCustomBendAllowance

	@get_custom_bend_allowance.setter
	def get_custom_bend_allowance(self, value):
		"""Gets the custom bend allowance for this edge flange."""
		self._instance.GetCustomBendAllowance = value

	@property
	def get_edge_count(self):
		"""Gets the number of edges for this edge flange."""
		return self._instance.GetEdgeCount

	@get_edge_count.setter
	def get_edge_count(self, value):
		"""Gets the number of edges for this edge flange."""
		self._instance.GetEdgeCount = value

	@property
	def get_position_reference_type(self):
		"""Gets the position reference type from the edge flange."""
		return self._instance.GetPositionReferenceType

	@get_position_reference_type.setter
	def get_position_reference_type(self, value):
		"""Gets the position reference type from the edge flange."""
		self._instance.GetPositionReferenceType = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that describe this edge flange."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that describe this edge flange."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_edges(self):
		"""Gets the edges for this edge flange."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Gets the edges for this edge flange."""
		self._instance.IGetEdges = value

	@property
	def i_set_edges(self):
		"""Sets the edges for this edge flange."""
		return self._instance.ISetEdges

	@i_set_edges.setter
	def i_set_edges(self, value):
		"""Sets the edges for this edge flange."""
		self._instance.ISetEdges = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe this edge flange feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe this edge flange feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def remove_edges(self):
		"""Removes edges from this edge flange."""
		return self._instance.RemoveEdges

	@remove_edges.setter
	def remove_edges(self, value):
		"""Removes edges from this edge flange."""
		self._instance.RemoveEdges = value

	@property
	def set_custom_bend_allowance(self):
		"""Sets the custom bend allowance for this edge flange."""
		return self._instance.SetCustomBendAllowance

	@set_custom_bend_allowance.setter
	def set_custom_bend_allowance(self, value):
		"""Sets the custom bend allowance for this edge flange."""
		self._instance.SetCustomBendAllowance = value

