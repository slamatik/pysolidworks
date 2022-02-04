# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInterference_members.html
class IInterference:
	def __init__(self, parent=None):
		self._instance = parent

	def components(self):
		"""Gets the components that interfere with each other."""
		# return self._instance.Components
		raise NotImplemented

	@property
	def ignore(self):
		"""Gets or sets whether to ignore this interference."""
		return self._instance.Ignore

	@ignore.setter
	def ignore(self, value):
		"""Gets or sets whether to ignore this interference."""
		self._instance.Ignore = value

	@property
	def is_fastener(self):
		"""Gets whether this interference includes a fastener or not."""
		return self._instance.IsFastener

	@is_fastener.setter
	def is_fastener(self, value):
		"""Gets whether this interference includes a fastener or not."""
		self._instance.IsFastener = value

	@property
	def is_possible_interference(self):
		"""Gets whether this interference is a possible interference."""
		return self._instance.IsPossibleInterference

	@is_possible_interference.setter
	def is_possible_interference(self, value):
		"""Gets whether this interference is a possible interference."""
		self._instance.IsPossibleInterference = value

	@property
	def volume(self):
		"""Gets the volume of the interference."""
		return self._instance.Volume

	@volume.setter
	def volume(self, value):
		"""Gets the volume of the interference."""
		self._instance.Volume = value

	@property
	def get_component_count(self):
		"""Gets the number of components interfering with each other."""
		return self._instance.GetComponentCount

	@get_component_count.setter
	def get_component_count(self, value):
		"""Gets the number of components interfering with each other."""
		self._instance.GetComponentCount = value

	@property
	def get_interference_body(self):
		"""Gets the interfering volume."""
		return self._instance.GetInterferenceBody

	@get_interference_body.setter
	def get_interference_body(self, value):
		"""Gets the interfering volume."""
		self._instance.GetInterferenceBody = value

	@property
	def i_get_components(self):
		"""Gets the components that interfere with each other."""
		return self._instance.IGetComponents

	@i_get_components.setter
	def i_get_components(self, value):
		"""Gets the components that interfere with each other."""
		self._instance.IGetComponents = value

