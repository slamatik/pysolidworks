# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties_members.html
class IFaceDecalProperties:
	def __init__(self, parent=None):
		self._instance = parent

	def texture_angle(self):
		"""Gets the angle of the texture of the decal."""
		# return self._instance.TextureAngle
		raise NotImplemented

	def texture_angle_u_v(self):
		"""Gets the UV angle of the texture of the decal."""
		# return self._instance.TextureAngleUV
		raise NotImplemented

	def texture_filename(self):
		"""Gets the file name of the texture of the decal."""
		# return self._instance.TextureFilename
		raise NotImplemented

	def texture_filename_i_d(self):
		"""Gets the ID of the texture file name of the decal."""
		# return self._instance.TextureFilenameID
		raise NotImplemented

	def texture_i_d(self):
		"""Gets the ID of the texture of the decal."""
		# return self._instance.TextureID
		raise NotImplemented

	def texture_map_i_d(self):
		"""Gets the map ID of the texture of the decal."""
		# return self._instance.TextureMapID
		raise NotImplemented

	def texture_mirrored(self):
		"""Gets whether the texture of the decal is mirrored."""
		# return self._instance.TextureMirrored
		raise NotImplemented

	def texture_render_mode(self):
		"""Gets the render mode of the texture of the decal."""
		# return self._instance.TextureRenderMode
		raise NotImplemented

	def texture_translation_u(self):
		"""Gets the translation of the decal texture in the U direction."""
		# return self._instance.TextureTranslationU
		raise NotImplemented

	def texture_translation_v(self):
		"""Gets the translation of the decal texture in the V direction."""
		# return self._instance.TextureTranslationV
		raise NotImplemented

	def texture_translation_x(self):
		"""Gets the translation of the decal texture in the X direction."""
		# return self._instance.TextureTranslationX
		raise NotImplemented

	def texture_translation_y(self):
		"""Gets the translation of the decal texture in the Y direction."""
		# return self._instance.TextureTranslationY
		raise NotImplemented

	def texture_u_scale(self):
		"""Gets the decal texture scale in the U direction."""
		# return self._instance.TextureUScale
		raise NotImplemented

	def texture_v_scale(self):
		"""Gets the decal texture scale in the V direction."""
		# return self._instance.TextureVScale
		raise NotImplemented

