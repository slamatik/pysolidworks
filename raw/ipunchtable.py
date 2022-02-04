# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPunchTable_members.html
class IPunchTable:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def combine_same_size(self):
		"""Gets or sets whether to merge Punch ID column cells that have the same contents."""
		return self._instance.CombineSameSize

	@combine_same_size.setter
	def combine_same_size(self, value):
		"""Gets or sets whether to merge Punch ID column cells that have the same contents."""
		self._instance.CombineSameSize = value

	@property
	def combine_tags(self):
		"""Gets or sets whether to combine tags for punches having the same Punch ID."""
		return self._instance.CombineTags

	@combine_tags.setter
	def combine_tags(self, value):
		"""Gets or sets whether to combine tags for punches having the same Punch ID."""
		self._instance.CombineTags = value

	@property
	def dual_dimensions(self):
		"""Gets or sets whether to display dual dimensions in this punch table."""
		return self._instance.DualDimensions

	@dual_dimensions.setter
	def dual_dimensions(self, value):
		"""Gets or sets whether to display dual dimensions in this punch table."""
		self._instance.DualDimensions = value

	@property
	def show_units(self):
		"""Gets or sets whether to show dual dimension units in this punch table."""
		return self._instance.ShowUnits

	@show_units.setter
	def show_units(self, value):
		"""Gets or sets whether to show dual dimension units in this punch table."""
		self._instance.ShowUnits = value

	@property
	def starting_value(self):
		"""Gets or sets the starting value for the datum tags of this punch table."""
		return self._instance.StartingValue

	@starting_value.setter
	def starting_value(self, value):
		"""Gets or sets the starting value for the datum tags of this punch table."""
		self._instance.StartingValue = value

	@property
	def tag_style(self):
		"""Gets or sets the tag style for this punch table."""
		return self._instance.TagStyle

	@tag_style.setter
	def tag_style(self, value):
		"""Gets or sets the tag style for this punch table."""
		self._instance.TagStyle = value

	@property
	def get_feature(self):
		"""Gets the IFeature object for this punch table."""
		return self._instance.GetFeature

	@get_feature.setter
	def get_feature(self, value):
		"""Gets the IFeature object for this punch table."""
		self._instance.GetFeature = value

	@property
	def get_table_annotation_count(self):
		"""Gets the number of punch table annotations for this punch table."""
		return self._instance.GetTableAnnotationCount

	@get_table_annotation_count.setter
	def get_table_annotation_count(self, value):
		"""Gets the number of punch table annotations for this punch table."""
		self._instance.GetTableAnnotationCount = value

	@property
	def get_table_annotations(self):
		"""Gets the punch table annotations for this punch table feature."""
		return self._instance.GetTableAnnotations

	@get_table_annotations.setter
	def get_table_annotations(self, value):
		"""Gets the punch table annotations for this punch table feature."""
		self._instance.GetTableAnnotations = value

	@property
	def i_get_table_annotations(self):
		"""Gets the punch table annotations for this punch table feature."""
		return self._instance.IGetTableAnnotations

	@i_get_table_annotations.setter
	def i_get_table_annotations(self, value):
		"""Gets the punch table annotations for this punch table feature."""
		self._instance.IGetTableAnnotations = value

