# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHemFeatureData_members.html
class IHemFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def angle(self):
		"""Gets or sets the hem size angle."""
		return self._instance.Angle

	@angle.setter
	def angle(self, value):
		"""Gets or sets the hem size angle."""
		self._instance.Angle = value

	@property
	def bend_position(self):
		"""Gets or sets the bend position."""
		return self._instance.BendPosition

	@bend_position.setter
	def bend_position(self, value):
		"""Gets or sets the bend position."""
		self._instance.BendPosition = value

	@property
	def edges(self):
		"""Gets or sets the edges for this hem feature."""
		return self._instance.Edges

	@edges.setter
	def edges(self, value):
		"""Gets or sets the edges for this hem feature."""
		self._instance.Edges = value

	@property
	def gap_distance(self):
		"""Gets or sets the hem gap distance for open hems only."""
		return self._instance.GapDistance

	@gap_distance.setter
	def gap_distance(self, value):
		"""Gets or sets the hem gap distance for open hems only."""
		self._instance.GapDistance = value

	@property
	def length(self):
		"""Gets or sets the hem length for closed and open hems only."""
		return self._instance.Length

	@length.setter
	def length(self, value):
		"""Gets or sets the hem length for closed and open hems only."""
		self._instance.Length = value

	@property
	def miter_gap(self):
		"""Gets or sets the miter gap for this hem feature."""
		return self._instance.MiterGap

	@miter_gap.setter
	def miter_gap(self, value):
		"""Gets or sets the miter gap for this hem feature."""
		self._instance.MiterGap = value

	@property
	def radius(self):
		"""Gets or sets the hem radius for tear drop and rolled hems only."""
		return self._instance.Radius

	@radius.setter
	def radius(self, value):
		"""Gets or sets the hem radius for tear drop and rolled hems only."""
		self._instance.Radius = value

	@property
	def reverse_direction(self):
		"""Gets or sets the reverse direction for this hem feature."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets the reverse direction for this hem feature."""
		self._instance.ReverseDirection = value

	@property
	def type(self):
		"""Gets or sets the hem type."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the hem type."""
		self._instance.Type = value

	@property
	def use_default_bend_allowance(self):
		"""Gets or sets whether to use the default bend allowance state for this hem feature."""
		return self._instance.UseDefaultBendAllowance

	@use_default_bend_allowance.setter
	def use_default_bend_allowance(self, value):
		"""Gets or sets whether to use the default bend allowance state for this hem feature."""
		self._instance.UseDefaultBendAllowance = value

	@property
	def access_selections(self):
		"""Gains access to selections used to define the hem feature."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to selections used to define the hem feature."""
		self._instance.AccessSelections = value

	@property
	def get_custom_bend_allowance(self):
		"""Gets the custom bend allowance for the hem feature."""
		return self._instance.GetCustomBendAllowance

	@get_custom_bend_allowance.setter
	def get_custom_bend_allowance(self, value):
		"""Gets the custom bend allowance for the hem feature."""
		self._instance.GetCustomBendAllowance = value

	@property
	def get_edges_count(self):
		"""Gets the number of edges for this hem."""
		return self._instance.GetEdgesCount

	@get_edges_count.setter
	def get_edges_count(self, value):
		"""Gets the number of edges for this hem."""
		self._instance.GetEdgesCount = value

	@property
	def i_access_selections(self):
		"""Gains access to selections used to define the hem feature."""
		return self._instance.IAccessSelections

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to selections used to define the hem feature."""
		self._instance.IAccessSelections = value

	@property
	def i_get_edges(self):
		"""Gets the edges for this hem."""
		return self._instance.IGetEdges

	@i_get_edges.setter
	def i_get_edges(self, value):
		"""Gets the edges for this hem."""
		self._instance.IGetEdges = value

	@property
	def i_set_edges(self):
		"""Sets the edges for this hem feature."""
		return self._instance.ISetEdges

	@i_set_edges.setter
	def i_set_edges(self, value):
		"""Sets the edges for this hem feature."""
		self._instance.ISetEdges = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections for this hem feature."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections for this hem feature."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_custom_bend_allowance(self):
		"""Sets the custom bend allowance for the hem feature."""
		return self._instance.SetCustomBendAllowance

	@set_custom_bend_allowance.setter
	def set_custom_bend_allowance(self, value):
		"""Sets the custom bend allowance for the hem feature."""
		self._instance.SetCustomBendAllowance = value

