# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView_members.html
class ITaskpaneView:
	def __init__(self, parent=None):
		self._instance = parent

	def add_control(self, class_name, lic_key):
		"""
		Adds an ActiveX control to the Task Pane view.
		:param class_name: Name or class ID for the ActiveX control
		:param lic_key: License key for the ActiveX control
		"""
		# return self._instance.AddControl(class_name, lic_key)
		raise NotImplemented

	def add_custom_button(self, image_list, tool_tip):
		"""
		Adds a custom button to the Task Pane.
		:param image_list: Array of strings for the paths for the image files for the custom button (see Remarks)
		:param tool_tip: Array of strings for the paths for the image files for the custom button (see Remarks)
		"""
		# return self._instance.AddCustomButton2(image_list, tool_tip)
		raise NotImplemented

	def add_standard_button(self, bitmap_option, tool_tip):
		"""
		Adds a standard SOLIDWORKS button to the Task Pane.
		:param bitmap_option: Type of standard SOLIDWORKS button as defined in swTaskPaneBitmapsOptions_e
		:param tool_tip: ToolTip for the standard SOLIDWORKS button
		"""
		# return self._instance.AddStandardButton(bitmap_option, tool_tip)
		raise NotImplemented

	def delete_view(self):
		"""Removes the application-level tab from the Task Pane view."""
		# return self._instance.DeleteView
		raise NotImplemented

	def display_window_from_handle(self, window_handle):
		"""
		Adds a .NET control to the Task Pane view.
		:param window_handle: Handle of .NET control
		"""
		# return self._instance.DisplayWindowFromHandle(window_handle)
		raise NotImplemented

	def display_window_from_handlex(self, window_handle):
		"""
		Adds a .NET control to the Task Pane view on 64-bit machines.
		:param window_handle: 64-bit handle of .NET control
		"""
		# return self._instance.DisplayWindowFromHandlex64(window_handle)
		raise NotImplemented

	def get_button_state(self, button_index):
		"""
		Gets whether the Task Pane button is enabled.
		:param button_index: Index of Task Pane button
		"""
		# return self._instance.GetButtonState(button_index)
		raise NotImplemented

	def get_control(self):
		"""Gets the control assigned to the Task Pane view."""
		# return self._instance.GetControl
		raise NotImplemented

	def hide_view(self):
		"""Hides the application-level tab on the Task Pane."""
		# return self._instance.HideView
		raise NotImplemented

	def i_get_control(self):
		"""Gets the control assigned to the Task Pane view."""
		# return self._instance.IGetControl
		raise NotImplemented

	def set_button_state(self, button_index, enable):
		"""
		Sets whether the Task Pane button is enabled.
		:param button_index: Index of Task Pane button
		:param enable: True to enable Task Pane button, false to disable it
		"""
		# return self._instance.SetButtonState(button_index, enable)
		raise NotImplemented

	def show_view(self):
		"""Activates the application-level tab of the Task Pane view and makes the view visible."""
		# return self._instance.ShowView
		raise NotImplemented

