# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakCornerFeatureData_members.html
class IBreakCornerFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def break_type(self):
		"""Gets or sets the break corner type."""
		return self._instance.BreakType

	@break_type.setter
	def break_type(self, value):
		"""Gets or sets the break corner type."""
		self._instance.BreakType = value

	@property
	def centered_on_bend_lines(self):
		"""Gets or sets whether to center the corner cuts relative to the bend lines of this break corner feature."""
		return self._instance.CenteredOnBendLines

	@centered_on_bend_lines.setter
	def centered_on_bend_lines(self, value):
		"""Gets or sets whether to center the corner cuts relative to the bend lines of this break corner feature."""
		self._instance.CenteredOnBendLines = value

	@property
	def distance(self):
		"""Gets or sets the chamfer length or fillet radius, depending on the break corner type."""
		return self._instance.Distance

	@distance.setter
	def distance(self, value):
		"""Gets or sets the chamfer length or fillet radius, depending on the break corner type."""
		self._instance.Distance = value

	@property
	def entities(self):
		"""Gets or sets the faces or edges to which this break corner is applied."""
		return self._instance.Entities

	@entities.setter
	def entities(self, value):
		"""Gets or sets the faces or edges to which this break corner is applied."""
		self._instance.Entities = value

	@property
	def internal_corners_only(self):
		"""Gets or sets whether to add or subtract material from break corner/corner trim features."""
		return self._instance.InternalCornersOnly

	@internal_corners_only.setter
	def internal_corners_only(self, value):
		"""Gets or sets whether to add or subtract material from break corner/corner trim features."""
		self._instance.InternalCornersOnly = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe this break corner feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe this break corner feature."""
		self._instance.AccessSelections = value

	@property
	def get_entities_count(self):
		"""Gets the number of faces or edges associated with this break corner feature."""
		return self._instance.GetEntitiesCount

	@get_entities_count.setter
	def get_entities_count(self, value):
		"""Gets the number of faces or edges associated with this break corner feature."""
		self._instance.GetEntitiesCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that describe this break corner feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that describe this break corner feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_entities(self):
		"""Gets the faces or edges to which this break corner is applied."""
		return self._instance.IGetEntities

	@i_get_entities.setter
	def i_get_entities(self, value):
		"""Gets the faces or edges to which this break corner is applied."""
		self._instance.IGetEntities = value

	@property
	def i_set_entities(self):
		"""Sets the faces or edges to which this break corner is applied."""
		return self._instance.ISetEntities

	@i_set_entities.setter
	def i_set_entities(self, value):
		"""Sets the faces or edges to which this break corner is applied."""
		self._instance.ISetEntities = value

	@property
	def release_selection_access(self):
		"""Releases access to selections for this break corner feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections for this break corner feature."""
		self._instance.ReleaseSelectionAccess = value

