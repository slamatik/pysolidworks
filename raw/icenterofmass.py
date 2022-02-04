# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterOfMass_members.html
class ICenterOfMass:
	def __init__(self, parent=None):
		self._instance = parent

	def get_annotation(self):
		"""Gets the annotation for this center of mass."""
		# return self._instance.GetAnnotation
		raise NotImplemented

	def get_coordinates(self):
		"""Gets the coordinates of this center of mass."""
		# return self._instance.GetCoordinates
		raise NotImplemented

	def get_next(self):
		"""Gets the next center of mass in this drawing view."""
		# return self._instance.GetNext
		raise NotImplemented

	def i_get_annotation(self):
		"""Gets the annotation for this center of mass."""
		# return self._instance.IGetAnnotation
		raise NotImplemented

	def i_get_coordinates(self):
		"""Gets the coordinates of this center of mass."""
		# return self._instance.IGetCoordinates
		raise NotImplemented

	def i_get_next(self):
		"""Gets the next center of mass in this drawing view."""
		# return self._instance.IGetNext
		raise NotImplemented

