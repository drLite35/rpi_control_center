import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import importlib
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
            button.props.icon_name = name.lower()
            if len(self.names) > 0:
                button.props.group = self.names['GPIO']
            toolbar_box.toolbar.insert(button, -1)
            self.names[name] = button
            button.connect('toggled', self.radiobutton_cb, name)

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

        # home screen
        self.radiobutton_cb(None, 'GPIO')

    def radiobutton_cb(self, button, name):
        # Dynamically import the module and retrieve class
        module = importlib.import_module('rp_tests.rp_' + name.lower())
        globals()[name] = getattr(module, name)
        # set canvas
        self.set_canvas(globals()[name].gui())
        canvas = self.get_canvas()
        canvas.override_background_color(
            Gtk.StateType.NORMAL, Gdk.RGBA(0.92, 0.92, 0.92, 1))
