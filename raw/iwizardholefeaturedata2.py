# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWizardHoleFeatureData2_members.html
class IWizardHoleFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def assembly_feature_scope(self):
		"""Gets or sets whether to use scope for this assembly Hole Wizard feature."""
		return self._instance.AssemblyFeatureScope

	@assembly_feature_scope.setter
	def assembly_feature_scope(self, value):
		"""Gets or sets whether to use scope for this assembly Hole Wizard feature."""
		self._instance.AssemblyFeatureScope = value

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all or only specific bodies for the Hole Wizard feature to affect in a multibody part."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all or only specific bodies for the Hole Wizard feature to affect in a multibody part."""
		self._instance.AutoSelect = value

	@property
	def auto_select_components(self):
		"""Gets or sets whether to auto-select all components that this assembly Hole Wizard feature affects in model."""
		return self._instance.AutoSelectComponents

	@auto_select_components.setter
	def auto_select_components(self, value):
		"""Gets or sets whether to auto-select all components that this assembly Hole Wizard feature affects in model."""
		self._instance.AutoSelectComponents = value

	@property
	def cosmetic_thread_type(self):
		"""Gets or sets the type of cosmetic thread for this tap or pipe-tap Hole Wizard feature."""
		return self._instance.CosmeticThreadType

	@cosmetic_thread_type.setter
	def cosmetic_thread_type(self, value):
		"""Gets or sets the type of cosmetic thread for this tap or pipe-tap Hole Wizard feature."""
		self._instance.CosmeticThreadType = value

	@property
	def counter_bore_depth(self):
		"""Gets or sets the Hole Wizard feature counterbore depth."""
		return self._instance.CounterBoreDepth

	@counter_bore_depth.setter
	def counter_bore_depth(self, value):
		"""Gets or sets the Hole Wizard feature counterbore depth."""
		self._instance.CounterBoreDepth = value

	@property
	def counter_bore_diameter(self):
		"""Gets or sets the Hole Wizard feature counterbore diameter."""
		return self._instance.CounterBoreDiameter

	@counter_bore_diameter.setter
	def counter_bore_diameter(self, value):
		"""Gets or sets the Hole Wizard feature counterbore diameter."""
		self._instance.CounterBoreDiameter = value

	@property
	def counter_drill_angle(self):
		"""Gets or sets the Hole Wizard feature counterdrill angle."""
		return self._instance.CounterDrillAngle

	@counter_drill_angle.setter
	def counter_drill_angle(self, value):
		"""Gets or sets the Hole Wizard feature counterdrill angle."""
		self._instance.CounterDrillAngle = value

	@property
	def counter_drill_depth(self):
		"""Gets or sets the Hole Wizard feature counterdrill depth."""
		return self._instance.CounterDrillDepth

	@counter_drill_depth.setter
	def counter_drill_depth(self, value):
		"""Gets or sets the Hole Wizard feature counterdrill depth."""
		self._instance.CounterDrillDepth = value

	@property
	def counter_drill_diameter(self):
		"""Gets or sets the Hole Wizard feature counterdrill diameter."""
		return self._instance.CounterDrillDiameter

	@counter_drill_diameter.setter
	def counter_drill_diameter(self, value):
		"""Gets or sets the Hole Wizard feature counterdrill diameter."""
		self._instance.CounterDrillDiameter = value

	@property
	def counter_sink_angle(self):
		"""Gets or sets the angle of the Hole Wizard countersink feature."""
		return self._instance.CounterSinkAngle

	@counter_sink_angle.setter
	def counter_sink_angle(self, value):
		"""Gets or sets the angle of the Hole Wizard countersink feature."""
		self._instance.CounterSinkAngle = value

	@property
	def counter_sink_diameter(self):
		"""Gets or sets the diameter of the Hole Wizard countersink feature."""
		return self._instance.CounterSinkDiameter

	@counter_sink_diameter.setter
	def counter_sink_diameter(self, value):
		"""Gets or sets the diameter of the Hole Wizard countersink feature."""
		self._instance.CounterSinkDiameter = value

	@property
	def depth(self):
		"""Gets or sets the Hole Wizard feature hole depth."""
		return self._instance.Depth

	@depth.setter
	def depth(self, value):
		"""Gets or sets the Hole Wizard feature hole depth."""
		self._instance.Depth = value

	@property
	def diameter(self):
		"""Gets or sets the diameter of the Hole Wizard feature."""
		return self._instance.Diameter

	@diameter.setter
	def diameter(self, value):
		"""Gets or sets the diameter of the Hole Wizard feature."""
		self._instance.Diameter = value

	@property
	def drill_angle(self):
		"""Gets or sets the drill angle for a Hole Wizard feature."""
		return self._instance.DrillAngle

	@drill_angle.setter
	def drill_angle(self, value):
		"""Gets or sets the drill angle for a Hole Wizard feature."""
		self._instance.DrillAngle = value

	@property
	def end_condition(self):
		"""Gets or sets the Hole Wizard feature end condition type."""
		return self._instance.EndCondition

	@end_condition.setter
	def end_condition(self, value):
		"""Gets or sets the Hole Wizard feature end condition type."""
		self._instance.EndCondition = value

	@property
	def face(self):
		"""Gets the end-condition face of the Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Face

	@face.setter
	def face(self, value):
		"""Gets the end-condition face of the Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Face = value

	@property
	def far_counter_sink_angle(self):
		"""Gets or sets the angle of the far side Hole Wizard countersink feature."""
		return self._instance.FarCounterSinkAngle

	@far_counter_sink_angle.setter
	def far_counter_sink_angle(self, value):
		"""Gets or sets the angle of the far side Hole Wizard countersink feature."""
		self._instance.FarCounterSinkAngle = value

	@property
	def far_counter_sink_diameter(self):
		"""Gets or sets the diameter of the far side Hole Wizard countersink feature."""
		return self._instance.FarCounterSinkDiameter

	@far_counter_sink_diameter.setter
	def far_counter_sink_diameter(self, value):
		"""Gets or sets the diameter of the far side Hole Wizard countersink feature."""
		self._instance.FarCounterSinkDiameter = value

	@property
	def far_side_counter_sink(self):
		"""Gets whether the far side option is selected for the Hole Wizard countersink feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.FarSideCounterSink

	@far_side_counter_sink.setter
	def far_side_counter_sink(self, value):
		"""Gets whether the far side option is selected for the Hole Wizard countersink feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.FarSideCounterSink = value

	@property
	def fastener_size(self):
		"""Gets the fastener size for this Wizard Hole feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.FastenerSize

	@fastener_size.setter
	def fastener_size(self, value):
		"""Gets the fastener size for this Wizard Hole feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.FastenerSize = value

	@property
	def fastener_type(self):
		"""Gets the fastener type for this Wizard Hole feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.FastenerType2

	@fastener_type.setter
	def fastener_type(self, value):
		"""Gets the fastener type for this Wizard Hole feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.FastenerType2 = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for the Hole Wizard feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for the Hole Wizard feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies that the Hole Wizard feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies that the Hole Wizard feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def head_clearance(self):
		"""Gets or sets the head clearance for this Wizard Hole feature."""
		return self._instance.HeadClearance

	@head_clearance.setter
	def head_clearance(self, value):
		"""Gets or sets the head clearance for this Wizard Hole feature."""
		self._instance.HeadClearance = value

	@property
	def head_clearance_type(self):
		"""Gets the type of head clearance for this countersink Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.HeadClearanceType

	@head_clearance_type.setter
	def head_clearance_type(self, value):
		"""Gets the type of head clearance for this countersink Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.HeadClearanceType = value

	@property
	def hole_depth(self):
		"""Gets or sets the Hole Wizard feature hole depth."""
		return self._instance.HoleDepth

	@hole_depth.setter
	def hole_depth(self, value):
		"""Gets or sets the Hole Wizard feature hole depth."""
		self._instance.HoleDepth = value

	@property
	def hole_diameter(self):
		"""Gets or sets the Hole Wizard feature hole diameter."""
		return self._instance.HoleDiameter

	@hole_diameter.setter
	def hole_diameter(self, value):
		"""Gets or sets the Hole Wizard feature hole diameter."""
		self._instance.HoleDiameter = value

	@property
	def hole_fit(self):
		"""Gets or sets the Hole Wizard feature fit information."""
		return self._instance.HoleFit

	@hole_fit.setter
	def hole_fit(self, value):
		"""Gets or sets the Hole Wizard feature fit information."""
		self._instance.HoleFit = value

	@property
	def i_face(self):
		"""Gets the end-condition face of the Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.IFace

	@i_face.setter
	def i_face(self, value):
		"""Gets the end-condition face of the Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.IFace = value

	@property
	def i_vertex(self):
		"""Gets the end-condition vertex for the Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.IVertex

	@i_vertex.setter
	def i_vertex(self, value):
		"""Gets the end-condition vertex for the Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.IVertex = value

	@property
	def length(self):
		"""Gets or sets the length of a Hole Wizard slot feature."""
		return self._instance.Length

	@length.setter
	def length(self, value):
		"""Gets or sets the length of a Hole Wizard slot feature."""
		self._instance.Length = value

	@property
	def major_diameter(self):
		"""Gets or sets the Hole Wizard feature major diameter for a tapered hole."""
		return self._instance.MajorDiameter

	@major_diameter.setter
	def major_diameter(self, value):
		"""Gets or sets the Hole Wizard feature major diameter for a tapered hole."""
		self._instance.MajorDiameter = value

	@property
	def mid_counter_sink_angle(self):
		"""Gets or sets the angle of the Hole Wizard middle countersink feature."""
		return self._instance.MidCounterSinkAngle

	@mid_counter_sink_angle.setter
	def mid_counter_sink_angle(self, value):
		"""Gets or sets the angle of the Hole Wizard middle countersink feature."""
		self._instance.MidCounterSinkAngle = value

	@property
	def mid_counter_sink_diameter(self):
		"""Gets or sets the diameter of the Hole Wizard middle countersink feature."""
		return self._instance.MidCounterSinkDiameter

	@mid_counter_sink_diameter.setter
	def mid_counter_sink_diameter(self, value):
		"""Gets or sets the diameter of the Hole Wizard middle countersink feature."""
		self._instance.MidCounterSinkDiameter = value

	@property
	def minor_diameter(self):
		"""Gets or sets the Hole Wizard feature minor diameter for a tapered hole."""
		return self._instance.MinorDiameter

	@minor_diameter.setter
	def minor_diameter(self, value):
		"""Gets or sets the Hole Wizard feature minor diameter for a tapered hole."""
		self._instance.MinorDiameter = value

	@property
	def near_counter_sink_angle(self):
		"""Gets or sets the angle of the near side Hole Wizard countersink feature."""
		return self._instance.NearCounterSinkAngle

	@near_counter_sink_angle.setter
	def near_counter_sink_angle(self, value):
		"""Gets or sets the angle of the near side Hole Wizard countersink feature."""
		self._instance.NearCounterSinkAngle = value

	@property
	def near_counter_sink_diameter(self):
		"""Gets or sets the diameter of the near side Hole Wizard countersink feature."""
		return self._instance.NearCounterSinkDiameter

	@near_counter_sink_diameter.setter
	def near_counter_sink_diameter(self, value):
		"""Gets or sets the diameter of the near side Hole Wizard countersink feature."""
		self._instance.NearCounterSinkDiameter = value

	@property
	def near_side_counter_sink(self):
		"""Gets whether the near side option is selected for the Hole Wizard countersink feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.NearSideCounterSink

	@near_side_counter_sink.setter
	def near_side_counter_sink(self, value):
		"""Gets whether the near side option is selected for the Hole Wizard countersink feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.NearSideCounterSink = value

	@property
	def offset_distance(self):
		"""Gets or sets the offset distance from the selected face, surface, or plane for this Hole Wizard feature."""
		return self._instance.OffsetDistance

	@offset_distance.setter
	def offset_distance(self, value):
		"""Gets or sets the offset distance from the selected face, surface, or plane for this Hole Wizard feature."""
		self._instance.OffsetDistance = value

	@property
	def propagate_feature_to_parts(self):
		"""Gets whether to propagate this assembly Hole Wizard feature to the parts that it affects in this model."""
		return self._instance.PropagateFeatureToParts

	@propagate_feature_to_parts.setter
	def propagate_feature_to_parts(self, value):
		"""Gets whether to propagate this assembly Hole Wizard feature to the parts that it affects in this model."""
		self._instance.PropagateFeatureToParts = value

	@property
	def reverse_direction(self):
		"""Gets or sets the direction of the Hole Wizard feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets the direction of the Hole Wizard feature."""
		self._instance.ReverseDirection = value

	@property
	def standard(self):
		"""Gets the design standard for this Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Standard

	@standard.setter
	def standard(self, value):
		"""Gets the design standard for this Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Standard = value

	@property
	def standard(self):
		"""Gets the design standard for this Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Standard2

	@standard.setter
	def standard(self, value):
		"""Gets the design standard for this Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Standard2 = value

	@property
	def tap_drill_depth(self):
		"""Gets or sets the Hole Wizard feature tap drill depth."""
		return self._instance.TapDrillDepth

	@tap_drill_depth.setter
	def tap_drill_depth(self, value):
		"""Gets or sets the Hole Wizard feature tap drill depth."""
		self._instance.TapDrillDepth = value

	@property
	def tap_drill_diameter(self):
		"""Gets or sets the Hole Wizard feature tap drill diameter."""
		return self._instance.TapDrillDiameter

	@tap_drill_diameter.setter
	def tap_drill_diameter(self, value):
		"""Gets or sets the Hole Wizard feature tap drill diameter."""
		self._instance.TapDrillDiameter = value

	@property
	def tap_type(self):
		"""Gets or sets the helicoil standard for this Hole Wizard feature."""
		return self._instance.TapType

	@tap_type.setter
	def tap_type(self, value):
		"""Gets or sets the helicoil standard for this Hole Wizard feature."""
		self._instance.TapType = value

	@property
	def thread_angle(self):
		"""Gets or sets the Hole Wizard feature thread angle."""
		return self._instance.ThreadAngle

	@thread_angle.setter
	def thread_angle(self, value):
		"""Gets or sets the Hole Wizard feature thread angle."""
		self._instance.ThreadAngle = value

	@property
	def thread_class(self):
		"""Gets or sets the thread class for this Hole Wizard feature.."""
		return self._instance.ThreadClass

	@thread_class.setter
	def thread_class(self, value):
		"""Gets or sets the thread class for this Hole Wizard feature.."""
		self._instance.ThreadClass = value

	@property
	def thread_depth(self):
		"""Gets or sets the Hole Wizard feature thread depth."""
		return self._instance.ThreadDepth

	@thread_depth.setter
	def thread_depth(self, value):
		"""Gets or sets the Hole Wizard feature thread depth."""
		self._instance.ThreadDepth = value

	@property
	def thread_diameter(self):
		"""Gets or sets the Hole Wizard feature thread diameter."""
		return self._instance.ThreadDiameter

	@thread_diameter.setter
	def thread_diameter(self, value):
		"""Gets or sets the Hole Wizard feature thread diameter."""
		self._instance.ThreadDiameter = value

	@property
	def thread_end_condition(self):
		"""Gets or sets the thread end condition for this Hole Wizard feature."""
		return self._instance.ThreadEndCondition

	@thread_end_condition.setter
	def thread_end_condition(self, value):
		"""Gets or sets the thread end condition for this Hole Wizard feature."""
		self._instance.ThreadEndCondition = value

	@property
	def thru_hole_depth(self):
		"""Gets or sets the Hole Wizard feature through hole depth."""
		return self._instance.ThruHoleDepth

	@thru_hole_depth.setter
	def thru_hole_depth(self, value):
		"""Gets or sets the Hole Wizard feature through hole depth."""
		self._instance.ThruHoleDepth = value

	@property
	def thru_hole_diameter(self):
		"""Gets or sets the Hole Wizard feature through-hole diameter."""
		return self._instance.ThruHoleDiameter

	@thru_hole_diameter.setter
	def thru_hole_diameter(self, value):
		"""Gets or sets the Hole Wizard feature through-hole diameter."""
		self._instance.ThruHoleDiameter = value

	@property
	def thru_tap_drill_depth(self):
		"""Gets or sets the Hole Wizard feature through-tap drill depth."""
		return self._instance.ThruTapDrillDepth

	@thru_tap_drill_depth.setter
	def thru_tap_drill_depth(self, value):
		"""Gets or sets the Hole Wizard feature through-tap drill depth."""
		self._instance.ThruTapDrillDepth = value

	@property
	def thru_tap_drill_diameter(self):
		"""Gets or sets the Hole Wizard feature through-tap drill diameter."""
		return self._instance.ThruTapDrillDiameter

	@thru_tap_drill_diameter.setter
	def thru_tap_drill_diameter(self, value):
		"""Gets or sets the Hole Wizard feature through-tap drill diameter."""
		self._instance.ThruTapDrillDiameter = value

	@property
	def type(self):
		"""Gets the Hole Wizard feature type.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the Hole Wizard feature type.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Type = value

	@property
	def vertex(self):
		"""Gets the end-condition vertex for the Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Vertex

	@vertex.setter
	def vertex(self, value):
		"""Gets the end-condition vertex for the Hole Wizard feature.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Vertex = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define the Hole Wizard feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define the Hole Wizard feature."""
		self._instance.AccessSelections = value

	@property
	def change_standard(self):
		"""Sets the standard for all of the parameters of the Hole Wizard feature that are driven by the database."""
		return self._instance.ChangeStandard

	@change_standard.setter
	def change_standard(self, value):
		"""Sets the standard for all of the parameters of the Hole Wizard feature that are driven by the database."""
		self._instance.ChangeStandard = value

	@property
	def get_end_condition_reference(self):
		"""Gets the reference entity that defines the end condition for this Hole Wizard feature."""
		return self._instance.GetEndConditionReference

	@get_end_condition_reference.setter
	def get_end_condition_reference(self, value):
		"""Gets the reference entity that defines the end condition for this Hole Wizard feature."""
		self._instance.GetEndConditionReference = value

	@property
	def get_feature_scope_bodies_count(self):
		"""Gets the number of solid bodies affected by the Hole Wizard feature in a multibody part."""
		return self._instance.GetFeatureScopeBodiesCount

	@get_feature_scope_bodies_count.setter
	def get_feature_scope_bodies_count(self, value):
		"""Gets the number of solid bodies affected by the Hole Wizard feature in a multibody part."""
		self._instance.GetFeatureScopeBodiesCount = value

	@property
	def get_sketch_point_count(self):
		"""Gets the number of center-hole sketch points in this Hole Wizard feature."""
		return self._instance.GetSketchPointCount

	@get_sketch_point_count.setter
	def get_sketch_point_count(self, value):
		"""Gets the number of center-hole sketch points in this Hole Wizard feature."""
		self._instance.GetSketchPointCount = value

	@property
	def get_sketch_points(self):
		"""Gets the center-hole sketch points in this Hole Wizard feature."""
		return self._instance.GetSketchPoints

	@get_sketch_points.setter
	def get_sketch_points(self, value):
		"""Gets the center-hole sketch points in this Hole Wizard feature."""
		self._instance.GetSketchPoints = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections used to define the Hole Wizard feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections used to define the Hole Wizard feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_feature_scope_bodies(self):
		"""Gets the solid bodies that the Hole Wizard feature affects in a multibody part."""
		return self._instance.IGetFeatureScopeBodies

	@i_get_feature_scope_bodies.setter
	def i_get_feature_scope_bodies(self, value):
		"""Gets the solid bodies that the Hole Wizard feature affects in a multibody part."""
		self._instance.IGetFeatureScopeBodies = value

	@property
	def i_get_sketch_points(self):
		"""Gets the center-hole sketch points in this Hole Wizard feature."""
		return self._instance.IGetSketchPoints

	@i_get_sketch_points.setter
	def i_get_sketch_points(self, value):
		"""Gets the center-hole sketch points in this Hole Wizard feature."""
		self._instance.IGetSketchPoints = value

	@property
	def initialize_hole(self):
		"""Initializes a newly created Hole Wizard feature data object."""
		return self._instance.InitializeHole

	@initialize_hole.setter
	def initialize_hole(self, value):
		"""Initializes a newly created Hole Wizard feature data object."""
		self._instance.InitializeHole = value

	@property
	def i_set_feature_scope_bodies(self):
		"""Sets the solid bodies that the Hole Wizard feature affects in the multibody part."""
		return self._instance.ISetFeatureScopeBodies

	@i_set_feature_scope_bodies.setter
	def i_set_feature_scope_bodies(self, value):
		"""Sets the solid bodies that the Hole Wizard feature affects in the multibody part."""
		self._instance.ISetFeatureScopeBodies = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections used to define the Hole Wizard feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections used to define the Hole Wizard feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_end_condition_reference(self):
		"""Sets the reference entity that defines the end condition for this Hole Wizard feature."""
		return self._instance.SetEndConditionReference

	@set_end_condition_reference.setter
	def set_end_condition_reference(self, value):
		"""Sets the reference entity that defines the end condition for this Hole Wizard feature."""
		self._instance.SetEndConditionReference = value

