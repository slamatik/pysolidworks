# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.html
class IPropertyManagerPageSelectionbox:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def allow_multiple_select_of_same_entity(self):
		"""Gets or sets whether the same entity can be selected multiple times in this selection box."""
		return self._instance.AllowMultipleSelectOfSameEntity

	@allow_multiple_select_of_same_entity.setter
	def allow_multiple_select_of_same_entity(self, value):
		"""Gets or sets whether the same entity can be selected multiple times in this selection box."""
		self._instance.AllowMultipleSelectOfSameEntity = value

	@property
	def allow_select_in_multiple_boxes(self):
		"""Gets or sets whether an entity can be selected in this selection box if the entity is selected elsewhere."""
		return self._instance.AllowSelectInMultipleBoxes

	@allow_select_in_multiple_boxes.setter
	def allow_select_in_multiple_boxes(self, value):
		"""Gets or sets whether an entity can be selected in this selection box if the entity is selected elsewhere."""
		self._instance.AllowSelectInMultipleBoxes = value

	@property
	def callout(self):
		"""Gets or sets a multi-row, editable callout for this selection box."""
		return self._instance.Callout

	@callout.setter
	def callout(self, value):
		"""Gets or sets a multi-row, editable callout for this selection box."""
		self._instance.Callout = value

	@property
	def current_selection(self):
		"""Gets or sets the index number of the currently selected item in this selection box."""
		return self._instance.CurrentSelection

	@current_selection.setter
	def current_selection(self, value):
		"""Gets or sets the index number of the currently selected item in this selection box."""
		self._instance.CurrentSelection = value

	@property
	def enable_select_identical_components(self):
		"""Gets or sets whether to enable Select Identical Components in the context menu of this PropertyManager page selection box."""
		return self._instance.EnableSelectIdenticalComponents

	@enable_select_identical_components.setter
	def enable_select_identical_components(self, value):
		"""Gets or sets whether to enable Select Identical Components in the context menu of this PropertyManager page selection box."""
		self._instance.EnableSelectIdenticalComponents = value

	@property
	def height(self):
		"""Gets or sets the height of this selection box."""
		return self._instance.Height

	@height.setter
	def height(self, value):
		"""Gets or sets the height of this selection box."""
		self._instance.Height = value

	@property
	def item_count(self):
		"""Gets the number of items currently in this selection box."""
		return self._instance.ItemCount

	@item_count.setter
	def item_count(self, value):
		"""Gets the number of items currently in this selection box."""
		self._instance.ItemCount = value

	@property
	def item_text(self):
		"""Gets the specified item in this selection box."""
		return self._instance.ItemText

	@item_text.setter
	def item_text(self, value):
		"""Gets the specified item in this selection box."""
		self._instance.ItemText = value

	@property
	def mark(self):
		"""Gets or sets the mark used on selected items in this selection box."""
		return self._instance.Mark

	@mark.setter
	def mark(self, value):
		"""Gets or sets the mark used on selected items in this selection box."""
		self._instance.Mark = value

	@property
	def selection_index(self):
		"""Gets the index number of the currently selected item in the selection box."""
		return self._instance.SelectionIndex

	@selection_index.setter
	def selection_index(self, value):
		"""Gets the index number of the currently selected item in the selection box."""
		self._instance.SelectionIndex = value

	@property
	def single_entity_only(self):
		"""Gets or sets whether this selection box is for single or multiple items."""
		return self._instance.SingleEntityOnly

	@single_entity_only.setter
	def single_entity_only(self, value):
		"""Gets or sets whether this selection box is for single or multiple items."""
		self._instance.SingleEntityOnly = value

	@property
	def style(self):
		"""Gets or sets style of this selection box."""
		return self._instance.Style

	@style.setter
	def style(self, value):
		"""Gets or sets style of this selection box."""
		self._instance.Style = value

	@property
	def add_menu_popup_item(self):
		"""Adds a menu item to the pop-up menu for this selection box of the PropertyManager page."""
		return self._instance.AddMenuPopupItem

	@add_menu_popup_item.setter
	def add_menu_popup_item(self, value):
		"""Adds a menu item to the pop-up menu for this selection box of the PropertyManager page."""
		self._instance.AddMenuPopupItem = value

	@property
	def get_selected_items(self):
		"""Gets the items selected in a PropertyManager selection box."""
		return self._instance.GetSelectedItems

	@get_selected_items.setter
	def get_selected_items(self, value):
		"""Gets the items selected in a PropertyManager selection box."""
		self._instance.GetSelectedItems = value

	@property
	def get_selected_items_count(self):
		"""Gets the number of currently selected items in this PropertyManager selection box."""
		return self._instance.GetSelectedItemsCount

	@get_selected_items_count.setter
	def get_selected_items_count(self, value):
		"""Gets the number of currently selected items in this PropertyManager selection box."""
		self._instance.GetSelectedItemsCount = value

	@property
	def get_selection_focus(self):
		"""Gets whether this is the active selection box."""
		return self._instance.GetSelectionFocus

	@get_selection_focus.setter
	def get_selection_focus(self, value):
		"""Gets whether this is the active selection box."""
		self._instance.GetSelectionFocus = value

	@property
	def i_get_selected_items(self):
		"""Gets the items selected in a PropertyManager selection box."""
		return self._instance.IGetSelectedItems

	@i_get_selected_items.setter
	def i_get_selected_items(self, value):
		"""Gets the items selected in a PropertyManager selection box."""
		self._instance.IGetSelectedItems = value

	@property
	def i_set_selection_filters(self):
		"""Defines the types of objects the user can select for this selection box."""
		return self._instance.ISetSelectionFilters

	@i_set_selection_filters.setter
	def i_set_selection_filters(self, value):
		"""Defines the types of objects the user can select for this selection box."""
		self._instance.ISetSelectionFilters = value

	@property
	def set_callout_label(self):
		"""Sets the default callout label for selections made in this selection box on the PropertyManager page."""
		return self._instance.SetCalloutLabel

	@set_callout_label.setter
	def set_callout_label(self, value):
		"""Sets the default callout label for selections made in this selection box on the PropertyManager page."""
		self._instance.SetCalloutLabel = value

	@property
	def set_selected_item(self):
		"""Sets whether an item is selected or cleared in a selection box enabled for multiple selection."""
		return self._instance.SetSelectedItem

	@set_selected_item.setter
	def set_selected_item(self, value):
		"""Sets whether an item is selected or cleared in a selection box enabled for multiple selection."""
		self._instance.SetSelectedItem = value

	@property
	def set_selection_color(self):
		"""Sets the color for selections made in this selection box on the PropertyManager page."""
		return self._instance.SetSelectionColor

	@set_selection_color.setter
	def set_selection_color(self, value):
		"""Sets the color for selections made in this selection box on the PropertyManager page."""
		self._instance.SetSelectionColor = value

	@property
	def set_selection_filters(self):
		"""Defines the types of objects the user can select for this selection box."""
		return self._instance.SetSelectionFilters

	@set_selection_filters.setter
	def set_selection_filters(self, value):
		"""Defines the types of objects the user can select for this selection box."""
		self._instance.SetSelectionFilters = value

	@property
	def set_selection_focus(self):
		"""Sets this object as the active selection box."""
		return self._instance.SetSelectionFocus

	@set_selection_focus.setter
	def set_selection_focus(self, value):
		"""Sets this object as the active selection box."""
		self._instance.SetSelectionFocus = value

