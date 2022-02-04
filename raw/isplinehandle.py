# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplineHandle_members.html
class ISplineHandle:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def curvature(self):
		"""Gets or sets the degree of curvature at any point where curvature control was added."""
		return self._instance.Curvature

	@curvature.setter
	def curvature(self, value):
		"""Gets or sets the degree of curvature at any point where curvature control was added."""
		self._instance.Curvature = value

	@property
	def curvature_controlled(self):
		"""Gets or sets whether the spline handle has curvature control."""
		return self._instance.CurvatureControlled

	@curvature_controlled.setter
	def curvature_controlled(self, value):
		"""Gets or sets whether the spline handle has curvature control."""
		self._instance.CurvatureControlled = value

	@property
	def editable(self):
		"""Gets or sets whether this spline handle can be edited."""
		return self._instance.Editable

	@editable.setter
	def editable(self, value):
		"""Gets or sets whether this spline handle can be edited."""
		self._instance.Editable = value

	@property
	def parameter(self):
		"""Gets value in the parameter space of the curve underlying the spline handle."""
		return self._instance.Parameter

	@parameter.setter
	def parameter(self, value):
		"""Gets value in the parameter space of the curve underlying the spline handle."""
		self._instance.Parameter = value

	@property
	def radius_of_curvature(self):
		"""Gets or sets the radius of curvature at any spline point."""
		return self._instance.RadiusOfCurvature

	@radius_of_curvature.setter
	def radius_of_curvature(self, value):
		"""Gets or sets the radius of curvature at any spline point."""
		self._instance.RadiusOfCurvature = value

	@property
	def spline_point_number(self):
		"""Gets the number of the points of this spline handle."""
		return self._instance.SplinePointNumber

	@spline_point_number.setter
	def spline_point_number(self, value):
		"""Gets the number of the points of this spline handle."""
		self._instance.SplinePointNumber = value

	@property
	def tangent_driving(self):
		"""Enables or disables spline control using tangent magnitude, tangent radial direction, and tangent polar direction."""
		return self._instance.TangentDriving

	@tangent_driving.setter
	def tangent_driving(self, value):
		"""Enables or disables spline control using tangent magnitude, tangent radial direction, and tangent polar direction."""
		self._instance.TangentDriving = value

	@property
	def tangent_magnitude(self):
		"""Gets or sets the weight for the tangency magnitude in the specified direction for this spline handle."""
		return self._instance.TangentMagnitude

	@tangent_magnitude.setter
	def tangent_magnitude(self, value):
		"""Gets or sets the weight for the tangency magnitude in the specified direction for this spline handle."""
		self._instance.TangentMagnitude = value

	@property
	def tangent_polar_direction(self):
		"""Gets or sets the tangent polar direction, which is the elevation angle of the tangent vector to a plane placed at a point perpendicular to a spline point."""
		return self._instance.TangentPolarDirection

	@tangent_polar_direction.setter
	def tangent_polar_direction(self, value):
		"""Gets or sets the tangent polar direction, which is the elevation angle of the tangent vector to a plane placed at a point perpendicular to a spline point."""
		self._instance.TangentPolarDirection = value

	@property
	def tangent_radial_direction(self):
		"""Gets or sets the tangent radial direction, which controls the tangency direction by allowing modification of the spline's angle of inclination relative to the x, y, or z axis."""
		return self._instance.TangentRadialDirection

	@tangent_radial_direction.setter
	def tangent_radial_direction(self, value):
		"""Gets or sets the tangent radial direction, which controls the tangency direction by allowing modification of the spline's angle of inclination relative to the x, y, or z axis."""
		self._instance.TangentRadialDirection = value

	@property
	def x(self):
		"""Gets or sets the x coordinate of the spline point."""
		return self._instance.X

	@x.setter
	def x(self, value):
		"""Gets or sets the x coordinate of the spline point."""
		self._instance.X = value

	@property
	def y(self):
		"""Gets or sets the y coordinate of the spline point."""
		return self._instance.Y

	@y.setter
	def y(self, value):
		"""Gets or sets the y coordinate of the spline point."""
		self._instance.Y = value

	@property
	def z(self):
		"""Gets or sets the z coordinate of the spline point."""
		return self._instance.Z

	@z.setter
	def z(self, value):
		"""Gets or sets the z coordinate of the spline point."""
		self._instance.Z = value

	@property
	def reset(self):
		"""Resets the selected handle to its initial state on this spline handle."""
		return self._instance.Reset

	@reset.setter
	def reset(self, value):
		"""Resets the selected handle to its initial state on this spline handle."""
		self._instance.Reset = value

	@property
	def select(self):
		"""Selects a spline handle."""
		return self._instance.Select

	@select.setter
	def select(self, value):
		"""Selects a spline handle."""
		self._instance.Select = value

