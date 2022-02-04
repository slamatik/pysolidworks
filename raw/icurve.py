# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.html
class ICurve:
	def __init__(self, parent=None):
		self._instance = parent

	def circle_params(self):
		"""Gets the parameters of a curve that is a circle."""
		# return self._instance.CircleParams
		raise NotImplemented

	def i_circle_params(self):
		"""Gets the parameters of a curve that is a circle."""
		# return self._instance.ICircleParams
		raise NotImplemented

	def i_line_params(self):
		"""Gets the parameters of a curve that is a line."""
		# return self._instance.ILineParams
		raise NotImplemented

	def line_params(self):
		"""Gets the parameters of a curve that is a line."""
		# return self._instance.LineParams
		raise NotImplemented

	def apply_transform(self, xform):
		"""
		Applies the transform to a curve.
		:param xform: Pointer to IMathTransform object
		"""
		# return self._instance.ApplyTransform(xform)
		raise NotImplemented

	def convert_arc_to_bcurve(self, center, axis, start, end):
		"""
		Gets the b-spline value representation of the arc.
		:param center: Array for the x, y, z coordinates of the center point of thearc
		:param axis: Array for the normal vector of the arc
		:param start: Array for the x, y, z coordinates of the start point of the arc
		:param end: Array for the x, y, z coordinates of the end point of the arc
		"""
		# return self._instance.ConvertArcToBcurve(center, axis, start, end)
		raise NotImplemented

	def convert_line_to_bcurve(self, start_point, end_point):
		"""
		Converts the specified line into a b-spline curve.
		:param start_point: Array values for the coordinates of the start point of the line
		:param end_point: Array values for the coordinates of the end point of the line
		"""
		# return self._instance.ConvertLineToBcurve(start_point, end_point)
		raise NotImplemented

	def copy(self):
		"""Gets a copy of this curve."""
		# return self._instance.Copy
		raise NotImplemented

	def create_trimmed_curve(self, x1, y1, z1, x2, y2, z2):
		"""
		Creates a trimmed curve.
		:param x1: x start point
		:param y1: y start point
		:param z1: z end point
		:param x2: x end point
		:param y2: y end point
		:param z2: z end point
		"""
		# return self._instance.CreateTrimmedCurve2(x1, y1, z1, x2, y2, z2)
		raise NotImplemented

	def create_wire_body(self):
		"""Creates a wire body from this curve."""
		# return self._instance.CreateWireBody
		raise NotImplemented

	def evaluate(self, parameter, number_of_derivatives):
		"""
		Evaluates the curve at the specified parameter of the curve.
		:param parameter: Curve parameter
		:param number_of_derivatives: Number of derivatives
		"""
		# return self._instance.Evaluate2(parameter, number_of_derivatives)
		raise NotImplemented

	def extent_curve(self, at_start, length, linear_ext):
		"""
		Extends a b-spline curve by the specified length.
		:param at_start: True to extend b-spline curve from start point, false to extend b-spline curve from end point
		:param length: Length by which to extend b-spline curve
		:param linear_ext: True if the extension is linear, false if not
		"""
		# return self._instance.ExtentCurve(at_start, length, linear_ext)
		raise NotImplemented

	def find_minimum_radius(self, bound, num_of_radius, radius, location, parameter):
		"""
		Finds the minimum radius of curvature of the selected curve and its position and u-v parameters.
		:param bound: Array of doubles containing the start and end boundaries (see Remarks)
		:param num_of_radius: Number of radius returned; can be 0 or 1
		:param radius: Minimum radius of curvature (see Remarks)
		:param location: Position where minimum radius curvature occurred (see Remarks)
		:param parameter: Curve parameter (see Remarks)
		"""
		# return self._instance.FindMinimumRadius(bound, num_of_radius, radius, location, parameter)
		raise NotImplemented

	def get_base_curve(self):
		"""Gets the base curve for this trimmed curve."""
		# return self._instance.GetBaseCurve
		raise NotImplemented

	def get_b_curve_params(self, want_cubic_in, want_n_rational, force_non_periodic, is_closed):
		"""
		Gets a data object containing the parameters of a Bézier curve.
		:param want_cubic_in: True to return cubic parameters, false to not
		:param want_n_rational: True to return non-rational parameters; false to return rational parameters
		:param force_non_periodic: True to convert the curve from periodic to nonperiodic, false to not (see Remarks)
		:param is_closed: True for a closed curve, false for an open curve (see Remarks)
		"""
		# return self._instance.GetBCurveParams5(want_cubic_in, want_n_rational, force_non_periodic, is_closed)
		raise NotImplemented

	def get_closest_point_on(self, x, y, z):
		"""
		Determines the closest point on the curve using the x,y,z input point.
		:param x: X value of the input point
		:param y: Y value of the input point
		:param z: Z value of the input point
		"""
		# return self._instance.GetClosestPointOn(x, y, z)
		raise NotImplemented

	def get_ellipse_params(self):
		"""Gets the parameters for this elliptical curve."""
		# return self._instance.GetEllipseParams
		raise NotImplemented

	def get_end_params(self, start, end, is_closed, is_periodic):
		"""
		Gets the end conditions of this curve.
		:param start: Start parameter value
		:param end: End parameter value
		:param is_closed: True for closed curves, false for other types
		:param is_periodic: True for periodic curves, false for other types
		"""
		# return self._instance.GetEndParams(start, end, is_closed, is_periodic)
		raise NotImplemented

	def get_length(self, start_param, end_param):
		"""
		Gets the length of a curve between the specified parameters.
		:param start_param: Start parameter
		:param end_param: End parameter
		"""
		# return self._instance.GetLength3(start_param, end_param)
		raise NotImplemented

	def get_p_curve_params(self):
		"""Gets the piecewise polynomial parameterization data for this curve."""
		# return self._instance.GetPCurveParams2
		raise NotImplemented

	def get_spline_pts(self, params_array_in):
		"""
		Gets the spline points for this curve.
		:param params_array_in: Array containing the definition of the spline
		"""
		# return self._instance.GetSplinePts(params_array_in)
		raise NotImplemented

	def get_tess_pts(self, chord_tolerance, length_tolerance, start_point, end_point):
		"""
		Gets a set of points that represent the tessellation of this curve.
		:param chord_tolerance: Chord tolerance to use in tessellation (meters); this is the maximum permitted distance from a cord to the curve between the cord endpoints; the smallest allowable value for this parameter is 1E-8; if 0.0 or a value smaller than 1E-8 is specified, then 1E-8 is used by default
		:param length_tolerance: Length tolerance to be used to filter out very short segments (meters); this method does not return tessellated segments shorter than this value
		:param start_point: Array containing the start point of the curve
		:param end_point: Array containing the end point of the curve
		"""
		# return self._instance.GetTessPts(chord_tolerance, length_tolerance, start_point, end_point)
		raise NotImplemented

	def i_convert_arc_to_bcurve_size(self, center, axis, start, end):
		"""
		Gets the b-curve size for the arc's conversion given the coordinates of the two end points of a line.
		:param center: Pointer to an array of doubles (x, y, z), the coordinates of the arc center
		:param axis: Pointer to an array of doubles (x, y, z), the normal vector of the arc
		:param start: Pointer to an array of doubles (x, y, z), the coordinates of the arc start point
		:param end: Pointer to an array of doubles (x, y, z), the coordinates of the arc end point
		"""
		# return self._instance.IConvertArcToBcurveSize(center, axis, start, end)
		raise NotImplemented

	def i_convert_line_to_bcurve_size(self, start_point, end_point):
		"""
		Converts the specified line into a b-spline curve.
		:param start_point: Array values for the coordinates of the start point of the line
		:param end_point: Array values for the coordinates of the end point of the line
		"""
		# return self._instance.IConvertLineToBcurveSize(start_point, end_point)
		raise NotImplemented

	def i_convert_pcurve_to_bcurve_size(self, dim, order, nsegs, coeffs, basis, xform, scale_factor):
		"""
		Creates a b-curve from piecewise data.
		:param dim: Dimension of the curve:


3 = nonrational

4 = rational
		:param order: Order of the curve; minimum is 2 (linear)
		:param nsegs: Number of segments in the curve; must be at least 1
		:param coeffs: Array of coefficients
		:param basis: 0; not currently used
		:param xform: Transformation matrix to apply after conversion to b-curve
		:param scale_factor: Units conversion factor to apply after conversion to b-curve
		"""
		# return self._instance.IConvertPcurveToBcurveSize(dim, order, nsegs, coeffs, basis, xform, scale_factor)
		raise NotImplemented

	def i_copy(self):
		"""Gets a copy of this curve."""
		# return self._instance.ICopy
		raise NotImplemented

	def identity(self):
		"""Gets the type of curve."""
		# return self._instance.Identity
		raise NotImplemented

	def i_evaluate(self, parameter):
		"""
		Evaluates the curve at the specified parameter of the curve.
		:param parameter: Curve parameter
		"""
		# return self._instance.IEvaluate(parameter)
		raise NotImplemented

	def i_evaluate(self, parameter, number_of_derivatives):
		"""
		Evaluates the curve at the specified parameter of the curve.
		:param parameter: Curve parameter
		:param number_of_derivatives: Number of derivatives
		"""
		# return self._instance.IEvaluate2(parameter, number_of_derivatives)
		raise NotImplemented

	def i_find_minimum_radius(self, bound, num_of_radius, radius, location, parameter):
		"""
		Finds the minimum radius of curvature of the selected curve and its position and u-v parameters.
		:param bound: Array containing the start and end boundary parameters (see Remarks)
		:param num_of_radius: Number of radius returned; can be 0 or 1
		:param radius: Minimum radius of curvature (see Remarks)
		:param location: Position where minimum radius curvature occurred  (see Remarks)
		:param parameter: Curve parameter  (see Remarks)
		"""
		# return self._instance.IFindMinimumRadius(bound, num_of_radius, radius, location, parameter)
		raise NotImplemented

	def i_get_b_curve_params_size(self, want_cubic_in, want_n_rational, force_non_periodic):
		"""
		Gets the b-curve size.
		:param want_cubic_in: True for cubic curves, false if not
		:param want_n_rational: True for non-rational curves, false if not
		:param force_non_periodic: True converts the curve to nonperiodic and returns parameters, false does not
		"""
		# return self._instance.IGetBCurveParamsSize3(want_cubic_in, want_n_rational, force_non_periodic)
		raise NotImplemented

	def i_get_closest_point_on(self, x, y, z):
		"""
		Determines the closest point on the curve using the x,y,z input point.
		:param x: X value of the input point
		:param y: Y value of the input point
		:param z: Z value of the input point
		"""
		# return self._instance.IGetClosestPointOn(x, y, z)
		raise NotImplemented

	def i_get_ellipse_params(self, param_array):
		"""
		Gets the parameters for this elliptical curve.
		:param param_array: 
in-process, unmanaged C++: Pointer to an array of doubles (see Remarks)
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IGetEllipseParams(param_array)
		raise NotImplemented

	def i_get_p_curve_params(self):
		"""Converts a curve to a piecewise rational cubic polynomial form."""
		# return self._instance.IGetPCurveParams
		raise NotImplemented

	def i_get_p_curve_params_size(self):
		"""Gets the p-curve size."""
		# return self._instance.IGetPCurveParamsSize
		raise NotImplemented

	def i_get_spline_pts(self):
		"""Gets the spline points for this curve."""
		# return self._instance.IGetSplinePts
		raise NotImplemented

	def i_get_spline_pts_size(self, prop_array, knots_array, cntrl_pnt_coord_array):
		"""
		Gets the size of the array required by ICurve::IGetSplinePts.
		:param prop_array: Array that includes dimension, order, number of control points, and periodicity
		:param knots_array: knot1, knot2, ..., knotn
		:param cntrl_pnt_coord_array: controlpoint1[dimension], controlpoint2[dimension], ...,  controlpointn[dimension]
		"""
		# return self._instance.IGetSplinePtsSize(prop_array, knots_array, cntrl_pnt_coord_array)
		raise NotImplemented

	def i_get_tess_pts(self, chord_tolerance, length_tolerance, start_point, end_point):
		"""
		Gets a set of points that represent the tessellation of this curve.
		:param chord_tolerance: Chord tolerance to use in tessellation (meters); this is the maximum permitted distance from a cord to the curve between the cord endpoints; the smallest allowable value for this parameter is 1E-8; if 0.0 or a value smaller than 1E-8 is specified, then 1E-8 is used by default
		:param length_tolerance: Length tolerance to be used to filter out very short segments (meters); this method does not return tessellated segments shorter than this value
		:param start_point: Pointer to an array containing the start point of the curve
		:param end_point: Pointer to an array containing the end point of the curve
		"""
		# return self._instance.IGetTessPts(chord_tolerance, length_tolerance, start_point, end_point)
		raise NotImplemented

	def i_get_tess_pts_size(self, chord_tolerance, length_tolerance, start_point, end_point):
		"""
		Gets the size of the array required by ICurve::IGetTessPts.
		:param chord_tolerance: Chord tolerance to be used in tessellation (meters); this is the maximum permitteddistance from a cord to the curve between the cord endpoints
		:param length_tolerance: Length tolerance to be used to filter out very short segments (meters);  tessellatedsegments shorter than this value are not returned
		:param start_point: Pointer to an array containing the start point of the curve
		:param end_point: Pointer to an array containing the end point of the curve
		"""
		# return self._instance.IGetTessPtsSize(chord_tolerance, length_tolerance, start_point, end_point)
		raise NotImplemented

	def i_intersect_curve(self, other_curve, this_start_point, this_end_point, other_start_point, other_end_point):
		"""
		Gets a set of points that represent the intersection of two trimmed curves.
		:param other_curve: Curve to intersect with this curve
		:param this_start_point: Start point of this curve
		:param this_end_point: End point of this curve
		:param other_start_point: Start point of otherCurve
		:param other_end_point: End point of otherCurve
		"""
		# return self._instance.IIntersectCurve(other_curve, this_start_point, this_end_point, other_start_point, other_end_point)
		raise NotImplemented

	def i_intersect_curve_size(self, other_curve, this_start_point, this_end_point, other_start_point, other_end_point):
		"""
		Gets the size of the array required by ICurve::IIntersectCurve.
		:param other_curve: Curve to intersect with this curve
		:param this_start_point: Start point of this curve
		:param this_end_point: End point of this curve
		:param other_start_point: Start point of otherCurve
		:param other_end_point: End point of otherCurve
		"""
		# return self._instance.IIntersectCurveSize(other_curve, this_start_point, this_end_point, other_start_point, other_end_point)
		raise NotImplemented

	def i_join_curves(self, n_curves, curves):
		"""
		Joins the specified curves.
		:param n_curves: Number of curves to join
		:param curves: 
