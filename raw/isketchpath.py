# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPath_members.html
class ISketchPath:
	def __init__(self, parent=None):
		self._instance = parent

	def get_constraints(self):
		"""Gets the names of the constraints in this sketch path."""
		# return self._instance.GetConstraints
		raise NotImplemented

	def get_constraints_count(self):
		"""Gets the number of constraints in this sketch path."""
		# return self._instance.GetConstraintsCount
		raise NotImplemented

	def get_length(self):
		"""Gets the length of the sketch path."""
		# return self._instance.GetLength
		raise NotImplemented

	def get_relations(self):
		"""Gets the sketch relations for this sketch path."""
		# return self._instance.GetRelations
		raise NotImplemented

	def get_relations_count(self):
		"""Gets the number of sketch relations in this sketch path."""
		# return self._instance.GetRelationsCount
		raise NotImplemented

	def get_sketch(self):
		"""Gets the sketch where this sketch path exists."""
		# return self._instance.GetSketch
		raise NotImplemented

	def get_sketch_segment_count(self):
		"""Gets the number of sketch segments in this sketch path."""
		# return self._instance.GetSketchSegmentCount
		raise NotImplemented

	def get_sketch_segments(self):
		"""Gets the sketch segments in this sketch path."""
		# return self._instance.GetSketchSegments
		raise NotImplemented

	def i_get_constraints(self, count):
		"""
		Gets the names of the constraints in this sketch path.
		:param count: Number of sketch constraints
		"""
		# return self._instance.IGetConstraints(count)
		raise NotImplemented

	def i_get_relations(self, count):
		"""
		Gets the sketch relations for this sketch path.
		:param count: Number of sketch relations
		"""
		# return self._instance.IGetRelations(count)
		raise NotImplemented

	def i_get_sketch_segments(self, count):
		"""
		Gets the sketch segments in this sketch path.
		:param count: Number of sketch segments
		"""
		# return self._instance.IGetSketchSegments(count)
		raise NotImplemented

	def select(self, append, data):
		"""
		Selects a sketch path.
		:param append: True appends the entity to the selection list, false replaces the selection list with this entity
		:param data: SelectData object
		"""
		# return self._instance.Select(append, data)
		raise NotImplemented

