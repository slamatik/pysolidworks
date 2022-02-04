# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData_members.html
class ISMNormalCutGroupData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def faces(self):
		"""Gets or sets the cut-extrude faces in this group."""
		return self._instance.Faces

	@faces.setter
	def faces(self, value):
		"""Gets or sets the cut-extrude faces in this group."""
		self._instance.Faces = value

	@property
	def get_group_name(self):
		"""Gets the name of the group."""
		return self._instance.GetGroupName

	@get_group_name.setter
	def get_group_name(self, value):
		"""Gets the name of the group."""
		self._instance.GetGroupName = value

