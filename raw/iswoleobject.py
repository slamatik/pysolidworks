# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwOLEObject_members.html
class ISwOLEObject:
	def __init__(self, parent=None):
		self._instance = parent

	def aspect(self):
		"""Gets the viewing aspect for this OLE object."""
		# return self._instance.Aspect
		raise NotImplemented

	@property
	def boundaries(self):
		"""Gets or sets the boundaries for this OLE object."""
		return self._instance.Boundaries

	@boundaries.setter
	def boundaries(self, value):
		"""Gets or sets the boundaries for this OLE object."""
		self._instance.Boundaries = value

	@property
	def buffer(self):
		"""Gets the data for this OLE object."""
		return self._instance.Buffer

	@buffer.setter
	def buffer(self, value):
		"""Gets the data for this OLE object."""
		self._instance.Buffer = value

	@property
	def buffer_size(self):
		"""Gets the size of the OLE object data."""
		return self._instance.BufferSize

	@buffer_size.setter
	def buffer_size(self, value):
		"""Gets the size of the OLE object data."""
		self._instance.BufferSize = value

	@property
	def clsid(self):
		"""Gets the class ID of this OLE object."""
		return self._instance.Clsid

	@clsid.setter
	def clsid(self, value):
		"""Gets the class ID of this OLE object."""
		self._instance.Clsid = value

	@property
	def file_name(self):
		"""Gets the path and name of the external file to which this OLE object is linked."""
		return self._instance.FileName

	@file_name.setter
	def file_name(self, value):
		"""Gets the path and name of the external file to which this OLE object is linked."""
		self._instance.FileName = value

	@property
	def is_linked(self):
		"""Gets whether the OLE objects are linked to external files or not."""
		return self._instance.IsLinked

	@is_linked.setter
	def is_linked(self, value):
		"""Gets whether the OLE objects are linked to external files or not."""
		self._instance.IsLinked = value

	@property
	def i_get_boundaries(self):
		"""Gets the boundaries for this OLE object."""
		return self._instance.IGetBoundaries

	@i_get_boundaries.setter
	def i_get_boundaries(self, value):
		"""Gets the boundaries for this OLE object."""
		self._instance.IGetBoundaries = value

	@property
	def i_get_buffer(self):
		"""Gets the data for this OLE object."""
		return self._instance.IGetBuffer

	@i_get_buffer.setter
	def i_get_buffer(self, value):
		"""Gets the data for this OLE object."""
		self._instance.IGetBuffer = value

	@property
	def i_set_boundaries(self):
		"""Sets the boundaries of this OLE object."""
		return self._instance.ISetBoundaries

	@i_set_boundaries.setter
	def i_set_boundaries(self, value):
		"""Sets the boundaries of this OLE object."""
		self._instance.ISetBoundaries = value

	@property
	def refresh(self):
		"""Refreshes the data (i.e., reloads the data from the external file in case it was changed by another application)."""
		return self._instance.Refresh

	@refresh.setter
	def refresh(self, value):
		"""Refreshes the data (i.e., reloads the data from the external file in case it was changed by another application)."""
		self._instance.Refresh = value

	@property
	def select(self):
		"""Selects an OLE object."""
		return self._instance.Select

	@select.setter
	def select(self, value):
		"""Selects an OLE object."""
		self._instance.Select = value

	@property
	def set_active(self):
		"""Activates or deactivates the OLE object."""
		return self._instance.SetActive

	@set_active.setter
	def set_active(self, value):
		"""Activates or deactivates the OLE object."""
		self._instance.SetActive = value

