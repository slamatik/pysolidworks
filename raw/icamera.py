# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICamera_members.html
class ICamera:
	def __init__(self, parent=None):
		self._instance = parent

	def aspect_ratio(self):
		"""Gets the aspect ratio (width/height) of the field of view rectangle for the camera.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.AspectRatio
		raise NotImplemented

	def depth_of_field_enabled(self):
		"""Gets whether depth of field effects are enabled or disabled.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DepthOfFieldEnabled
		raise NotImplemented

	def depth_of_field_offset(self):
		"""Gets the approximate distance from the camera's focal plane to point where focus is lost.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.DepthOfFieldOffset
		raise NotImplemented

	def field_of_view_angle(self):
		"""Gets the camera's horizontal angle of the field of view.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.FieldOfViewAngle
		raise NotImplemented

	def field_of_view_depth(self):
		"""Gets the camera's depth of the field of view.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.FieldOfViewDepth
		raise NotImplemented

	def field_of_view_height(self):
		"""Gets the camera's height of the field of view.
NOTE: This property is a get-only property. Set is not implemented."""
		# return self._instance.FieldOfViewHeight
		raise NotImplemented

	def i_d(self):
		"""Gets the ID for this camera."""
		# return self._instance.ID
		raise NotImplemented

	@property
	def lock_camera_position(self):
		"""Gets or sets whether the camera position is locked."""
		return self._instance.LockCameraPosition

	@lock_camera_position.setter
	def lock_camera_position(self, value):
		"""Gets or sets whether the camera position is locked."""
		self._instance.LockCameraPosition = value

	@property
	def perspective(self):
		"""Gets whether the camera is in perspective mode or not.
NOTE: This property is a get-only property. Set is not implemented."""
		return self._instance.Perspective

	@perspective.setter
	def perspective(self, value):
		"""Gets whether the camera is in perspective mode or not.
