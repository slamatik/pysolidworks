# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html
class ICenterMark:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def center_line_font(self):
		"""Gets or sets whether the centerline font is used for the lines in this center mark."""
		return self._instance.CenterLineFont

	@center_line_font.setter
	def center_line_font(self, value):
		"""Gets or sets whether the centerline font is used for the lines in this center mark."""
		self._instance.CenterLineFont = value

	@property
	def connection_lines(self):
		"""Gets or sets the visibility of the connection line of this center mark."""
		return self._instance.ConnectionLines

	@connection_lines.setter
	def connection_lines(self, value):
		"""Gets or sets the visibility of the connection line of this center mark."""
		self._instance.ConnectionLines = value

	@property
	def gap(self):
		"""Gets or sets the gap between this center mark and extension line."""
		return self._instance.Gap

	@gap.setter
	def gap(self, value):
		"""Gets or sets the gap between this center mark and extension line."""
		self._instance.Gap = value

	@property
	def group_count(self):
		"""Gets the number of center marks in a center mark set."""
		return self._instance.GroupCount

	@group_count.setter
	def group_count(self, value):
		"""Gets the number of center marks in a center mark set."""
		self._instance.GroupCount = value

	@property
	def is_grouped(self):
		"""Gets whether a center mark is in a center mark set."""
		return self._instance.IsGrouped

	@is_grouped.setter
	def is_grouped(self, value):
		"""Gets whether a center mark is in a center mark set."""
		self._instance.IsGrouped = value

	@property
	def rotation_angle(self):
		"""Gets or sets the angle for this center mark."""
		return self._instance.RotationAngle

	@rotation_angle.setter
	def rotation_angle(self, value):
		"""Gets or sets the angle for this center mark."""
		self._instance.RotationAngle = value

	@property
	def show_lines(self):
		"""Gets or sets whether the extension lines are shown in this center mark."""
		return self._instance.ShowLines

	@show_lines.setter
	def show_lines(self, value):
		"""Gets or sets whether the extension lines are shown in this center mark."""
		self._instance.ShowLines = value

	@property
	def size(self):
		"""Gets or sets the length of the lines in this center mark."""
		return self._instance.Size

	@size.setter
	def size(self, value):
		"""Gets or sets the length of the lines in this center mark."""
		self._instance.Size = value

	@property
	def style(self):
		"""Gets the style of this center mark."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets the style of this center mark."""
		self._instance.Style = value

	@property
	def use_doc_display_settings(self):
		"""Gets or sets whether to use the document defaults for this center mark's display settings."""
		return self._instance.UseDocDisplaySettings

	@use_doc_display_settings.setter
	def use_doc_display_settings(self, value):
		"""Gets or sets whether to use the document defaults for this center mark's display settings."""
		self._instance.UseDocDisplaySettings = value

	@property
	def add_to_center_mark_group(self):
		"""Adds a center mark for the selected entity in an existing center mark set."""
		return self._instance.AddToCenterMarkGroup

	@add_to_center_mark_group.setter
	def add_to_center_mark_group(self, value):
		"""Adds a center mark for the selected entity in an existing center mark set."""
		self._instance.AddToCenterMarkGroup = value

	@property
	def get_annotation(self):
		"""Gets the annotation for this center mark."""
		return self._instance.GetAnnotation

	@get_annotation.setter
	def get_annotation(self, value):
		"""Gets the annotation for this center mark."""
		self._instance.GetAnnotation = value

	@property
	def get_extended_length(self):
		"""Gets the extended length of the specified arm (handle) of this center mark."""
		return self._instance.GetExtendedLength

	@get_extended_length.setter
	def get_extended_length(self, value):
		"""Gets the extended length of the specified arm (handle) of this center mark."""
		self._instance.GetExtendedLength = value

	@property
	def get_next(self):
		"""Gets the next center mark."""
		return self._instance.GetNext

	@get_next.setter
	def get_next(self, value):
		"""Gets the next center mark."""
		self._instance.GetNext = value

	@property
	def get_position(self):
		"""Gets the x, y, and z coordinates for the specified center mark."""
		return self._instance.GetPosition

	@get_position.setter
	def get_position(self, value):
		"""Gets the x, y, and z coordinates for the specified center mark."""
		self._instance.GetPosition = value

	@property
	def has_detach_center_mark(self):
		"""Gets whether the selected center mark set contains any detached center marks."""
		return self._instance.HasDetachCenterMark

	@has_detach_center_mark.setter
	def has_detach_center_mark(self, value):
		"""Gets whether the selected center mark set contains any detached center marks."""
		self._instance.HasDetachCenterMark = value

	@property
	def is_deleted(self):
		"""Gets whether the specified center mark is deleted in this center mark set."""
		return self._instance.IsDeleted

	@is_deleted.setter
	def is_deleted(self, value):
		"""Gets whether the specified center mark is deleted in this center mark set."""
		self._instance.IsDeleted = value

	@property
	def is_detached(self):
		"""Gets whether the specified center mark is detached."""
		return self._instance.IsDetached

	@is_detached.setter
	def is_detached(self, value):
		"""Gets whether the specified center mark is detached."""
		self._instance.IsDetached = value

	@property
	def reattach_to_center_mark_group(self):
		"""Reattaches the specified center mark to the selected entity in a center mark set."""
		return self._instance.ReattachToCenterMarkGroup

	@reattach_to_center_mark_group.setter
	def reattach_to_center_mark_group(self, value):
		"""Reattaches the specified center mark to the selected entity in a center mark set."""
		self._instance.ReattachToCenterMarkGroup = value

	@property
	def select(self):
		"""Selects the center mark."""
		return self._instance.Select

	@select.setter
	def select(self, value):
		"""Selects the center mark."""
		self._instance.Select = value

	@property
	def set_extended_length(self):
		"""Sets the extended length of this center mark."""
		return self._instance.SetExtendedLength

	@set_extended_length.setter
	def set_extended_length(self, value):
		"""Sets the extended length of this center mark."""
		self._instance.SetExtendedLength = value

