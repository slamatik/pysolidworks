# http://help.solidworks.com/2021/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html
class IModelViewManager:
	def __init__(self, parent=None):
		self._instance = parent

	@property
	def active_feature_manager_tab_index(self):
		"""Gets or sets the index of the active tab in the Manager Pane."""
		return self._instance.ActiveFeatureManagerTabIndex

	@active_feature_manager_tab_index.setter
	def active_feature_manager_tab_index(self, value):
		"""Gets or sets the index of the active tab in the Manager Pane."""
		self._instance.ActiveFeatureManagerTabIndex = value

	@property
	def document(self):
		"""Gets the document to which this model view belongs."""
		return self._instance.Document

	@document.setter
	def document(self, value):
		"""Gets the document to which this model view belongs."""
		self._instance.Document = value

	@property
	def feature_manager_tabs_visible(self):
		"""Gets or sets whether all of the tabs in the Manager Pane are visible."""
		return self._instance.FeatureManagerTabsVisible

	@feature_manager_tabs_visible.setter
	def feature_manager_tabs_visible(self, value):
		"""Gets or sets whether all of the tabs in the Manager Pane are visible."""
		self._instance.FeatureManagerTabsVisible = value

	@property
	def linked_views(self):
		"""Gets or sets whether linking of viewports is enabled in this document."""
		return self._instance.LinkedViews

	@linked_views.setter
	def linked_views(self, value):
		"""Gets or sets whether linking of viewports is enabled in this document."""
		self._instance.LinkedViews = value

	@property
	def viewport_display(self):
		"""Sets the model's viewport arrangement."""
		return self._instance.ViewportDisplay

	@viewport_display.setter
	def viewport_display(self, value):
		"""Sets the model's viewport arrangement."""
		self._instance.ViewportDisplay = value

	@property
	def activate_control_tab(self):
		"""Selects a control tab on the model view to be the active tab."""
		return self._instance.ActivateControlTab

	@activate_control_tab.setter
	def activate_control_tab(self, value):
		"""Selects a control tab on the model view to be the active tab."""
		self._instance.ActivateControlTab = value

	@property
	def activate_model_tab(self):
		"""Selects a control tab on the model view."""
		return self._instance.ActivateModelTab

	@activate_model_tab.setter
	def activate_model_tab(self, value):
		"""Selects a control tab on the model view."""
		self._instance.ActivateModelTab = value

	@property
	def add_control(self):
		"""Adds a tab to this model view using the specified ActiveX control."""
		return self._instance.AddControl

	@add_control.setter
	def add_control(self, value):
		"""Adds a tab to this model view using the specified ActiveX control."""
		self._instance.AddControl = value

	@property
	def add_control(self):
		"""Adds a tab to this model view that supports tab traversal using the specified ActiveX control."""
		return self._instance.AddControl3

	@add_control.setter
	def add_control(self, value):
		"""Adds a tab to this model view that supports tab traversal using the specified ActiveX control."""
		self._instance.AddControl3 = value

	@property
	def add_snap_shot(self):
		"""Creates a snapshot with the specified name of an assembly."""
		return self._instance.AddSnapShot

	@add_snap_shot.setter
	def add_snap_shot(self, value):
		"""Creates a snapshot with the specified name of an assembly."""
		self._instance.AddSnapShot = value

	@property
	def create_feature_mgr_control(self):
		"""Creates a new FeatureManager design tree view containing the specified ActiveX control with a tab that displays the specified scaleable icon."""
		return self._instance.CreateFeatureMgrControl4

	@create_feature_mgr_control.setter
	def create_feature_mgr_control(self, value):
		"""Creates a new FeatureManager design tree view containing the specified ActiveX control with a tab that displays the specified scaleable icon."""
		self._instance.CreateFeatureMgrControl4 = value

	@property
	def create_feature_mgr_view(self):
		"""Creates a new view (tab) in this FeatureManager design tree."""
		return self._instance.CreateFeatureMgrView2

	@create_feature_mgr_view.setter
	def create_feature_mgr_view(self, value):
		"""Creates a new view (tab) in this FeatureManager design tree."""
		self._instance.CreateFeatureMgrView2 = value

	@property
	def create_feature_mgr_window_from_handle(self):
		"""Creates a new view in the FeatureManager design tree using the specified .NET tab control."""
		return self._instance.CreateFeatureMgrWindowFromHandle

	@create_feature_mgr_window_from_handle.setter
	def create_feature_mgr_window_from_handle(self, value):
		"""Creates a new view in the FeatureManager design tree using the specified .NET tab control."""
		self._instance.CreateFeatureMgrWindowFromHandle = value

	@property
	def create_feature_mgr_window_from_handlex(self):
		"""On 64-bit machines, creates a new view in the FeatureManager design tree using the specified .NET tab control."""
		return self._instance.CreateFeatureMgrWindowFromHandlex64

	@create_feature_mgr_window_from_handlex.setter
	def create_feature_mgr_window_from_handlex(self, value):
		"""On 64-bit machines, creates a new view in the FeatureManager design tree using the specified .NET tab control."""
		self._instance.CreateFeatureMgrWindowFromHandlex64 = value

	@property
	def create_manipulator(self):
		"""Creates a manipulator, which is similar to the triad in the SOLIDWORKS user interface."""
		return self._instance.CreateManipulator

	@create_manipulator.setter
	def create_manipulator(self, value):
		"""Creates a manipulator, which is similar to the triad in the SOLIDWORKS user interface."""
		self._instance.CreateManipulator = value

	@property
	def create_section_view(self):
		"""Creates a section view in parts and assemblies."""
		return self._instance.CreateSectionView

	@create_section_view.setter
	def create_section_view(self, value):
		"""Creates a section view in parts and assemblies."""
		self._instance.CreateSectionView = value

	@property
	def create_section_view_data(self):
		"""Creates an empty ISectionViewData object whose properties you set before creating a section view in a part or an assembly."""
		return self._instance.CreateSectionViewData

	@create_section_view_data.setter
	def create_section_view_data(self, value):
		"""Creates an empty ISectionViewData object whose properties you set before creating a section view in a part or an assembly."""
		self._instance.CreateSectionViewData = value

	@property
	def delete_control_tab(self):
		"""Deletes the specified control tab."""
		return self._instance.DeleteControlTab

	@delete_control_tab.setter
	def delete_control_tab(self, value):
		"""Deletes the specified control tab."""
		self._instance.DeleteControlTab = value

	@property
	def delete_snap_shot(self):
		"""Deletes the specified snapshot from an assembly."""
		return self._instance.DeleteSnapShot

	@delete_snap_shot.setter
	def delete_snap_shot(self, value):
		"""Deletes the specified snapshot from an assembly."""
		self._instance.DeleteSnapShot = value

	@property
	def display_window_from_handle(self):
		"""Displays a .NET control in this model view."""
		return self._instance.DisplayWindowFromHandle

	@display_window_from_handle.setter
	def display_window_from_handle(self, value):
		"""Displays a .NET control in this model view."""
		self._instance.DisplayWindowFromHandle = value

	@property
	def display_window_from_handlex(self):
		"""Displays a .NET control in this model view on 64-bit machines."""
		return self._instance.DisplayWindowFromHandlex64

	@display_window_from_handlex.setter
	def display_window_from_handlex(self, value):
		"""Displays a .NET control in this model view on 64-bit machines."""
		self._instance.DisplayWindowFromHandlex64 = value

	@property
	def get_configuration_manager_tab_index(self):
		"""Gets the index of the ConfigurationManager tab in the Manager Pane."""
		return self._instance.GetConfigurationManagerTabIndex

	@get_configuration_manager_tab_index.setter
	def get_configuration_manager_tab_index(self, value):
		"""Gets the index of the ConfigurationManager tab in the Manager Pane."""
		self._instance.GetConfigurationManagerTabIndex = value

	@property
	def get_control(self):
		"""Gets the control associated with this model view."""
		return self._instance.GetControl

	@get_control.setter
	def get_control(self, value):
		"""Gets the control associated with this model view."""
		self._instance.GetControl = value

	@property
	def get_dim_xpert_manager_tab_index(self):
		"""Gets the index of the DimXpertManager tab in the Manager Pane."""
		return self._instance.GetDimXpertManagerTabIndex

	@get_dim_xpert_manager_tab_index.setter
	def get_dim_xpert_manager_tab_index(self, value):
		"""Gets the index of the DimXpertManager tab in the Manager Pane."""
		self._instance.GetDimXpertManagerTabIndex = value

	@property
	def get_display_manager_tab_index(self):
		"""Gets the index of the DisplayManager tab in the Manager Pane."""
		return self._instance.GetDisplayManagerTabIndex

	@get_display_manager_tab_index.setter
	def get_display_manager_tab_index(self, value):
		"""Gets the index of the DisplayManager tab in the Manager Pane."""
		self._instance.GetDisplayManagerTabIndex = value

	@property
	def get_feature_manager_tabs(self):
		"""Gets the tabs from right to left in the Manager Pane."""
		return self._instance.GetFeatureManagerTabs

	@get_feature_manager_tabs.setter
	def get_feature_manager_tabs(self, value):
		"""Gets the tabs from right to left in the Manager Pane."""
		self._instance.GetFeatureManagerTabs = value

	@property
	def get_feature_manager_tree_tab_index(self):
		"""Gets the index of the FeatureManager design tree tab in the Manager Pane."""
		return self._instance.GetFeatureManagerTreeTabIndex

	@get_feature_manager_tree_tab_index.setter
	def get_feature_manager_tree_tab_index(self, value):
		"""Gets the index of the FeatureManager design tree tab in the Manager Pane."""
		self._instance.GetFeatureManagerTreeTabIndex = value

	@property
	def get_feature_mgr_view_h_wnd(self):
		"""Gets the window handle for the specified FeatureManager design tree view."""
		return self._instance.GetFeatureMgrViewHWnd

	@get_feature_mgr_view_h_wnd.setter
	def get_feature_mgr_view_h_wnd(self, value):
		"""Gets the window handle for the specified FeatureManager design tree view."""
		self._instance.GetFeatureMgrViewHWnd = value

	@property
	def get_feature_mgr_view_h_wndx(self):
		"""Gets the window handle for the specified FeatureManager design tree view in 64-bit applications."""
		return self._instance.GetFeatureMgrViewHWndx64

	@get_feature_mgr_view_h_wndx.setter
	def get_feature_mgr_view_h_wndx(self, value):
		"""Gets the window handle for the specified FeatureManager design tree view in 64-bit applications."""
		self._instance.GetFeatureMgrViewHWndx64 = value

	@property
	def get_property_manager_tab_index(self):
		"""Gets the index of the PropertyManager tab in the Manager Pane."""
		return self._instance.GetPropertyManagerTabIndex

	@get_property_manager_tab_index.setter
	def get_property_manager_tab_index(self, value):
		"""Gets the index of the PropertyManager tab in the Manager Pane."""
		self._instance.GetPropertyManagerTabIndex = value

	@property
	def get_section_view_data(self):
		"""Gets access to the data of the specified section view."""
		return self._instance.GetSectionViewData

	@get_section_view_data.setter
	def get_section_view_data(self, value):
		"""Gets access to the data of the specified section view."""
		self._instance.GetSectionViewData = value

	@property
	def get_snap_shot(self):
		"""Gets the specified snapshot of an assembly."""
		return self._instance.GetSnapShot

	@get_snap_shot.setter
	def get_snap_shot(self, value):
		"""Gets the specified snapshot of an assembly."""
		self._instance.GetSnapShot = value

	@property
	def get_snap_shots(self):
		"""Gets the snapshots of an assembly."""
		return self._instance.GetSnapShots

	@get_snap_shots.setter
	def get_snap_shots(self, value):
		"""Gets the snapshots of an assembly."""
		self._instance.GetSnapShots = value

	@property
	def i_get_control(self):
		"""Gets the control associated with this model view."""
		return self._instance.IGetControl

	@i_get_control.setter
	def i_get_control(self, value):
		"""Gets the control associated with this model view."""
		self._instance.IGetControl = value

	@property
	def is_control_tab_active(self):
		"""Gets whether the specified control is active."""
		return self._instance.IsControlTabActive

	@is_control_tab_active.setter
	def is_control_tab_active(self, value):
		"""Gets whether the specified control is active."""
		self._instance.IsControlTabActive = value

	@property
	def is_model_tab_active(self):
		"""Gets whether the control on this model view is active."""
		return self._instance.IsModelTabActive

	@is_model_tab_active.setter
	def is_model_tab_active(self, value):
		"""Gets whether the control on this model view is active."""
		self._instance.IsModelTabActive = value

	@property
	def remove_section_view(self):
		"""Removes a section view from a part and assembly."""
		return self._instance.RemoveSectionView

	@remove_section_view.setter
	def remove_section_view(self, value):
		"""Removes a section view from a part and assembly."""
		self._instance.RemoveSectionView = value

