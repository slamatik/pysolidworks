# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet_members.html
class ISWPropertySheet:
	def __init__(self, parent=None):
		self._instance = parent

	def add_active_page(self, title, prog_id, license_key):
		"""
		Adds a third-party CPropertyPage to ISWPropertySheet and adds an ActiveX control on top of the page.
		:param title: Title of CPropertyPage
		:param prog_id: Name, ProgID, or CLSID of the ActiveX control (see Remarks)
		:param license_key: License key for the ActiveX control
		"""
		# return self._instance.AddActivePage(title, prog_id, license_key)
		raise NotImplemented

	def add_page(self, page):
		"""
		Adds a CPropertyPage-derived page to an ISWPropertySheet.
		:param page: Pointer to the CPropertyPage to add, cast to a long
		"""
		# return self._instance.AddPage(page)
		raise NotImplemented

	def add_pagex(self, page):
		"""
		Adds a CPropertyPage-derived page to an ISWPropertySheet in 64-bit applications.
		:param page: Pointer to the CPropertyPage to add, cast to a long long
		"""
		# return self._instance.AddPagex64(page)
		raise NotImplemented

	def get_control(self, page_index):
		"""
		Gets the ActiveX control on the property sheet.
		:param page_index: Index of property sheet
		"""
		# return self._instance.GetControl(page_index)
		raise NotImplemented

	def remove_page(self, page):
		"""
		Removes a CPropertyPage derived page from an ISWPropertySheet.
		:param page: CPropertyPage to add, cast to a long
		"""
		# return self._instance.RemovePage(page)
		raise NotImplemented

