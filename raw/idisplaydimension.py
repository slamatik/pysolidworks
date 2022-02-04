# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension_members.html
class IDisplayDimension:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def arc_extension_line_or_opposite_side(self):
		"""Gets or sets whether to attach or extend the radial dimension leader on this radial display dimension."""
		return self._instance.ArcExtensionLineOrOppositeSide

	@arc_extension_line_or_opposite_side.setter
	def arc_extension_line_or_opposite_side(self, value):
		"""Gets or sets whether to attach or extend the radial dimension leader on this radial display dimension."""
		self._instance.ArcExtensionLineOrOppositeSide = value

	@property
	def arrow_side(self):
		"""Gets or sets the position of the dimension arrows."""
		return self._instance.ArrowSide

	@arrow_side.setter
	def arrow_side(self, value):
		"""Gets or sets the position of the dimension arrows."""
		self._instance.ArrowSide = value

	@property
	def center_text(self):
		"""Gets or sets whether the text of this display dimension should be automatically centered."""
		return self._instance.CenterText

	@center_text.setter
	def center_text(self, value):
		"""Gets or sets whether the text of this display dimension should be automatically centered."""
		self._instance.CenterText = value

	@property
	def chamfer_precision(self):
		"""Gets or sets the precision of the length and angle values in a chamfer display dimension."""
		return self._instance.ChamferPrecision

	@chamfer_precision.setter
	def chamfer_precision(self, value):
		"""Gets or sets the precision of the length and angle values in a chamfer display dimension."""
		self._instance.ChamferPrecision = value

	@property
	def chamfer_text_style(self):
		"""Gets or sets the text style for chamfer dimensions."""
		return self._instance.ChamferTextStyle

	@chamfer_text_style.setter
	def chamfer_text_style(self, value):
		"""Gets or sets the text style for chamfer dimensions."""
		self._instance.ChamferTextStyle = value

	@property
	def diametric(self):
		"""Gets or sets whether this diameter dimension is displayed as a diameter dimension or a radial dimension."""
		return self._instance.Diametric

	@diametric.setter
	def diametric(self, value):
		"""Gets or sets whether this diameter dimension is displayed as a diameter dimension or a radial dimension."""
		self._instance.Diametric = value

	@property
	def dimension_to_inside(self):
		"""Gets or sets whether dimensions to arcs are always to the inside of the arc."""
		return self._instance.DimensionToInside

	@dimension_to_inside.setter
	def dimension_to_inside(self, value):
		"""Gets or sets whether dimensions to arcs are always to the inside of the arc."""
		self._instance.DimensionToInside = value

	@property
	def display_as_chain(self):
		"""Gets or sets whether the extension lines of every dimension in this set of angular running or ordinate dimensions are chained together."""
		return self._instance.DisplayAsChain

	@display_as_chain.setter
	def display_as_chain(self, value):
		"""Gets or sets whether the extension lines of every dimension in this set of angular running or ordinate dimensions are chained together."""
		self._instance.DisplayAsChain = value

	@property
	def display_as_linear(self):
		"""Gets or sets whether this diameter dimension is displayed as a linear dimension."""
		return self._instance.DisplayAsLinear

	@display_as_linear.setter
	def display_as_linear(self, value):
		"""Gets or sets whether this diameter dimension is displayed as a linear dimension."""
		self._instance.DisplayAsLinear = value

	@property
	def elevation(self):
		"""Gets or sets whether to display an elevation symbol, which is controlled by IDisplayDimension::EndSymbol, at the end of ordinate dimension extension lines."""
		return self._instance.Elevation

	@elevation.setter
	def elevation(self, value):
		"""Gets or sets whether to display an elevation symbol, which is controlled by IDisplayDimension::EndSymbol, at the end of ordinate dimension extension lines."""
		self._instance.Elevation = value

	@property
	def end_symbol(self):
		"""Gets or sets the ordinate dimension end symbol."""
		return self._instance.EndSymbol

	@end_symbol.setter
	def end_symbol(self, value):
		"""Gets or sets the ordinate dimension end symbol."""
		self._instance.EndSymbol = value

	@property
	def extension_line_extends_from_center_of_set(self):
		"""Gets or sets whether extension lines extend from the center of this set of angular running dimensions."""
		return self._instance.ExtensionLineExtendsFromCenterOfSet

	@extension_line_extends_from_center_of_set.setter
	def extension_line_extends_from_center_of_set(self, value):
		"""Gets or sets whether extension lines extend from the center of this set of angular running dimensions."""
		self._instance.ExtensionLineExtendsFromCenterOfSet = value

	@property
	def extension_line_same_as_leader_style(self):
		"""Gets or sets whether to use leader line styles for extension line styles."""
		return self._instance.ExtensionLineSameAsLeaderStyle

	@extension_line_same_as_leader_style.setter
	def extension_line_same_as_leader_style(self, value):
		"""Gets or sets whether to use leader line styles for extension line styles."""
		self._instance.ExtensionLineSameAsLeaderStyle = value

	@property
	def extension_line_use_document_display(self):
		"""Gets or sets whether to use the document settings for extension lines."""
		return self._instance.ExtensionLineUseDocumentDisplay

	@extension_line_use_document_display.setter
	def extension_line_use_document_display(self, value):
		"""Gets or sets whether to use the document settings for extension lines."""
		self._instance.ExtensionLineUseDocumentDisplay = value

	@property
	def foreshortened(self):
		"""Gets or sets whether a linear dimension is foreshortened in a drawing."""
		return self._instance.Foreshortened

	@foreshortened.setter
	def foreshortened(self, value):
		"""Gets or sets whether a linear dimension is foreshortened in a drawing."""
		self._instance.Foreshortened = value

	@property
	def grid_bubble(self):
		"""Gets or sets whether to display a grid bubble at the end of ordinate dimension extension lines."""
		return self._instance.GridBubble

	@grid_bubble.setter
	def grid_bubble(self, value):
		"""Gets or sets whether to display a grid bubble at the end of ordinate dimension extension lines."""
		self._instance.GridBubble = value

	@property
	def horizontal_justification(self):
		"""Gets or sets the dimension text's horizontal justification."""
		return self._instance.HorizontalJustification

	@horizontal_justification.setter
	def horizontal_justification(self, value):
		"""Gets or sets the dimension text's horizontal justification."""
		self._instance.HorizontalJustification = value

	@property
	def inspection(self):
		"""Gets or sets whether a display dimension above the dimension line is displayed as an inspection dimension."""
		return self._instance.Inspection

	@inspection.setter
	def inspection(self, value):
		"""Gets or sets whether a display dimension above the dimension line is displayed as an inspection dimension."""
		self._instance.Inspection = value

	@property
	def is_linked(self):
		"""Gets whether the dimension has text linked to it."""
		return self._instance.IsLinked

	@is_linked.setter
	def is_linked(self, value):
		"""Gets whether the dimension has text linked to it."""
		self._instance.IsLinked = value

	@property
	def jogged(self):
		"""Gets or sets whether this ordinate or angular running dimension is jogged."""
		return self._instance.Jogged

	@jogged.setter
	def jogged(self, value):
		"""Gets or sets whether this ordinate or angular running dimension is jogged."""
		self._instance.Jogged = value

	@property
	def leader_visibility(self):
		"""Gets or sets which leader lines (dimension lines) are visible on a display dimension."""
		return self._instance.LeaderVisibility

	@leader_visibility.setter
	def leader_visibility(self, value):
		"""Gets or sets which leader lines (dimension lines) are visible on a display dimension."""
		self._instance.LeaderVisibility = value

	@property
	def lower_inspection(self):
		"""Gets or sets whether a display dimension below the dimension line is displayed as an inspection dimension."""
		return self._instance.LowerInspection

	@lower_inspection.setter
	def lower_inspection(self, value):
		"""Gets or sets whether a display dimension below the dimension line is displayed as an inspection dimension."""
		self._instance.LowerInspection = value

	@property
	def marked_for_drawing(self):
		"""Gets or sets whether this display dimension is marked to include in a drawing document."""
		return self._instance.MarkedForDrawing

	@marked_for_drawing.setter
	def marked_for_drawing(self, value):
		"""Gets or sets whether this display dimension is marked to include in a drawing document."""
		self._instance.MarkedForDrawing = value

	@property
	def max_witness_line_length(self):
		"""Gets or sets the maximum length of dimension extension lines."""
		return self._instance.MaxWitnessLineLength

	@max_witness_line_length.setter
	def max_witness_line_length(self, value):
		"""Gets or sets the maximum length of dimension extension lines."""
		self._instance.MaxWitnessLineLength = value

	@property
	def offset_text(self):
		"""Gets or sets whether or not to offset the text of a dimension."""
		return self._instance.OffsetText

	@offset_text.setter
	def offset_text(self, value):
		"""Gets or sets whether or not to offset the text of a dimension."""
		self._instance.OffsetText = value

	@property
	def run_bidirectionally(self):
		"""Gets or sets whether each dimension runs in a direction closest to the baseline in this angular running dimension."""
		return self._instance.RunBidirectionally

	@run_bidirectionally.setter
	def run_bidirectionally(self, value):
		"""Gets or sets whether each dimension runs in a direction closest to the baseline in this angular running dimension."""
		self._instance.RunBidirectionally = value

	@property
	def scale(self):
		"""Gets or sets the scale value that is applied to the dimension value of this non-associative distance dimension."""
		return self._instance.Scale2

	@scale.setter
	def scale(self, value):
		"""Gets or sets the scale value that is applied to the dimension value of this non-associative distance dimension."""
		self._instance.Scale2 = value

	@property
	def shortened_radius(self):
		"""Gets or sets whether to display this radius display dimension with a foreshortened radius."""
		return self._instance.ShortenedRadius

	@shortened_radius.setter
	def shortened_radius(self, value):
		"""Gets or sets whether to display this radius display dimension with a foreshortened radius."""
		self._instance.ShortenedRadius = value

	@property
	def show_dimension_value(self):
		"""Gets or sets whether the dimension value is displayed as part of the dimension text."""
		return self._instance.ShowDimensionValue

	@show_dimension_value.setter
	def show_dimension_value(self, value):
		"""Gets or sets whether the dimension value is displayed as part of the dimension text."""
		self._instance.ShowDimensionValue = value

	@property
	def show_lower_parenthesis(self):
		"""Gets or sets whether to enclose the text below the dimension line of the display dimension in parentheses."""
		return self._instance.ShowLowerParenthesis

	@show_lower_parenthesis.setter
	def show_lower_parenthesis(self, value):
		"""Gets or sets whether to enclose the text below the dimension line of the display dimension in parentheses."""
		self._instance.ShowLowerParenthesis = value

	@property
	def show_parenthesis(self):
		"""Gets or sets whether to enclose the text above the dimension line of the display dimension in parentheses."""
		return self._instance.ShowParenthesis

	@show_parenthesis.setter
	def show_parenthesis(self, value):
		"""Gets or sets whether to enclose the text above the dimension line of the display dimension in parentheses."""
		self._instance.ShowParenthesis = value

	@property
	def smart_witness(self):
		"""Gets or sets the smart display of extension lines."""
		return self._instance.SmartWitness

	@smart_witness.setter
	def smart_witness(self, value):
		"""Gets or sets the smart display of extension lines."""
		self._instance.SmartWitness = value

	@property
	def solid_leader(self):
		"""Gets or sets whether this display dimension is displayed with a solid leader for arc and radial dimensions."""
		return self._instance.SolidLeader

	@solid_leader.setter
	def solid_leader(self, value):
		"""Gets or sets whether this display dimension is displayed with a solid leader for arc and radial dimensions."""
		self._instance.SolidLeader = value

	@property
	def split(self):
		"""Gets or sets whether to split a dual dimension above and below an unbroken dimension line (also called a leader)."""
		return self._instance.Split

	@split.setter
	def split(self, value):
		"""Gets or sets whether to split a dual dimension above and below an unbroken dimension line (also called a leader)."""
		self._instance.Split = value

	@property
	def type(self):
		"""Gets the type of dimension."""
		return self._instance.Type2

	@type.setter
	def type(self, value):
		"""Gets the type of dimension."""
		self._instance.Type2 = value

	@property
	def vertical_justification(self):
		"""Gets the dimension text's vertical justification."""
		return self._instance.VerticalJustification

	@vertical_justification.setter
	def vertical_justification(self, value):
		"""Gets the dimension text's vertical justification."""
		self._instance.VerticalJustification = value

	@property
	def witness_visibility(self):
		"""Gets or sets which extension lines are visible."""
		return self._instance.WitnessVisibility

	@witness_visibility.setter
	def witness_visibility(self, value):
		"""Gets or sets which extension lines are visible."""
		self._instance.WitnessVisibility = value

	@property
	def add_display_ent(self):
		"""Overrides the display graphics of objects."""
		return self._instance.AddDisplayEnt

	@add_display_ent.setter
	def add_display_ent(self, value):
		"""Overrides the display graphics of objects."""
		self._instance.AddDisplayEnt = value

	@property
	def add_display_text(self):
		"""Overrides the display text."""
		return self._instance.AddDisplayText

	@add_display_text.setter
	def add_display_text(self, value):
		"""Overrides the display text."""
		self._instance.AddDisplayText = value

	@property
	def auto_jog_ordinate(self):
		"""Sets the auto-jog for this ordinate dimension."""
		return self._instance.AutoJogOrdinate

	@auto_jog_ordinate.setter
	def auto_jog_ordinate(self, value):
		"""Sets the auto-jog for this ordinate dimension."""
		self._instance.AutoJogOrdinate = value

	@property
	def explementary_angle(self):
		"""Flips an angular dimension to its explementary angle."""
		return self._instance.ExplementaryAngle

	@explementary_angle.setter
	def explementary_angle(self, value):
		"""Flips an angular dimension to its explementary angle."""
		self._instance.ExplementaryAngle = value

	@property
	def get_alternate_precision(self):
		"""Gets the displayed precision for the dual portion of this dimension."""
		return self._instance.GetAlternatePrecision2

	@get_alternate_precision.setter
	def get_alternate_precision(self, value):
		"""Gets the displayed precision for the dual portion of this dimension."""
		self._instance.GetAlternatePrecision2 = value

	@property
	def get_alternate_tol_precision(self):
		"""Gets the displayed precision for the dual tolerance portion of this dimension."""
		return self._instance.GetAlternateTolPrecision2

	@get_alternate_tol_precision.setter
	def get_alternate_tol_precision(self, value):
		"""Gets the displayed precision for the dual tolerance portion of this dimension."""
		self._instance.GetAlternateTolPrecision2 = value

	@property
	def get_annotation(self):
		"""Gets the IAnnotation object for this specific annotation."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the IAnnotation object for this specific annotation."""
		self._instance.GetAnnotation = value

	@property
	def get_arc_length_leader(self):
		"""Gets the leader style of this arc length dimension."""
		return self._instance.GetArcLengthLeader

	@get_arc_length_leader.setter
	def get_arc_length_leader(self, value):
		"""Gets the leader style of this arc length dimension."""
		self._instance.GetArcLengthLeader = value

	@property
	def get_arrow_head_style(self):
		"""Gets the arrowhead style used by this display dimension."""
		return self._instance.GetArrowHeadStyle2

	@get_arrow_head_style.setter
	def get_arrow_head_style(self, value):
		"""Gets the arrowhead style used by this display dimension."""
		self._instance.GetArrowHeadStyle2 = value

	@property
	def get_auto_arc_length_leader(self):
		"""Gets whether the leader style of this arc-length dimension is being automatically selected or selected by the user."""
		return self._instance.GetAutoArcLengthLeader

	@get_auto_arc_length_leader.setter
	def get_auto_arc_length_leader(self, value):
		"""Gets whether the leader style of this arc-length dimension is being automatically selected or selected by the user."""
		self._instance.GetAutoArcLengthLeader = value

	@property
	def get_bent_leader_length(self):
		"""Gets the length of the bent leader to use when displaying this dimension."""
		return self._instance.GetBentLeaderLength

	@get_bent_leader_length.setter
	def get_bent_leader_length(self, value):
		"""Gets the length of the bent leader to use when displaying this dimension."""
		self._instance.GetBentLeaderLength = value

	@property
	def get_broken_leader(self):
		"""Gets whether this display dimension has a broken or split leader."""
		return self._instance.GetBrokenLeader2

	@get_broken_leader.setter
	def get_broken_leader(self, value):
		"""Gets whether this display dimension has a broken or split leader."""
		self._instance.GetBrokenLeader2 = value

	@property
	def get_chamfer_units(self):
		"""Gets the local units of measurement for a chamfer display dimension."""
		return self._instance.GetChamferUnits

	@get_chamfer_units.setter
	def get_chamfer_units(self, value):
		"""Gets the local units of measurement for a chamfer display dimension."""
		self._instance.GetChamferUnits = value

	@property
	def get_definition_transform(self):
		"""Gets the transform for this dimension."""
		return self._instance.GetDefinitionTransform

	@get_definition_transform.setter
	def get_definition_transform(self, value):
		"""Gets the transform for this dimension."""
		self._instance.GetDefinitionTransform = value

	@property
	def get_dimension(self):
		"""Gets the model dimension used to create this display dimension."""
		return self._instance.GetDimension2

	@get_dimension.setter
	def get_dimension(self, value):
		"""Gets the model dimension used to create this display dimension."""
		self._instance.GetDimension2 = value

	@property
	def get_display_data(self):
		"""Gets the display data for this display dimension."""
		return self._instance.GetDisplayData

	@get_display_data.setter
	def get_display_data(self, value):
		"""Gets the display data for this display dimension."""
		self._instance.GetDisplayData = value

	@property
	def get_extension_line_as_centerline(self):
		"""Gets whether the specified extension line is a centerline."""
		return self._instance.GetExtensionLineAsCenterline

	@get_extension_line_as_centerline.setter
	def get_extension_line_as_centerline(self, value):
		"""Gets whether the specified extension line is a centerline."""
		self._instance.GetExtensionLineAsCenterline = value

	@property
	def get_fraction_base(self):
		"""Gets whether this display dimension is displayed as a decimal value or a fraction."""
		return self._instance.GetFractionBase

	@get_fraction_base.setter
	def get_fraction_base(self, value):
		"""Gets whether this display dimension is displayed as a decimal value or a fraction."""
		self._instance.GetFractionBase = value

	@property
	def get_fraction_value(self):
		"""Gets the largest fraction denominator to be used when this display dimension is displayed in fraction format."""
		return self._instance.GetFractionValue

	@get_fraction_value.setter
	def get_fraction_value(self, value):
		"""Gets the largest fraction denominator to be used when this display dimension is displayed in fraction format."""
		self._instance.GetFractionValue = value

	@property
	def get_hole_callout_variables(self):
		"""Gets access to hole callout variables in a hole callout."""
		return self._instance.GetHoleCalloutVariables

	@get_hole_callout_variables.setter
	def get_hole_callout_variables(self, value):
		"""Gets access to hole callout variables in a hole callout."""
		self._instance.GetHoleCalloutVariables = value

	@property
	def get_jog_parameters(self):
		"""Gets the jog in a linear dimension extension line."""
		return self._instance.GetJogParameters

	@get_jog_parameters.setter
	def get_jog_parameters(self, value):
		"""Gets the jog in a linear dimension extension line."""
		self._instance.GetJogParameters = value

	@property
	def get_linked_text(self):
		"""Gets the text linked to this display dimension."""
		return self._instance.GetLinkedText

	@get_linked_text.setter
	def get_linked_text(self, value):
		"""Gets the text linked to this display dimension."""
		self._instance.GetLinkedText = value

	@property
	def get_lower_text(self):
		"""Gets the text below the dimension line in a display dimension."""
		return self._instance.GetLowerText

	@get_lower_text.setter
	def get_lower_text(self, value):
		"""Gets the text below the dimension line in a display dimension."""
		self._instance.GetLowerText = value

	@property
	def get_name_for_selection(self):
		"""Gets the name of the selected display dimension needed by IModelDocExtension::SelectByID2."""
		return self._instance.GetNameForSelection

	@get_name_for_selection.setter
	def get_name_for_selection(self, value):
		"""Gets the name of the selected display dimension needed by IModelDocExtension::SelectByID2."""
		self._instance.GetNameForSelection = value

	@property
	def get_next(self):
		"""Gets the next display dimension."""
		return self._instance.GetNext5

	@get_next.setter
	def get_next(self, value):
		"""Gets the next display dimension."""
		self._instance.GetNext5 = value

	@property
	def get_ordinate_dimension_arrow_size(self):
		"""Gets the diameter of the circle for the arrow of the base ordinate dimension."""
		return self._instance.GetOrdinateDimensionArrowSize

	@get_ordinate_dimension_arrow_size.setter
	def get_ordinate_dimension_arrow_size(self, value):
		"""Gets the diameter of the circle for the arrow of the base ordinate dimension."""
		self._instance.GetOrdinateDimensionArrowSize = value

	@property
	def get_override(self):
		"""Gets whether to display the actual dimension value or to override it with another value."""
		return self._instance.GetOverride

	@get_override.setter
	def get_override(self, value):
		"""Gets whether to display the actual dimension value or to override it with another value."""
		self._instance.GetOverride = value

	@property
	def get_override_value(self):
		"""Gets the value to display instead of the actual dimension value."""
		return self._instance.GetOverrideValue

	@get_override_value.setter
	def get_override_value(self, value):
		"""Gets the value to display instead of the actual dimension value."""
		self._instance.GetOverrideValue = value

	@property
	def get_primary_precision(self):
		"""Gets the primary dimension precision setting for this display dimension."""
		return self._instance.GetPrimaryPrecision2

	@get_primary_precision.setter
	def get_primary_precision(self, value):
		"""Gets the primary dimension precision setting for this display dimension."""
		self._instance.GetPrimaryPrecision2 = value

	@property
	def get_primary_tol_precision(self):
		"""Gets the primary tolerance precision setting for this display dimension."""
		return self._instance.GetPrimaryTolPrecision2

	@get_primary_tol_precision.setter
	def get_primary_tol_precision(self, value):
		"""Gets the primary tolerance precision setting for this display dimension."""
		self._instance.GetPrimaryTolPrecision2 = value

	@property
	def get_round_to_fraction(self):
		"""Gets whether the displayed dimension value is rounded off so that SOLIDWORKS can display it as a fraction."""
		return self._instance.GetRoundToFraction

	@get_round_to_fraction.setter
	def get_round_to_fraction(self, value):
		"""Gets whether the displayed dimension value is rounded off so that SOLIDWORKS can display it as a fraction."""
		self._instance.GetRoundToFraction = value

	@property
	def get_second_arrow(self):
		"""Gets whether this diameter display dimension has the second arrow enabled."""
		return self._instance.GetSecondArrow

	@get_second_arrow.setter
	def get_second_arrow(self, value):
		"""Gets whether this diameter display dimension has the second arrow enabled."""
		self._instance.GetSecondArrow = value

	@property
	def get_supports_generic_text(self):
		"""Gets whether the display dimension was created in SOLIDWORKS 2011 or later, which, if so, indicates that the display dimension is generic text."""
		return self._instance.GetSupportsGenericText

	@get_supports_generic_text.setter
	def get_supports_generic_text(self, value):
		"""Gets whether the display dimension was created in SOLIDWORKS 2011 or later, which, if so, indicates that the display dimension is generic text."""
		self._instance.GetSupportsGenericText = value

	@property
	def get_text(self):
		"""Gets the text above the dimension line in a display dimension."""
		return self._instance.GetText

	@get_text.setter
	def get_text(self, value):
		"""Gets the text above the dimension line in a display dimension."""
		self._instance.GetText = value

	@property
	def get_text_format_items(self):
		"""Gets the format tokens of the specified text portion of a multi-value display dimension."""
		return self._instance.GetTextFormatItems

	@get_text_format_items.setter
	def get_text_format_items(self, value):
		"""Gets the format tokens of the specified text portion of a multi-value display dimension."""
		self._instance.GetTextFormatItems = value

	@property
	def get_units(self):
		"""Gets the units used by this display dimension."""
		return self._instance.GetUnits

	@get_units.setter
	def get_units(self, value):
		"""Gets the units used by this display dimension."""
		self._instance.GetUnits = value

	@property
	def get_use_doc_arrow_head_style(self):
		"""Gets whether this display dimension uses the document default setting for dimension arrowhead style."""
		return self._instance.GetUseDocArrowHeadStyle

	@get_use_doc_arrow_head_style.setter
	def get_use_doc_arrow_head_style(self, value):
		"""Gets whether this display dimension uses the document default setting for dimension arrowhead style."""
		self._instance.GetUseDocArrowHeadStyle = value

	@property
	def get_use_doc_bent_leader_length(self):
		"""Gets whether this dimension is using the document default for bent leader length or not."""
		return self._instance.GetUseDocBentLeaderLength

	@get_use_doc_bent_leader_length.setter
	def get_use_doc_bent_leader_length(self, value):
		"""Gets whether this dimension is using the document default for bent leader length or not."""
		self._instance.GetUseDocBentLeaderLength = value

	@property
	def get_use_doc_broken_leader(self):
		"""Gets whether this display dimension uses the document default setting for displaying leaders as broken."""
		return self._instance.GetUseDocBrokenLeader

	@get_use_doc_broken_leader.setter
	def get_use_doc_broken_leader(self, value):
		"""Gets whether this display dimension uses the document default setting for displaying leaders as broken."""
		self._instance.GetUseDocBrokenLeader = value

	@property
	def get_use_doc_dual(self):
		"""Gets whether this display dimension uses the document setting for positioning dual dimensions."""
		return self._instance.GetUseDocDual

	@get_use_doc_dual.setter
	def get_use_doc_dual(self, value):
		"""Gets whether this display dimension uses the document setting for positioning dual dimensions."""
		self._instance.GetUseDocDual = value

	@property
	def get_use_doc_second_arrow(self):
		"""Gets whether this diameter display dimension uses the document default setting for the display of the second outside arrow."""
		return self._instance.GetUseDocSecondArrow

	@get_use_doc_second_arrow.setter
	def get_use_doc_second_arrow(self, value):
		"""Gets whether this diameter display dimension uses the document default setting for the display of the second outside arrow."""
		self._instance.GetUseDocSecondArrow = value

	@property
	def get_use_doc_units(self):
		"""Gets whether this display dimension uses the document default setting for units."""
		return self._instance.GetUseDocUnits

	@get_use_doc_units.setter
	def get_use_doc_units(self, value):
		"""Gets whether this display dimension uses the document default setting for units."""
		self._instance.GetUseDocUnits = value

	@property
	def get_witness_line_gap(self):
		"""Gets the gap of the specified dimension extension line."""
		return self._instance.GetWitnessLineGap

	@get_witness_line_gap.setter
	def get_witness_line_gap(self, value):
		"""Gets the gap of the specified dimension extension line."""
		self._instance.GetWitnessLineGap = value

	@property
	def i_add_display_ent(self):
		"""Overrides the display graphics of objects for this display dimension."""
		return self._instance.IAddDisplayEnt

	@i_add_display_ent.setter
	def i_add_display_ent(self, value):
		"""Overrides the display graphics of objects for this display dimension."""
		self._instance.IAddDisplayEnt = value

	@property
	def i_add_display_text(self):
		"""Overrides the display text for this display dimension."""
		return self._instance.IAddDisplayText

	@i_add_display_text.setter
	def i_add_display_text(self, value):
		"""Overrides the display text for this display dimension."""
		self._instance.IAddDisplayText = value

	@property
	def i_get_annotation(self):
		"""Gets the IAnnotation object for this specific annotation."""
		return self._instance.IGetAnnotation

	@i_get_annotation.setter
	def i_get_annotation(self, value):
		"""Gets the IAnnotation object for this specific annotation."""
		self._instance.IGetAnnotation = value

	@property
	def i_get_display_data(self):
		"""Gets the display data for this display dimension."""
		return self._instance.IGetDisplayData

	@i_get_display_data.setter
	def i_get_display_data(self, value):
		"""Gets the display data for this display dimension."""
		self._instance.IGetDisplayData = value

	@property
	def is_hole_callout(self):
		"""Gets whether this display dimension is a hole callout."""
		return self._instance.IsHoleCallout

	@is_hole_callout.setter
	def is_hole_callout(self, value):
		"""Gets whether this display dimension is a hole callout."""
		self._instance.IsHoleCallout = value

	@property
	def is_reference_dim(self):
		"""Gets whether this display dimension is a reference dimension."""
		return self._instance.IsReferenceDim

	@is_reference_dim.setter
	def is_reference_dim(self, value):
		"""Gets whether this display dimension is a reference dimension."""
		self._instance.IsReferenceDim = value

	@property
	def reset_extension_line_style(self):
		"""Resets the style of the specified extension line."""
		return self._instance.ResetExtensionLineStyle

	@reset_extension_line_style.setter
	def reset_extension_line_style(self, value):
		"""Resets the style of the specified extension line."""
		self._instance.ResetExtensionLineStyle = value

	@property
	def set_arc_length_leader(self):
		"""Sets the leader style of this arc-length dimension."""
		return self._instance.SetArcLengthLeader

	@set_arc_length_leader.setter
	def set_arc_length_leader(self, value):
		"""Sets the leader style of this arc-length dimension."""
		self._instance.SetArcLengthLeader = value

	@property
	def set_arrow_head_style(self):
		"""Sets the arrowhead style of this display dimension."""
		return self._instance.SetArrowHeadStyle2

	@set_arrow_head_style.setter
	def set_arrow_head_style(self, value):
		"""Sets the arrowhead style of this display dimension."""
		self._instance.SetArrowHeadStyle2 = value

	@property
	def set_bent_leader_length(self):
		"""Sets the bent leader length to use for this dimension."""
		return self._instance.SetBentLeaderLength

	@set_bent_leader_length.setter
	def set_bent_leader_length(self, value):
		"""Sets the bent leader length to use for this dimension."""
		self._instance.SetBentLeaderLength = value

	@property
	def set_broken_leader(self):
		"""Sets the broken leader display characteristic of this display dimension."""
		return self._instance.SetBrokenLeader2

	@set_broken_leader.setter
	def set_broken_leader(self, value):
		"""Sets the broken leader display characteristic of this display dimension."""
		self._instance.SetBrokenLeader2 = value

	@property
	def set_dual(self):
		"""Controls the display of dual dimensions of this display dimension."""
		return self._instance.SetDual2

	@set_dual.setter
	def set_dual(self, value):
		"""Controls the display of dual dimensions of this display dimension."""
		self._instance.SetDual2 = value

	@property
	def set_extension_line_as_centerline(self):
		"""Sets whether the specified extension line is a centerline."""
		return self._instance.SetExtensionLineAsCenterline

	@set_extension_line_as_centerline.setter
	def set_extension_line_as_centerline(self, value):
		"""Sets whether the specified extension line is a centerline."""
		self._instance.SetExtensionLineAsCenterline = value

	@property
	def set_jog_parameters(self):
		"""Set the linear dimension extension line to be jogged."""
		return self._instance.SetJogParameters

	@set_jog_parameters.setter
	def set_jog_parameters(self, value):
		"""Set the linear dimension extension line to be jogged."""
		self._instance.SetJogParameters = value

	@property
	def set_line_font_dimension_style(self):
		"""Sets the style of leader for this display dimension."""
		return self._instance.SetLineFontDimensionStyle

	@set_line_font_dimension_style.setter
	def set_line_font_dimension_style(self, value):
		"""Sets the style of leader for this display dimension."""
		self._instance.SetLineFontDimensionStyle = value

	@property
	def set_line_font_dimension_thickness(self):
		"""Sets the thickness of leaders of this display dimension."""
		return self._instance.SetLineFontDimensionThickness

	@set_line_font_dimension_thickness.setter
	def set_line_font_dimension_thickness(self, value):
		"""Sets the thickness of leaders of this display dimension."""
		self._instance.SetLineFontDimensionThickness = value

	@property
	def set_line_font_extension_style(self):
		"""Sets the line font style for the extension lines of this display dimension."""
		return self._instance.SetLineFontExtensionStyle

	@set_line_font_extension_style.setter
	def set_line_font_extension_style(self, value):
		"""Sets the line font style for the extension lines of this display dimension."""
		self._instance.SetLineFontExtensionStyle = value

	@property
	def set_line_font_extension_thickness(self):
		"""Sets the thickness of the extension lines of this display dimension."""
		return self._instance.SetLineFontExtensionThickness

	@set_line_font_extension_thickness.setter
	def set_line_font_extension_thickness(self, value):
		"""Sets the thickness of the extension lines of this display dimension."""
		self._instance.SetLineFontExtensionThickness = value

	@property
	def set_linked_text(self):
		"""Sets the text to link to this display dimension."""
		return self._instance.SetLinkedText

	@set_linked_text.setter
	def set_linked_text(self, value):
		"""Sets the text to link to this display dimension."""
		self._instance.SetLinkedText = value

	@property
	def set_lower_text(self):
		"""Sets the text below the dimension line in a display dimension."""
		return self._instance.SetLowerText

	@set_lower_text.setter
	def set_lower_text(self, value):
		"""Sets the text below the dimension line in a display dimension."""
		self._instance.SetLowerText = value

	@property
	def set_ordinate_dimension_arrow_size(self):
		"""Sets the diameter of the circle for the arrow of the base ordinate dimension if the base ordinate dimension standard is set to DIN."""
		return self._instance.SetOrdinateDimensionArrowSize

	@set_ordinate_dimension_arrow_size.setter
	def set_ordinate_dimension_arrow_size(self, value):
		"""Sets the diameter of the circle for the arrow of the base ordinate dimension if the base ordinate dimension standard is set to DIN."""
		self._instance.SetOrdinateDimensionArrowSize = value

	@property
	def set_override(self):
		"""Sets whether to display the actual dimension value or to display another value, and, if so, that value."""
		return self._instance.SetOverride

	@set_override.setter
	def set_override(self, value):
		"""Sets whether to display the actual dimension value or to display another value, and, if so, that value."""
		self._instance.SetOverride = value

	@property
	def set_precision(self):
		"""Sets the number of digits to display after the decimal point for precision and tolerance values in this display dimension."""
		return self._instance.SetPrecision3

	@set_precision.setter
	def set_precision(self, value):
		"""Sets the number of digits to display after the decimal point for precision and tolerance values in this display dimension."""
		self._instance.SetPrecision3 = value

	@property
	def set_second_arrow(self):
		"""Sets the second arrow characteristics of this diameter display dimension."""
		return self._instance.SetSecondArrow

	@set_second_arrow.setter
	def set_second_arrow(self, value):
		"""Sets the second arrow characteristics of this diameter display dimension."""
		self._instance.SetSecondArrow = value

	@property
	def set_text(self):
		"""Sets the text above the dimension line in a display dimension."""
		return self._instance.SetText

	@set_text.setter
	def set_text(self, value):
		"""Sets the text above the dimension line in a display dimension."""
		self._instance.SetText = value

	@property
	def set_units(self):
		"""Sets the unit display characteristics of this display dimension."""
		return self._instance.SetUnits2

	@set_units.setter
	def set_units(self, value):
		"""Sets the unit display characteristics of this display dimension."""
		self._instance.SetUnits2 = value

	@property
	def set_witness_line_gap(self):
		"""Sets the gap for the specified dimension extension line."""
		return self._instance.SetWitnessLineGap

	@set_witness_line_gap.setter
	def set_witness_line_gap(self, value):
		"""Sets the gap for the specified dimension extension line."""
		self._instance.SetWitnessLineGap = value

	@property
	def supplementary_angle(self):
		"""Changes the angle in the selected angular dimension to its supplementary angle."""
		return self._instance.SupplementaryAngle

	@supplementary_angle.setter
	def supplementary_angle(self, value):
		"""Changes the angle in the selected angular dimension to its supplementary angle."""
		self._instance.SupplementaryAngle = value

	@property
	def unlink(self):
		"""Unlinks a previously linked display dimension."""
		return self._instance.Unlink

	@unlink.setter
	def unlink(self, value):
		"""Unlinks a previously linked display dimension."""
		self._instance.Unlink = value

	@property
	def vertically_opposite_angle(self):
		"""Flips an angular dimension to its vertically opposite angle."""
		return self._instance.VerticallyOppositeAngle

	@vertically_opposite_angle.setter
	def vertically_opposite_angle(self, value):
		"""Flips an angular dimension to its vertically opposite angle."""
		self._instance.VerticallyOppositeAngle = value

