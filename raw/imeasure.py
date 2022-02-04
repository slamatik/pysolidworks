# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeasure_members.html
class IMeasure:
	def __init__(self, parent=None):
		self._instance = parent

	def angle(self):
		"""Gets the angle between the two selected entities."""
		# return self._instance.Angle
		raise NotImplemented

	@property
	def angle_decimal_places(self):
		"""Gets or sets the number of decimal places for angle measurements."""
		return self._instance.AngleDecimalPlaces

	@angle_decimal_places.setter
	def angle_decimal_places(self, value):
		"""Gets or sets the number of decimal places for angle measurements."""
		self._instance.AngleDecimalPlaces = value

	@property
	def arc_length(self):
		"""Gets the length of the selected arc."""
		return self._instance.ArcLength

	@arc_length.setter
	def arc_length(self, value):
		"""Gets the length of the selected arc."""
		self._instance.ArcLength = value

	@property
	def arc_option(self):
		"""Gets or sets how to measure an arc or circle."""
		return self._instance.ArcOption

	@arc_option.setter
	def arc_option(self, value):
		"""Gets or sets how to measure an arc or circle."""
		self._instance.ArcOption = value

	@property
	def area(self):
		"""Gets the area of the selected entity."""
		return self._instance.Area

	@area.setter
	def area(self, value):
		"""Gets the area of the selected entity."""
		self._instance.Area = value

	@property
	def center_distance(self):
		"""Gets the distance between the selected cylinder axes, circle centers, or both."""
		return self._instance.CenterDistance

	@center_distance.setter
	def center_distance(self, value):
		"""Gets the distance between the selected cylinder axes, circle centers, or both."""
		self._instance.CenterDistance = value

	@property
	def chord_length(self):
		"""Gets the chord length of the selected arc."""
		return self._instance.ChordLength

	@chord_length.setter
	def chord_length(self, value):
		"""Gets the chord length of the selected arc."""
		self._instance.ChordLength = value

	@property
	def delta_x(self):
		"""Gets the Delta X distance between the selected entities."""
		return self._instance.DeltaX

	@delta_x.setter
	def delta_x(self, value):
		"""Gets the Delta X distance between the selected entities."""
		self._instance.DeltaX = value

	@property
	def delta_y(self):
		"""Gets the Delta Y distance between the selected entities."""
		return self._instance.DeltaY

	@delta_y.setter
	def delta_y(self, value):
		"""Gets the Delta Y distance between the selected entities."""
		self._instance.DeltaY = value

	@property
	def delta_z(self):
		"""Gets the Delta Z distance between the selected entities."""
		return self._instance.DeltaZ

	@delta_z.setter
	def delta_z(self, value):
		"""Gets the Delta Z distance between the selected entities."""
		self._instance.DeltaZ = value

	@property
	def diameter(self):
		"""Gets the diameter of the selected circle or cylinder."""
		return self._instance.Diameter

	@diameter.setter
	def diameter(self, value):
		"""Gets the diameter of the selected circle or cylinder."""
		self._instance.Diameter = value

	@property
	def distance(self):
		"""Gets the distance between the selected entities."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets the distance between the selected entities."""
		self._instance.Distance = value

	@property
	def is_concentric_spheres(self):
		"""Gets whether the two selected entities are concentric spheres."""
		return self._instance.IsConcentricSpheres

	@is_concentric_spheres.setter
	def is_concentric_spheres(self, value):
		"""Gets whether the two selected entities are concentric spheres."""
		self._instance.IsConcentricSpheres = value

	@property
	def is_intersect(self):
		"""Gets whether the two selected entities intersect."""
		return self._instance.IsIntersect

	@is_intersect.setter
	def is_intersect(self, value):
		"""Gets whether the two selected entities intersect."""
		self._instance.IsIntersect = value

	@property
	def is_parallel(self):
		"""Gets whether the two selected entities are parallel."""
		return self._instance.IsParallel

	@is_parallel.setter
	def is_parallel(self, value):
		"""Gets whether the two selected entities are parallel."""
		self._instance.IsParallel = value

	@property
	def is_perpendicular(self):
		"""Gets whether the two selected entities are perpendicular."""
		return self._instance.IsPerpendicular

	@is_perpendicular.setter
	def is_perpendicular(self, value):
		"""Gets whether the two selected entities are perpendicular."""
		self._instance.IsPerpendicular = value

	@property
	def length(self):
		"""Gets the length of the selected entity."""
		return self._instance.Length

	@length.setter
	def length(self, value):
		"""Gets the length of the selected entity."""
		self._instance.Length = value

	@property
	def length_decimal_places(self):
		"""Gets or sets the number of decimal places for length measurements."""
		return self._instance.LengthDecimalPlaces

	@length_decimal_places.setter
	def length_decimal_places(self, value):
		"""Gets or sets the number of decimal places for length measurements."""
		self._instance.LengthDecimalPlaces = value

	@property
	def normal(self):
		"""Gets the normal distance (normal to the selected plane) between the selected face and plane."""
		return self._instance.Normal

	@normal.setter
	def normal(self, value):
		"""Gets the normal distance (normal to the selected plane) between the selected face and plane."""
		self._instance.Normal = value

	@property
	def normal_distance(self):
		"""Gets the normal distance (normal to the selected plane) between the selected entity and plane."""
		return self._instance.NormalDistance

	@normal_distance.setter
	def normal_distance(self, value):
		"""Gets the normal distance (normal to the selected plane) between the selected entity and plane."""
		self._instance.NormalDistance = value

	@property
	def perimeter(self):
		"""Gets the perimeter of the selected entity."""
		return self._instance.Perimeter

	@perimeter.setter
	def perimeter(self, value):
		"""Gets the perimeter of the selected entity."""
		self._instance.Perimeter = value

	@property
	def projection(self):
		"""Gets the projected distance between the two selected entities."""
		return self._instance.Projection

	@projection.setter
	def projection(self, value):
		"""Gets the projected distance between the two selected entities."""
		self._instance.Projection = value

	@property
	def projection_option(self):
		"""Gets or sets whether the distance between the selected entities is projected."""
		return self._instance.ProjectionOption

	@projection_option.setter
	def projection_option(self, value):
		"""Gets or sets whether the distance between the selected entities is projected."""
		self._instance.ProjectionOption = value

	@property
	def radius(self):
		"""Gets the radius of the selected arc or cylinder."""
		return self._instance.Radius

	@radius.setter
	def radius(self, value):
		"""Gets the radius of the selected arc or cylinder."""
		self._instance.Radius = value

	@property
	def sperical_center_distance(self):
		"""Gets the distance between the two selected spherical faces."""
		return self._instance.SpericalCenterDistance

	@sperical_center_distance.setter
	def sperical_center_distance(self, value):
		"""Gets the distance between the two selected spherical faces."""
		self._instance.SpericalCenterDistance = value

	@property
	def total_area(self):
		"""Gets the total area of the two selected entities."""
		return self._instance.TotalArea

	@total_area.setter
	def total_area(self, value):
		"""Gets the total area of the two selected entities."""
		self._instance.TotalArea = value

	@property
	def total_length(self):
		"""Gets the total length of the two selected entities."""
		return self._instance.TotalLength

	@total_length.setter
	def total_length(self, value):
		"""Gets the total length of the two selected entities."""
		self._instance.TotalLength = value

	@property
	def x(self):
		"""Gets the x coordinate of the selected point in model space."""
		return self._instance.X

	@x.setter
	def x(self, value):
		"""Gets the x coordinate of the selected point in model space."""
		self._instance.X = value

	@property
	def y(self):
		"""Gets the y coordinate of the selected point in model space."""
		return self._instance.Y

	@y.setter
	def y(self, value):
		"""Gets the y coordinate of the selected point in model space."""
		self._instance.Y = value

	@property
	def z(self):
		"""Gets the z coordinate of the selected point in model space."""
		return self._instance.Z

	@z.setter
	def z(self, value):
		"""Gets the z coordinate of the selected point in model space."""
		self._instance.Z = value

	@property
	def calculate(self):
		"""Measures the selected or specified entities."""
		return self._instance.Calculate

	@calculate.setter
	def calculate(self, value):
		"""Measures the selected or specified entities."""
		self._instance.Calculate = value

	@property
	def set_projection_entity(self):
		"""Sets the face or plane to which to project the measured distance."""
		return self._instance.SetProjectionEntity

	@set_projection_entity.setter
	def set_projection_entity(self, value):
		"""Sets the face or plane to which to project the measured distance."""
		self._instance.SetProjectionEntity = value

