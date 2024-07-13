import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# from gettext import gettext as _
# from time import sleep


def gui():
    scrolled_window = Gtk.ScrolledWindow()
    mainVbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    mainVbox.set_margin_bottom(60)

    scrolled_window.add(mainVbox)
    scrolled_window.set_policy(
        hscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
        vscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
    )

    gpiotxt = Gtk.Label()
    mainVbox.pack_start(gpiotxt, False, False, 100)
    gpiotxt.set_markup('<span font="25">Connected SPI devices</span>')
    gpiotxt.set_use_markup(True)
    gpiotxt.show()
    mainVbox.show()
    scrolled_window.show()

    # check if spi devices are connected
    # shell command to discover spi: ls /dev/spi*:
    #       /dev/spidev0.0  /dev/spidev`0.1
    # When no spi detected the output would be:
    #       ls: cannot access '/dev/spi*': No such file or directory

    return scrolled_window
