# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISwPEClassFactory_members.html
class ISwPEClassFactory:
	def __init__(self, parent=None):
		self._instance = parent

	def set_partner_key(self, str_partner_entitlement, token_object):
		"""
		Sets the license key which SOLIDWORKS uses to verify SOLIDWORKS Partner entitlement.
		:param str_partner_entitlement: License key string (see Remarks)
		:param token_object: ISwPEToken (for future use only - see Remarks)
		"""
		# return self._instance.SetPartnerKey(str_partner_entitlement, token_object)
		raise NotImplemented

