# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleTable_members.html
class IHoleTable:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def combine_same_size(self):
		"""Gets or sets whether to merge cells of the same size in this hole table."""
		return self._instance.CombineSameSize

	@combine_same_size.setter
	def combine_same_size(self, value):
		"""Gets or sets whether to merge cells of the same size in this hole table."""
		self._instance.CombineSameSize = value

	@property
	def combine_tags(self):
		"""Gets or sets whether to combine tags for same-size holes."""
		return self._instance.CombineTags

	@combine_tags.setter
	def combine_tags(self, value):
		"""Gets or sets whether to combine tags for same-size holes."""
		self._instance.CombineTags = value

	@property
	def datum_origin(self):
		"""Gets the datum origin annotation for this hole table."""
		return self._instance.DatumOrigin

	@datum_origin.setter
	def datum_origin(self, value):
		"""Gets the datum origin annotation for this hole table."""
		self._instance.DatumOrigin = value

	@property
	def enable_update(self):
		"""Gets or sets whether to update hole table and graphics after changing hole tags."""
		return self._instance.EnableUpdate

	@enable_update.setter
	def enable_update(self, value):
		"""Gets or sets whether to update hole table and graphics after changing hole tags."""
		self._instance.EnableUpdate = value

	@property
	def hole_centers_visible(self):
		"""Gets or sets whether to show the hole center marks for this hole table."""
		return self._instance.HoleCentersVisible

	@hole_centers_visible.setter
	def hole_centers_visible(self, value):
		"""Gets or sets whether to show the hole center marks for this hole table."""
		self._instance.HoleCentersVisible = value

	@property
	def hole_tag(self):
		"""Gets or sets the name of the specified tag in a hole table."""
		return self._instance.HoleTag

	@hole_tag.setter
	def hole_tag(self, value):
		"""Gets or sets the name of the specified tag in a hole table."""
		self._instance.HoleTag = value

	@property
	def hole_tags_visible(self):
		"""Gets whether the hole tags are visible for this hole table."""
		return self._instance.HoleTagsVisible

	@hole_tags_visible.setter
	def hole_tags_visible(self, value):
		"""Gets whether the hole tags are visible for this hole table."""
		self._instance.HoleTagsVisible = value

	@property
	def show_a_n_s_i_inch_letter_number_drill_sizes(self):
		"""Gets or sets whether to display hole sizes in this hole table using ANSI inch letters and drill numbers."""
		return self._instance.ShowANSIInchLetterNumberDrillSizes

	@show_a_n_s_i_inch_letter_number_drill_sizes.setter
	def show_a_n_s_i_inch_letter_number_drill_sizes(self, value):
		"""Gets or sets whether to display hole sizes in this hole table using ANSI inch letters and drill numbers."""
		self._instance.ShowANSIInchLetterNumberDrillSizes = value

	@property
	def starting_value(self):
		"""Gets or sets the starting value for the datum tags of this hole table."""
		return self._instance.StartingValue

	@starting_value.setter
	def starting_value(self, value):
		"""Gets or sets the starting value for the datum tags of this hole table."""
		self._instance.StartingValue = value

	@property
	def tag_style(self):
		"""Gets or sets the tag style for this hole table."""
		return self._instance.TagStyle

	@tag_style.setter
	def tag_style(self, value):
		"""Gets or sets the tag style for this hole table."""
		self._instance.TagStyle = value

	@property
	def add_hole(self):
		"""Adds holes to this hole table."""
		return self._instance.AddHole

	@add_hole.setter
	def add_hole(self, value):
		"""Adds holes to this hole table."""
		self._instance.AddHole = value

	@property
	def assign_tag_prefix(self):
		"""Prefixes the manual datum tags of specified holes with specified text."""
		return self._instance.AssignTagPrefix

	@assign_tag_prefix.setter
	def assign_tag_prefix(self, value):
		"""Prefixes the manual datum tags of specified holes with specified text."""
		self._instance.AssignTagPrefix = value

	@property
	def get_feature(self):
		"""Gets the IFeature object for this hole table."""
		return self._instance.GetFeature

	@get_feature.setter
	def get_feature(self, value):
		"""Gets the IFeature object for this hole table."""
		self._instance.GetFeature = value

	@property
	def get_hole_location_precision(self):
		"""Gets the precision to use for location values for this hole table."""
		return self._instance.GetHoleLocationPrecision

	@get_hole_location_precision.setter
	def get_hole_location_precision(self, value):
		"""Gets the precision to use for location values for this hole table."""
		self._instance.GetHoleLocationPrecision = value

	@property
	def get_hole_location_use_doc_precision(self):
		"""Gets whether to display the location of this hole table using the document's location precision."""
		return self._instance.GetHoleLocationUseDocPrecision

	@get_hole_location_use_doc_precision.setter
	def get_hole_location_use_doc_precision(self, value):
		"""Gets whether to display the location of this hole table using the document's location precision."""
		self._instance.GetHoleLocationUseDocPrecision = value

	@property
	def get_table_annotation_count(self):
		"""Gets the number of hole table annotations for this hole table."""
		return self._instance.GetTableAnnotationCount

	@get_table_annotation_count.setter
	def get_table_annotation_count(self, value):
		"""Gets the number of hole table annotations for this hole table."""
		self._instance.GetTableAnnotationCount = value

	@property
	def get_table_annotations(self):
		"""Gets the hole table annotations for this hole table feature."""
		return self._instance.GetTableAnnotations

	@get_table_annotations.setter
	def get_table_annotations(self, value):
		"""Gets the hole table annotations for this hole table feature."""
		self._instance.GetTableAnnotations = value

	@property
	def i_get_table_annotations(self):
		"""Gets the hole table annotations for this hole table feature."""
		return self._instance.IGetTableAnnotations

	@i_get_table_annotations.setter
	def i_get_table_annotations(self, value):
		"""Gets the hole table annotations for this hole table feature."""
		self._instance.IGetTableAnnotations = value

	@property
	def set_hole_location_precision(self):
		"""Sets the precision to use for location values for this hole table."""
		return self._instance.SetHoleLocationPrecision

	@set_hole_location_precision.setter
	def set_hole_location_precision(self, value):
		"""Sets the precision to use for location values for this hole table."""
		self._instance.SetHoleLocationPrecision = value

