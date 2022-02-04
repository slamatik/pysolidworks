# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.html
class IMathUtility:
	def __init__(self, parent=None):
		self._instance = parent

	def compose_transform(self, x_vec, y_vec, z_vec, trans_vec, scale):
		"""
		Creates a new transform matrix.
		:param x_vec: X-axis of the transform origin
		:param y_vec: Y-axis of the transform origin
		:param z_vec: Z-axis of the transform origin
		:param trans_vec: Translation of the origin in space
		:param scale: Scale factor (typically 1; must be > 0)
		"""
		# return self._instance.ComposeTransform(x_vec, y_vec, z_vec, trans_vec, scale)
		raise NotImplemented

	def create_point(self, array_data_in):
		"""
		Creates a new math point.
		:param array_data_in: Array of doubles representing the coordinates (x,y,z) of the point
		"""
		# return self._instance.CreatePoint(array_data_in)
		raise NotImplemented

	def create_transform(self, array_data_in):
		"""
		Creates a new math transform.
		:param array_data_in: Sixteen (16) components of the transform (see Remarks)
		"""
		# return self._instance.CreateTransform(array_data_in)
		raise NotImplemented

	def create_transform_rotate_axis(self, point_obj_in, vector_obj_in, angle):
		"""
		Creates a new math transform matrix that represents the rotation by an angle about a vector positioned at a point.
		:param point_obj_in: Center point of the axis of the transform
		:param vector_obj_in: Axis vector of the transform
		:param angle: Angle of rotation about the X axis vector
		"""
		# return self._instance.CreateTransformRotateAxis(point_obj_in, vector_obj_in, angle)
		raise NotImplemented

	def create_vector(self, array_data_in):
		"""
		Creates a math vector.
		:param array_data_in: Array of doubles representing the x,y,z components of the vector
		"""
		# return self._instance.CreateVector(array_data_in)
		raise NotImplemented

	def i_create_point(self, array_data_in):
		"""
		Creates a new math point.
		:param array_data_in: Array of doubles representing the coordinates (x,y,z) of the point
		"""
		# return self._instance.ICreatePoint(array_data_in)
		raise NotImplemented

	def i_create_transform(self, array_data_in):
		"""
		Creates a new math transform.
		:param array_data_in: 

in-process, unmanaged C++: Pointer to sixteen (16) components of the transform (see Remarks)
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.ICreateTransform(array_data_in)
		raise NotImplemented

	def i_create_transform_rotate_axis(self, point_obj_in, vector_obj_in, angle):
		"""
		Creates a new math transform matrix that represents the rotation by an angle about a vector positioned at a point.
		:param point_obj_in: Center point of the axis of the transform
		:param vector_obj_in: Axis vector of the transform
		:param angle: Angle of rotation about the X axis vector
		"""
		# return self._instance.ICreateTransformRotateAxis(point_obj_in, vector_obj_in, angle)
		raise NotImplemented

	def i_create_vector(self, array_data_in):
		"""
		Creates a math vector.
		:param array_data_in: 

in-process, unmanaged C++: Pointer to an array of doubles representing the x,y,z components of the vector
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.ICreateVector(array_data_in)
		raise NotImplemented

