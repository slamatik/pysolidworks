# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmapButton_members.html
class IPropertyManagerPageBitmapButton:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def checked(self):
		"""Gets or sets the state of the bitmap button."""
		return self._instance.Checked

	@checked.setter
	def checked(self, value):
		"""Gets or sets the state of the bitmap button."""
		self._instance.Checked = value

	@property
	def is_checkable(self):
		"""Gets whether the bitmap button is clickable."""
		return self._instance.IsCheckable

	@is_checkable.setter
	def is_checkable(self, value):
		"""Gets whether the bitmap button is clickable."""
		self._instance.IsCheckable = value

	@property
	def set_bitmaps(self):
		"""Sets the images for this button."""
		return self._instance.SetBitmaps

	@set_bitmaps.setter
	def set_bitmaps(self, value):
		"""Sets the images for this button."""
		self._instance.SetBitmaps = value

	@property
	def set_bitmaps_by_name(self):
		"""Inserts the specified image for this button."""
		return self._instance.SetBitmapsByName3

	@set_bitmaps_by_name.setter
	def set_bitmaps_by_name(self, value):
		"""Inserts the specified image for this button."""
		self._instance.SetBitmapsByName3 = value

	@property
	def set_bitmapsx(self):
		"""Sets the images for this button in 64-bit applications."""
		return self._instance.SetBitmapsx64

	@set_bitmapsx.setter
	def set_bitmapsx(self, value):
		"""Sets the images for this button in 64-bit applications."""
		self._instance.SetBitmapsx64 = value

	@property
	def set_standard_bitmaps(self):
		"""Sets the standard images for this button."""
		return self._instance.SetStandardBitmaps

	@set_standard_bitmaps.setter
	def set_standard_bitmaps(self, value):
		"""Sets the standard images for this button."""
		self._instance.SetStandardBitmaps = value

