# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBoundingBoxFeatureData_members.html
class IBoundingBoxFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def include_envelope_components(self):
		"""Gets or sets whether to include envelope components in this bounding box feature."""
		return self._instance.IncludeEnvelopeComponents

	@include_envelope_components.setter
	def include_envelope_components(self, value):
		"""Gets or sets whether to include envelope components in this bounding box feature."""
		self._instance.IncludeEnvelopeComponents = value

	@property
	def include_hidden_bodies(self):
		"""Gets or sets whether to include hidden bodies in this bounding box feature."""
		return self._instance.IncludeHiddenBodies

	@include_hidden_bodies.setter
	def include_hidden_bodies(self, value):
		"""Gets or sets whether to include hidden bodies in this bounding box feature."""
		self._instance.IncludeHiddenBodies = value

	@property
	def include_hidden_components(self):
		"""Gets or sets whether to include hidden components in this bounding box feature."""
		return self._instance.IncludeHiddenComponents

	@include_hidden_components.setter
	def include_hidden_components(self, value):
		"""Gets or sets whether to include hidden components in this bounding box feature."""
		self._instance.IncludeHiddenComponents = value

	@property
	def include_surfaces(self):
		"""Gets or sets whether to include surfaces in this bounding box feature."""
		return self._instance.IncludeSurfaces

	@include_surfaces.setter
	def include_surfaces(self, value):
		"""Gets or sets whether to include surfaces in this bounding box feature."""
		self._instance.IncludeSurfaces = value

	@property
	def planar_entity(self):
		"""Gets or sets the reference face or plane for this bounding box feature."""
		return self._instance.PlanarEntity

	@planar_entity.setter
	def planar_entity(self, value):
		"""Gets or sets the reference face or plane for this bounding box feature."""
		self._instance.PlanarEntity = value

	@property
	def reference_face_or_plane(self):
		"""Gets or sets how to create the bounding box."""
		return self._instance.ReferenceFaceOrPlane

	@reference_face_or_plane.setter
	def reference_face_or_plane(self, value):
		"""Gets or sets how to create the bounding box."""
		self._instance.ReferenceFaceOrPlane = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this bounding box feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this bounding box feature."""
		self._instance.AccessSelections = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this bounding box feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this bounding box feature."""
		self._instance.ReleaseSelectionAccess = value

