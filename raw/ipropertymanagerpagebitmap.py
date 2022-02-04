# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageBitmap_members.html
class IPropertyManagerPageBitmap:
	def __init__(self, parent=None):
		self._instance = parent

	def set_bitmap_by_name(self, color_bitmap, mask_bitmap):
		"""
		Sets the bitmap for this control.
		:param color_bitmap: Full path and filename of the bitmap on disk
		:param mask_bitmap: Full path and filename of the alpha mask bitmap on disk
		"""
		# return self._instance.SetBitmapByName(color_bitmap, mask_bitmap)
		raise NotImplemented

	def set_standard_bitmap(self, bitmap):
		"""
		Sets the bitmap or PNG image for this control.
		:param bitmap: Control standard type as defined in swBitmapControlStandardTypes_e
		"""
		# return self._instance.SetStandardBitmap(bitmap)
		raise NotImplemented

