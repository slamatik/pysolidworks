# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html
class IIntersectFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def cap_planar(self):
		"""Gets or sets whether to close the flat openings of surfaces."""
		return self._instance.CapPlanar

	@cap_planar.setter
	def cap_planar(self, value):
		"""Gets or sets whether to close the flat openings of surfaces."""
		self._instance.CapPlanar = value

	@property
	def consume(self):
		"""Gets or sets whether to remove input surfaces from the FeatureManager design tree."""
		return self._instance.Consume

	@consume.setter
	def consume(self, value):
		"""Gets or sets whether to remove input surfaces from the FeatureManager design tree."""
		self._instance.Consume = value

	@property
	def merge(self):
		"""Gets or sets whether to merge included regions into one body."""
		return self._instance.Merge

	@merge.setter
	def merge(self, value):
		"""Gets or sets whether to merge included regions into one body."""
		self._instance.Merge = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this intersect feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this intersect feature."""
		self._instance.AccessSelections = value

	@property
	def get_intersections(self):
		"""Gets the intersect regions in this intersect feature."""
		return self._instance.GetIntersections

	@get_intersections.setter
	def get_intersections(self, value):
		"""Gets the intersect regions in this intersect feature."""
		self._instance.GetIntersections = value

	@property
	def get_intersections_count(self):
		"""Gets the number of intersect regions in this intersect feature."""
		return self._instance.GetIntersectionsCount

	@get_intersections_count.setter
	def get_intersections_count(self, value):
		"""Gets the number of intersect regions in this intersect feature."""
		self._instance.GetIntersectionsCount = value

	@property
	def get_intersections_tools(self):
		"""Gets the intersecting solids, surfaces, and planes in this intersect feature."""
		return self._instance.GetIntersectionsTools

	@get_intersections_tools.setter
	def get_intersections_tools(self, value):
		"""Gets the intersecting solids, surfaces, and planes in this intersect feature."""
		self._instance.GetIntersectionsTools = value

	@property
	def get_intersections_tools_count(self):
		"""Gets the number of solids, surfaces, and planes used to create this intersect feature."""
		return self._instance.GetIntersectionsToolsCount

	@get_intersections_tools_count.setter
	def get_intersections_tools_count(self, value):
		"""Gets the number of solids, surfaces, and planes used to create this intersect feature."""
		self._instance.GetIntersectionsToolsCount = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this intersect feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this intersect feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_intersections(self):
		"""Specifies which of the intersect regions to exclude from this intersect feature."""
		return self._instance.SetIntersections

	@set_intersections.setter
	def set_intersections(self, value):
		"""Specifies which of the intersect regions to exclude from this intersect feature."""
		self._instance.SetIntersections = value

	@property
	def set_intersections_tools(self):
		"""Specifies the intersecting solids, surfaces, and planes for this intersect feature."""
		return self._instance.SetIntersectionsTools

	@set_intersections_tools.setter
	def set_intersections_tools(self, value):
		"""Specifies the intersecting solids, surfaces, and planes for this intersect feature."""
		self._instance.SetIntersectionsTools = value

