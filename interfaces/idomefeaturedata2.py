# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDomeFeatureData2_members.html
class IDomeFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	def constraint_point_or_sketch(self):
		"""Gets or sets the constraining point or sketch for a dome feature."""
		# return self._instance.ConstraintPointOrSketch
		raise NotImplemented

	def direction(self):
		"""Gets or sets the direction of the dome feature."""
		# return self._instance.Direction
		raise NotImplemented

	def elliptical(self):
		"""Gets or sets whether this dome is a half ellipsoid, with a height equal to one of the ellipsoid radii."""
		# return self._instance.Elliptical
		raise NotImplemented

	def faces(self):
		"""Gets or sets the planar or non-planar faces of this dome feature."""
		# return self._instance.Faces
		raise NotImplemented

	def height(self):
		"""Gets or sets the height of the dome."""
		# return self._instance.Height
		raise NotImplemented

	def reverse_dir(self):
		"""Gets or sets whether this dome is convex or concave."""
		# return self._instance.ReverseDir
		raise NotImplemented

	def access_selections(self, top_doc, component):
		"""
		Gains access to selections used to define the dome.
		:param top_doc: Top level document (see Remarks)
		:param component: Component for the feature (see Remarks)
		"""
		# return self._instance.AccessSelections(top_doc, component)
		raise NotImplemented

	def get_face_count(self):
		"""Gets the number of planar and non-planar faces of this dome feature."""
		# return self._instance.GetFaceCount
		raise NotImplemented

	def i_access_selections(self, top_doc, component):
		"""
		Gains access to selections used to define the dome.
		:param top_doc: Top level document (see Remarks)
		:param component: Component for the feature (see Remarks)
		"""
		# return self._instance.IAccessSelections(top_doc, component)
		raise NotImplemented

	def i_get_faces(self, face_count):
		"""
		Gets the planar or non-planar faces of this dome feature.
		:param face_count: Number of planar or non-planar faces of this dome feature
		"""
		# return self._instance.IGetFaces(face_count)
		raise NotImplemented

	def i_set_faces(self, face_count, face_list):
		"""
		Sets the planar or non-planar faces of this dome feature.
		:param face_count: Number of planar or non-planar faces
		:param face_list: 

in-process, unmanaged C++: Pointer to an array of planar and non-planar faces of this dome feature
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.ISetFaces(face_count, face_list)
		raise NotImplemented

	def release_selection_access(self):
		"""Releases access to the selections used to define this dome feature."""
		# return self._instance.ReleaseSelectionAccess
		raise NotImplemented

