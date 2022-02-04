# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface_members.html
class ISurface:
	def __init__(self, parent=None):
		self._instance = parent

	def cone_params(self):
		"""Gets the parameters of a conical surface."""
		# return self._instance.ConeParams2
		raise NotImplemented

	def cylinder_params(self):
		"""Gets the parameters of a cylindrical surface."""
		# return self._instance.CylinderParams
		raise NotImplemented

	def i_cone_params(self):
		"""Gets the parameters of a conical surface."""
		# return self._instance.IConeParams
		raise NotImplemented

	def i_cylinder_params(self):
		"""Gets the parameters of a cylindrical surface."""
		# return self._instance.ICylinderParams
		raise NotImplemented

	def i_plane_params(self):
		"""Gets the parameters of a planar surface."""
		# return self._instance.IPlaneParams
		raise NotImplemented

	def i_sphere_params(self):
		"""Gets the parameters of a spherical surface."""
		# return self._instance.ISphereParams
		raise NotImplemented

	def i_torus_params(self):
		"""Gets the parameters of a toroidal surface."""
		# return self._instance.ITorusParams
		raise NotImplemented

	def plane_params(self):
		"""Gets the parameters of a planar surface."""
		# return self._instance.PlaneParams
		raise NotImplemented

	def sphere_params(self):
		"""Gets the parameters of a spherical surface."""
		# return self._instance.SphereParams
		raise NotImplemented

	def torus_params(self):
		"""Gets the parameters of a toroidal surface."""
		# return self._instance.TorusParams
		raise NotImplemented

	def add_trimming_loop(self, n_crvs, v_order, v_dim, v_periodic, v_num_knots, v_num_ctrl_points, v_knots, v_ctrl_point_dbls, uv_range):
		"""
		Creates a trimming loop out of specified surface parametric UV-curves and adds it to a list of such loops.
		:param n_crvs: Number of surface parametric (UV) curves constituting the loop and the size of each of the VOrder, VDim, VPeriodic, VNumKnots, VNumControlPnts arrays
		:param v_order: Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing orders of the curves (see Remarks)
		:param v_dim: Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing dimensions (2, 3, or 4) of the control points of the curves (see Remarks)
		:param v_periodic: Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing whether the curve is periodic (1) or non-periodic (0) (see Remarks)
		:param v_num_knots: Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing number of knots on the curves (see Remarks)
		:param v_num_ctrl_points: Array containing NCrvs longs (VBA), Integers (VB.NET), or ints (C#, C++) representing number of control points on the curves (see Remarks)
		:param v_knots: Knot vector array of <TotalNumKnots> doubles, where TotalNumKnots = (TotalNumKnots + VNumKnots[i]) for i = 1 to NCrvs (see Remarks)
		:param v_ctrl_point_dbls: Control point coordinate array of <TotalNumCPCoords> doubles, where TotalNumCPCoords = (TotalNumCPCoords + (VDim[i] * VNumCtrlPoints[i])) for i = 1 to NCrvs (see Remarks)
		:param uv_range: Array of four doubles representing U Low, U High, V Low, and V High (see Remarks)
		"""
		# return self._instance.AddTrimmingLoop2(n_crvs, v_order, v_dim, v_periodic, v_num_knots, v_num_ctrl_points, v_knots, v_ctrl_point_dbls, uv_range)
		raise NotImplemented

	def copy(self):
		"""Gets a copy of this surface."""
		# return self._instance.Copy
		raise NotImplemented

	def create_new_curve(self):
		"""Creates a new empty curve for the part."""
		# return self._instance.CreateNewCurve
		raise NotImplemented

	def create_trimmed_sheet(self, curves, preserve_analytic_curves, tolerance):
		"""
		Creates a trimmed sheet body from this surface.
		:param curves: Array of curves that represent the boundary of the trimmed sheet (see Remarks)
		:param preserve_analytic_curves: True to preserve analytic curves, false to store all trimming curves as SP-curves
		:param tolerance: Tolerance for gaps between edges (see Remarks)
		"""
		# return self._instance.CreateTrimmedSheet5(curves, preserve_analytic_curves, tolerance)
		raise NotImplemented

	def evaluate(self, u_param, v_param, num_u_deriv, num_v_deriv):
		"""
		Evaluates the surface, given the u and v parameters of the surface.
		:param u_param: Value of u parameter
		:param v_param: Value of v parameter
		:param num_u_deriv: Number of u derivatives required
		:param num_v_deriv: Number of v derivatives required
		"""
		# return self._instance.Evaluate(u_param, v_param, num_u_deriv, num_v_deriv)
		raise NotImplemented

	def evaluate_at_point(self, position_x, position_y, position_z):
		"""
		Evaluates a surface at the specified XYZ point.
		:param position_x: X position
		:param position_y: Y position
		:param position_z: Z position
		"""
		# return self._instance.EvaluateAtPoint(position_x, position_y, position_z)
		raise NotImplemented

	def find_minimum_radius(self, u_bound, v_bound, num_of_radius, radius, location, u_v_parameter):
		"""
		Gets the minimum radius of curvature for the selected surface.
		:param u_bound: MinMax UParameter
		:param v_bound: MinMax VParameter
		:param num_of_radius: Number of radius; can be 0, 1, or 2
		:param radius: Minimum radius of curvature (see Remarks)
		:param location: Position where the minimum radius curvature occurred (see Remarks)
		:param u_v_parameter: UV parameters; because points are UV, third ordinates are 0 (see Remarks)
		"""
		# return self._instance.FindMinimumRadius(u_bound, v_bound, num_of_radius, radius, location, u_v_parameter)
		raise NotImplemented

	def get_b_surf_params(self, want_cubic, want_non_rational, v_p0, tolerance, sense):
		"""
		Gets the parameterization data for a B-spline surface.
		:param want_cubic: True if cubic is needed, false if not; specifying true converts any surface to a cubic B-spline surface
		:param want_non_rational: True if non-rational is needed, false if not; specifying true converts any surface to a non-rational B-spline surface; if you specify true, then you should only use this method for surfaces that are of B-spline or blend type; otherwise, the underlying call is not made and the values returned from this are not initialized, or they contain the values from the last call
		:param v_p0: ISurfaceParameterizationData
		:param tolerance: Tolerance, in meters, between the approximated B-spline surface and the underlying surface; the default value is 0.01 and should generally be reduced to the tolerance desired
		:param sense: Approximated B-spline surface is not always in the same direction as the original surface; if Sense is true, then the underlying surface and the B-spline surface are in the same direction
		"""
		# return self._instance.GetBSurfParams3(want_cubic, want_non_rational, v_p0, tolerance, sense)
		raise NotImplemented

	def get_closest_point_on(self, x, y, z):
		"""
		Uses the X,Y,Z input point to determine the closest point on the surface.
		:param x: x coordinate of the approximate position on the surface
		:param y: y coordinate of the approximate position on the surface
		:param z: z coordinate of the approximate position on the surface
		"""
		# return self._instance.GetClosestPointOn(x, y, z)
		raise NotImplemented

	def get_extrusionsurf_params(self):
		"""Gets the parameters for the extrusion surface."""
		# return self._instance.GetExtrusionsurfParams
		raise NotImplemented

	def get_intersect_curve_count(self, other_curve, curve_bound):
		"""
		Gets the number of points for a surface-curve intersection.
		:param other_curve: Curve
		:param curve_bound: Array of 6 doubles representing the start and end points of the curve
		"""
		# return self._instance.GetIntersectCurveCount2(other_curve, curve_bound)
		raise NotImplemented

	def get_intersect_surface_count(self, other_surface):
		"""
		Gets the number of curves for a surface-surface intersection.
		:param other_surface: Other surface
		"""
		# return self._instance.GetIntersectSurfaceCount(other_surface)
		raise NotImplemented

	def get_offset_surf_params(self, base_surf, sense):
		"""
		Gets the overall offset distance of this offset surface.
		:param base_surf: Base surface used to generate the offset surface
		:param sense: If true, then the offset is in the direction of the original surface's normal, if fakse, then the offset is in the opposite direction of the original surface's normal
		"""
		# return self._instance.GetOffsetSurfParams2(base_surf, sense)
		raise NotImplemented

	def get_profile_curve(self):
		"""Gets the curve used to create the surface of revolution or extrusion surface and applies to only surface of revolution or extrusion surface."""
		# return self._instance.GetProfileCurve
		raise NotImplemented

	def get_projected_point_on(self, point, direction):
		"""
		Gets the point where the input point is projected on to this surface.
		:param point: Point to project
		:param direction: Direction to project the point
		"""
		# return self._instance.GetProjectedPointOn(point, direction)
		raise NotImplemented

	def get_revsurf_params(self):
		"""Gets the parameters for the surface."""
		# return self._instance.GetRevsurfParams
		raise NotImplemented

	def i_add_trimming_loop(self, curve_count, order, dim, periodic, num_knots, num_ctrl_points, knots, ctrl_point_dbls, uv_range):
		"""
		Creates a trimming loop out of specified surface parametric (UV-curves) and adds it to a list of such loops.
		:param curve_count: Number of surface parametric (UV) curves constituting the loop; the size of Order, Dim, Periodic, NumKnots, and NumControlPnts arrays
		:param order: Orders of the curves; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)
		:param dim: Dimensions of the curves' control points; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++); if you set the first value in this array to negative of its absolute value, then 3D trim curves are expected
		:param periodic: 0 for non-periodic or 1 for periodic; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)
		:param num_knots: Number of knots in the curves; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)
		:param num_ctrl_points: Number of control points in the curves; array of CurveCount longs (VBA), Integers (VB.NET), or ints (C#, C++)
		:param knots: Knot vectors of the curves; array of <TotalNumKnots> doubles, where TotalNumKnots = (TotalNumKnots + NumKnots[i]) for i = 1 to CurveCount
		:param ctrl_point_dbls: Control point coordinates of the curves; array of <TotalNumCPCoords> doubles, where TotalNumCPCoords = (TotalNumCPCoords + (Dim[i] * NumCtrlPoints[i])) for i = 1 to CurveCount
		:param uv_range: Array of four doubles defining U Low U High V Low V High
		"""
		# return self._instance.IAddTrimmingLoop2(curve_count, order, dim, periodic, num_knots, num_ctrl_points, knots, ctrl_point_dbls, uv_range)
		raise NotImplemented

	def i_copy(self):
		"""Gets a copy of this surface."""
		# return self._instance.ICopy
		raise NotImplemented

	def i_create_new_curve(self):
		"""Creates a new empty curve for the part."""
		# return self._instance.ICreateNewCurve
		raise NotImplemented

	def identity(self):
		"""Gets the type of surface."""
		# return self._instance.Identity
		raise NotImplemented

	def i_evaluate(self, u_param, v_param, num_u_deriv, num_v_deriv):
		"""
		Evaluates the surface, given the u and v parameters of the surface.
		:param u_param: Value of u parameter
		:param v_param: Value of v parameter
		:param num_u_deriv: Number of u derivatives required
		:param num_v_deriv: Number of v derivatives required
		"""
		# return self._instance.IEvaluate(u_param, v_param, num_u_deriv, num_v_deriv)
		raise NotImplemented

	def i_evaluate_at_point(self, position_x, position_y, position_z):
		"""
		Evaluates a surface at the specified XYZ point.
		:param position_x: X position
		:param position_y: Y position
		:param position_z: Z position
		"""
		# return self._instance.IEvaluateAtPoint(position_x, position_y, position_z)
		raise NotImplemented

	def i_find_minimum_radius(self, u_bound, v_bound, num_of_radius, radius, location, u_v_parameter):
		"""
		Gets the minimum radius of curvature for the selected surface.
		:param u_bound: MinMax UParameter
		:param v_bound: MinMax VParameter
		:param num_of_radius: Number of radius; can be 0, 1, or 2
		:param radius: Minimum radius of curvature (see Remarks)
		:param location: Position where the minimum radius curvature occurred (see Remarks)
		:param u_v_parameter: UV parameters; because points are UV, third ordinates are 0 (see Remarks)
		"""
		# return self._instance.IFindMinimumRadius(u_bound, v_bound, num_of_radius, radius, location, u_v_parameter)
		raise NotImplemented

	def i_get_b_surf_params(self):
		"""Gets the b-spline surface parameters for the surface."""
		# return self._instance.IGetBSurfParams
		raise NotImplemented

	def i_get_b_surf_params_size(self, want_cubic, want_non_rational, range, tolerance, sense):
		"""
		Gets the allocation size necessary for Bsurface parameter data retrieval in a subsequent call to ISurface::IGetBSurfParams.
		:param want_cubic: True for surface to be a cubic, false for not 
		:param want_non_rational: True if non-rational is needed, false if not; specifying true converts any surface type to a non-rational Bsurface; if you specify true, then you should only use this method for surfaces that are Bsurface or blend surface; otherwise, the underlying call is not made and the values returned from this are not initialized or contain the values from the last call
		:param range: Array of 4 doubles describing the U,V Range
		:param tolerance: Tolerance, in meters, between the approximated b-spline surface and the underlying surface; the default value is 0.01 and should generally be reduced to the tolerance desired
		:param sense: Approximated b-spline surface is not always in the same direction as the original surface; if sense is true, then the underlying surface and the b-spline surface are in the same direction
		"""
		# return self._instance.IGetBSurfParamsSize3(want_cubic, want_non_rational, range, tolerance, sense)
		raise NotImplemented

	def i_get_closest_point_on(self, x, y, z):
		"""
		Uses the X,Y,Z input point to determine the closest point on the surface.
		:param x: x coordinate of the approximate position on the surface
		:param y: y coordinate of the approximate position on the surface
		:param z: z coordinate of the approximate position on the surface
		"""
		# return self._instance.IGetClosestPointOn(x, y, z)
		raise NotImplemented

	def i_get_extrusionsurf_params(self):
		"""Gets the parameters for the extrusion surface."""
		# return self._instance.IGetExtrusionsurfParams
		raise NotImplemented

	def i_get_make_iso_curves_count(self, uv_range, dir, angle, tol):
		"""
		Gets the number of curves that represent the ISO line of a given direction.
		:param uv_range: Array of 4 doubles indicating the range of surface to use (see Remarks)
		:param dir: Array of 3 doubles indicating the direction of the projection on the surface (seeRemarks)
		:param angle: Angle relative to Dir where to create the curves
		:param tol: Tolerance of the curves to create
		"""
		# return self._instance.IGetMakeIsoCurvesCount(uv_range, dir, angle, tol)
		raise NotImplemented

	def i_get_offset_surf_params(self, base_surf, sense):
		"""
		Gets the overall offset distance of this offset surface.
		:param base_surf: Base surface used to generate the offset surface
		:param sense: If true, then the offset is in the direction of the original surface's normal; if false, then the offset is in the opposite direction of the original surface's normal
		"""
		# return self._instance.IGetOffsetSurfParams2(base_surf, sense)
		raise NotImplemented

	def i_get_profile_curve(self):
		"""Gets the curve used to create the surface of revolution or extrusion surface and applies to only surface of revolution or extrusion surface."""
		# return self._instance.IGetProfileCurve
		raise NotImplemented

	def i_get_revsurf_params(self):
		"""Gets the parameters for the surface."""
		# return self._instance.IGetRevsurfParams
		raise NotImplemented

	def i_intersect_curve(self, other_curve, curve_bound, point_count, point_array, t_array, uv_array):
		"""
		Gets a surface-curve intersection.
		:param other_curve: Curve
		:param curve_bound: Array of 6 doubles representing the start and end points of the curve
		:param point_count: Number of points
		:param point_array: Array of points of size PointCount*3
		:param t_array: Array of parameters on curve  of size PointCount
		:param uv_array: Array of parameters on surface of size PointCount*2
		"""
		# return self._instance.IIntersectCurve2(other_curve, curve_bound, point_count, point_array, t_array, uv_array)
		raise NotImplemented

	def i_intersect_surface(self, other_surf, curve_count, curve_array, bounds_array):
		"""
		Gets a surface-surface intersection.
		:param other_surf: Intersecting surface
		:param curve_count: Number of curves
		:param curve_array: Array of curves of size CurveCount
		:param bounds_array: Array of curve bounds of size CurveCount*2
		"""
		# return self._instance.IIntersectSurface(other_surf, curve_count, curve_array, bounds_array)
		raise NotImplemented

	def i_make_iso_curve(self, uor_v, uv_value):
		"""
		Creates a curve that represents the ISO line of a given surface.
		:param uor_v: True to specify V, false to specify U
		:param uv_value: U or V vertex or point that specifies the intersection of two curves
		"""
		# return self._instance.IMakeIsoCurve(uor_v, uv_value)
		raise NotImplemented

	def i_make_iso_curves(self, uv_range, dir, angle, tol, curve_count, curves, curve_bounds):
		"""
		Creates curves on a surface.
		:param uv_range: Array of 4 doubles indicating the range of the surface to use (see Remarks)
		:param dir: Array of 3 doubles indicating the direction of projection on the surface (see Remarks)
		:param angle: Angle relative to dir where to create the curves
		:param tol: Tolerance of the curves
		:param curve_count: Number of curves to create (see Remarks)
		:param curves: Array of curves of size CurveCount
		:param curve_bounds: Array of doubles of size 2*Curves indicating the parametric bounds of the curve
		"""
		# return self._instance.IMakeIsoCurves(uv_range, dir, angle, tol, curve_count, curves, curve_bounds)
		raise NotImplemented

	def intersect_curve(self, other_curve, curve_bound, point_array, t_array, uv_array):
		"""
		Gets a surface-curve intersection.
		:param other_curve: Curve
		:param curve_bound: Array of 6 doubles representing the start and end points of the curve
		:param point_array: Array of points
		:param t_array: Array of parameters on curve
		:param uv_array: Array of parameters on surface
		"""
		# return self._instance.IntersectCurve2(other_curve, curve_bound, point_array, t_array, uv_array)
		raise NotImplemented

	def intersect_surface(self, other_surf, curve_array, bounds_array):
		"""
		Gets a surface-surface intersection.
		:param other_surf: Intersecting surface
		:param curve_array: Array of curves 
		:param bounds_array: Array containing the curve bounds
		"""
		# return self._instance.IntersectSurface(other_surf, curve_array, bounds_array)
		raise NotImplemented

	def i_parameterization(self):
		"""Gets the parameterization of the surface."""
		# return self._instance.IParameterization
		raise NotImplemented

	def i_reverse_evaluate(self, position_x, position_y, position_z):
		"""
		Gets the UV parameters at the specified location, which must be on the surface.
		:param position_x: X position on the surface
		:param position_y: Y position on the surface
		:param position_z: Z position on the surface
		"""
		# return self._instance.IReverseEvaluate(position_x, position_y, position_z)
		raise NotImplemented

	def is_blending(self):
		"""Gets whether the surface is a blending surface."""
		# return self._instance.IsBlending
		raise NotImplemented

	def is_cone(self):
		"""Gets whether the surface is a cone."""
		# return self._instance.IsCone
		raise NotImplemented

	def is_cylinder(self):
		"""Gets whether the surface is a cylinder."""
		# return self._instance.IsCylinder
		raise NotImplemented

	def is_foreign(self):
		"""Gets whether the surface is a foreign surface."""
		# return self._instance.IsForeign
		raise NotImplemented

	def is_offset(self):
		"""Gets whether the surface is an offset surface."""
		# return self._instance.IsOffset
		raise NotImplemented

	def is_parametric(self):
		"""Gets whether the surface is a parametric (spline type) surface."""
		# return self._instance.IsParametric
		raise NotImplemented

	def is_plane(self):
		"""Gets whether the surface is a planar surface."""
		# return self._instance.IsPlane
		raise NotImplemented

	def is_revolved(self):
		"""Gets whether the surface is a revolved surface."""
		# return self._instance.IsRevolved
		raise NotImplemented

	def is_sphere(self):
		"""Gets whether the surface is a sphere."""
		# return self._instance.IsSphere
		raise NotImplemented

	def is_swept(self):
		"""Gets whether the surface is swept."""
		# return self._instance.IsSwept
		raise NotImplemented

	def is_torus(self):
		"""Gets whether the surface is a torus."""
		# return self._instance.IsTorus
		raise NotImplemented

	def make_iso_curve(self, uor_v, uv_value):
		"""
		Creates an untrimmed curve using the specified surface parameter.
		:param uor_v: True to specify v, false to specify u
		:param uv_value: U or v value
		"""
		# return self._instance.MakeIsoCurve(uor_v, uv_value)
		raise NotImplemented

	def make_iso_curve(self, uor_v, uv_value):
		"""
		Creates an untrimmed curve on a surface using the specified u or v surface function parameter.
		:param uor_v: True to specify the surface function's v parameter in UvValue, false to specify its u parameter
		:param uv_value: 


If UorV is...
Then UvValue is the surface function's...


True
V parameter

False
U parameter
		"""
		# return self._instance.MakeIsoCurve2(uor_v, uv_value)
		raise NotImplemented

	def make_iso_curves(self, uv_range, dir, angle, tol, curves, curve_bounds):
		"""
		Creates curves on a surface.
		:param uv_range: Array of 4 doubles indicating the range of the surface to use (see Remarks)
		:param dir: Array of 3 doubles indicating the direction of projection on the surface (see Remarks)
		:param angle: Angle relative to Dir where to create the curves
		:param tol: Tolerance of the curves
		:param curves: Array of curves
		:param curve_bounds: Array of doubles of size 2*Curves indicating the parametric bounds of the curve
		"""
		# return self._instance.MakeIsoCurves(uv_range, dir, angle, tol, curves, curve_bounds)
		raise NotImplemented

	def parameterization(self):
		"""Gets the parameterization of the surface."""
		# return self._instance.Parameterization2
		raise NotImplemented

	def reverse_evaluate(self, position_x, position_y, position_z):
		"""
		Gets the UV parameters at the specified location, which must be on the surface.
		:param position_x: X position on the surface
		:param position_y: Y position on the surface
		:param position_z: Z position on the surface
		"""
		# return self._instance.ReverseEvaluate(position_x, position_y, position_z)
		raise NotImplemented

