# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html
class IMidSurface3:
	def __init__(self, parent=None):
		self._instance = parent

	def edge_get_face(self, edge_in_disp):
		"""
		Gets the body face on which the specified midsurface edge lies.
		:param edge_in_disp: Midsurface edge
		"""
		# return self._instance.EdgeGetFace(edge_in_disp)
		raise NotImplemented

	def get_face_count(self):
		"""Gets the number of faces in the midsurface feature."""
		# return self._instance.GetFaceCount
		raise NotImplemented

	def get_face_pair_count(self):
		"""Gets the number of parallel pairs of faces found in the original part body that were used to calculate the midsurface feature."""
		# return self._instance.GetFacePairCount
		raise NotImplemented

	def get_faces(self):
		"""Gets the faces in this midsurface feature."""
		# return self._instance.GetFaces
		raise NotImplemented

	def get_first_face(self, from_face1_disp, from_face2_disp, thickness):
		"""
		Gets the first face in this midsurface feature and three other items.
		:param from_face1_disp: Face on the original part body used in generating the neutral face
		:param from_face2_disp: Parallel face to FromFace1Disp on the original part body used in generating the neutral face
		:param thickness: Distance between the two parallel faces, FromFace1Disp and FromFace2Disp
		"""
		# return self._instance.GetFirstFace(from_face1_disp, from_face2_disp, thickness)
		raise NotImplemented

	def get_first_face_array(self, thickness):
		"""
		Gets the first face and the thickness between the faces.
		:param thickness: Thickness between the faces
		"""
		# return self._instance.GetFirstFaceArray(thickness)
		raise NotImplemented

	def get_first_face_pair(self, thickness, partner_face_disp):
		"""
		Gets the first pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.
		:param thickness: Distance between these two parallel faces
		:param partner_face_disp: Face on the original part body used in generating the neutral face
		"""
		# return self._instance.GetFirstFacePair(thickness, partner_face_disp)
		raise NotImplemented

	def get_first_neutral_sheet(self):
		"""Gets the first reference surface in this midsurface feature."""
		# return self._instance.GetFirstNeutralSheet
		raise NotImplemented

	def get_neutral_sheet_count(self):
		"""Gets the total number of reference surfaces found in this midsurface feature."""
		# return self._instance.GetNeutralSheetCount
		raise NotImplemented

	def get_next_face(self, from_face1_disp, from_face2_disp, thickness):
		"""
		Gets the next neutral face in this midsurface feature.
		:param from_face1_disp: Face on the original part body used in generating the neutral face
		:param from_face2_disp: Face on the original part body used in generating the neutral face
		:param thickness: Distance between the two parallel faces, FromFace1Disp and FromFace2Disp
		"""
		# return self._instance.GetNextFace(from_face1_disp, from_face2_disp, thickness)
		raise NotImplemented

	def get_next_face_array(self, thickness):
		"""
		Gets the next face from the original paired faces and the thickness between the faces.
		:param thickness: Thickness between the faces 

		"""
		# return self._instance.GetNextFaceArray(thickness)
		raise NotImplemented

	def get_next_face_pair(self, thickness, partner_face_disp):
		"""
		Gets the next pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.
		:param thickness: Distance between theses two parallel faces
		:param partner_face_disp: Face on the original part body used in generating the neutral face
		"""
		# return self._instance.GetNextFacePair(thickness, partner_face_disp)
		raise NotImplemented

	def get_next_neutral_sheet(self):
		"""Gets the next reference surface in this midsurface feature."""
		# return self._instance.GetNextNeutralSheet
		raise NotImplemented

	def i_edge_get_face(self, edge_in_disp):
		"""
		Gets the body face on which the specified midsurface edge lies.
		:param edge_in_disp: Midsurface edge
		"""
		# return self._instance.IEdgeGetFace(edge_in_disp)
		raise NotImplemented

	def i_get_faces(self, num_faces):
		"""
		Gets the faces in this midsurface feature.
		:param num_faces: Number of faces
		"""
		# return self._instance.IGetFaces(num_faces)
		raise NotImplemented

	def i_get_first_face(self, from_face1_disp, from_face2_disp, thickness):
		"""
		Gets the next neutral face in this midsurface feature.
		:param from_face1_disp: Face on the original part body used in generating the neutral face
		:param from_face2_disp: Parallel face to FromFace1Disp on the original part body used in generating the neutral face
		:param thickness: Distance between the two parallel faces, FromFace1Disp and FromFace2Disp
		"""
		# return self._instance.IGetFirstFace(from_face1_disp, from_face2_disp, thickness)
		raise NotImplemented

	def i_get_first_face_array(self, from_front_face_list_disp, size_of_front_face_list, from_face_back_list_disp, size_of_back_face_list, thickness):
		"""
		Gets the first face and the thickness between the faces.
		:param from_front_face_list_disp: 
in-process, unmanaged C++: Pointer to an array of front faces

VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		:param size_of_front_face_list: 
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		:param from_face_back_list_disp: Number of front faces
		:param size_of_back_face_list: 
in-process, unmanaged C++: Pointer to an array of back faces
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		:param thickness: Number of back faces
		"""
		# return self._instance.IGetFirstFaceArray(from_front_face_list_disp, size_of_front_face_list, from_face_back_list_disp, size_of_back_face_list, thickness)
		raise NotImplemented

	def i_get_first_face_pair(self, thickness, partner_face_disp):
		"""
		Gets the first pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.
		:param thickness: Distance between these two parallel faces
		:param partner_face_disp: Face on the original part body used in generating the neutral face
		"""
		# return self._instance.IGetFirstFacePair(thickness, partner_face_disp)
		raise NotImplemented

	def i_get_first_neutral_sheet(self):
		"""Gets the first reference surface in this midsurface feature."""
		# return self._instance.IGetFirstNeutralSheet
		raise NotImplemented

	def i_get_next_face(self, from_face1_disp, from_face2_disp, thickness):
		"""
		Gets the next neutral face in this midsurface feature.
		:param from_face1_disp: Face on the original part body used in generating the neutral face
		:param from_face2_disp: Face on the original part body used in generating the neutral face
		:param thickness: Distance between the two parallel faces, FromFace1Disp and FromFace2Disp
		"""
		# return self._instance.IGetNextFace(from_face1_disp, from_face2_disp, thickness)
		raise NotImplemented

	def i_get_next_face_array(self, from_front_face_list_disp, size_of_front_face_list, from_face_back_list_disp, size_of_back_face_list, thickness):
		"""
		Gets the next face from the original paired faces and the thickness between the faces.
		:param from_front_face_list_disp: 
in-process,unmanaged C++: Pointer to an array of front faces
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method. 
		:param size_of_front_face_list: Number of front faces
		:param from_face_back_list_disp: 
in-process, unmanaged C++: Pointer to an array of back faces
VBA, VB.NET, C#, and C++/CLI: Not supported 
See In-process Methods for details about this type of method.
		:param size_of_back_face_list: Number of back faces
		:param thickness: Thickness between the faces
		"""
		# return self._instance.IGetNextFaceArray(from_front_face_list_disp, size_of_front_face_list, from_face_back_list_disp, size_of_back_face_list, thickness)
		raise NotImplemented

	def i_get_next_face_pair(self, thickness, partner_face_disp):
		"""
		Gets the next pair of parallel faces in this midsurface feature and the thickness (in meters) between the two faces.
		:param thickness: Distance between theses two parallel faces
		:param partner_face_disp: Face on the original part body used in generating the neutral face
		"""
		# return self._instance.IGetNextFacePair(thickness, partner_face_disp)
		raise NotImplemented

	def i_get_next_neutral_sheet(self):
		"""Gets the next reference surface in this midsurface feature."""
		# return self._instance.IGetNextNeutralSheet
		raise NotImplemented

