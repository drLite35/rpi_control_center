import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pyaudio
import wave

from utils import Window

# from gettext import gettext as _


def play_test_sound(device_index):
    chunk = 1024
    test_file = "test.wav"  # Ensure you have a test.wav file in your directory

    wf = wave.open(test_file, 'rb')
    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    output_device_index=device_index)

    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()


def gui():
    window = Window()
    scrolled_window = window.get_scrolled_window()
    mainVbox = window.get_mainbox()
    window.set_markup("Camera status")

    # Audio device selection
    device_store = Gtk.ListStore(str, int)
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        device_store.append([device_info['name'], i])
    p.terminate()

    device_combo = Gtk.ComboBox.new_with_model(device_store)
    renderer_text = Gtk.CellRendererText()
    device_combo.pack_start(renderer_text, True)
    device_combo.add_attribute(renderer_text, "text", 0)
    mainVbox.pack_start(device_combo, False, False, 0)

    test_button = Gtk.Button(label="Test Audio")
    test_button.connect("clicked", lambda w: play_test_sound(
        device_combo.get_active()))
    mainVbox.pack_start(test_button, False, False, 0)

    return scrolled_window
