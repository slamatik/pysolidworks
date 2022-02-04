# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html
class ISketchBlockDefinition:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def file_name(self):
		"""Gets or sets the name of the file to which the block definition is linked."""
		return self._instance.FileName

	@file_name.setter
	def file_name(self, value):
		"""Gets or sets the name of the file to which the block definition is linked."""
		self._instance.FileName = value

	@property
	def insertion_point(self):
		"""Gets or sets the insertion point for the block definition."""
		return self._instance.InsertionPoint

	@insertion_point.setter
	def insertion_point(self, value):
		"""Gets or sets the insertion point for the block definition."""
		self._instance.InsertionPoint = value

	@property
	def link_to_file(self):
		"""Gets or sets whether the block definition file is linked to a file."""
		return self._instance.LinkToFile

	@link_to_file.setter
	def link_to_file(self, value):
		"""Gets or sets whether the block definition file is linked to a file."""
		self._instance.LinkToFile = value

	@property
	def get_arc_count(self):
		"""Gets the number of arcs in this block definition."""
		return self._instance.GetArcCount

	@get_arc_count.setter
	def get_arc_count(self, value):
		"""Gets the number of arcs in this block definition."""
		self._instance.GetArcCount = value

	@property
	def get_arcs(self):
		"""Gets information about all of the arcs in the block definition."""
		return self._instance.GetArcs

	@get_arcs.setter
	def get_arcs(self, value):
		"""Gets information about all of the arcs in the block definition."""
		self._instance.GetArcs = value

	@property
	def get_display_dimension_count(self):
		"""Gets the number of display dimensions in this block definition."""
		return self._instance.GetDisplayDimensionCount

	@get_display_dimension_count.setter
	def get_display_dimension_count(self, value):
		"""Gets the number of display dimensions in this block definition."""
		self._instance.GetDisplayDimensionCount = value

	@property
	def get_display_dimensions(self):
		"""Gets the display dimensions in this block definition."""
		return self._instance.GetDisplayDimensions

	@get_display_dimensions.setter
	def get_display_dimensions(self, value):
		"""Gets the display dimensions in this block definition."""
		self._instance.GetDisplayDimensions = value

	@property
	def get_ellipse_count(self):
		"""Gets the number of ellipses in this block definition."""
		return self._instance.GetEllipseCount

	@get_ellipse_count.setter
	def get_ellipse_count(self, value):
		"""Gets the number of ellipses in this block definition."""
		self._instance.GetEllipseCount = value

	@property
	def get_ellipses(self):
		"""Gets the information about all of the ellipses in this block definition."""
		return self._instance.GetEllipses

	@get_ellipses.setter
	def get_ellipses(self, value):
		"""Gets the information about all of the ellipses in this block definition."""
		self._instance.GetEllipses = value

	@property
	def get_feature(self):
		"""Gets the feature for this block definition."""
		return self._instance.GetFeature

	@get_feature.setter
	def get_feature(self, value):
		"""Gets the feature for this block definition."""
		self._instance.GetFeature = value

	@property
	def get_instance_count(self):
		"""Gets the number of block instances of this block definition."""
		return self._instance.GetInstanceCount

	@get_instance_count.setter
	def get_instance_count(self, value):
		"""Gets the number of block instances of this block definition."""
		self._instance.GetInstanceCount = value

	@property
	def get_instances(self):
		"""Gets all of the block instances of this block definition."""
		return self._instance.GetInstances

	@get_instances.setter
	def get_instances(self, value):
		"""Gets all of the block instances of this block definition."""
		self._instance.GetInstances = value

	@property
	def get_line_count(self):
		"""Gets the number of lines in this block definition."""
		return self._instance.GetLineCount

	@get_line_count.setter
	def get_line_count(self, value):
		"""Gets the number of lines in this block definition."""
		self._instance.GetLineCount = value

	@property
	def get_lines(self):
		"""Gets information about all of the lines in this block definition."""
		return self._instance.GetLines

	@get_lines.setter
	def get_lines(self, value):
		"""Gets information about all of the lines in this block definition."""
		self._instance.GetLines = value

	@property
	def get_note_count(self):
		"""Gets the number of notes in this block definition."""
		return self._instance.GetNoteCount

	@get_note_count.setter
	def get_note_count(self, value):
		"""Gets the number of notes in this block definition."""
		self._instance.GetNoteCount = value

	@property
	def get_notes(self):
		"""Gets the notes in this block definition."""
		return self._instance.GetNotes

	@get_notes.setter
	def get_notes(self, value):
		"""Gets the notes in this block definition."""
		self._instance.GetNotes = value

	@property
	def get_parabola_count(self):
		"""Gets the number of parabolas in this block definition."""
		return self._instance.GetParabolaCount

	@get_parabola_count.setter
	def get_parabola_count(self, value):
		"""Gets the number of parabolas in this block definition."""
		self._instance.GetParabolaCount = value

	@property
	def get_parabolas(self):
		"""Gets information about all of the parabolas in this block definition."""
		return self._instance.GetParabolas

	@get_parabolas.setter
	def get_parabolas(self, value):
		"""Gets information about all of the parabolas in this block definition."""
		self._instance.GetParabolas = value

	@property
	def get_sketch(self):
		"""Gets the underlying sketch of this block definition."""
		return self._instance.GetSketch

	@get_sketch.setter
	def get_sketch(self, value):
		"""Gets the underlying sketch of this block definition."""
		self._instance.GetSketch = value

	@property
	def get_spline_count(self):
		"""Gets the number of splines in this block definition."""
		return self._instance.GetSplineCount

	@get_spline_count.setter
	def get_spline_count(self, value):
		"""Gets the number of splines in this block definition."""
		self._instance.GetSplineCount = value

	@property
	def get_spline_interpolate_count(self):
		"""Gets the number of splines in the sketch block definition and the size of array required to hold the data for the interpolation of these splines."""
		return self._instance.GetSplineInterpolateCount

	@get_spline_interpolate_count.setter
	def get_spline_interpolate_count(self, value):
		"""Gets the number of splines in the sketch block definition and the size of array required to hold the data for the interpolation of these splines."""
		self._instance.GetSplineInterpolateCount = value

	@property
	def get_spline_params(self):
		"""Gets all the parameters of the splines in the sketch block definition."""
		return self._instance.GetSplineParams

	@get_spline_params.setter
	def get_spline_params(self, value):
		"""Gets all the parameters of the splines in the sketch block definition."""
		self._instance.GetSplineParams = value

	@property
	def get_spline_params_count(self):
		"""Gets the number of splines in the sketch block definition and the size of array required to hold the data for the parameters of these splines."""
		return self._instance.GetSplineParamsCount

	@get_spline_params_count.setter
	def get_spline_params_count(self, value):
		"""Gets the number of splines in the sketch block definition and the size of array required to hold the data for the parameters of these splines."""
		self._instance.GetSplineParamsCount = value

	@property
	def get_splines(self):
		"""Gets the spline points by tessellation instead of by interpolation as is done by ISketchBlockDefinition::GetSplinesInterpolate and ISketchBlockDefinition::IGetSplinesInterpolate."""
		return self._instance.GetSplines2

	@get_splines.setter
	def get_splines(self, value):
		"""Gets the spline points by tessellation instead of by interpolation as is done by ISketchBlockDefinition::GetSplinesInterpolate and ISketchBlockDefinition::IGetSplinesInterpolate."""
		self._instance.GetSplines2 = value

	@property
	def get_splines_interpolate(self):
		"""Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by ISketch::GetSplines2 and ISketch::IGetSplines2."""
		return self._instance.GetSplinesInterpolate

	@get_splines_interpolate.setter
	def get_splines_interpolate(self, value):
		"""Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by ISketch::GetSplines2 and ISketch::IGetSplines2."""
		self._instance.GetSplinesInterpolate = value

	@property
	def get_user_points(self):
		"""Gets information about all of the user points in this block definition."""
		return self._instance.GetUserPoints

	@get_user_points.setter
	def get_user_points(self, value):
		"""Gets information about all of the user points in this block definition."""
		self._instance.GetUserPoints = value

	@property
	def get_user_points_count(self):
		"""Gets the number of user points in this block definition."""
		return self._instance.GetUserPointsCount

	@get_user_points_count.setter
	def get_user_points_count(self, value):
		"""Gets the number of user points in this block definition."""
		self._instance.GetUserPointsCount = value

	@property
	def i_get_arcs(self):
		"""Gets information about all of the arcs in the block definition."""
		return self._instance.IGetArcs

	@i_get_arcs.setter
	def i_get_arcs(self, value):
		"""Gets information about all of the arcs in the block definition."""
		self._instance.IGetArcs = value

	@property
	def i_get_display_dimensions(self):
		"""Gets the display dimensions in this block definition."""
		return self._instance.IGetDisplayDimensions

	@i_get_display_dimensions.setter
	def i_get_display_dimensions(self, value):
		"""Gets the display dimensions in this block definition."""
		self._instance.IGetDisplayDimensions = value

	@property
	def i_get_ellipses(self):
		"""Gets the information about all of the ellipses in this block definition."""
		return self._instance.IGetEllipses

	@i_get_ellipses.setter
	def i_get_ellipses(self, value):
		"""Gets the information about all of the ellipses in this block definition."""
		self._instance.IGetEllipses = value

	@property
	def i_get_instances(self):
		"""Gets all of the block instances of this block definition."""
		return self._instance.IGetInstances

	@i_get_instances.setter
	def i_get_instances(self, value):
		"""Gets all of the block instances of this block definition."""
		self._instance.IGetInstances = value

	@property
	def i_get_lines(self):
		"""Gets information about all of the lines in this block definition."""
		return self._instance.IGetLines

	@i_get_lines.setter
	def i_get_lines(self, value):
		"""Gets information about all of the lines in this block definition."""
		self._instance.IGetLines = value

	@property
	def i_get_notes(self):
		"""Gets the notes in this block definition."""
		return self._instance.IGetNotes

	@i_get_notes.setter
	def i_get_notes(self, value):
		"""Gets the notes in this block definition."""
		self._instance.IGetNotes = value

	@property
	def i_get_parabolas(self):
		"""Gets information about all of the parabolas in this block definition."""
		return self._instance.IGetParabolas

	@i_get_parabolas.setter
	def i_get_parabolas(self, value):
		"""Gets information about all of the parabolas in this block definition."""
		self._instance.IGetParabolas = value

	@property
	def i_get_spline_params(self):
		"""Gets all the parameters of the splines in the sketch block definition."""
		return self._instance.IGetSplineParams

	@i_get_spline_params.setter
	def i_get_spline_params(self, value):
		"""Gets all the parameters of the splines in the sketch block definition."""
		self._instance.IGetSplineParams = value

	@property
	def i_get_splines(self):
		"""Gets the spline points by tessellation instead of by interpolation as is done by ISketchBlockDefinition::GetSplinesInterpolate and ISketchBlockDefinition::IGetSplinesInterpolate."""
		return self._instance.IGetSplines2

	@i_get_splines.setter
	def i_get_splines(self, value):
		"""Gets the spline points by tessellation instead of by interpolation as is done by ISketchBlockDefinition::GetSplinesInterpolate and ISketchBlockDefinition::IGetSplinesInterpolate."""
		self._instance.IGetSplines2 = value

	@property
	def i_get_splines_interpolate(self):
		"""Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by ISketch::GetSplines2 and ISketch::IGetSplines2."""
		return self._instance.IGetSplinesInterpolate

	@i_get_splines_interpolate.setter
	def i_get_splines_interpolate(self, value):
		"""Gets all of the parameers of the splines by interpolation instead of by tessellation as is done by ISketch::GetSplines2 and ISketch::IGetSplines2."""
		self._instance.IGetSplinesInterpolate = value

	@property
	def i_get_user_points(self):
		"""Gets information about all of the user points in this block definition."""
		return self._instance.IGetUserPoints

	@i_get_user_points.setter
	def i_get_user_points(self, value):
		"""Gets information about all of the user points in this block definition."""
		self._instance.IGetUserPoints = value

	@property
	def save(self):
		"""Saves the block definition."""
		return self._instance.Save

	@save.setter
	def save(self, value):
		"""Saves the block definition."""
		self._instance.Save = value

