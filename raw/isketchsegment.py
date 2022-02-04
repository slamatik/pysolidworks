# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment_members.html
class ISketchSegment:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def color(self):
		"""Gets or sets the color of this sketch segment. Sketch segment color is only supported in drawing documents."""
		return self._instance.Color

	@color.setter
	def color(self, value):
		"""Gets or sets the color of this sketch segment. Sketch segment color is only supported in drawing documents."""
		self._instance.Color = value

	@property
	def construction_geometry(self):
		"""Gets or sets whether this sketch segment is construction geometry, for example, a centerline for a feature revolve operation."""
		return self._instance.ConstructionGeometry

	@construction_geometry.setter
	def construction_geometry(self, value):
		"""Gets or sets whether this sketch segment is construction geometry, for example, a centerline for a feature revolve operation."""
		self._instance.ConstructionGeometry = value

	@property
	def layer(self):
		"""gets or sets the layer used by this sketch segment."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""gets or sets the layer used by this sketch segment."""
		self._instance.Layer = value

	@property
	def layer_override(self):
		"""Gets or sets whether the sketch segment has properties that override the default properties of the layer."""
		return self._instance.LayerOverride

	@layer_override.setter
	def layer_override(self, value):
		"""Gets or sets whether the sketch segment has properties that override the default properties of the layer."""
		self._instance.LayerOverride = value

	@property
	def status(self):
		"""Gets the type of sketch constraint for this sketch segment.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Status

	@status.setter
	def status(self, value):
		"""Gets the type of sketch constraint for this sketch segment.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Status = value

	@property
	def style(self):
		"""Gets or sets the line style for this sketch segment."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets the line style for this sketch segment."""
		self._instance.Style = value

	@property
	def width(self):
		"""Gets or sets the line width for this sketch segment."""
		return self._instance.Width

	@width.setter
	def width(self, value):
		"""Gets or sets the line width for this sketch segment."""
		self._instance.Width = value

	@property
	def create_wire_body(self):
		"""Creates a wire body using the selected sketch segment."""
		return self._instance.CreateWireBody

	@create_wire_body.setter
	def create_wire_body(self, value):
		"""Creates a wire body using the selected sketch segment."""
		self._instance.CreateWireBody = value

	@property
	def de_select(self):
		"""Deselects the sketch segment."""
		return self._instance.DeSelect

	@de_select.setter
	def de_select(self, value):
		"""Deselects the sketch segment."""
		self._instance.DeSelect = value

	@property
	def equal_segment(self):
		"""Divides this sketch segment into equally spaced sketch segments or points."""
		return self._instance.EqualSegment

	@equal_segment.setter
	def equal_segment(self, value):
		"""Divides this sketch segment into equally spaced sketch segments or points."""
		self._instance.EqualSegment = value

	@property
	def get_constraints(self):
		"""Gets the constraints for this sketch segment."""
		return self._instance.GetConstraints

	@get_constraints.setter
	def get_constraints(self, value):
		"""Gets the constraints for this sketch segment."""
		self._instance.GetConstraints = value

	@property
	def get_curve(self):
		"""Gets the underlying curve for this sketch segment."""
		return self._instance.GetCurve

	@get_curve.setter
	def get_curve(self, value):
		"""Gets the underlying curve for this sketch segment."""
		self._instance.GetCurve = value

	@property
	def get_i_d(self):
		"""Gets the for this sketch segment."""
		return self._instance.GetID

	@get_i_d.setter
	def get_i_d(self, value):
		"""Gets the for this sketch segment."""
		self._instance.GetID = value

	@property
	def get_length(self):
		"""Gets the length of this sketch segment."""
		return self._instance.GetLength

	@get_length.setter
	def get_length(self, value):
		"""Gets the length of this sketch segment."""
		self._instance.GetLength = value

	@property
	def get_name(self):
		"""Gets the name of this sketch segment."""
		return self._instance.GetName

	@get_name.setter
	def get_name(self, value):
		"""Gets the name of this sketch segment."""
		self._instance.GetName = value

	@property
	def get_relations(self):
		"""Gets the sketch relations for this sketch segment."""
		return self._instance.GetRelations

	@get_relations.setter
	def get_relations(self, value):
		"""Gets the sketch relations for this sketch segment."""
		self._instance.GetRelations = value

	@property
	def get_relations_count(self):
		"""Gets the number of sketch relations for this sketch segment."""
		return self._instance.GetRelationsCount

	@get_relations_count.setter
	def get_relations_count(self, value):
		"""Gets the number of sketch relations for this sketch segment."""
		self._instance.GetRelationsCount = value

	@property
	def get_sketch(self):
		"""Gets the sketch for the current sketch segment."""
		return self._instance.GetSketch

	@get_sketch.setter
	def get_sketch(self, value):
		"""Gets the sketch for the current sketch segment."""
		self._instance.GetSketch = value

	@property
	def get_sketch_path_count(self):
		"""Gets the number of sketch paths for this sketch segment"""
		return self._instance.GetSketchPathCount

	@get_sketch_path_count.setter
	def get_sketch_path_count(self, value):
		"""Gets the number of sketch paths for this sketch segment"""
		self._instance.GetSketchPathCount = value

	@property
	def get_sketch_paths(self):
		"""Gets the sketch paths for this sketch segment."""
		return self._instance.GetSketchPaths

	@get_sketch_paths.setter
	def get_sketch_paths(self, value):
		"""Gets the sketch paths for this sketch segment."""
		self._instance.GetSketchPaths = value

	@property
	def get_sketch_slot(self):
		"""Gets sketch slot with which this sketch segment is associated."""
		return self._instance.GetSketchSlot

	@get_sketch_slot.setter
	def get_sketch_slot(self, value):
		"""Gets sketch slot with which this sketch segment is associated."""
		self._instance.GetSketchSlot = value

	@property
	def get_type(self):
		"""Gets the type of sketch segment."""
		return self._instance.GetType

	@get_type.setter
	def get_type(self, value):
		"""Gets the type of sketch segment."""
		self._instance.GetType = value

	@property
	def i_get_constraints(self):
		"""Gets the constraints for this sketch segment."""
		return self._instance.IGetConstraints

	@i_get_constraints.setter
	def i_get_constraints(self, value):
		"""Gets the constraints for this sketch segment."""
		self._instance.IGetConstraints = value

	@property
	def i_get_constraints_count(self):
		"""Gets the number of constraints on the sketch segment."""
		return self._instance.IGetConstraintsCount

	@i_get_constraints_count.setter
	def i_get_constraints_count(self, value):
		"""Gets the number of constraints on the sketch segment."""
		self._instance.IGetConstraintsCount = value

	@property
	def i_get_curve(self):
		"""Gets the underlying curve for this sketch segment."""
		return self._instance.IGetCurve

	@i_get_curve.setter
	def i_get_curve(self, value):
		"""Gets the underlying curve for this sketch segment."""
		self._instance.IGetCurve = value

	@property
	def i_get_i_d(self):
		"""Gets the ID for this sketch segment."""
		return self._instance.IGetID

	@i_get_i_d.setter
	def i_get_i_d(self, value):
		"""Gets the ID for this sketch segment."""
		self._instance.IGetID = value

	@property
	def i_get_relations(self):
		"""Gets the sketch relations for this sketch segment."""
		return self._instance.IGetRelations

	@i_get_relations.setter
	def i_get_relations(self, value):
		"""Gets the sketch relations for this sketch segment."""
		self._instance.IGetRelations = value

	@property
	def i_get_sketch_paths(self):
		"""Gets the sketch paths in this sketch segment."""
		return self._instance.IGetSketchPaths

	@i_get_sketch_paths.setter
	def i_get_sketch_paths(self, value):
		"""Gets the sketch paths in this sketch segment."""
		self._instance.IGetSketchPaths = value

	@property
	def is_bend_line(self):
		"""Gets whether the sketch segment is a bendline."""
		return self._instance.IsBendLine

	@is_bend_line.setter
	def is_bend_line(self, value):
		"""Gets whether the sketch segment is a bendline."""
		self._instance.IsBendLine = value

	@property
	def jog_line(self):
		"""Creates rectangular jog on the specified line."""
		return self._instance.JogLine

	@jog_line.setter
	def jog_line(self, value):
		"""Creates rectangular jog on the specified line."""
		self._instance.JogLine = value

	@property
	def select(self):
		"""Selects this sketch segment and marks it."""
		return self._instance.Select4

	@select.setter
	def select(self, value):
		"""Selects this sketch segment and marks it."""
		self._instance.Select4 = value

	@property
	def select_chain(self):
		"""Selects chains of entities attached to this sketch segment."""
		return self._instance.SelectChain

	@select_chain.setter
	def select_chain(self, value):
		"""Selects chains of entities attached to this sketch segment."""
		self._instance.SelectChain = value

	@property
	def split_entity(self):
		"""Splits the selected sketch entity at the specified point."""
		return self._instance.SplitEntity

	@split_entity.setter
	def split_entity(self, value):
		"""Splits the selected sketch entity at the specified point."""
		self._instance.SplitEntity = value

