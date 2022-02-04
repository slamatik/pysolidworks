# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html
class IWeldmentBeadFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bead_length(self):
		"""Gets or sets the length of each bead segment of the weld bead."""
		return self._instance.BeadLength

	@bead_length.setter
	def bead_length(self, value):
		"""Gets or sets the length of each bead segment of the weld bead."""
		self._instance.BeadLength = value

	@property
	def bead_pitch(self):
		"""Gets or sets the distance between the start of each weld bead."""
		return self._instance.BeadPitch

	@bead_pitch.setter
	def bead_pitch(self, value):
		"""Gets or sets the distance between the start of each weld bead."""
		self._instance.BeadPitch = value

	@property
	def bead_size(self):
		"""Gets or sets the length of the leg of the weld bead."""
		return self._instance.BeadSize

	@bead_size.setter
	def bead_size(self, value):
		"""Gets or sets the length of the leg of the weld bead."""
		self._instance.BeadSize = value

	@property
	def bead_type(self):
		"""Gets or sets the type of weld bead."""
		return self._instance.BeadType

	@bead_type.setter
	def bead_type(self, value):
		"""Gets or sets the type of weld bead."""
		self._instance.BeadType = value

	@property
	def tangent_propagation(self):
		"""Gets or sets whether to propagate the weld bead along the tangent."""
		return self._instance.TangentPropagation

	@tangent_propagation.setter
	def tangent_propagation(self, value):
		"""Gets or sets whether to propagate the weld bead along the tangent."""
		self._instance.TangentPropagation = value

	@property
	def use_other_side(self):
		"""Gets or sets whether to apply the weld bead to both sides of the intersecting faces."""
		return self._instance.UseOtherSide

	@use_other_side.setter
	def use_other_side(self, value):
		"""Gets or sets whether to apply the weld bead to both sides of the intersecting faces."""
		self._instance.UseOtherSide = value

	@property
	def access_selections(self):
		"""Gains access to the selections that define this weld bead."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections that define this weld bead."""
		self._instance.AccessSelections = value

	@property
	def get_faces(self):
		"""Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied."""
		return self._instance.GetFaces

	@get_faces.setter
	def get_faces(self, value):
		"""Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied."""
		self._instance.GetFaces = value

	@property
	def get_faces_count(self):
		"""Gets the number of faces in each sets of faces whose intersection defines the edges to which this weld bead is applied."""
		return self._instance.GetFacesCount

	@get_faces_count.setter
	def get_faces_count(self, value):
		"""Gets the number of faces in each sets of faces whose intersection defines the edges to which this weld bead is applied."""
		self._instance.GetFacesCount = value

	@property
	def get_virtual_edges(self):
		"""Gets the edges to which the weld bead is applied."""
		return self._instance.GetVirtualEdges

	@get_virtual_edges.setter
	def get_virtual_edges(self, value):
		"""Gets the edges to which the weld bead is applied."""
		self._instance.GetVirtualEdges = value

	@property
	def get_virtual_edges_count(self):
		"""Gets the number of edges to which the weld bead is applied."""
		return self._instance.GetVirtualEdgesCount

	@get_virtual_edges_count.setter
	def get_virtual_edges_count(self, value):
		"""Gets the number of edges to which the weld bead is applied."""
		self._instance.GetVirtualEdgesCount = value

	@property
	def i_get_faces(self):
		"""Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied."""
		return self._instance.IGetFaces

	@i_get_faces.setter
	def i_get_faces(self, value):
		"""Gets the sets of faces whose edges intersection defines the edges to which the weld bead is applied."""
		self._instance.IGetFaces = value

	@property
	def i_get_virtual_edges(self):
		"""Gets the edges to which the weld bead is applied."""
		return self._instance.IGetVirtualEdges

	@i_get_virtual_edges.setter
	def i_get_virtual_edges(self, value):
		"""Gets the edges to which the weld bead is applied."""
		self._instance.IGetVirtualEdges = value

	@property
	def i_set_faces(self):
		"""Sets the faces to which to apply the weld bead."""
		return self._instance.ISetFaces

	@i_set_faces.setter
	def i_set_faces(self, value):
		"""Sets the faces to which to apply the weld bead."""
		self._instance.ISetFaces = value

	@property
	def i_set_virtual_edges(self):
		"""Sets the edges to which to apply this weld bead."""
		return self._instance.ISetVirtualEdges

	@i_set_virtual_edges.setter
	def i_set_virtual_edges(self, value):
		"""Sets the edges to which to apply this weld bead."""
		self._instance.ISetVirtualEdges = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that define this weld bead."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that define this weld bead."""
		self._instance.ReleaseSelectionAccess = value

	@property
	def set_faces(self):
		"""Sets the faces to which to apply the weld bead."""
		return self._instance.SetFaces

	@set_faces.setter
	def set_faces(self, value):
		"""Sets the faces to which to apply the weld bead."""
		self._instance.SetFaces = value

	@property
	def set_virtual_edges(self):
		"""Sets the edges to which to apply this weld bead."""
		return self._instance.SetVirtualEdges

	@set_virtual_edges.setter
	def set_virtual_edges(self, value):
		"""Sets the edges to which to apply this weld bead."""
		self._instance.SetVirtualEdges = value

