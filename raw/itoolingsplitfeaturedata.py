# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IToolingSplitFeatureData_members.html
class IToolingSplitFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the draft angle for this tooling split feature if an interlock surface exists."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the draft angle for this tooling split feature if an interlock surface exists."""
		self._instance.Angle = value

	@property
	def cavity_surfaces(self):
		"""Gets or sets the cavity surface bodies for this tooling split feature."""
		return self._instance.CavitySurfaces

	@cavity_surfaces.setter
	def cavity_surfaces(self, value):
		"""Gets or sets the cavity surface bodies for this tooling split feature."""
		self._instance.CavitySurfaces = value

	@property
	def core_surfaces(self):
		"""Gets or sets the core surface bodies for this tooling split feature."""
		return self._instance.CoreSurfaces

	@core_surfaces.setter
	def core_surfaces(self, value):
		"""Gets or sets the core surface bodies for this tooling split feature."""
		self._instance.CoreSurfaces = value

	@property
	def depth(self):
		"""Gets or sets the depth of the block in the specified direction for this tooling split feature."""
		return self._instance.Depth

	@depth.setter
	def depth(self, value):
		"""Gets or sets the depth of the block in the specified direction for this tooling split feature."""
		self._instance.Depth = value

	@property
	def interlock_surface(self):
		"""Gets or sets whether to create an interlock surface for this tooling split feature."""
		return self._instance.InterlockSurface

	@interlock_surface.setter
	def interlock_surface(self, value):
		"""Gets or sets whether to create an interlock surface for this tooling split feature."""
		self._instance.InterlockSurface = value

	@property
	def parting_surfaces(self):
		"""Gets or sets the parting surface bodies for this tooling split feature."""
		return self._instance.PartingSurfaces

	@parting_surfaces.setter
	def parting_surfaces(self, value):
		"""Gets or sets the parting surface bodies for this tooling split feature."""
		self._instance.PartingSurfaces = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this tooling split feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this tooling split feature."""
		self._instance.AccessSelections = value

	@property
	def get_cavity_surfaces_count(self):
		"""Gets the number of cavity surface bodies in this tooling split feature."""
		return self._instance.GetCavitySurfacesCount

	@get_cavity_surfaces_count.setter
	def get_cavity_surfaces_count(self, value):
		"""Gets the number of cavity surface bodies in this tooling split feature."""
		self._instance.GetCavitySurfacesCount = value

	@property
	def get_core_surfaces_count(self):
		"""Gets the number of core surface bodies in this tooling split feature."""
		return self._instance.GetCoreSurfacesCount

	@get_core_surfaces_count.setter
	def get_core_surfaces_count(self, value):
		"""Gets the number of core surface bodies in this tooling split feature."""
		self._instance.GetCoreSurfacesCount = value

	@property
	def get_parting_surfaces_count(self):
		"""Gets the number of parting surface bodies in this tooling split feature."""
		return self._instance.GetPartingSurfacesCount

	@get_parting_surfaces_count.setter
	def get_parting_surfaces_count(self, value):
		"""Gets the number of parting surface bodies in this tooling split feature."""
		self._instance.GetPartingSurfacesCount = value

	@property
	def i_get_cavity_surfaces(self):
		"""Gets the cavity surface bodies in this tooling split feature."""
		return self._instance.IGetCavitySurfaces

	@i_get_cavity_surfaces.setter
	def i_get_cavity_surfaces(self, value):
		"""Gets the cavity surface bodies in this tooling split feature."""
		self._instance.IGetCavitySurfaces = value

	@property
	def i_get_core_surfaces(self):
		"""Gets the core surface bodies in this tooling split feature."""
		return self._instance.IGetCoreSurfaces

	@i_get_core_surfaces.setter
	def i_get_core_surfaces(self, value):
		"""Gets the core surface bodies in this tooling split feature."""
		self._instance.IGetCoreSurfaces = value

	@property
	def i_get_parting_surfaces(self):
		"""Gets the parting surface bodies in this tooling split feature."""
		return self._instance.IGetPartingSurfaces

	@i_get_parting_surfaces.setter
	def i_get_parting_surfaces(self, value):
		"""Gets the parting surface bodies in this tooling split feature."""
		self._instance.IGetPartingSurfaces = value

	@property
	def i_set_cavity_surfaces(self):
		"""Sets the cavity surface bodies for this tooling split feature."""
		return self._instance.ISetCavitySurfaces

	@i_set_cavity_surfaces.setter
	def i_set_cavity_surfaces(self, value):
		"""Sets the cavity surface bodies for this tooling split feature."""
		self._instance.ISetCavitySurfaces = value

	@property
	def i_set_core_surfaces(self):
		"""Sets the core surface bodies for this tooling split feature."""
		return self._instance.ISetCoreSurfaces

	@i_set_core_surfaces.setter
	def i_set_core_surfaces(self, value):
		"""Sets the core surface bodies for this tooling split feature."""
		self._instance.ISetCoreSurfaces = value

	@property
	def i_set_parting_surfaces(self):
		"""Sets the parting surface bodies for this tooling split feature."""
		return self._instance.ISetPartingSurfaces

	@i_set_parting_surfaces.setter
	def i_set_parting_surfaces(self, value):
		"""Sets the parting surface bodies for this tooling split feature."""
		self._instance.ISetPartingSurfaces = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this tooling split feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this tooling split feature."""
		self._instance.ReleaseSelectionAccess = value

