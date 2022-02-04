# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData_members.html
class IAdvancedHoleElementData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def blind_depth(self):
		"""Gets or sets the depth for the blind end condition of this Advanced Hole element."""
		return self._instance.BlindDepth

	@blind_depth.setter
	def blind_depth(self, value):
		"""Gets or sets the depth for the blind end condition of this Advanced Hole element."""
		self._instance.BlindDepth = value

	@property
	def callout_string(self):
		"""Gets or sets the hole callout string for this Advanced Hole element."""
		return self._instance.CalloutString

	@callout_string.setter
	def callout_string(self, value):
		"""Gets or sets the hole callout string for this Advanced Hole element."""
		self._instance.CalloutString = value

	@property
	def diameter(self):
		"""Gets or sets the diameter of this Advanced Hole element."""
		return self._instance.Diameter

	@diameter.setter
	def diameter(self, value):
		"""Gets or sets the diameter of this Advanced Hole element."""
		self._instance.Diameter = value

	@property
	def diameter_override(self):
		"""Gets or sets whether to override the diameter of this Advanced Hole element."""
		return self._instance.DiameterOverride

	@diameter_override.setter
	def diameter_override(self, value):
		"""Gets or sets whether to override the diameter of this Advanced Hole element."""
		self._instance.DiameterOverride = value

	@property
	def element_type(self):
		"""Gets the type of this Advanced Hole element."""
		return self._instance.ElementType

	@element_type.setter
	def element_type(self, value):
		"""Gets the type of this Advanced Hole element."""
		self._instance.ElementType = value

	@property
	def end_condition(self):
		"""Gets or sets the end condition for this Advanced Hole element."""
		return self._instance.EndCondition

	@end_condition.setter
	def end_condition(self, value):
		"""Gets or sets the end condition for this Advanced Hole element."""
		self._instance.EndCondition = value

	@property
	def fastener_type(self):
		"""Gets or sets the fastener type for this Advanced Hole element."""
		return self._instance.FastenerType

	@fastener_type.setter
	def fastener_type(self, value):
		"""Gets or sets the fastener type for this Advanced Hole element."""
		self._instance.FastenerType = value

	@property
	def offset_distance(self):
		"""Gets or sets the offset distance for this Advanced Hole element."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the offset distance for this Advanced Hole element."""
		self._instance.OffsetDistance = value

	@property
	def offset_reverse_direction(self):
		"""Gets or sets whether to reverse the offset direction for this Advanced Hole element."""
		return self._instance.OffsetReverseDirection

	@offset_reverse_direction.setter
	def offset_reverse_direction(self, value):
		"""Gets or sets whether to reverse the offset direction for this Advanced Hole element."""
		self._instance.OffsetReverseDirection = value

	@property
	def orientation(self):
		"""Gets or sets the orientation of this Advanced Hole element."""
		return self._instance.Orientation

	@orientation.setter
	def orientation(self, value):
		"""Gets or sets the orientation of this Advanced Hole element."""
		self._instance.Orientation = value

	@property
	def selection_entity(self):
		"""Gets or sets the entity used to specify the Up to Selection or Offset from Surface end condition for this Advanced Hole element."""
		return self._instance.SelectionEntity

	@selection_entity.setter
	def selection_entity(self, value):
		"""Gets or sets the entity used to specify the Up to Selection or Offset from Surface end condition for this Advanced Hole element."""
		self._instance.SelectionEntity = value

	@property
	def size(self):
		"""Gets or sets the size of this Advanced Hole element."""
		return self._instance.Size

	@size.setter
	def size(self, value):
		"""Gets or sets the size of this Advanced Hole element."""
		self._instance.Size = value

	@property
	def standard(self):
		"""Gets or sets the hole standard used for this Advanced Hole element."""
		return self._instance.Standard

	@standard.setter
	def standard(self, value):
		"""Gets or sets the hole standard used for this Advanced Hole element."""
		self._instance.Standard = value

