# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html
class ISketchSpline:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def curve_degree(self):
		"""Gets or sets the degree of curve for this Bezier curve style spline."""
		return self._instance.CurveDegree

	@curve_degree.setter
	def curve_degree(self, value):
		"""Gets or sets the degree of curve for this Bezier curve style spline."""
		self._instance.CurveDegree = value

	@property
	def curve_type(self):
		"""Gets or sets the type of curve for this style spline."""
		return self._instance.CurveType

	@curve_type.setter
	def curve_type(self, value):
		"""Gets or sets the type of curve for this style spline."""
		self._instance.CurveType = value

	@property
	def display_control_polygon(self):
		"""Gets or sets whether to add a control polygon to this spline."""
		return self._instance.DisplayControlPolygon

	@display_control_polygon.setter
	def display_control_polygon(self, value):
		"""Gets or sets whether to add a control polygon to this spline."""
		self._instance.DisplayControlPolygon = value

	@property
	def is_rational_curve(self):
		"""Gets whether this spline is rational or non-rational."""
		return self._instance.IsRationalCurve

	@is_rational_curve.setter
	def is_rational_curve(self, value):
		"""Gets whether this spline is rational or non-rational."""
		self._instance.IsRationalCurve = value

	@property
	def is_style_spline(self):
		"""Gets whether this spline is a style spline."""
		return self._instance.IsStyleSpline

	@is_style_spline.setter
	def is_style_spline(self, value):
		"""Gets whether this spline is a style spline."""
		self._instance.IsStyleSpline = value

	@property
	def proportional(self):
		"""Gets or sets whether the spline resizes proportionally when you drag an endpoint the spline."""
		return self._instance.Proportional

	@proportional.setter
	def proportional(self, value):
		"""Gets or sets whether the spline resizes proportionally when you drag an endpoint the spline."""
		self._instance.Proportional = value

	@property
	def show_curvature_combs(self):
		"""Gets or sets whether to show curvature combs."""
		return self._instance.ShowCurvatureCombs

	@show_curvature_combs.setter
	def show_curvature_combs(self, value):
		"""Gets or sets whether to show curvature combs."""
		self._instance.ShowCurvatureCombs = value

	@property
	def show_inflection_points(self):
		"""Gets or sets whether show the inflection points of this spline."""
		return self._instance.ShowInflectionPoints

	@show_inflection_points.setter
	def show_inflection_points(self, value):
		"""Gets or sets whether show the inflection points of this spline."""
		self._instance.ShowInflectionPoints = value

	@property
	def show_minimum_radius(self):
		"""Gets or sets the minimum radius of a curve for this spline."""
		return self._instance.ShowMinimumRadius

	@show_minimum_radius.setter
	def show_minimum_radius(self, value):
		"""Gets or sets the minimum radius of a curve for this spline."""
		self._instance.ShowMinimumRadius = value

	@property
	def show_spline_handles(self):
		"""Gets or sets whether to show the handles for this spline."""
		return self._instance.ShowSplineHandles

	@show_spline_handles.setter
	def show_spline_handles(self, value):
		"""Gets or sets whether to show the handles for this spline."""
		self._instance.ShowSplineHandles = value

	@property
	def add_curvature_control(self):
		"""Adds a curvature control pointer to this spline."""
		return self._instance.AddCurvatureControl

	@add_curvature_control.setter
	def add_curvature_control(self, value):
		"""Adds a curvature control pointer to this spline."""
		self._instance.AddCurvatureControl = value

	@property
	def add_tangency_control(self):
		"""Adds a new handle to help control the tangency of this spline."""
		return self._instance.AddTangencyControl

	@add_tangency_control.setter
	def add_tangency_control(self, value):
		"""Adds a new handle to help control the tangency of this spline."""
		self._instance.AddTangencyControl = value

	@property
	def delete_point(self):
		"""Deletes a point on this spline."""
		return self._instance.DeletePoint

	@delete_point.setter
	def delete_point(self, value):
		"""Deletes a point on this spline."""
		self._instance.DeletePoint = value

	@property
	def get_control_vertex_weights(self):
		"""Gets the weights of the control vetexes of this rational spline."""
		return self._instance.GetControlVertexWeights

	@get_control_vertex_weights.setter
	def get_control_vertex_weights(self, value):
		"""Gets the weights of the control vetexes of this rational spline."""
		self._instance.GetControlVertexWeights = value

	@property
	def get_equation_parameters(self):
		"""Gets an equation-driven curve's parameters."""
		return self._instance.GetEquationParameters2

	@get_equation_parameters.setter
	def get_equation_parameters(self, value):
		"""Gets an equation-driven curve's parameters."""
		self._instance.GetEquationParameters2 = value

	@property
	def get_point_count(self):
		"""Gets the number of points in this sketch spline segment."""
		return self._instance.GetPointCount

	@get_point_count.setter
	def get_point_count(self, value):
		"""Gets the number of points in this sketch spline segment."""
		self._instance.GetPointCount = value

	@property
	def get_points(self):
		"""Gets an array of sketch points for the spline."""
		return self._instance.GetPoints2

	@get_points.setter
	def get_points(self, value):
		"""Gets an array of sketch points for the spline."""
		self._instance.GetPoints2 = value

	@property
	def get_spline_handle_count(self):
		"""Gets the number of handles in this spline."""
		return self._instance.GetSplineHandleCount

	@get_spline_handle_count.setter
	def get_spline_handle_count(self, value):
		"""Gets the number of handles in this spline."""
		self._instance.GetSplineHandleCount = value

	@property
	def get_spline_handles(self):
		"""Gets the handles of this spline."""
		return self._instance.GetSplineHandles

	@get_spline_handles.setter
	def get_spline_handles(self, value):
		"""Gets the handles of this spline."""
		self._instance.GetSplineHandles = value

	@property
	def i_enum_points(self):
		"""Gets an enumeration of sketch points for the spline."""
		return self._instance.IEnumPoints

	@i_enum_points.setter
	def i_enum_points(self, value):
		"""Gets an enumeration of sketch points for the spline."""
		self._instance.IEnumPoints = value

	@property
	def i_get_spline_handles(self):
		"""Gets the handles of this spline."""
		return self._instance.IGetSplineHandles

	@i_get_spline_handles.setter
	def i_get_spline_handles(self, value):
		"""Gets the handles of this spline."""
		self._instance.IGetSplineHandles = value

	@property
	def insert_point(self):
		"""Inserts a point at the specified coordinates of this spline."""
		return self._instance.InsertPoint

	@insert_point.setter
	def insert_point(self, value):
		"""Inserts a point at the specified coordinates of this spline."""
		self._instance.InsertPoint = value

	@property
	def make_rational(self):
		"""Sets whether this spline is rational or non-rational."""
		return self._instance.MakeRational

	@make_rational.setter
	def make_rational(self, value):
		"""Sets whether this spline is rational or non-rational."""
		self._instance.MakeRational = value

	@property
	def modify_control_point(self):
		"""Specifies new coordinates for the specified control point of this sketch spline."""
		return self._instance.ModifyControlPoint

	@modify_control_point.setter
	def modify_control_point(self, value):
		"""Specifies new coordinates for the specified control point of this sketch spline."""
		self._instance.ModifyControlPoint = value

	@property
	def modify_knot(self):
		"""Modifies the specified interior knot of this sketch spline."""
		return self._instance.ModifyKnot

	@modify_knot.setter
	def modify_knot(self, value):
		"""Modifies the specified interior knot of this sketch spline."""
		self._instance.ModifyKnot = value

	@property
	def relax_spline(self):
		"""Smoothens the shape of a spline that was changed by dragging a node on a control polygon."""
		return self._instance.RelaxSpline

	@relax_spline.setter
	def relax_spline(self, value):
		"""Smoothens the shape of a spline that was changed by dragging a node on a control polygon."""
		self._instance.RelaxSpline = value

	@property
	def reset_all_handles(self):
		"""Resets all handles to their initial state."""
		return self._instance.ResetAllHandles

	@reset_all_handles.setter
	def reset_all_handles(self, value):
		"""Resets all handles to their initial state."""
		self._instance.ResetAllHandles = value

	@property
	def set_control_vertex_weights(self):
		"""Sets the weights of the control vetexes of this rational spline."""
		return self._instance.SetControlVertexWeights

	@set_control_vertex_weights.setter
	def set_control_vertex_weights(self, value):
		"""Sets the weights of the control vetexes of this rational spline."""
		self._instance.SetControlVertexWeights = value

	@property
	def set_equation_parameters(self):
		"""Sets an equation-driven curve's parameters."""
		return self._instance.SetEquationParameters2

	@set_equation_parameters.setter
	def set_equation_parameters(self, value):
		"""Sets an equation-driven curve's parameters."""
		self._instance.SetEquationParameters2 = value

	@property
	def simplify(self):
		"""Reduces the number of points in a spline to increase system performance in models with complex spline curves."""
		return self._instance.Simplify

	@simplify.setter
	def simplify(self, value):
		"""Reduces the number of points in a spline to increase system performance in models with complex spline curves."""
		self._instance.Simplify = value

