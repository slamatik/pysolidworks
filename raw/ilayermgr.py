# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILayerMgr_members.html
class ILayerMgr:
	def __init__(self, parent=None):
		self._instance = parent

	def add_layer(self, name_in, desc_in, color_in, style_in, width_in):
		"""
		Adds a layer to this drawing document.
		:param name_in: Layer name
		:param desc_in: Description for the new layer
		:param color_in: COLORREF value specifying the desired color of items within this layer
		:param style_in: Line style as defined in swLineStyles_e
		:param width_in: Line width as defined in swLineWeights_e
		"""
		# return self._instance.AddLayer(name_in, desc_in, color_in, style_in, width_in)
		raise NotImplemented

	def delete_layer(self, name):
		"""
		Deletes the specified layer in this drawing document.
		:param name: Name of the layer to delete
		"""
		# return self._instance.DeleteLayer(name)
		raise NotImplemented

	def get_count(self):
		"""Gets the number of layers in this drawing document."""
		# return self._instance.GetCount
		raise NotImplemented

	def get_current_layer(self):
		"""Gets the name of the current (active) layer in this drawing document."""
		# return self._instance.GetCurrentLayer
		raise NotImplemented

	def get_layer(self, name_in):
		"""
		Gets the specified layer in this drawing document.
		:param name_in: Layer name
		"""
		# return self._instance.GetLayer(name_in)
		raise NotImplemented

	def get_layer_by_id(self, layer_id):
		"""
		Gets the layer using the specified layer ID in this drawing document.
		:param layer_id: Layer ID
		"""
		# return self._instance.GetLayerById(layer_id)
		raise NotImplemented

	def get_layer_list(self):
		"""Gets a list of layers in this drawing document."""
		# return self._instance.GetLayerList
		raise NotImplemented

	def i_get_layer(self, name_in):
		"""
		Gets the specified layer in this drawing document.
		:param name_in: Layer name
		"""
		# return self._instance.IGetLayer(name_in)
		raise NotImplemented

	def i_get_layer_by_id(self, layer_id):
		"""
		Gets the layer using the specified layer ID in this drawing document.
		:param layer_id: Layer ID
		"""
		# return self._instance.IGetLayerById(layer_id)
		raise NotImplemented

	def i_get_layer_list(self):
		"""Gets a list of layers in this drawing document."""
		# return self._instance.IGetLayerList
		raise NotImplemented

	def set_current_layer(self, name_in):
		"""
		Sets the current (or active) layer in this drawing document.
		:param name_in: Name of the layer to become the active layer
		"""
		# return self._instance.SetCurrentLayer(name_in)
		raise NotImplemented

