# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IManipulator_members.html
class IManipulator:
	def __init__(self, parent=None):
		self._instance = parent

	def name(self):
		"""Gets and sets the name of a manipulator."""
		# return self._instance.Name
		raise NotImplemented

	@property
	def options(self):
		"""Gets or sets whether the manipulator is deleted when a component in an assembly is modified or deleted."""
		return self._instance.Options

	@options.setter
	def options(self, value):
		"""Gets or sets whether the manipulator is deleted when a component in an assembly is modified or deleted."""
		self._instance.Options = value

	@property
	def selectable(self):
		"""Gets or sets whether the manipulator can be selected in a PropertyManager page's selection box."""
		return self._instance.Selectable

	@selectable.setter
	def selectable(self, value):
		"""Gets or sets whether the manipulator can be selected in a PropertyManager page's selection box."""
		self._instance.Selectable = value

	@property
	def visible(self):
		"""Gets or sets whether the manipulator is visible in this SOLIDWORKS part or assembly document."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets whether the manipulator is visible in this SOLIDWORKS part or assembly document."""
		self._instance.Visible = value

	@property
	def get_specific_manipulator(self):
		"""Gets the manipulator for this SOLIDWORKS part or assembly document."""
		return self._instance.GetSpecificManipulator

	@get_specific_manipulator.setter
	def get_specific_manipulator(self, value):
		"""Gets the manipulator for this SOLIDWORKS part or assembly document."""
		self._instance.GetSpecificManipulator = value

	@property
	def remove(self):
		"""Removes the manipulator from this SOLIDWORKS part or assembly document."""
		return self._instance.Remove

	@remove.setter
	def remove(self, value):
		"""Removes the manipulator from this SOLIDWORKS part or assembly document."""
		self._instance.Remove = value

	@property
	def select(self):
		"""Select a manipulator."""
		return self._instance.Select

	@select.setter
	def select(self, value):
		"""Select a manipulator."""
		self._instance.Select = value

	@property
	def show(self):
		"""Shows the manipulator in this SOLIDWORKS part or assembly document."""
		return self._instance.Show

	@show.setter
	def show(self, value):
		"""Shows the manipulator in this SOLIDWORKS part or assembly document."""
		self._instance.Show = value

