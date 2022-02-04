# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector_members.html
class IMathVector:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def array_data(self):
		"""Gets or sets the array of three doubles for this vector."""
		return self._instance.ArrayData

	@array_data.setter
	def array_data(self, value):
		"""Gets or sets the array of three doubles for this vector."""
		self._instance.ArrayData = value

	@property
	def i_array_data(self):
		"""Gets or sets the array of three doubles for this vector."""
		return self._instance.IArrayData

	@i_array_data.setter
	def i_array_data(self, value):
		"""Gets or sets the array of three doubles for this vector."""
		self._instance.IArrayData = value

	@property
	def add(self):
		"""Adds this math vector with the specified math vector."""
		return self._instance.Add

	@add.setter
	def add(self, value):
		"""Adds this math vector with the specified math vector."""
		self._instance.Add = value

	@property
	def convert_to_point(self):
		"""Converts this math vector to a point by using the three components of the math vector to be the coordinates of a new math point."""
		return self._instance.ConvertToPoint

	@convert_to_point.setter
	def convert_to_point(self, value):
		"""Converts this math vector to a point by using the three components of the math vector to be the coordinates of a new math point."""
		self._instance.ConvertToPoint = value

	@property
	def cross(self):
		"""Gets the cross product between two math vectors."""
		return self._instance.Cross

	@cross.setter
	def cross(self, value):
		"""Gets the cross product between two math vectors."""
		self._instance.Cross = value

	@property
	def dot(self):
		"""Gets the value of the dot product between two math vectors."""
		return self._instance.Dot

	@dot.setter
	def dot(self, value):
		"""Gets the value of the dot product between two math vectors."""
		self._instance.Dot = value

	@property
	def get_length(self):
		"""Gets the length of a math vector."""
		return self._instance.GetLength

	@get_length.setter
	def get_length(self, value):
		"""Gets the length of a math vector."""
		self._instance.GetLength = value

	@property
	def i_add(self):
		"""Adds this math vector with the specified math vector."""
		return self._instance.IAdd

	@i_add.setter
	def i_add(self, value):
		"""Adds this math vector with the specified math vector."""
		self._instance.IAdd = value

	@property
	def i_convert_to_point(self):
		"""Converts this math vector to a point by using the three components of the math vector to be the coordinates of a new math point."""
		return self._instance.IConvertToPoint

	@i_convert_to_point.setter
	def i_convert_to_point(self, value):
		"""Converts this math vector to a point by using the three components of the math vector to be the coordinates of a new math point."""
		self._instance.IConvertToPoint = value

	@property
	def i_cross(self):
		"""Gets the cross product between two math vectors."""
		return self._instance.ICross

	@i_cross.setter
	def i_cross(self, value):
		"""Gets the cross product between two math vectors."""
		self._instance.ICross = value

	@property
	def i_dot(self):
		"""Gets the value of the dot product between two math vectors."""
		return self._instance.IDot

	@i_dot.setter
	def i_dot(self, value):
		"""Gets the value of the dot product between two math vectors."""
		self._instance.IDot = value

	@property
	def i_multiply_transform(self):
		"""Multiplies this math vector by the specified math transform."""
		return self._instance.IMultiplyTransform

	@i_multiply_transform.setter
	def i_multiply_transform(self, value):
		"""Multiplies this math vector by the specified math transform."""
		self._instance.IMultiplyTransform = value

	@property
	def i_scale(self):
		"""Scales this math vector's magnitude by a factor and returns a new math vector."""
		return self._instance.IScale

	@i_scale.setter
	def i_scale(self, value):
		"""Scales this math vector's magnitude by a factor and returns a new math vector."""
		self._instance.IScale = value

	@property
	def i_subtract(self):
		"""Subtracts the specified math vector's magnitude from this math vector and returns a new math vector."""
		return self._instance.ISubtract

	@i_subtract.setter
	def i_subtract(self, value):
		"""Subtracts the specified math vector's magnitude from this math vector and returns a new math vector."""
		self._instance.ISubtract = value

	@property
	def multiply_transform(self):
		"""Multiplies this math vector by the specified math transform."""
		return self._instance.MultiplyTransform

	@multiply_transform.setter
	def multiply_transform(self, value):
		"""Multiplies this math vector by the specified math transform."""
		self._instance.MultiplyTransform = value

	@property
	def normalise(self):
		"""Gets the unit-length vector for this math vector."""
		return self._instance.Normalise

	@normalise.setter
	def normalise(self, value):
		"""Gets the unit-length vector for this math vector."""
		self._instance.Normalise = value

	@property
	def scale(self):
		"""Scales this math vector's magnitude by a factor and returns a new math vector."""
		return self._instance.Scale

	@scale.setter
	def scale(self, value):
		"""Scales this math vector's magnitude by a factor and returns a new math vector."""
		self._instance.Scale = value

	@property
	def subtract(self):
		"""Subtracts the specified math vector's magnitude from this math vector and returns a new math vector."""
		return self._instance.Subtract

	@subtract.setter
	def subtract(self, value):
		"""Subtracts the specified math vector's magnitude from this math vector and returns a new math vector."""
		self._instance.Subtract = value

