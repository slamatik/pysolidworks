# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserProgressBar_members.html
class IUserProgressBar:
	def __init__(self, parent=None):
		self._instance = parent

	def end(self):
		"""Removes the progress indicator from the SOLIDWORKS status bar."""
		# return self._instance.End
		raise NotImplemented

	def start(self, lower_bound, upper_bound, progress_bar_title):
		"""
		Sets the range of the progress indicator display and shows it on the SOLIDWORKS status bar.
		:param lower_bound: Lower bound of range
		:param upper_bound: Upper bound of range
		:param progress_bar_title: Title of progress indicator to show in status bar
		"""
		# return self._instance.Start(lower_bound, upper_bound, progress_bar_title)
		raise NotImplemented

	def update_progress(self, position):
		"""
		Increments the progress indicator.
		:param position: New position of the progress indicator
		"""
		# return self._instance.UpdateProgress(position)
		raise NotImplemented

	def update_title(self, progress_bar_title):
		"""
		Changes the title of the progress indicator.
		:param progress_bar_title: New title of progress indicator
		"""
		# return self._instance.UpdateTitle(progress_bar_title)
		raise NotImplemented

