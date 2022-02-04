# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.html
class ISketchBlockInstance:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the angle around the insertion point which to rotate this block instance."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle around the insertion point which to rotate this block instance."""
		self._instance.Angle = value

	@property
	def block_to_sketch_transform(self):
		"""Gets all of the sketch entities from a block definition and transforms them to coordinates in sketch space."""
		return self._instance.BlockToSketchTransform

	@block_to_sketch_transform.setter
	def block_to_sketch_transform(self, value):
		"""Gets all of the sketch entities from a block definition and transforms them to coordinates in sketch space."""
		self._instance.BlockToSketchTransform = value

	@property
	def definition(self):
		"""Gets or sets the block definition for this block instance."""
		return self._instance.Definition

	@definition.setter
	def definition(self, value):
		"""Gets or sets the block definition for this block instance."""
		self._instance.Definition = value

	@property
	def dimension_display(self):
		"""Gets whether dimensions are displayed."""
		return self._instance.DimensionDisplay

	@dimension_display.setter
	def dimension_display(self, value):
		"""Gets whether dimensions are displayed."""
		self._instance.DimensionDisplay = value

	@property
	def instance_position(self):
		"""Gets or sets the position for this block instance."""
		return self._instance.InstancePosition

	@instance_position.setter
	def instance_position(self, value):
		"""Gets or sets the position for this block instance."""
		self._instance.InstancePosition = value

	@property
	def layer(self):
		"""Gets or sets the name of the layer where this block is located."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""Gets or sets the name of the layer where this block is located."""
		self._instance.Layer = value

	@property
	def lock_angle(self):
		"""Gets or sets whether the angle around the insertion point which to rotate this block instance is locked."""
		return self._instance.LockAngle

	@lock_angle.setter
	def lock_angle(self, value):
		"""Gets or sets whether the angle around the insertion point which to rotate this block instance is locked."""
		self._instance.LockAngle = value

	@property
	def name(self):
		"""Gets or sets the name of this block instance."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the name of this block instance."""
		self._instance.Name = value

	@property
	def scale(self):
		"""Gets or sets the scale for this block instance."""
		return self._instance.Scale2

	@scale.setter
	def scale(self, value):
		"""Gets or sets the scale for this block instance."""
		self._instance.Scale2 = value

	@property
	def text_display(self):
		"""Gets or sets whether to display text for this block instance."""
		return self._instance.TextDisplay

	@text_display.setter
	def text_display(self, value):
		"""Gets or sets whether to display text for this block instance."""
		self._instance.TextDisplay = value

	@property
	def visible(self):
		"""Gets or sets the visibility of this block instance."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets the visibility of this block instance."""
		self._instance.Visible = value

	@property
	def get_arrow_head_style(self):
		"""Gets the arrowhead style of the leader on this block instance."""
		return self._instance.GetArrowHeadStyle

	@get_arrow_head_style.setter
	def get_arrow_head_style(self, value):
		"""Gets the arrowhead style of the leader on this block instance."""
		self._instance.GetArrowHeadStyle = value

	@property
	def get_attached_entities(self):
		"""Gets the entities to which this block instance is attached."""
		return self._instance.GetAttachedEntities

	@get_attached_entities.setter
	def get_attached_entities(self, value):
		"""Gets the entities to which this block instance is attached."""
		self._instance.GetAttachedEntities = value

	@property
	def get_attribute_count(self):
		"""Gets the number of attributes for this block instance."""
		return self._instance.GetAttributeCount

	@get_attribute_count.setter
	def get_attribute_count(self, value):
		"""Gets the number of attributes for this block instance."""
		self._instance.GetAttributeCount = value

	@property
	def get_attributes(self):
		"""Gets the attributes for this block instance."""
		return self._instance.GetAttributes

	@get_attributes.setter
	def get_attributes(self, value):
		"""Gets the attributes for this block instance."""
		self._instance.GetAttributes = value

	@property
	def get_attribute_value(self):
		"""Gets the value of the specified attribute for this block instance."""
		return self._instance.GetAttributeValue

	@get_attribute_value.setter
	def get_attribute_value(self, value):
		"""Gets the value of the specified attribute for this block instance."""
		self._instance.GetAttributeValue = value

	@property
	def get_leader_points(self):
		"""Gets the coordinate information for the leader on this block instance."""
		return self._instance.GetLeaderPoints

	@get_leader_points.setter
	def get_leader_points(self, value):
		"""Gets the coordinate information for the leader on this block instance."""
		self._instance.GetLeaderPoints = value

	@property
	def get_leader_style(self):
		"""Gets the leader style of this block instance."""
		return self._instance.GetLeaderStyle

	@get_leader_style.setter
	def get_leader_style(self, value):
		"""Gets the leader style of this block instance."""
		self._instance.GetLeaderStyle = value

	@property
	def get_sketch(self):
		"""Gets the sketch in which this block instance is present."""
		return self._instance.GetSketch

	@get_sketch.setter
	def get_sketch(self, value):
		"""Gets the sketch in which this block instance is present."""
		self._instance.GetSketch = value

	@property
	def i_get_attributes(self):
		"""Gets the attributes for this block instance."""
		return self._instance.IGetAttributes

	@i_get_attributes.setter
	def i_get_attributes(self, value):
		"""Gets the attributes for this block instance."""
		self._instance.IGetAttributes = value

	@property
	def i_get_leader_points(self):
		"""Gets the coordinate information for the leader on this block instance."""
		return self._instance.IGetLeaderPoints

	@i_get_leader_points.setter
	def i_get_leader_points(self, value):
		"""Gets the coordinate information for the leader on this block instance."""
		self._instance.IGetLeaderPoints = value

	@property
	def select(self):
		"""Selects and marks the block instance."""
		return self._instance.Select

	@select.setter
	def select(self, value):
		"""Selects and marks the block instance."""
		self._instance.Select = value

	@property
	def set_attribute_value(self):
		"""Sets the value of the specified attribute for this block instance."""
		return self._instance.SetAttributeValue

	@set_attribute_value.setter
	def set_attribute_value(self, value):
		"""Sets the value of the specified attribute for this block instance."""
		self._instance.SetAttributeValue = value

	@property
	def set_leader(self):
		"""Sets the leader style for this block instance."""
		return self._instance.SetLeader

	@set_leader.setter
	def set_leader(self, value):
		"""Sets the leader style for this block instance."""
		self._instance.SetLeader = value

