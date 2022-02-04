# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchedBendFeatureData_members.html
class ISketchedBendFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bend_angle(self):
		"""Gets or sets the bend angle of this sketched bend feature."""
		return self._instance.BendAngle

	@bend_angle.setter
	def bend_angle(self, value):
		"""Gets or sets the bend angle of this sketched bend feature."""
		self._instance.BendAngle = value

	@property
	def bend_radius(self):
		"""Gets or sets the bend radius of this sketched bend feature."""
		return self._instance.BendRadius

	@bend_radius.setter
	def bend_radius(self, value):
		"""Gets or sets the bend radius of this sketched bend feature."""
		self._instance.BendRadius = value

	@property
	def position_type(self):
		"""Gets or sets the position of this sketched bend feature."""
		return self._instance.PositionType

	@position_type.setter
	def position_type(self, value):
		"""Gets or sets the position of this sketched bend feature."""
		self._instance.PositionType = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether the direction of the sketched bend is reversed."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether the direction of the sketched bend is reversed."""
		self._instance.ReverseDirection = value

	@property
	def use_default_bend_allowance(self):
		"""Gets or sets whether to use the default bend allowance for this sketched bend feature."""
		return self._instance.UseDefaultBendAllowance

	@use_default_bend_allowance.setter
	def use_default_bend_allowance(self, value):
		"""Gets or sets whether to use the default bend allowance for this sketched bend feature."""
		self._instance.UseDefaultBendAllowance = value

	@property
	def use_default_bend_radius(self):
		"""Gets or sets whether to use the default bend radius of the sketched bend feature."""
		return self._instance.UseDefaultBendRadius

	@use_default_bend_radius.setter
	def use_default_bend_radius(self, value):
		"""Gets or sets whether to use the default bend radius of the sketched bend feature."""
		self._instance.UseDefaultBendRadius = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe this sketched bend feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe this sketched bend feature."""
		self._instance.AccessSelections = value

	@property
	def get_custom_bend_allowance(self):
		"""Gets the custom bend allowance for this sketched bend feature."""
		return self._instance.GetCustomBendAllowance

	@get_custom_bend_allowance.setter
	def get_custom_bend_allowance(self, value):
		"""Gets the custom bend allowance for this sketched bend feature."""
		self._instance.GetCustomBendAllowance = value

	@property
	def get_fixed_face(self):
		"""Gets the fixed face from this sketched bend feature."""
		return self._instance.GetFixedFace

	@get_fixed_face.setter
	def get_fixed_face(self, value):
		"""Gets the fixed face from this sketched bend feature."""
		self._instance.GetFixedFace = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that describe this sketched bend feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that describe this sketched bend feature."""
		self._instance.IAccessSelections2 = value

	@property
	def release_selection_access(self):
		"""Releases access to selections that describe this sketched bend feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to selections that describe this sketched bend feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_custom_bend_allowance(self):
		"""Sets the custom bend allowance for this sketched bend feature."""
		return self._instance.SetCustomBendAllowance

	@set_custom_bend_allowance.setter
	def set_custom_bend_allowance(self, value):
		"""Sets the custom bend allowance for this sketched bend feature."""
		self._instance.SetCustomBendAllowance = value

	@property
	def set_fixed_face(self):
		"""Sets the fixed face of this sketched bend feature."""
		return self._instance.SetFixedFace

	@set_fixed_face.setter
	def set_fixed_face(self, value):
		"""Sets the fixed face of this sketched bend feature."""
		self._instance.SetFixedFace = value

