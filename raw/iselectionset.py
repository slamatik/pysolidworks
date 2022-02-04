# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionSet_members.html
class ISelectionSet:
	def __init__(self, parent=None):
		self._instance = parent

	def get_name(self):
		"""Gets the name of the selection set."""
		# return self._instance.GetName
		raise NotImplemented

	def get_selection_set_items(self):
		"""Gets the selection set items in this selection set."""
		# return self._instance.GetSelectionSetItems
		raise NotImplemented

	def get_selection_set_item_types(self):
		"""Gets the types of entities in this selection set."""
		# return self._instance.GetSelectionSetItemTypes
		raise NotImplemented

	def remove_selection_set(self):
		"""Deletes this selection set from the Selection Sets folder."""
		# return self._instance.RemoveSelectionSet
		raise NotImplemented

	def select(self):
		"""Selects all of the objects in this selection set."""
		# return self._instance.Select
		raise NotImplemented

