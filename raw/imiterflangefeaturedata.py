# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMiterFlangeFeatureData_members.html
class IMiterFlangeFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bend_radius(self):
		"""Gets or sets the bend radius for this miter flange feature."""
		return self._instance.BendRadius

	@bend_radius.setter
	def bend_radius(self, value):
		"""Gets or sets the bend radius for this miter flange feature."""
		self._instance.BendRadius = value

	@property
	def edges(self):
		"""Gets or sets the edges for this miter flange feature."""
		return self._instance.Edges

	@edges.setter
	def edges(self, value):
		"""Gets or sets the edges for this miter flange feature."""
		self._instance.Edges = value

	@property
	def end_offset(self):
		"""Gets or sets the end offset for this miter flange."""
		return self._instance.EndOffset

	@end_offset.setter
	def end_offset(self, value):
		"""Gets or sets the end offset for this miter flange."""
		self._instance.EndOffset = value

	@property
	def gap_distance(self):
		"""Gets or sets the gap distance of the tear for this miter flange feature."""
		return self._instance.GapDistance

	@gap_distance.setter
	def gap_distance(self, value):
		"""Gets or sets the gap distance of the tear for this miter flange feature."""
		self._instance.GapDistance = value

	@property
	def position_type(self):
		"""Gets or sets the position for this miter flange feature."""
		return self._instance.PositionType

	@position_type.setter
	def position_type(self, value):
		"""Gets or sets the position for this miter flange feature."""
		self._instance.PositionType = value

	@property
	def relief_depth(self):
		"""Gets or sets the relief depth for this miter flange."""
		return self._instance.ReliefDepth

	@relief_depth.setter
	def relief_depth(self, value):
		"""Gets or sets the relief depth for this miter flange."""
		self._instance.ReliefDepth = value

	@property
	def relief_ratio(self):
		"""gets or sets the relief ratio for this miter flange."""
		return self._instance.ReliefRatio

	@relief_ratio.setter
	def relief_ratio(self, value):
		"""gets or sets the relief ratio for this miter flange."""
		self._instance.ReliefRatio = value

	@property
	def relief_type(self):
		"""Gets or sets the relief type for this miter flange."""
		return self._instance.ReliefType

	@relief_type.setter
	def relief_type(self, value):
		"""Gets or sets the relief type for this miter flange."""
		self._instance.ReliefType = value

	@property
	def relief_width(self):
		"""Gets or sets the relief width for this miter flange."""
		return self._instance.ReliefWidth

	@relief_width.setter
	def relief_width(self, value):
		"""Gets or sets the relief width for this miter flange."""
		self._instance.ReliefWidth = value

	@property
	def start_offset(self):
		"""Gets or sets the start offset for this miter flange."""
		return self._instance.StartOffset

	@start_offset.setter
	def start_offset(self, value):
		"""Gets or sets the start offset for this miter flange."""
		self._instance.StartOffset = value

	@property
	def use_default_bend_allowance(self):
		"""Gets or sets whether to use the default bend allowance for this miter flange feature."""
		return self._instance.UseDefaultBendAllowance

	@use_default_bend_allowance.setter
	def use_default_bend_allowance(self, value):
		"""Gets or sets whether to use the default bend allowance for this miter flange feature."""
		self._instance.UseDefaultBendAllowance = value

	@property
	def use_default_bend_radius(self):
		"""Gets or sets whether to use the default bend radius for this miter flange feature."""
		return self._instance.UseDefaultBendRadius

	@use_default_bend_radius.setter
	def use_default_bend_radius(self, value):
		"""Gets or sets whether to use the default bend radius for this miter flange feature."""
		self._instance.UseDefaultBendRadius = value

	@property
	def use_default_bend_relief(self):
		"""Gets or sets whether to use the default bend relief for this miter flange feature."""
		return self._instance.UseDefaultBendRelief

	@use_default_bend_relief.setter
	def use_default_bend_relief(self, value):
		"""Gets or sets whether to use the default bend relief for this miter flange feature."""
		self._instance.UseDefaultBendRelief = value

	@property
	def use_position_trim_side_bends(self):
		"""Gets or sets whether to remove extra material in neighboring bends for this miter flange feature."""
		return self._instance.UsePositionTrimSideBends

	@use_position_trim_side_bends.setter
	def use_position_trim_side_bends(self, value):
		"""Gets or sets whether to remove extra material in neighboring bends for this miter flange feature."""
		self._instance.UsePositionTrimSideBends = value

	@property
	def use_relief_ratio(self):
		"""Gets or sets whether to use the specified relief ratio for this miter flange."""
		return self._instance.UseReliefRatio

	@use_relief_ratio.setter
	def use_relief_ratio(self, value):
		"""Gets or sets whether to use the specified relief ratio for this miter flange."""
		self._instance.UseReliefRatio = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this miter flange feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this miter flange feature."""
		self._instance.AccessSelections = value

	@property
	def get_custom_bend_allowance(self):
		"""Gets the custom bend allowance for this miter flange feature."""
		return self._instance.GetCustomBendAllowance

	@get_custom_bend_allowance.setter
	def get_custom_bend_allowance(self, value):
		"""Gets the custom bend allowance for this miter flange feature."""
		self._instance.GetCustomBendAllowance = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this miter flange feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this miter flange feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_edges(self):
		"""Gets the edges for this miter flange feature."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Gets the edges for this miter flange feature."""
		self._instance.IGetEdges = value

	@property
	def i_get_edges_count(self):
		"""Gets the number of edges for this miter flange feature."""
		return self._instance.IGetEdgesCount

	@i_get_edges_count.setter
	def i_get_edges_count(self, value):
		"""Gets the number of edges for this miter flange feature."""
		self._instance.IGetEdgesCount = value

	@property
	def i_set_edges(self):
		"""Sets the edges for this miter flange feature."""
		return self._instance.ISetEdges

	@i_set_edges.setter
	def i_set_edges(self, value):
		"""Sets the edges for this miter flange feature."""
		self._instance.ISetEdges = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the miter flange feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the miter flange feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_custom_bend_allowance(self):
		"""Sets the custom bend allowance for this miter flange feature."""
		return self._instance.SetCustomBendAllowance

	@set_custom_bend_allowance.setter
	def set_custom_bend_allowance(self, value):
		"""Sets the custom bend allowance for this miter flange feature."""
		self._instance.SetCustomBendAllowance = value

