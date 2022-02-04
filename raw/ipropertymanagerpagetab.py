# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageTab_members.html
class IPropertyManagerPageTab:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def caption(self):
		"""Gets or sets the caption for this tab."""
		return self._instance.Caption

	@caption.setter
	def caption(self, value):
		"""Gets or sets the caption for this tab."""
		self._instance.Caption = value

	@property
	def activate(self):
		"""Activates this tab in the PropertyManager page."""
		return self._instance.Activate

	@activate.setter
	def activate(self, value):
		"""Activates this tab in the PropertyManager page."""
		self._instance.Activate = value

	@property
	def add_control(self):
		"""Adds a control to this tab on a PropertyManager page."""
		return self._instance.AddControl2

	@add_control.setter
	def add_control(self, value):
		"""Adds a control to this tab on a PropertyManager page."""
		self._instance.AddControl2 = value

	@property
	def add_group_box(self):
		"""Adds a group box to this tab on a PropertyManager page."""
		return self._instance.AddGroupBox

	@add_group_box.setter
	def add_group_box(self, value):
		"""Adds a group box to this tab on a PropertyManager page."""
		self._instance.AddGroupBox = value

	@property
	def i_add_group_box(self):
		"""Adds a group box to this tab on a PropertyManager page."""
		return self._instance.IAddGroupBox

	@i_add_group_box.setter
	def i_add_group_box(self, value):
		"""Adds a group box to this tab on a PropertyManager page."""
		self._instance.IAddGroupBox = value

