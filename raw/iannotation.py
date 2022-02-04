# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html
class IAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def annotation_view(self):
		"""Gets the annotation view for this annotation."""
		# return self._instance.AnnotationView
		raise NotImplemented

	@property
	def bent_leader_length(self):
		"""Gets or sets the length of the bent leader for this annotation."""
		return self._instance.BentLeaderLength

	@bent_leader_length.setter
	def bent_leader_length(self, value):
		"""Gets or sets the length of the bent leader for this annotation."""
		self._instance.BentLeaderLength = value

	@property
	def color(self):
		"""Gets or sets the color of this annotation. Annotation color is supported only in SOLIDWORKS drawings."""
		return self._instance.Color

	@color.setter
	def color(self, value):
		"""Gets or sets the color of this annotation. Annotation color is supported only in SOLIDWORKS drawings."""
		self._instance.Color = value

	@property
	def frame_line_style(self):
		"""Gets or sets the frame's line style for this annotation."""
		return self._instance.FrameLineStyle

	@frame_line_style.setter
	def frame_line_style(self, value):
		"""Gets or sets the frame's line style for this annotation."""
		self._instance.FrameLineStyle = value

	@property
	def frame_thickness(self):
		"""Gets or sets the frame's line thickness for this annotation."""
		return self._instance.FrameThickness

	@frame_thickness.setter
	def frame_thickness(self, value):
		"""Gets or sets the frame's line thickness for this annotation."""
		self._instance.FrameThickness = value

	@property
	def frame_thickness_custom(self):
		"""Gets or sets the frame's line thickness for this annotation."""
		return self._instance.FrameThicknessCustom

	@frame_thickness_custom.setter
	def frame_thickness_custom(self, value):
		"""Gets or sets the frame's line thickness for this annotation."""
		self._instance.FrameThicknessCustom = value

	@property
	def layer(self):
		"""Gets or sets the layer used by this annotation. Layers are supported only in SOLIDWORKSdrawings."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""Gets or sets the layer used by this annotation. Layers are supported only in SOLIDWORKSdrawings."""
		self._instance.Layer = value

	@property
	def layer_override(self):
		"""Gets or sets whether the annotation has properties that override the default properties of the layer."""
		return self._instance.LayerOverride

	@layer_override.setter
	def layer_override(self, value):
		"""Gets or sets whether the annotation has properties that override the default properties of the layer."""
		self._instance.LayerOverride = value

	@property
	def leader_line_style(self):
		"""Gets or sets the leader's lines style for this annotation."""
		return self._instance.LeaderLineStyle

	@leader_line_style.setter
	def leader_line_style(self, value):
		"""Gets or sets the leader's lines style for this annotation."""
		self._instance.LeaderLineStyle = value

	@property
	def leader_thickness(self):
		"""Gets or sets the leader's line thickness for this annotation."""
		return self._instance.LeaderThickness

	@leader_thickness.setter
	def leader_thickness(self, value):
		"""Gets or sets the leader's line thickness for this annotation."""
		self._instance.LeaderThickness = value

	@property
	def leader_thickness_custom(self):
		"""Gets or sets the leader's custom line thickness for this annotation."""
		return self._instance.LeaderThicknessCustom

	@leader_thickness_custom.setter
	def leader_thickness_custom(self, value):
		"""Gets or sets the leader's custom line thickness for this annotation."""
		self._instance.LeaderThicknessCustom = value

	@property
	def owner(self):
		"""Gets the owner of this annotation.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Owner

	@owner.setter
	def owner(self, value):
		"""Gets the owner of this annotation.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Owner = value

	@property
	def owner_type(self):
		"""Gets the type of owner of this annotation.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.OwnerType

	@owner_type.setter
	def owner_type(self, value):
		"""Gets the type of owner of this annotation.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.OwnerType = value

	@property
	def style(self):
		"""Gets or sets the line style for this annotation."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets the line style for this annotation."""
		self._instance.Style = value

	@property
	def use_doc_disp_frame(self):
		"""Gets or sets whether to use the document's frame's line style and thickness or a specified line style and thickness for this annotation."""
		return self._instance.UseDocDispFrame

	@use_doc_disp_frame.setter
	def use_doc_disp_frame(self, value):
		"""Gets or sets whether to use the document's frame's line style and thickness or a specified line style and thickness for this annotation."""
		self._instance.UseDocDispFrame = value

	@property
	def use_doc_disp_leader(self):
		"""Gets or sets whether to use the document's leader's line style and thickness or a specified line style and thickness for this annotation."""
		return self._instance.UseDocDispLeader

	@use_doc_disp_leader.setter
	def use_doc_disp_leader(self, value):
		"""Gets or sets whether to use the document's leader's line style and thickness or a specified line style and thickness for this annotation."""
		self._instance.UseDocDispLeader = value

	@property
	def visible(self):
		"""Gets or sets the visibility state of this annotation."""
		return self._instance.Visible

	@visible.setter
	def visible(self, value):
		"""Gets or sets the visibility state of this annotation."""
		self._instance.Visible = value

	@property
	def width(self):
		"""Gets or sets the line width enumeration value for this annotation."""
		return self._instance.Width

	@width.setter
	def width(self, value):
		"""Gets or sets the line width enumeration value for this annotation."""
		self._instance.Width = value

	@property
	def add_or_update_style(self):
		"""Adds or updates the annotation linked to the specified style."""
		return self._instance.AddOrUpdateStyle

	@add_or_update_style.setter
	def add_or_update_style(self, value):
		"""Adds or updates the annotation linked to the specified style."""
		self._instance.AddOrUpdateStyle = value

	@property
	def apply_default_style_attributes(self):
		"""Applies the default style attribute to this annotation."""
		return self._instance.ApplyDefaultStyleAttributes

	@apply_default_style_attributes.setter
	def apply_default_style_attributes(self, value):
		"""Applies the default style attribute to this annotation."""
		self._instance.ApplyDefaultStyleAttributes = value

	@property
	def can_show_in_annotation_view(self):
		"""Gets whether this annotation can be shown in the specified annotation view."""
		return self._instance.CanShowInAnnotationView

	@can_show_in_annotation_view.setter
	def can_show_in_annotation_view(self, value):
		"""Gets whether this annotation can be shown in the specified annotation view."""
		self._instance.CanShowInAnnotationView = value

	@property
	def can_show_in_multiple_annotation_views(self):
		"""Gets whether this annotation can be shown in multiple annotation views."""
		return self._instance.CanShowInMultipleAnnotationViews

	@can_show_in_multiple_annotation_views.setter
	def can_show_in_multiple_annotation_views(self, value):
		"""Gets whether this annotation can be shown in multiple annotation views."""
		self._instance.CanShowInMultipleAnnotationViews = value

	@property
	def check_spelling(self):
		"""Spell checks the text in this annotation."""
		return self._instance.CheckSpelling

	@check_spelling.setter
	def check_spelling(self, value):
		"""Spell checks the text in this annotation."""
		self._instance.CheckSpelling = value

	@property
	def convert_to_multi_jog(self):
		"""Converts a note with a leader to a note with a multi-jog leader."""
		return self._instance.ConvertToMultiJog

	@convert_to_multi_jog.setter
	def convert_to_multi_jog(self, value):
		"""Converts a note with a leader to a note with a multi-jog leader."""
		self._instance.ConvertToMultiJog = value

	@property
	def delete_style(self):
		"""Deletes the specified style."""
		return self._instance.DeleteStyle

	@delete_style.setter
	def delete_style(self, value):
		"""Deletes the specified style."""
		self._instance.DeleteStyle = value

	@property
	def de_select(self):
		"""Deselects this annotation."""
		return self._instance.DeSelect

	@de_select.setter
	def de_select(self, value):
		"""Deselects this annotation."""
		self._instance.DeSelect = value

	@property
	def get_arrow_head_count(self):
		"""Gets the number of arrowheads on this symbol."""
		return self._instance.GetArrowHeadCount

	@get_arrow_head_count.setter
	def get_arrow_head_count(self, value):
		"""Gets the number of arrowheads on this symbol."""
		self._instance.GetArrowHeadCount = value

	@property
	def get_arrow_head_size_at_index(self):
		"""Gets the arrow head size of the specified leader on this annotation."""
		return self._instance.GetArrowHeadSizeAtIndex

	@get_arrow_head_size_at_index.setter
	def get_arrow_head_size_at_index(self, value):
		"""Gets the arrow head size of the specified leader on this annotation."""
		self._instance.GetArrowHeadSizeAtIndex = value

	@property
	def get_arrow_head_style_at_index(self):
		"""Gets the arrow head style of a specific leader on this annotation."""
		return self._instance.GetArrowHeadStyleAtIndex

	@get_arrow_head_style_at_index.setter
	def get_arrow_head_style_at_index(self, value):
		"""Gets the arrow head style of a specific leader on this annotation."""
		self._instance.GetArrowHeadStyleAtIndex = value

	@property
	def get_attached_entities(self):
		"""Gets the entities to which this annotation is attached."""
		return self._instance.GetAttachedEntities3

	@get_attached_entities.setter
	def get_attached_entities(self, value):
		"""Gets the entities to which this annotation is attached."""
		self._instance.GetAttachedEntities3 = value

	@property
	def get_attached_entity_count(self):
		"""Gets the number of entities to which this annotation is attached."""
		return self._instance.GetAttachedEntityCount3

	@get_attached_entity_count.setter
	def get_attached_entity_count(self, value):
		"""Gets the number of entities to which this annotation is attached."""
		self._instance.GetAttachedEntityCount3 = value

	@property
	def get_attached_entity_types(self):
		"""Gets the types of entities attached to this annotation."""
		return self._instance.GetAttachedEntityTypes

	@get_attached_entity_types.setter
	def get_attached_entity_types(self, value):
		"""Gets the types of entities attached to this annotation."""
		self._instance.GetAttachedEntityTypes = value

	@property
	def get_dashed_leader(self):
		"""Gets whether this leader is a dashed line or a solid line."""
		return self._instance.GetDashedLeader

	@get_dashed_leader.setter
	def get_dashed_leader(self, value):
		"""Gets whether this leader is a dashed line or a solid line."""
		self._instance.GetDashedLeader = value

	@property
	def get_dim_xpert_feature(self):
		"""Gets the DimXpert feature associated with this annotation."""
		return self._instance.GetDimXpertFeature

	@get_dim_xpert_feature.setter
	def get_dim_xpert_feature(self, value):
		"""Gets the DimXpert feature associated with this annotation."""
		self._instance.GetDimXpertFeature = value

	@property
	def get_dim_xpert_name(self):
		"""Gets the DimXpert name for this annotation."""
		return self._instance.GetDimXpertName

	@get_dim_xpert_name.setter
	def get_dim_xpert_name(self, value):
		"""Gets the DimXpert name for this annotation."""
		self._instance.GetDimXpertName = value

	@property
	def get_display_data(self):
		"""Gets the display data for this annotation."""
		return self._instance.GetDisplayData

	@get_display_data.setter
	def get_display_data(self, value):
		"""Gets the display data for this annotation."""
		self._instance.GetDisplayData = value

	@property
	def get_flip_plane_transform(self):
		"""Gets the transformation matrix of the annotation plane in the opposite direction."""
		return self._instance.GetFlipPlaneTransform

	@get_flip_plane_transform.setter
	def get_flip_plane_transform(self, value):
		"""Gets the transformation matrix of the annotation plane in the opposite direction."""
		self._instance.GetFlipPlaneTransform = value

	@property
	def get_leader_all_around(self):
		"""Gets the setting for all-around symbol display of this annotation."""
		return self._instance.GetLeaderAllAround

	@get_leader_all_around.setter
	def get_leader_all_around(self, value):
		"""Gets the setting for all-around symbol display of this annotation."""
		self._instance.GetLeaderAllAround = value

	@property
	def get_leader_count(self):
		"""Gets the number of leaders on this annotation."""
		return self._instance.GetLeaderCount

	@get_leader_count.setter
	def get_leader_count(self, value):
		"""Gets the number of leaders on this annotation."""
		self._instance.GetLeaderCount = value

	@property
	def get_leader_perpendicular(self):
		"""Gets the perpendicular bent leader display setting for this annotation."""
		return self._instance.GetLeaderPerpendicular

	@get_leader_perpendicular.setter
	def get_leader_perpendicular(self, value):
		"""Gets the perpendicular bent leader display setting for this annotation."""
		self._instance.GetLeaderPerpendicular = value

	@property
	def get_leader_points_at_index(self):
		"""Gets coordinate information about a specified leader on this annotation."""
		return self._instance.GetLeaderPointsAtIndex

	@get_leader_points_at_index.setter
	def get_leader_points_at_index(self, value):
		"""Gets coordinate information about a specified leader on this annotation."""
		self._instance.GetLeaderPointsAtIndex = value

	@property
	def get_leader_side(self):
		"""Gets the leader attachment side setting for this annotation."""
		return self._instance.GetLeaderSide

	@get_leader_side.setter
	def get_leader_side(self, value):
		"""Gets the leader attachment side setting for this annotation."""
		self._instance.GetLeaderSide = value

	@property
	def get_leader_style(self):
		"""Gets the style of this leader."""
		return self._instance.GetLeaderStyle

	@get_leader_style.setter
	def get_leader_style(self, value):
		"""Gets the style of this leader."""
		self._instance.GetLeaderStyle = value

	@property
	def get_multi_jog_leader_count(self):
		"""Gets the number of multi-jog leaders on this annotation."""
		return self._instance.GetMultiJogLeaderCount

	@get_multi_jog_leader_count.setter
	def get_multi_jog_leader_count(self, value):
		"""Gets the number of multi-jog leaders on this annotation."""
		self._instance.GetMultiJogLeaderCount = value

	@property
	def get_multi_jog_leaders(self):
		"""Gets the multi-jog leaders on this annotation."""
		return self._instance.GetMultiJogLeaders

	@get_multi_jog_leaders.setter
	def get_multi_jog_leaders(self, value):
		"""Gets the multi-jog leaders on this annotation."""
		self._instance.GetMultiJogLeaders = value

	@property
	def get_name(self):
		"""Gets the name of this annotation."""
		return self._instance.GetName

	@get_name.setter
	def get_name(self, value):
		"""Gets the name of this annotation."""
		self._instance.GetName = value

	@property
	def get_next(self):
		"""Gets the next annotation."""
		return self._instance.GetNext3

	@get_next.setter
	def get_next(self, value):
		"""Gets the next annotation."""
		self._instance.GetNext3 = value

	@property
	def get_paragraphs(self):
		"""Gets the paragraphs in this note annotation."""
		return self._instance.GetParagraphs

	@get_paragraphs.setter
	def get_paragraphs(self, value):
		"""Gets the paragraphs in this note annotation."""
		self._instance.GetParagraphs = value

	@property
	def get_plane(self):
		"""Gets the rotation matrix of the annotation relative to the X-Y plane of the model."""
		return self._instance.GetPlane

	@get_plane.setter
	def get_plane(self, value):
		"""Gets the rotation matrix of the annotation relative to the X-Y plane of the model."""
		self._instance.GetPlane = value

	@property
	def get_p_m_i_data(self):
		"""Gets the Product and Manufacturing Information (PMI) feature data object for this STEP 242 annotation."""
		return self._instance.GetPMIData

	@get_p_m_i_data.setter
	def get_p_m_i_data(self, value):
		"""Gets the Product and Manufacturing Information (PMI) feature data object for this STEP 242 annotation."""
		self._instance.GetPMIData = value

	@property
	def get_p_m_i_type(self):
		"""Gets the type of Product and Manufacturing Information (PMI) associated with this STEP 242 annotation."""
		return self._instance.GetPMIType

	@get_p_m_i_type.setter
	def get_p_m_i_type(self, value):
		"""Gets the type of Product and Manufacturing Information (PMI) associated with this STEP 242 annotation."""
		self._instance.GetPMIType = value

	@property
	def get_position(self):
		"""Gets the position of this annotation."""
		return self._instance.GetPosition

	@get_position.setter
	def get_position(self, value):
		"""Gets the position of this annotation."""
		self._instance.GetPosition = value

	@property
	def get_smart_arrow_head_style(self):
		"""Gets the setting for smart arrowhead style for this annotation."""
		return self._instance.GetSmartArrowHeadStyle

	@get_smart_arrow_head_style.setter
	def get_smart_arrow_head_style(self, value):
		"""Gets the setting for smart arrowhead style for this annotation."""
		self._instance.GetSmartArrowHeadStyle = value

	@property
	def get_specific_annotation(self):
		"""Gets the specific underlying object associated with this annotation."""
		return self._instance.GetSpecificAnnotation

	@get_specific_annotation.setter
	def get_specific_annotation(self, value):
		"""Gets the specific underlying object associated with this annotation."""
		self._instance.GetSpecificAnnotation = value

	@property
	def get_style_name(self):
		"""Gets the name of the style applied to this annotation."""
		return self._instance.GetStyleName

	@get_style_name.setter
	def get_style_name(self, value):
		"""Gets the name of the style applied to this annotation."""
		self._instance.GetStyleName = value

	@property
	def get_text_format(self):
		"""Gets the text format for the specified text in this annotation."""
		return self._instance.GetTextFormat

	@get_text_format.setter
	def get_text_format(self, value):
		"""Gets the text format for the specified text in this annotation."""
		self._instance.GetTextFormat = value

	@property
	def get_text_format_count(self):
		"""Gets the number of text formats for this annotation."""
		return self._instance.GetTextFormatCount

	@get_text_format_count.setter
	def get_text_format_count(self, value):
		"""Gets the number of text formats for this annotation."""
		self._instance.GetTextFormatCount = value

	@property
	def get_type(self):
		"""Gets the type of the annotation."""
		return self._instance.GetType

	@get_type.setter
	def get_type(self, value):
		"""Gets the type of the annotation."""
		self._instance.GetType = value

	@property
	def get_use_doc_text_format(self):
		"""Gets whether SOLIDWORKS is currently using the document default text format setting for this annotation."""
		return self._instance.GetUseDocTextFormat

	@get_use_doc_text_format.setter
	def get_use_doc_text_format(self, value):
		"""Gets whether SOLIDWORKS is currently using the document default text format setting for this annotation."""
		self._instance.GetUseDocTextFormat = value

	@property
	def get_visual_properties(self):
		"""Gets the visual properties of this annotation."""
		return self._instance.GetVisualProperties

	@get_visual_properties.setter
	def get_visual_properties(self, value):
		"""Gets the visual properties of this annotation."""
		self._instance.GetVisualProperties = value

	@property
	def i_get_attached_entity_types(self):
		"""Gets the types of all entities attached to this annotation."""
		return self._instance.IGetAttachedEntityTypes

	@i_get_attached_entity_types.setter
	def i_get_attached_entity_types(self, value):
		"""Gets the types of all entities attached to this annotation."""
		self._instance.IGetAttachedEntityTypes = value

	@property
	def i_get_display_data(self):
		"""Gets the display data for the annotation."""
		return self._instance.IGetDisplayData

	@i_get_display_data.setter
	def i_get_display_data(self, value):
		"""Gets the display data for the annotation."""
		self._instance.IGetDisplayData = value

	@property
	def i_get_leader_points_at_index(self):
		"""Gets coordinate information about a specified leader on this annotation."""
		return self._instance.IGetLeaderPointsAtIndex

	@i_get_leader_points_at_index.setter
	def i_get_leader_points_at_index(self, value):
		"""Gets coordinate information about a specified leader on this annotation."""
		self._instance.IGetLeaderPointsAtIndex = value

	@property
	def i_get_multi_jog_leaders(self):
		"""Gets the multi-jog leaders on this annotation."""
		return self._instance.IGetMultiJogLeaders

	@i_get_multi_jog_leaders.setter
	def i_get_multi_jog_leaders(self, value):
		"""Gets the multi-jog leaders on this annotation."""
		self._instance.IGetMultiJogLeaders = value

	@property
	def i_get_position(self):
		"""Gets the position of this annotation."""
		return self._instance.IGetPosition

	@i_get_position.setter
	def i_get_position(self, value):
		"""Gets the position of this annotation."""
		self._instance.IGetPosition = value

	@property
	def i_get_specific_annotation(self):
		"""Gets the specific underlying object associated with this annotation."""
		return self._instance.IGetSpecificAnnotation

	@i_get_specific_annotation.setter
	def i_get_specific_annotation(self, value):
		"""Gets the specific underlying object associated with this annotation."""
		self._instance.IGetSpecificAnnotation = value

	@property
	def i_get_text_format(self):
		"""Gets the text format for the specified text in this annotation."""
		return self._instance.IGetTextFormat

	@i_get_text_format.setter
	def i_get_text_format(self, value):
		"""Gets the text format for the specified text in this annotation."""
		self._instance.IGetTextFormat = value

	@property
	def i_get_visual_properties(self):
		"""Gets the visual properties of this annotation."""
		return self._instance.IGetVisualProperties

	@i_get_visual_properties.setter
	def i_get_visual_properties(self, value):
		"""Gets the visual properties of this annotation."""
		self._instance.IGetVisualProperties = value

	@property
	def is_dangling(self):
		"""Gets whether this annotation is dangling."""
		return self._instance.IsDangling

	@is_dangling.setter
	def is_dangling(self, value):
		"""Gets whether this annotation is dangling."""
		self._instance.IsDangling = value

	@property
	def is_dim_xpert(self):
		"""Gets whether the annotation is a DimXpert annotation."""
		return self._instance.IsDimXpert

	@is_dim_xpert.setter
	def is_dim_xpert(self, value):
		"""Gets whether the annotation is a DimXpert annotation."""
		self._instance.IsDimXpert = value

	@property
	def i_set_attached_entities(self):
		"""Attaches this annotation to the specified entities."""
		return self._instance.ISetAttachedEntities

	@i_set_attached_entities.setter
	def i_set_attached_entities(self, value):
		"""Attaches this annotation to the specified entities."""
		self._instance.ISetAttachedEntities = value

	@property
	def i_set_text_format(self):
		"""Sets the text format information for the specified text within this annotation."""
		return self._instance.ISetTextFormat

	@i_set_text_format.setter
	def i_set_text_format(self, value):
		"""Sets the text format information for the specified text within this annotation."""
		self._instance.ISetTextFormat = value

	@property
	def load_style(self):
		"""Loads the specified style."""
		return self._instance.LoadStyle

	@load_style.setter
	def load_style(self, value):
		"""Loads the specified style."""
		self._instance.LoadStyle = value

	@property
	def save_style(self):
		"""Saves the specified style."""
		return self._instance.SaveStyle

	@save_style.setter
	def save_style(self, value):
		"""Saves the specified style."""
		self._instance.SaveStyle = value

	@property
	def select(self):
		"""Selects this annotation and marks it."""
		return self._instance.Select3

	@select.setter
	def select(self, value):
		"""Selects this annotation and marks it."""
		self._instance.Select3 = value

	@property
	def set_arrow_head_size_at_index(self):
		"""Sets the size of the arrow head of the specified leader on this annotation."""
		return self._instance.SetArrowHeadSizeAtIndex

	@set_arrow_head_size_at_index.setter
	def set_arrow_head_size_at_index(self, value):
		"""Sets the size of the arrow head of the specified leader on this annotation."""
		self._instance.SetArrowHeadSizeAtIndex = value

	@property
	def set_arrow_head_style_at_index(self):
		"""Sets the arrow head style of a specific leader on this annotation."""
		return self._instance.SetArrowHeadStyleAtIndex

	@set_arrow_head_style_at_index.setter
	def set_arrow_head_style_at_index(self, value):
		"""Sets the arrow head style of a specific leader on this annotation."""
		self._instance.SetArrowHeadStyleAtIndex = value

	@property
	def set_attached_entities(self):
		"""Attaches this annotation to the specified entities."""
		return self._instance.SetAttachedEntities

	@set_attached_entities.setter
	def set_attached_entities(self, value):
		"""Attaches this annotation to the specified entities."""
		self._instance.SetAttachedEntities = value

	@property
	def set_leader(self):
		"""Sets the leader characteristics for this annotation."""
		return self._instance.SetLeader3

	@set_leader.setter
	def set_leader(self, value):
		"""Sets the leader characteristics for this annotation."""
		self._instance.SetLeader3 = value

	@property
	def set_leader_attachment_point_at_index(self):
		"""Sets the specified attachment point of a leader for an annotation with the specified index."""
		return self._instance.SetLeaderAttachmentPointAtIndex

	@set_leader_attachment_point_at_index.setter
	def set_leader_attachment_point_at_index(self, value):
		"""Sets the specified attachment point of a leader for an annotation with the specified index."""
		self._instance.SetLeaderAttachmentPointAtIndex = value

	@property
	def set_name(self):
		"""Sets the name of this annotation."""
		return self._instance.SetName

	@set_name.setter
	def set_name(self, value):
		"""Sets the name of this annotation."""
		self._instance.SetName = value

	@property
	def set_position(self):
		"""Sets the position of this annotation."""
		return self._instance.SetPosition2

	@set_position.setter
	def set_position(self, value):
		"""Sets the position of this annotation."""
		self._instance.SetPosition2 = value

	@property
	def set_style_name(self):
		"""Sets the style for this annotation."""
		return self._instance.SetStyleName

	@set_style_name.setter
	def set_style_name(self, value):
		"""Sets the style for this annotation."""
		self._instance.SetStyleName = value

	@property
	def set_text_format(self):
		"""Sets the text format for the specified text in this annotation."""
		return self._instance.SetTextFormat

	@set_text_format.setter
	def set_text_format(self, value):
		"""Sets the text format for the specified text in this annotation."""
		self._instance.SetTextFormat = value

