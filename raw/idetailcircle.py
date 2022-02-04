# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html
class IDetailCircle:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def jagged_outline(self):
		"""Gets or sets whether to show a jagged outline in the detail view."""
		return self._instance.JaggedOutline

	@jagged_outline.setter
	def jagged_outline(self, value):
		"""Gets or sets whether to show a jagged outline in the detail view."""
		self._instance.JaggedOutline = value

	@property
	def layer(self):
		"""Gets or sets the layer on which the detail circle is on."""
		return self._instance.Layer

	@layer.setter
	def layer(self, value):
		"""Gets or sets the layer on which the detail circle is on."""
		self._instance.Layer = value

	@property
	def no_outline(self):
		"""Gets or sets whether to show an outline in the detail view."""
		return self._instance.NoOutline

	@no_outline.setter
	def no_outline(self, value):
		"""Gets or sets whether to show an outline in the detail view."""
		self._instance.NoOutline = value

	@property
	def pin_position(self):
		"""Sets the pin position for this detail circle."""
		return self._instance.PinPosition

	@pin_position.setter
	def pin_position(self, value):
		"""Sets the pin position for this detail circle."""
		self._instance.PinPosition = value

	@property
	def scale_hatch_pattern(self):
		"""Gets or sets whether to scale the hatch pattern for this detail circle."""
		return self._instance.ScaleHatchPattern

	@scale_hatch_pattern.setter
	def scale_hatch_pattern(self, value):
		"""Gets or sets whether to scale the hatch pattern for this detail circle."""
		self._instance.ScaleHatchPattern = value

	@property
	def shape_intensity(self):
		"""Gets or sets the shape intensity of the jagged outline in the detail view."""
		return self._instance.ShapeIntensity

	@shape_intensity.setter
	def shape_intensity(self, value):
		"""Gets or sets the shape intensity of the jagged outline in the detail view."""
		self._instance.ShapeIntensity = value

	@property
	def get_arrow_info(self):
		"""Gets the position of the arrows for this detail circle."""
		return self._instance.GetArrowInfo

	@get_arrow_info.setter
	def get_arrow_info(self, value):
		"""Gets the position of the arrows for this detail circle."""
		self._instance.GetArrowInfo = value

	@property
	def get_connecting_line(self):
		"""Gets the end point coordinates of the connecting line for this detail circle."""
		return self._instance.GetConnectingLine

	@get_connecting_line.setter
	def get_connecting_line(self, value):
		"""Gets the end point coordinates of the connecting line for this detail circle."""
		self._instance.GetConnectingLine = value

	@property
	def get_detail_view(self):
		"""Gets the drawing view of this detail circle."""
		return self._instance.GetDetailView

	@get_detail_view.setter
	def get_detail_view(self, value):
		"""Gets the drawing view of this detail circle."""
		self._instance.GetDetailView = value

	@property
	def get_display(self):
		"""Gets the type of circle or profile used to create the detail."""
		return self._instance.GetDisplay

	@get_display.setter
	def get_display(self, value):
		"""Gets the type of circle or profile used to create the detail."""
		self._instance.GetDisplay = value

	@property
	def get_label(self):
		"""Gets the label for this detail circle."""
		return self._instance.GetLabel

	@get_label.setter
	def get_label(self, value):
		"""Gets the label for this detail circle."""
		self._instance.GetLabel = value

	@property
	def get_label_position(self):
		"""Gets the position of the label of this detail circle."""
		return self._instance.GetLabelPosition

	@get_label_position.setter
	def get_label_position(self, value):
		"""Gets the position of the label of this detail circle."""
		self._instance.GetLabelPosition = value

	@property
	def get_leader_info(self):
		"""Gets the leader information for this detail circle."""
		return self._instance.GetLeaderInfo

	@get_leader_info.setter
	def get_leader_info(self, value):
		"""Gets the leader information for this detail circle."""
		self._instance.GetLeaderInfo = value

	@property
	def get_name(self):
		"""Gets the name of this detail circle."""
		return self._instance.GetName

	@get_name.setter
	def get_name(self, value):
		"""Gets the name of this detail circle."""
		self._instance.GetName = value

	@property
	def get_profile_items(self):
		"""Gets the sketch segments that make up this detail circle profile."""
		return self._instance.GetProfileItems

	@get_profile_items.setter
	def get_profile_items(self, value):
		"""Gets the sketch segments that make up this detail circle profile."""
		self._instance.GetProfileItems = value

	@property
	def get_profile_items_count(self):
		"""Gets the number of sketch segments that make up this detail circle profile."""
		return self._instance.GetProfileItemsCount

	@get_profile_items_count.setter
	def get_profile_items_count(self, value):
		"""Gets the number of sketch segments that make up this detail circle profile."""
		self._instance.GetProfileItemsCount = value

	@property
	def get_style(self):
		"""Gets the style of this detail circle."""
		return self._instance.GetStyle

	@get_style.setter
	def get_style(self, value):
		"""Gets the style of this detail circle."""
		self._instance.GetStyle = value

	@property
	def get_text_format(self):
		"""Gets the text format for this detail circle."""
		return self._instance.GetTextFormat

	@get_text_format.setter
	def get_text_format(self, value):
		"""Gets the text format for this detail circle."""
		self._instance.GetTextFormat = value

	@property
	def get_use_doc_text_format(self):
		"""Gets whether or not SOLIDWORKS is currently using the document default setting for text format."""
		return self._instance.GetUseDocTextFormat

	@get_use_doc_text_format.setter
	def get_use_doc_text_format(self, value):
		"""Gets whether or not SOLIDWORKS is currently using the document default setting for text format."""
		self._instance.GetUseDocTextFormat = value

	@property
	def get_view(self):
		"""Gets the the drawing view that displays this detail circle."""
		return self._instance.GetView

	@get_view.setter
	def get_view(self, value):
		"""Gets the the drawing view that displays this detail circle."""
		self._instance.GetView = value

	@property
	def has_full_outline(self):
		"""Gets whether this detail circle has a full outline in the detail view."""
		return self._instance.HasFullOutline

	@has_full_outline.setter
	def has_full_outline(self, value):
		"""Gets whether this detail circle has a full outline in the detail view."""
		self._instance.HasFullOutline = value

	@property
	def i_get_arrow_info(self):
		"""Gets the position of the arrows for this detail circle."""
		return self._instance.IGetArrowInfo

	@i_get_arrow_info.setter
	def i_get_arrow_info(self, value):
		"""Gets the position of the arrows for this detail circle."""
		self._instance.IGetArrowInfo = value

	@property
	def i_get_connecting_line(self):
		"""Gets the end point coordinates of the connecting line"""
		return self._instance.IGetConnectingLine

	@i_get_connecting_line.setter
	def i_get_connecting_line(self, value):
		"""Gets the end point coordinates of the connecting line"""
		self._instance.IGetConnectingLine = value

	@property
	def i_get_leader_info(self):
		"""Gets the leader information for this detail circle."""
		return self._instance.IGetLeaderInfo

	@i_get_leader_info.setter
	def i_get_leader_info(self, value):
		"""Gets the leader information for this detail circle."""
		self._instance.IGetLeaderInfo = value

	@property
	def i_get_profile_items(self):
		"""Gets the sketch segments that make up this detail circle profile."""
		return self._instance.IGetProfileItems

	@i_get_profile_items.setter
	def i_get_profile_items(self, value):
		"""Gets the sketch segments that make up this detail circle profile."""
		self._instance.IGetProfileItems = value

	@property
	def select(self):
		"""Selects the detail circle."""
		return self._instance.Select

	@select.setter
	def select(self, value):
		"""Selects the detail circle."""
		self._instance.Select = value

	@property
	def set_display(self):
		"""Sets the display of the detail circle to a circle or to the profile."""
		return self._instance.SetDisplay

	@set_display.setter
	def set_display(self, value):
		"""Sets the display of the detail circle to a circle or to the profile."""
		self._instance.SetDisplay = value

	@property
	def set_full_outline(self):
		"""Sets whether the complete detail circle or detail profile is shown in the detail view, or if just the part of the circle or profile that intersects the view geometry is shown."""
		return self._instance.SetFullOutline

	@set_full_outline.setter
	def set_full_outline(self, value):
		"""Sets whether the complete detail circle or detail profile is shown in the detail view, or if just the part of the circle or profile that intersects the view geometry is shown."""
		self._instance.SetFullOutline = value

	@property
	def set_label(self):
		"""Sets the label for this detail circle."""
		return self._instance.SetLabel

	@set_label.setter
	def set_label(self, value):
		"""Sets the label for this detail circle."""
		self._instance.SetLabel = value

	@property
	def set_label_position(self):
		"""Sets the position of the label for this detail circle."""
		return self._instance.SetLabelPosition

	@set_label_position.setter
	def set_label_position(self, value):
		"""Sets the position of the label for this detail circle."""
		self._instance.SetLabelPosition = value

	@property
	def set_name(self):
		"""Sets the name of this detail circle, as displayed in the FeatureManager design tree."""
		return self._instance.SetName

	@set_name.setter
	def set_name(self, value):
		"""Sets the name of this detail circle, as displayed in the FeatureManager design tree."""
		self._instance.SetName = value

	@property
	def set_parameters(self):
		"""Sets the location and size of this detail circle."""
		return self._instance.SetParameters

	@set_parameters.setter
	def set_parameters(self, value):
		"""Sets the location and size of this detail circle."""
		self._instance.SetParameters = value

	@property
	def set_style(self):
		"""Sets the style of the detail circle (for example, standard, broken, leader, no leader, or connected)."""
		return self._instance.SetStyle

	@set_style.setter
	def set_style(self, value):
		"""Sets the style of the detail circle (for example, standard, broken, leader, no leader, or connected)."""
		self._instance.SetStyle = value

	@property
	def set_text_format(self):
		"""Sets the text format for this detail circle."""
		return self._instance.SetTextFormat

	@set_text_format.setter
	def set_text_format(self, value):
		"""Sets the text format for this detail circle."""
		self._instance.SetTextFormat = value

