# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMotionPlotAxisFeatureData_members.html
class IMotionPlotAxisFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def component(self):
		"""Gets or sets the component of the result vector quantity."""
		return self._instance.Component

	@component.setter
	def component(self, value):
		"""Gets or sets the component of the result vector quantity."""
		self._instance.Component = value

	@property
	def entities(self):
		"""Gets or sets the entities whose motion you want to measure."""
		return self._instance.Entities

	@entities.setter
	def entities(self, value):
		"""Gets or sets the entities whose motion you want to measure."""
		self._instance.Entities = value

	@property
	def reference_part(self):
		"""Gets or sets the result component."""
		return self._instance.ReferencePart

	@reference_part.setter
	def reference_part(self, value):
		"""Gets or sets the result component."""
		self._instance.ReferencePart = value

	@property
	def type(self):
		"""Gets or sets the type of plot."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of plot."""
		self._instance.Type = value

