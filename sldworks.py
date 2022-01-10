import subprocess as sb
import win32com.client as win32
from interfaces import *


class SldWorks(ISldWorks):
    def __init__(self):
        super().__init__()

    @property
    def active_doc(self):
        # todo return Doc()
        return self._active_doc()

    @property
    def application_type(self):
        return self._application_type()

    def command_in_progress(self, state):
        self._command_in_progress(state)

    @property
    def enable_background_processing(self):
        return self._get_enable_background_processing()

    @enable_background_processing.setter
    def enable_background_processing(self, state):
        self._set_enable_background_processing(state)

    @property
    def enable_file_menu(self):
        return self._get_enable_file_menu()

    @enable_file_menu.setter
    def enable_file_menu(self, state):
        self._set_enable_file_menu(state)

    @property
    def frame_height(self):
        return self._get_frame_height()

    @frame_height.setter
    def frame_height(self, value):
        self._set_frame_height(value)

    @property
    def frame_width(self):
        return self._get_frame_width()

    @frame_width.setter
    def frame_width(self, value):
        self._set_frame_width(value)

    @property
    def visible(self):
        return self._get_visible()

    @visible.setter
    def visible(self, state):
        self._set_visible(state)

    @staticmethod
    def start(*args):
        """Starts a SolidWorks session.

        This method starts a new SolidWorks Session. It is equivalent to
        launching SolidWorks manually and all add-in, user-preference, etc.
        will be loaded using this method. If SolidWorks session with all the
        user preferences loaded is desired. Launch the session using this
        static method proir to instantiating an instance of :class:'SolidWorks'

        Args:
            version (int, optional): Last 2-digits of the year of the
            SolidWorks instance you would like to use. If there is only one
            version of SolidWorks installed on your machine DO NOT enter an
            arguement

        Examples: SolidWorks.start(20)
        """

        if not args:
            SW_PROCESS_NAME = (
                r"C:/Program Files/SOLIDWORKS Corp/SOLIDWORKS/SLDWORKS.exe"
            )
            sb.Popen(SW_PROCESS_NAME)
        else:
            year = int(args[0][-1])
            SW_PROCESS_NAME = f"SldWorks.Application.{(20 + (year - 2))}"
            win32.Dispatch(SW_PROCESS_NAME)
