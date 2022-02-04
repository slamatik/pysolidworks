# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html
class IBomFeature:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def configuration(self):
		"""Gets or sets the name of configuration for this BOM table."""
		return self._instance.Configuration

	@configuration.setter
	def configuration(self, value):
		"""Gets or sets the name of configuration for this BOM table."""
		self._instance.Configuration = value

	@property
	def detailed_cut_list(self):
		"""Gets or sets whether to show the detailed cut list in this BOM table."""
		return self._instance.DetailedCutList

	@detailed_cut_list.setter
	def detailed_cut_list(self, value):
		"""Gets or sets whether to show the detailed cut list in this BOM table."""
		self._instance.DetailedCutList = value

	@property
	def display_as_one_item(self):
		"""Gets or sets whether all of the configurations appear with the same item number if the BOM table contains components that have multiple configurations."""
		return self._instance.DisplayAsOneItem

	@display_as_one_item.setter
	def display_as_one_item(self, value):
		"""Gets or sets whether all of the configurations appear with the same item number if the BOM table contains components that have multiple configurations."""
		self._instance.DisplayAsOneItem = value

	@property
	def follow_assembly_order(self):
		"""Gets or sets whether the order of the item numbers in the BOM follows the order in which the assembly appears in the FeatureManager design tree."""
		return self._instance.FollowAssemblyOrder2

	@follow_assembly_order.setter
	def follow_assembly_order(self, value):
		"""Gets or sets whether the order of the item numbers in the BOM follows the order in which the assembly appears in the FeatureManager design tree."""
		self._instance.FollowAssemblyOrder2 = value

	@property
	def keep_current_item_numbers(self):
		"""Gets or sets whether item numbers are kept with their components when reordering rows of a BOM table."""
		return self._instance.KeepCurrentItemNumbers

	@keep_current_item_numbers.setter
	def keep_current_item_numbers(self, value):
		"""Gets or sets whether item numbers are kept with their components when reordering rows of a BOM table."""
		self._instance.KeepCurrentItemNumbers = value

	@property
	def keep_missing_items(self):
		"""Gets and sets the Keep Missing Items option for this BOM feature."""
		return self._instance.KeepMissingItems

	@keep_missing_items.setter
	def keep_missing_items(self, value):
		"""Gets and sets the Keep Missing Items option for this BOM feature."""
		self._instance.KeepMissingItems = value

	@property
	def keep_replaced_comp_option(self):
		"""Gets or sets how to replace components when keeping missing items."""
		return self._instance.KeepReplacedCompOption

	@keep_replaced_comp_option.setter
	def keep_replaced_comp_option(self, value):
		"""Gets or sets how to replace components when keeping missing items."""
		self._instance.KeepReplacedCompOption = value

	@property
	def name(self):
		"""Gets the name of this BOM table feature."""
		return self._instance.Name

	@name.setter
	def name(self, value):
		"""Gets the name of this BOM table feature."""
		self._instance.Name = value

	@property
	def numbering_type_on_indented_b_o_m(self):
		"""Gets and sets the type of numbering for this indented BOM table."""
		return self._instance.NumberingTypeOnIndentedBOM

	@numbering_type_on_indented_b_o_m.setter
	def numbering_type_on_indented_b_o_m(self, value):
		"""Gets and sets the type of numbering for this indented BOM table."""
		self._instance.NumberingTypeOnIndentedBOM = value

	@property
	def part_configuration_grouping(self):
		"""Gets and sets the part configuration grouping for this BOM table."""
		return self._instance.PartConfigurationGrouping

	@part_configuration_grouping.setter
	def part_configuration_grouping(self, value):
		"""Gets and sets the part configuration grouping for this BOM table."""
		self._instance.PartConfigurationGrouping = value

	@property
	def routing_component_grouping(self):
		"""Gets or sets the routing component grouping options for this BOM table in a drawing of an assembly containing routing components."""
		return self._instance.RoutingComponentGrouping

	@routing_component_grouping.setter
	def routing_component_grouping(self, value):
		"""Gets or sets the routing component grouping options for this BOM table in a drawing of an assembly containing routing components."""
		self._instance.RoutingComponentGrouping = value

	@property
	def sequence_start_number(self):
		"""Gets or sets the number with which to start the numbering for this BOM table."""
		return self._instance.SequenceStartNumber

	@sequence_start_number.setter
	def sequence_start_number(self, value):
		"""Gets or sets the number with which to start the numbering for this BOM table."""
		self._instance.SequenceStartNumber = value

	@property
	def strikeout_missing_items(self):
		"""Inserts a horizontal line through missing items in this BOM table (also called strike outs)."""
		return self._instance.StrikeoutMissingItems

	@strikeout_missing_items.setter
	def strikeout_missing_items(self, value):
		"""Inserts a horizontal line through missing items in this BOM table (also called strike outs)."""
		self._instance.StrikeoutMissingItems = value

	@property
	def table_type(self):
		"""Gets and sets the type of table for the Bill of Materials."""
		return self._instance.TableType

	@table_type.setter
	def table_type(self, value):
		"""Gets and sets the type of table for the Bill of Materials."""
		self._instance.TableType = value

	@property
	def zero_quantity_display(self):
		"""Gets or sets the character or value to display when a value is 0 in this BOM table."""
		return self._instance.ZeroQuantityDisplay

	@zero_quantity_display.setter
	def zero_quantity_display(self, value):
		"""Gets or sets the character or value to display when a value is 0 in this BOM table."""
		self._instance.ZeroQuantityDisplay = value

	@property
	def get_configuration_count(self):
		"""Gets the number of configurations available to this BOM table or used in this BOM table."""
		return self._instance.GetConfigurationCount

	@get_configuration_count.setter
	def get_configuration_count(self, value):
		"""Gets the number of configurations available to this BOM table or used in this BOM table."""
		self._instance.GetConfigurationCount = value

	@property
	def get_configurations(self):
		"""Gets the configurations available to this BOM table or used in this BOM table."""
		return self._instance.GetConfigurations

	@get_configurations.setter
	def get_configurations(self, value):
		"""Gets the configurations available to this BOM table or used in this BOM table."""
		self._instance.GetConfigurations = value

	@property
	def get_feature(self):
		"""Gets the BOM table feature."""
		return self._instance.GetFeature

	@get_feature.setter
	def get_feature(self, value):
		"""Gets the BOM table feature."""
		self._instance.GetFeature = value

	@property
	def get_referenced_model_name(self):
		"""Gets the name of the model referenced by this BOM feature."""
		return self._instance.GetReferencedModelName

	@get_referenced_model_name.setter
	def get_referenced_model_name(self, value):
		"""Gets the name of the model referenced by this BOM feature."""
		self._instance.GetReferencedModelName = value

	@property
	def get_table_annotation_count(self):
		"""Gets the number of BOM table annotations for this BOM table feature."""
		return self._instance.GetTableAnnotationCount

	@get_table_annotation_count.setter
	def get_table_annotation_count(self, value):
		"""Gets the number of BOM table annotations for this BOM table feature."""
		self._instance.GetTableAnnotationCount = value

	@property
	def get_table_annotations(self):
		"""Gets the BOM table annotations for this BOM table feature."""
		return self._instance.GetTableAnnotations

	@get_table_annotations.setter
	def get_table_annotations(self, value):
		"""Gets the BOM table annotations for this BOM table feature."""
		self._instance.GetTableAnnotations = value

	@property
	def i_get_configurations(self):
		"""Gets the configurations available to this BOM table or used in this BOM table."""
		return self._instance.IGetConfigurations

	@i_get_configurations.setter
	def i_get_configurations(self, value):
		"""Gets the configurations available to this BOM table or used in this BOM table."""
		self._instance.IGetConfigurations = value

	@property
	def i_get_table_annotations(self):
		"""Gets the BOM table annotations for this BOM table feature."""
		return self._instance.IGetTableAnnotations

	@i_get_table_annotations.setter
	def i_get_table_annotations(self, value):
		"""Gets the BOM table annotations for this BOM table feature."""
		self._instance.IGetTableAnnotations = value

	@property
	def i_set_configurations(self):
		"""Sets the configurations used in this BOM table."""
		return self._instance.ISetConfigurations

	@i_set_configurations.setter
	def i_set_configurations(self, value):
		"""Sets the configurations used in this BOM table."""
		self._instance.ISetConfigurations = value

	@property
	def set_configurations(self):
		"""Sets the configurations used in this BOM table."""
		return self._instance.SetConfigurations

	@set_configurations.setter
	def set_configurations(self, value):
		"""Sets the configurations used in this BOM table."""
		self._instance.SetConfigurations = value

