# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumFeature_members.html
class IPMIDatumFeature:
	def __init__(self, parent=None):
		self._instance = parent

	def label(self):
		"""Gets the non-numeric label of this PMI datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Label
		raise NotImplemented

	def leader_anchor_style(self):
		"""Gets the PMI datum leader anchor style.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.LeaderAnchorStyle
		raise NotImplemented

	def leader_bend_length(self):
		"""Gets the length of the unbent portion of the leader to this PMI datum.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.LeaderBendLength
		raise NotImplemented

	def shape(self):
		"""Gets the PMI datum shape.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Shape
		raise NotImplemented

	def text(self):
		"""Gets the PMI datum text.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.Text
		raise NotImplemented

