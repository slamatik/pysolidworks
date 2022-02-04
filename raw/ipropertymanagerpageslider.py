# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSlider_members.html
class IPropertyManagerPageSlider:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def height(self):
		"""Gets or sets the height of the slider control."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of the slider control."""
		self._instance.Height = value

	@property
	def line_size(self):
		"""Gets or sets how much the slider moves when the arrow keys are used to move the slider."""
		return self._instance.LineSize

	@line_size.setter
	def line_size(self, value):
		"""Gets or sets how much the slider moves when the arrow keys are used to move the slider."""
		self._instance.LineSize = value

	@property
	def page_size(self):
		"""Gets or sets how much the slider moves when the Page Up or Page Down keys are used to move the slider."""
		return self._instance.PageSize

	@page_size.setter
	def page_size(self, value):
		"""Gets or sets how much the slider moves when the Page Up or Page Down keys are used to move the slider."""
		self._instance.PageSize = value

	@property
	def position(self):
		"""Gets or sets the current position of the slider."""
		return self._instance.Position

	@position.setter
	def position(self, value):
		"""Gets or sets the current position of the slider."""
		self._instance.Position = value

	@property
	def style(self):
		"""Gets or sets the display properties of a slider control."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets the display properties of a slider control."""
		self._instance.Style = value

	@property
	def tick_frequency(self):
		"""Gets or sets the frequency of tick marks on a slider."""
		return self._instance.TickFrequency

	@tick_frequency.setter
	def tick_frequency(self, value):
		"""Gets or sets the frequency of tick marks on a slider."""
		self._instance.TickFrequency = value

	@property
	def get_range(self):
		"""Gets the range of the slider."""
		return self._instance.GetRange

	@get_range.setter
	def get_range(self, value):
		"""Gets the range of the slider."""
		self._instance.GetRange = value

	@property
	def set_range(self):
		"""Sets the range of a slider."""
		return self._instance.SetRange

	@set_range.setter
	def set_range(self, value):
		"""Sets the range of a slider."""
		self._instance.SetRange = value

