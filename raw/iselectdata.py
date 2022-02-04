# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData_members.html
class ISelectData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def callout(self):
		"""Gets or sets the callout to attach to the selected object."""
		return self._instance.Callout

	@callout.setter
	def callout(self, value):
		"""Gets or sets the callout to attach to the selected object."""
		self._instance.Callout = value

	@property
	def mark(self):
		"""Gets or sets the value to use to mark the selected object."""
		return self._instance.Mark

	@mark.setter
	def mark(self, value):
		"""Gets or sets the value to use to mark the selected object."""
		self._instance.Mark = value

	@property
	def view(self):
		"""Gets or sets the drawing view that contains the selected object."""
		return self._instance.View

	@view.setter
	def view(self, value):
		"""Gets or sets the drawing view that contains the selected object."""
		self._instance.View = value

	@property
	def x(self):
		"""Gets or sets the X coordinate for the selection point."""
		return self._instance.X

	@x.setter
	def x(self, value):
		"""Gets or sets the X coordinate for the selection point."""
		self._instance.X = value

	@property
	def y(self):
		"""Gets or sets the Y coordinate for the selection point."""
		return self._instance.Y

	@y.setter
	def y(self, value):
		"""Gets or sets the Y coordinate for the selection point."""
		self._instance.Y = value

	@property
	def z(self):
		"""Gets or sets the Z coordinate for the selection point."""
		return self._instance.Z

	@z.setter
	def z(self, value):
		"""Gets or sets the Z coordinate for the selection point."""
		self._instance.Z = value

	@property
	def get_cell_range(self):
		"""Gets the specified range of table cells for this selection."""
		return self._instance.GetCellRange

	@get_cell_range.setter
	def get_cell_range(self, value):
		"""Gets the specified range of table cells for this selection."""
		self._instance.GetCellRange = value

	@property
	def set_cell_range(self):
		"""Sets the specified range of table cells for this selection."""
		return self._instance.SetCellRange

	@set_cell_range.setter
	def set_cell_range(self, value):
		"""Sets the specified range of table cells for this selection."""
		self._instance.SetCellRange = value

