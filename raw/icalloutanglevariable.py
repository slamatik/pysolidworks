# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICalloutAngleVariable_members.html
class ICalloutAngleVariable:
	def __init__(self, parent=None):
		self._instance = parent

	def angle(self):
		"""Gets the value of an angle variable in a hole callout."""
		# return self._instance.Angle
		raise NotImplemented

