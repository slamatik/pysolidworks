# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRenderer_members.html
class IRayTraceRenderer:
	def __init__(self, parent=None):
		self._instance = parent

	def ray_trace_renderer_options(self):
		"""Gets a ray-trace rendering engine's options."""
		# return self._instance.RayTraceRendererOptions
		raise NotImplemented

	def abort_final_render(self):
		"""Aborts the final render window."""
		# return self._instance.AbortFinalRender
		raise NotImplemented

	def close_final_render_window(self):
		"""Closes the final render window, but leaves the preview window open."""
		# return self._instance.CloseFinalRenderWindow
		raise NotImplemented

	def close_ray_trace_render(self):
		"""Closes both the preview and final render windows."""
		# return self._instance.CloseRayTraceRender
		raise NotImplemented

	def display_preview_window(self):
		"""Displays the preview render window."""
		# return self._instance.DisplayPreviewWindow
		raise NotImplemented

	def invoke_final_render(self):
		"""Invokes the final render window."""
		# return self._instance.InvokeFinalRender
		raise NotImplemented

	def render_to_file(self, image_file_name, width, height):
		"""
		Saves the current view of the rendered model as an image to the specified file.
		:param image_file_name: File path and name (see Remarks)
		:param width: Width of image in pixels (see Remarks)
		:param height: Height of image in pixels (see Remarks)
		"""
		# return self._instance.RenderToFile(image_file_name, width, height)
		raise NotImplemented

