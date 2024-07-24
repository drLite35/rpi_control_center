import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# from gettext import gettext as _
# from time import sleep

from rp_tests.utils import Window


class RP_SPI:
    @staticmethod
    def gui():
        window = Window()
        scrolled_window = window.get_scrolled_window()
        mainVbox = window.get_mainbox()
        window.set_markup("Connected SPI devices")

        # check if spi devices are connected
        # shell command to discover spi: ls /dev/spi*:
        #       /dev/spidev0.0  /dev/spidev`0.1
        # When no spi detected the output would be:
        #       ls: cannot access '/dev/spi*': No such file or directory

        return scrolled_window
