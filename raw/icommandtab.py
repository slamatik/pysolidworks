# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTab_members.html
class ICommandTab:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def active(self):
		"""Gets or sets whether this CommandManager tab is active."""
		return self._instance.Active

	@active.setter
	def active(self, value):
		"""Gets or sets whether this CommandManager tab is active."""
		self._instance.Active = value

	@property
	def name(self):
		"""Gets or sets the name of this CommandManager tab."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the name of this CommandManager tab."""
		self._instance.Name = value

	@property
	def visible(self):
		"""Gets or sets whether to show or hide this CommandManager tab."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets whether to show or hide this CommandManager tab."""
		self._instance.Visible = value

	@property
	def add_command_tab_box(self):
		"""Adds a tab box to this CommandManager tab."""
		return self._instance.AddCommandTabBox

	@add_command_tab_box.setter
	def add_command_tab_box(self, value):
		"""Adds a tab box to this CommandManager tab."""
		self._instance.AddCommandTabBox = value

	@property
	def add_separator(self):
		"""Adds a separator to this CommandManager tab."""
		return self._instance.AddSeparator

	@add_separator.setter
	def add_separator(self, value):
		"""Adds a separator to this CommandManager tab."""
		self._instance.AddSeparator = value

	@property
	def command_tab_boxes(self):
		"""Gets the tab boxes on this CommandManager tab."""
		return self._instance.CommandTabBoxes

	@command_tab_boxes.setter
	def command_tab_boxes(self, value):
		"""Gets the tab boxes on this CommandManager tab."""
		self._instance.CommandTabBoxes = value

	@property
	def get_command_tab_box_count(self):
		"""Gets the number of tab boxes on this CommandManager tab."""
		return self._instance.GetCommandTabBoxCount

	@get_command_tab_box_count.setter
	def get_command_tab_box_count(self, value):
		"""Gets the number of tab boxes on this CommandManager tab."""
		self._instance.GetCommandTabBoxCount = value

	@property
	def i_get_command_tab_boxes(self):
		"""Gets the CommandManager tab boxes on this CommandManager tab."""
		return self._instance.IGetCommandTabBoxes

	@i_get_command_tab_boxes.setter
	def i_get_command_tab_boxes(self, value):
		"""Gets the CommandManager tab boxes on this CommandManager tab."""
		self._instance.IGetCommandTabBoxes = value

	@property
	def remove_command_tab_box(self):
		"""Removes the specified tab box and its buttons from this CommandManager tab."""
		return self._instance.RemoveCommandTabBox

	@remove_command_tab_box.setter
	def remove_command_tab_box(self, value):
		"""Removes the specified tab box and its buttons from this CommandManager tab."""
		self._instance.RemoveCommandTabBox = value

