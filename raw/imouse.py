# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMouse_members.html
class IMouse:
	def __init__(self, parent=None):
		self._instance = parent

	def mouse_wheel_x_y_z(self, x, y, z, clicks, flags):
		"""
		Zoom in or zoom out using the mouse.
		:param x: x coordinate where to move the pointer
		:param y: y coordinate where to move the pointer
		:param z: z coordinate where to move the pointer
		:param clicks: Number of clicks to zoom in and out; specify -120 to to zoom in one click and specify 120 to to zoom out
		:param flags: Mouse command as defined in swMouse_e (see Remarks)
		"""
		# return self._instance.MouseWheelXYZ(x, y, z, clicks, flags)
		raise NotImplemented

	def move(self, x, y, flags):
		"""
		Moves the mouse pointer in the window space.
		:param x: x coordinate where to move the pointer
		:param y: y coordinate where to move the pointer
		:param flags: Mouse command as defined in swMouse_e (see Remarks)
		"""
		# return self._instance.Move(x, y, flags)
		raise NotImplemented

	def move_x_y_z(self, x, y, z, flags):
		"""
		Moves the mouse pointer in the model space.
		:param x: x coordinate where to move the pointer
		:param y: y coordinate where to move the pointer
		:param z: z coordinate where to move the pointer
		:param flags: Mouse command as defined in swMouse_e (see Remarks)
		"""
		# return self._instance.MoveXYZ(x, y, z, flags)
		raise NotImplemented

