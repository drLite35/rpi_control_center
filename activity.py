import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

# from gpio import gui
from rp_tests.rp_gpio import RP_GPIO
from rp_tests.rp_i2c import RP_I2C
from rp_tests.rp_camera import RP_CAM
from rp_tests.rp_settings import RP_SETTINGS
from rp_tests.rp_audio RP_AUDIO
from rp_tests.rp_spi RP_SPI
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
        self.radiobutton_cb(None, 'gpio')

    def radiobutton_cb(self, name):
        button = 'RP_' + name.upper()

        # set canvas
        self.set_canvas(globals()[button].gui)
        canvas = self.get_canvas()
        canvas.override_background_color(
            Gtk.StateType.NORMAL, Gdk.RGBA(0.92, 0.92, 0.92, 1))
