# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.html
class IRenderMaterial:
	def __init__(self, parent=None):
		self._instance = parent

	def accurate_reflections(self):
		"""Selects or clears the Accurate reflections (slower) setting, which controls the level of surface reflections, for illuminating this appearance."""
		# return self._instance.AccurateReflections
		raise NotImplemented

	@property
	def ambient(self):
		"""Gets or sets the ambient light intensity for illuminating this appearance."""
		return self._instance.Ambient

	@ambient.setter
	def ambient(self, value):
		"""Gets or sets the ambient light intensity for illuminating this appearance."""
		self._instance.Ambient = value

	@property
	def anisotropic_bias(self):
		"""Gets or sets the anisotropic bias, which makes the effect of light on the surface stronger in the horizontal or vertical direction, for illuminating this appearance."""
		return self._instance.AnisotropicBias

	@anisotropic_bias.setter
	def anisotropic_bias(self, value):
		"""Gets or sets the anisotropic bias, which makes the effect of light on the surface stronger in the horizontal or vertical direction, for illuminating this appearance."""
		self._instance.AnisotropicBias = value

	@property
	def anisotropic_cylinder_distance(self):
		"""Gets or sets the anisotropic cylinder distance for illuminating this appearance."""
		return self._instance.AnisotropicCylinderDistance

	@anisotropic_cylinder_distance.setter
	def anisotropic_cylinder_distance(self, value):
		"""Gets or sets the anisotropic cylinder distance for illuminating this appearance."""
		self._instance.AnisotropicCylinderDistance = value

	@property
	def anisotropic_floor_height(self):
		"""Gets or sets the anisotropic floor height for illuminating this appearance."""
		return self._instance.AnisotropicFloorHeight

	@anisotropic_floor_height.setter
	def anisotropic_floor_height(self, value):
		"""Gets or sets the anisotropic floor height for illuminating this appearance."""
		self._instance.AnisotropicFloorHeight = value

	@property
	def brightness(self):
		"""Gets or sets how emissive the material is for the Constant illumination type for this appearance."""
		return self._instance.Brightness

	@brightness.setter
	def brightness(self, value):
		"""Gets or sets how emissive the material is for the Constant illumination type for this appearance."""
		self._instance.Brightness = value

	@property
	def bump_amplitude(self):
		"""Gets or sets the amplitude of the surface layer for this appearance."""
		return self._instance.BumpAmplitude

	@bump_amplitude.setter
	def bump_amplitude(self, value):
		"""Gets or sets the amplitude of the surface layer for this appearance."""
		self._instance.BumpAmplitude = value

	@property
	def bump_blend(self):
		"""Gets or sets the blend, which is the extent of the boundary between each bump and the surface, of the surface finish for this appearance."""
		return self._instance.BumpBlend

	@bump_blend.setter
	def bump_blend(self, value):
		"""Gets or sets the blend, which is the extent of the boundary between each bump and the surface, of the surface finish for this appearance."""
		self._instance.BumpBlend = value

	@property
	def bump_detail(self):
		"""Gets or sets the level of granularity for any surface finish for this appearance."""
		return self._instance.BumpDetail

	@bump_detail.setter
	def bump_detail(self, value):
		"""Gets or sets the level of granularity for any surface finish for this appearance."""
		self._instance.BumpDetail = value

	@property
	def bump_map(self):
		"""Gets or sets the type of surface finish for the appearance."""
		return self._instance.BumpMap

	@bump_map.setter
	def bump_map(self, value):
		"""Gets or sets the type of surface finish for the appearance."""
		self._instance.BumpMap = value

	@property
	def bump_radius(self):
		"""Gets or sets the radius, which controls the relative size and spacing of bumps for dimpled and tread plate styles, of the surface finish for this appearance."""
		return self._instance.BumpRadius

	@bump_radius.setter
	def bump_radius(self, value):
		"""Gets or sets the radius, which controls the relative size and spacing of bumps for dimpled and tread plate styles, of the surface finish for this appearance."""
		self._instance.BumpRadius = value

	@property
	def bump_rough_high(self):
		"""Gets or sets the high threshold of the surface finish for this appearance."""
		return self._instance.BumpRoughHigh

	@bump_rough_high.setter
	def bump_rough_high(self, value):
		"""Gets or sets the high threshold of the surface finish for this appearance."""
		self._instance.BumpRoughHigh = value

	@property
	def bump_rough_low(self):
		"""Gets or sets the low threshold of the surface finish for this appearance."""
		return self._instance.BumpRoughLow

	@bump_rough_low.setter
	def bump_rough_low(self, value):
		"""Gets or sets the low threshold of the surface finish for this appearance."""
		self._instance.BumpRoughLow = value

	@property
	def bump_scale(self):
		"""Gets or sets the scale for the surface-finish pattern incidence for this appearance."""
		return self._instance.BumpScale

	@bump_scale.setter
	def bump_scale(self, value):
		"""Gets or sets the scale for the surface-finish pattern incidence for this appearance."""
		self._instance.BumpScale = value

	@property
	def bump_sharpness(self):
		"""Gets or sets the sharpness, which influences the shape of the surface finish, of this appearance."""
		return self._instance.BumpSharpness

	@bump_sharpness.setter
	def bump_sharpness(self, value):
		"""Gets or sets the sharpness, which influences the shape of the surface finish, of this appearance."""
		self._instance.BumpSharpness = value

	@property
	def bump_texture_filename(self):
		"""Gets or sets the path and file name of the pattern based on an image file for the surface finish of this appearance."""
		return self._instance.BumpTextureFilename

	@bump_texture_filename.setter
	def bump_texture_filename(self, value):
		"""Gets or sets the path and file name of the pattern based on an image file for the surface finish of this appearance."""
		self._instance.BumpTextureFilename = value

	@property
	def bump_use_mapping_scale(self):
		"""Gets or sets whether to use the material's scale and mapping for the surface finish of this appearance."""
		return self._instance.BumpUseMappingScale

	@bump_use_mapping_scale.setter
	def bump_use_mapping_scale(self, value):
		"""Gets or sets whether to use the material's scale and mapping for the surface finish of this appearance."""
		self._instance.BumpUseMappingScale = value

	@property
	def caustics_cast(self):
		"""Gets or sets whether specular materials reflect caustic photons for illuminating this appearance."""
		return self._instance.CausticsCast

	@caustics_cast.setter
	def caustics_cast(self, value):
		"""Gets or sets whether specular materials reflect caustic photons for illuminating this appearance."""
		self._instance.CausticsCast = value

	@property
	def caustics_receive(self):
		"""Gets or sets whether diffuse materials absorb caustic photons for illuminating this appearance."""
		return self._instance.CausticsReceive

	@caustics_receive.setter
	def caustics_receive(self, value):
		"""Gets or sets whether diffuse materials absorb caustic photons for illuminating this appearance."""
		self._instance.CausticsReceive = value

	@property
	def color_form(self):
		"""Gets or sets the number of colors required to describe the appearance ."""
		return self._instance.ColorForm

	@color_form.setter
	def color_form(self, value):
		"""Gets or sets the number of colors required to describe the appearance ."""
		self._instance.ColorForm = value

	@property
	def density_of_holes(self):
		"""Gets or sets the density of the holes of the mesh in corroded or eroded materials for illuminating this appearance."""
		return self._instance.DensityOfHoles

	@density_of_holes.setter
	def density_of_holes(self, value):
		"""Gets or sets the density of the holes of the mesh in corroded or eroded materials for illuminating this appearance."""
		self._instance.DensityOfHoles = value

	@property
	def diffuse(self):
		"""Gets or sets the intensity of a light source illuminating a surface from all directions without attenuation or shadowing for this appearance."""
		return self._instance.Diffuse

	@diffuse.setter
	def diffuse(self, value):
		"""Gets or sets the intensity of a light source illuminating a surface from all directions without attenuation or shadowing for this appearance."""
		self._instance.Diffuse = value

	@property
	def direction_rotation_angle(self):
		"""Gets or sets the angle at which to rotate the texture relative to the horizontal axis for mapping this appearance."""
		return self._instance.Direction1RotationAngle

	@direction_rotation_angle.setter
	def direction_rotation_angle(self, value):
		"""Gets or sets the angle at which to rotate the texture relative to the horizontal axis for mapping this appearance."""
		self._instance.Direction1RotationAngle = value

	@property
	def direction_rotation_angle(self):
		"""Gets or sets the angle at which to rotate the texture relative to the vertical axis for mapping this appearance."""
		return self._instance.Direction2RotationAngle

	@direction_rotation_angle.setter
	def direction_rotation_angle(self, value):
		"""Gets or sets the angle at which to rotate the texture relative to the vertical axis for mapping this appearance."""
		self._instance.Direction2RotationAngle = value

	@property
	def double_sided(self):
		"""Gets or sets whether to enable shading from both sides of a surface when rendering a model with PhotoView 360."""
		return self._instance.DoubleSided

	@double_sided.setter
	def double_sided(self, value):
		"""Gets or sets whether to enable shading from both sides of a surface when rendering a model with PhotoView 360."""
		self._instance.DoubleSided = value

	@property
	def emission(self):
		"""Gets or sets how much light is projected from the appearance."""
		return self._instance.Emission

	@emission.setter
	def emission(self, value):
		"""Gets or sets how much light is projected from the appearance."""
		self._instance.Emission = value

	@property
	def file_name(self):
		"""Gets or sets the path and file name (.p2m) of the appearance."""
		return self._instance.FileName

	@file_name.setter
	def file_name(self, value):
		"""Gets or sets the path and file name (.p2m) of the appearance."""
		self._instance.FileName = value

	@property
	def fit_height(self):
		"""Gets or sets whether to stretch the height of the appearance texture to the selected entity when mapping the appearance."""
		return self._instance.FitHeight

	@fit_height.setter
	def fit_height(self, value):
		"""Gets or sets whether to stretch the height of the appearance texture to the selected entity when mapping the appearance."""
		self._instance.FitHeight = value

	@property
	def fit_width(self):
		"""Gets or sets whether to stretch the width of the appearance texture to the selected entity when mapping the appearance."""
		return self._instance.FitWidth

	@fit_width.setter
	def fit_width(self, value):
		"""Gets or sets whether to stretch the width of the appearance texture to the selected entity when mapping the appearance."""
		self._instance.FitWidth = value

	@property
	def fixed_aspect_ratio(self):
		"""Gets or sets whether the aspect ratio is fixed for mapping this appearance texture."""
		return self._instance.FixedAspectRatio

	@fixed_aspect_ratio.setter
	def fixed_aspect_ratio(self, value):
		"""Gets or sets whether the aspect ratio is fixed for mapping this appearance texture."""
		self._instance.FixedAspectRatio = value

	@property
	def global_illumination_cast(self):
		"""Gets whether specular materials reflect photons for illuminating this appearance.."""
		return self._instance.GlobalIlluminationCast

	@global_illumination_cast.setter
	def global_illumination_cast(self, value):
		"""Gets whether specular materials reflect photons for illuminating this appearance.."""
		self._instance.GlobalIlluminationCast = value

	@property
	def global_illumination_receive(self):
		"""Gets or sets whether diffuse materials absorb photons for illuminating this appearance."""
		return self._instance.GlobalIlluminationReceive

	@global_illumination_receive.setter
	def global_illumination_receive(self, value):
		"""Gets or sets whether diffuse materials absorb photons for illuminating this appearance."""
		self._instance.GlobalIlluminationReceive = value

	@property
	def glossy(self):
		"""Gets or sets the specular factor of the lights reflected by the appearance."""
		return self._instance.Glossy

	@glossy.setter
	def glossy(self, value):
		"""Gets or sets the specular factor of the lights reflected by the appearance."""
		self._instance.Glossy = value

	@property
	def height(self):
		"""Gets or sets the height for mapping this appearance texture."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height for mapping this appearance texture."""
		self._instance.Height = value

	@property
	def height_mirror(self):
		"""Gets or sets whether to flip the appearance texture about the selected direction vertically."""
		return self._instance.HeightMirror

	@height_mirror.setter
	def height_mirror(self, value):
		"""Gets or sets whether to flip the appearance texture about the selected direction vertically."""
		self._instance.HeightMirror = value

	@property
	def ignore_missing_file(self):
		"""Gets or sets whether to ignore any missing image file warnings."""
		return self._instance.IgnoreMissingFile

	@ignore_missing_file.setter
	def ignore_missing_file(self, value):
		"""Gets or sets whether to ignore any missing image file warnings."""
		self._instance.IgnoreMissingFile = value

	@property
	def illumination_shader_type(self):
		"""Gets or sets the type of illumination of the appearance."""
		return self._instance.IlluminationShaderType

	@illumination_shader_type.setter
	def illumination_shader_type(self, value):
		"""Gets or sets the type of illumination of the appearance."""
		self._instance.IlluminationShaderType = value

	@property
	def index_of_refraction(self):
		"""Gets or sets the index of refraction for illuminating this appearance."""
		return self._instance.IndexOfRefraction

	@index_of_refraction.setter
	def index_of_refraction(self, value):
		"""Gets or sets the index of refraction for illuminating this appearance."""
		self._instance.IndexOfRefraction = value

	@property
	def link_to_file(self):
		"""Gets or sets whether to link instances of the appearance to an appearance file (.p2m)."""
		return self._instance.LinkToFile

	@link_to_file.setter
	def link_to_file(self, value):
		"""Gets or sets whether to link instances of the appearance to an appearance file (.p2m)."""
		self._instance.LinkToFile = value

	@property
	def mapping_type(self):
		"""Gets or sets the mapping type for this appearance."""
		return self._instance.MappingType

	@mapping_type.setter
	def mapping_type(self, value):
		"""Gets or sets the mapping type for this appearance."""
		self._instance.MappingType = value

	@property
	def material_i_d(self):
		"""Not supported in SOLIDWORKS 2011 and later. Superseded by IRenderMaterial::GetMaterialIds."""
		return self._instance.MaterialID

	@material_i_d.setter
	def material_i_d(self, value):
		"""Not supported in SOLIDWORKS 2011 and later. Superseded by IRenderMaterial::GetMaterialIds."""
		self._instance.MaterialID = value

	@property
	def metallic_amplitude(self):
		"""Gets or sets the amplitude of the metallic flakes for illuminating the appearance."""
		return self._instance.MetallicAmplitude

	@metallic_amplitude.setter
	def metallic_amplitude(self, value):
		"""Gets or sets the amplitude of the metallic flakes for illuminating the appearance."""
		self._instance.MetallicAmplitude = value

	@property
	def metallic_flake_material(self):
		"""Gets or sets the metallic flake material for illuminating the appearance."""
		return self._instance.MetallicFlakeMaterial

	@metallic_flake_material.setter
	def metallic_flake_material(self, value):
		"""Gets or sets the metallic flake material for illuminating the appearance."""
		self._instance.MetallicFlakeMaterial = value

	@property
	def metallic_mix(self):
		"""Gets or sets the metallic quality of a material for illuminating the appearance."""
		return self._instance.MetallicMix

	@metallic_mix.setter
	def metallic_mix(self, value):
		"""Gets or sets the metallic quality of a material for illuminating the appearance."""
		self._instance.MetallicMix = value

	@property
	def metallic_roughness(self):
		"""Gets or sets the size (coarseness) any highlights on the surface for illuminating the appearance."""
		return self._instance.MetallicRoughness

	@metallic_roughness.setter
	def metallic_roughness(self, value):
		"""Gets or sets the size (coarseness) any highlights on the surface for illuminating the appearance."""
		self._instance.MetallicRoughness = value

	@property
	def metallic_scale(self):
		"""Gets or sets the size of the metallic flakes in the metallic layer for illuminating the appearance."""
		return self._instance.MetallicScale

	@metallic_scale.setter
	def metallic_scale(self, value):
		"""Gets or sets the size of the metallic flakes in the metallic layer for illuminating the appearance."""
		self._instance.MetallicScale = value

	@property
	def n_samples(self):
		"""Gets or sets the number of samples used to calculate the contribution of the glossy component for illuminating the appearance."""
		return self._instance.NSamples

	@n_samples.setter
	def n_samples(self, value):
		"""Gets or sets the number of samples used to calculate the contribution of the glossy component for illuminating the appearance."""
		self._instance.NSamples = value

	@property
	def object_area_light(self):
		"""Gets or sets whether the appearance is an object area light or whether it has realistic falloff, or both."""
		return self._instance.ObjectAreaLight

	@object_area_light.setter
	def object_area_light(self, value):
		"""Gets or sets whether the appearance is an object area light or whether it has realistic falloff, or both."""
		self._instance.ObjectAreaLight = value

	@property
	def pattern_scale(self):
		"""Gets or sets the pattern scale of procedural textures for mapping the appearance."""
		return self._instance.PatternScale

	@pattern_scale.setter
	def pattern_scale(self, value):
		"""Gets or sets the pattern scale of procedural textures for mapping the appearance."""
		self._instance.PatternScale = value

	@property
	def primary_color(self):
		"""Gets or sets the primary color of the appearance."""
		return self._instance.PrimaryColor

	@primary_color.setter
	def primary_color(self, value):
		"""Gets or sets the primary color of the appearance."""
		self._instance.PrimaryColor = value

	@property
	def projection_reference(self):
		"""Gets or sets the projection direction for mapping the appearance."""
		return self._instance.ProjectionReference

	@projection_reference.setter
	def projection_reference(self, value):
		"""Gets or sets the projection direction for mapping the appearance."""
		self._instance.ProjectionReference = value

	@property
	def reflectivity(self):
		"""Gets or sets the reflectivity for illuminating the appearance."""
		return self._instance.Reflectivity

	@reflectivity.setter
	def reflectivity(self, value):
		"""Gets or sets the reflectivity for illuminating the appearance."""
		self._instance.Reflectivity = value

	@property
	def rotation_angle(self):
		"""Gets or sets the angle by which to rotate the texture relative to the axes for mapping this appearance."""
		return self._instance.RotationAngle

	@rotation_angle.setter
	def rotation_angle(self, value):
		"""Gets or sets the angle by which to rotate the texture relative to the axes for mapping this appearance."""
		self._instance.RotationAngle = value

	@property
	def roughness(self):
		"""Gets or sets the specular spread (roughness) of the appearance."""
		return self._instance.Roughness

	@roughness.setter
	def roughness(self, value):
		"""Gets or sets the specular spread (roughness) of the appearance."""
		self._instance.Roughness = value

	@property
	def round_sharp_edges(self):
		"""Gets or sets the value by which to round sharp edges when rendering a model with PhotoView 360."""
		return self._instance.RoundSharpEdges

	@round_sharp_edges.setter
	def round_sharp_edges(self, value):
		"""Gets or sets the value by which to round sharp edges when rendering a model with PhotoView 360."""
		self._instance.RoundSharpEdges = value

	@property
	def secondary_color(self):
		"""Gets or sets the secondary color of the appearance."""
		return self._instance.SecondaryColor

	@secondary_color.setter
	def secondary_color(self, value):
		"""Gets or sets the secondary color of the appearance."""
		self._instance.SecondaryColor = value

	@property
	def specular(self):
		"""Gets or sets the intensity of the light surface for illuminating the appearance."""
		return self._instance.Specular

	@specular.setter
	def specular(self, value):
		"""Gets or sets the intensity of the light surface for illuminating the appearance."""
		self._instance.Specular = value

	@property
	def specular_color(self):
		"""Gets or sets the specular color for illuminating this appearance."""
		return self._instance.SpecularColor

	@specular_color.setter
	def specular_color(self, value):
		"""Gets or sets the specular color for illuminating this appearance."""
		self._instance.SpecularColor = value

	@property
	def tertiary_color(self):
		"""Gets or sets the tertiary color of the appearance."""
		return self._instance.TertiaryColor

	@tertiary_color.setter
	def tertiary_color(self, value):
		"""Gets or sets the tertiary color of the appearance."""
		self._instance.TertiaryColor = value

	@property
	def texture_filename(self):
		"""Gets or sets the path and filename of the texture for this appearance."""
		return self._instance.TextureFilename

	@texture_filename.setter
	def texture_filename(self, value):
		"""Gets or sets the path and filename of the texture for this appearance."""
		self._instance.TextureFilename = value

	@property
	def toon_shader_texture_filename(self):
		"""Gets or sets the path and filename for the toon shader texture file."""
		return self._instance.ToonShaderTextureFilename

	@toon_shader_texture_filename.setter
	def toon_shader_texture_filename(self, value):
		"""Gets or sets the path and filename for the toon shader texture file."""
		self._instance.ToonShaderTextureFilename = value

	@property
	def translucency(self):
		"""Gets or sets the degree to which the material is able to filter and diffuse light for illuminating the appearance."""
		return self._instance.Translucency

	@translucency.setter
	def translucency(self, value):
		"""Gets or sets the degree to which the material is able to filter and diffuse light for illuminating the appearance."""
		self._instance.Translucency = value

	@property
	def transparency(self):
		"""Gets or sets the degree to which a material allows light to pass through for illuminating the appearance."""
		return self._instance.Transparency

	@transparency.setter
	def transparency(self, value):
		"""Gets or sets the degree to which a material allows light to pass through for illuminating the appearance."""
		self._instance.Transparency = value

	@property
	def width(self):
		"""Gets or sets the width for mapping this appearance texture."""
		return self._instance.Width

	@width.setter
	def width(self, value):
		"""Gets or sets the width for mapping this appearance texture."""
		self._instance.Width = value

	@property
	def width_mirror(self):
		"""Gets or sets whether to flip the appearance texture about the selected direction horizontally."""
		return self._instance.WidthMirror

	@width_mirror.setter
	def width_mirror(self, value):
		"""Gets or sets whether to flip the appearance texture about the selected direction horizontally."""
		self._instance.WidthMirror = value

	@property
	def x_position(self):
		"""Gets or sets the X offset direction for the appearance."""
		return self._instance.XPosition

	@x_position.setter
	def x_position(self, value):
		"""Gets or sets the X offset direction for the appearance."""
		self._instance.XPosition = value

	@property
	def y_position(self):
		"""Gets or sets the Y offset direction for the appearance."""
		return self._instance.YPosition

	@y_position.setter
	def y_position(self, value):
		"""Gets or sets the Y offset direction for the appearance."""
		self._instance.YPosition = value

	@property
	def add_entity(self):
		"""Adds the appearance to the specified entity."""
		return self._instance.AddEntity

	@add_entity.setter
	def add_entity(self, value):
		"""Adds the appearance to the specified entity."""
		self._instance.AddEntity = value

	@property
	def get_center_point(self):
		"""Gets the center point of the mapping for texture-based appearances."""
		return self._instance.GetCenterPoint2

	@get_center_point.setter
	def get_center_point(self, value):
		"""Gets the center point of the mapping for texture-based appearances."""
		self._instance.GetCenterPoint2 = value

	@property
	def get_entities(self):
		"""Gets the entities on which this appearance is applied."""
		return self._instance.GetEntities

	@get_entities.setter
	def get_entities(self, value):
		"""Gets the entities on which this appearance is applied."""
		self._instance.GetEntities = value

	@property
	def get_entities_count(self):
		"""Gets the number of entities on which this appearance was applied."""
		return self._instance.GetEntitiesCount

	@get_entities_count.setter
	def get_entities_count(self, value):
		"""Gets the number of entities on which this appearance was applied."""
		self._instance.GetEntitiesCount = value

	@property
	def get_linked_display_states(self):
		"""Gets the display states to which this appearance is applied."""
		return self._instance.GetLinkedDisplayStates

	@get_linked_display_states.setter
	def get_linked_display_states(self, value):
		"""Gets the display states to which this appearance is applied."""
		self._instance.GetLinkedDisplayStates = value

	@property
	def get_material_ids(self):
		"""Gets the material IDs of an appearance."""
		return self._instance.GetMaterialIds

	@get_material_ids.setter
	def get_material_ids(self, value):
		"""Gets the material IDs of an appearance."""
		self._instance.GetMaterialIds = value

	@property
	def get_u_direction(self):
		"""Gets the U direction of the texture-based appearance."""
		return self._instance.GetUDirection2

	@get_u_direction.setter
	def get_u_direction(self, value):
		"""Gets the U direction of the texture-based appearance."""
		self._instance.GetUDirection2 = value

	@property
	def get_v_direction(self):
		"""Gets the V direction of the texture-based appearance."""
		return self._instance.GetVDirection2

	@get_v_direction.setter
	def get_v_direction(self, value):
		"""Gets the V direction of the texture-based appearance."""
		self._instance.GetVDirection2 = value

	@property
	def i_get_entities(self):
		"""Gets the entities on which this appearance is applied."""
		return self._instance.IGetEntities

	@i_get_entities.setter
	def i_get_entities(self, value):
		"""Gets the entities on which this appearance is applied."""
		self._instance.IGetEntities = value

	@property
	def remove_all_entities(self):
		"""Removes the appearance from all entities on which it is applied."""
		return self._instance.RemoveAllEntities

	@remove_all_entities.setter
	def remove_all_entities(self, value):
		"""Removes the appearance from all entities on which it is applied."""
		self._instance.RemoveAllEntities = value

	@property
	def set_center_point(self):
		"""Sets the center point of the mapping for texture-based appearances."""
		return self._instance.SetCenterPoint2

	@set_center_point.setter
	def set_center_point(self, value):
		"""Sets the center point of the mapping for texture-based appearances."""
		self._instance.SetCenterPoint2 = value

	@property
	def set_linked_display_states(self):
		"""Sets the display states to which this appearance is applied."""
		return self._instance.SetLinkedDisplayStates

	@set_linked_display_states.setter
	def set_linked_display_states(self, value):
		"""Sets the display states to which this appearance is applied."""
		self._instance.SetLinkedDisplayStates = value

	@property
	def set_u_direction(self):
		"""Sets the U direction of the texture-based appearance."""
		return self._instance.SetUDirection2

	@set_u_direction.setter
	def set_u_direction(self, value):
		"""Sets the U direction of the texture-based appearance."""
		self._instance.SetUDirection2 = value

	@property
	def set_v_direction(self):
		"""Sets the V direction of the texture-based appearance."""
		return self._instance.SetVDirection2

	@set_v_direction.setter
	def set_v_direction(self, value):
		"""Sets the V direction of the texture-based appearance."""
		self._instance.SetVDirection2 = value

