# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathTransform_members.html
class IMathTransform:
	def __init__(self, parent=None):
		self._instance = parent

	def array_data(self):
		"""Gets and sets the array of 16 doubles for this transform."""
		# return self._instance.ArrayData
		raise NotImplemented

	def i_array_data(self):
		"""Gets and sets the array of 16 doubles for this transform."""
		# return self._instance.IArrayData
		raise NotImplemented

	def get_data(self, x_axis_obj_out, y_axis_obj_out, z_axis_obj_out, transform_obj_out, scale_out):
		"""
		Gets the math vectors and data that describe the transformation matrix.
		:param x_axis_obj_out: Rotation about the x axis
		:param y_axis_obj_out: Rotation about the y axis
		:param z_axis_obj_out: Rotation about the z axis
		:param transform_obj_out: Transformation vector
		:param scale_out: Scale
		"""
		# return self._instance.GetData2(x_axis_obj_out, y_axis_obj_out, z_axis_obj_out, transform_obj_out, scale_out)
		raise NotImplemented

	def i_get_data(self, x_axis_obj_out, y_axis_obj_out, z_axis_obj_out, transform_obj_out, scale_out):
		"""
		Gets the math vectors and data that describe the transformation matrix.
		:param x_axis_obj_out: Rotation about the x axis
		:param y_axis_obj_out: Rotation about the y axis
		:param z_axis_obj_out: Rotation about the z axis
		:param transform_obj_out: Transformation vector
		:param scale_out: Scale
		"""
		# return self._instance.IGetData2(x_axis_obj_out, y_axis_obj_out, z_axis_obj_out, transform_obj_out, scale_out)
		raise NotImplemented

	def i_inverse(self):
		"""Creates a new math transform by inverting the values in an already existing math transform."""
		# return self._instance.IInverse
		raise NotImplemented

	def i_multiply(self, transform_obj_in):
		"""
		Multiplies two matrices together.
		:param transform_obj_in: Math transform by which to multiply the calling math transform
		"""
		# return self._instance.IMultiply(transform_obj_in)
		raise NotImplemented

	def inverse(self):
		"""Creates a new math transform by inverting the values in an already existing math transform."""
		# return self._instance.Inverse
		raise NotImplemented

	def i_set_data(self, x_axis_obj_in, y_axis_obj_in, z_axis_obj_in, transform_obj_in, scale_val_in):
		"""
		Sets the math vectors and data that describe the transformation matrix.
		:param x_axis_obj_in: X rotation math vector object of the transform
		:param y_axis_obj_in: Y rotation math vector object of the transform
		:param z_axis_obj_in: Z rotation math vector object of the transform
		:param transform_obj_in: Translation math vector object of the transform
		:param scale_val_in: Scale component of the transform
		"""
		# return self._instance.ISetData(x_axis_obj_in, y_axis_obj_in, z_axis_obj_in, transform_obj_in, scale_val_in)
		raise NotImplemented

	def multiply(self, transform_obj_in):
		"""
		Multiplies two matrices together.
		:param transform_obj_in: Math transform by which to multiply the calling math transform
		"""
		# return self._instance.Multiply(transform_obj_in)
		raise NotImplemented

	def set_data(self, x_axis_obj_in, y_axis_obj_in, z_axis_obj_in, transform_obj_in, scale_val_in):
		"""
		Sets the math vectors and data that describe the transformation matrix.
		:param x_axis_obj_in: X rotation math vector object of the transform
		:param y_axis_obj_in: Y rotation math vector object of the transform
		:param z_axis_obj_in: Z rotation math vector object of the transform
		:param transform_obj_in: Translation math vector object of the transform
		:param scale_val_in: Scale component of the transform
		"""
		# return self._instance.SetData(x_axis_obj_in, y_axis_obj_in, z_axis_obj_in, transform_obj_in, scale_val_in)
		raise NotImplemented

