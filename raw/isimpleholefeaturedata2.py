# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.html
class ISimpleHoleFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def assembly_feature_scope(self):
		"""Gets or sets whether to use scope for this assembly simple hole feature."""
		return self._instance.AssemblyFeatureScope

	@assembly_feature_scope.setter
	def assembly_feature_scope(self, value):
		"""Gets or sets whether to use scope for this assembly simple hole feature."""
		self._instance.AssemblyFeatureScope = value

	@property
	def auto_select(self):
		"""Gets or sets whether to automatically select all or only specific bodies for the simple hole feature to affect in a multibody body."""
		return self._instance.AutoSelect

	@auto_select.setter
	def auto_select(self, value):
		"""Gets or sets whether to automatically select all or only specific bodies for the simple hole feature to affect in a multibody body."""
		self._instance.AutoSelect = value

	@property
	def auto_select_components(self):
		"""Gets or sets whether to auto-select all components that this assembly simple hole feature affects in model."""
		return self._instance.AutoSelectComponents

	@auto_select_components.setter
	def auto_select_components(self, value):
		"""Gets or sets whether to auto-select all components that this assembly simple hole feature affects in model."""
		self._instance.AutoSelectComponents = value

	@property
	def depth(self):
		"""Gets or sets the depth of this simple hole feature."""
		return self._instance.Depth

	@depth.setter
	def depth(self, value):
		"""Gets or sets the depth of this simple hole feature."""
		self._instance.Depth = value

	@property
	def diameter(self):
		"""Gets or sets the diameter of this simple hole feature"""
		return self._instance.Diameter

	@diameter.setter
	def diameter(self, value):
		"""Gets or sets the diameter of this simple hole feature"""
		self._instance.Diameter = value

	@property
	def draft_angle(self):
		"""Gets or sets the draft angle for this simple hole feature."""
		return self._instance.DraftAngle

	@draft_angle.setter
	def draft_angle(self, value):
		"""Gets or sets the draft angle for this simple hole feature."""
		self._instance.DraftAngle = value

	@property
	def draft_outward(self):
		"""Gets or sets whether to draft the simple hole feature outward."""
		return self._instance.DraftOutward

	@draft_outward.setter
	def draft_outward(self, value):
		"""Gets or sets whether to draft the simple hole feature outward."""
		self._instance.DraftOutward = value

	@property
	def draft_while_extruding(self):
		"""Gets or sets whether to draft the simple hole feature while extruding."""
		return self._instance.DraftWhileExtruding

	@draft_while_extruding.setter
	def draft_while_extruding(self, value):
		"""Gets or sets whether to draft the simple hole feature while extruding."""
		self._instance.DraftWhileExtruding = value

	@property
	def face(self):
		"""Gets or sets the end-condition face of this simple hole feature."""
		return self._instance.Face

	@face.setter
	def face(self, value):
		"""Gets or sets the end-condition face of this simple hole feature."""
		self._instance.Face = value

	@property
	def feature_scope(self):
		"""Gets or sets whether to use scope for the simple hole feature in a multibody part."""
		return self._instance.FeatureScope

	@feature_scope.setter
	def feature_scope(self, value):
		"""Gets or sets whether to use scope for the simple hole feature in a multibody part."""
		self._instance.FeatureScope = value

	@property
	def feature_scope_bodies(self):
		"""Gets or sets the solid bodies that the simple hole feature affects in a multibody part."""
		return self._instance.FeatureScopeBodies

	@feature_scope_bodies.setter
	def feature_scope_bodies(self, value):
		"""Gets or sets the solid bodies that the simple hole feature affects in a multibody part."""
		self._instance.FeatureScopeBodies = value

	@property
	def i_face(self):
		"""Gets or sets the end-condition face of this simple hole feature."""
		return self._instance.IFace

	@i_face.setter
	def i_face(self, value):
		"""Gets or sets the end-condition face of this simple hole feature."""
		self._instance.IFace = value

	@property
	def i_vertex(self):
		"""Gets or sets the end-condition vertex of this simple hole feature."""
		return self._instance.IVertex

	@i_vertex.setter
	def i_vertex(self, value):
		"""Gets or sets the end-condition vertex of this simple hole feature."""
		self._instance.IVertex = value

	@property
	def propagate_feature_to_parts(self):
		"""Gets whether to propagate this assembly simple hole feature to the parts that it affects in this model."""
		return self._instance.PropagateFeatureToParts

	@propagate_feature_to_parts.setter
	def propagate_feature_to_parts(self, value):
		"""Gets whether to propagate this assembly simple hole feature to the parts that it affects in this model."""
		self._instance.PropagateFeatureToParts = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of the cut."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of the cut."""
		self._instance.ReverseDirection = value

	@property
	def reverse_offset(self):
		"""Gets or sets whether to reverse the offset from the surface."""
		return self._instance.ReverseOffset

	@reverse_offset.setter
	def reverse_offset(self, value):
		"""Gets or sets whether to reverse the offset from the surface."""
		self._instance.ReverseOffset = value

	@property
	def surface_offset(self):
		"""Gets or sets the depth of this simple hole feature offset from the surface."""
		return self._instance.SurfaceOffset

	@surface_offset.setter
	def surface_offset(self, value):
		"""Gets or sets the depth of this simple hole feature offset from the surface."""
		self._instance.SurfaceOffset = value

	@property
	def translate_surface(self):
		"""Gets or sets whether to translate the surface of this simple hole."""
		return self._instance.TranslateSurface

	@translate_surface.setter
	def translate_surface(self, value):
		"""Gets or sets whether to translate the surface of this simple hole."""
		self._instance.TranslateSurface = value

	@property
	def type(self):
		"""Gets or sets the end-condition of the simple hole."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the end-condition of the simple hole."""
		self._instance.Type = value

	@property
	def vertex(self):
		"""Gets or sets the end-condition vertex of this simple hole feature."""
		return self._instance.Vertex

	@vertex.setter
	def vertex(self, value):
		"""Gets or sets the end-condition vertex of this simple hole feature."""
		self._instance.Vertex = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define the simple hole feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define the simple hole feature."""
		self._instance.AccessSelections = value

	@property
	def get_direction_reference(self):
		"""Gets the direction of the cut extrude for this simple hole feature."""
		return self._instance.GetDirectionReference

	@get_direction_reference.setter
	def get_direction_reference(self, value):
		"""Gets the direction of the cut extrude for this simple hole feature."""
		self._instance.GetDirectionReference = value

	@property
	def get_end_condition_reference(self):
		"""Gets the reference entity that defines the end condition for this simple hole feature."""
		return self._instance.GetEndConditionReference

	@get_end_condition_reference.setter
	def get_end_condition_reference(self, value):
		"""Gets the reference entity that defines the end condition for this simple hole feature."""
		self._instance.GetEndConditionReference = value

	@property
	def get_feature_scope_bodies_count(self):
		"""Gets the number of solid bodies affected by the simple hole feature in a multibody part."""
		return self._instance.GetFeatureScopeBodiesCount

	@get_feature_scope_bodies_count.setter
	def get_feature_scope_bodies_count(self, value):
		"""Gets the number of solid bodies affected by the simple hole feature in a multibody part."""
		self._instance.GetFeatureScopeBodiesCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections used to define the simple hole feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections used to define the simple hole feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_feature_scope_bodies(self):
		"""Gets the solid bodies that the simple hole feature affects in a multibody part."""
		return self._instance.IGetFeatureScopeBodies

	@i_get_feature_scope_bodies.setter
	def i_get_feature_scope_bodies(self, value):
		"""Gets the solid bodies that the simple hole feature affects in a multibody part."""
		self._instance.IGetFeatureScopeBodies = value

	@property
	def i_set_feature_scope_bodies(self):
		"""Sets the solid bodies that the simple hole feature affects in the multibody part."""
		return self._instance.ISetFeatureScopeBodies

	@i_set_feature_scope_bodies.setter
	def i_set_feature_scope_bodies(self, value):
		"""Sets the solid bodies that the simple hole feature affects in the multibody part."""
		self._instance.ISetFeatureScopeBodies = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define the simple hole feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define the simple hole feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_direction_reference(self):
		"""Sets the direction of the cut extrude for this simple hole feature."""
		return self._instance.SetDirectionReference

	@set_direction_reference.setter
	def set_direction_reference(self, value):
		"""Sets the direction of the cut extrude for this simple hole feature."""
		self._instance.SetDirectionReference = value

	@property
	def set_end_condition_reference(self):
		"""Sets the reference entity that defines the end condition for this simple hole feature."""
		return self._instance.SetEndConditionReference

	@set_end_condition_reference.setter
	def set_end_condition_reference(self, value):
		"""Sets the reference entity that defines the end condition for this simple hole feature."""
		self._instance.SetEndConditionReference = value

