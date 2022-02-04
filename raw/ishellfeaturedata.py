# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IShellFeatureData_members.html
class IShellFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	def direction(self):
		"""Gets and sets the direction of this shell feature."""
		# return self._instance.Direction
		raise NotImplemented

	def faces_removed(self):
		"""Gets the faces removed and sets the faces to remove in this shell feature."""
		# return self._instance.FacesRemoved
		raise NotImplemented

	def faces_removed_count(self):
		"""Gets the number of faces removed in this shell feature."""
		# return self._instance.FacesRemovedCount
		raise NotImplemented

	def multiple_thickness_faces(self):
		"""Gets and sets the multiple-thickness faces in this shell feature."""
		# return self._instance.MultipleThicknessFaces
		raise NotImplemented

	def thickness(self):
		"""Gets and sets the overall thickness of the shell feature."""
		# return self._instance.Thickness
		raise NotImplemented

	def access_selections(self, top_doc, component):
		"""
		Gains access to the selections that define this shell feature.
		:param top_doc: Top-level document (see Remarks)
		:param component: Component in which the feature is to be modified (see Remarks)
		"""
		# return self._instance.AccessSelections(top_doc, component)
		raise NotImplemented

	def get_multiple_thickness_at_index(self, index):
		"""
		Gets the thickness of the shell at the specified index in this shell feature.
		:param index: 0-based index for the thickness
		"""
		# return self._instance.GetMultipleThicknessAtIndex(index)
		raise NotImplemented

	def get_multiple_thickness_faces_count(self):
		"""Gets the number of faces with multiple thickness in this shell feature."""
		# return self._instance.GetMultipleThicknessFacesCount
		raise NotImplemented

	def i_access_selections(self, top_doc, component):
		"""
		Gains access to the selections that define this shell feature.
		:param top_doc: Top-level document (see Remarks)
		:param component: Component in which the feature is to be modified (see Remarks)
		"""
		# return self._instance.IAccessSelections(top_doc, component)
		raise NotImplemented

	def i_get_faces_removed(self, count):
		"""
		Gets the faces removed in this shell feature.
		:param count: Number of removed faces
		"""
		# return self._instance.IGetFacesRemoved(count)
		raise NotImplemented

	def i_get_multiple_thickness_faces(self, count):
		"""
		Gets the multiple-thickness faces in this shell feature.
		:param count: Number of multiple-thickness faces
		"""
		# return self._instance.IGetMultipleThicknessFaces(count)
		raise NotImplemented

	def i_set_faces_removed(self, count, face_array):
		"""
		Sets the faces to remove in this shell feature.
		:param count: Number of faces
		:param face_array: 

in-process, unmanaged C++: Pointer to an array of faces to remove of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
		"""
		# return self._instance.ISetFacesRemoved(count, face_array)
		raise NotImplemented

	def i_set_multiple_thickness_faces(self, count, face_array):
		"""
		Sets the multiple-thickness faces in this shell feature.
		:param count: Number of faces
		:param face_array: 

in-process, unmanaged C++: Pointer to an array of faces to set to multiple thickness of size Count

VBA, VB.NET, C#, and C++/CLI: Not supported
See In-process Methods for details about this type of method.
		"""
		# return self._instance.ISetMultipleThicknessFaces(count, face_array)
		raise NotImplemented

	def release_selection_access(self):
		"""Releases access to the selections used to define this shell feature."""
		# return self._instance.ReleaseSelectionAccess
		raise NotImplemented

	def set_multiple_thickness_at_index(self, index, thickness):
		"""
		Sets the thickness of the shell at this index in this shell feature.
		:param index: 0-based index for new thickness
		:param thickness: New thickness
		"""
		# return self._instance.SetMultipleThicknessAtIndex(index, thickness)
		raise NotImplemented