in-process, unmanaged C++: Pointer to an array of curves to join
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IJoinCurves(n_curves, curves)
		raise NotImplemented

	def intersect_curve(self, other_curve, this_start_point, this_end_point, other_start_point, other_end_point):
		"""
		Gets a set of points that represent the intersection of two trimmed curves.
		:param other_curve: Curve to intersect with this curve
		:param this_start_point: Array containing the start point of this curve
		:param this_end_point: Array containing the end point of this curve
		:param other_start_point: Array containing the start point of otherCurve
		:param other_end_point: Array containing the end point of otherCurve
		"""
		# return self._instance.IntersectCurve(other_curve, this_start_point, this_end_point, other_start_point, other_end_point)
		raise NotImplemented

	def i_reverse_curve(self):
		"""Gets the reversed copy of this curve."""
		# return self._instance.IReverseCurve
		raise NotImplemented

	def is_bcurve(self):
		"""Gets whether the curve is a b-spline curve."""
		# return self._instance.IsBcurve
		raise NotImplemented

	def is_circle(self):
		"""Gets whether the curve is a circle."""
		# return self._instance.IsCircle
		raise NotImplemented

	def is_ellipse(self):
		"""Gets whether the curve is an ellipse."""
		# return self._instance.IsEllipse
		raise NotImplemented

	def is_line(self):
		"""Gets whether the curve is a line."""
		# return self._instance.IsLine
		raise NotImplemented

	def is_trimmed_curve(self):
		"""Gets whether the curve is trimmed."""
		# return self._instance.IsTrimmedCurve
		raise NotImplemented

	def join_curves(self, curves):
		"""
		Joins the specified curves.
		:param curves: Curves to join
		"""
		# return self._instance.JoinCurves(curves)
		raise NotImplemented

	def make_bspline_curve(self):
		"""Creates a b-spline curve."""
		# return self._instance.MakeBsplineCurve2
		raise NotImplemented

	def reverse_curve(self):
		"""Gets the reversed copy of this curve."""
		# return self._instance.ReverseCurve
		raise NotImplemented

	def reverse_evaluate(self, position_x, position_y, position_z):
		"""
		Gets the U parameter for the given XYZ location on this curve.
		:param position_x: X coordinate of this location on the curve
		:param position_y: Y coordinate of this location on the curve
		:param position_z: Z coordinate of this location on the curve
		"""
		# return self._instance.ReverseEvaluate(position_x, position_y, position_z)
		raise NotImplemented

	def simplify_b_curve(self, tol_in):
		"""
		Simplifies a b-curve.
		:param tol_in: Tolerance
		"""
		# return self._instance.SimplifyBCurve(tol_in)
		raise NotImplemented

