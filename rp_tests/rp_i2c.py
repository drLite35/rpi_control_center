import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
import subprocess

# from gettext import gettext as _
from utils import Window, load_css


def gui():
    window = Window()
    scrolled_window = window.get_scrolled_window()
    mainVbox = window.get_mainbox()
    window.set_markup("Connected I2C devices")

    css = b"""
    .terminal-txt {
        background-color: #000;
        color: #ACED9A;
        padding-top: 5px;
        padding-right: 50px;
        padding-left: 50px;
        border-radius: 20px;
        font-family: monospace;
        font-size: 25px;
    }
    """
    load_css(css)

#     output_eg = """
#       0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
# 00 :                      -- -- -- -- -- -- -- -- --
# 10 : -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 20 : -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 30 : -- -- -- -- -- -- -- -- -- -- -- -- 3c -- -- --
# 40 : -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 50 : -- -- -- -- -- -- -- -- -- -- -- -- -- 5d -- --
# 60 : -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
# 70 : -- -- -- -- -- -- -- --
#     """

    output = subprocess.check_output(['i2cdetect', '-y', '1']).decode('utf-8')

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    available_devices = Gtk.Label()
    available_devices.set_halign(Gtk.Align.CENTER)
    hbox.get_style_context().add_class("terminal-txt")
    hbox.set_halign(Gtk.Align.CENTER)
    hbox.set_margin_start(50)
    hbox.set_margin_end(50)
    hbox.set_margin_top(20)
    hbox.set_margin_bottom(20)

    lines = output.strip().replace(":", "").split("\n")

    available_devices_txt = '<span font="20">\
Available device(s) at address(es): '
    devices_found = False
    # Skip the first line (column headers)
    for line in lines[1:]:
        elements = line.split()
        for i, element in enumerate(elements[1:]):
            if element != "--":
                devices_found = True
                # Calculate the device address correctly
                # device_address = (row_address << 4) | i
                available_devices_txt += f"0x{element}, "

    if not devices_found:
        available_devices_txt = '<span font="20">No devices found</span>'
    else:
        available_devices_txt = available_devices_txt.rstrip(", ") + "</span>"
    available_devices.set_markup(available_devices_txt)
    available_devices.show()

    output_label = Gtk.Label()
    output_label.set_text(output)
    hbox.pack_start(output_label, False, False, 0)
    mainVbox.pack_start(hbox, False, False, 0)
    mainVbox.pack_start(available_devices, False, False, 50)
    output_label.show()

    return scrolled_window
