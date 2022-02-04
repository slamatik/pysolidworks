# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html
class IMate2:
	def __init__(self, parent=None):
		self._instance = parent

	def alignment(self):
		"""Gets the type of alignment for this mate."""
		# return self._instance.Alignment
		raise NotImplemented

	def can_be_flipped(self):
		"""Gets whether this distance or angle mate can be flipped."""
		# return self._instance.CanBeFlipped
		raise NotImplemented

	def display_dimension(self, index):
		"""
		Gets the specified display dimension for this mate.
		:param index: Number indicating which mate's display dimension to get (see Remarks)
		"""
		# return self._instance.DisplayDimension2(index)
		raise NotImplemented

	def distance_first_arc_condition(self):
		"""Gets the the first arc condition of this distance mate between cylindrical components."""
		# return self._instance.DistanceFirstArcCondition
		raise NotImplemented

	def distance_second_arc_condition(self):
		"""Gets the the second arc condition of this distance mate between cylindrical components."""
		# return self._instance.DistanceSecondArcCondition
		raise NotImplemented

	@property
	def flipped(self):
		"""Gets or sets whether to flip the distance or angle mate."""
		return self._instance.Flipped

	@flipped.setter
	def flipped(self, value):
		"""Gets or sets whether to flip the distance or angle mate."""
		self._instance.Flipped = value

	@property
	def has_load_bearing_faces(self):
		"""Gets whether this mate has load bearing faces."""
		return self._instance.HasLoadBearingFaces

	@has_load_bearing_faces.setter
	def has_load_bearing_faces(self, value):
		"""Gets whether this mate has load bearing faces."""
		self._instance.HasLoadBearingFaces = value

	@property
	def has_treat_interference_as_shrink_fit(self):
		"""Gets whether interference in this mate is treated as shrink/press fit."""
		return self._instance.HasTreatInterferenceAsShrinkFit

	@has_treat_interference_as_shrink_fit.setter
	def has_treat_interference_as_shrink_fit(self, value):
		"""Gets whether interference in this mate is treated as shrink/press fit."""
		self._instance.HasTreatInterferenceAsShrinkFit = value

	@property
	def is_load_bearing_faces_bonded(self):
		"""Get whether the load bearing faces of this mate are bonded."""
		return self._instance.IsLoadBearingFacesBonded

	@is_load_bearing_faces_bonded.setter
	def is_load_bearing_faces_bonded(self, value):
		"""Get whether the load bearing faces of this mate are bonded."""
		self._instance.IsLoadBearingFacesBonded = value

	@property
	def lock_magnetic_mate(self):
		"""Gets or sets whether to lock this magnetic mate."""
		return self._instance.LockMagneticMate

	@lock_magnetic_mate.setter
	def lock_magnetic_mate(self, value):
		"""Gets or sets whether to lock this magnetic mate."""
		self._instance.LockMagneticMate = value

	@property
	def mate_load_reference(self):
		"""Gets the mate load reference associated with this mate."""
		return self._instance.MateLoadReference

	@mate_load_reference.setter
	def mate_load_reference(self, value):
		"""Gets the mate load reference associated with this mate."""
		self._instance.MateLoadReference = value

	@property
	def maximum_variation(self):
		"""Gets the maximum variation, in meters or radians, for the dimension of this distance or angle mate."""
		return self._instance.MaximumVariation

	@maximum_variation.setter
	def maximum_variation(self, value):
		"""Gets the maximum variation, in meters or radians, for the dimension of this distance or angle mate."""
		self._instance.MaximumVariation = value

	@property
	def minimum_variation(self):
		"""Gets the minimum variation, in meters or radians, for the dimension of this distance or angle mate."""
		return self._instance.MinimumVariation

	@minimum_variation.setter
	def minimum_variation(self, value):
		"""Gets the minimum variation, in meters or radians, for the dimension of this distance or angle mate."""
		self._instance.MinimumVariation = value

	@property
	def type(self):
		"""Gets the type of mate."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets the type of mate."""
		self._instance.Type = value

	@property
	def force_misalignment(self):
		"""Forces a misaligned mate condition for this concentric mate."""
		return self._instance.ForceMisalignment

	@force_misalignment.setter
	def force_misalignment(self, value):
		"""Forces a misaligned mate condition for this concentric mate."""
		self._instance.ForceMisalignment = value

	@property
	def get_concentric_alignment_type(self):
		"""Gets the alignment type of this mate."""
		return self._instance.GetConcentricAlignmentType

	@get_concentric_alignment_type.setter
	def get_concentric_alignment_type(self, value):
		"""Gets the alignment type of this mate."""
		self._instance.GetConcentricAlignmentType = value

	@property
	def get_current_misaligned_deviation(self):
		"""Gets the current misalignment deviation for the misaligned concentric mate."""
		return self._instance.GetCurrentMisalignedDeviation

	@get_current_misaligned_deviation.setter
	def get_current_misaligned_deviation(self, value):
		"""Gets the current misalignment deviation for the misaligned concentric mate."""
		self._instance.GetCurrentMisalignedDeviation = value

	@property
	def get_force(self):
		"""Gets the magnitude and direction of the force applied to this mate."""
		return self._instance.GetForce

	@get_force.setter
	def get_force(self, value):
		"""Gets the magnitude and direction of the force applied to this mate."""
		self._instance.GetForce = value

	@property
	def get_linked_mate(self):
		"""Gets the linked mate of this concentric mate."""
		return self._instance.GetLinkedMate

	@get_linked_mate.setter
	def get_linked_mate(self, value):
		"""Gets the linked mate of this concentric mate."""
		self._instance.GetLinkedMate = value

	@property
	def get_mate_entity_count(self):
		"""Gets the number of entities for this mate."""
		return self._instance.GetMateEntityCount

	@get_mate_entity_count.setter
	def get_mate_entity_count(self, value):
		"""Gets the number of entities for this mate."""
		self._instance.GetMateEntityCount = value

	@property
	def get_maximum_misaligned_deviation(self):
		"""Gets the maximum allowed misalignment deviation for this misaligned concentric mate."""
		return self._instance.GetMaximumMisalignedDeviation

	@get_maximum_misaligned_deviation.setter
	def get_maximum_misaligned_deviation(self, value):
		"""Gets the maximum allowed misalignment deviation for this misaligned concentric mate."""
		self._instance.GetMaximumMisalignedDeviation = value

	@property
	def get_supplemental_faces(self):
		"""Gets the faces in this mate."""
		return self._instance.GetSupplementalFaces

	@get_supplemental_faces.setter
	def get_supplemental_faces(self, value):
		"""Gets the faces in this mate."""
		self._instance.GetSupplementalFaces = value

	@property
	def get_torque(self):
		"""Gets the angle and the axis of the torque applied to this mate."""
		return self._instance.GetTorque

	@get_torque.setter
	def get_torque(self, value):
		"""Gets the angle and the axis of the torque applied to this mate."""
		self._instance.GetTorque = value

	@property
	def get_use_misaligned_deviation_document_property(self):
		"""Gets whether to use the document property value for the maximum misalignment deviation of the misaligned concentric mate."""
		return self._instance.GetUseMisalignedDeviationDocumentProperty

	@get_use_misaligned_deviation_document_property.setter
	def get_use_misaligned_deviation_document_property(self, value):
		"""Gets whether to use the document property value for the maximum misalignment deviation of the misaligned concentric mate."""
		self._instance.GetUseMisalignedDeviationDocumentProperty = value

	@property
	def i_get_supplemental_faces(self):
		"""Gets the faces in this mate."""
		return self._instance.IGetSupplementalFaces

	@i_get_supplemental_faces.setter
	def i_get_supplemental_faces(self, value):
		"""Gets the faces in this mate."""
		self._instance.IGetSupplementalFaces = value

	@property
	def mate_entity(self):
		"""Gets an entity associated with a mate."""
		return self._instance.MateEntity

	@mate_entity.setter
	def mate_entity(self, value):
		"""Gets an entity associated with a mate."""
		self._instance.MateEntity = value

	@property
	def remove_misalignment(self):
		"""Removes the misaligned mate condition of this concentric mate."""
		return self._instance.RemoveMisalignment

	@remove_misalignment.setter
	def remove_misalignment(self, value):
		"""Removes the misaligned mate condition of this concentric mate."""
		self._instance.RemoveMisalignment = value

	@property
	def set_concentric_alignment_type(self):
		"""Sets the alignment type of this mate."""
		return self._instance.SetConcentricAlignmentType

	@set_concentric_alignment_type.setter
	def set_concentric_alignment_type(self, value):
		"""Sets the alignment type of this mate."""
		self._instance.SetConcentricAlignmentType = value

	@property
	def set_force(self):
		"""Sets the magnitude and direction of the force to apply to this mate."""
		return self._instance.SetForce

	@set_force.setter
	def set_force(self, value):
		"""Sets the magnitude and direction of the force to apply to this mate."""
		self._instance.SetForce = value

	@property
	def set_maximum_misaligned_deviation(self):
		"""Sets the maximum allowed misalignment deviation for this misaligned concentric mate."""
		return self._instance.SetMaximumMisalignedDeviation

	@set_maximum_misaligned_deviation.setter
	def set_maximum_misaligned_deviation(self, value):
		"""Sets the maximum allowed misalignment deviation for this misaligned concentric mate."""
		self._instance.SetMaximumMisalignedDeviation = value

	@property
	def set_torque(self):
		"""Sets the angle and the axis of the torque to apply to this mate."""
		return self._instance.SetTorque

	@set_torque.setter
	def set_torque(self, value):
		"""Sets the angle and the axis of the torque to apply to this mate."""
		self._instance.SetTorque = value

	@property
	def set_use_misaligned_deviation_document_property(self):
		"""Sets whether to use the document property value for the maximum misalignment deviation for the misaligned concentric mate."""
		return self._instance.SetUseMisalignedDeviationDocumentProperty

	@set_use_misaligned_deviation_document_property.setter
	def set_use_misaligned_deviation_document_property(self, value):
		"""Sets whether to use the document property value for the maximum misalignment deviation for the misaligned concentric mate."""
		self._instance.SetUseMisalignedDeviationDocumentProperty = value

