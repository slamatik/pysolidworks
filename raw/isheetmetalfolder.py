# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFolder_members.html
class ISheetMetalFolder:
	def __init__(self, parent=None):
		self._instance = parent

	def get_feature(self):
		"""Gets the feature for this sheet metal folder."""
		# return self._instance.GetFeature
		raise NotImplemented

	def get_sheet_metal_count(self):
		"""Gets the number of sheet metal features in this folder."""
		# return self._instance.GetSheetMetalCount
		raise NotImplemented

	def get_sheet_metals(self):
		"""Gets the sheet metal features in this folder."""
		# return self._instance.GetSheetMetals
		raise NotImplemented

