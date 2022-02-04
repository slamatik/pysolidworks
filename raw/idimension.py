# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html
class IDimension:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def dimension_line_direction(self):
		"""Gets or sets the direction of this dimension line."""
		return self._instance.DimensionLineDirection

	@dimension_line_direction.setter
	def dimension_line_direction(self, value):
		"""Gets or sets the direction of this dimension line."""
		self._instance.DimensionLineDirection = value

	@property
	def driven_state(self):
		"""Gets or sets the driven state of a dimension."""
		return self._instance.DrivenState

	@driven_state.setter
	def driven_state(self, value):
		"""Gets or sets the driven state of a dimension."""
		self._instance.DrivenState = value

	@property
	def extension_line_direction(self):
		"""Gets or sets the direction of the extension line."""
		return self._instance.ExtensionLineDirection

	@extension_line_direction.setter
	def extension_line_direction(self, value):
		"""Gets or sets the direction of the extension line."""
		self._instance.ExtensionLineDirection = value

	@property
	def full_name(self):
		"""Gets the full name of a dimension including the feature and the model."""
		return self._instance.FullName

	@full_name.setter
	def full_name(self, value):
		"""Gets the full name of a dimension including the feature and the model."""
		self._instance.FullName = value

	@property
	def name(self):
		"""Gets or sets the name of a dimension."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets or sets the name of a dimension."""
		self._instance.Name = value

	@property
	def read_only(self):
		"""Gets or sets the read-only state of a dimension."""
		return self._instance.ReadOnly

	@read_only.setter
	def read_only(self, value):
		"""Gets or sets the read-only state of a dimension."""
		self._instance.ReadOnly = value

	@property
	def reference_points(self):
		"""Gets or sets the reference points for this dimension."""
		return self._instance.ReferencePoints

	@reference_points.setter
	def reference_points(self, value):
		"""Gets or sets the reference points for this dimension."""
		self._instance.ReferencePoints = value

	@property
	def tolerance(self):
		"""Gets the IDimensionTolerance object."""
		return self._instance.Tolerance

	@tolerance.setter
	def tolerance(self, value):
		"""Gets the IDimensionTolerance object."""
		self._instance.Tolerance = value

	@property
	def get_arc_end_condition(self):
		"""Gets the end conditions for linear dimensions that end on an arc."""
		return self._instance.GetArcEndCondition

	@get_arc_end_condition.setter
	def get_arc_end_condition(self, value):
		"""Gets the end conditions for linear dimensions that end on an arc."""
		self._instance.GetArcEndCondition = value

	@property
	def get_feature_owner(self):
		"""Gets the feature for this dimension."""
		return self._instance.GetFeatureOwner

	@get_feature_owner.setter
	def get_feature_owner(self, value):
		"""Gets the feature for this dimension."""
		self._instance.GetFeatureOwner = value

	@property
	def get_name_for_selection(self):
		"""Gets the name of the selected dimension needed by IModelDocExtension::SelectByID2."""
		return self._instance.GetNameForSelection

	@get_name_for_selection.setter
	def get_name_for_selection(self, value):
		"""Gets the name of the selected dimension needed by IModelDocExtension::SelectByID2."""
		self._instance.GetNameForSelection = value

	@property
	def get_reference_points_count(self):
		"""Gets the number of reference points for this dimension."""
		return self._instance.GetReferencePointsCount

	@get_reference_points_count.setter
	def get_reference_points_count(self, value):
		"""Gets the number of reference points for this dimension."""
		self._instance.GetReferencePointsCount = value

	@property
	def get_system_chamfer_values(self):
		"""Gets the chamfer dimension values in system units."""
		return self._instance.GetSystemChamferValues

	@get_system_chamfer_values.setter
	def get_system_chamfer_values(self, value):
		"""Gets the chamfer dimension values in system units."""
		self._instance.GetSystemChamferValues = value

	@property
	def get_system_value(self):
		"""Gets the value of the current dimension in system units in the named configuration."""
		return self._instance.GetSystemValue3

	@get_system_value.setter
	def get_system_value(self, value):
		"""Gets the value of the current dimension in system units in the named configuration."""
		self._instance.GetSystemValue3 = value

	@property
	def get_type(self):
		"""Gets the type of dimension."""
		return self._instance.GetType

	@get_type.setter
	def get_type(self, value):
		"""Gets the type of dimension."""
		self._instance.GetType = value

	@property
	def get_user_value_in(self):
		"""Gets the value of this dimension in the units of the specified document."""
		return self._instance.GetUserValueIn

	@get_user_value_in.setter
	def get_user_value_in(self, value):
		"""Gets the value of this dimension in the units of the specified document."""
		self._instance.GetUserValueIn = value

	@property
	def get_value(self):
		"""Gets the values of the dimensions in the specified configurations."""
		return self._instance.GetValue3

	@get_value.setter
	def get_value(self, value):
		"""Gets the values of the dimensions in the specified configurations."""
		self._instance.GetValue3 = value

	@property
	def i_get_reference_points(self):
		"""Gets the reference points for this dimension."""
		return self._instance.IGetReferencePoints

	@i_get_reference_points.setter
	def i_get_reference_points(self, value):
		"""Gets the reference points for this dimension."""
		self._instance.IGetReferencePoints = value

	@property
	def i_get_system_value(self):
		"""Gets the value of the current dimension in system units in the named configuration."""
		return self._instance.IGetSystemValue3

	@i_get_system_value.setter
	def i_get_system_value(self, value):
		"""Gets the value of the current dimension in system units in the named configuration."""
		self._instance.IGetSystemValue3 = value

	@property
	def i_get_user_value_in(self):
		"""Gets the value of this dimension in the units of the specified document."""
		return self._instance.IGetUserValueIn2

	@i_get_user_value_in.setter
	def i_get_user_value_in(self, value):
		"""Gets the value of this dimension in the units of the specified document."""
		self._instance.IGetUserValueIn2 = value

	@property
	def i_get_value(self):
		"""Gets the values of the dimensions in the specified configurations."""
		return self._instance.IGetValue3

	@i_get_value.setter
	def i_get_value(self, value):
		"""Gets the values of the dimensions in the specified configurations."""
		self._instance.IGetValue3 = value

	@property
	def is_applied_to_all_configurations(self):
		"""Gets whether a dimension is currently applied to all configurations of the model or to just the current configuration."""
		return self._instance.IsAppliedToAllConfigurations

	@is_applied_to_all_configurations.setter
	def is_applied_to_all_configurations(self, value):
		"""Gets whether a dimension is currently applied to all configurations of the model or to just the current configuration."""
		self._instance.IsAppliedToAllConfigurations = value

	@property
	def is_design_table_dimension(self):
		"""Gets whether this dimension is driven by a design table."""
		return self._instance.IsDesignTableDimension

	@is_design_table_dimension.setter
	def is_design_table_dimension(self, value):
		"""Gets whether this dimension is driven by a design table."""
		self._instance.IsDesignTableDimension = value

	@property
	def i_set_reference_points(self):
		"""Sets the reference points for this dimension."""
		return self._instance.ISetReferencePoints

	@i_set_reference_points.setter
	def i_set_reference_points(self, value):
		"""Sets the reference points for this dimension."""
		self._instance.ISetReferencePoints = value

	@property
	def i_set_system_value(self):
		"""Sets the value of this dimension in system units (meters) in the specified configuration."""
		return self._instance.ISetSystemValue3

	@i_set_system_value.setter
	def i_set_system_value(self, value):
		"""Sets the value of this dimension in system units (meters) in the specified configuration."""
		self._instance.ISetSystemValue3 = value

	@property
	def i_set_user_value_in(self):
		"""Sets the value of this dimension in the units of the specified document."""
		return self._instance.ISetUserValueIn3

	@i_set_user_value_in.setter
	def i_set_user_value_in(self, value):
		"""Sets the value of this dimension in the units of the specified document."""
		self._instance.ISetUserValueIn3 = value

	@property
	def i_set_value(self):
		"""Sets the values of the dimensions in the specified configurations."""
		return self._instance.ISetValue3

	@i_set_value.setter
	def i_set_value(self, value):
		"""Sets the values of the dimensions in the specified configurations."""
		self._instance.ISetValue3 = value

	@property
	def is_reference(self):
		"""Gets whether the dimension is a reference dimension."""
		return self._instance.IsReference

	@is_reference.setter
	def is_reference(self, value):
		"""Gets whether the dimension is a reference dimension."""
		self._instance.IsReference = value

	@property
	def set_arc_end_condition(self):
		"""Sets the end conditions for linear dimensions that end on an arc."""
		return self._instance.SetArcEndCondition

	@set_arc_end_condition.setter
	def set_arc_end_condition(self, value):
		"""Sets the end conditions for linear dimensions that end on an arc."""
		self._instance.SetArcEndCondition = value

	@property
	def set_system_value(self):
		"""Sets the value of this dimension in system units (meters) in the specified configuration."""
		return self._instance.SetSystemValue3

	@set_system_value.setter
	def set_system_value(self, value):
		"""Sets the value of this dimension in system units (meters) in the specified configuration."""
		self._instance.SetSystemValue3 = value

	@property
	def set_user_value_in(self):
		"""Sets the value of this dimension in the units of the specified document."""
		return self._instance.SetUserValueIn2

	@set_user_value_in.setter
	def set_user_value_in(self, value):
		"""Sets the value of this dimension in the units of the specified document."""
		self._instance.SetUserValueIn2 = value

	@property
	def set_value(self):
		"""Sets the values of the dimensions in the specified configurations."""
		return self._instance.SetValue3

	@set_value.setter
	def set_value(self, value):
		"""Sets the values of the dimensions in the specified configurations."""
		self._instance.SetValue3 = value

