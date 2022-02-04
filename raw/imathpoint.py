# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint_members.html
class IMathPoint:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def array_data(self):
		"""Gets or sets the array of x,y,z coordinates that describe this math point."""
		return self._instance.ArrayData

	@array_data.setter
	def array_data(self, value):
		"""Gets or sets the array of x,y,z coordinates that describe this math point."""
		self._instance.ArrayData = value

	@property
	def i_array_data(self):
		"""Gets or sets the array of x,y,z coordinates that describe this math point."""
		return self._instance.IArrayData

	@i_array_data.setter
	def i_array_data(self, value):
		"""Gets or sets the array of x,y,z coordinates that describe this math point."""
		self._instance.IArrayData = value

	@property
	def add_vector(self):
		"""Translates a math point by a math vector to create a new math point."""
		return self._instance.AddVector

	@add_vector.setter
	def add_vector(self, value):
		"""Translates a math point by a math vector to create a new math point."""
		self._instance.AddVector = value

	@property
	def convert_to_vector(self):
		"""Converts a math point to a math vector by using the three coordinates of the math point for the components of the math vector."""
		return self._instance.ConvertToVector

	@convert_to_vector.setter
	def convert_to_vector(self, value):
		"""Converts a math point to a math vector by using the three coordinates of the math point for the components of the math vector."""
		self._instance.ConvertToVector = value

	@property
	def i_add_vector(self):
		"""Translates a math point by a math vector to create a new math point."""
		return self._instance.IAddVector

	@i_add_vector.setter
	def i_add_vector(self, value):
		"""Translates a math point by a math vector to create a new math point."""
		self._instance.IAddVector = value

	@property
	def i_convert_to_vector(self):
		"""Converts a math point to a math vector by using the three coordinates of the math point for the components of the math vector."""
		return self._instance.IConvertToVector

	@i_convert_to_vector.setter
	def i_convert_to_vector(self, value):
		"""Converts a math point to a math vector by using the three coordinates of the math point for the components of the math vector."""
		self._instance.IConvertToVector = value

	@property
	def i_multiply_transform(self):
		"""Multiplies a math point with a math transform; the point is rotated, scaled, and then translated."""
		return self._instance.IMultiplyTransform

	@i_multiply_transform.setter
	def i_multiply_transform(self, value):
		"""Multiplies a math point with a math transform; the point is rotated, scaled, and then translated."""
		self._instance.IMultiplyTransform = value

	@property
	def i_scale(self):
		"""Scales a math point's magnitude."""
		return self._instance.IScale

	@i_scale.setter
	def i_scale(self, value):
		"""Scales a math point's magnitude."""
		self._instance.IScale = value

	@property
	def i_subtract(self):
		"""Gets a math vector that describes the difference between the math point magnitude from the calling math point."""
		return self._instance.ISubtract

	@i_subtract.setter
	def i_subtract(self, value):
		"""Gets a math vector that describes the difference between the math point magnitude from the calling math point."""
		self._instance.ISubtract = value

	@property
	def i_subtract_vector(self):
		"""Gets a math point that describes the difference between a math vector's magnitude from the calling math point"""
		return self._instance.ISubtractVector

	@i_subtract_vector.setter
	def i_subtract_vector(self, value):
		"""Gets a math point that describes the difference between a math vector's magnitude from the calling math point"""
		self._instance.ISubtractVector = value

	@property
	def multiply_transform(self):
		"""Multiplies a math point with a math transform; the point is rotated, scaled, and then translated."""
		return self._instance.MultiplyTransform

	@multiply_transform.setter
	def multiply_transform(self, value):
		"""Multiplies a math point with a math transform; the point is rotated, scaled, and then translated."""
		self._instance.MultiplyTransform = value

	@property
	def scale(self):
		"""Scales a math point's magnitude."""
		return self._instance.Scale

	@scale.setter
	def scale(self, value):
		"""Scales a math point's magnitude."""
		self._instance.Scale = value

	@property
	def subtract(self):
		"""Gets a math vector that describes the difference between the math point magnitude from the calling math point."""
		return self._instance.Subtract

	@subtract.setter
	def subtract(self, value):
		"""Gets a math vector that describes the difference between the math point magnitude from the calling math point."""
		self._instance.Subtract = value

	@property
	def subtract_vector(self):
		"""Gets a math point that describes the difference between a math vector's magnitude from the calling math point"""
		return self._instance.SubtractVector

	@subtract_vector.setter
	def subtract_vector(self, value):
		"""Gets a math point that describes the difference between a math vector's magnitude from the calling math point"""
		self._instance.SubtractVector = value

