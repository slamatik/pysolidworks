# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData_members.html
class IPartingLineFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the draft angle for the parting line."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the draft angle for the parting line."""
		self._instance.Angle = value

	@property
	def core_cavity_split(self):
		"""Gets or sets the core/cavity split option for a parting line."""
		return self._instance.CoreCavitySplit

	@core_cavity_split.setter
	def core_cavity_split(self, value):
		"""Gets or sets the core/cavity split option for a parting line."""
		self._instance.CoreCavitySplit = value

	@property
	def parting_lines(self):
		"""Gets and sets the edges for the parting lines."""
		return self._instance.PartingLines

	@parting_lines.setter
	def parting_lines(self, value):
		"""Gets and sets the edges for the parting lines."""
		self._instance.PartingLines = value

	@property
	def pull_direction(self):
		"""Gets whether the direction of pull is reversed."""
		return self._instance.PullDirection

	@pull_direction.setter
	def pull_direction(self, value):
		"""Gets whether the direction of pull is reversed."""
		self._instance.PullDirection = value

	@property
	def pull_direction_base(self):
		"""Gets or sets the direction of pull for the parting line feature."""
		return self._instance.PullDirectionBase

	@pull_direction_base.setter
	def pull_direction_base(self, value):
		"""Gets or sets the direction of pull for the parting line feature."""
		self._instance.PullDirectionBase = value

	@property
	def pull_direction_type(self):
		"""Gets the type of entity indicating the direction of pull."""
		return self._instance.PullDirectionType

	@pull_direction_type.setter
	def pull_direction_type(self, value):
		"""Gets the type of entity indicating the direction of pull."""
		self._instance.PullDirectionType = value

	@property
	def split_faces(self):
		"""Gets or sets whether to split faces."""
		return self._instance.SplitFaces

	@split_faces.setter
	def split_faces(self, value):
		"""Gets or sets whether to split faces."""
		self._instance.SplitFaces = value

	@property
	def split_faces_option(self):
		"""Gets or sets the split faces option for this parting line."""
		return self._instance.SplitFacesOption

	@split_faces_option.setter
	def split_faces_option(self, value):
		"""Gets or sets the split faces option for this parting line."""
		self._instance.SplitFacesOption = value

	@property
	def access_selections(self):
		"""Gains access to the selections that describe the parting line feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that describe the parting line feature."""
		self._instance.AccessSelections = value

	@property
	def draft_analysis(self):
		"""Performs draft analysis for the input angle and the direction of pull."""
		return self._instance.DraftAnalysis

	@draft_analysis.setter
	def draft_analysis(self, value):
		"""Performs draft analysis for the input angle and the direction of pull."""
		self._instance.DraftAnalysis = value

	@property
	def get_entities_to_split(self):
		"""Gets the entities that are used to split a face."""
		return self._instance.GetEntitiesToSplit

	@get_entities_to_split.setter
	def get_entities_to_split(self, value):
		"""Gets the entities that are used to split a face."""
		self._instance.GetEntitiesToSplit = value

	@property
	def get_entities_to_split_count(self):
		"""Gets the number of entities to use to split a face and add edges to the parting line feature."""
		return self._instance.GetEntitiesToSplitCount

	@get_entities_to_split_count.setter
	def get_entities_to_split_count(self, value):
		"""Gets the number of entities to use to split a face and add edges to the parting line feature."""
		self._instance.GetEntitiesToSplitCount = value

	@property
	def get_faces_by_type(self):
		"""Gets the specified faces after performing a draft analysis of the parting line feature."""
		return self._instance.GetFacesByType

	@get_faces_by_type.setter
	def get_faces_by_type(self, value):
		"""Gets the specified faces after performing a draft analysis of the parting line feature."""
		self._instance.GetFacesByType = value

	@property
	def get_faces_by_type_count(self):
		"""Gets the number of faces of the specified type for this parting line."""
		return self._instance.GetFacesByTypeCount

	@get_faces_by_type_count.setter
	def get_faces_by_type_count(self, value):
		"""Gets the number of faces of the specified type for this parting line."""
		self._instance.GetFacesByTypeCount = value

	@property
	def get_parting_lines_count(self):
		"""Gets the number of edges used as parting lines."""
		return self._instance.GetPartingLinesCount

	@get_parting_lines_count.setter
	def get_parting_lines_count(self, value):
		"""Gets the number of edges used as parting lines."""
		self._instance.GetPartingLinesCount = value

	@property
	def i_get_entities_to_split(self):
		"""Gets the entities that are used to split a face."""
		return self._instance.IGetEntitiesToSplit

	@i_get_entities_to_split.setter
	def i_get_entities_to_split(self, value):
		"""Gets the entities that are used to split a face."""
		self._instance.IGetEntitiesToSplit = value

	@property
	def i_get_faces_by_type(self):
		"""Gets the specified faces after performing a draft analysis of the parting line feature."""
		return self._instance.IGetFacesByType

	@i_get_faces_by_type.setter
	def i_get_faces_by_type(self, value):
		"""Gets the specified faces after performing a draft analysis of the parting line feature."""
		self._instance.IGetFacesByType = value

	@property
	def i_get_parting_lines(self):
		"""Gets the edges used as parting lines."""
		return self._instance.IGetPartingLines

	@i_get_parting_lines.setter
	def i_get_parting_lines(self, value):
		"""Gets the edges used as parting lines."""
		self._instance.IGetPartingLines = value

	@property
	def i_set_entities_to_split(self):
		"""Sets the entities to use to split a face and add edges to the parting line feature."""
		return self._instance.ISetEntitiesToSplit

	@i_set_entities_to_split.setter
	def i_set_entities_to_split(self, value):
		"""Sets the entities to use to split a face and add edges to the parting line feature."""
		self._instance.ISetEntitiesToSplit = value

	@property
	def i_set_parting_lines(self):
		"""Sets the edges to use as parting lines."""
		return self._instance.ISetPartingLines

	@i_set_parting_lines.setter
	def i_set_parting_lines(self, value):
		"""Sets the edges to use as parting lines."""
		self._instance.ISetPartingLines = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this parting line feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this parting line feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_entities_to_split(self):
		"""Sets the entities to use to split a face and add edges to the parting line feature."""
		return self._instance.SetEntitiesToSplit

	@set_entities_to_split.setter
	def set_entities_to_split(self, value):
		"""Sets the entities to use to split a face and add edges to the parting line feature."""
		self._instance.SetEntitiesToSplit = value

	@property
	def status(self):
		"""Gets the status of this parting line feature."""
		return self._instance.Status

	@status.setter
	def status(self, value):
		"""Gets the status of this parting line feature."""
		self._instance.Status = value

