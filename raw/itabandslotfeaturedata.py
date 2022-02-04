# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotFeatureData_members.html
class ITabAndSlotFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def access_selections(self, top_doc, component):
		"""
		Accesses the selections that define this Tab and Slot feature.
		:param top_doc: Top-level document
		:param component: Component in which the feature is to be modified
		"""
		# return self._instance.AccessSelections(top_doc, component)
		raise NotImplemented

	def release_selection_access(self):
		"""Releases access to the selections for this Tab and Slot feature."""
		# return self._instance.ReleaseSelectionAccess
		raise NotImplemented

	def selection_add_new_group(self):
		"""Adds a Tab and Slot group."""
		# return self._instance.SelectionAddNewGroup
		raise NotImplemented

	def selection_get_groups(self):
		"""Gets the Tab and Slot groups defined for this part."""
		# return self._instance.SelectionGetGroups
		raise NotImplemented

