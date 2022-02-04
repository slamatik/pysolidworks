# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData_members.html
class ISplitLineFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the angle by which to project the split line feature."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the angle by which to project the split line feature."""
		self._instance.Angle = value

	@property
	def contours(self):
		"""Gets or sets the contours for this split line feature."""
		return self._instance.Contours

	@contours.setter
	def contours(self, value):
		"""Gets or sets the contours for this split line feature."""
		self._instance.Contours = value

	@property
	def faces(self):
		"""Gets or sets the faces to split by the split line."""
		return self._instance.Faces

	@faces.setter
	def faces(self, value):
		"""Gets or sets the faces to split by the split line."""
		self._instance.Faces = value

	@property
	def pull_direction_base(self):
		"""Gets or sets the entity indicating the direction of pull of this split line feature."""
		return self._instance.PullDirectionBase

	@pull_direction_base.setter
	def pull_direction_base(self, value):
		"""Gets or sets the entity indicating the direction of pull of this split line feature."""
		self._instance.PullDirectionBase = value

	@property
	def pull_direction_type(self):
		"""Gets the type of entity indicating the direction of pull for this split line feature."""
		return self._instance.PullDirectionType

	@pull_direction_type.setter
	def pull_direction_type(self, value):
		"""Gets the type of entity indicating the direction of pull for this split line feature."""
		self._instance.PullDirectionType = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of pull of this split line."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of pull of this split line."""
		self._instance.ReverseDirection = value

	@property
	def single_direction(self):
		"""Gets or sets whether the projection split line is in a single direction."""
		return self._instance.SingleDirection

	@single_direction.setter
	def single_direction(self, value):
		"""Gets or sets whether the projection split line is in a single direction."""
		self._instance.SingleDirection = value

	@property
	def sketch(self):
		"""Gets the seed sketch for this split line feature."""
		return self._instance.Sketch

	@sketch.setter
	def sketch(self, value):
		"""Gets the seed sketch for this split line feature."""
		self._instance.Sketch = value

	@property
	def split_all(self):
		"""Gets or sets whether to split all targets."""
		return self._instance.SplitAll

	@split_all.setter
	def split_all(self, value):
		"""Gets or sets whether to split all targets."""
		self._instance.SplitAll = value

	@property
	def split_targets(self):
		"""Gets or sets the faces or bodies to split."""
		return self._instance.SplitTargets

	@split_targets.setter
	def split_targets(self, value):
		"""Gets or sets the faces or bodies to split."""
		self._instance.SplitTargets = value

	@property
	def split_tools(self):
		"""Gets or sets the tools used to make the split."""
		return self._instance.SplitTools

	@split_tools.setter
	def split_tools(self, value):
		"""Gets or sets the tools used to make the split."""
		self._instance.SplitTools = value

	@property
	def split_type(self):
		"""Gets or sets the type of split."""
		return self._instance.SplitType

	@split_type.setter
	def split_type(self, value):
		"""Gets or sets the type of split."""
		self._instance.SplitType = value

	@property
	def access_selections(self):
		"""Gains access to a split line feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to a split line feature."""
		self._instance.AccessSelections = value

	@property
	def get_contours_count(self):
		"""Gets the number of selected contours for this split line feature."""
		return self._instance.GetContoursCount

	@get_contours_count.setter
	def get_contours_count(self, value):
		"""Gets the number of selected contours for this split line feature."""
		self._instance.GetContoursCount = value

	@property
	def get_faces_count(self):
		"""Gets the number of faces split by this split line."""
		return self._instance.GetFacesCount

	@get_faces_count.setter
	def get_faces_count(self, value):
		"""Gets the number of faces split by this split line."""
		self._instance.GetFacesCount = value

	@property
	def get_split_targets_count(self):
		"""Gets the number of faces or bodies to split."""
		return self._instance.GetSplitTargetsCount

	@get_split_targets_count.setter
	def get_split_targets_count(self, value):
		"""Gets the number of faces or bodies to split."""
		self._instance.GetSplitTargetsCount = value

	@property
	def get_split_tools_count(self):
		"""Gets the number of tools used to make the split."""
		return self._instance.GetSplitToolsCount

	@get_split_tools_count.setter
	def get_split_tools_count(self, value):
		"""Gets the number of tools used to make the split."""
		self._instance.GetSplitToolsCount = value

	@property
	def get_type(self):
		"""Gets the type of split line feature."""
		return self._instance.GetType

	@get_type.setter
	def get_type(self, value):
		"""Gets the type of split line feature."""
		self._instance.GetType = value

	@property
	def i_get_contours(self):
		"""Gets the selected contours for this split line feature."""
		return self._instance.IGetContours

	@i_get_contours.setter
	def i_get_contours(self, value):
		"""Gets the selected contours for this split line feature."""
		self._instance.IGetContours = value

	@property
	def i_get_faces(self):
		"""Gets the faces split by the split line."""
		return self._instance.IGetFaces

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets the faces split by the split line."""
		self._instance.IGetFaces = value

	@property
	def i_get_split_targets(self):
		"""Gets the faces or bodies to split."""
		return self._instance.IGetSplitTargets

	@i_get_split_targets.setter
	def i_get_split_targets(self, value):
		"""Gets the faces or bodies to split."""
		self._instance.IGetSplitTargets = value

	@property
	def i_get_split_tools(self):
		"""Gets the tools to use to make the split."""
		return self._instance.IGetSplitTools

	@i_get_split_tools.setter
	def i_get_split_tools(self, value):
		"""Gets the tools to use to make the split."""
		self._instance.IGetSplitTools = value

	@property
	def i_set_contours(self):
		"""Sets the selected contours for this split line feature."""
		return self._instance.ISetContours

	@i_set_contours.setter
	def i_set_contours(self, value):
		"""Sets the selected contours for this split line feature."""
		self._instance.ISetContours = value

	@property
	def i_set_faces(self):
		"""Sets the faces split by the split line."""
		return self._instance.ISetFaces

	@i_set_faces.setter
	def i_set_faces(self, value):
		"""Sets the faces split by the split line."""
		self._instance.ISetFaces = value

	@property
	def i_set_split_targets(self):
		"""Sets the faces or bodies to split."""
		return self._instance.ISetSplitTargets

	@i_set_split_targets.setter
	def i_set_split_targets(self, value):
		"""Sets the faces or bodies to split."""
		self._instance.ISetSplitTargets = value

	@property
	def i_set_split_tools(self):
		"""Sets the tools used to make the split."""
		return self._instance.ISetSplitTools

	@i_set_split_tools.setter
	def i_set_split_tools(self, value):
		"""Sets the tools used to make the split."""
		self._instance.ISetSplitTools = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this split line feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this split line feature."""
		self._instance.ReleaseSelectionAccess = value

