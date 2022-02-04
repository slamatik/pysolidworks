# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSetItem_members.html
class ISelectionSetItem:
	def __init__(self, parent=None):
		self._instance = parent

	def get_corresponding_item(self):
		"""Gets the Dispatch object for this selection set item."""
		# return self._instance.GetCorrespondingItem
		raise NotImplemented

	def remove_from_selection_set(self):
		"""Deletes this selection set item from this selection set."""
		# return self._instance.RemoveFromSelectionSet
		raise NotImplemented

