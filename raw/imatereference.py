# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.html
class IMateReference:
	def __init__(self, parent=None):
		self._instance = parent

	def name(self):
		"""Gets the name of the selected mate reference."""
		# return self._instance.Name
		raise NotImplemented

	def reference_alignment(self, index):
		"""
		Gets the mate reference alignment for the specified mate reference entity in the selected mate reference.
		:param index: Mate reference entity as defined by swMateReferenceIndex_e
		"""
		# return self._instance.ReferenceAlignment(index)
		raise NotImplemented

	def reference_entity(self, index):
		"""
		Gets the specified mate entity in this mate reference.
		:param index: Mate reference entity as defined in swMateReferenceIndex_e
		"""
		# return self._instance.ReferenceEntity2(index)
		raise NotImplemented

	def reference_entity_count(self):
		"""Gets the number of mate reference entities for the selected mate reference."""
		# return self._instance.ReferenceEntityCount
		raise NotImplemented

	def reference_entity_type(self, index):
		"""
		Gets the exact entity type returned by IMateReference::ReferenceEntity2.
		:param index: Mate reference entity as defined in swMateReferenceIndex_e
		"""
		# return self._instance.ReferenceEntityType(index)
		raise NotImplemented

	def reference_type(self, index):
		"""
		Gets the mate type for the specified entity in this mate reference.
		:param index: Mate reference entity as defined by swMateReferenceIndex_e
		"""
		# return self._instance.ReferenceType(index)
		raise NotImplemented

	def edit(self, bstr_mate_reference_name, primary_reference_entity, primary_reference_type, primary_reference_alignment, secondary_reference_entity, secondary_reference_type, secondary_reference_alignment, tertiary_reference_entity, tertiary_reference_type, tertiary_reference_alignment):
		"""
		Lets you edit the selected mate reference.
		:param bstr_mate_reference_name: Name of the new mate reference, which replaces the selected mate reference
		:param primary_reference_entity: Primary mate reference entity, a pointer to an IEntity object
		:param primary_reference_type: Type of mate as defined by swMateReferenceType_e for PrimaryReferenceEntity
		:param primary_reference_alignment: Type of alignment as defined by swMateReferenceAlignment_e for PrimaryReferenceEntity
		:param secondary_reference_entity: Secondary mate reference entity, a pointer to an IEntity object
		:param secondary_reference_type: Type of mate as defined by swMateReferenceType_e for SecondaryReferenceEntity
		:param secondary_reference_alignment: Type of alignment as defined by swMateReferenceAlignment_e for SecondaryReferenceEntity
		:param tertiary_reference_entity: Tertiary mate reference entity, a pointer to an IEntity object
		:param tertiary_reference_type: Type of mate as defined by swMateReferenceType_e for TertiaryReferenceEntity
		:param tertiary_reference_alignment: Type of alignment as defined by swMateReferenceAlignment_e for TertiaryReferenceEntity
		"""
		# return self._instance.Edit(bstr_mate_reference_name, primary_reference_entity, primary_reference_type, primary_reference_alignment, secondary_reference_entity, secondary_reference_type, secondary_reference_alignment, tertiary_reference_entity, tertiary_reference_type, tertiary_reference_alignment)
		raise NotImplemented

