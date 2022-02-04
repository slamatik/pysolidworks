# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetFolder_members.html
class ISelectionSetFolder:
	def __init__(self, parent=None):
		self._instance = parent

	def get_selection_set_by_name(self, name):
		"""
		Gets the specified selection set.
		:param name: Name of the selection set
		"""
		# return self._instance.GetSelectionSetByName(name)
		raise NotImplemented

	def get_selection_sets(self):
		"""Gets the selection sets in the Selection Sets folder."""
		# return self._instance.GetSelectionSets
		raise NotImplemented

