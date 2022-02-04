# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageNumberbox_members.html
class IPropertyManagerPageNumberbox:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def current_selection(self):
		"""Gets or sets the item that is currently selected in the number box."""
		return self._instance.CurrentSelection

	@current_selection.setter
	def current_selection(self, value):
		"""Gets or sets the item that is currently selected in the number box."""
		self._instance.CurrentSelection = value

	@property
	def displayed_unit(self):
		"""Gets or sets the unit type to display in this PropertyManager page number box."""
		return self._instance.DisplayedUnit

	@displayed_unit.setter
	def displayed_unit(self, value):
		"""Gets or sets the unit type to display in this PropertyManager page number box."""
		self._instance.DisplayedUnit = value

	@property
	def height(self):
		"""Gets or sets the maximum height of the attached drop-down list for this number box."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the maximum height of the attached drop-down list for this number box."""
		self._instance.Height = value

	@property
	def item_text(self):
		"""Gets the text for an item in the attached drop-down list for this number box."""
		return self._instance.ItemText

	@item_text.setter
	def item_text(self, value):
		"""Gets the text for an item in the attached drop-down list for this number box."""
		self._instance.ItemText = value

	@property
	def style(self):
		"""Gets or sets the style of the attached drop-down list for this number box."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets the style of the attached drop-down list for this number box."""
		self._instance.Style = value

	@property
	def text(self):
		"""Gets the text that appears in the number box."""
		return self._instance.Text

	@text.setter
	def text(self, value):
		"""Gets the text that appears in the number box."""
		self._instance.Text = value

	@property
	def value(self):
		"""Gets and sets the value that appears in the number box."""
		return self._instance.Value

	@value.setter
	def value(self, value):
		"""Gets and sets the value that appears in the number box."""
		self._instance.Value = value

	@property
	def add_items(self):
		"""Adds items to the attached drop-down list of a number box."""
		return self._instance.AddItems

	@add_items.setter
	def add_items(self, value):
		"""Adds items to the attached drop-down list of a number box."""
		self._instance.AddItems = value

	@property
	def clear(self):
		"""Clears all items from the attached drop-down list for this the number box."""
		return self._instance.Clear

	@clear.setter
	def clear(self, value):
		"""Clears all items from the attached drop-down list for this the number box."""
		self._instance.Clear = value

	@property
	def delete_item(self):
		"""Deletes an item from the attached drop-down list for this number box."""
		return self._instance.DeleteItem

	@delete_item.setter
	def delete_item(self, value):
		"""Deletes an item from the attached drop-down list for this number box."""
		self._instance.DeleteItem = value

	@property
	def i_add_items(self):
		"""Adds items to the attached drop-down list of a number box."""
		return self._instance.IAddItems

	@i_add_items.setter
	def i_add_items(self, value):
		"""Adds items to the attached drop-down list of a number box."""
		self._instance.IAddItems = value

	@property
	def insert_item(self):
		"""Inserts an item in the attached drop-down list for this number box."""
		return self._instance.InsertItem

	@insert_item.setter
	def insert_item(self, value):
		"""Inserts an item in the attached drop-down list for this number box."""
		self._instance.InsertItem = value

	@property
	def set_range(self):
		"""Sets the range and increment for the slider."""
		return self._instance.SetRange2

	@set_range.setter
	def set_range(self, value):
		"""Sets the range and increment for the slider."""
		self._instance.SetRange2 = value

	@property
	def set_slider_parameters(self):
		"""Sets the parameters for the slider."""
		return self._instance.SetSliderParameters

	@set_slider_parameters.setter
	def set_slider_parameters(self, value):
		"""Sets the parameters for the slider."""
		self._instance.SetSliderParameters = value

