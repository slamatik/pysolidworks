# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonStack_members.html
class IBalloonStack:
	def __init__(self, parent=None):
		self._instance = parent

	def count(self):
		"""Gets the number of stacked notes in this balloon stack, excluding the master balloon."""
		# return self._instance.Count
		raise NotImplemented

	@property
	def direction(self):
		"""Gets or sets the direction of this balloon stack."""
		return self._instance.Direction

	@direction.setter
	def direction(self, value):
		"""Gets or sets the direction of this balloon stack."""
		self._instance.Direction = value

	@property
	def length(self):
		"""Gets or sets the number of notes that can be stacked before another row is started."""
		return self._instance.Length

	@length.setter
	def length(self, value):
		"""Gets or sets the number of notes that can be stacked before another row is started."""
		self._instance.Length = value

	@property
	def master(self):
		"""Gets the master note in this balloon stack."""
		return self._instance.Master

	@master.setter
	def master(self, value):
		"""Gets the master note in this balloon stack."""
		self._instance.Master = value

	@property
	def stack(self):
		"""Gets the stacked notes in this balloon stack, excluding the master balloon."""
		return self._instance.Stack

	@stack.setter
	def stack(self, value):
		"""Gets the stacked notes in this balloon stack, excluding the master balloon."""
		self._instance.Stack = value

	@property
	def add_to(self):
		"""Adds a balloon note to this balloon stack."""
		return self._instance.AddTo

	@add_to.setter
	def add_to(self, value):
		"""Adds a balloon note to this balloon stack."""
		self._instance.AddTo = value

	@property
	def i_get_stack(self):
		"""Gets the stacked notes in this balloon stack, excluding the master balloon."""
		return self._instance.IGetStack

	@i_get_stack.setter
	def i_get_stack(self, value):
		"""Gets the stacked notes in this balloon stack, excluding the master balloon."""
		self._instance.IGetStack = value

