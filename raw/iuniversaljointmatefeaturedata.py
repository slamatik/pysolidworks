# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUniversalJointMateFeatureData_members.html
class IUniversalJointMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def define_joint_point(self):
		"""Gets or sets whether to define a joint point."""
		return self._instance.DefineJointPoint

	@define_joint_point.setter
	def define_joint_point(self, value):
		"""Gets or sets whether to define a joint point."""
		self._instance.DefineJointPoint = value

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities to mate in this universal joint mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities to mate in this universal joint mate."""
		self._instance.EntitiesToMate = value

	@property
	def joint_point(self):
		"""Gets or sets the joint point of this universal joint mate."""
		return self._instance.JointPoint

	@joint_point.setter
	def joint_point(self, value):
		"""Gets or sets the joint point of this universal joint mate."""
		self._instance.JointPoint = value

