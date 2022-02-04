# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScrewMateFeatureData_members.html
class IScrewMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this screw mate feature."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this screw mate feature."""
		self._instance.EntitiesToMate = value

	@property
	def mate_alignment(self):
		"""Gets or sets the alignment of this screw mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the alignment of this screw mate."""
		self._instance.MateAlignment = value

	@property
	def reverse(self):
		"""Gets or sets whether to change the direction of movement of the components relative to one another."""
		return self._instance.Reverse

	@reverse.setter
	def reverse(self, value):
		"""Gets or sets whether to change the direction of movement of the components relative to one another."""
		self._instance.Reverse = value

	@property
	def revolution_type(self):
		"""Gets or sets the type of revolution to specify for this screw mate."""
		return self._instance.RevolutionType

	@revolution_type.setter
	def revolution_type(self, value):
		"""Gets or sets the type of revolution to specify for this screw mate."""
		self._instance.RevolutionType = value

	@property
	def revolution_val(self):
		"""Gets or sets either the number of revolutions one component makes for each unit length that the other component translates or the distance that one component translates for each revolution of the other component."""
		return self._instance.RevolutionVal

	@revolution_val.setter
	def revolution_val(self, value):
		"""Gets or sets either the number of revolutions one component makes for each unit length that the other component translates or the distance that one component translates for each revolution of the other component."""
		self._instance.RevolutionVal = value

