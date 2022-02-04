# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITabAndSlotGroupData_members.html
class ITabAndSlotGroupData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def d_offset_from_start(self):
		"""Gets or sets the starting offset of the tabs/slots in this group."""
		return self._instance.D1OffsetFromStart

	@d_offset_from_start.setter
	def d_offset_from_start(self, value):
		"""Gets or sets the starting offset of the tabs/slots in this group."""
		self._instance.D1OffsetFromStart = value

	@property
	def d_offset_from_end(self):
		"""Gets or sets the ending offset of the tabs/slots in this group."""
		return self._instance.D2OffsetFromEnd

	@d_offset_from_end.setter
	def d_offset_from_end(self, value):
		"""Gets or sets the ending offset of the tabs/slots in this group."""
		self._instance.D2OffsetFromEnd = value

	@property
	def offset(self):
		"""Gets or sets whether to offset the tabs/slots from the edge of the model."""
		return self._instance.Offset

	@offset.setter
	def offset(self, value):
		"""Gets or sets whether to offset the tabs/slots from the edge of the model."""
		self._instance.Offset = value

	@property
	def selection_end_reference_point(self):
		"""Gets or sets the end location of this Tab and Slot group."""
		return self._instance.SelectionEndReferencePoint

	@selection_end_reference_point.setter
	def selection_end_reference_point(self, value):
		"""Gets or sets the end location of this Tab and Slot group."""
		self._instance.SelectionEndReferencePoint = value

	@property
	def selection_slot_face(self):
		"""Gets or sets the slot face of this Tab and Slot group."""
		return self._instance.SelectionSlotFace

	@selection_slot_face.setter
	def selection_slot_face(self, value):
		"""Gets or sets the slot face of this Tab and Slot group."""
		self._instance.SelectionSlotFace = value

	@property
	def selection_start_reference_point(self):
		"""Gets or sets the start location of this Tab and Slot group."""
		return self._instance.SelectionStartReferencePoint

	@selection_start_reference_point.setter
	def selection_start_reference_point(self, value):
		"""Gets or sets the start location of this Tab and Slot group."""
		self._instance.SelectionStartReferencePoint = value

	@property
	def selection_tab_edge(self):
		"""Gets or sets the tab edge of this Tab and Slot group."""
		return self._instance.SelectionTabEdge

	@selection_tab_edge.setter
	def selection_tab_edge(self, value):
		"""Gets or sets the tab edge of this Tab and Slot group."""
		self._instance.SelectionTabEdge = value

	@property
	def slot_clearance(self):
		"""Gets or sets the offset of the slots relative to the tabs."""
		return self._instance.SlotClearance

	@slot_clearance.setter
	def slot_clearance(self, value):
		"""Gets or sets the offset of the slots relative to the tabs."""
		self._instance.SlotClearance = value

	@property
	def spacing(self):
		"""Gets or sets the spacing between tabs/slots."""
		return self._instance.Spacing

	@spacing.setter
	def spacing(self, value):
		"""Gets or sets the spacing between tabs/slots."""
		self._instance.Spacing = value

	@property
	def spacing_number_of_instances(self):
		"""Gets or sets the number of instances of equally spaced tabs/slots in this group."""
		return self._instance.SpacingNumberOfInstances

	@spacing_number_of_instances.setter
	def spacing_number_of_instances(self, value):
		"""Gets or sets the number of instances of equally spaced tabs/slots in this group."""
		self._instance.SpacingNumberOfInstances = value

	@property
	def spacing_type(self):
		"""Gets or sets the type of spacing of tabs/slots in this group."""
		return self._instance.SpacingType

	@spacing_type.setter
	def spacing_type(self, value):
		"""Gets or sets the type of spacing of tabs/slots in this group."""
		self._instance.SpacingType = value

	@property
	def tab_chamfer_edge_treatment_value(self):
		"""Gets or sets the chamfer distance for tab edges."""
		return self._instance.TabChamferEdgeTreatmentValue

	@tab_chamfer_edge_treatment_value.setter
	def tab_chamfer_edge_treatment_value(self, value):
		"""Gets or sets the chamfer distance for tab edges."""
		self._instance.TabChamferEdgeTreatmentValue = value

	@property
	def tab_edges_type(self):
		"""Gets or sets the tab edge treatment."""
		return self._instance.TabEdgesType

	@tab_edges_type.setter
	def tab_edges_type(self, value):
		"""Gets or sets the tab edge treatment."""
		self._instance.TabEdgesType = value

	@property
	def tab_face(self):
		"""Gets or sets the tab face that defines the tab thickness."""
		return self._instance.TabFace

	@tab_face.setter
	def tab_face(self, value):
		"""Gets or sets the tab face that defines the tab thickness."""
		self._instance.TabFace = value

	@property
	def tab_fillet_edge_treatment_value(self):
		"""Gets or sets the fillet radius for tab edges."""
		return self._instance.TabFilletEdgeTreatmentValue

	@tab_fillet_edge_treatment_value.setter
	def tab_fillet_edge_treatment_value(self, value):
		"""Gets or sets the fillet radius for tab edges."""
		self._instance.TabFilletEdgeTreatmentValue = value

	@property
	def tab_height_type(self):
		"""Gets or sets the type of tab height."""
		return self._instance.TabHeightType

	@tab_height_type.setter
	def tab_height_type(self, value):
		"""Gets or sets the type of tab height."""
		self._instance.TabHeightType = value

	@property
	def tab_height_value(self):
		"""Gets or sets the tab height."""
		return self._instance.TabHeightValue

	@tab_height_value.setter
	def tab_height_value(self, value):
		"""Gets or sets the tab height."""
		self._instance.TabHeightValue = value

	@property
	def tab_length(self):
		"""Gets or sets the tab length."""
		return self._instance.TabLength

	@tab_length.setter
	def tab_length(self, value):
		"""Gets or sets the tab length."""
		self._instance.TabLength = value

	@property
	def tab_offset_value(self):
		"""Gets or sets the tab offset value."""
		return self._instance.TabOffsetValue

	@tab_offset_value.setter
	def tab_offset_value(self, value):
		"""Gets or sets the tab offset value."""
		self._instance.TabOffsetValue = value

	@property
	def tab_reverse_direction(self):
		"""Gets or sets whether to reverse the tab offset from surface value."""
		return self._instance.TabReverseDirection

	@tab_reverse_direction.setter
	def tab_reverse_direction(self, value):
		"""Gets or sets whether to reverse the tab offset from surface value."""
		self._instance.TabReverseDirection = value

	@property
	def tab_thickness(self):
		"""Gets or sets the tab thickness."""
		return self._instance.TabThickness

	@tab_thickness.setter
	def tab_thickness(self, value):
		"""Gets or sets the tab thickness."""
		self._instance.TabThickness = value

