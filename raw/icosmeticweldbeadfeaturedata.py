# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.html
class ICosmeticWeldBeadFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bead_size(self):
		"""Gets or sets the thickness of a weld bead."""
		return self._instance.BeadSize

	@bead_size.setter
	def bead_size(self, value):
		"""Gets or sets the thickness of a weld bead."""
		self._instance.BeadSize = value

	@property
	def from_to_length(self):
		"""Gets or sets whether to enable the from/to length properties."""
		return self._instance.FromToLength

	@from_to_length.setter
	def from_to_length(self, value):
		"""Gets or sets whether to enable the from/to length properties."""
		self._instance.FromToLength = value

	@property
	def from_to_reverse(self):
		"""Gets or sets whether to start the weld from the opposite end."""
		return self._instance.FromToReverse

	@from_to_reverse.setter
	def from_to_reverse(self, value):
		"""Gets or sets whether to start the weld from the opposite end."""
		self._instance.FromToReverse = value

	@property
	def from_to_start_point(self):
		"""Gets or sets the position of the first weld bead with respect to the end of the selected face or edge."""
		return self._instance.FromToStartPoint

	@from_to_start_point.setter
	def from_to_start_point(self, value):
		"""Gets or sets the position of the first weld bead with respect to the end of the selected face or edge."""
		self._instance.FromToStartPoint = value

	@property
	def from_to_weld_length(self):
		"""Gets or sets the length of the weld."""
		return self._instance.FromToWeldLength

	@from_to_weld_length.setter
	def from_to_weld_length(self, value):
		"""Gets or sets the length of the weld."""
		self._instance.FromToWeldLength = value

	@property
	def gap(self):
		"""Gets or sets the gap between intermittent weld beads."""
		return self._instance.Gap

	@gap.setter
	def gap(self, value):
		"""Gets or sets the gap between intermittent weld beads."""
		self._instance.Gap = value

	@property
	def gap_or_pitch(self):
		"""Gets or sets whether to use gap or pitch spacing for intermittent weld beads."""
		return self._instance.GapOrPitch

	@gap_or_pitch.setter
	def gap_or_pitch(self, value):
		"""Gets or sets whether to use gap or pitch spacing for intermittent weld beads."""
		self._instance.GapOrPitch = value

	@property
	def intermittent_weld(self):
		"""Gets or sets whether to enable intermittent weld properties."""
		return self._instance.IntermittentWeld

	@intermittent_weld.setter
	def intermittent_weld(self, value):
		"""Gets or sets whether to enable intermittent weld properties."""
		self._instance.IntermittentWeld = value

	@property
	def intermittent_weld_length(self):
		"""Gets or sets the length of the weld for intermittent weld beads."""
		return self._instance.IntermittentWeldLength

	@intermittent_weld_length.setter
	def intermittent_weld_length(self, value):
		"""Gets or sets the length of the weld for intermittent weld beads."""
		self._instance.IntermittentWeldLength = value

	@property
	def pitch(self):
		"""Gets or sets the pitch of intermittent weld beads."""
		return self._instance.Pitch

	@pitch.setter
	def pitch(self, value):
		"""Gets or sets the pitch of intermittent weld beads."""
		self._instance.Pitch = value

	@property
	def side(self):
		"""Gets or sets how the weld bead is applied to selected faces or edges."""
		return self._instance.Side

	@side.setter
	def side(self, value):
		"""Gets or sets how the weld bead is applied to selected faces or edges."""
		self._instance.Side = value

	@property
	def staggered(self):
		"""Gets or sets whether to alternate the positioning of the weld beads on both sides of the weld body."""
		return self._instance.Staggered

	@staggered.setter
	def staggered(self, value):
		"""Gets or sets whether to alternate the positioning of the weld beads on both sides of the weld body."""
		self._instance.Staggered = value

	@property
	def tangent_propagation(self):
		"""Gets or sets whether to apply the weld bead to all edges that are tangent to the selected faces or edges."""
		return self._instance.TangentPropagation

	@tangent_propagation.setter
	def tangent_propagation(self, value):
		"""Gets or sets whether to apply the weld bead to all edges that are tangent to the selected faces or edges."""
		self._instance.TangentPropagation = value

	@property
	def weld_symbol(self):
		"""Gets or sets the weld symbol for this weld bead."""
		return self._instance.WeldSymbol

	@weld_symbol.setter
	def weld_symbol(self, value):
		"""Gets or sets the weld symbol for this weld bead."""
		self._instance.WeldSymbol = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this cosmetic weld bead feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this cosmetic weld bead feature."""
		self._instance.AccessSelections = value

	@property
	def get_entities_weld_from(self):
		"""Gets the weld-from entity type and weld-from entities for this cosmetic weld bead, which was created using weld geometry."""
		return self._instance.GetEntitiesWeldFrom

	@get_entities_weld_from.setter
	def get_entities_weld_from(self, value):
		"""Gets the weld-from entity type and weld-from entities for this cosmetic weld bead, which was created using weld geometry."""
		self._instance.GetEntitiesWeldFrom = value

	@property
	def get_entities_weld_path(self):
		"""Gets the entities for this cosmetic weld bead, which was created using a weld path."""
		return self._instance.GetEntitiesWeldPath

	@get_entities_weld_path.setter
	def get_entities_weld_path(self, value):
		"""Gets the entities for this cosmetic weld bead, which was created using a weld path."""
		self._instance.GetEntitiesWeldPath = value

	@property
	def get_entities_weld_to(self):
		"""Gets the weld-to entity type and weld-to entities for this cosmetic weld bead, which was created using weld geometry."""
		return self._instance.GetEntitiesWeldTo

	@get_entities_weld_to.setter
	def get_entities_weld_to(self, value):
		"""Gets the weld-to entity type and weld-to entities for this cosmetic weld bead, which was created using weld geometry."""
		self._instance.GetEntitiesWeldTo = value

	@property
	def get_reference_edges(self):
		"""Gets the reference edges created by this cosmetic weld bead feature."""
		return self._instance.GetReferenceEdges

	@get_reference_edges.setter
	def get_reference_edges(self, value):
		"""Gets the reference edges created by this cosmetic weld bead feature."""
		self._instance.GetReferenceEdges = value

	@property
	def get_weld_bead_folder(self):
		"""Gets the weld bead folder."""
		return self._instance.GetWeldBeadFolder

	@get_weld_bead_folder.setter
	def get_weld_bead_folder(self, value):
		"""Gets the weld bead folder."""
		self._instance.GetWeldBeadFolder = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this cosmetic weld bead feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this cosmetic weld bead feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_entities_weld_from(self):
		"""Sets the weld-from entities for this cosmetic weld bead, which was created using weld geometry."""
		return self._instance.SetEntitiesWeldFrom

	@set_entities_weld_from.setter
	def set_entities_weld_from(self, value):
		"""Sets the weld-from entities for this cosmetic weld bead, which was created using weld geometry."""
		self._instance.SetEntitiesWeldFrom = value

	@property
	def set_entities_weld_path(self):
		"""Sets the entities for this cosmetic weld bead, which was created using a weld path."""
		return self._instance.SetEntitiesWeldPath

	@set_entities_weld_path.setter
	def set_entities_weld_path(self, value):
		"""Sets the entities for this cosmetic weld bead, which was created using a weld path."""
		self._instance.SetEntitiesWeldPath = value

	@property
	def set_entities_weld_to(self):
		"""Sets the weld-to entities for this cosmetic weld bead, which was created using weld geometry."""
		return self._instance.SetEntitiesWeldTo

	@set_entities_weld_to.setter
	def set_entities_weld_to(self, value):
		"""Sets the weld-to entities for this cosmetic weld bead, which was created using weld geometry."""
		self._instance.SetEntitiesWeldTo = value

