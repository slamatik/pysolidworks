# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.html
class ISurfaceRadiateFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def direction_reference(self):
		"""Gets or sets the radiate direction setting for this surface radiate feature."""
		return self._instance.DirectionReference

	@direction_reference.setter
	def direction_reference(self, value):
		"""Gets or sets the radiate direction setting for this surface radiate feature."""
		self._instance.DirectionReference = value

	@property
	def distance(self):
		"""Gets or sets the radiate distance for this surface radiate feature."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the radiate distance for this surface radiate feature."""
		self._instance.Distance = value

	@property
	def flip(self):
		"""Gets or sets whether to flip the direction of this surface radiate feature."""
		return self._instance.Flip

	@flip.setter
	def flip(self, value):
		"""Gets or sets whether to flip the direction of this surface radiate feature."""
		self._instance.Flip = value

	@property
	def propagate_to_tangent_faces(self):
		"""Gets or sets whether to propagate the tangent faces of this surface radiate feature."""
		return self._instance.PropagateToTangentFaces

	@propagate_to_tangent_faces.setter
	def propagate_to_tangent_faces(self, value):
		"""Gets or sets whether to propagate the tangent faces of this surface radiate feature."""
		self._instance.PropagateToTangentFaces = value

	@property
	def radiated_entities(self):
		"""Gets or sets the radiated entities for this surface radiate feature."""
		return self._instance.RadiatedEntities

	@radiated_entities.setter
	def radiated_entities(self, value):
		"""Gets or sets the radiated entities for this surface radiate feature."""
		self._instance.RadiatedEntities = value

	@property
	def access_selections(self):
		"""Accesses the selections for this surface radiate feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Accesses the selections for this surface radiate feature."""
		self._instance.AccessSelections = value

	@property
	def get_radiated_entities_count(self):
		"""Gets the number of radiated entities for this surface radiate feature."""
		return self._instance.GetRadiatedEntitiesCount

	@get_radiated_entities_count.setter
	def get_radiated_entities_count(self, value):
		"""Gets the number of radiated entities for this surface radiate feature."""
		self._instance.GetRadiatedEntitiesCount = value

	@property
	def i_access_selections(self):
		"""Accesses the selections for this surface radiate feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Accesses the selections for this surface radiate feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_radiated_entities(self):
		"""Gets the radiated entities for this surface radiate feature."""
		return self._instance.IGetRadiatedEntities

	@i_get_radiated_entities.setter
	def i_get_radiated_entities(self, value):
		"""Gets the radiated entities for this surface radiate feature."""
		self._instance.IGetRadiatedEntities = value

	@property
	def i_set_radiated_entities(self):
		"""Sets the radiated entities for this surface radiate feature."""
		return self._instance.ISetRadiatedEntities

	@i_set_radiated_entities.setter
	def i_set_radiated_entities(self, value):
		"""Sets the radiated entities for this surface radiate feature."""
		self._instance.ISetRadiatedEntities = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this surface radiate feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this surface radiate feature."""
		self._instance.ReleaseSelectionAccess = value

