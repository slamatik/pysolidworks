# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrSection_members.html
class IDrSection:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def cut_surface_bodies(self):
		"""Gets or sets whether to hide cut surface bodies in this section view."""
		return self._instance.CutSurfaceBodies

	@cut_surface_bodies.setter
	def cut_surface_bodies(self, value):
		"""Gets or sets whether to hide cut surface bodies in this section view."""
		self._instance.CutSurfaceBodies = value

	@property
	def cutting_line_shoulders(self):
		"""Gets or sets whether to hide cutting line shoulders in this section view."""
		return self._instance.CuttingLineShoulders

	@cutting_line_shoulders.setter
	def cutting_line_shoulders(self, value):
		"""Gets or sets whether to hide cutting line shoulders in this section view."""
		self._instance.CuttingLineShoulders = value

	@property
	def display_surface_bodies(self):
		"""Gets or sets whether to display surface bodies in this section view."""
		return self._instance.DisplaySurfaceBodies

	@display_surface_bodies.setter
	def display_surface_bodies(self, value):
		"""Gets or sets whether to display surface bodies in this section view."""
		self._instance.DisplaySurfaceBodies = value

	@property
	def exclude_fasteners(self):
		"""Gets or sets whether to exclude fasteners in the section view."""
		return self._instance.ExcludeFasteners

	@exclude_fasteners.setter
	def exclude_fasteners(self, value):
		"""Gets or sets whether to exclude fasteners in the section view."""
		self._instance.ExcludeFasteners = value

	@property
	def exclude_slice_section_bodies(self):
		"""Gets or sets whether to exclude slice section bodies in this section view."""
		return self._instance.ExcludeSliceSectionBodies

	@exclude_slice_section_bodies.setter
	def exclude_slice_section_bodies(self, value):
		"""Gets or sets whether to exclude slice section bodies in this section view."""
		self._instance.ExcludeSliceSectionBodies = value

	@property
	def layer(self):
		"""Gets or sets the name of the layer on which the section line lies."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""Gets or sets the name of the layer on which the section line lies."""
		self._instance.Layer = value

	@property
	def randomize_scale(self):
		"""Gets or sets whether to randomize the scale when auto hatching this section view."""
		return self._instance.RandomizeScale

	@randomize_scale.setter
	def randomize_scale(self, value):
		"""Gets or sets whether to randomize the scale when auto hatching this section view."""
		self._instance.RandomizeScale = value

	@property
	def scale_hatch_pattern(self):
		"""Gets or sets whether to scale the hatch pattern to the section view."""
		return self._instance.ScaleHatchPattern

	@scale_hatch_pattern.setter
	def scale_hatch_pattern(self, value):
		"""Gets or sets whether to scale the hatch pattern to the section view."""
		self._instance.ScaleHatchPattern = value

	@property
	def section_depth(self):
		"""Gets or sets the distance from the section line of the section view."""
		return self._instance.SectionDepth

	@section_depth.setter
	def section_depth(self, value):
		"""Gets or sets the distance from the section line of the section view."""
		self._instance.SectionDepth = value

	@property
	def enum_excluded_components(self):
		"""Gets all of the assembly components that are excluded from this section view."""
		return self._instance.EnumExcludedComponents2

	@enum_excluded_components.setter
	def enum_excluded_components(self, value):
		"""Gets all of the assembly components that are excluded from this section view."""
		self._instance.EnumExcludedComponents2 = value

	@property
	def get_arrow_info(self):
		"""Gets the position of the arrows for the section line."""
		return self._instance.GetArrowInfo

	@get_arrow_info.setter
	def get_arrow_info(self, value):
		"""Gets the position of the arrows for the section line."""
		self._instance.GetArrowInfo = value

	@property
	def get_auto_hatch(self):
		"""Gets whether auto hatching is enabled for the section view resulting from this section cut."""
		return self._instance.GetAutoHatch

	@get_auto_hatch.setter
	def get_auto_hatch(self, value):
		"""Gets whether auto hatching is enabled for the section view resulting from this section cut."""
		self._instance.GetAutoHatch = value

	@property
	def get_display_only_speed_pak_bodies(self):
		"""Gets whether to display in this section view only the bodies included in the SpeedPak configuration."""
		return self._instance.GetDisplayOnlySpeedPakBodies

	@get_display_only_speed_pak_bodies.setter
	def get_display_only_speed_pak_bodies(self, value):
		"""Gets whether to display in this section view only the bodies included in the SpeedPak configuration."""
		self._instance.GetDisplayOnlySpeedPakBodies = value

	@property
	def get_display_only_surface_cut(self):
		"""Gets whether to display only the surface cut by the section line."""
		return self._instance.GetDisplayOnlySurfaceCut

	@get_display_only_surface_cut.setter
	def get_display_only_surface_cut(self, value):
		"""Gets whether to display only the surface cut by the section line."""
		self._instance.GetDisplayOnlySurfaceCut = value

	@property
	def get_dont_cut_all_instances(self):
		"""Gets whether all instances of the specified component are uncut in this section view or only in the specified component."""
		return self._instance.GetDontCutAllInstances

	@get_dont_cut_all_instances.setter
	def get_dont_cut_all_instances(self, value):
		"""Gets whether all instances of the specified component are uncut in this section view or only in the specified component."""
		self._instance.GetDontCutAllInstances = value

	@property
	def get_excluded_components(self):
		"""Gets all of the assembly components that are excluded from this section view."""
		return self._instance.GetExcludedComponents

	@get_excluded_components.setter
	def get_excluded_components(self, value):
		"""Gets all of the assembly components that are excluded from this section view."""
		self._instance.GetExcludedComponents = value

	@property
	def get_label(self):
		"""Gets the label for this section view."""
		return self._instance.GetLabel

	@get_label.setter
	def get_label(self, value):
		"""Gets the label for this section view."""
		self._instance.GetLabel = value

	@property
	def get_line_info(self):
		"""Gets the vertices of the section line."""
		return self._instance.GetLineInfo

	@get_line_info.setter
	def get_line_info(self, value):
		"""Gets the vertices of the section line."""
		self._instance.GetLineInfo = value

	@property
	def get_name(self):
		"""Gets the name of the section line."""
		return self._instance.GetName

	@get_name.setter
	def get_name(self, value):
		"""Gets the name of the section line."""
		self._instance.GetName = value

	@property
	def get_partial_section(self):
		"""Gets whether this is a partial section cut."""
		return self._instance.GetPartialSection

	@get_partial_section.setter
	def get_partial_section(self, value):
		"""Gets whether this is a partial section cut."""
		self._instance.GetPartialSection = value

	@property
	def get_reversed_cut_direction(self):
		"""Gets whether the section cut direction is reversed from the default direction."""
		return self._instance.GetReversedCutDirection

	@get_reversed_cut_direction.setter
	def get_reversed_cut_direction(self, value):
		"""Gets whether the section cut direction is reversed from the default direction."""
		self._instance.GetReversedCutDirection = value

	@property
	def get_scale_with_model_changes(self):
		"""Gets whether the section line scales with changes to the model."""
		return self._instance.GetScaleWithModelChanges

	@get_scale_with_model_changes.setter
	def get_scale_with_model_changes(self, value):
		"""Gets whether the section line scales with changes to the model."""
		self._instance.GetScaleWithModelChanges = value

	@property
	def get_section_view(self):
		"""Gets the section view of this section cut."""
		return self._instance.GetSectionView

	@get_section_view.setter
	def get_section_view(self, value):
		"""Gets the section view of this section cut."""
		self._instance.GetSectionView = value

	@property
	def get_text_format(self):
		"""Gets the text format for the text for this section line."""
		return self._instance.GetTextFormat

	@get_text_format.setter
	def get_text_format(self, value):
		"""Gets the text format for the text for this section line."""
		self._instance.GetTextFormat = value

	@property
	def get_text_info(self):
		"""Gets the location of the section line text."""
		return self._instance.GetTextInfo

	@get_text_info.setter
	def get_text_info(self, value):
		"""Gets the location of the section line text."""
		self._instance.GetTextInfo = value

	@property
	def get_use_doc_text_format(self):
		"""Gets whether SOLIDWORKS is currently using the document default setting for text format."""
		return self._instance.GetUseDocTextFormat

	@get_use_doc_text_format.setter
	def get_use_doc_text_format(self, value):
		"""Gets whether SOLIDWORKS is currently using the document default setting for text format."""
		self._instance.GetUseDocTextFormat = value

	@property
	def get_view(self):
		"""Gets the drawing view where the section line appears."""
		return self._instance.GetView

	@get_view.setter
	def get_view(self, value):
		"""Gets the drawing view where the section line appears."""
		self._instance.GetView = value

	@property
	def i_get_arrow_info(self):
		"""Gets the position of the arrows for this section line."""
		return self._instance.IGetArrowInfo

	@i_get_arrow_info.setter
	def i_get_arrow_info(self, value):
		"""Gets the position of the arrows for this section line."""
		self._instance.IGetArrowInfo = value

	@property
	def i_get_line_info(self):
		"""Gets the vertices of the section line."""
		return self._instance.IGetLineInfo

	@i_get_line_info.setter
	def i_get_line_info(self, value):
		"""Gets the vertices of the section line."""
		self._instance.IGetLineInfo = value

	@property
	def i_get_line_segment_count(self):
		"""Gets the number of line segments making up this section line."""
		return self._instance.IGetLineSegmentCount

	@i_get_line_segment_count.setter
	def i_get_line_segment_count(self, value):
		"""Gets the number of line segments making up this section line."""
		self._instance.IGetLineSegmentCount = value

	@property
	def i_get_section_view(self):
		"""Gets the section view of this section cut."""
		return self._instance.IGetSectionView

	@i_get_section_view.setter
	def i_get_section_view(self, value):
		"""Gets the section view of this section cut."""
		self._instance.IGetSectionView = value

	@property
	def i_get_text_format(self):
		"""Gets the text format for the text for this section line."""
		return self._instance.IGetTextFormat

	@i_get_text_format.setter
	def i_get_text_format(self, value):
		"""Gets the text format for the text for this section line."""
		self._instance.IGetTextFormat = value

	@property
	def i_get_text_info(self):
		"""Gets the location of the section line text."""
		return self._instance.IGetTextInfo

	@i_get_text_info.setter
	def i_get_text_info(self, value):
		"""Gets the location of the section line text."""
		self._instance.IGetTextInfo = value

	@property
	def i_get_view(self):
		"""Gets the drawing view where the section line appears."""
		return self._instance.IGetView

	@i_get_view.setter
	def i_get_view(self, value):
		"""Gets the drawing view where the section line appears."""
		self._instance.IGetView = value

	@property
	def is_aligned(self):
		"""Gets whether this is an aligned section view."""
		return self._instance.IsAligned

	@is_aligned.setter
	def is_aligned(self, value):
		"""Gets whether this is an aligned section view."""
		self._instance.IsAligned = value

	@property
	def i_set_excluded_components(self):
		"""Excludes the specified components from this section view."""
		return self._instance.ISetExcludedComponents

	@i_set_excluded_components.setter
	def i_set_excluded_components(self, value):
		"""Excludes the specified components from this section view."""
		self._instance.ISetExcludedComponents = value

	@property
	def i_set_line_info(self):
		"""Sets the location (both position and arrow heads) of the section line."""
		return self._instance.ISetLineInfo

	@i_set_line_info.setter
	def i_set_line_info(self, value):
		"""Sets the location (both position and arrow heads) of the section line."""
		self._instance.ISetLineInfo = value

	@property
	def i_set_text_format(self):
		"""Sets the text format for the text for this section line."""
		return self._instance.ISetTextFormat

	@i_set_text_format.setter
	def i_set_text_format(self, value):
		"""Sets the text format for the text for this section line."""
		self._instance.ISetTextFormat = value

	@property
	def set_auto_hatch(self):
		"""Sets whether auto hatching is enabled for the section view resulting from this section cut."""
		return self._instance.SetAutoHatch

	@set_auto_hatch.setter
	def set_auto_hatch(self, value):
		"""Sets whether auto hatching is enabled for the section view resulting from this section cut."""
		self._instance.SetAutoHatch = value

	@property
	def set_display_only_speed_pak_bodies(self):
		"""Sets whether to display in this section view only the bodies included in the SpeedPak configuration."""
		return self._instance.SetDisplayOnlySpeedPakBodies

	@set_display_only_speed_pak_bodies.setter
	def set_display_only_speed_pak_bodies(self, value):
		"""Sets whether to display in this section view only the bodies included in the SpeedPak configuration."""
		self._instance.SetDisplayOnlySpeedPakBodies = value

	@property
	def set_display_only_surface_cut(self):
		"""Sets whether to display only the surface cut by the section line."""
		return self._instance.SetDisplayOnlySurfaceCut

	@set_display_only_surface_cut.setter
	def set_display_only_surface_cut(self, value):
		"""Sets whether to display only the surface cut by the section line."""
		self._instance.SetDisplayOnlySurfaceCut = value

	@property
	def set_dont_cut_all_instances(self):
		"""Sets whether all instances of the specified component are uncut in this section view or only in the specified component."""
		return self._instance.SetDontCutAllInstances

	@set_dont_cut_all_instances.setter
	def set_dont_cut_all_instances(self, value):
		"""Sets whether all instances of the specified component are uncut in this section view or only in the specified component."""
		self._instance.SetDontCutAllInstances = value

	@property
	def set_excluded_components(self):
		"""Excludes the specified components from this section view."""
		return self._instance.SetExcludedComponents

	@set_excluded_components.setter
	def set_excluded_components(self, value):
		"""Excludes the specified components from this section view."""
		self._instance.SetExcludedComponents = value

	@property
	def set_label(self):
		"""Sets the label for this section view."""
		return self._instance.SetLabel2

	@set_label.setter
	def set_label(self, value):
		"""Sets the label for this section view."""
		self._instance.SetLabel2 = value

	@property
	def set_line_info(self):
		"""Sets the location (both position and arrow heads) of the section line."""
		return self._instance.SetLineInfo

	@set_line_info.setter
	def set_line_info(self, value):
		"""Sets the location (both position and arrow heads) of the section line."""
		self._instance.SetLineInfo = value

	@property
	def set_partial_section(self):
		"""Sets whether this is a partial section cut."""
		return self._instance.SetPartialSection

	@set_partial_section.setter
	def set_partial_section(self, value):
		"""Sets whether this is a partial section cut."""
		self._instance.SetPartialSection = value

	@property
	def set_reversed_cut_direction(self):
		"""Sets whether the section cut direction is reversed from the default."""
		return self._instance.SetReversedCutDirection

	@set_reversed_cut_direction.setter
	def set_reversed_cut_direction(self, value):
		"""Sets whether the section cut direction is reversed from the default."""
		self._instance.SetReversedCutDirection = value

	@property
	def set_scale_with_model_changes(self):
		"""Sets whether the section line scales with changes to the model."""
		return self._instance.SetScaleWithModelChanges

	@set_scale_with_model_changes.setter
	def set_scale_with_model_changes(self, value):
		"""Sets whether the section line scales with changes to the model."""
		self._instance.SetScaleWithModelChanges = value

	@property
	def set_text_format(self):
		"""Sets the text format for the text for this section line."""
		return self._instance.SetTextFormat

	@set_text_format.setter
	def set_text_format(self, value):
		"""Sets the text format for the text for this section line."""
		self._instance.SetTextFormat = value

