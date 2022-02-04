# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleStandardsData_members.html
class IHoleStandardsData:
	def __init__(self, parent=None):
		self._instance = parent

	def get_fastener_table(self, standard_name, fastener_i_d, table_i_d, hole_table):
		"""
		Gets the Hole Wizard fastener table for the specified Hole Wizard standard, fastener ID, and fastener table type ID.
		:param standard_name: Standard name (see Remarks)
		:param fastener_i_d: Fastener ID (see Remarks)
		:param table_i_d: Fastener table type ID (see Remarks)
		:param hole_table: IHoleDataTable
		"""
		# return self._instance.GetFastenerTable(standard_name, fastener_i_d, table_i_d, hole_table)
		raise NotImplemented

	def get_fastener_table_types(self, standard_name, fastener_i_d, fastener_table_type_i_ds):
		"""
		Gets the array of three fastener table type IDs for the given fastener in the given Hole Wizard standard.
		:param standard_name: Standard name (see Remarks)
		:param fastener_i_d: Fastener ID (see Remarks)
		:param fastener_table_type_i_ds: Array of three fastener table type IDs (see Remarks)
		"""
		# return self._instance.GetFastenerTableTypes(standard_name, fastener_i_d, fastener_table_type_i_ds)
		raise NotImplemented

	def get_fastener_types(self, standard_name, fastener_indexes, fastener_names):
		"""
		Gets the fasteners in the specified Hole Wizard standard.
		:param standard_name: Standard name (see Remarks)
		:param fastener_indexes: Array of fastener indexes
		:param fastener_names: Array of fastener names
		"""
		# return self._instance.GetFastenerTypes(standard_name, fastener_indexes, fastener_names)
		raise NotImplemented

	def get_hole_standards(self, indexes, names):
		"""
		Gets Hole Wizard standards.
		:param indexes: Array of Hole Wizard standards as defined in swWzdHoleStandards_e
		:param names: Array of names of Hole Wizard standards
		"""
		# return self._instance.GetHoleStandards(indexes, names)
		raise NotImplemented

