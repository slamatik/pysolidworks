# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomBendAllowance_members.html
class ICustomBendAllowance:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bend_allowance(self):
		"""Gets or sets the value of the bend allowance."""
		return self._instance.BendAllowance

	@bend_allowance.setter
	def bend_allowance(self, value):
		"""Gets or sets the value of the bend allowance."""
		self._instance.BendAllowance = value

	@property
	def bend_deduction(self):
		"""Gets or sets the value of the bend deduction."""
		return self._instance.BendDeduction

	@bend_deduction.setter
	def bend_deduction(self, value):
		"""Gets or sets the value of the bend deduction."""
		self._instance.BendDeduction = value

	@property
	def bend_table_file(self):
		"""Gets or sets the path and file name for the bend table."""
		return self._instance.BendTableFile

	@bend_table_file.setter
	def bend_table_file(self, value):
		"""Gets or sets the path and file name for the bend table."""
		self._instance.BendTableFile = value

	@property
	def k_factor(self):
		"""Gets or sets the K-factor."""
		return self._instance.KFactor

	@k_factor.setter
	def k_factor(self, value):
		"""Gets or sets the K-factor."""
		self._instance.KFactor = value

	@property
	def type(self):
		"""Gets or sets the bend allowance type."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the bend allowance type."""
		self._instance.Type = value

