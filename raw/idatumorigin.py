# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumOrigin_members.html
class IDatumOrigin:
	def __init__(self, parent=None):
		self._instance = parent

	def table(self):
		"""Gets the hole table associated with this datum origin."""
		# return self._instance.Table
		raise NotImplemented

	@property
	def x_label(self):
		"""Gets or sets the label for the X axis for this datum origin."""
		return self._instance.XLabel

	@x_label.setter
	def x_label(self, value):
		"""Gets or sets the label for the X axis for this datum origin."""
		self._instance.XLabel = value

	@property
	def y_label(self):
		"""Gets or sets the label for the Y axis for this datum origin."""
		return self._instance.YLabel

	@y_label.setter
	def y_label(self, value):
		"""Gets or sets the label for the Y axis for this datum origin."""
		self._instance.YLabel = value

	@property
	def get_annotation(self):
		"""Gets the IAnnotation object for this datum origin."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the IAnnotation object for this datum origin."""
		self._instance.GetAnnotation = value

	@property
	def get_axis_points(self):
		"""Gets the points that define the geometry of this datum origin."""
		return self._instance.GetAxisPoints2

	@get_axis_points.setter
	def get_axis_points(self, value):
		"""Gets the points that define the geometry of this datum origin."""
		self._instance.GetAxisPoints2 = value

	@property
	def get_next(self):
		"""Gets the next datum origin in the view."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next datum origin in the view."""
		self._instance.GetNext = value

	@property
	def i_get_axis_points(self):
		"""Gets the points that define the geometry of this datum origin."""
		return self._instance.IGetAxisPoints2

	@i_get_axis_points.setter
	def i_get_axis_points(self, value):
		"""Gets the points that define the geometry of this datum origin."""
		self._instance.IGetAxisPoints2 = value

	@property
	def i_set_axis_points(self):
		"""Sets the points that define the geometry of this datum origin."""
		return self._instance.ISetAxisPoints

	@i_set_axis_points.setter
	def i_set_axis_points(self, value):
		"""Sets the points that define the geometry of this datum origin."""
		self._instance.ISetAxisPoints = value

	@property
	def reattach(self):
		"""Attaches the datum origin to a different entity."""
		return self._instance.Reattach

	@reattach.setter
	def reattach(self, value):
		"""Attaches the datum origin to a different entity."""
		self._instance.Reattach = value

	@property
	def set_axis_points(self):
		"""Sets the points that define the geometry of this datum origin."""
		return self._instance.SetAxisPoints

	@set_axis_points.setter
	def set_axis_points(self, value):
		"""Sets the points that define the geometry of this datum origin."""
		self._instance.SetAxisPoints = value

