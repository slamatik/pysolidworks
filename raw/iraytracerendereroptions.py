# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRayTraceRendererOptions_members.html
class IRayTraceRendererOptions:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def alpha_output(self):
		"""Gets or sets whether to render the model as alpha or final color output."""
		return self._instance.AlphaOutput

	@alpha_output.setter
	def alpha_output(self, value):
		"""Gets or sets whether to render the model as alpha or final color output."""
		self._instance.AlphaOutput = value

	@property
	def bloom_enabled(self):
		"""Gets or sets whether to enable bloom effect."""
		return self._instance.BloomEnabled

	@bloom_enabled.setter
	def bloom_enabled(self, value):
		"""Gets or sets whether to enable bloom effect."""
		self._instance.BloomEnabled = value

	@property
	def bloom_radius(self):
		"""Gets or sets the the distance bloom radiates from source."""
		return self._instance.BloomRadius

	@bloom_radius.setter
	def bloom_radius(self, value):
		"""Gets or sets the the distance bloom radiates from source."""
		self._instance.BloomRadius = value

	@property
	def bloom_threshold(self):
		"""Gets or sets the level of brightness or emissiveness to which bloom effect is applied."""
		return self._instance.BloomThreshold

	@bloom_threshold.setter
	def bloom_threshold(self, value):
		"""Gets or sets the level of brightness or emissiveness to which bloom effect is applied."""
		self._instance.BloomThreshold = value

	@property
	def caustic_amount(self):
		"""Gets or sets the maximum number of photons fired, which controls the amount of visible caustics."""
		return self._instance.CausticAmount

	@caustic_amount.setter
	def caustic_amount(self, value):
		"""Gets or sets the maximum number of photons fired, which controls the amount of visible caustics."""
		self._instance.CausticAmount = value

	@property
	def caustic_quality(self):
		"""Gets or sets the number of photons sampled at each pixel, which controls the quality of the caustics."""
		return self._instance.CausticQuality

	@caustic_quality.setter
	def caustic_quality(self, value):
		"""Gets or sets the number of photons sampled at each pixel, which controls the quality of the caustics."""
		self._instance.CausticQuality = value

	@property
	def client_workload(self):
		"""Gets or sets how many buckets (sections of rendering) are sent to each client processor."""
		return self._instance.ClientWorkload

	@client_workload.setter
	def client_workload(self, value):
		"""Gets or sets how many buckets (sections of rendering) are sent to each client processor."""
		self._instance.ClientWorkload = value

	@property
	def contour_cartoon_rendering_enabled(self):
		"""Gets or sets whether to enable contour/cartoon rendering."""
		return self._instance.ContourCartoonRenderingEnabled

	@contour_cartoon_rendering_enabled.setter
	def contour_cartoon_rendering_enabled(self, value):
		"""Gets or sets whether to enable contour/cartoon rendering."""
		self._instance.ContourCartoonRenderingEnabled = value

	@property
	def contour_line_color(self):
		"""Gets or sets the color of the contour lines."""
		return self._instance.ContourLineColor

	@contour_line_color.setter
	def contour_line_color(self, value):
		"""Gets or sets the color of the contour lines."""
		self._instance.ContourLineColor = value

	@property
	def contour_line_thickness(self):
		"""Gets or sets the thickness of contour lines."""
		return self._instance.ContourLineThickness

	@contour_line_thickness.setter
	def contour_line_thickness(self, value):
		"""Gets or sets the thickness of contour lines."""
		self._instance.ContourLineThickness = value

	@property
	def custom_render_settings(self):
		"""Gets or sets whether to enable custom render settings."""
		return self._instance.CustomRenderSettings

	@custom_render_settings.setter
	def custom_render_settings(self, value):
		"""Gets or sets whether to enable custom render settings."""
		self._instance.CustomRenderSettings = value

	@property
	def default_image_path(self):
		"""Gets or sets the default path to which to save the image."""
		return self._instance.DefaultImagePath

	@default_image_path.setter
	def default_image_path(self, value):
		"""Gets or sets the default path to which to save the image."""
		self._instance.DefaultImagePath = value

	@property
	def direct_caustics(self):
		"""Gets or sets whether to enable direct caustics in the final render."""
		return self._instance.DirectCaustics

	@direct_caustics.setter
	def direct_caustics(self, value):
		"""Gets or sets whether to enable direct caustics in the final render."""
		self._instance.DirectCaustics = value

	@property
	def final_render_quality(self):
		"""Gets or sets quality of the final render."""
		return self._instance.FinalRenderQuality

	@final_render_quality.setter
	def final_render_quality(self, value):
		"""Gets or sets quality of the final render."""
		self._instance.FinalRenderQuality = value

	@property
	def gamma(self):
		"""Gets or sets the value for midtones of the rendered image while preserving the extreme whites and blacks."""
		return self._instance.Gamma

	@gamma.setter
	def gamma(self, value):
		"""Gets or sets the value for midtones of the rendered image while preserving the extreme whites and blacks."""
		self._instance.Gamma = value

	@property
	def has_cartoon_edges(self):
		"""Gets or sets whether to render with cartoon edges."""
		return self._instance.HasCartoonEdges

	@has_cartoon_edges.setter
	def has_cartoon_edges(self, value):
		"""Gets or sets whether to render with cartoon edges."""
		self._instance.HasCartoonEdges = value

	@property
	def has_cartoon_shading(self):
		"""Gets or sets whether to render with cartoon shading."""
		return self._instance.HasCartoonShading

	@has_cartoon_shading.setter
	def has_cartoon_shading(self, value):
		"""Gets or sets whether to render with cartoon shading."""
		self._instance.HasCartoonShading = value

	@property
	def image_format(self):
		"""Gets or sets the format of the image."""
		return self._instance.ImageFormat

	@image_format.setter
	def image_format(self, value):
		"""Gets or sets the format of the image."""
		self._instance.ImageFormat = value

	@property
	def image_height(self):
		"""Gets or sets the height of the image."""
		return self._instance.ImageHeight

	@image_height.setter
	def image_height(self, value):
		"""Gets or sets the height of the image."""
		self._instance.ImageHeight = value

	@property
	def image_width(self):
		"""Gets or sets the width of the image."""
		return self._instance.ImageWidth

	@image_width.setter
	def image_width(self, value):
		"""Gets or sets the width of the image."""
		self._instance.ImageWidth = value

	@property
	def include_annotations_in_rendering(self):
		"""Gets or sets whether to include annotations and dimensions visible in the model when rendering to a file."""
		return self._instance.IncludeAnnotationsInRendering

	@include_annotations_in_rendering.setter
	def include_annotations_in_rendering(self, value):
		"""Gets or sets whether to include annotations and dimensions visible in the model when rendering to a file."""
		self._instance.IncludeAnnotationsInRendering = value

	@property
	def network_rendering(self):
		"""Gets or sets whether to enable network rendering."""
		return self._instance.NetworkRendering

	@network_rendering.setter
	def network_rendering(self, value):
		"""Gets or sets whether to enable network rendering."""
		self._instance.NetworkRendering = value

	@property
	def network_shared_directory(self):
		"""Gets or sets the name of the shared network directory for network renders."""
		return self._instance.NetworkSharedDirectory

	@network_shared_directory.setter
	def network_shared_directory(self, value):
		"""Gets or sets the name of the shared network directory for network renders."""
		self._instance.NetworkSharedDirectory = value

	@property
	def number_of_reflections(self):
		"""Gets or sets the number of reflections in the final render."""
		return self._instance.NumberOfReflections

	@number_of_reflections.setter
	def number_of_reflections(self, value):
		"""Gets or sets the number of reflections in the final render."""
		self._instance.NumberOfReflections = value

	@property
	def number_of_refractions(self):
		"""Gets or sets the number of refractions in the final render."""
		return self._instance.NumberOfRefractions

	@number_of_refractions.setter
	def number_of_refractions(self, value):
		"""Gets or sets the number of refractions in the final render."""
		self._instance.NumberOfRefractions = value

	@property
	def offloaded_rendering(self):
		"""Gets or sets whether to offload rendering to other networked machines."""
		return self._instance.OffloadedRendering

	@offloaded_rendering.setter
	def offloaded_rendering(self, value):
		"""Gets or sets whether to offload rendering to other networked machines."""
		self._instance.OffloadedRendering = value

	@property
	def output_ambient_occlusion(self):
		"""Gets or sets whether to render with ambient occlusion."""
		return self._instance.OutputAmbientOcclusion

	@output_ambient_occlusion.setter
	def output_ambient_occlusion(self, value):
		"""Gets or sets whether to render with ambient occlusion."""
		self._instance.OutputAmbientOcclusion = value

	@property
	def preview_render_quality(self):
		"""Gets or sets the quality of the rendering in the preview window."""
		return self._instance.PreviewRenderQuality

	@preview_render_quality.setter
	def preview_render_quality(self, value):
		"""Gets or sets the quality of the rendering in the preview window."""
		self._instance.PreviewRenderQuality = value

	@property
	def render_annotations_to_separate_image(self):
		"""Gets or sets whether to render annotations and dimensions visible in the model to a separate image file."""
		return self._instance.RenderAnnotationsToSeparateImage

	@render_annotations_to_separate_image.setter
	def render_annotations_to_separate_image(self, value):
		"""Gets or sets whether to render annotations and dimensions visible in the model to a separate image file."""
		self._instance.RenderAnnotationsToSeparateImage = value

	@property
	def render_type(self):
		"""Gets or sets whether to render with contour or cartoon lines."""
		return self._instance.RenderType

	@render_type.setter
	def render_type(self, value):
		"""Gets or sets whether to render with contour or cartoon lines."""
		self._instance.RenderType = value

	@property
	def send_data_for_network_job(self):
		"""Gets or sets whether to send rendering data over the network."""
		return self._instance.SendDataForNetworkJob

	@send_data_for_network_job.setter
	def send_data_for_network_job(self, value):
		"""Gets or sets whether to send rendering data over the network."""
		self._instance.SendDataForNetworkJob = value

	@property
	def shaded_contour(self):
		"""Gets or sets whether to shade the contours lines."""
		return self._instance.ShadedContour

	@shaded_contour.setter
	def shaded_contour(self, value):
		"""Gets or sets whether to shade the contours lines."""
		self._instance.ShadedContour = value

	@property
	def use_scene_background_image_aspect_ratio(self):
		"""Gets or sets whether to use the aspect ratio of the scene's background image for PhotoView preview and final renders."""
		return self._instance.UseSceneBackgroundImageAspectRatio

	@use_scene_background_image_aspect_ratio.setter
	def use_scene_background_image_aspect_ratio(self, value):
		"""Gets or sets whether to use the aspect ratio of the scene's background image for PhotoView preview and final renders."""
		self._instance.UseSceneBackgroundImageAspectRatio = value

	@property
	def use_solid_works_view_aspect_ratio(self):
		"""Gets or sets whether to use the aspect ratio of the SOLIDWORKS view for PhotoView preview and final renders."""
		return self._instance.UseSolidWorksViewAspectRatio

	@use_solid_works_view_aspect_ratio.setter
	def use_solid_works_view_aspect_ratio(self, value):
		"""Gets or sets whether to use the aspect ratio of the SOLIDWORKS view for PhotoView preview and final renders."""
		self._instance.UseSolidWorksViewAspectRatio = value

	@property
	def update_graphics(self):
		"""Updates the graphics area."""
		return self._instance.UpdateGraphics

	@update_graphics.setter
	def update_graphics(self, value):
		"""Updates the graphics area."""
		self._instance.UpdateGraphics = value

