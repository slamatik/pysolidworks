# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.html
class IInstanceToVaryOptions:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def d_spacing_increment(self):
		"""Gets or sets the spacing increment of all pattern instances in Direction 1."""
		return self._instance.D1SpacingIncrement

	@d_spacing_increment.setter
	def d_spacing_increment(self, value):
		"""Gets or sets the spacing increment of all pattern instances in Direction 1."""
		self._instance.D1SpacingIncrement = value

	@property
	def d_spacing_increment(self):
		"""Gets or sets the spacing increment of all pattern instances in Direction 2."""
		return self._instance.D2SpacingIncrement

	@d_spacing_increment.setter
	def d_spacing_increment(self, value):
		"""Gets or sets the spacing increment of all pattern instances in Direction 2."""
		self._instance.D2SpacingIncrement = value

	@property
	def get_d_increment_dimensions(self):
		"""Gets the dimensions to increment in Direction 1."""
		return self._instance.GetD1IncrementDimensions

	@get_d_increment_dimensions.setter
	def get_d_increment_dimensions(self, value):
		"""Gets the dimensions to increment in Direction 1."""
		self._instance.GetD1IncrementDimensions = value

	@property
	def get_d_modified_spacing_value(self):
		"""Gets the spacing in Direction 1 of the specified modified pattern instance."""
		return self._instance.GetD1ModifiedSpacingValue

	@get_d_modified_spacing_value.setter
	def get_d_modified_spacing_value(self, value):
		"""Gets the spacing in Direction 1 of the specified modified pattern instance."""
		self._instance.GetD1ModifiedSpacingValue = value

	@property
	def get_d_increment_dimensions(self):
		"""Gets the dimensions to increment in Direction 2."""
		return self._instance.GetD2IncrementDimensions

	@get_d_increment_dimensions.setter
	def get_d_increment_dimensions(self, value):
		"""Gets the dimensions to increment in Direction 2."""
		self._instance.GetD2IncrementDimensions = value

	@property
	def get_d_modified_spacing_value(self):
		"""Gets the modified spacing in Direction 2 of the specified pattern instance."""
		return self._instance.GetD2ModifiedSpacingValue

	@get_d_modified_spacing_value.setter
	def get_d_modified_spacing_value(self, value):
		"""Gets the modified spacing in Direction 2 of the specified pattern instance."""
		self._instance.GetD2ModifiedSpacingValue = value

	@property
	def get_modified_dimensions(self):
		"""Gets the modified dimensions of the specified pattern instance."""
		return self._instance.GetModifiedDimensions

	@get_modified_dimensions.setter
	def get_modified_dimensions(self, value):
		"""Gets the modified dimensions of the specified pattern instance."""
		self._instance.GetModifiedDimensions = value

	@property
	def get_modified_instances(self):
		"""Gets instance numbers of modified pattern instances of the specified type."""
		return self._instance.GetModifiedInstances

	@get_modified_instances.setter
	def get_modified_instances(self, value):
		"""Gets instance numbers of modified pattern instances of the specified type."""
		self._instance.GetModifiedInstances = value

	@property
	def modify_d_spacing_value(self):
		"""Modifies the spacing in Direction 1 of the specified pattern instance."""
		return self._instance.ModifyD1SpacingValue

	@modify_d_spacing_value.setter
	def modify_d_spacing_value(self, value):
		"""Modifies the spacing in Direction 1 of the specified pattern instance."""
		self._instance.ModifyD1SpacingValue = value

	@property
	def modify_d_spacing_value(self):
		"""Modifies the spacing in Direction 2 of the specified pattern instance."""
		return self._instance.ModifyD2SpacingValue

	@modify_d_spacing_value.setter
	def modify_d_spacing_value(self, value):
		"""Modifies the spacing in Direction 2 of the specified pattern instance."""
		self._instance.ModifyD2SpacingValue = value

	@property
	def modify_dimensions(self):
		"""Modifies the specified dimensions of the specified pattern instance."""
		return self._instance.ModifyDimensions

	@modify_dimensions.setter
	def modify_dimensions(self, value):
		"""Modifies the specified dimensions of the specified pattern instance."""
		self._instance.ModifyDimensions = value

	@property
	def set_d_increment_dimensions(self):
		"""Sets the dimensions to increment in Direction 1."""
		return self._instance.SetD1IncrementDimensions

	@set_d_increment_dimensions.setter
	def set_d_increment_dimensions(self, value):
		"""Sets the dimensions to increment in Direction 1."""
		self._instance.SetD1IncrementDimensions = value

	@property
	def set_d_increment_dimensions(self):
		"""Sets the dimensions to increment in Direction 2."""
		return self._instance.SetD2IncrementDimensions

	@set_d_increment_dimensions.setter
	def set_d_increment_dimensions(self, value):
		"""Sets the dimensions to increment in Direction 2."""
		self._instance.SetD2IncrementDimensions = value

