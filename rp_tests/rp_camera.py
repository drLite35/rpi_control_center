import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from gettext import gettext as _
# from picamera2 import Picamera2, Preview
from time import sleep


def gui():
    scrolled_window = Gtk.ScrolledWindow()
    scrolled_window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(.92, .92, .92, 1))
    mainVbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    mainVbox.set_margin_bottom(60)
    
    scrolled_window.add(mainVbox)
    scrolled_window.set_policy(hscrollbar_policy=Gtk.PolicyType.AUTOMATIC, vscrollbar_policy=Gtk.PolicyType.AUTOMATIC)

    gpiotxt=Gtk.Label()
    mainVbox.pack_start(gpiotxt, False, False, 100)
    gpiotxt.set_markup('<span font="25">Camera status</span>') 
    gpiotxt.set_use_markup(True)
    gpiotxt.show()
    mainVbox.show()
    scrolled_window.show()
    
    # shell command to discover cam: vcgencmd get_camera;   supported=1 detected=1, libcamera interfaces=0;;    
    # When no camera detected the output would be:  vcgencmd get_camera--->supported=0 detected=0
    
    # picam2 = Picamera2()
    # picam2.start_preview(Preview.QTGL)
    # picam2.start()
    # sleep(5)
    # picam2.close()

    
    return scrolled_window