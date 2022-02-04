# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgePoint_members.html
class IEdgePoint:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entity(self):
		"""Gets or sets edge or reference curve on which the point is located."""
		return self._instance.Entity

	@entity.setter
	def entity(self, value):
		"""Gets or sets edge or reference curve on which the point is located."""
		self._instance.Entity = value

	@property
	def position(self):
		"""Gets or sets the position of the midpoint on an edge or an endpoint or midpoint on a reference curve."""
		return self._instance.Position

	@position.setter
	def position(self, value):
		"""Gets or sets the position of the midpoint on an edge or an endpoint or midpoint on a reference curve."""
		self._instance.Position = value

	@property
	def get_point_coordinates(self):
		"""Gets the coordinates for this midpoint on an edge or an endpoint or midpoint on a reference curve."""
		return self._instance.GetPointCoordinates

	@get_point_coordinates.setter
	def get_point_coordinates(self, value):
		"""Gets the coordinates for this midpoint on an edge or an endpoint or midpoint on a reference curve."""
		self._instance.GetPointCoordinates = value

	@property
	def select(self):
		"""Selects a midpoint on an edge or an endpoint or midpoint on a reference curve."""
		return self._instance.Select

	@select.setter
	def select(self, value):
		"""Selects a midpoint on an edge or an endpoint or midpoint on a reference curve."""
		self._instance.Select = value

