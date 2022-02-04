# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageListbox_members.html
class IPropertyManagerPageListbox:
	def __init__(self, parent=None):
		self._instance = parent

	def current_selection(self):
		"""Gets and sets the item that is currently selected in this list box."""
		# return self._instance.CurrentSelection
		raise NotImplemented

	def height(self):
		"""Gets and sets the height of the attached drop-down list for this list box."""
		# return self._instance.Height
		raise NotImplemented

	def item_count(self):
		"""Gets the number of items in the attached drop-down list for this list box."""
		# return self._instance.ItemCount
		raise NotImplemented

	def item_text(self, item):
		"""
		Gets the text for the specified item in this list box.
		:param item: Position of the item where to get the text in the 0-based list or -1 to get the text of the currently selected item
		"""
		# return self._instance.ItemText(item)
		raise NotImplemented

	@property
	def style(self):
		"""Gets or sets style for this list box."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets style for this list box."""
		self._instance.Style = value

	@property
	def add_items(self):
		"""Adds items to the attached drop-down list for this list box."""
		return self._instance.AddItems

	@add_items.setter
	def add_items(self, value):
		"""Adds items to the attached drop-down list for this list box."""
		self._instance.AddItems = value

	@property
	def clear(self):
		"""Clears all items from attached drop-down list for this list box."""
		return self._instance.Clear

	@clear.setter
	def clear(self, value):
		"""Clears all items from attached drop-down list for this list box."""
		self._instance.Clear = value

	@property
	def delete_item(self):
		"""Removes the specified item from the attached drop-down list for this list box."""
		return self._instance.DeleteItem

	@delete_item.setter
	def delete_item(self, value):
		"""Removes the specified item from the attached drop-down list for this list box."""
		self._instance.DeleteItem = value

	@property
	def get_selected_items(self):
		"""Gets the items selected in a list box enabled for multiple selections."""
		return self._instance.GetSelectedItems

	@get_selected_items.setter
	def get_selected_items(self, value):
		"""Gets the items selected in a list box enabled for multiple selections."""
		self._instance.GetSelectedItems = value

	@property
	def get_selected_items_count(self):
		"""Gets the number of items currently selected in a list box enabled for multiple selection."""
		return self._instance.GetSelectedItemsCount

	@get_selected_items_count.setter
	def get_selected_items_count(self, value):
		"""Gets the number of items currently selected in a list box enabled for multiple selection."""
		self._instance.GetSelectedItemsCount = value

	@property
	def i_add_items(self):
		"""Adds items to the attached drop-down list for this list box."""
		return self._instance.IAddItems

	@i_add_items.setter
	def i_add_items(self, value):
		"""Adds items to the attached drop-down list for this list box."""
		self._instance.IAddItems = value

	@property
	def i_get_selected_items(self):
		"""Gets the items selected in a list box enabled for multiple selections."""
		return self._instance.IGetSelectedItems

	@i_get_selected_items.setter
	def i_get_selected_items(self, value):
		"""Gets the items selected in a list box enabled for multiple selections."""
		self._instance.IGetSelectedItems = value

	@property
	def insert_item(self):
		"""Inserts an item in the attached drop-down list of this list box."""
		return self._instance.InsertItem

	@insert_item.setter
	def insert_item(self, value):
		"""Inserts an item in the attached drop-down list of this list box."""
		self._instance.InsertItem = value

	@property
	def set_selected_item(self):
		"""Sets whether an item is selected or cleared in a list box enabled for multiple selection."""
		return self._instance.SetSelectedItem

	@set_selected_item.setter
	def set_selected_item(self, value):
		"""Sets whether an item is selected or cleared in a list box enabled for multiple selection."""
		self._instance.SetSelectedItem = value

