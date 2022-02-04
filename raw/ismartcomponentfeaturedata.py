# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData_members.html
class ISmartComponentFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def access_selections(self, show_p_m_p):
		"""
		Gains access to the selection lists on the PropertyManager page of a Smart Component.
		:param show_p_m_p: True to display the PropertyManager page, false to not (see Remarks)
		"""
		# return self._instance.AccessSelections(show_p_m_p)
		raise NotImplemented

	def release_selection_access(self):
		"""Releases access to the selection lists of a Smart Component."""
		# return self._instance.ReleaseSelectionAccess
		raise NotImplemented

