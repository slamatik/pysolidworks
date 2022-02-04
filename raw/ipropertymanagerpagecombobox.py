# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageCombobox_members.html
class IPropertyManagerPageCombobox:
	def __init__(self, parent=None):
		self._instance = parent

	def current_selection(self):
		"""Gets and sets the item that is currently selected for this combo box."""
		# return self._instance.CurrentSelection
		raise NotImplemented

	@property
	def edit_text(self):
		"""Gets or sets the text in the combo box."""
		return self._instance.EditText

	@edit_text.setter
	def edit_text(self, value):
		"""Gets or sets the text in the combo box."""
		self._instance.EditText = value

	@property
	def height(self):
		"""Gets and sets the maximum height of the attached drop-down combo box."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets and sets the maximum height of the attached drop-down combo box."""
		self._instance.Height = value

	@property
	def item_text(self):
		"""Gets the text from the attached drop-down list for this combo box."""
		return self._instance.ItemText

	@item_text.setter
	def item_text(self, value):
		"""Gets the text from the attached drop-down list for this combo box."""
		self._instance.ItemText = value

	@property
	def style(self):
		"""Gets or sets the style for the attached drop-down list for this combo box."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets the style for the attached drop-down list for this combo box."""
		self._instance.Style = value

	@property
	def add_items(self):
		"""Adds items to the attached drop-down list for this combo box."""
		return self._instance.AddItems

	@add_items.setter
	def add_items(self, value):
		"""Adds items to the attached drop-down list for this combo box."""
		self._instance.AddItems = value

	@property
	def clear(self):
		"""Clears all items from the attached drop-down list for this combo box."""
		return self._instance.Clear

	@clear.setter
	def clear(self, value):
		"""Clears all items from the attached drop-down list for this combo box."""
		self._instance.Clear = value

	@property
	def delete_item(self):
		"""Deletes an item from the attached drop-down list of this combo box."""
		return self._instance.DeleteItem

	@delete_item.setter
	def delete_item(self, value):
		"""Deletes an item from the attached drop-down list of this combo box."""
		self._instance.DeleteItem = value

	@property
	def i_add_items(self):
		"""Adds items to the attached drop-down list for this combo box."""
		return self._instance.IAddItems

	@i_add_items.setter
	def i_add_items(self, value):
		"""Adds items to the attached drop-down list for this combo box."""
		self._instance.IAddItems = value

	@property
	def insert_item(self):
		"""Inserts an item in the attached drop-down list of this combo box."""
		return self._instance.InsertItem

	@insert_item.setter
	def insert_item(self, value):
		"""Inserts an item in the attached drop-down list of this combo box."""
		self._instance.InsertItem = value

