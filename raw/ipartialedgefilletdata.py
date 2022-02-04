# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.html
class IPartialEdgeFilletData:
	def __init__(self, parent=None):
		self._instance = parent

	def along_edge_direction(self):
		"""Gets which end of the edge to start the fillet."""
		# return self._instance.AlongEdgeDirection
		raise NotImplemented

	def distance_offset_end(self):
		"""Gets the offset distance from the end point for this partial edge fillet."""
		# return self._instance.DistanceOffsetEnd
		raise NotImplemented

	def distance_offset_start(self):
		"""Gets the offset distance from the start point for this partial edge fillet."""
		# return self._instance.DistanceOffsetStart
		raise NotImplemented

	def end_condition(self):
		"""Gets the type of end condition for this partial edge fillet."""
		# return self._instance.EndCondition
		raise NotImplemented

	def percent_offset_end(self):
		"""Gets the percentage offset from the end point for this partial edge fillet."""
		# return self._instance.PercentOffsetEnd
		raise NotImplemented

	def percent_offset_start(self):
		"""Gets the percentage offset from the start point for this partial edge fillet."""
		# return self._instance.PercentOffsetStart
		raise NotImplemented

	def reference_offset_end(self):
		"""Gets the offset reference for the end condition for this partial edge fillet."""
		# return self._instance.ReferenceOffsetEnd
		raise NotImplemented

	def reference_offset_end_type(self):
		"""Gets the type of offset reference for the end condition for this partial edge fillet."""
		# return self._instance.ReferenceOffsetEndType
		raise NotImplemented

	def reference_offset_start(self):
		"""Gets the offset reference for the start condition for this partial edge fillet."""
		# return self._instance.ReferenceOffsetStart
		raise NotImplemented

	def reference_offset_start_type(self):
		"""Gets the type of offset reference for the start condition for this partial edge fillet."""
		# return self._instance.ReferenceOffsetStartType
		raise NotImplemented

	def start_condition(self):
		"""Gets the type of start condition for this partial edge fillet."""
		# return self._instance.StartCondition
		raise NotImplemented

	def set_partial_fillet_parameters(self, along_edge_direction, start_condition, start_value, start_reference, end_condition, end_value, end_reference):
		"""
		Sets the properties of this partial edge fillet.
		:param along_edge_direction: True to start the fillet at the start point of the edge, false to start the fillet at the end point of the edge
		:param start_condition: Start condition as defined in swSimpleFilletPartialEdgeCondition_e (see Remarks)
		:param start_value: Distance or percent offset from the start point (see Remarks)
		:param start_reference: Offset reference (2D/3D sketch point, reference point, planar face); valid only if StartCondition is swPartialEdgeReferenceOffset
		:param end_condition: End condition as defined in swSimpleFilletPartialEdgeCondition_e (see Remarks)
		:param end_value: Distance or percent offset from the end point (see Remarks)
		:param end_reference: Offset reference (2D/3D sketch point, reference point, planar face); valid only if EndCondition is swPartialEdgeReferenceOffset
		"""
		# return self._instance.SetPartialFilletParameters(along_edge_direction, start_condition, start_value, start_reference, end_condition, end_value, end_reference)
		raise NotImplemented

