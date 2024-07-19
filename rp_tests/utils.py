from gi.repository import Gtk, Gdk


class Window:

    def __init__(self):
        self.scrolled_window = Gtk.ScrolledWindow()
        self.mainVbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.mainVbox.set_margin_bottom(60)

        self.scrolled_window.add(self.mainVbox)
        self.scrolled_window.set_policy(
            hscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
            vscrollbar_policy=Gtk.PolicyType.AUTOMATIC,
        )

        self.gpiotxt = Gtk.Label()
        self.mainVbox.pack_start(self.gpiotxt, False, False, 100)
        self.gpiotxt.show()
        self.mainVbox.show()
        self.scrolled_window.show()

    def set_markup(self, text):
        self.gpiotxt.set_markup(f'<span font="25">{text}</span>')
        self.gpiotxt.set_use_markup(True)

    def get_mainbox(self):
        return self.mainVbox

    def get_scrolled_window(self):
        return self.scrolled_window


def load_css(css):
    style_provider = Gtk.CssProvider()
    style_provider.load_from_data(css)
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
