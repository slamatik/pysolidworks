# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureStatistics_members.html
class IFeatureStatistics:
	def __init__(self, parent=None):
		self._instance = parent

	def feature_count(self):
		"""Gets the number of features in a part document."""
		# return self._instance.FeatureCount
		raise NotImplemented

	def feature_names(self):
		"""Gets the names of the features in a part document."""
		# return self._instance.FeatureNames
		raise NotImplemented

	def features(self):
		"""Gets the features in a part document."""
		# return self._instance.Features
		raise NotImplemented

	def feature_types(self):
		"""Gets the types of features in a part document."""
		# return self._instance.FeatureTypes
		raise NotImplemented

	def feature_update_percentage_times(self):
		"""Gets the percentages of time it takes to update (rebuild) each feature in a part document relative to the total time it takes to update all features in that part document."""
		# return self._instance.FeatureUpdatePercentageTimes
		raise NotImplemented

	def feature_update_times(self):
		"""Gets the times, in seconds, it takes to update (rebuild) each feature in a part document."""
		# return self._instance.FeatureUpdateTimes
		raise NotImplemented

	def part_name(self):
		"""Gets the name of the part document whose feature statistics you want."""
		# return self._instance.PartName
		raise NotImplemented

	def solid_bodies_count(self):
		"""Gets the number of solid bodies in a part document."""
		# return self._instance.SolidBodiesCount
		raise NotImplemented

	def surface_bodies_count(self):
		"""Gets the number of surface bodies in a part document."""
		# return self._instance.SurfaceBodiesCount
		raise NotImplemented

	def total_rebuild_time(self):
		"""Gets the time, in seconds, it takes to rebuild (update) all features in a part document."""
		# return self._instance.TotalRebuildTime
		raise NotImplemented

	def refresh(self):
		"""Refreshes the feature statistics in a part document."""
		# return self._instance.Refresh
		raise NotImplemented

