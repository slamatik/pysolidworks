# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html
class IExplodeStep:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def auto_space_components_on_drag(self):
		"""Gets or sets whether to automatically space a group of components equally along an axis as you drag them."""
		return self._instance.AutoSpaceComponentsOnDrag

	@auto_space_components_on_drag.setter
	def auto_space_components_on_drag(self, value):
		"""Gets or sets whether to automatically space a group of components equally along an axis as you drag them."""
		self._instance.AutoSpaceComponentsOnDrag = value

	@property
	def diverge_direction(self):
		"""Gets or sets the diverge direction entity for this radial explode step."""
		return self._instance.DivergeDirection

	@diverge_direction.setter
	def diverge_direction(self, value):
		"""Gets or sets the diverge direction entity for this radial explode step."""
		self._instance.DivergeDirection = value

	@property
	def diverge_from_axis(self):
		"""Gets or sets whether to move components at an angle from the explode direction of this radial explode step."""
		return self._instance.DivergeFromAxis

	@diverge_from_axis.setter
	def diverge_from_axis(self, value):
		"""Gets or sets whether to move components at an angle from the explode direction of this radial explode step."""
		self._instance.DivergeFromAxis = value

	@property
	def explode_distance(self):
		"""Gets or sets the distance to move components in this regular or radial explode step."""
		return self._instance.ExplodeDistance

	@explode_distance.setter
	def explode_distance(self, value):
		"""Gets or sets the distance to move components in this regular or radial explode step."""
		self._instance.ExplodeDistance = value

	@property
	def explode_step_type(self):
		"""Gets the type of this explode step."""
		return self._instance.ExplodeStepType

	@explode_step_type.setter
	def explode_step_type(self, value):
		"""Gets the type of this explode step."""
		self._instance.ExplodeStepType = value

	@property
	def name(self):
		"""Gets or sets the name of this explode step."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the name of this explode step."""
		self._instance.Name = value

	@property
	def reverse_rotation_direction(self):
		"""Gets or sets whether to reverse the direction of rotation of components in this regular explode step."""
		return self._instance.ReverseRotationDirection

	@reverse_rotation_direction.setter
	def reverse_rotation_direction(self, value):
		"""Gets or sets whether to reverse the direction of rotation of components in this regular explode step."""
		self._instance.ReverseRotationDirection = value

	@property
	def reverse_translation_direction(self):
		"""Gets or sets whether to reverse the explode direction in this regular explode step."""
		return self._instance.ReverseTranslationDirection

	@reverse_translation_direction.setter
	def reverse_translation_direction(self, value):
		"""Gets or sets whether to reverse the explode direction in this regular explode step."""
		self._instance.ReverseTranslationDirection = value

	@property
	def rotate_about_each_component_origin(self):
		"""Gets or sets whether components rotate about their origins in this regular explode step."""
		return self._instance.RotateAboutEachComponentOrigin

	@rotate_about_each_component_origin.setter
	def rotate_about_each_component_origin(self, value):
		"""Gets or sets whether components rotate about their origins in this regular explode step."""
		self._instance.RotateAboutEachComponentOrigin = value

	@property
	def rotation_angle(self):
		"""Gets or sets the angle of component rotation in this regular or radial explode step."""
		return self._instance.RotationAngle

	@rotation_angle.setter
	def rotation_angle(self, value):
		"""Gets or sets the angle of component rotation in this regular or radial explode step."""
		self._instance.RotationAngle = value

	@property
	def get_component(self):
		"""Gets the specified component in this explode step."""
		return self._instance.GetComponent

	@get_component.setter
	def get_component(self, value):
		"""Gets the specified component in this explode step."""
		self._instance.GetComponent = value

	@property
	def get_component_name(self):
		"""Gets the name of the specified component in this explode step."""
		return self._instance.GetComponentName

	@get_component_name.setter
	def get_component_name(self, value):
		"""Gets the name of the specified component in this explode step."""
		self._instance.GetComponentName = value

	@property
	def get_components(self):
		"""Gets the components of this explode step."""
		return self._instance.GetComponents

	@get_components.setter
	def get_components(self, value):
		"""Gets the components of this explode step."""
		self._instance.GetComponents = value

	@property
	def get_component_xform(self):
		"""Gets the transform of this explode step."""
		return self._instance.GetComponentXform

	@get_component_xform.setter
	def get_component_xform(self, value):
		"""Gets the transform of this explode step."""
		self._instance.GetComponentXform = value

	@property
	def get_explode_direction(self):
		"""Gets the explode direction (manipulator index and entity) for this explode step."""
		return self._instance.GetExplodeDirection

	@get_explode_direction.setter
	def get_explode_direction(self, value):
		"""Gets the explode direction (manipulator index and entity) for this explode step."""
		self._instance.GetExplodeDirection = value

	@property
	def get_num_of_components(self):
		"""Gets the number of components in this explode step."""
		return self._instance.GetNumOfComponents

	@get_num_of_components.setter
	def get_num_of_components(self, value):
		"""Gets the number of components in this explode step."""
		self._instance.GetNumOfComponents = value

	@property
	def get_rotation_axis(self):
		"""Gets the rotation axis (manipulator index and entity) for this regular explode step."""
		return self._instance.GetRotationAxis

	@get_rotation_axis.setter
	def get_rotation_axis(self, value):
		"""Gets the rotation axis (manipulator index and entity) for this regular explode step."""
		self._instance.GetRotationAxis = value

	@property
	def get_specific_component_x_form(self):
		"""Gets the transformation matrix of the specified component in this explode step."""
		return self._instance.GetSpecificComponentXForm

	@get_specific_component_x_form.setter
	def get_specific_component_x_form(self, value):
		"""Gets the transformation matrix of the specified component in this explode step."""
		self._instance.GetSpecificComponentXForm = value

	@property
	def get_sub_assembly_explode_steps(self):
		"""Gets the explode steps of this subassembly explode step."""
		return self._instance.GetSubAssemblyExplodeSteps

	@get_sub_assembly_explode_steps.setter
	def get_sub_assembly_explode_steps(self, value):
		"""Gets the explode steps of this subassembly explode step."""
		self._instance.GetSubAssemblyExplodeSteps = value

	@property
	def i_get_component(self):
		"""Gets the specified component in this explode step."""
		return self._instance.IGetComponent

	@i_get_component.setter
	def i_get_component(self, value):
		"""Gets the specified component in this explode step."""
		self._instance.IGetComponent = value

	@property
	def i_get_component_xform(self):
		"""Gets the transform for this explode step."""
		return self._instance.IGetComponentXform

	@i_get_component_xform.setter
	def i_get_component_xform(self, value):
		"""Gets the transform for this explode step."""
		self._instance.IGetComponentXform = value

	@property
	def is_sub_assembly_rigid(self):
		"""Gets whether the subassembly is rigid or flexible."""
		return self._instance.IsSubAssemblyRigid

	@is_sub_assembly_rigid.setter
	def is_sub_assembly_rigid(self, value):
		"""Gets whether the subassembly is rigid or flexible."""
		self._instance.IsSubAssemblyRigid = value

	@property
	def set_components(self):
		"""Specifies the components of this explode step."""
		return self._instance.SetComponents

	@set_components.setter
	def set_components(self, value):
		"""Specifies the components of this explode step."""
		self._instance.SetComponents = value

	@property
	def set_explode_direction(self):
		"""Sets the explode direction (manipulator index and entity) for this explode step."""
		return self._instance.SetExplodeDirection

	@set_explode_direction.setter
	def set_explode_direction(self, value):
		"""Sets the explode direction (manipulator index and entity) for this explode step."""
		self._instance.SetExplodeDirection = value

	@property
	def set_rotation_axis(self):
		"""Sets the rotation axis (manipulator index and entity) for this regular explode step."""
		return self._instance.SetRotationAxis

	@set_rotation_axis.setter
	def set_rotation_axis(self, value):
		"""Sets the rotation axis (manipulator index and entity) for this regular explode step."""
		self._instance.SetRotationAxis = value

