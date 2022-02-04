# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData_members.html
class IFlatPatternFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def break_corner_radius(self):
		"""Gets or sets the radius of the break corner for the Flat-Pattern feature."""
		return self._instance.BreakCornerRadius

	@break_corner_radius.setter
	def break_corner_radius(self, value):
		"""Gets or sets the radius of the break corner for the Flat-Pattern feature."""
		self._instance.BreakCornerRadius = value

	@property
	def break_corner_type(self):
		"""Gets or sets the type of break corner for the Flat-Pattern feature."""
		return self._instance.BreakCornerType

	@break_corner_type.setter
	def break_corner_type(self, value):
		"""Gets or sets the type of break corner for the Flat-Pattern feature."""
		self._instance.BreakCornerType = value

	@property
	def corner_treatment(self):
		"""Gets or sets whether to apply smooth edges in the flat pattern to the Flat-Pattern feature."""
		return self._instance.CornerTreatment

	@corner_treatment.setter
	def corner_treatment(self, value):
		"""Gets or sets whether to apply smooth edges in the flat pattern to the Flat-Pattern feature."""
		self._instance.CornerTreatment = value

	@property
	def corner_trim_ratio_to_thickness(self):
		"""Gets or sets the ratio of the relief thickness of the corner trim for the Flat-Pattern feature."""
		return self._instance.CornerTrimRatioToThickness

	@corner_trim_ratio_to_thickness.setter
	def corner_trim_ratio_to_thickness(self, value):
		"""Gets or sets the ratio of the relief thickness of the corner trim for the Flat-Pattern feature."""
		self._instance.CornerTrimRatioToThickness = value

	@property
	def corner_trim_relief_distance(self):
		"""Gets or sets the distance of the relief for the corner trim for the Flat-Pattern feature."""
		return self._instance.CornerTrimReliefDistance

	@corner_trim_relief_distance.setter
	def corner_trim_relief_distance(self, value):
		"""Gets or sets the distance of the relief for the corner trim for the Flat-Pattern feature."""
		self._instance.CornerTrimReliefDistance = value

	@property
	def corner_trim_relief_type(self):
		"""Gets or sets the type of relief for the corner trim for the Flat-Pattern feature."""
		return self._instance.CornerTrimReliefType

	@corner_trim_relief_type.setter
	def corner_trim_relief_type(self, value):
		"""Gets or sets the type of relief for the corner trim for the Flat-Pattern feature."""
		self._instance.CornerTrimReliefType = value

	@property
	def excluded_faces(self):
		"""Gets and sets the faces to exclude from this Flat-Pattern feature."""
		return self._instance.ExcludedFaces

	@excluded_faces.setter
	def excluded_faces(self, value):
		"""Gets and sets the faces to exclude from this Flat-Pattern feature."""
		self._instance.ExcludedFaces = value

	@property
	def fixed_face(self):
		"""Gets or sets the fixed face of this Flat-Pattern feature."""
		return self._instance.FixedFace2

	@fixed_face.setter
	def fixed_face(self, value):
		"""Gets or sets the fixed face of this Flat-Pattern feature."""
		self._instance.FixedFace2 = value

	@property
	def merge_face(self):
		"""Gets or sets whether to merge the faces that are planar and coincident in the Flat-Pattern feature."""
		return self._instance.MergeFace

	@merge_face.setter
	def merge_face(self, value):
		"""Gets or sets whether to merge the faces that are planar and coincident in the Flat-Pattern feature."""
		self._instance.MergeFace = value

	@property
	def show_slit_in_corner_relief(self):
		"""Get or set whether to show the slit in the corner relief of this Flat-Pattern feature."""
		return self._instance.ShowSlitInCornerRelief

	@show_slit_in_corner_relief.setter
	def show_slit_in_corner_relief(self, value):
		"""Get or set whether to show the slit in the corner relief of this Flat-Pattern feature."""
		self._instance.ShowSlitInCornerRelief = value

	@property
	def simplify_bends(self):
		"""Gets or sets whether to simplify bends in this Flat-Pattern feature."""
		return self._instance.SimplifyBends

	@simplify_bends.setter
	def simplify_bends(self, value):
		"""Gets or sets whether to simplify bends in this Flat-Pattern feature."""
		self._instance.SimplifyBends = value

	@property
	def use_ratio_to_thickness(self):
		"""Gets or sets whether to use the ratio to thickness setting for the corner trim for the Flat-Pattern feature."""
		return self._instance.UseRatioToThickness

	@use_ratio_to_thickness.setter
	def use_ratio_to_thickness(self, value):
		"""Gets or sets whether to use the ratio to thickness setting for the corner trim for the Flat-Pattern feature."""
		self._instance.UseRatioToThickness = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe this Flat-Pattern feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe this Flat-Pattern feature."""
		self._instance.AccessSelections = value

	@property
	def get_add_corner_trim(self):
		"""Gets whether to add a corner trim to the Flat-Pattern feature."""
		return self._instance.GetAddCornerTrim

	@get_add_corner_trim.setter
	def get_add_corner_trim(self, value):
		"""Gets whether to add a corner trim to the Flat-Pattern feature."""
		self._instance.GetAddCornerTrim = value

	@property
	def get_break_corners(self):
		"""Gets whether to add break corners to the Flat-Pattern feature."""
		return self._instance.GetBreakCorners

	@get_break_corners.setter
	def get_break_corners(self, value):
		"""Gets whether to add break corners to the Flat-Pattern feature."""
		self._instance.GetBreakCorners = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that describe this Flat-Pattern feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that describe this Flat-Pattern feature."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_excluded_faces(self):
		"""Gets the faces that are excluded from this Flat-Pattern feature."""
		return self._instance.IGetExcludedFaces

	@i_get_excluded_faces.setter
	def i_get_excluded_faces(self, value):
		"""Gets the faces that are excluded from this Flat-Pattern feature."""
		self._instance.IGetExcludedFaces = value

	@property
	def i_get_excluded_faces_count(self):
		"""Gets the number of faces that are excluded from this Flat-Pattern feature."""
		return self._instance.IGetExcludedFacesCount

	@i_get_excluded_faces_count.setter
	def i_get_excluded_faces_count(self, value):
		"""Gets the number of faces that are excluded from this Flat-Pattern feature."""
		self._instance.IGetExcludedFacesCount = value

	@property
	def i_set_excluded_faces(self):
		"""Sets the faces to exclude from this Flat-Pattern feature."""
		return self._instance.ISetExcludedFaces

	@i_set_excluded_faces.setter
	def i_set_excluded_faces(self, value):
		"""Sets the faces to exclude from this Flat-Pattern feature."""
		self._instance.ISetExcludedFaces = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe this Flat-Pattern feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe this Flat-Pattern feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_add_corner_trim(self):
		"""Sets whether to add corner trims to the Flat-Pattern feature."""
		return self._instance.SetAddCornerTrim

	@set_add_corner_trim.setter
	def set_add_corner_trim(self, value):
		"""Sets whether to add corner trims to the Flat-Pattern feature."""
		self._instance.SetAddCornerTrim = value

	@property
	def set_break_corners(self):
		"""Sets whether to add break corners to the Flat-Pattern feature."""
		return self._instance.SetBreakCorners

	@set_break_corners.setter
	def set_break_corners(self, value):
		"""Sets whether to add break corners to the Flat-Pattern feature."""
		self._instance.SetBreakCorners = value

