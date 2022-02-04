# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html
class IDecal:
	def __init__(self, parent=None):
		self._instance = parent

	def decal_i_d(self):
		"""Gets the SOLIDWORKS decal ID."""
		# return self._instance.DecalID
		raise NotImplemented

	@property
	def hidden(self):
		"""Gets or sets whether the decal hidden."""
		return self._instance.Hidden

	@hidden.setter
	def hidden(self, value):
		"""Gets or sets whether the decal hidden."""
		self._instance.Hidden = value

	@property
	def mask_filename(self):
		"""Gets or sets the path and filename for the image to use as a mask for this decal."""
		return self._instance.MaskFilename

	@mask_filename.setter
	def mask_filename(self, value):
		"""Gets or sets the path and filename for the image to use as a mask for this decal."""
		self._instance.MaskFilename = value

	@property
	def mask_invert(self):
		"""Gets or sets whether the mask is inverted."""
		return self._instance.MaskInvert

	@mask_invert.setter
	def mask_invert(self, value):
		"""Gets or sets whether the mask is inverted."""
		self._instance.MaskInvert = value

	@property
	def mask_type(self):
		"""Gets or sets the type of mask used with this decal."""
		return self._instance.MaskType

	@mask_type.setter
	def mask_type(self, value):
		"""Gets or sets the type of mask used with this decal."""
		self._instance.MaskType = value

	@property
	def get_mask_excluded_colors_count(self):
		"""Gets the number of colors excluded from the mask image for this decal."""
		return self._instance.GetMaskExcludedColorsCount

	@get_mask_excluded_colors_count.setter
	def get_mask_excluded_colors_count(self, value):
		"""Gets the number of colors excluded from the mask image for this decal."""
		self._instance.GetMaskExcludedColorsCount = value

	@property
	def i_get_mask_excluded_colors(self):
		"""Gets the colors excluded from the mask image for this decal."""
		return self._instance.IGetMaskExcludedColors

	@i_get_mask_excluded_colors.setter
	def i_get_mask_excluded_colors(self, value):
		"""Gets the colors excluded from the mask image for this decal."""
		self._instance.IGetMaskExcludedColors = value

	@property
	def i_set_mask_excluded_colors(self):
		"""Sets the colors to exclude from the mask image for this decal."""
		return self._instance.ISetMaskExcludedColors

	@i_set_mask_excluded_colors.setter
	def i_set_mask_excluded_colors(self, value):
		"""Sets the colors to exclude from the mask image for this decal."""
		self._instance.ISetMaskExcludedColors = value

