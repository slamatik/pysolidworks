# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISafeArrayUtility_members.html
class ISafeArrayUtility:
	def __init__(self, parent=None):
		self._instance = parent

	def get_boolean(self, variant_array, index):
		"""
		Gets the specified Boolean value in a Variant SafeArray of Boolean values.
		:param variant_array: Variant SafeArray of Boolean values
		:param index: Index of Boolean value
		"""
		# return self._instance.GetBoolean(variant_array, index)
		raise NotImplemented

	def get_bstr(self, variant_array, index):
		"""
		Gets the specified BSTR in a Variant SafeArray of BSTRs.
		:param variant_array: Variant SafeArray of BSTRs
		:param index: Index of BSTR
		"""
		# return self._instance.GetBstr(variant_array, index)
		raise NotImplemented

	def get_byte(self, variant_array, index):
		"""
		Gets the specified byte value in a Variant SafeArray of byte values.
		:param variant_array: Variant SafeArray of byte values
		:param index: Index of byte value
		"""
		# return self._instance.GetByte(variant_array, index)
		raise NotImplemented

	def get_dispatch(self, variant_array, index):
		"""
		Gets the specified Dispatch object in a Variant SafeArray of Dispatch objects.
		:param variant_array: Variant SafeArray of Dispatch objects
		:param index: Index of Dispatch object
		"""
		# return self._instance.GetDispatch(variant_array, index)
		raise NotImplemented

	def get_double(self, variant_array, index):
		"""
		Gets the specified double value in a Variant SafeArray of double values.
		:param variant_array: Variant SafeArray of double values
		:param index: Index of double value
		"""
		# return self._instance.GetDouble(variant_array, index)
		raise NotImplemented

	def get_info(self, variant_array, count, type):
		"""
		Gets the number of elements in a Variant SafeArray and their data type.
		:param variant_array: Variant SafeArray
		:param count: Number of elements in VariantArray
		:param type: Data type of elements in VariantArray as defined in swSafeArrayType_e
		"""
		# return self._instance.GetInfo(variant_array, count, type)
		raise NotImplemented

	def get_long(self, variant_array, index):
		"""
		Gets the specified long value in a Variant SafeArray of long values.
		:param variant_array: Variant SafeArray of long values
		:param index: Index of a long value
		"""
		# return self._instance.GetLong(variant_array, index)
		raise NotImplemented

	def get_long_long(self, variant_array, index):
		"""
		Gets the specified long long value in a Variant SafeArray of long long values.
		:param variant_array: Variant SafeArray of long long values
		:param index: Index of long long value
		"""
		# return self._instance.GetLongLong(variant_array, index)
		raise NotImplemented

	def get_short(self, variant_array, index):
		"""
		Gets the specified short value in a Variant SafeArray of short values.
		:param variant_array: Variant SafeArray of short values
		:param index: Index of short value
		"""
		# return self._instance.GetShort(variant_array, index)
		raise NotImplemented

	def get_u_n_k_n_o_w_n(self, variant_array, index):
		"""
		Gets the specified UNKNOWN object in a Variant SafeArray of UNKNOWN objects.
		:param variant_array: Variant SafeArray of UNKNOWN objects
		:param index: Index of UNKNOWN object
		"""
		# return self._instance.GetUNKNOWN(variant_array, index)
		raise NotImplemented

	def pack_variant(self, variant_array, count, type, data):
		"""
		Packs the specified native SOLIDWORKS Dispatch-based objects of the same data type into a Variant SafeArray and returns that packed Variant SafeArray to use in methods requiring passing a packed Variant SafeArray.
		:param variant_array: Packed Variant SafeArray
		:param count: Number of native SOLIDWORKS Dispatch-based objects of Type
		:param type: Data type as defined in swSafeArrayType_e
		:param data: Native SOLIDWORKS Dispatch-based objects of Type
		"""
		# return self._instance.PackVariant(variant_array, count, type, data)
		raise NotImplemented

	def put_boolean(self, variant_array, index, value):
		"""
		Adds the specified Boolean value to a Variant SafeArray of Boolean values.
		:param variant_array: Variant SafeArray of Boolean values
		:param index: Index of Boolean value
		:param value: Boolean value
		"""
		# return self._instance.PutBoolean(variant_array, index, value)
		raise NotImplemented

	def put_bstr(self, variant_array, index, value):
		"""
		Adds the specified BSTR to a Variant SafeArray of BSTRs.
		:param variant_array: Variant SafeArray of BSTRs
		:param index: Index of BSTR
		:param value: BSTR
		"""
		# return self._instance.PutBstr(variant_array, index, value)
		raise NotImplemented

	def put_byte(self, variant_array, index, value):
		"""
		Adds the specified byte value to a Variant SafeArray of byte values.
		:param variant_array: Variant SafeArray of byte values
		:param index: Index of byte value
		:param value: Byte value
		"""
		# return self._instance.PutByte(variant_array, index, value)
		raise NotImplemented

	def put_dispatch(self, variant_array, index, value):
		"""
		Adds the specified Dispatch object to a Variant SafeArray of Dispatch objects.
		:param variant_array: Variant SafeArray of Dispatch objects
		:param index: Index of Dispatch object
		:param value: Dispatch object
		"""
		# return self._instance.PutDispatch(variant_array, index, value)
		raise NotImplemented

	def put_double(self, variant_array, index, value):
		"""
		Adds the specified double value to a Variant SafeArray of double values.
		:param variant_array: Variant SafeArray of double values
		:param index: Index of double value
		:param value: Double value
		"""
		# return self._instance.PutDouble(variant_array, index, value)
		raise NotImplemented

	def put_long(self, variant_array, index, value):
		"""
		Adds the specified long value to a Variant SafeArray of long values.
		:param variant_array: Variant SafeArray of long values
		:param index: Index of long value
		:param value: Long value
		"""
		# return self._instance.PutLong(variant_array, index, value)
		raise NotImplemented

	def put_long_long(self, variant_array, index, value):
		"""
		Adds the specified long long value to a Variant SafeArray of long long values.
		:param variant_array: Variant SafeArray of long long values
		:param index: Index of long long value
		:param value: Long long value
		"""
		# return self._instance.PutLongLong(variant_array, index, value)
		raise NotImplemented

	def put_short(self, variant_array, index, value):
		"""
		Adds the specified short value to a Variant SafeArray of short values.
		:param variant_array: Variant SafeArray of short values
		:param index: Index of short value
		:param value: Short value
		"""
		# return self._instance.PutShort(variant_array, index, value)
		raise NotImplemented

	def put_u_n_k_n_o_w_n(self, variant_array, index, value):
		"""
		Adds the specified UNKNOWN object to a Variant SafeArray of UNKNOWN objects.
		:param variant_array: Variant SafeArray of UNKNOWN objects
		:param index: Index of UNKNOWN object
		:param value: UNKNOWN object
		"""
		# return self._instance.PutUNKNOWN(variant_array, index, value)
		raise NotImplemented

	def un_pack_variant(self, variant_array, count):
		"""
		Unpacks the specified packed Variant SafeArray to native SOLIDWORKS Dispatch-based objects of the same data type.
		:param variant_array: Variant SafeArray
		:param count: Number of native SOLIDWORKS Dispatch-based objects of the same data type
		"""
		# return self._instance.UnPackVariant(variant_array, count)
		raise NotImplemented

