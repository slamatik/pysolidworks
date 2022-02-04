# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomTableAnnotation_members.html
class IBomTableAnnotation:
	def __init__(self, parent=None):
		self._instance = parent

	def bom_feature(self):
		"""Gets the BOM for this table annotation."""
		# return self._instance.BomFeature
		raise NotImplemented

	def apply_saved_sort_scheme(self, sort_data):
		"""
		Sorts this BOM table using the sort data that was previously saved in the table.
		:param sort_data: IBomTableSortData
		"""
		# return self._instance.ApplySavedSortScheme(sort_data)
		raise NotImplemented

	def collapse(self, collapse_type, index):
		"""
		Collapses the specified item.
		:param collapse_type: Type of item to collapse as defined in swBOMTableObjectType_e (see Remarks)
		:param index: Row index; valid only if CollapseType is swBOMTableObjectType_e.swBOMTableObjectType_RowIndex
		"""
		# return self._instance.Collapse(collapse_type, index)
		raise NotImplemented

	def dissolve(self, row_index):
		"""
		Dissolves into individual components the subassembly or weldment at the specified row index of this BOM table annotation.
		:param row_index: 1-based row index of the subassembly or weldment to dissolve
		"""
		# return self._instance.Dissolve(row_index)
		raise NotImplemented

	def expand(self, expand_type, index):
		"""
		Expands the specified item.
		:param expand_type: Type of item to expand as defined in swBOMTableObjectType_e
		:param index: Row index; valid only if ExpandType is swBOMTableObjectType_e.swBOMTableObjectType_RowIndex
		"""
		# return self._instance.Expand(expand_type, index)
		raise NotImplemented

	def get_all_custom_properties(self):
		"""Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation."""
		# return self._instance.GetAllCustomProperties
		raise NotImplemented

	def get_all_custom_properties_count(self):
		"""Gets the number of items in the list of available custom properties that can be used for a custom properties column in this BOM table annotation."""
		# return self._instance.GetAllCustomPropertiesCount
		raise NotImplemented

	def get_bom_table_sort_data(self):
		"""Gets an instance of IBomTableSortData."""
		# return self._instance.GetBomTableSortData
		raise NotImplemented

	def get_column_custom_property(self, index):
		"""
		Gets the custom property used to fill the values in a specified user-defined column.
		:param index: Column from which to get the custom property
		"""
		# return self._instance.GetColumnCustomProperty(index)
		raise NotImplemented

	def get_column_use_title_as_part_number(self, index):
		"""
		Gets whether the document title is being used for the specified part-number column.
		:param index: 0-based number indicating the part-number column
		"""
		# return self._instance.GetColumnUseTitleAsPartNumber(index)
		raise NotImplemented

	def get_components(self, row_index, configuration):
		"""
		Gets the components in the specified row for the specified configuration in this BOM table annotation.
		:param row_index: Row in the BOM table where to get the components; 0-based index
		:param configuration: Configuration for which to get components in top-level only BOMs; specify an empty string for parts only and indented BOMs
		"""
		# return self._instance.GetComponents2(row_index, configuration)
		raise NotImplemented

	def get_components_count(self, row_index, configuration, item_number, part_number):
		"""
		Gets the number of components, the item number, and the part number in the specified row for the specified configuration in this BOM table annotation.
		:param row_index: Row in the BOM table where to get the number of components; 0-based index
		:param configuration: Configuration for which to count components in top-level only BOMs; specify an empty string for parts only and indented BOMs
		:param item_number: Item number of the specified row
		:param part_number: Part number of the specified row
		"""
		# return self._instance.GetComponentsCount2(row_index, configuration, item_number, part_number)
		raise NotImplemented

	def get_model_path_names(self, row_index, item_number, part_number):
		"""
		Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row.
		:param row_index: Row in the BOM table; 0-based index
		:param item_number: Item number for the specified BOM table row
		:param part_number: Part number for the specified BOM table row
		"""
		# return self._instance.GetModelPathNames(row_index, item_number, part_number)
		raise NotImplemented

	def get_model_path_names_count(self, row_index):
		"""
		Gets the number of model pathnames in the specified row of this BOM table annotation.
		:param row_index: Row in the BOM table; 0-based index
		"""
		# return self._instance.GetModelPathNamesCount(row_index)
		raise NotImplemented

	def i_get_all_custom_properties(self, count):
		"""
		Gets the list of available custom properties that can be used for a custom properties column in this BOM table annotation.
		:param count: Number of available custom properties
		"""
		# return self._instance.IGetAllCustomProperties(count)
		raise NotImplemented

	def i_get_components(self, row_index, configuration, count):
		"""
		Gets the components in the specified row for the specified configuration in this BOM table annotation.
		:param row_index: Row in the BOM table where to get the components; 0-based index
		:param configuration: Configuration for which to count components in top-level only BOMs; specify an empty string for parts only and indented BOMs
		:param count: Number of components in the specified row
		"""
		# return self._instance.IGetComponents2(row_index, configuration, count)
		raise NotImplemented

	def i_get_model_path_names(self, row_index, count, item_number, part_number):
		"""
		Gets the full pathnames of all documents in the specified row of this BOM table annotation. Also gets the item and part numbers associated with the specified row.
		:param row_index: Row in the BOM table; 0-based index
		:param count: Number of model pathnames
		:param item_number: Item number for the specified BOM table row
		:param part_number: Part number for the specified BOM table row
		"""
		# return self._instance.IGetModelPathNames(row_index, count, item_number, part_number)
		raise NotImplemented

	def restore_restructured_components(self, row_index):
		"""
		Restores the previously dissolved subassembly or weldment at the specified row index of this BOM table annotation.
		:param row_index: 1-based row index, if more than one subassembly or weldment are dissolved; 0, if only one subassembly or weldment is dissolved
		"""
		# return self._instance.RestoreRestructuredComponents(row_index)
		raise NotImplemented

	def save_as_excel(self, file_name, include_hidden, include_file_images):
		"""
		Saves this BOM table annotation as a Microsoft Excel document with the specified properties.
		:param file_name: Full path and file name of the Microsoft Excel file to save to (*.xls)
		:param include_hidden: True to include text in hidden cells, false to not
		:param include_file_images: True to include file images, false to not
		"""
		# return self._instance.SaveAsExcel(file_name, include_hidden, include_file_images)
		raise NotImplemented

	def set_column_custom_property(self, index, custom_prop):
		"""
		Sets the custom property used to fill the values in a specified user-defined column.
		:param index: Column for which to get the custom property
		:param custom_prop: Custom property used to fill the values in this user-defined column
		"""
		# return self._instance.SetColumnCustomProperty(index, custom_prop)
		raise NotImplemented

	def set_column_use_title_as_part_number(self, index, use_title):
		"""
		Sets whether to use the document title for the specified part-number column.
		:param index: 0-based index indicating the part-number column
		:param use_title: True to use the document title for the specified part-number column, false to not
		"""
		# return self._instance.SetColumnUseTitleAsPartNumber(index, use_title)
		raise NotImplemented

	def sort(self, sort_data):
		"""
		Sorts this BOM table using the specified sorting data.
		:param sort_data: IBomTableSortData
		"""
		# return self._instance.Sort(sort_data)
		raise NotImplemented

