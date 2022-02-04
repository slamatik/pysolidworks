# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.html
class ISpring:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def base_profile(self):
		"""Gets or sets the base profile of the spring."""
		return self._instance.BaseProfile

	@base_profile.setter
	def base_profile(self, value):
		"""Gets or sets the base profile of the spring."""
		self._instance.BaseProfile = value

	@property
	def clockwise(self):
		"""Gets or sets the direction of the coils of the spring."""
		return self._instance.Clockwise

	@clockwise.setter
	def clockwise(self, value):
		"""Gets or sets the direction of the coils of the spring."""
		self._instance.Clockwise = value

	@property
	def define_type(self):
		"""Gets or sets how the number of revolutions, pitch, and height of the spring are defined."""
		return self._instance.DefineType

	@define_type.setter
	def define_type(self, value):
		"""Gets or sets how the number of revolutions, pitch, and height of the spring are defined."""
		self._instance.DefineType = value

	@property
	def ending_end_length(self):
		"""Gets or sets the ending end length of a torsion spring."""
		return self._instance.EndingEndLength

	@ending_end_length.setter
	def ending_end_length(self, value):
		"""Gets or sets the ending end length of a torsion spring."""
		self._instance.EndingEndLength = value

	@property
	def ending_end_type(self):
		"""Gets or sets the ending end type for either an extension spring or a torsion spring."""
		return self._instance.EndingEndType

	@ending_end_type.setter
	def ending_end_type(self, value):
		"""Gets or sets the ending end type for either an extension spring or a torsion spring."""
		self._instance.EndingEndType = value

	@property
	def ending_pitch(self):
		"""Gets or sets pitch of the end section of a compression spring."""
		return self._instance.EndingPitch

	@ending_pitch.setter
	def ending_pitch(self, value):
		"""Gets or sets pitch of the end section of a compression spring."""
		self._instance.EndingPitch = value

	@property
	def ending_revolution(self):
		"""Gets or sets the number of revolutions for the end section of a compression spring."""
		return self._instance.EndingRevolution

	@ending_revolution.setter
	def ending_revolution(self, value):
		"""Gets or sets the number of revolutions for the end section of a compression spring."""
		self._instance.EndingRevolution = value

	@property
	def ground_type(self):
		"""Gets or sets whether the ends of compression spring are ground to a flat surface or have the same pitch as the coil."""
		return self._instance.GroundType

	@ground_type.setter
	def ground_type(self, value):
		"""Gets or sets whether the ends of compression spring are ground to a flat surface or have the same pitch as the coil."""
		self._instance.GroundType = value

	@property
	def height(self):
		"""Gets or sets the height of the spring."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of the spring."""
		self._instance.Height = value

	@property
	def pitch(self):
		"""Gets or sets the pitch of the spring."""
		return self._instance.Pitch

	@pitch.setter
	def pitch(self, value):
		"""Gets or sets the pitch of the spring."""
		self._instance.Pitch = value

	@property
	def profile_parameters(self):
		"""Gets or sets the section profile parameters for the spring."""
		return self._instance.ProfileParameters

	@profile_parameters.setter
	def profile_parameters(self, value):
		"""Gets or sets the section profile parameters for the spring."""
		self._instance.ProfileParameters = value

	@property
	def profile_type(self):
		"""Gets or sets the section profile type of the spring."""
		return self._instance.ProfileType

	@profile_type.setter
	def profile_type(self, value):
		"""Gets or sets the section profile type of the spring."""
		self._instance.ProfileType = value

	@property
	def reverse_direction(self):
		"""Gets or sets the direction of a compression, extension, or torsion spring."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets the direction of a compression, extension, or torsion spring."""
		self._instance.ReverseDirection = value

	@property
	def revolution(self):
		"""Gets or sets the number of revolutions for the spring."""
		return self._instance.Revolution

	@revolution.setter
	def revolution(self, value):
		"""Gets or sets the number of revolutions for the spring."""
		self._instance.Revolution = value

	@property
	def section_profile(self):
		"""Gets or sets the section profile for the spring."""
		return self._instance.SectionProfile

	@section_profile.setter
	def section_profile(self, value):
		"""Gets or sets the section profile for the spring."""
		self._instance.SectionProfile = value

	@property
	def section_profile_center(self):
		"""Gets or sets the center point of the section profile of the spring."""
		return self._instance.SectionProfileCenter

	@section_profile_center.setter
	def section_profile_center(self, value):
		"""Gets or sets the center point of the section profile of the spring."""
		self._instance.SectionProfileCenter = value

	@property
	def spring_type(self):
		"""Gets or sets the type of parameters that define the spring."""
		return self._instance.SpringType

	@spring_type.setter
	def spring_type(self, value):
		"""Gets or sets the type of parameters that define the spring."""
		self._instance.SpringType = value

	@property
	def starting_end_length(self):
		"""Gets or sets the starting end length of a torsion spring."""
		return self._instance.StartingEndLength

	@starting_end_length.setter
	def starting_end_length(self, value):
		"""Gets or sets the starting end length of a torsion spring."""
		self._instance.StartingEndLength = value

	@property
	def starting_end_type(self):
		"""Gets or sets the starting end type for either an extension spring or a torsion spring."""
		return self._instance.StartingEndType

	@starting_end_type.setter
	def starting_end_type(self, value):
		"""Gets or sets the starting end type for either an extension spring or a torsion spring."""
		self._instance.StartingEndType = value

	@property
	def starting_pitch(self):
		"""Gets the pitch of the starting section of a compression spring."""
		return self._instance.StartingPitch

	@starting_pitch.setter
	def starting_pitch(self, value):
		"""Gets the pitch of the starting section of a compression spring."""
		self._instance.StartingPitch = value

	@property
	def starting_revolution(self):
		"""Gets or sets the number of revolutions for the starting section of a compression spring."""
		return self._instance.StartingRevolution

	@starting_revolution.setter
	def starting_revolution(self, value):
		"""Gets or sets the number of revolutions for the starting section of a compression spring."""
		self._instance.StartingRevolution = value

	@property
	def taper_angle(self):
		"""Gets or sets the angle by which to taper a compression spring."""
		return self._instance.TaperAngle

	@taper_angle.setter
	def taper_angle(self, value):
		"""Gets or sets the angle by which to taper a compression spring."""
		self._instance.TaperAngle = value

	@property
	def taper_outward(self):
		"""Gets or sets the direction by which to taper the helix of a compression spring."""
		return self._instance.TaperOutward

	@taper_outward.setter
	def taper_outward(self, value):
		"""Gets or sets the direction by which to taper the helix of a compression spring."""
		self._instance.TaperOutward = value

	@property
	def tolerance(self):
		"""Gets or sets the precision of the helical curve."""
		return self._instance.Tolerance

	@tolerance.setter
	def tolerance(self, value):
		"""Gets or sets the precision of the helical curve."""
		self._instance.Tolerance = value

	@property
	def get_profile_points(self):
		"""Gets the points for creating the profile sketch."""
		return self._instance.GetProfilePoints

	@get_profile_points.setter
	def get_profile_points(self, value):
		"""Gets the points for creating the profile sketch."""
		self._instance.GetProfilePoints = value

	@property
	def get_spring_body(self):
		"""Gets the spring body."""
		return self._instance.GetSpringBody

	@get_spring_body.setter
	def get_spring_body(self, value):
		"""Gets the spring body."""
		self._instance.GetSpringBody = value

