# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html
class IFrame:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def keep_invisible(self):
		"""Gets or sets whether to keep the SOLIDWORKS frame invisible."""
		return self._instance.KeepInvisible

	@keep_invisible.setter
	def keep_invisible(self, value):
		"""Gets or sets whether to keep the SOLIDWORKS frame invisible."""
		self._instance.KeepInvisible = value

	@property
	def menu_pinned(self):
		"""Gets or sets whether the SOLIDWORKS main menu is pinned."""
		return self._instance.MenuPinned

	@menu_pinned.setter
	def menu_pinned(self, value):
		"""Gets or sets whether the SOLIDWORKS main menu is pinned."""
		self._instance.MenuPinned = value

	@property
	def model_windows(self):
		"""Gets the client model windows for this frame."""
		return self._instance.ModelWindows

	@model_windows.setter
	def model_windows(self, value):
		"""Gets the client model windows for this frame."""
		self._instance.ModelWindows = value

	@property
	def add_menu(self):
		"""Adds a menu item."""
		return self._instance.AddMenu

	@add_menu.setter
	def add_menu(self, value):
		"""Adds a menu item."""
		self._instance.AddMenu = value

	@property
	def add_menu_item(self):
		"""Adds a menu item and bitmap or a separator to an existing menu."""
		return self._instance.AddMenuItem2

	@add_menu_item.setter
	def add_menu_item(self, value):
		"""Adds a menu item and bitmap or a separator to an existing menu."""
		self._instance.AddMenuItem2 = value

	@property
	def add_menu_popup_icon(self):
		"""Adds an icon to a context-sensitive menu of a C++ SOLIDWORKS add-in."""
		return self._instance.AddMenuPopupIcon

	@add_menu_popup_icon.setter
	def add_menu_popup_icon(self, value):
		"""Adds an icon to a context-sensitive menu of a C++ SOLIDWORKS add-in."""
		self._instance.AddMenuPopupIcon = value

	@property
	def add_menu_popup_icon(self):
		"""Adds an icon to a context-sensitive menu of a SOLIDWORKS add-in."""
		return self._instance.AddMenuPopupIcon3

	@add_menu_popup_icon.setter
	def add_menu_popup_icon(self, value):
		"""Adds an icon to a context-sensitive menu of a SOLIDWORKS add-in."""
		self._instance.AddMenuPopupIcon3 = value

	@property
	def add_menu_popup_item(self):
		"""Adds a menu item or separator to a shortcut menu (i.e., a right-click pop-up menu)."""
		return self._instance.AddMenuPopupItem2

	@add_menu_popup_item.setter
	def add_menu_popup_item(self, value):
		"""Adds a menu item or separator to a shortcut menu (i.e., a right-click pop-up menu)."""
		self._instance.AddMenuPopupItem2 = value

	@property
	def get_h_wnd(self):
		"""Gets the window handle for the main frame."""
		return self._instance.GetHWnd

	@get_h_wnd.setter
	def get_h_wnd(self, value):
		"""Gets the window handle for the main frame."""
		self._instance.GetHWnd = value

	@property
	def get_h_wndx(self):
		"""Gets the window handle for the main frame in 64-bit applications."""
		return self._instance.GetHWndx64

	@get_h_wndx.setter
	def get_h_wndx(self, value):
		"""Gets the window handle for the main frame in 64-bit applications."""
		self._instance.GetHWndx64 = value

	@property
	def get_menu(self):
		"""Gets the menu handle for the main frame."""
		return self._instance.GetMenu

	@get_menu.setter
	def get_menu(self, value):
		"""Gets the menu handle for the main frame."""
		self._instance.GetMenu = value

	@property
	def get_menux(self):
		"""Gets the menu handle for the main frame in 64-bit applications."""
		return self._instance.GetMenux64

	@get_menux.setter
	def get_menux(self, value):
		"""Gets the menu handle for the main frame in 64-bit applications."""
		self._instance.GetMenux64 = value

	@property
	def get_model_window_count(self):
		"""Gets the number of child model windows for this frame."""
		return self._instance.GetModelWindowCount

	@get_model_window_count.setter
	def get_model_window_count(self, value):
		"""Gets the number of child model windows for this frame."""
		self._instance.GetModelWindowCount = value

	@property
	def get_status_bar_pane(self):
		"""Gets a pointer to one of up to five panes on the right side of the status bar."""
		return self._instance.GetStatusBarPane

	@get_status_bar_pane.setter
	def get_status_bar_pane(self, value):
		"""Gets a pointer to one of up to five panes on the right side of the status bar."""
		self._instance.GetStatusBarPane = value

	@property
	def get_sub_menu_count(self):
		"""Gets the number of submenus for this frame."""
		return self._instance.GetSubMenuCount

	@get_sub_menu_count.setter
	def get_sub_menu_count(self, value):
		"""Gets the number of submenus for this frame."""
		self._instance.GetSubMenuCount = value

	@property
	def get_sub_menus(self):
		"""Gets the submenus for this frame."""
		return self._instance.GetSubMenus

	@get_sub_menus.setter
	def get_sub_menus(self, value):
		"""Gets the submenus for this frame."""
		self._instance.GetSubMenus = value

	@property
	def i_get_model_windows(self):
		"""Gets the child model windows for this frame."""
		return self._instance.IGetModelWindows

	@i_get_model_windows.setter
	def i_get_model_windows(self, value):
		"""Gets the child model windows for this frame."""
		self._instance.IGetModelWindows = value

	@property
	def i_get_sub_menus(self):
		"""Gets the submenus for this frame."""
		return self._instance.IGetSubMenus

	@i_get_sub_menus.setter
	def i_get_sub_menus(self, value):
		"""Gets the submenus for this frame."""
		self._instance.IGetSubMenus = value

	@property
	def remove_menu(self):
		"""Removes a menu item."""
		return self._instance.RemoveMenu

	@remove_menu.setter
	def remove_menu(self, value):
		"""Removes a menu item."""
		self._instance.RemoveMenu = value

	@property
	def remove_menu_popup_icon(self):
		"""Removes an icon from a context-sensitive shortcut (popup) menu."""
		return self._instance.RemoveMenuPopupIcon

	@remove_menu_popup_icon.setter
	def remove_menu_popup_icon(self, value):
		"""Removes an icon from a context-sensitive shortcut (popup) menu."""
		self._instance.RemoveMenuPopupIcon = value

	@property
	def rename_menu(self):
		"""Renames a menu item."""
		return self._instance.RenameMenu

	@rename_menu.setter
	def rename_menu(self, value):
		"""Renames a menu item."""
		self._instance.RenameMenu = value

	@property
	def set_status_bar_text(self):
		"""Displays a text string in the main status bar area to the left of the status bar."""
		return self._instance.SetStatusBarText

	@set_status_bar_text.setter
	def set_status_bar_text(self, value):
		"""Displays a text string in the main status bar area to the left of the status bar."""
		self._instance.SetStatusBarText = value

	@property
	def show_model_window(self):
		"""Shows a client model window."""
		return self._instance.ShowModelWindow

	@show_model_window.setter
	def show_model_window(self, value):
		"""Shows a client model window."""
		self._instance.ShowModelWindow = value

