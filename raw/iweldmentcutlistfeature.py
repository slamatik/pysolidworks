# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature_members.html
class IWeldmentCutListFeature:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def configuration(self):
		"""Gets or sets the name of the configuration for this weldment cut list table."""
		return self._instance.Configuration

	@configuration.setter
	def configuration(self, value):
		"""Gets or sets the name of the configuration for this weldment cut list table."""
		self._instance.Configuration = value

	@property
	def keep_current_item_numbers(self):
		"""Gets or sets whether item numbers are kept with their rows when columns are sorted or reordered in this weldment cut list table."""
		return self._instance.KeepCurrentItemNumbers

	@keep_current_item_numbers.setter
	def keep_current_item_numbers(self, value):
		"""Gets or sets whether item numbers are kept with their rows when columns are sorted or reordered in this weldment cut list table."""
		self._instance.KeepCurrentItemNumbers = value

	@property
	def keep_missing_items(self):
		"""Gets or sets whether to continue to show cut list items that were deleted from the weldment in the weldment cut list table."""
		return self._instance.KeepMissingItems

	@keep_missing_items.setter
	def keep_missing_items(self, value):
		"""Gets or sets whether to continue to show cut list items that were deleted from the weldment in the weldment cut list table."""
		self._instance.KeepMissingItems = value

	@property
	def sequence_start_number(self):
		"""Gets or sets the starting sequence number for this weldment cut list table."""
		return self._instance.SequenceStartNumber

	@sequence_start_number.setter
	def sequence_start_number(self, value):
		"""Gets or sets the starting sequence number for this weldment cut list table."""
		self._instance.SequenceStartNumber = value

	@property
	def strikeout_missing_items(self):
		"""Gets or sets whether to strike out missing items in the weldment cut list table."""
		return self._instance.StrikeoutMissingItems

	@strikeout_missing_items.setter
	def strikeout_missing_items(self, value):
		"""Gets or sets whether to strike out missing items in the weldment cut list table."""
		self._instance.StrikeoutMissingItems = value

	@property
	def get_feature(self):
		"""Gets the feature for this weldment cut list table."""
		return self._instance.GetFeature

	@get_feature.setter
	def get_feature(self, value):
		"""Gets the feature for this weldment cut list table."""
		self._instance.GetFeature = value

	@property
	def get_table_annotation_count(self):
		"""Gets the number of weldment cut list annotations for this weldment cut list table."""
		return self._instance.GetTableAnnotationCount

	@get_table_annotation_count.setter
	def get_table_annotation_count(self, value):
		"""Gets the number of weldment cut list annotations for this weldment cut list table."""
		self._instance.GetTableAnnotationCount = value

	@property
	def get_table_annotations(self):
		"""Gets the weldment cut list annotations for this weldment cut list table."""
		return self._instance.GetTableAnnotations

	@get_table_annotations.setter
	def get_table_annotations(self, value):
		"""Gets the weldment cut list annotations for this weldment cut list table."""
		self._instance.GetTableAnnotations = value

	@property
	def i_get_table_annotations(self):
		"""Gets the weldment cut list annotations for this weldment cut list table."""
		return self._instance.IGetTableAnnotations

	@i_get_table_annotations.setter
	def i_get_table_annotations(self, value):
		"""Gets the weldment cut list annotations for this weldment cut list table."""
		self._instance.IGetTableAnnotations = value

