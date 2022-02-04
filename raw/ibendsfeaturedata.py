# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.html
class IBendsFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bend_radius(self):
		"""Gets or sets the bend radius for this Flatten-Bends/Process-Bends feature."""
		return self._instance.BendRadius

	@bend_radius.setter
	def bend_radius(self, value):
		"""Gets or sets the bend radius for this Flatten-Bends/Process-Bends feature."""
		self._instance.BendRadius = value

	@property
	def use_default_bend_allowance(self):
		"""Gets or sets whether to use the default bend allowance for this Flatten-Bends/Process-Bends feature."""
		return self._instance.UseDefaultBendAllowance

	@use_default_bend_allowance.setter
	def use_default_bend_allowance(self, value):
		"""Gets or sets whether to use the default bend allowance for this Flatten-Bends/Process-Bends feature."""
		self._instance.UseDefaultBendAllowance = value

	@property
	def use_default_bend_radius(self):
		"""Get or sets whether to use the default bend radius for this Flatten-Bends/Process-Bends feature."""
		return self._instance.UseDefaultBendRadius

	@use_default_bend_radius.setter
	def use_default_bend_radius(self, value):
		"""Get or sets whether to use the default bend radius for this Flatten-Bends/Process-Bends feature."""
		self._instance.UseDefaultBendRadius = value

	@property
	def access_selections(self):
		"""Allows access to the selections that describe this Flatten-Bends/Process-Bends feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Allows access to the selections that describe this Flatten-Bends/Process-Bends feature."""
		self._instance.AccessSelections = value

	@property
	def get_custom_bend_allowance(self):
		"""Gets the custom bend allowance for this Flatten-Bends/Process-Bends feature."""
		return self._instance.GetCustomBendAllowance

	@get_custom_bend_allowance.setter
	def get_custom_bend_allowance(self, value):
		"""Gets the custom bend allowance for this Flatten-Bends/Process-Bends feature."""
		self._instance.GetCustomBendAllowance = value

	@property
	def get_fixed_face(self):
		"""Gets the fixed face of a flatten-bends feature."""
		return self._instance.GetFixedFace

	@get_fixed_face.setter
	def get_fixed_face(self, value):
		"""Gets the fixed face of a flatten-bends feature."""
		self._instance.GetFixedFace = value

	@property
	def i_access_selections(self):
		"""Allows access to the selections that describe this Flatten-Bends/Process-Bends feature."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Allows access to the selections that describe this Flatten-Bends/Process-Bends feature."""
		self._instance.IAccessSelections2 = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that describe this Flatten-Bends/Process-Bends feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that describe this Flatten-Bends/Process-Bends feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_custom_bend_allowance(self):
		"""Sets the custom bend allowance for the Flatten-Bends/Process-Bends feature."""
		return self._instance.SetCustomBendAllowance

	@set_custom_bend_allowance.setter
	def set_custom_bend_allowance(self, value):
		"""Sets the custom bend allowance for the Flatten-Bends/Process-Bends feature."""
		self._instance.SetCustomBendAllowance = value

