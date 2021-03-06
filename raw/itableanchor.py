# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnchor_members.html
class ITableAnchor:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def position(self):
		"""Gets or sets the location of the table anchor."""
		return self._instance.Position

	@position.setter
	def position(self, value):
		"""Gets or sets the location of the table anchor."""
		self._instance.Position = value

	@property
	def type(self):
		"""Gets the type of table anchor."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the type of table anchor."""
		self._instance.Type = value

	@property
	def get_feature(self):
		"""Gets the feature for this table anchor."""
		return self._instance.GetFeature

	@get_feature.setter
	def get_feature(self, value):
		"""Gets the feature for this table anchor."""
		self._instance.GetFeature = value

