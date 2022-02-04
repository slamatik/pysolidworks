# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.html
class IPMIGtolData:
	def __init__(self, parent=None):
		self._instance = parent

	def instance_count(self):
		"""Gets the number of times this PMI Gtol is repeated.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.InstanceCount
		raise NotImplemented

	def leader_location(self):
		"""Gets the leader location of this PMI Gtol.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.LeaderLocation
		raise NotImplemented

	def leader_modifier(self):
		"""Gets the leader modifier of this PMI Gtol.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.LeaderModifier
		raise NotImplemented

	def leader_style(self):
		"""Gets the leader style of this PMI Gtol.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.LeaderStyle
		raise NotImplemented

	def leader_type(self):
		"""Gets the leader type of this PMI Gtol.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.LeaderType
		raise NotImplemented

	def get_first_point(self):
		"""Gets the label of the first point for tolerances applied between two points or entities in this PMI Gtol."""
		# return self._instance.GetFirstPoint
		raise NotImplemented

	def get_frame_at_index(self, index):
		"""
		Gets the data of the frame at the specified index of this PMI Gtol.
		:param index: Zero-based index of the frame to get
		"""
		# return self._instance.GetFrameAtIndex(index)
		raise NotImplemented

	def get_frame_count(self):
		"""Gets the number of frames in this PMI Gtol."""
		# return self._instance.GetFrameCount
		raise NotImplemented

	def get_second_point(self):
		"""Gets the label of the second point for tolerances applied between two points or entities in this PMI Gtol."""
		# return self._instance.GetSecondPoint
		raise NotImplemented

	def get_text(self):
		"""Gets the text of this PMI Gtol."""
		# return self._instance.GetText
		raise NotImplemented

	def get_text_below_frames(self):
		"""Gets the text below the feature control frame of this PMI Gtol."""
		# return self._instance.GetTextBelowFrames
		raise NotImplemented

	def is_composite(self):
		"""Gets whether this PMI Gtol combines the symbols of two frames."""
		# return self._instance.IsComposite
		raise NotImplemented

