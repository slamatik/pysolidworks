# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwScene_members.html
class ISwScene:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def accurate_env_lighting(self):
		"""Gets or sets whether to use the accurate environment lighting calculations from the high dynamic range imaging (HDRI) scene environment."""
		return self._instance.AccurateEnvLighting

	@accurate_env_lighting.setter
	def accurate_env_lighting(self, value):
		"""Gets or sets whether to use the accurate environment lighting calculations from the high dynamic range imaging (HDRI) scene environment."""
		self._instance.AccurateEnvLighting = value

	@property
	def aspect_ratio(self):
		"""Gets the aspect ratio of the scene floor."""
		return self._instance.AspectRatio

	@aspect_ratio.setter
	def aspect_ratio(self, value):
		"""Gets the aspect ratio of the scene floor."""
		self._instance.AspectRatio = value

	@property
	def background_bottom_gradient_color(self):
		"""Gets or sets the bottom color of the graduated range of background colors of this scene."""
		return self._instance.BackgroundBottomGradientColor

	@background_bottom_gradient_color.setter
	def background_bottom_gradient_color(self, value):
		"""Gets or sets the bottom color of the graduated range of background colors of this scene."""
		self._instance.BackgroundBottomGradientColor = value

	@property
	def background_brightness(self):
		"""Gets or sets the brightness of the background."""
		return self._instance.BackgroundBrightness

	@background_brightness.setter
	def background_brightness(self, value):
		"""Gets or sets the brightness of the background."""
		self._instance.BackgroundBrightness = value

	@property
	def background_env_image(self):
		"""Gets or sets the environment image of this scene."""
		return self._instance.BackgroundEnvImage

	@background_env_image.setter
	def background_env_image(self, value):
		"""Gets or sets the environment image of this scene."""
		self._instance.BackgroundEnvImage = value

	@property
	def background_image(self):
		"""Gets or sets the background image for this scene."""
		return self._instance.BackgroundImage

	@background_image.setter
	def background_image(self, value):
		"""Gets or sets the background image for this scene."""
		self._instance.BackgroundImage = value

	@property
	def background_top_gradient_color(self):
		"""Gets or sets the background color of this scene."""
		return self._instance.BackgroundTopGradientColor

	@background_top_gradient_color.setter
	def background_top_gradient_color(self, value):
		"""Gets or sets the background color of this scene."""
		self._instance.BackgroundTopGradientColor = value

	@property
	def background_type(self):
		"""Gets or sets the type of background for this scene."""
		return self._instance.BackgroundType

	@background_type.setter
	def background_type(self, value):
		"""Gets or sets the type of background for this scene."""
		self._instance.BackgroundType = value

	@property
	def environment_rotation(self):
		"""Gets or sets the rotation of the environment image of this scene."""
		return self._instance.EnvironmentRotation

	@environment_rotation.setter
	def environment_rotation(self, value):
		"""Gets or sets the rotation of the environment image of this scene."""
		self._instance.EnvironmentRotation = value

	@property
	def environment_size(self):
		"""Gets or sets the size of the high dynamic range imaging (HDRI) scene sphere that surrounds the model."""
		return self._instance.EnvironmentSize

	@environment_size.setter
	def environment_size(self, value):
		"""Gets or sets the size of the high dynamic range imaging (HDRI) scene sphere that surrounds the model."""
		self._instance.EnvironmentSize = value

	@property
	def fit_to_s_w_window(self):
		"""Gets or sets whether to stretch an image to fit the SOLIDWORKS window."""
		return self._instance.FitToSWWindow

	@fit_to_s_w_window.setter
	def fit_to_s_w_window(self, value):
		"""Gets or sets whether to stretch an image to fit the SOLIDWORKS window."""
		self._instance.FitToSWWindow = value

	@property
	def fixed_aspect_ratio(self):
		"""Gets or sets whether to fix the aspect ratio of the scene floor."""
		return self._instance.FixedAspectRatio

	@fixed_aspect_ratio.setter
	def fixed_aspect_ratio(self, value):
		"""Gets or sets whether to fix the aspect ratio of the scene floor."""
		self._instance.FixedAspectRatio = value

	@property
	def flatten_floor(self):
		"""Get or sets whether to flatten the floor of a spherical environment to improve the look of models that naturally rest on flat floors."""
		return self._instance.FlattenFloor

	@flatten_floor.setter
	def flatten_floor(self, value):
		"""Get or sets whether to flatten the floor of a spherical environment to improve the look of models that naturally rest on flat floors."""
		self._instance.FlattenFloor = value

	@property
	def floor_alignment(self):
		"""Gets or sets the plane with which to align the scene floor."""
		return self._instance.FloorAlignment

	@floor_alignment.setter
	def floor_alignment(self, value):
		"""Gets or sets the plane with which to align the scene floor."""
		self._instance.FloorAlignment = value

	@property
	def floor_auto_size(self):
		"""Gets or sets whether to resize the scene floor based on the model bounding box."""
		return self._instance.FloorAutoSize

	@floor_auto_size.setter
	def floor_auto_size(self, value):
		"""Gets or sets whether to resize the scene floor based on the model bounding box."""
		self._instance.FloorAutoSize = value

	@property
	def floor_depth(self):
		"""Gets or sets the depth of the scene floor."""
		return self._instance.FloorDepth

	@floor_depth.setter
	def floor_depth(self, value):
		"""Gets or sets the depth of the scene floor."""
		self._instance.FloorDepth = value

	@property
	def floor_direction(self):
		"""Gets or sets whether to flip the direction of the floor of this scene."""
		return self._instance.FloorDirection

	@floor_direction.setter
	def floor_direction(self, value):
		"""Gets or sets whether to flip the direction of the floor of this scene."""
		self._instance.FloorDirection = value

	@property
	def floor_offset(self):
		"""Gets or sets the height of the model above or below the floor of this scene."""
		return self._instance.FloorOffset

	@floor_offset.setter
	def floor_offset(self, value):
		"""Gets or sets the height of the model above or below the floor of this scene."""
		self._instance.FloorOffset = value

	@property
	def floor_offset_direction(self):
		"""Gets or sets whether to swap the positions of the scene floor and the model."""
		return self._instance.FloorOffsetDirection

	@floor_offset_direction.setter
	def floor_offset_direction(self, value):
		"""Gets or sets whether to swap the positions of the scene floor and the model."""
		self._instance.FloorOffsetDirection = value

	@property
	def floor_reflections(self):
		"""Gets or sets whether to show reflections of the model on the scene floor."""
		return self._instance.FloorReflections

	@floor_reflections.setter
	def floor_reflections(self, value):
		"""Gets or sets whether to show reflections of the model on the scene floor."""
		self._instance.FloorReflections = value

	@property
	def floor_rotation(self):
		"""Gets or sets the rotation of the scene floor relative to the environment of this scene."""
		return self._instance.FloorRotation

	@floor_rotation.setter
	def floor_rotation(self, value):
		"""Gets or sets the rotation of the scene floor relative to the environment of this scene."""
		self._instance.FloorRotation = value

	@property
	def floor_selection(self):
		"""Gets or sets the floor appearance of this scene."""
		return self._instance.FloorSelection

	@floor_selection.setter
	def floor_selection(self, value):
		"""Gets or sets the floor appearance of this scene."""
		self._instance.FloorSelection = value

	@property
	def floor_shadows(self):
		"""Gets or sets whether to show shadows cast by the model on the scene floor."""
		return self._instance.FloorShadows

	@floor_shadows.setter
	def floor_shadows(self, value):
		"""Gets or sets whether to show shadows cast by the model on the scene floor."""
		self._instance.FloorShadows = value

	@property
	def floor_width(self):
		"""Gets or sets the width of the scene floor."""
		return self._instance.FloorWidth

	@floor_width.setter
	def floor_width(self, value):
		"""Gets or sets the width of the scene floor."""
		self._instance.FloorWidth = value

	@property
	def horizon_height(self):
		"""Gets or sets the height on the high dynamic range imaging (HDRI) scene sphere where the scene floor starts to flatten."""
		return self._instance.HorizonHeight

	@horizon_height.setter
	def horizon_height(self, value):
		"""Gets or sets the height on the high dynamic range imaging (HDRI) scene sphere where the scene floor starts to flatten."""
		self._instance.HorizonHeight = value

	@property
	def keep_background(self):
		"""Gets or sets whether to retain the background when replacing the scene."""
		return self._instance.KeepBackground

	@keep_background.setter
	def keep_background(self, value):
		"""Gets or sets whether to retain the background when replacing the scene."""
		self._instance.KeepBackground = value

	@property
	def rendering_brightness(self):
		"""Gets or sets the brightness contributed by the high dynamic range imaging (HDRI) environment."""
		return self._instance.RenderingBrightness

	@rendering_brightness.setter
	def rendering_brightness(self, value):
		"""Gets or sets the brightness contributed by the high dynamic range imaging (HDRI) environment."""
		self._instance.RenderingBrightness = value

	@property
	def scene_reflectivity(self):
		"""Gets or sets the amount of reflectivity provided by the high dynamic range imaging (HDRI) environment."""
		return self._instance.SceneReflectivity

	@scene_reflectivity.setter
	def scene_reflectivity(self, value):
		"""Gets or sets the amount of reflectivity provided by the high dynamic range imaging (HDRI) environment."""
		self._instance.SceneReflectivity = value

	@property
	def delete_floor_appearance(self):
		"""Deletes the floor appearance of this scene."""
		return self._instance.DeleteFloorAppearance

	@delete_floor_appearance.setter
	def delete_floor_appearance(self, value):
		"""Deletes the floor appearance of this scene."""
		self._instance.DeleteFloorAppearance = value

	@property
	def get_floor_normal(self):
		"""Gets the normal to the floor of this scene."""
		return self._instance.GetFloorNormal

	@get_floor_normal.setter
	def get_floor_normal(self, value):
		"""Gets the normal to the floor of this scene."""
		self._instance.GetFloorNormal = value

	@property
	def get_p_s_file_name(self):
		"""Gets the scene file for this scene."""
		return self._instance.GetP2SFileName

	@get_p_s_file_name.setter
	def get_p_s_file_name(self, value):
		"""Gets the scene file for this scene."""
		self._instance.GetP2SFileName = value

	@property
	def modify(self):
		"""Modifies and saves this scene."""
		return self._instance.Modify

	@modify.setter
	def modify(self, value):
		"""Modifies and saves this scene."""
		self._instance.Modify = value

	@property
	def offset_to_geometry(self):
		"""Resets the floor offset."""
		return self._instance.OffsetToGeometry

	@offset_to_geometry.setter
	def offset_to_geometry(self, value):
		"""Resets the floor offset."""
		self._instance.OffsetToGeometry = value

