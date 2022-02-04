# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html
class IImport3DInterconnectData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def axes(self):
		"""Gets or sets whether to import reference axes."""
		return self._instance.Axes

	@axes.setter
	def axes(self, value):
		"""Gets or sets whether to import reference axes."""
		self._instance.Axes = value

	@property
	def custom_properties(self):
		"""Gets or sets whether to import custom properties."""
		return self._instance.CustomProperties

	@custom_properties.setter
	def custom_properties(self, value):
		"""Gets or sets whether to import custom properties."""
		self._instance.CustomProperties = value

	@property
	def ignore_hidden_entities(self):
		"""Gets or sets whether to ignore hidden entities."""
		return self._instance.IgnoreHiddenEntities

	@ignore_hidden_entities.setter
	def ignore_hidden_entities(self, value):
		"""Gets or sets whether to ignore hidden entities."""
		self._instance.IgnoreHiddenEntities = value

	@property
	def material(self):
		"""Gets or sets whether to import material properties."""
		return self._instance.Material

	@material.setter
	def material(self, value):
		"""Gets or sets whether to import material properties."""
		self._instance.Material = value

	@property
	def planes(self):
		"""Gets or sets whether to import reference planes."""
		return self._instance.Planes

	@planes.setter
	def planes(self, value):
		"""Gets or sets whether to import reference planes."""
		self._instance.Planes = value

	@property
	def sketches_and_curves(self):
		"""Gets or sets whether to import unconsumed sketches or curve data as 2D or 3D sketches."""
		return self._instance.SketchesAndCurves

	@sketches_and_curves.setter
	def sketches_and_curves(self, value):
		"""Gets or sets whether to import unconsumed sketches or curve data as 2D or 3D sketches."""
		self._instance.SketchesAndCurves = value

	@property
	def solid_bodies(self):
		"""Gets or sets whether to import solid bodies."""
		return self._instance.SolidBodies

	@solid_bodies.setter
	def solid_bodies(self, value):
		"""Gets or sets whether to import solid bodies."""
		self._instance.SolidBodies = value

	@property
	def surface_bodies(self):
		"""Gets or sets whether to import the data as surface entities."""
		return self._instance.SurfaceBodies

	@surface_bodies.setter
	def surface_bodies(self, value):
		"""Gets or sets whether to import the data as surface entities."""
		self._instance.SurfaceBodies = value

	@property
	def get_authoring_info(self):
		"""Gets the name of the authoring application."""
		return self._instance.GetAuthoringInfo

	@get_authoring_info.setter
	def get_authoring_info(self, value):
		"""Gets the name of the authoring application."""
		self._instance.GetAuthoringInfo = value

	@property
	def get_referenced_file_name(self):
		"""Gets the full path name of the proprietary, non-native CAD file."""
		return self._instance.GetReferencedFileName

	@get_referenced_file_name.setter
	def get_referenced_file_name(self, value):
		"""Gets the full path name of the proprietary, non-native CAD file."""
		self._instance.GetReferencedFileName = value

	@property
	def set_referenced_file_name(self):
		"""Sets the full path name of the proprietary, non-native CAD file."""
		return self._instance.SetReferencedFileName

	@set_referenced_file_name.setter
	def set_referenced_file_name(self, value):
		"""Sets the full path name of the proprietary, non-native CAD file."""
		self._instance.SetReferencedFileName = value

