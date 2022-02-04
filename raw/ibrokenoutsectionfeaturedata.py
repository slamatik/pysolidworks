# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBrokenOutSectionFeatureData_members.html
class IBrokenOutSectionFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def depth(self):
		"""Gets or sets the depth of exposure of inner details of the model in the broken-out section feature."""
		return self._instance.Depth

	@depth.setter
	def depth(self, value):
		"""Gets or sets the depth of exposure of inner details of the model in the broken-out section feature."""
		self._instance.Depth = value

	@property
	def depth_reference(self):
		"""Gets or sets the geometry reference that defines the depth of exposure of inner details of the model in the broken-out section feature."""
		return self._instance.DepthReference

	@depth_reference.setter
	def depth_reference(self, value):
		"""Gets or sets the geometry reference that defines the depth of exposure of inner details of the model in the broken-out section feature."""
		self._instance.DepthReference = value

	@property
	def edit_sketch(self):
		"""Gets or sets whether to place this broken-out section feature in edit sketch mode."""
		return self._instance.EditSketch

	@edit_sketch.setter
	def edit_sketch(self, value):
		"""Gets or sets whether to place this broken-out section feature in edit sketch mode."""
		self._instance.EditSketch = value

	@property
	def sketch_segment(self):
		"""Gets the sketch segments that form the border of this broken-out section feature."""
		return self._instance.SketchSegment

	@sketch_segment.setter
	def sketch_segment(self, value):
		"""Gets the sketch segments that form the border of this broken-out section feature."""
		self._instance.SketchSegment = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this broken-out section feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this broken-out section feature."""
		self._instance.AccessSelections = value

	@property
	def get_sketch_segment_count(self):
		"""Gets the number of sketch segments that form the border of this broken-out section feature."""
		return self._instance.GetSketchSegmentCount

	@get_sketch_segment_count.setter
	def get_sketch_segment_count(self, value):
		"""Gets the number of sketch segments that form the border of this broken-out section feature."""
		self._instance.GetSketchSegmentCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this broken-out section feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this broken-out section feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_sketch_segment(self):
		"""Gets the sketch segments that form the border of this broken-out section feature."""
		return self._instance.IGetSketchSegment

	@i_get_sketch_segment.setter
	def i_get_sketch_segment(self, value):
		"""Gets the sketch segments that form the border of this broken-out section feature."""
		self._instance.IGetSketchSegment = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections in this broken-out section feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections in this broken-out section feature."""
		self._instance.ReleaseSelectionAccess = value

