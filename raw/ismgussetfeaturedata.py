# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData_members.html
class ISMGussetFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def draft_angle(self):
		"""Gets or sets the angle by which to draft the side faces of this gusset."""
		return self._instance.DraftAngle

	@draft_angle.setter
	def draft_angle(self, value):
		"""Gets or sets the angle by which to draft the side faces of this gusset."""
		self._instance.DraftAngle = value

	@property
	def draft_side_faces(self):
		"""Gets or sets whether to draft the side faces of this gusset."""
		return self._instance.DraftSideFaces

	@draft_side_faces.setter
	def draft_side_faces(self, value):
		"""Gets or sets whether to draft the side faces of this gusset."""
		self._instance.DraftSideFaces = value

	@property
	def edge_fillet_radius(self):
		"""Gets or sets the fillet radius of edges in this flat-back gusset."""
		return self._instance.EdgeFilletRadius

	@edge_fillet_radius.setter
	def edge_fillet_radius(self, value):
		"""Gets or sets the fillet radius of edges in this flat-back gusset."""
		self._instance.EdgeFilletRadius = value

	@property
	def fillet_gusset_edges(self):
		"""Gets or sets whether to fillet the edges of this gusset."""
		return self._instance.FilletGussetEdges

	@fillet_gusset_edges.setter
	def fillet_gusset_edges(self, value):
		"""Gets or sets whether to fillet the edges of this gusset."""
		self._instance.FilletGussetEdges = value

	@property
	def fillet_inner_corners(self):
		"""Gets or sets whether to fillet the inner corners of this gusset."""
		return self._instance.FilletInnerCorners

	@fillet_inner_corners.setter
	def fillet_inner_corners(self, value):
		"""Gets or sets whether to fillet the inner corners of this gusset."""
		self._instance.FilletInnerCorners = value

	@property
	def fillet_outer_corners(self):
		"""Gets or sets whether to fillet the outer corners of this gusset."""
		return self._instance.FilletOuterCorners

	@fillet_outer_corners.setter
	def fillet_outer_corners(self, value):
		"""Gets or sets whether to fillet the outer corners of this gusset."""
		self._instance.FilletOuterCorners = value

	@property
	def flip_dim_sides(self):
		"""Gets or sets whether to swap the gusset legs in the dimensioning scheme."""
		return self._instance.FlipDimSides

	@flip_dim_sides.setter
	def flip_dim_sides(self, value):
		"""Gets or sets whether to swap the gusset legs in the dimensioning scheme."""
		self._instance.FlipDimSides = value

	@property
	def flip_offset(self):
		"""Gets or sets whether to offset the gusset section plane on the opposite side of the specified reference point."""
		return self._instance.FlipOffset

	@flip_offset.setter
	def flip_offset(self, value):
		"""Gets or sets whether to offset the gusset section plane on the opposite side of the specified reference point."""
		self._instance.FlipOffset = value

	@property
	def gusset_thickness(self):
		"""Gets or sets the indent thickness of this gusset."""
		return self._instance.GussetThickness

	@gusset_thickness.setter
	def gusset_thickness(self, value):
		"""Gets or sets the indent thickness of this gusset."""
		self._instance.GussetThickness = value

	@property
	def gusset_type(self):
		"""Gets or sets the type of this gusset."""
		return self._instance.GussetType

	@gusset_type.setter
	def gusset_type(self, value):
		"""Gets or sets the type of this gusset."""
		self._instance.GussetType = value

	@property
	def indent_depth(self):
		"""Gets or sets the indent depth of this gusset."""
		return self._instance.IndentDepth

	@indent_depth.setter
	def indent_depth(self, value):
		"""Gets or sets the indent depth of this gusset."""
		self._instance.IndentDepth = value

	@property
	def indent_width(self):
		"""Gets or sets the indent width of this gusset."""
		return self._instance.IndentWidth

	@indent_width.setter
	def indent_width(self, value):
		"""Gets or sets the indent width of this gusset."""
		self._instance.IndentWidth = value

	@property
	def inner_corner_fillet_radius(self):
		"""Gets or sets the fillet radius for the inner corners of this gusset."""
		return self._instance.InnerCornerFilletRadius

	@inner_corner_fillet_radius.setter
	def inner_corner_fillet_radius(self, value):
		"""Gets or sets the fillet radius for the inner corners of this gusset."""
		self._instance.InnerCornerFilletRadius = value

	@property
	def offset_distance(self):
		"""Gets or sets the offset of the gusset's section plane from a specified reference point."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the offset of the gusset's section plane from a specified reference point."""
		self._instance.OffsetDistance = value

	@property
	def outer_corner_fillet_radius(self):
		"""Gets or sets the fillet radius for the outer corners of this gusset."""
		return self._instance.OuterCornerFilletRadius

	@outer_corner_fillet_radius.setter
	def outer_corner_fillet_radius(self, value):
		"""Gets or sets the fillet radius for the outer corners of this gusset."""
		self._instance.OuterCornerFilletRadius = value

	@property
	def override_doc_settings(self):
		"""Gets or sets whether to override the document flat pattern properties."""
		return self._instance.OverrideDocSettings

	@override_doc_settings.setter
	def override_doc_settings(self, value):
		"""Gets or sets whether to override the document flat pattern properties."""
		self._instance.OverrideDocSettings = value

	@property
	def profile_angle_dim(self):
		"""Gets or sets the angle formed by the intersection of this gusset with one face adjacent to the bend of the sheet metal part."""
		return self._instance.ProfileAngleDim

	@profile_angle_dim.setter
	def profile_angle_dim(self, value):
		"""Gets or sets the angle formed by the intersection of this gusset with one face adjacent to the bend of the sheet metal part."""
		self._instance.ProfileAngleDim = value

	@property
	def profile_dimension_scheme(self):
		"""Gets or sets the type of profile dimensioning scheme for this gusset."""
		return self._instance.ProfileDimensionScheme

	@profile_dimension_scheme.setter
	def profile_dimension_scheme(self, value):
		"""Gets or sets the type of profile dimensioning scheme for this gusset."""
		self._instance.ProfileDimensionScheme = value

	@property
	def profile_height_dim(self):
		"""Gets or sets the length of the d2 leg of this gusset."""
		return self._instance.ProfileHeightDim

	@profile_height_dim.setter
	def profile_height_dim(self, value):
		"""Gets or sets the length of the d2 leg of this gusset."""
		self._instance.ProfileHeightDim = value

	@property
	def profile_length_dim(self):
		"""Gets or sets the length of the d1 leg of this gusset."""
		return self._instance.ProfileLengthDim

	@profile_length_dim.setter
	def profile_length_dim(self, value):
		"""Gets or sets the length of the d1 leg of this gusset."""
		self._instance.ProfileLengthDim = value

	@property
	def profile_type(self):
		"""Gets or sets the type of profile of this gusset feature."""
		return self._instance.ProfileType

	@profile_type.setter
	def profile_type(self, value):
		"""Gets or sets the type of profile of this gusset feature."""
		self._instance.ProfileType = value

	@property
	def reference_line(self):
		"""Gets or sets the orientation reference for this gusset's section plane."""
		return self._instance.ReferenceLine

	@reference_line.setter
	def reference_line(self, value):
		"""Gets or sets the orientation reference for this gusset's section plane."""
		self._instance.ReferenceLine = value

	@property
	def reference_point(self):
		"""Gets or sets a position reference for this gusset."""
		return self._instance.ReferencePoint

	@reference_point.setter
	def reference_point(self, value):
		"""Gets or sets a position reference for this gusset."""
		self._instance.ReferencePoint = value

	@property
	def show_center(self):
		"""Gets or sets whether to display the center marks of the gusset in its flattened state."""
		return self._instance.ShowCenter

	@show_center.setter
	def show_center(self, value):
		"""Gets or sets whether to display the center marks of the gusset in its flattened state."""
		self._instance.ShowCenter = value

	@property
	def show_profile(self):
		"""Gets or sets whether to display the profile of the gusset in its flattened state."""
		return self._instance.ShowProfile

	@show_profile.setter
	def show_profile(self, value):
		"""Gets or sets whether to display the profile of the gusset in its flattened state."""
		self._instance.ShowProfile = value

	@property
	def supporting_faces(self):
		"""Gets or sets the legs of this gusset."""
		return self._instance.SupportingFaces

	@supporting_faces.setter
	def supporting_faces(self, value):
		"""Gets or sets the legs of this gusset."""
		self._instance.SupportingFaces = value

	@property
	def use_angle_dim_for_profile(self):
		"""Gets or sets whether to dimension this gusset using an angle."""
		return self._instance.UseAngleDimForProfile

	@use_angle_dim_for_profile.setter
	def use_angle_dim_for_profile(self, value):
		"""Gets or sets whether to dimension this gusset using an angle."""
		self._instance.UseAngleDimForProfile = value

	@property
	def use_offset(self):
		"""Gets or sets whether to offset the gusset section plane from a specified reference point."""
		return self._instance.UseOffset

	@use_offset.setter
	def use_offset(self, value):
		"""Gets or sets whether to offset the gusset section plane from a specified reference point."""
		self._instance.UseOffset = value

	@property
	def access_selections(self):
		"""Gains access to a sheet metal gusset."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to a sheet metal gusset."""
		self._instance.AccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this sheet metal gusset feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this sheet metal gusset feature."""
		self._instance.ReleaseSelectionAccess = value

