# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.html
class IProjectionCurveFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def bidirectional(self):
		"""Gets or sets whether the sketch is projected bidirectionally."""
		return self._instance.Bidirectional

	@bidirectional.setter
	def bidirectional(self, value):
		"""Gets or sets whether the sketch is projected bidirectionally."""
		self._instance.Bidirectional = value

	@property
	def face_array(self):
		"""Gets or sets the target faces for this projected curve."""
		return self._instance.FaceArray

	@face_array.setter
	def face_array(self, value):
		"""Gets or sets the target faces for this projected curve."""
		self._instance.FaceArray = value

	@property
	def reverse(self):
		"""Reverses the direction that the curve is projected."""
		return self._instance.Reverse

	@reverse.setter
	def reverse(self, value):
		"""Reverses the direction that the curve is projected."""
		self._instance.Reverse = value

	@property
	def sketch(self):
		"""Gets or sets the sketch to project in this projection curve feature."""
		return self._instance.Sketch

	@sketch.setter
	def sketch(self, value):
		"""Gets or sets the sketch to project in this projection curve feature."""
		self._instance.Sketch = value

	@property
	def access_selections(self):
		"""Gains access to the selections used to define the projected curve."""
		return self._instance.AccessSelections

	@access_selections.setter
	def access_selections(self, value):
		"""Gains access to the selections used to define the projected curve."""
		self._instance.AccessSelections = value

	@property
	def get_face_array_count(self):
		"""Gets the number of target faces for this projected curve."""
		return self._instance.GetFaceArrayCount

	@get_face_array_count.setter
	def get_face_array_count(self, value):
		"""Gets the number of target faces for this projected curve."""
		self._instance.GetFaceArrayCount = value

	@property
	def i_access_selections(self):
		"""Gains access to the selections used to define the projected curve."""
		return self._instance.IAccessSelections2

	@i_access_selections.setter
	def i_access_selections(self, value):
		"""Gains access to the selections used to define the projected curve."""
		self._instance.IAccessSelections2 = value

	@property
	def i_get_face_array(self):
		"""Gets a list of target faces for the projected curve."""
		return self._instance.IGetFaceArray

	@i_get_face_array.setter
	def i_get_face_array(self, value):
		"""Gets a list of target faces for the projected curve."""
		self._instance.IGetFaceArray = value

	@property
	def i_set_face_array(self):
		"""Sets the target faces for the projected curve."""
		return self._instance.ISetFaceArray

	@i_set_face_array.setter
	def i_set_face_array(self, value):
		"""Sets the target faces for the projected curve."""
		self._instance.ISetFaceArray = value

	@property
	def release_selection_access(self):
		"""Releases access to the selections that created this projected curve."""
		return self._instance.ReleaseSelectionAccess

	@release_selection_access.setter
	def release_selection_access(self, value):
		"""Releases access to the selections that created this projected curve."""
		self._instance.ReleaseSelectionAccess = value

