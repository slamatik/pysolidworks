# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html
class IDomeFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def constraint_point_or_sketch(self):
		"""Gets or sets the constraining point or sketch for a dome feature."""
		return self._instance.ConstraintPointOrSketch

	@constraint_point_or_sketch.setter
	def constraint_point_or_sketch(self, value):
		"""Gets or sets the constraining point or sketch for a dome feature."""
		self._instance.ConstraintPointOrSketch = value

	@property
	def direction(self):
		"""Gets or sets the direction of the dome feature."""
		return self._instance.Direction

	@direction.setter
	def direction(self, value):
		"""Gets or sets the direction of the dome feature."""
		self._instance.Direction = value

	@property
	def elliptical(self):
		"""Gets or sets whether this dome is a half ellipsoid, with a height equal to one of the ellipsoid radii."""
		return self._instance.Elliptical

	@elliptical.setter
	def elliptical(self, value):
		"""Gets or sets whether this dome is a half ellipsoid, with a height equal to one of the ellipsoid radii."""
		self._instance.Elliptical = value

	@property
	def faces(self):
		"""Gets or sets the planar or non-planar faces of this dome feature."""
		return self._instance.Faces

	@faces.setter
	def faces(self, value):
		"""Gets or sets the planar or non-planar faces of this dome feature."""
		self._instance.Faces = value

	@property
	def height(self):
		"""Gets or sets the height of the dome."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of the dome."""
		self._instance.Height = value

	@property
	def reverse_dir(self):
		"""Gets or sets whether this dome is convex or concave."""
		return self._instance.ReverseDir

	@reverse_dir.setter
	def reverse_dir(self, value):
		"""Gets or sets whether this dome is convex or concave."""
		self._instance.ReverseDir = value

	@property
	def access_selections(self):
		"""Gains access to selections used to define the dome."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections used to define the dome."""
		self._instance.AccessSelections = value

	@property
	def get_face_count(self):
		"""Gets the number of planar and non-planar faces of this dome feature."""
		return self._instance.GetFaceCount

	@get_face_count.setter
	def get_face_count(self, value):
		"""Gets the number of planar and non-planar faces of this dome feature."""
		self._instance.GetFaceCount = value

	@property
	def i_access_selections(self):
		"""Gains access to selections used to define the dome."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to selections used to define the dome."""
		self._instance.IAccessSelections = value

	@property
	def i_get_faces(self):
		"""Gets the planar or non-planar faces of this dome feature."""
		return self._instance.IGetFaces

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets the planar or non-planar faces of this dome feature."""
		self._instance.IGetFaces = value

	@property
	def i_set_faces(self):
		"""Sets the planar or non-planar faces of this dome feature."""
		return self._instance.ISetFaces

	@i_set_faces.setter
	def i_set_faces(self, value):
		"""Sets the planar or non-planar faces of this dome feature."""
		self._instance.ISetFaces = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define this dome feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define this dome feature."""
		self._instance.ReleaseSelectionAccess = value

