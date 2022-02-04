# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandTabBox_members.html
class ICommandTabBox:
	def __init__(self, parent=None):
		self._instance = parent

	def add_commands(self, command_i_ds, text_display_styles):
		"""
		Adds buttons to this CommandManager tab box.
		:param command_i_ds: Array of command IDs for the buttons (see Remarks)
		:param text_display_styles: Array of the text display styles for the buttons as defined in swCommandTabButtonTextDisplay_e
		"""
		# return self._instance.AddCommands(command_i_ds, text_display_styles)
		raise NotImplemented

	def get_commands(self, command_i_ds, text_display_styles):
		"""
		Gets the buttons' command IDs, text display styles, and number of commands on the CommandManager tab box.
		:param command_i_ds: Array of command IDs for the buttons
		:param text_display_styles: Array of the text display styles for the buttons as defined in swCommandTabButtonTextDisplay_e
		"""
		# return self._instance.GetCommands(command_i_ds, text_display_styles)
		raise NotImplemented

	def i_add_commands(self, command_i_d_count, command_i_ds, text_display_styles):
		"""
		Adds buttons to this CommandManager tab box.
		:param command_i_d_count: Number of buttons to add
		:param command_i_ds: 
in-process, unmanaged C++: Pointer to an array of command IDs (see Remarks) 
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		:param text_display_styles: 
in-process, unmanaged C++: Pointer to an array the text display styles for the buttons as defined in swCommandTabButtonTextDisplay_e
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IAddCommands(command_i_d_count, command_i_ds, text_display_styles)
		raise NotImplemented

	def i_get_commands(self, command_i_ds, text_display_styles):
		"""
		Gets the buttons' Command IDs, text display styles, and number of commands on the CommandManager tab box.
		:param command_i_ds: 
in-process, unmanaged C++: Pointer to an array of command IDs (see Remarks) 
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		:param text_display_styles: 
in-process, unmanaged C++: Pointer to an array the text display styles for the buttons as defined in swCommandTabButtonTextDisplay_e
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method
		"""
		# return self._instance.IGetCommands(command_i_ds, text_display_styles)
		raise NotImplemented

	def i_remove_commands(self, command_i_d_count, command_i_ds):
		"""
		Removes the specified buttons from this CommandManager tab box.
		:param command_i_d_count: Number of buttons to remove from this CommandManager tab box
		:param command_i_ds: 
in-process, unmanaged C++: Pointer to an array of the command IDs for the buttons you want removed from this CommandManager tab box (see Remarks)
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.IRemoveCommands(command_i_d_count, command_i_ds)
		raise NotImplemented

	def remove_commands(self, command_i_ds):
		"""
		Removes the specified buttons from this CommandManager tab box.
		:param command_i_ds: Array of command IDs for the buttons you want removed from this CommandManager tab box (see Remarks)
		"""
		# return self._instance.RemoveCommands(command_i_ds)
		raise NotImplemented

