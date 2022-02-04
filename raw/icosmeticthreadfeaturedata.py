# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticThreadFeatureData_members.html
class ICosmeticThreadFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def apply_thread(self):
		"""Gets or sets how to apply the cosmetic thread."""
		return self._instance.ApplyThread

	@apply_thread.setter
	def apply_thread(self, value):
		"""Gets or sets how to apply the cosmetic thread."""
		self._instance.ApplyThread = value

	@property
	def blind_depth(self):
		"""Gets or sets the depth of a blind cosmetic thread."""
		return self._instance.BlindDepth

	@blind_depth.setter
	def blind_depth(self, value):
		"""Gets or sets the depth of a blind cosmetic thread."""
		self._instance.BlindDepth = value

	@property
	def configuration_names(self):
		"""Gets or sets the thread configuration names."""
		return self._instance.ConfigurationNames

	@configuration_names.setter
	def configuration_names(self, value):
		"""Gets or sets the thread configuration names."""
		self._instance.ConfigurationNames = value

	@property
	def configuration_option(self):
		"""Gets or sets the thread configuration option."""
		return self._instance.ConfigurationOption

	@configuration_option.setter
	def configuration_option(self, value):
		"""Gets or sets the thread configuration option."""
		self._instance.ConfigurationOption = value

	@property
	def diameter(self):
		"""Gets or sets the value of the diameter of the cosmetic thread."""
		return self._instance.Diameter

	@diameter.setter
	def diameter(self, value):
		"""Gets or sets the value of the diameter of the cosmetic thread."""
		self._instance.Diameter = value

	@property
	def diameter_type(self):
		"""Gets the type of diameter for the cosmetic thread."""
		return self._instance.DiameterType

	@diameter_type.setter
	def diameter_type(self, value):
		"""Gets the type of diameter for the cosmetic thread."""
		self._instance.DiameterType = value

	@property
	def edge(self):
		"""Gets or sets the circular edge to which this cosmetic thread is attached."""
		return self._instance.Edge

	@edge.setter
	def edge(self, value):
		"""Gets or sets the circular edge to which this cosmetic thread is attached."""
		self._instance.Edge = value

	@property
	def end_condition(self):
		"""Gets or sets the thread end condition."""
		return self._instance.EndCondition

	@end_condition.setter
	def end_condition(self, value):
		"""Gets or sets the thread end condition."""
		self._instance.EndCondition = value

	@property
	def patterned_transforms(self):
		"""Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature."""
		return self._instance.PatternedTransforms

	@patterned_transforms.setter
	def patterned_transforms(self, value):
		"""Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature."""
		self._instance.PatternedTransforms = value

	@property
	def size(self):
		"""Gets or sets the thread size."""
		return self._instance.Size

	@size.setter
	def size(self, value):
		"""Gets or sets the thread size."""
		self._instance.Size = value

	@property
	def standard(self):
		"""Gets or sets the thread standard."""
		return self._instance.Standard

	@standard.setter
	def standard(self, value):
		"""Gets or sets the thread standard."""
		self._instance.Standard = value

	@property
	def standard_type(self):
		"""Gets or sets the thread standard type."""
		return self._instance.StandardType

	@standard_type.setter
	def standard_type(self, value):
		"""Gets or sets the thread standard type."""
		self._instance.StandardType = value

	@property
	def start_from_face_plane(self):
		"""Gets or sets the start face or plane."""
		return self._instance.StartFromFacePlane

	@start_from_face_plane.setter
	def start_from_face_plane(self, value):
		"""Gets or sets the start face or plane."""
		self._instance.StartFromFacePlane = value

	@property
	def thread_callout(self):
		"""Gets or sets the callout text for this cosmetic thread feature in a drawing."""
		return self._instance.ThreadCallout

	@thread_callout.setter
	def thread_callout(self, value):
		"""Gets or sets the callout text for this cosmetic thread feature in a drawing."""
		self._instance.ThreadCallout = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this cosmetic thread feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this cosmetic thread feature."""
		self._instance.AccessSelections = value

	@property
	def get_patterned_transforms_count(self):
		"""Gets the number of instances of this cosmetic thread that are patterns of this feature."""
		return self._instance.GetPatternedTransformsCount

	@get_patterned_transforms_count.setter
	def get_patterned_transforms_count(self, value):
		"""Gets the number of instances of this cosmetic thread that are patterns of this feature."""
		self._instance.GetPatternedTransformsCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections that define this cosmetic thread feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections that define this cosmetic thread feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_patterned_transforms(self):
		"""Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature."""
		return self._instance.IGetPatternedTransforms

	@i_get_patterned_transforms.setter
	def i_get_patterned_transforms(self, value):
		"""Gets the transforms from this cosmetic thread for all of the instances of this cosmetic thread that are patterns of this feature."""
		self._instance.IGetPatternedTransforms = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this cosmetic thread feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this cosmetic thread feature."""
		self._instance.ReleaseSelectionAccess = value

