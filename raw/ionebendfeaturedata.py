# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IOneBendFeatureData_members.html
class IOneBendFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_relief_type(self):
		"""Gets or sets the auto-relief type from this bend."""
		return self._instance.AutoReliefType

	@auto_relief_type.setter
	def auto_relief_type(self, value):
		"""Gets or sets the auto-relief type from this bend."""
		self._instance.AutoReliefType = value

	@property
	def bend_angle(self):
		"""Gets or sets the bend angle of this bend."""
		return self._instance.BendAngle

	@bend_angle.setter
	def bend_angle(self, value):
		"""Gets or sets the bend angle of this bend."""
		self._instance.BendAngle = value

	@property
	def bend_direction(self):
		"""Gets the direction of this bend."""
		return self._instance.BendDirection

	@bend_direction.setter
	def bend_direction(self, value):
		"""Gets the direction of this bend."""
		self._instance.BendDirection = value

	@property
	def bend_down(self):
		"""Gets or sets the bend-down state of this bend."""
		return self._instance.BendDown

	@bend_down.setter
	def bend_down(self, value):
		"""Gets or sets the bend-down state of this bend."""
		self._instance.BendDown = value

	@property
	def bend_order(self):
		"""Gets or sets the bend order of this bend."""
		return self._instance.BendOrder

	@bend_order.setter
	def bend_order(self, value):
		"""Gets or sets the bend order of this bend."""
		self._instance.BendOrder = value

	@property
	def bend_radius(self):
		"""Gets or sets the bend radius of this bend."""
		return self._instance.BendRadius

	@bend_radius.setter
	def bend_radius(self, value):
		"""Gets or sets the bend radius of this bend."""
		self._instance.BendRadius = value

	@property
	def flat_pattern_sketch_segments(self):
		"""Gets the sketch segments and bend lines for this bend."""
		return self._instance.FlatPatternSketchSegments2

	@flat_pattern_sketch_segments.setter
	def flat_pattern_sketch_segments(self, value):
		"""Gets the sketch segments and bend lines for this bend."""
		self._instance.FlatPatternSketchSegments2 = value

	@property
	def relief_depth(self):
		"""Gets or sets the relief depth for this bend."""
		return self._instance.ReliefDepth

	@relief_depth.setter
	def relief_depth(self, value):
		"""Gets or sets the relief depth for this bend."""
		self._instance.ReliefDepth = value

	@property
	def relief_ratio(self):
		"""Gets and sets the relief ratio for the one bend feature."""
		return self._instance.ReliefRatio

	@relief_ratio.setter
	def relief_ratio(self, value):
		"""Gets and sets the relief ratio for the one bend feature."""
		self._instance.ReliefRatio = value

	@property
	def relief_width(self):
		"""Gets or sets the relief width of this bend."""
		return self._instance.ReliefWidth

	@relief_width.setter
	def relief_width(self, value):
		"""Gets or sets the relief width of this bend."""
		self._instance.ReliefWidth = value

	@property
	def simplify_geometry(self):
		"""Gets or sets whether to simplify the geometry for this bend feature."""
		return self._instance.SimplifyGeometry

	@simplify_geometry.setter
	def simplify_geometry(self, value):
		"""Gets or sets whether to simplify the geometry for this bend feature."""
		self._instance.SimplifyGeometry = value

	@property
	def use_auto_relief(self):
		"""Gets or sets whether to use auto relief for this bend."""
		return self._instance.UseAutoRelief

	@use_auto_relief.setter
	def use_auto_relief(self, value):
		"""Gets or sets whether to use auto relief for this bend."""
		self._instance.UseAutoRelief = value

	@property
	def use_default_bend_allowance(self):
		"""Gets or sets whether to use the default bend allowance for this bend."""
		return self._instance.UseDefaultBendAllowance

	@use_default_bend_allowance.setter
	def use_default_bend_allowance(self, value):
		"""Gets or sets whether to use the default bend allowance for this bend."""
		self._instance.UseDefaultBendAllowance = value

	@property
	def use_default_bend_radius(self):
		"""Gets or sets whether to use the default bend radius of this bend."""
		return self._instance.UseDefaultBendRadius

	@use_default_bend_radius.setter
	def use_default_bend_radius(self, value):
		"""Gets or sets whether to use the default bend radius of this bend."""
		self._instance.UseDefaultBendRadius = value

	@property
	def use_default_bend_relief(self):
		"""Gets or sets whether to use the default bend relief of this bend."""
		return self._instance.UseDefaultBendRelief

	@use_default_bend_relief.setter
	def use_default_bend_relief(self, value):
		"""Gets or sets whether to use the default bend relief of this bend."""
		self._instance.UseDefaultBendRelief = value

	@property
	def use_relief_ratio(self):
		"""Gets or sets whether to use the relief ratio for this bend feature."""
		return self._instance.UseReliefRatio

	@use_relief_ratio.setter
	def use_relief_ratio(self, value):
		"""Gets or sets whether to use the relief ratio for this bend feature."""
		self._instance.UseReliefRatio = value

	@property
	def access_selections(self):
		"""Gains access to selections that define this bend feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections that define this bend feature."""
		self._instance.AccessSelections = value

	@property
	def get_custom_bend_allowance(self):
		"""Gets the custom bend allowance for this bend feature."""
		return self._instance.GetCustomBendAllowance

	@get_custom_bend_allowance.setter
	def get_custom_bend_allowance(self, value):
		"""Gets the custom bend allowance for this bend feature."""
		self._instance.GetCustomBendAllowance = value

	@property
	def get_flat_pattern_sketch_segment_count(self):
		"""Gets the number of sketch segments, including bend lines, in this bend."""
		return self._instance.GetFlatPatternSketchSegmentCount2

	@get_flat_pattern_sketch_segment_count.setter
	def get_flat_pattern_sketch_segment_count(self, value):
		"""Gets the number of sketch segments, including bend lines, in this bend."""
		self._instance.GetFlatPatternSketchSegmentCount2 = value

	@property
	def get_type(self):
		"""Gets the type of bend for this one bend feature."""
		return self._instance.GetType

	@get_type.setter
	def get_type(self, value):
		"""Gets the type of bend for this one bend feature."""
		self._instance.GetType = value

	@property
	def i_access_selections(self):
		"""Gains access to selections that define this bend feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to selections that define this bend feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_flat_pattern_sketch_segments(self):
		"""Gets the sketch segments and bend lines for this bend."""
		return self._instance.IFlatPatternSketchSegments2

	@i_flat_pattern_sketch_segments.setter
	def i_flat_pattern_sketch_segments(self, value):
		"""Gets the sketch segments and bend lines for this bend."""
		self._instance.IFlatPatternSketchSegments2 = value

	@property
	def release_selection_access(self):
		"""Accesses the selections that describe this bend feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Accesses the selections that describe this bend feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_custom_bend_allowance(self):
		"""Sets the custom bend allowance for the bend feature."""
		return self._instance.SetCustomBendAllowance

	@set_custom_bend_allowance.setter
	def set_custom_bend_allowance(self, value):
		"""Sets the custom bend allowance for the bend feature."""
		self._instance.SetCustomBendAllowance = value

