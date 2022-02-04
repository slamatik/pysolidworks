# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEquationMgr_members.html
class IEquationMgr:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angular_equation_units(self):
		"""Gets or sets the angular units used in equations."""
		return self._instance.AngularEquationUnits

	@angular_equation_units.setter
	def angular_equation_units(self, value):
		"""Gets or sets the angular units used in equations."""
		self._instance.AngularEquationUnits = value

	@property
	def automatic_rebuild(self):
		"""Gets or sets whether to automatically rebuild after modifications."""
		return self._instance.AutomaticRebuild

	@automatic_rebuild.setter
	def automatic_rebuild(self, value):
		"""Gets or sets whether to automatically rebuild after modifications."""
		self._instance.AutomaticRebuild = value

	@property
	def automatic_solve_order(self):
		"""Gets or sets whether to automatically sequence equations in an order determined by SOLIDWORKS to produce accurate results."""
		return self._instance.AutomaticSolveOrder

	@automatic_solve_order.setter
	def automatic_solve_order(self, value):
		"""Gets or sets whether to automatically sequence equations in an order determined by SOLIDWORKS to produce accurate results."""
		self._instance.AutomaticSolveOrder = value

	@property
	def disabled(self):
		"""Gets or sets whether to disable the specified equation in the model."""
		return self._instance.Disabled

	@disabled.setter
	def disabled(self, value):
		"""Gets or sets whether to disable the specified equation in the model."""
		self._instance.Disabled = value

	@property
	def equation(self):
		"""Gets or sets the equation at the specified index."""
		return self._instance.Equation

	@equation.setter
	def equation(self, value):
		"""Gets or sets the equation at the specified index."""
		self._instance.Equation = value

	@property
	def file_path(self):
		"""Gets or sets the path for an exported equation text (.txt) file."""
		return self._instance.FilePath

	@file_path.setter
	def file_path(self, value):
		"""Gets or sets the path for an exported equation text (.txt) file."""
		self._instance.FilePath = value

	@property
	def global_variable(self):
		"""Gets whether the equation at the specified index is a global variable."""
		return self._instance.GlobalVariable

	@global_variable.setter
	def global_variable(self, value):
		"""Gets whether the equation at the specified index is a global variable."""
		self._instance.GlobalVariable = value

	@property
	def link_to_file(self):
		"""Gets or sets whether the equation is linked to an exported equation text (.txt) file."""
		return self._instance.LinkToFile

	@link_to_file.setter
	def link_to_file(self, value):
		"""Gets or sets whether the equation is linked to an exported equation text (.txt) file."""
		self._instance.LinkToFile = value

	@property
	def status(self):
		"""Gets the status of the last equation that was executed."""
		return self._instance.Status

	@status.setter
	def status(self, value):
		"""Gets the status of the last equation that was executed."""
		self._instance.Status = value

	@property
	def value(self):
		"""Gets the value of the equation at the specified index."""
		return self._instance.Value

	@value.setter
	def value(self, value):
		"""Gets the value of the equation at the specified index."""
		self._instance.Value = value

	@property
	def add(self):
		"""Adds an equation at the specified index."""
		return self._instance.Add2

	@add.setter
	def add(self, value):
		"""Adds an equation at the specified index."""
		self._instance.Add2 = value

	@property
	def add(self):
		"""Adds an equation at the specified index for the specified configurations."""
		return self._instance.Add3

	@add.setter
	def add(self, value):
		"""Adds an equation at the specified index for the specified configurations."""
		self._instance.Add3 = value

	@property
	def change_suppression_for_all_configurations(self):
		"""Changes the suppression state of the specified equation in all configurations."""
		return self._instance.ChangeSuppressionForAllConfigurations

	@change_suppression_for_all_configurations.setter
	def change_suppression_for_all_configurations(self, value):
		"""Changes the suppression state of the specified equation in all configurations."""
		self._instance.ChangeSuppressionForAllConfigurations = value

	@property
	def change_suppression_for_configuration(self):
		"""Changes the suppression state of an equation in the specified configuration."""
		return self._instance.ChangeSuppressionForConfiguration

	@change_suppression_for_configuration.setter
	def change_suppression_for_configuration(self, value):
		"""Changes the suppression state of an equation in the specified configuration."""
		self._instance.ChangeSuppressionForConfiguration = value

	@property
	def delete(self):
		"""Deletes the equation at the specified index."""
		return self._instance.Delete

	@delete.setter
	def delete(self, value):
		"""Deletes the equation at the specified index."""
		self._instance.Delete = value

	@property
	def evaluate_all(self):
		"""Evaluates all equations."""
		return self._instance.EvaluateAll

	@evaluate_all.setter
	def evaluate_all(self, value):
		"""Evaluates all equations."""
		self._instance.EvaluateAll = value

	@property
	def get_configuration_option(self):
		"""Gets the configuration option for the equation at the specified index."""
		return self._instance.GetConfigurationOption

	@get_configuration_option.setter
	def get_configuration_option(self, value):
		"""Gets the configuration option for the equation at the specified index."""
		self._instance.GetConfigurationOption = value

	@property
	def get_count(self):
		"""Gets the number of equations in the model."""
		return self._instance.GetCount

	@get_count.setter
	def get_count(self, value):
		"""Gets the number of equations in the model."""
		self._instance.GetCount = value

	@property
	def get_disabled_equation_count(self):
		"""Gets the number of disabled equations in the model."""
		return self._instance.GetDisabledEquationCount

	@get_disabled_equation_count.setter
	def get_disabled_equation_count(self, value):
		"""Gets the number of disabled equations in the model."""
		self._instance.GetDisabledEquationCount = value

	@property
	def i_add(self):
		"""Adds an equation at the specified index for the specified configurations."""
		return self._instance.IAdd3

	@i_add.setter
	def i_add(self, value):
		"""Adds an equation at the specified index for the specified configurations."""
		self._instance.IAdd3 = value

	@property
	def i_set_equation_and_configuration_option(self):
		"""Modifies the equation at the specified index for the specified configurations."""
		return self._instance.ISetEquationAndConfigurationOption

	@i_set_equation_and_configuration_option.setter
	def i_set_equation_and_configuration_option(self, value):
		"""Modifies the equation at the specified index for the specified configurations."""
		self._instance.ISetEquationAndConfigurationOption = value

	@property
	def set_equation_and_configuration_option(self):
		"""Modifies the equation at the specified index for the specified configurations."""
		return self._instance.SetEquationAndConfigurationOption

	@set_equation_and_configuration_option.setter
	def set_equation_and_configuration_option(self, value):
		"""Modifies the equation at the specified index for the specified configurations."""
		self._instance.SetEquationAndConfigurationOption = value

	@property
	def update_values_from_external_equation_file(self):
		"""Updates equations dependent on a linked equation file and ensures that the linked equation file exists and updates its current path, if necessary."""
		return self._instance.UpdateValuesFromExternalEquationFile

	@update_values_from_external_equation_file.setter
	def update_values_from_external_equation_file(self, value):
		"""Updates equations dependent on a linked equation file and ensures that the linked equation file exists and updates its current path, if necessary."""
		self._instance.UpdateValuesFromExternalEquationFile = value

