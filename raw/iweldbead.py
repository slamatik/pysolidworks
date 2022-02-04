# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldBead_members.html
class IWeldBead:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def solid_fill(self):
		"""Gets or sets whether to fill the weld bead annotation."""
		return self._instance.SolidFill

	@solid_fill.setter
	def solid_fill(self, value):
		"""Gets or sets whether to fill the weld bead annotation."""
		self._instance.SolidFill = value

	@property
	def get_annotation(self):
		"""Gets the annotation for this weld bead."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the annotation for this weld bead."""
		self._instance.GetAnnotation = value

	@property
	def get_next(self):
		"""Gets the next weld bead annotation in the drawing view."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next weld bead annotation in the drawing view."""
		self._instance.GetNext = value

