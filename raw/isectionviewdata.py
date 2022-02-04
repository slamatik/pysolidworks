# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.html
class ISectionViewData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def exclude_selected_items(self):
		"""Gets or sets whether to exclude or include the specific bodies in the multibody part or specific components in the assembly in selective sectioning in this section view."""
		return self._instance.ExcludeSelectedItems

	@exclude_selected_items.setter
	def exclude_selected_items(self, value):
		"""Gets or sets whether to exclude or include the specific bodies in the multibody part or specific components in the assembly in selective sectioning in this section view."""
		self._instance.ExcludeSelectedItems = value

	@property
	def first_color(self):
		"""Gets or sets the first color of the section view in the part or assembly."""
		return self._instance.FirstColor

	@first_color.setter
	def first_color(self, value):
		"""Gets or sets the first color of the section view in the part or assembly."""
		self._instance.FirstColor = value

	@property
	def first_offset(self):
		"""Gets or sets the first offset distance of the section view for this part or assembly."""
		return self._instance.FirstOffset

	@first_offset.setter
	def first_offset(self, value):
		"""Gets or sets the first offset distance of the section view for this part or assembly."""
		self._instance.FirstOffset = value

	@property
	def first_plane(self):
		"""Gets or sets the section plane for the first section of the section view for the part or assembly."""
		return self._instance.FirstPlane

	@first_plane.setter
	def first_plane(self, value):
		"""Gets or sets the section plane for the first section of the section view for the part or assembly."""
		self._instance.FirstPlane = value

	@property
	def first_reverse_direction(self):
		"""Gets or sets whether to reverse the first direction of the section view for this part or assembly."""
		return self._instance.FirstReverseDirection

	@first_reverse_direction.setter
	def first_reverse_direction(self, value):
		"""Gets or sets whether to reverse the first direction of the section view for this part or assembly."""
		self._instance.FirstReverseDirection = value

	@property
	def first_rotation_x(self):
		"""Gets or sets the first x rotation of the section view in the part or assembly."""
		return self._instance.FirstRotationX

	@first_rotation_x.setter
	def first_rotation_x(self, value):
		"""Gets or sets the first x rotation of the section view in the part or assembly."""
		self._instance.FirstRotationX = value

	@property
	def first_rotation_y(self):
		"""Gets or sets the first y rotation of the section view in the part or assembly."""
		return self._instance.FirstRotationY

	@first_rotation_y.setter
	def first_rotation_y(self, value):
		"""Gets or sets the first y rotation of the section view in the part or assembly."""
		self._instance.FirstRotationY = value

	@property
	def graphics_only_section(self):
		"""Gets or sets whether to generate a graphics-only section view."""
		return self._instance.GraphicsOnlySection

	@graphics_only_section.setter
	def graphics_only_section(self, value):
		"""Gets or sets whether to generate a graphics-only section view."""
		self._instance.GraphicsOnlySection = value

	@property
	def keep_cap_color(self):
		"""Gets or sets whether to color the caps of section views."""
		return self._instance.KeepCapColor

	@keep_cap_color.setter
	def keep_cap_color(self, value):
		"""Gets or sets whether to color the caps of section views."""
		self._instance.KeepCapColor = value

	@property
	def redraw(self):
		"""Gets or sets whether to have IModelViewManager::CreateSectionView validate and return a status for section bodies instead of section views."""
		return self._instance.Redraw

	@redraw.setter
	def redraw(self, value):
		"""Gets or sets whether to have IModelViewManager::CreateSectionView validate and return a status for section bodies instead of section views."""
		self._instance.Redraw = value

	@property
	def second_color(self):
		"""Gets or sets the second color of the section view in the part or assembly."""
		return self._instance.SecondColor

	@second_color.setter
	def second_color(self, value):
		"""Gets or sets the second color of the section view in the part or assembly."""
		self._instance.SecondColor = value

	@property
	def second_offset(self):
		"""Gets or sets the second offset distance of the section view for this part or assembly."""
		return self._instance.SecondOffset

	@second_offset.setter
	def second_offset(self, value):
		"""Gets or sets the second offset distance of the section view for this part or assembly."""
		self._instance.SecondOffset = value

	@property
	def second_plane(self):
		"""Gets or sets the section plane for the second section of the section view for the part or assembly."""
		return self._instance.SecondPlane

	@second_plane.setter
	def second_plane(self, value):
		"""Gets or sets the section plane for the second section of the section view for the part or assembly."""
		self._instance.SecondPlane = value

	@property
	def second_reverse_direction(self):
		"""Gets or sets whether to reverse the second direction of the section view for this part or assembly."""
		return self._instance.SecondReverseDirection

	@second_reverse_direction.setter
	def second_reverse_direction(self, value):
		"""Gets or sets whether to reverse the second direction of the section view for this part or assembly."""
		self._instance.SecondReverseDirection = value

	@property
	def second_rotation_x(self):
		"""Gets or sets the second x rotation of the section view in the part or assembly."""
		return self._instance.SecondRotationX

	@second_rotation_x.setter
	def second_rotation_x(self, value):
		"""Gets or sets the second x rotation of the section view in the part or assembly."""
		self._instance.SecondRotationX = value

	@property
	def second_rotation_y(self):
		"""Gets or sets the second y rotation of the section view in the part or assembly."""
		return self._instance.SecondRotationY

	@second_rotation_y.setter
	def second_rotation_y(self, value):
		"""Gets or sets the second y rotation of the section view in the part or assembly."""
		self._instance.SecondRotationY = value

	@property
	def sectioned_zones(self):
		"""Gets or sets the intersection zones that define how to section this section view."""
		return self._instance.SectionedZones

	@sectioned_zones.setter
	def sectioned_zones(self, value):
		"""Gets or sets the intersection zones that define how to section this section view."""
		self._instance.SectionedZones = value

	@property
	def section_transparent_items_transparent(self):
		"""Gets or sets whether the specified sectioned bodies in the multibody part or the specified sectioned components in the assembly are transparently sectioned in this section view."""
		return self._instance.SectionTransparentItemsTransparent

	@section_transparent_items_transparent.setter
	def section_transparent_items_transparent(self, value):
		"""Gets or sets whether the specified sectioned bodies in the multibody part or the specified sectioned components in the assembly are transparently sectioned in this section view."""
		self._instance.SectionTransparentItemsTransparent = value

	@property
	def selective_section(self):
		"""Gets or sets whether selective sectioning is enabled in this section view."""
		return self._instance.SelectiveSection

	@selective_section.setter
	def selective_section(self, value):
		"""Gets or sets whether selective sectioning is enabled in this section view."""
		self._instance.SelectiveSection = value

	@property
	def selective_sectioning_list(self):
		"""Gets or sets the bodies in the multibody part or the components in the assembly for selective sectioning in this section view."""
		return self._instance.SelectiveSectioningList

	@selective_sectioning_list.setter
	def selective_sectioning_list(self, value):
		"""Gets or sets the bodies in the multibody part or the components in the assembly for selective sectioning in this section view."""
		self._instance.SelectiveSectioningList = value

	@property
	def show_section_cap(self):
		"""Gets or sets whether to cap the section views."""
		return self._instance.ShowSectionCap

	@show_section_cap.setter
	def show_section_cap(self, value):
		"""Gets or sets whether to cap the section views."""
		self._instance.ShowSectionCap = value

	@property
	def third_color(self):
		"""Gets or sets the third color of the section view in this part or assembly."""
		return self._instance.ThirdColor

	@third_color.setter
	def third_color(self, value):
		"""Gets or sets the third color of the section view in this part or assembly."""
		self._instance.ThirdColor = value

	@property
	def third_offset(self):
		"""Gets or sets the third offset distance of the section view for this part or assembly."""
		return self._instance.ThirdOffset

	@third_offset.setter
	def third_offset(self, value):
		"""Gets or sets the third offset distance of the section view for this part or assembly."""
		self._instance.ThirdOffset = value

	@property
	def third_plane(self):
		"""Gets or sets the section plane for the third section of the section view for the part or assembly."""
		return self._instance.ThirdPlane

	@third_plane.setter
	def third_plane(self, value):
		"""Gets or sets the section plane for the third section of the section view for the part or assembly."""
		self._instance.ThirdPlane = value

	@property
	def third_reverse_direction(self):
		"""Gets or sets whether to reverse the third direction of the section view for this part or assembly."""
		return self._instance.ThirdReverseDirection

	@third_reverse_direction.setter
	def third_reverse_direction(self, value):
		"""Gets or sets whether to reverse the third direction of the section view for this part or assembly."""
		self._instance.ThirdReverseDirection = value

	@property
	def third_rotation_x(self):
		"""Gets or sets the third x rotation of the section view in the part or assembly."""
		return self._instance.ThirdRotationX

	@third_rotation_x.setter
	def third_rotation_x(self, value):
		"""Gets or sets the third x rotation of the section view in the part or assembly."""
		self._instance.ThirdRotationX = value

	@property
	def third_rotation_y(self):
		"""Gets or sets the third y rotation of the section view in the part or assembly."""
		return self._instance.ThirdRotationY

	@third_rotation_y.setter
	def third_rotation_y(self, value):
		"""Gets or sets the third y rotation of the section view in the part or assembly."""
		self._instance.ThirdRotationY = value

	@property
	def transparency_list(self):
		"""Gets or sets the sectioned bodies in the multibody part or the sectioned components in the assembly to transparently section in this section view."""
		return self._instance.TransparencyList

	@transparency_list.setter
	def transparency_list(self, value):
		"""Gets or sets the sectioned bodies in the multibody part or the sectioned components in the assembly to transparently section in this section view."""
		self._instance.TransparencyList = value

	@property
	def transparency_value(self):
		"""Gets or sets the level of transparency for the specified transparently sectioned bodies in the multibody part or the specified transparently sectioned components in the assembly in this section view."""
		return self._instance.TransparencyValue

	@transparency_value.setter
	def transparency_value(self, value):
		"""Gets or sets the level of transparency for the specified transparently sectioned bodies in the multibody part or the specified transparently sectioned components in the assembly in this section view."""
		self._instance.TransparencyValue = value

	@property
	def transparent_section(self):
		"""Gets or sets whether transparent sectioning is enabled in this section view."""
		return self._instance.TransparentSection

	@transparent_section.setter
	def transparent_section(self, value):
		"""Gets or sets whether transparent sectioning is enabled in this section view."""
		self._instance.TransparentSection = value

	@property
	def zonal_section(self):
		"""Gets or sets whether the section method is zonal or planar."""
		return self._instance.ZonalSection

	@zonal_section.setter
	def zonal_section(self, value):
		"""Gets or sets whether the section method is zonal or planar."""
		self._instance.ZonalSection = value

	@property
	def get_dynamic_center_transform(self):
		"""Gets the translation between the center of the model and the plane in the specified section in this section view."""
		return self._instance.GetDynamicCenterTransform

	@get_dynamic_center_transform.setter
	def get_dynamic_center_transform(self, value):
		"""Gets the translation between the center of the model and the plane in the specified section in this section view."""
		self._instance.GetDynamicCenterTransform = value

	@property
	def get_first_plane_parameters(self):
		"""Gets the first transformed plane's parameters for this section view."""
		return self._instance.GetFirstPlaneParameters

	@get_first_plane_parameters.setter
	def get_first_plane_parameters(self, value):
		"""Gets the first transformed plane's parameters for this section view."""
		self._instance.GetFirstPlaneParameters = value

	@property
	def get_second_plane_parameters(self):
		"""Gets the second transformed plane's parameters for this section view."""
		return self._instance.GetSecondPlaneParameters

	@get_second_plane_parameters.setter
	def get_second_plane_parameters(self, value):
		"""Gets the second transformed plane's parameters for this section view."""
		self._instance.GetSecondPlaneParameters = value

	@property
	def get_third_plane_parameters(self):
		"""Gets the third transformed plane's parameters for this section view."""
		return self._instance.GetThirdPlaneParameters

	@get_third_plane_parameters.setter
	def get_third_plane_parameters(self, value):
		"""Gets the third transformed plane's parameters for this section view."""
		self._instance.GetThirdPlaneParameters = value

