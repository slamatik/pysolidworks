# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D_members.html
class IView3D:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def annotation_views(self):
		"""Gets or sets the annotation views assigned to this 3D View."""
		return self._instance.AnnotationViews

	@annotation_views.setter
	def annotation_views(self, value):
		"""Gets or sets the annotation views assigned to this 3D View."""
		self._instance.AnnotationViews = value

	@property
	def annotation_views(self):
		"""Gets the annotation views assigned to this 3D View."""
		return self._instance.AnnotationViews2

	@annotation_views.setter
	def annotation_views(self, value):
		"""Gets the annotation views assigned to this 3D View."""
		self._instance.AnnotationViews2 = value

	@property
	def configuration_name(self):
		"""Gets or sets the name of this 3D View's configuration."""
		return self._instance.ConfigurationName

	@configuration_name.setter
	def configuration_name(self, value):
		"""Gets or sets the name of this 3D View's configuration."""
		self._instance.ConfigurationName = value

	@property
	def display_mode(self):
		"""Gets or sets the display mode of this 3D View."""
		return self._instance.DisplayMode

	@display_mode.setter
	def display_mode(self, value):
		"""Gets or sets the display mode of this 3D View."""
		self._instance.DisplayMode = value

	@property
	def display_state(self):
		"""Gets or sets the name this 3D View's display state."""
		return self._instance.DisplayState

	@display_state.setter
	def display_state(self, value):
		"""Gets or sets the name this 3D View's display state."""
		self._instance.DisplayState = value

	@property
	def model_break_view_name(self):
		"""Gets the name of the Model Break View in this 3D View."""
		return self._instance.ModelBreakViewName

	@model_break_view_name.setter
	def model_break_view_name(self, value):
		"""Gets the name of the Model Break View in this 3D View."""
		self._instance.ModelBreakViewName = value

	@property
	def name(self):
		"""Gets or sets the name of this 3D View."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the name of this 3D View."""
		self._instance.Name = value

	@property
	def rotation(self):
		"""Gets or sets the 3D View rotation with respect to the Front view."""
		return self._instance.Rotation

	@rotation.setter
	def rotation(self, value):
		"""Gets or sets the 3D View rotation with respect to the Front view."""
		self._instance.Rotation = value

	@property
	def scale(self):
		"""Gets or sets this 3D View's scale."""
		return self._instance.Scale

	@scale.setter
	def scale(self, value):
		"""Gets or sets this 3D View's scale."""
		self._instance.Scale = value

	@property
	def translation(self):
		"""Gets or sets the translation vector of this 3D View."""
		return self._instance.Translation

	@translation.setter
	def translation(self, value):
		"""Gets or sets the translation vector of this 3D View."""
		self._instance.Translation = value

	@property
	def activate(self):
		"""Activates this 3D View."""
		return self._instance.Activate

	@activate.setter
	def activate(self, value):
		"""Activates this 3D View."""
		self._instance.Activate = value

	@property
	def deactivate(self):
		"""Restores the previously backed-up model state of a 3D View."""
		return self._instance.Deactivate

	@deactivate.setter
	def deactivate(self, value):
		"""Restores the previously backed-up model state of a 3D View."""
		self._instance.Deactivate = value

	@property
	def get_d_view_annotation_text_scale(self):
		"""Gets the annotation text scale for this 3D View."""
		return self._instance.Get3DViewAnnotationTextScale

	@get_d_view_annotation_text_scale.setter
	def get_d_view_annotation_text_scale(self, value):
		"""Gets the annotation text scale for this 3D View."""
		self._instance.Get3DViewAnnotationTextScale = value

