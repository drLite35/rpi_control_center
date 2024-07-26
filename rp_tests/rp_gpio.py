import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# from gettext import gettext as _

import digitalio
import board

import rp_tests.rp_list as rp_list
from rp_tests.utils import Window, load_css


class GPIO:
    @staticmethod
    def gui():
        window = Window()
        scrolled_window = window.get_scrolled_window()
        mainVbox = window.get_mainbox()
        window.set_markup("GPIO Pins Control")

        secVbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        gpioTopRow = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        gpioBottomRow = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        gpioBottomRow.set_halign(Gtk.Align.CENTER)
        gpioTopRow.set_halign(Gtk.Align.CENTER)

        # load css
        css = b"""
        button.5v, button.5v:checked, button.5v:active,
        button.3v3, button.3v3:checked, button.3v3:active{
            color: #FFF;
            background-color: #FF616D;
        }
        button.gnd, button.gnd:checked, button.gnd:active {
            background-color: #000;
            color: #FFF;
        }
        button.eep, button.eep:checked, button.eep:active {
            color: #000;
            background-color: #FFF;
        }
        .gpio-tb{
            border: none;
            margin: 5px;
            color: #FFF;
            border-radius: 50px;
            font-size: 18px;
        }

        .gpio-tb:checked, .gpio-tb:active{
            background-color: #A3F5FF;
            color: #000;
                }

        #secVbox{
            border-radius: 25px;
            background-color: #B4B4B4;
        }
        """
        load_css(css)

        # create toggle buttons
        for index, pin in enumerate(rp_list.gpio):
            btn = Gtk.ToggleButton()
            btn.get_style_context().add_class("gpio-tb")
            btn.set_halign(Gtk.Align.START)
            btn.set_label(pin)
            if index % 2 == 0:
                gpioBottomRow.pack_start(btn, False, False, 0)
            else:
                gpioTopRow.pack_start(btn, False, False, 0)
            btn.set_size_request(60, 60)

            # other settings
            if pin in rp_list.disabled_gpio:
                btn.get_style_context().add_class(pin.lower())
            else:
                btn.connect("toggled", on_gpio_toggle, "D" + pin)

            btn.show()

        # mainVbox items
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        mainVbox.pack_start(hbox, False, False, 0)
        hbox.pack_start(secVbox, False, False, 0)
        hbox.set_halign(Gtk.Align.CENTER)
        hbox.set_margin_bottom(50)
        hbox.show()

        # hbox items
        secVbox.pack_start(gpioTopRow, False, False, 0)
        secVbox.pack_start(gpioBottomRow, False, False, 0)
        gpioBottomRow.set_margin_bottom(20)
        gpioTopRow.set_margin_start(25)
        gpioTopRow.set_margin_end(25)
        gpioTopRow.set_margin_top(25)
        secVbox.set_name("secVbox")

        gpioBottomRow.show()
        gpioTopRow.show()
        secVbox.show()

        return scrolled_window


def on_gpio_toggle(button, pin_no):
    pin = digitalio.DigitalInOut(getattr(board, pin_no))
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = 1 if button.get_active() else 0
