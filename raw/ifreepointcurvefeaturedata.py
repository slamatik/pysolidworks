# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFreePointCurveFeatureData_members.html
class IFreePointCurveFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def point_array(self):
		"""Gets or sets the list of X, Y, Z coordinates for the points for this free-point curve."""
		return self._instance.PointArray

	@point_array.setter
	def point_array(self, value):
		"""Gets or sets the list of X, Y, Z coordinates for the points for this free-point curve."""
		self._instance.PointArray = value

	@property
	def get_point_count(self):
		"""Gets the number of doubles (3 * number of points) of this free-point curve."""
		return self._instance.GetPointCount

	@get_point_count.setter
	def get_point_count(self, value):
		"""Gets the number of doubles (3 * number of points) of this free-point curve."""
		self._instance.GetPointCount = value

	@property
	def i_get_point_array(self):
		"""Gets the list of X, Y, Z coordinates for the points for this free-point curve."""
		return self._instance.IGetPointArray

	@i_get_point_array.setter
	def i_get_point_array(self, value):
		"""Gets the list of X, Y, Z coordinates for the points for this free-point curve."""
		self._instance.IGetPointArray = value

	@property
	def i_set_point_array(self):
		"""Sets the list of X, Y, Z coordinates for the points for this free-point curve."""
		return self._instance.ISetPointArray

	@i_set_point_array.setter
	def i_set_point_array(self, value):
		"""Sets the list of X, Y, Z coordinates for the points for this free-point curve."""
		self._instance.ISetPointArray = value

	@property
	def load_points_from_file(self):
		"""Loads the points for this free-point curve from a file."""
		return self._instance.LoadPointsFromFile

	@load_points_from_file.setter
	def load_points_from_file(self, value):
		"""Loads the points for this free-point curve from a file."""
		self._instance.LoadPointsFromFile = value

	@property
	def save_points_to_file(self):
		"""Saves the points for this free-point curve to a file."""
		return self._instance.SavePointsToFile

	@save_points_to_file.setter
	def save_points_to_file(self, value):
		"""Saves the points for this free-point curve to a file."""
		self._instance.SavePointsToFile = value

