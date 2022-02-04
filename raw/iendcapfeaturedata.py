# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEndCapFeatureData_members.html
class IEndCapFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def chamfer_distance(self):
		"""Gets or sets the chamfer distance or fillet radius of the corner of this end-cap feature."""
		return self._instance.ChamferDistance

	@chamfer_distance.setter
	def chamfer_distance(self, value):
		"""Gets or sets the chamfer distance or fillet radius of the corner of this end-cap feature."""
		self._instance.ChamferDistance = value

	@property
	def depth_distance(self):
		"""Gets or sets the depth distance for this end cap feature."""
		return self._instance.DepthDistance

	@depth_distance.setter
	def depth_distance(self, value):
		"""Gets or sets the depth distance for this end cap feature."""
		self._instance.DepthDistance = value

	@property
	def face(self):
		"""Gets the face that is capped or sets the face to cap."""
		return self._instance.Face

	@face.setter
	def face(self, value):
		"""Gets the face that is capped or sets the face to cap."""
		self._instance.Face = value

	@property
	def is_end_cap_inward(self):
		"""Gets or sets the thickness direction of this end cap feature."""
		return self._instance.IsEndCapInward

	@is_end_cap_inward.setter
	def is_end_cap_inward(self, value):
		"""Gets or sets the thickness direction of this end cap feature."""
		self._instance.IsEndCapInward = value

	@property
	def offset_distance(self):
		"""Gets or sets the offset distance for this end-cap feature."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the offset distance for this end-cap feature."""
		self._instance.OffsetDistance = value

	@property
	def thickness(self):
		"""Gets or sets the thickness for this end-cap feature."""
		return self._instance.Thickness

	@thickness.setter
	def thickness(self, value):
		"""Gets or sets the thickness for this end-cap feature."""
		self._instance.Thickness = value

	@property
	def thickness_ratio_for_offset(self):
		"""Gets or sets the offset distance of the end cap as a ratio of the thickness of the structural member being capped."""
		return self._instance.ThicknessRatioForOffset

	@thickness_ratio_for_offset.setter
	def thickness_ratio_for_offset(self, value):
		"""Gets or sets the offset distance of the end cap as a ratio of the thickness of the structural member being capped."""
		self._instance.ThicknessRatioForOffset = value

	@property
	def use_chamfer_corners(self):
		"""Gets or sets whether to chamfer the corners of this end-cap feature."""
		return self._instance.UseChamferCorners

	@use_chamfer_corners.setter
	def use_chamfer_corners(self, value):
		"""Gets or sets whether to chamfer the corners of this end-cap feature."""
		self._instance.UseChamferCorners = value

	@property
	def use_corner_treatment(self):
		"""Gets or sets whether to apply a corner treatment to this end cap feature."""
		return self._instance.UseCornerTreatment

	@use_corner_treatment.setter
	def use_corner_treatment(self, value):
		"""Gets or sets whether to apply a corner treatment to this end cap feature."""
		self._instance.UseCornerTreatment = value

	@property
	def use_reverse(self):
		"""Gets or sets whether to reverse the offset of this end cap feature."""
		return self._instance.UseReverse

	@use_reverse.setter
	def use_reverse(self, value):
		"""Gets or sets whether to reverse the offset of this end cap feature."""
		self._instance.UseReverse = value

	@property
	def use_thickness_ratio_for_offset(self):
		"""Gets or sets whether a ratio of the thickness is used to specify the offset for this end-cap feature."""
		return self._instance.UseThicknessRatioForOffset

	@use_thickness_ratio_for_offset.setter
	def use_thickness_ratio_for_offset(self, value):
		"""Gets or sets whether a ratio of the thickness is used to specify the offset for this end-cap feature."""
		self._instance.UseThicknessRatioForOffset = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this end-cap feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this end-cap feature."""
		self._instance.AccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this end-cap feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this end-cap feature."""
		self._instance.ReleaseSelectionAccess = value

