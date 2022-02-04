# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICutListSortOptions_members.html
class ICutListSortOptions:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def collect_identical_bodies(self):
		"""Gets or sets whether to collect identical bodies into a cut list sub-folder."""
		return self._instance.CollectIdenticalBodies

	@collect_identical_bodies.setter
	def collect_identical_bodies(self, value):
		"""Gets or sets whether to collect identical bodies into a cut list sub-folder."""
		self._instance.CollectIdenticalBodies = value

	@property
	def get_faces_or_features_to_exclude(self):
		"""Gets the faces or features to exclude from cut list sorting."""
		return self._instance.GetFacesOrFeaturesToExclude

	@get_faces_or_features_to_exclude.setter
	def get_faces_or_features_to_exclude(self, value):
		"""Gets the faces or features to exclude from cut list sorting."""
		self._instance.GetFacesOrFeaturesToExclude = value

	@property
	def set_faces_or_features_to_exclude(self):
		"""Sets the faces or features to exclude from cut list sorting."""
		return self._instance.SetFacesOrFeaturesToExclude

	@set_faces_or_features_to_exclude.setter
	def set_faces_or_features_to_exclude(self, value):
		"""Sets the faces or features to exclude from cut list sorting."""
		self._instance.SetFacesOrFeaturesToExclude = value

