# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICallout_members.html
class ICallout:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def enable_push_pin(self):
		"""Gets or sets whether to enable the pushpin for this callout."""
		return self._instance.EnablePushPin

	@enable_push_pin.setter
	def enable_push_pin(self, value):
		"""Gets or sets whether to enable the pushpin for this callout."""
		self._instance.EnablePushPin = value

	@property
	def font_size(self):
		"""Gets or sets the font size for this callout."""
		return self._instance.FontSize

	@font_size.setter
	def font_size(self, value):
		"""Gets or sets the font size for this callout."""
		self._instance.FontSize = value

	@property
	def ignore_value(self):
		"""Gets or sets whether to ignore the callout value in the given row."""
		return self._instance.IgnoreValue

	@ignore_value.setter
	def ignore_value(self, value):
		"""Gets or sets whether to ignore the callout value in the given row."""
		self._instance.IgnoreValue = value

	@property
	def label(self):
		"""Gets or sets the text for the label in the specified row of this callout."""
		return self._instance.Label2

	@label.setter
	def label(self, value):
		"""Gets or sets the text for the label in the specified row of this callout."""
		self._instance.Label2 = value

	@property
	def multiple_leaders(self):
		"""Gets or sets the display of multiple leaders for this callout."""
		return self._instance.MultipleLeaders

	@multiple_leaders.setter
	def multiple_leaders(self, value):
		"""Gets or sets the display of multiple leaders for this callout."""
		self._instance.MultipleLeaders = value

	@property
	def opaque_color(self):
		"""Gets or sets the opaque (background) color for the labels for this callout."""
		return self._instance.OpaqueColor

	@opaque_color.setter
	def opaque_color(self, value):
		"""Gets or sets the opaque (background) color for the labels for this callout."""
		self._instance.OpaqueColor = value

	@property
	def position(self):
		"""Gets and sets the position of this callout."""
		return self._instance.Position

	@position.setter
	def position(self, value):
		"""Gets and sets the position of this callout."""
		self._instance.Position = value

	@property
	def skip_colon(self):
		"""Gets and sets whether to add a colon at the end of the callout label."""
		return self._instance.SkipColon

	@skip_colon.setter
	def skip_colon(self, value):
		"""Gets and sets whether to add a colon at the end of the callout label."""
		self._instance.SkipColon = value

	@property
	def target_style(self):
		"""Gets or sets the type of connection at the target point for this callout."""
		return self._instance.TargetStyle

	@target_style.setter
	def target_style(self, value):
		"""Gets or sets the type of connection at the target point for this callout."""
		self._instance.TargetStyle = value

	@property
	def text_box(self):
		"""Gets or sets whether the callout text is enclosed within a box."""
		return self._instance.TextBox

	@text_box.setter
	def text_box(self, value):
		"""Gets or sets whether the callout text is enclosed within a box."""
		self._instance.TextBox = value

	@property
	def text_color(self):
		"""Gets or sets the color of the text in the specified row in this callout."""
		return self._instance.TextColor

	@text_color.setter
	def text_color(self, value):
		"""Gets or sets the color of the text in the specified row in this callout."""
		self._instance.TextColor = value

	@property
	def text_format(self):
		"""Gets or sets the text format for this callout."""
		return self._instance.TextFormat

	@text_format.setter
	def text_format(self, value):
		"""Gets or sets the text format for this callout."""
		self._instance.TextFormat = value

	@property
	def value(self):
		"""Gets or sets the value in for the specified row in this callout."""
		return self._instance.Value

	@value.setter
	def value(self, value):
		"""Gets or sets the value in for the specified row in this callout."""
		self._instance.Value = value

	@property
	def value_inactive(self):
		"""Gets or sets whether the user can edit the value in the specified row in this callout."""
		return self._instance.ValueInactive

	@value_inactive.setter
	def value_inactive(self, value):
		"""Gets or sets whether the user can edit the value in the specified row in this callout."""
		self._instance.ValueInactive = value

	@property
	def display(self):
		"""Shows or hides the independent (i.e., not attached to a selection) callout."""
		return self._instance.Display

	@display.setter
	def display(self, value):
		"""Shows or hides the independent (i.e., not attached to a selection) callout."""
		self._instance.Display = value

	@property
	def get_leader(self):
		"""Gets the leader properties of the callout."""
		return self._instance.GetLeader

	@get_leader.setter
	def get_leader(self, value):
		"""Gets the leader properties of the callout."""
		self._instance.GetLeader = value

	@property
	def get_target_point(self):
		"""Gets the target point for the specified row in this callout."""
		return self._instance.GetTargetPoint

	@get_target_point.setter
	def get_target_point(self, value):
		"""Gets the target point for the specified row in this callout."""
		self._instance.GetTargetPoint = value

	@property
	def set_leader(self):
		"""Sets the leader properties of the callout."""
		return self._instance.SetLeader

	@set_leader.setter
	def set_leader(self, value):
		"""Sets the leader properties of the callout."""
		self._instance.SetLeader = value

	@property
	def set_target_point(self):
		"""Sets the target point for the specified row in this callout."""
		return self._instance.SetTargetPoint

	@set_target_point.setter
	def set_target_point(self, value):
		"""Sets the target point for the specified row in this callout."""
		self._instance.SetTargetPoint = value

