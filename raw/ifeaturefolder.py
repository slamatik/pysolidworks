# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureFolder_members.html
class IFeatureFolder:
	def __init__(self, parent=None):
		self._instance = parent

	def get_feature_count(self):
		"""Gets the number of features in this feature folder."""
		# return self._instance.GetFeatureCount
		raise NotImplemented

	def get_features(self):
		"""Gets the features in this feature folder."""
		# return self._instance.GetFeatures
		raise NotImplemented

	def i_get_features(self, num_of_features):
		"""
		Gets the features in this feature folder.
		:param num_of_features: Number of features in the folder
		"""
		# return self._instance.IGetFeatures(num_of_features)
		raise NotImplemented

