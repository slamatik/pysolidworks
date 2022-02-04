# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.html
class ISlicingData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def add_slicing_planes_and_sketches_to_folder(self):
		"""Gets or sets whether to add slicing planes and sketches to a folder in the FeatureManager design tree."""
		return self._instance.AddSlicingPlanesAndSketchesToFolder

	@add_slicing_planes_and_sketches_to_folder.setter
	def add_slicing_planes_and_sketches_to_folder(self, value):
		"""Gets or sets whether to add slicing planes and sketches to a folder in the FeatureManager design tree."""
		self._instance.AddSlicingPlanesAndSketchesToFolder = value

	@property
	def number_of_planes(self):
		"""Gets or sets the number of slicing planes."""
		return self._instance.NumberOfPlanes

	@number_of_planes.setter
	def number_of_planes(self, value):
		"""Gets or sets the number of slicing planes."""
		self._instance.NumberOfPlanes = value

	@property
	def offset(self):
		"""Gets or sets the linear or radial spacing between slicing planes."""
		return self._instance.Offset

	@offset.setter
	def offset(self, value):
		"""Gets or sets the linear or radial spacing between slicing planes."""
		self._instance.Offset = value

	@property
	def plane_references(self):
		"""Sets the reference entities of the first slicing plane."""
		return self._instance.PlaneReferences

	@plane_references.setter
	def plane_references(self, value):
		"""Sets the reference entities of the first slicing plane."""
		self._instance.PlaneReferences = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to reverse the direction of slicing the model with respect to the initial reference plane."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to reverse the direction of slicing the model with respect to the initial reference plane."""
		self._instance.ReverseDirection = value

	@property
	def slices_to_generate(self):
		"""Gets or sets the slicing method."""
		return self._instance.SlicesToGenerate

	@slices_to_generate.setter
	def slices_to_generate(self, value):
		"""Gets or sets the slicing method."""
		self._instance.SlicesToGenerate = value

	@property
	def get_bounding_box_direction(self):
		"""Gets bounding box direction 1 (top manipulator for both linear and radial slicing)."""
		return self._instance.GetBoundingBoxDirection1

	@get_bounding_box_direction.setter
	def get_bounding_box_direction(self, value):
		"""Gets bounding box direction 1 (top manipulator for both linear and radial slicing)."""
		self._instance.GetBoundingBoxDirection1 = value

	@property
	def get_bounding_box_direction(self):
		"""Gets bounding box direction 2 (right manipulator for linear slicing, bottom manipulator for radial slicing)."""
		return self._instance.GetBoundingBoxDirection2

	@get_bounding_box_direction.setter
	def get_bounding_box_direction(self, value):
		"""Gets bounding box direction 2 (right manipulator for linear slicing, bottom manipulator for radial slicing)."""
		self._instance.GetBoundingBoxDirection2 = value

	@property
	def get_bounding_box_direction(self):
		"""Gets bounding box direction 3 (left manipulator for linear slicing, inner radius for radial slicing)."""
		return self._instance.GetBoundingBoxDirection3

	@get_bounding_box_direction.setter
	def get_bounding_box_direction(self, value):
		"""Gets bounding box direction 3 (left manipulator for linear slicing, inner radius for radial slicing)."""
		self._instance.GetBoundingBoxDirection3 = value

	@property
	def get_bounding_box_direction(self):
		"""Gets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing)."""
		return self._instance.GetBoundingBoxDirection4

	@get_bounding_box_direction.setter
	def get_bounding_box_direction(self, value):
		"""Gets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing)."""
		self._instance.GetBoundingBoxDirection4 = value

	@property
	def set_bounding_box_direction(self):
		"""Sets bounding box direction 1 (top manipulator for both linear and radial slicing)."""
		return self._instance.SetBoundingBoxDirection1

	@set_bounding_box_direction.setter
	def set_bounding_box_direction(self, value):
		"""Sets bounding box direction 1 (top manipulator for both linear and radial slicing)."""
		self._instance.SetBoundingBoxDirection1 = value

	@property
	def set_bounding_box_direction(self):
		"""Sets bounding box direction 2 (right manipulator for linear slicing, bottom manipulator for radial slicing)."""
		return self._instance.SetBoundingBoxDirection2

	@set_bounding_box_direction.setter
	def set_bounding_box_direction(self, value):
		"""Sets bounding box direction 2 (right manipulator for linear slicing, bottom manipulator for radial slicing)."""
		self._instance.SetBoundingBoxDirection2 = value

	@property
	def set_bounding_box_direction(self):
		"""Sets bounding box direction 3 (left manipulator for linear slicing, inner radius for radial slicing)."""
		return self._instance.SetBoundingBoxDirection3

	@set_bounding_box_direction.setter
	def set_bounding_box_direction(self, value):
		"""Sets bounding box direction 3 (left manipulator for linear slicing, inner radius for radial slicing)."""
		self._instance.SetBoundingBoxDirection3 = value

	@property
	def set_bounding_box_direction(self):
		"""Sets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing)."""
		return self._instance.SetBoundingBoxDirection4

	@set_bounding_box_direction.setter
	def set_bounding_box_direction(self, value):
		"""Sets bounding box direction 4 (bottom manipulator for linear slicing, outer radius for radial slicing)."""
		self._instance.SetBoundingBoxDirection4 = value

