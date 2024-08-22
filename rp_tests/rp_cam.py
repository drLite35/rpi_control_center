import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# from gettext import gettext as _

# from picamera2 import Picamera2, Preview
# from time import sleep

from rp_tests.utils import Window


class CAM:
    @staticmethod
    def gui():
        window = Window()
        scrolled_window = window.get_scrolled_window()
        mainVbox = window.get_mainbox()
        window.set_markup("Camera status")

        # shell command to discover cam: vcgencmd get_camera:
        #       supported=1 detected=1, libcamera interfaces=0;
        # When no camera detected the output would be:
        #       vcgencmd get_camera--->supported=0 detected=0

        # picam2 = Picamera2()
        # picam2.start_preview(Preview.QTGL)
        # picam2.start()
        # sleep(5)
        # picam2.close()

        return scrolled_window
