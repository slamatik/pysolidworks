# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGroundPlaneFeatureData_members.html
class IGroundPlaneFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def planar_entity(self):
		"""Gets or sets the planar entity for this ground plane feature."""
		return self._instance.PlanarEntity

	@planar_entity.setter
	def planar_entity(self, value):
		"""Gets or sets the planar entity for this ground plane feature."""
		self._instance.PlanarEntity = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse direction of alignment in this ground plane feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse direction of alignment in this ground plane feature."""
		self._instance.ReverseDirection = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this ground plane feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this ground plane feature."""
		self._instance.AccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this ground plane feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this ground plane feature."""
		self._instance.ReleaseSelectionAccess = value

