from com import Com
from enums import *


class ISldWorks:
    def __init__(self):
        self._isldworks = Com('SldWorks.Application')

    def _active_doc(self):
        return self._isldworks.ActiveDoc

    def _application_type(self):
        return ApplicationType(self._isldworks.ApplicationType)

    def _command_in_progress(self, value: bool):
        self._isldworks.CommandInProgress = value

    def _get_enable_background_processing(self):
        return self._isldworks.EnableBackgroundProcessing

    def _set_enable_background_processing(self, state):
        self._isldworks.EnableBackgroundProcessing = state

    def _get_enable_file_menu(self):
        return self._isldworks.EnableFileMenu

    def _set_enable_file_menu(self, state):
        self._isldworks.EnableFileMenu = state

    def _get_frame_height(self):
        return self._isldworks.FrameHeight

    def _set_frame_height(self, value):
        self._isldworks.FrameHeight = value

    def _get_frame_width(self):
        return self._isldworks.FrameWidth

    def _set_frame_width(self, value):
        self._isldworks.FrameWidth = value

    def _get_visible(self):
        return self._isldworks.Visible

    def _set_visible(self, state):
        self._isldworks.Visible = state
