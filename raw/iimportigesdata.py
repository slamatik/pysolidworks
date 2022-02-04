# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImportIgesData_members.html
class IImportIgesData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def curves_as_sketches(self):
		"""Gets or sets whether the curves are imported as sketches or reference curve features."""
		return self._instance.CurvesAsSketches

	@curves_as_sketches.setter
	def curves_as_sketches(self, value):
		"""Gets or sets whether the curves are imported as sketches or reference curve features."""
		self._instance.CurvesAsSketches = value

	@property
	def include_all_levels(self):
		"""Gets whether all levels (layers) are imported."""
		return self._instance.IncludeAllLevels

	@include_all_levels.setter
	def include_all_levels(self, value):
		"""Gets whether all levels (layers) are imported."""
		self._instance.IncludeAllLevels = value

	@property
	def include_curves(self):
		"""Gets or sets whether or not to import curves."""
		return self._instance.IncludeCurves

	@include_curves.setter
	def include_curves(self, value):
		"""Gets or sets whether or not to import curves."""
		self._instance.IncludeCurves = value

	@property
	def include_only_levels(self):
		"""Gets the levels (layers) to import."""
		return self._instance.IncludeOnlyLevels

	@include_only_levels.setter
	def include_only_levels(self, value):
		"""Gets the levels (layers) to import."""
		self._instance.IncludeOnlyLevels = value

	@property
	def include_surfaces(self):
		"""Gets or sets whether to import surfaces."""
		return self._instance.IncludeSurfaces

	@include_surfaces.setter
	def include_surfaces(self, value):
		"""Gets or sets whether to import surfaces."""
		self._instance.IncludeSurfaces = value

	@property
	def process_by_level(self):
		"""Gets or sets whether to process surfaces together."""
		return self._instance.ProcessByLevel

	@process_by_level.setter
	def process_by_level(self, value):
		"""Gets or sets whether to process surfaces together."""
		self._instance.ProcessByLevel = value

	@property
	def set_levels(self):
		"""Sets the levels-related information for importing and IGES file."""
		return self._instance.SetLevels

	@set_levels.setter
	def set_levels(self, value):
		"""Sets the levels-related information for importing and IGES file."""
		self._instance.SetLevels = value

