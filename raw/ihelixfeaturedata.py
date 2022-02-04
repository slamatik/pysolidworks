# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData_members.html
class IHelixFeatureData:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def clockwise(self):
		"""Gets or sets the direction of the turns of this helix feature."""
		return self._instance.Clockwise

	@clockwise.setter
	def clockwise(self, value):
		"""Gets or sets the direction of the turns of this helix feature."""
		self._instance.Clockwise = value

	@property
	def defined_by(self):
		"""Gets or sets the definition of this helix feature."""
		return self._instance.DefinedBy

	@defined_by.setter
	def defined_by(self, value):
		"""Gets or sets the definition of this helix feature."""
		self._instance.DefinedBy = value

	@property
	def height(self):
		"""Gets or sets the height of this helix feature."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of this helix feature."""
		self._instance.Height = value

	@property
	def pitch(self):
		"""Gets or sets the pitch of this helix feature."""
		return self._instance.Pitch

	@pitch.setter
	def pitch(self, value):
		"""Gets or sets the pitch of this helix feature."""
		self._instance.Pitch = value

	@property
	def pitch_count(self):
		"""Gets the number of regions in this variable-pitch helix."""
		return self._instance.PitchCount

	@pitch_count.setter
	def pitch_count(self, value):
		"""Gets the number of regions in this variable-pitch helix."""
		self._instance.PitchCount = value

	@property
	def reverse_direction(self):
		"""Gets or sets whether to make this helix feature extend backward from the point of origin."""
		return self._instance.ReverseDirection

	@reverse_direction.setter
	def reverse_direction(self, value):
		"""Gets or sets whether to make this helix feature extend backward from the point of origin."""
		self._instance.ReverseDirection = value

	@property
	def revolution(self):
		"""Gets or sets the number of revolutions for this helix feature."""
		return self._instance.Revolution

	@revolution.setter
	def revolution(self, value):
		"""Gets or sets the number of revolutions for this helix feature."""
		self._instance.Revolution = value

	@property
	def starting_angle(self):
		"""Gets or sets the angle for the first turn of this helix feature."""
		return self._instance.StartingAngle

	@starting_angle.setter
	def starting_angle(self, value):
		"""Gets or sets the angle for the first turn of this helix feature."""
		self._instance.StartingAngle = value

	@property
	def taper(self):
		"""Gets or sets whether this constant-pitch helix feature is tapered."""
		return self._instance.Taper

	@taper.setter
	def taper(self, value):
		"""Gets or sets whether this constant-pitch helix feature is tapered."""
		self._instance.Taper = value

	@property
	def taper_angle(self):
		"""Gets or sets the angle of the taper for this constant-pitch helix feature."""
		return self._instance.TaperAngle

	@taper_angle.setter
	def taper_angle(self, value):
		"""Gets or sets the angle of the taper for this constant-pitch helix feature."""
		self._instance.TaperAngle = value

	@property
	def taper_outward(self):
		"""Gets or sets the direction of the taper for this constant-pitch helix feature."""
		return self._instance.TaperOutward

	@taper_outward.setter
	def taper_outward(self, value):
		"""Gets or sets the direction of the taper for this constant-pitch helix feature."""
		self._instance.TaperOutward = value

	@property
	def variable_pitch(self):
		"""Gets whether this helix feature has a variable or constant pitch."""
		return self._instance.VariablePitch

	@variable_pitch.setter
	def variable_pitch(self, value):
		"""Gets whether this helix feature has a variable or constant pitch."""
		self._instance.VariablePitch = value

	@property
	def add_last_record(self):
		"""Adds a region to the end of the Region parameters table of this variable-pitch helix."""
		return self._instance.AddLastRecord

	@add_last_record.setter
	def add_last_record(self, value):
		"""Adds a region to the end of the Region parameters table of this variable-pitch helix."""
		self._instance.AddLastRecord = value

	@property
	def delete_record(self):
		"""Deletes the specified records in the Region parameters table of this variable-pitch helix."""
		return self._instance.DeleteRecord

	@delete_record.setter
	def delete_record(self, value):
		"""Deletes the specified records in the Region parameters table of this variable-pitch helix."""
		self._instance.DeleteRecord = value

	@property
	def get_region_parameter_at_index(self):
		"""Gets the specified parameter value for the specified region in this variable-pitch helix."""
		return self._instance.GetRegionParameterAtIndex

	@get_region_parameter_at_index.setter
	def get_region_parameter_at_index(self, value):
		"""Gets the specified parameter value for the specified region in this variable-pitch helix."""
		self._instance.GetRegionParameterAtIndex = value

	@property
	def insert_record(self):
		"""Inserts a record before the specified index in the Region parameters table of this variable-pitch helix."""
		return self._instance.InsertRecord

	@insert_record.setter
	def insert_record(self, value):
		"""Inserts a record before the specified index in the Region parameters table of this variable-pitch helix."""
		self._instance.InsertRecord = value

	@property
	def set_region_parameter_at_index(self):
		"""Sets the specified parameter for the specified region in this variable-pitch helix."""
		return self._instance.SetRegionParameterAtIndex

	@set_region_parameter_at_index.setter
	def set_region_parameter_at_index(self, value):
		"""Sets the specified parameter for the specified region in this variable-pitch helix."""
		self._instance.SetRegionParameterAtIndex = value

