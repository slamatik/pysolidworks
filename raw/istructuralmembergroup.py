# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberGroup_members.html
class IStructuralMemberGroup:
	def __init__(self, parent=None):
		self._instance = parent

	def align_axis(self):
		"""Gets and sets the axis on which to align this structural-member group."""
		# return self._instance.AlignAxis
		raise NotImplemented

	def alignment_vector(self):
		"""Gets and sets a reference vector for this structural-member group."""
		# return self._instance.AlignmentVector
		raise NotImplemented

	def angle(self):
		"""Gets and sets the rotational angle of this structural-member group."""
		# return self._instance.Angle
		raise NotImplemented

	def apply_corner_treatment(self):
		"""Gets and sets whether or not to apply a corner treatment to this structural-member group."""
		# return self._instance.ApplyCornerTreatment
		raise NotImplemented

	def corner_treatment_type(self):
		"""Gets and sets the type of corner treatment for this structural-member group."""
		# return self._instance.CornerTreatmentType
		raise NotImplemented

	def gap_for_other_groups(self):
		"""Gets and sets the gap between segments in different structural-member groups."""
		# return self._instance.GapForOtherGroups
		raise NotImplemented

	def gap_within_group(self):
		"""Gets and sets the gap between connected segments within this structural-member group."""
		# return self._instance.GapWithinGroup
		raise NotImplemented

	def locate_profile_point(self):
		"""Gets and sets the point to use to locate the profile for this structural-member group."""
		# return self._instance.LocateProfilePoint
		raise NotImplemented

	@property
	def merge_arc_segment_bodies(self):
		"""Gets or sets whether to merge arc segment bodies with adjacent bodies in this structural-member group."""
		return self._instance.MergeArcSegmentBodies

	@merge_arc_segment_bodies.setter
	def merge_arc_segment_bodies(self, value):
		"""Gets or sets whether to merge arc segment bodies with adjacent bodies in this structural-member group."""
		self._instance.MergeArcSegmentBodies = value

	@property
	def mirror_profile(self):
		"""Gets and sets whether to mirror the profile of this structural-member group."""
		return self._instance.MirrorProfile

	@mirror_profile.setter
	def mirror_profile(self, value):
		"""Gets and sets whether to mirror the profile of this structural-member group."""
		self._instance.MirrorProfile = value

	@property
	def mirror_profile_axis(self):
		"""Gets and sets the axis about which to mirror the profile of this structural-member group."""
		return self._instance.MirrorProfileAxis

	@mirror_profile_axis.setter
	def mirror_profile_axis(self, value):
		"""Gets and sets the axis about which to mirror the profile of this structural-member group."""
		self._instance.MirrorProfileAxis = value

	@property
	def miter_merge_condition(self):
		"""Get or set whether to merge miter trimmed bodies in this structural-member group."""
		return self._instance.MiterMergeCondition

	@miter_merge_condition.setter
	def miter_merge_condition(self, value):
		"""Get or set whether to merge miter trimmed bodies in this structural-member group."""
		self._instance.MiterMergeCondition = value

	@property
	def segments(self):
		"""Gets and sets the sketch segments to use in this structural-member group."""
		return self._instance.Segments

	@segments.setter
	def segments(self, value):
		"""Gets and sets the sketch segments to use in this structural-member group."""
		self._instance.Segments = value

	@property
	def get_segments_count(self):
		"""Gets the number of segments in this structural-member group."""
		return self._instance.GetSegmentsCount

	@get_segments_count.setter
	def get_segments_count(self, value):
		"""Gets the number of segments in this structural-member group."""
		self._instance.GetSegmentsCount = value

	@property
	def i_get_segments(self):
		"""Gets the sketch segments in this structural-member group."""
		return self._instance.IGetSegments

	@i_get_segments.setter
	def i_get_segments(self, value):
		"""Gets the sketch segments in this structural-member group."""
		self._instance.IGetSegments = value

	@property
	def i_set_segments(self):
		"""Sets the sketch segments to use in this structural-member group."""
		return self._instance.ISetSegments

	@i_set_segments.setter
	def i_set_segments(self, value):
		"""Sets the sketch segments to use in this structural-member group."""
		self._instance.ISetSegments = value

