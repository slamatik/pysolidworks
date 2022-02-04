# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPicture_members.html
class ISketchPicture:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the rotation angle of the picture in the sketch."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the rotation angle of the picture in the sketch."""
		self._instance.Angle = value

	@property
	def flipped(self):
		"""Gets whether the picture has been flipped in the sketch."""
		return self._instance.Flipped

	@flipped.setter
	def flipped(self, value):
		"""Gets whether the picture has been flipped in the sketch."""
		self._instance.Flipped = value

	@property
	def flip(self):
		"""Flips the picture, in its same position, either side to side or top to bottom."""
		return self._instance.Flip

	@flip.setter
	def flip(self, value):
		"""Flips the picture, in its same position, either side to side or top to bottom."""
		self._instance.Flip = value

	@property
	def get_feature(self):
		"""Gets the feature associated with this sketch picture."""
		return self._instance.GetFeature

	@get_feature.setter
	def get_feature(self, value):
		"""Gets the feature associated with this sketch picture."""
		self._instance.GetFeature = value

	@property
	def get_origin(self):
		"""Gets the origin of the picture on the sketch."""
		return self._instance.GetOrigin

	@get_origin.setter
	def get_origin(self, value):
		"""Gets the origin of the picture on the sketch."""
		self._instance.GetOrigin = value

	@property
	def get_pixelmap(self):
		"""Gets the picture pixels."""
		return self._instance.GetPixelmap

	@get_pixelmap.setter
	def get_pixelmap(self, value):
		"""Gets the picture pixels."""
		self._instance.GetPixelmap = value

	@property
	def get_pixelmap_size(self):
		"""Gets the size of the array for the picture pixels."""
		return self._instance.GetPixelmapSize

	@get_pixelmap_size.setter
	def get_pixelmap_size(self, value):
		"""Gets the size of the array for the picture pixels."""
		self._instance.GetPixelmapSize = value

	@property
	def get_point_on_sketch_from_pixel(self):
		"""Gets the sketch coordinate for the specified pixel."""
		return self._instance.GetPointOnSketchFromPixel

	@get_point_on_sketch_from_pixel.setter
	def get_point_on_sketch_from_pixel(self, value):
		"""Gets the sketch coordinate for the specified pixel."""
		self._instance.GetPointOnSketchFromPixel = value

	@property
	def get_size(self):
		"""Gets the size of the picture on the sketch."""
		return self._instance.GetSize

	@get_size.setter
	def get_size(self, value):
		"""Gets the size of the picture on the sketch."""
		self._instance.GetSize = value

	@property
	def get_transparency(self):
		"""Gets transparency parameters for this picture."""
		return self._instance.GetTransparency

	@get_transparency.setter
	def get_transparency(self, value):
		"""Gets transparency parameters for this picture."""
		self._instance.GetTransparency = value

	@property
	def i_get_pixelmap(self):
		"""Gets the picture pixels."""
		return self._instance.IGetPixelmap

	@i_get_pixelmap.setter
	def i_get_pixelmap(self, value):
		"""Gets the picture pixels."""
		self._instance.IGetPixelmap = value

	@property
	def set_origin(self):
		"""Sets the origin of the picture of the sketch."""
		return self._instance.SetOrigin

	@set_origin.setter
	def set_origin(self, value):
		"""Sets the origin of the picture of the sketch."""
		self._instance.SetOrigin = value

	@property
	def set_size(self):
		"""Sets the size of the picture on the sketch."""
		return self._instance.SetSize

	@set_size.setter
	def set_size(self, value):
		"""Sets the size of the picture on the sketch."""
		self._instance.SetSize = value

	@property
	def set_transparency(self):
		"""Sets the transparency parameters of this picture on the sketch."""
		return self._instance.SetTransparency

	@set_transparency.setter
	def set_transparency(self, value):
		"""Sets the transparency parameters of this picture on the sketch."""
		self._instance.SetTransparency = value

