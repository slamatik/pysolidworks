# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.html
class IMateLoadReference:
	def __init__(self, parent=None):
		self._instance = parent

	def component(self, which_one):
		"""
		Gets the specified component associated with the mate that owns this load reference.
		:param which_one: 
0 = Component1

1 = Component2
		"""
		# return self._instance.Component(which_one)
		raise NotImplemented

	def mate(self):
		"""Gets the mate that owns this mate load reference."""
		# return self._instance.Mate
		raise NotImplemented

	def name(self):
		"""Gets the name of this mate load reference."""
		# return self._instance.Name
		raise NotImplemented

	def delete(self):
		"""Deletes this mate load reference."""
		# return self._instance.Delete
		raise NotImplemented

	def get_faces(self, which_one):
		"""
		Gets the supplemental faces of the mate associated with the specified component.
		:param which_one: 
0 = Component1 

1 = Component2 
		"""
		# return self._instance.GetFaces(which_one)
		raise NotImplemented

	def get_faces_count(self, which_one):
		"""
		Gets the number of supplemental faces of the mate associated with the specified component.
		:param which_one: 
0 = Component1 
1 = Component2
		"""
		# return self._instance.GetFacesCount(which_one)
		raise NotImplemented

	def i_get_faces(self, which_one, face_count):
		"""
		Gets the supplemental faces of the mate associated with the specified component.
		:param which_one: 
0 = Component1 
1 = Component2 
		:param face_count: Number of supplemental faces
		"""
		# return self._instance.IGetFaces(which_one, face_count)
		raise NotImplemented