NOTE: This property is a get-only property. Set is not implemented."""
		self._instance.Perspective = value

	@property
	def pitch(self):
		"""Gets or sets the pitch (up or down angle) of a floating camera."""
		return self._instance.Pitch

	@pitch.setter
	def pitch(self, value):
		"""Gets or sets the pitch (up or down angle) of a floating camera."""
		self._instance.Pitch = value

	@property
	def position_type(self):
		"""Gets or sets the camera position type."""
		return self._instance.PositionType

	@position_type.setter
	def position_type(self, value):
		"""Gets or sets the camera position type."""
		self._instance.PositionType = value

	@property
	def rotation_roll_angle(self):
		"""Gets or sets the camera's roll angle."""
		return self._instance.RotationRollAngle

	@rotation_roll_angle.setter
	def rotation_roll_angle(self, value):
		"""Gets or sets the camera's roll angle."""
		self._instance.RotationRollAngle = value

	@property
	def rotation_roll_by_selection(self):
		"""Gets or sets whether you can select the camera's rotation roll direction."""
		return self._instance.RotationRollBySelection

	@rotation_roll_by_selection.setter
	def rotation_roll_by_selection(self, value):
		"""Gets or sets whether you can select the camera's rotation roll direction."""
		self._instance.RotationRollBySelection = value

	@property
	def rotation_roll_entity(self):
		"""Gets or sets the entity (line, edge, face, or plane) that defines the camera's rotation up direction."""
		return self._instance.RotationRollEntity

	@rotation_roll_entity.setter
	def rotation_roll_entity(self, value):
		"""Gets or sets the entity (line, edge, face, or plane) that defines the camera's rotation up direction."""
		self._instance.RotationRollEntity = value

	@property
	def rotation_roll_flip_direction(self):
		"""Gets or sets whether to flip the direction of the camera 180."""
		return self._instance.RotationRollFlipDirection

	@rotation_roll_flip_direction.setter
	def rotation_roll_flip_direction(self, value):
		"""Gets or sets whether to flip the direction of the camera 180."""
		self._instance.RotationRollFlipDirection = value

	@property
	def target_point_by_selection(self):
		"""Gets or sets whether you can set the target point."""
		return self._instance.TargetPointBySelection

	@target_point_by_selection.setter
	def target_point_by_selection(self, value):
		"""Gets or sets whether you can set the target point."""
		self._instance.TargetPointBySelection = value

	@property
	def target_point_position(self):
		"""Gets or sets the position of the target point."""
		return self._instance.TargetPointPosition

	@target_point_position.setter
	def target_point_position(self, value):
		"""Gets or sets the position of the target point."""
		self._instance.TargetPointPosition = value

	@property
	def type(self):
		"""Gets or sets the type of camera."""
		return self._instance.Type

	@type.setter
	def type(self, value):
		"""Gets or sets the type of camera."""
		self._instance.Type = value

	@property
	def yaw(self):
		"""Gets or sets the yaw (side-to-side angle) of a floating camera."""
		return self._instance.Yaw

	@yaw.setter
	def yaw(self, value):
		"""Gets or sets the yaw (side-to-side angle) of a floating camera."""
		self._instance.Yaw = value

	@property
	def get_focal_distance(self):
		"""Gets the camera's focal distance."""
		return self._instance.GetFocalDistance

	@get_focal_distance.setter
	def get_focal_distance(self, value):
		"""Gets the camera's focal distance."""
		self._instance.GetFocalDistance = value

	@property
	def get_point_of_interest_distance(self):
		"""Gets the distance of the point of interest from the camera."""
		return self._instance.GetPointOfInterestDistance

	@get_point_of_interest_distance.setter
	def get_point_of_interest_distance(self, value):
		"""Gets the distance of the point of interest from the camera."""
		self._instance.GetPointOfInterestDistance = value

	@property
	def get_position(self):
		"""Gets the current position of the camera."""
		return self._instance.GetPosition

	@get_position.setter
	def get_position(self, value):
		"""Gets the current position of the camera."""
		self._instance.GetPosition = value

	@property
	def get_position_cartesian(self):
		"""Gets the Cartesian coordinates for the camera position."""
		return self._instance.GetPositionCartesian

	@get_position_cartesian.setter
	def get_position_cartesian(self, value):
		"""Gets the Cartesian coordinates for the camera position."""
		self._instance.GetPositionCartesian = value

	@property
	def get_position_entity(self):
		"""Gets the entity to which the camera is attached."""
		return self._instance.GetPositionEntity

	@get_position_entity.setter
	def get_position_entity(self, value):
		"""Gets the entity to which the camera is attached."""
		self._instance.GetPositionEntity = value

	@property
	def get_position_spherical(self):
		"""Gets the spherical coordinates for the camera position relative to the target, based on a sphere around the Z axis with the zero (0) point at the target."""
		return self._instance.GetPositionSpherical

	@get_position_spherical.setter
	def get_position_spherical(self, value):
		"""Gets the spherical coordinates for the camera position relative to the target, based on a sphere around the Z axis with the zero (0) point at the target."""
		self._instance.GetPositionSpherical = value

	@property
	def get_target_point_entity(self):
		"""Gets the target point on the entity for the camera."""
		return self._instance.GetTargetPointEntity

	@get_target_point_entity.setter
	def get_target_point_entity(self, value):
		"""Gets the target point on the entity for the camera."""
		self._instance.GetTargetPointEntity = value

	@property
	def get_up_vector(self):
		"""Gets the camera's up direction."""
		return self._instance.GetUpVector

	@get_up_vector.setter
	def get_up_vector(self, value):
		"""Gets the camera's up direction."""
		self._instance.GetUpVector = value

	@property
	def get_view_vector(self):
		"""Gets the direction in which the camera is looking."""
		return self._instance.GetViewVector

	@get_view_vector.setter
	def get_view_vector(self, value):
		"""Gets the direction in which the camera is looking."""
		self._instance.GetViewVector = value

	@property
	def set_position_cartesian(self):
		"""Sets the Cartesian coordinates for the camera position."""
		return self._instance.SetPositionCartesian

	@set_position_cartesian.setter
	def set_position_cartesian(self, value):
		"""Sets the Cartesian coordinates for the camera position."""
		self._instance.SetPositionCartesian = value

	@property
	def set_position_entity(self):
		"""Sets the entity to which the camera is attached."""
		return self._instance.SetPositionEntity

	@set_position_entity.setter
	def set_position_entity(self, value):
		"""Sets the entity to which the camera is attached."""
		self._instance.SetPositionEntity = value

	@property
	def set_position_spherical(self):
		"""Sets the spherical coordinates for the camera position relative to the target, based on a sphere around the Z axis with the zero (0) point at the target."""
		return self._instance.SetPositionSpherical

	@set_position_spherical.setter
	def set_position_spherical(self, value):
		"""Sets the spherical coordinates for the camera position relative to the target, based on a sphere around the Z axis with the zero (0) point at the target."""
		self._instance.SetPositionSpherical = value

	@property
	def set_target_point_entity(self):
		"""Gets the target point on the entity for the camera."""
		return self._instance.SetTargetPointEntity

	@set_target_point_entity.setter
	def set_target_point_entity(self, value):
		"""Gets the target point on the entity for the camera."""
		self._instance.SetTargetPointEntity = value

