# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICompositeCurveFeatureData_members.html
class ICompositeCurveFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def access_selections(self, top_doc, component):
		"""
		Gains access to the selections that define this composite curve.
		:param top_doc: Top-level document
		:param component: Component in which the feature is to be modified
		"""
		# return self._instance.AccessSelections(top_doc, component)
		raise NotImplemented

	def get_entities_to_join(self, type):
		"""
		Gets the entities to join to create this composite curve feature.
		:param type: Type of entity as defined in swSelectType_e
		"""
		# return self._instance.GetEntitiesToJoin(type)
		raise NotImplemented

	def get_entities_to_join_count(self):
		"""Gets the number of entities that are joined to create a composite curve."""
		# return self._instance.GetEntitiesToJoinCount
		raise NotImplemented

	def i_get_entities_to_join(self, count, type):
		"""
		Gets the entities to join to create this composite curve.
		:param count: Number of entities 
		:param type: Type of entity as defined in swSelectType_e
		"""
		# return self._instance.IGetEntitiesToJoin(count, type)
		raise NotImplemented

	def i_set_entities_to_join(self, count, ents):
		"""
		Sets the entities to join to create this composite curve.
		:param count: Number of entities
		:param ents: in-process, unmanaged C++: Pointer to an array of entities (see Remarks)
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		"""
		# return self._instance.ISetEntitiesToJoin(count, ents)
		raise NotImplemented

	def release_selection_access(self):
		"""Releases access to the selections that define this composite curve."""
		# return self._instance.ReleaseSelectionAccess
		raise NotImplemented

	def set_entities_to_join(self, ent_var):
		"""
		Sets the entities to join to create this composite curve.
		:param ent_var: Array of entities (see Remarks)
		"""
		# return self._instance.SetEntitiesToJoin(ent_var)
		raise NotImplemented

