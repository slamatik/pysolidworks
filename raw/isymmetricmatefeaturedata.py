# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData_members.html
class ISymmetricMateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def entities_to_mate(self):
		"""Gets or sets the entities in this symmetry mate."""
		return self._instance.EntitiesToMate

	@entities_to_mate.setter
	def entities_to_mate(self, value):
		"""Gets or sets the entities in this symmetry mate."""
		self._instance.EntitiesToMate = value

	@property
	def mate_alignment(self):
		"""Gets or sets the alignment of this symmetry mate."""
		return self._instance.MateAlignment

	@mate_alignment.setter
	def mate_alignment(self, value):
		"""Gets or sets the alignment of this symmetry mate."""
		self._instance.MateAlignment = value

	@property
	def symmetry_plane(self):
		"""Gets or sets the symmetry plane of this symmetry mate."""
		return self._instance.SymmetryPlane

	@symmetry_plane.setter
	def symmetry_plane(self, value):
		"""Gets or sets the symmetry plane of this symmetry mate."""
		self._instance.SymmetryPlane = value

