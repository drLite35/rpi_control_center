import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from gettext import gettext as _

# from gpio import gui
import rp_tests.rp_gpio as rp_gpio
import rp_tests.rp_i2c as rp_i2c
import rp_tests.rp_camera as rp_camera
import rp_tests.rp_settings as rp_settings
import rp_tests.rp_audio as rp_audio
import rp_tests.rp_spi as rp_spi
from rp_tests.rp_list import names, tooltips

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.radiotoolbutton import RadioToolButton


class RPiControlCenterActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.max_participants = 1

        # toolbar
        toolbar_box = ToolbarBox()
        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        # toolbar buttons
        self.names = {}
        for name in names:
            button = RadioToolButton()
            button.set_tooltip(tooltips[name])
            button.props.icon_name = name
            if len(self.names) > 0:
                button.props.group = self.names['gpio']
            toolbar_box.toolbar.insert(button, -1)
            self.names[name] = button
            button.connect('toggled', self.on_radiobutton_toggle, name)
 
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        self.show_all()

        # canvas
        self.set_canvas(rp_settings.gui())


    def on_radiobutton_toggle(self, _b, name):
        if name == 'gpio':
            self.set_canvas(rp_gpio.gui())
        elif name == 'i2c':
            self.set_canvas(rp_i2c.gui())
        elif name == 'cam':
            self.set_canvas(rp_camera.gui())
        elif name == 'settings':
            self.set_canvas(rp_settings.gui())
        elif name == 'audio':
            self.set_canvas(rp_audio.gui())
        elif name == 'spi':
            self.set_canvas(rp_spi.gui())
        
