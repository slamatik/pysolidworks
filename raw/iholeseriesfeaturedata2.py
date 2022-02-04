# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html
class IHoleSeriesFeatureData2:
	def __init__(self, parent=None):
		self._instance = parent

	def bolt_diameter(self):
		"""Gets the diameter of the bolt in this hole series."""
		# return self._instance.BoltDiameter
		raise NotImplemented

	def bolt_head_diameter(self):
		"""Gets the diameter of the head of the bolt in this hole series."""
		# return self._instance.BoltHeadDiameter
		raise NotImplemented

	def end_face(self):
		"""Gets the end face for this hole series."""
		# return self._instance.EndFace
		raise NotImplemented

	def fastener_bottom_hole_type(self):
		"""Gets the fastener bottom hole type in this hole series."""
		# return self._instance.FastenerBottomHoleType
		raise NotImplemented

	def fastener_default_units(self):
		"""Gets the fastener default units for this hole series."""
		# return self._instance.FastenerDefaultUnits
		raise NotImplemented

	def fastener_hole_count(self):
		"""Gets the number of fastener holes in this hole series."""
		# return self._instance.FastenerHoleCount
		raise NotImplemented

	def fastener_top_hole_type(self):
		"""Gets the fastener top hole type for this hole series."""
		# return self._instance.FastenerTopHoleType
		raise NotImplemented

	def material(self):
		"""Gets the name of the bolt material in this hole series."""
		# return self._instance.Material
		raise NotImplemented

	def nut_diameter(self):
		"""Gets the diameter of the nut in this hole series."""
		# return self._instance.NutDiameter
		raise NotImplemented

	def preload(self):
		"""Gets the preload information for this hole series."""
		# return self._instance.Preload
		raise NotImplemented

	def size(self, hole_series_which_part):
		"""
		Gets the fastener size in the specified part in this hole series.
		:param hole_series_which_part: Which part the hole series passes through as defined by swHoleSeriesWhichParts_e
		"""
		# return self._instance.Size(hole_series_which_part)
		raise NotImplemented

	def standard(self):
		"""Gets the design standard for this hole series."""
		# return self._instance.Standard
		raise NotImplemented

	def start_face(self):
		"""Gets the start face for this hole series."""
		# return self._instance.StartFace
		raise NotImplemented

	def type(self, hole_series_which_part):
		"""
		Gets the type of fastener in the specified part in this hole series.
		:param hole_series_which_part: Which part the hole series passes through as defined by swHoleSeriesWhichParts_e
		"""
		# return self._instance.Type(hole_series_which_part)
		raise NotImplemented

	def access_selections(self, top_doc, component):
		"""
		Gains access to the selections that define this hole series feature.
		:param top_doc: Top-level document (see Remarks)
		:param component: Component in which the feature is to be modified (see Remarks)
		"""
		# return self._instance.AccessSelections(top_doc, component)
		raise NotImplemented

	def get_components(self):
		"""Gets the components in this hole series."""
		# return self._instance.GetComponents
		raise NotImplemented

	def get_components_count(self):
		"""Gets the number of components in this hole series."""
		# return self._instance.GetComponentsCount
		raise NotImplemented

	def get_hole_bottom_mate_entity(self, hole_instance, hole_type):
		"""
		Gets the entity to which the bottom of the hole is mated in this hole series.
		:param hole_instance: Index number of the hole whose entity you want
		:param hole_type: Type of hole as defined by swWzdHoleTypes_e
		"""
		# return self._instance.GetHoleBottomMateEntity(hole_instance, hole_type)
		raise NotImplemented

	def get_hole_top_mate_entity(self, hole_instance, hole_type):
		"""
		Gets the entity to which the top of the hole is mated in this hole series.
		:param hole_instance: Index number of the hole whose entity you want
		:param hole_type: Type of hole as defined by swWzdHoleTypes_e
		"""
		# return self._instance.GetHoleTopMateEntity(hole_instance, hole_type)
		raise NotImplemented

	def get_sketch_points(self):
		"""Gets the center-hole sketch points in this hole series."""
		# return self._instance.GetSketchPoints
		raise NotImplemented

	def get_sketch_points_count(self):
		"""Gets the number of center-hole sketch points in this hole series."""
		# return self._instance.GetSketchPointsCount
		raise NotImplemented

	def i_access_selections(self, top_doc, component):
		"""
		Gains access to the selections that define this hole series feature.
		:param top_doc: Top-level document (see Remarks)
		:param component: Component in which the feature is to be modified (see Remarks)
		"""
		# return self._instance.IAccessSelections(top_doc, component)
		raise NotImplemented

	def i_get_components(self, n_count):
		"""
		Gets the components in this hole series.
		:param n_count: Number of components in this hole series
		"""
		# return self._instance.IGetComponents(n_count)
		raise NotImplemented

	def i_get_hole_bottom_mate_entity(self, hole_instance, hole_type):
		"""
		Gets the entity to which the bottom of the hole is mated in this hole series.
		:param hole_instance: Index number of the hole whose entity you want
		:param hole_type: Type of hole as defined by swWzdHoleTypes_e
		"""
		# return self._instance.IGetHoleBottomMateEntity(hole_instance, hole_type)
		raise NotImplemented

	def i_get_hole_top_mate_entity(self, hole_instance, hole_type):
		"""
		Gets the entity to which the top of the hole is mated in this hole series.
		:param hole_instance: Index number of the hole whose entity you want
		:param hole_type: Type of hole as defined by swWzdHoleTypes_e
		"""
		# return self._instance.IGetHoleTopMateEntity(hole_instance, hole_type)
		raise NotImplemented

	def i_get_sketch_points(self, n_count):
		"""
		Gets the center-hole sketch points in this hole series.
		:param n_count: Number of center-hole sketch points
		"""
		# return self._instance.IGetSketchPoints(n_count)
		raise NotImplemented

	def release_selection_access(self):
		"""Releases access to the selections that define this hole series feature."""
		# return self._instance.ReleaseSelectionAccess
		raise NotImplemented

