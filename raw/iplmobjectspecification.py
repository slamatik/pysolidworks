# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification_members.html
class IPLMObjectSpecification:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def p_l_m_i_d(self):
		"""Gets or sets the ID of a SOLIDWORKS Connected document."""
		return self._instance.PLMID

	@p_l_m_i_d.setter
	def p_l_m_i_d(self, value):
		"""Gets or sets the ID of a SOLIDWORKS Connected document."""
		self._instance.PLMID = value

