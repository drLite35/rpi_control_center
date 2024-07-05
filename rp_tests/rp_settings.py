import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

from gettext import gettext as _
import rp_tests.rp_list as rp_list

import os
import subprocess


def gui():
    get_settings()
    scrolled_window = Gtk.ScrolledWindow()
    scrolled_window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(.92, .92, .92, 1))
    mainVbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    mainVbox.set_margin_bottom(60)
    
    scrolled_window.add(mainVbox)
    scrolled_window.set_policy(hscrollbar_policy=Gtk.PolicyType.AUTOMATIC,\
        vscrollbar_policy=Gtk.PolicyType.AUTOMATIC)

    heading_label=Gtk.Label()
    mainVbox.pack_start(heading_label, False, False, 60)
    heading_label.set_markup('<span font="25">Settings</span>') 
    heading_label.set_use_markup(True)
    heading_label.set_halign(Gtk.Align.CENTER)
    scrolled_window.show_all()
    
    # god these boxes
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    b_pad1 = Gtk.Grid()
    b_pad2 = Gtk.Grid()
    b_pad3 = Gtk.Grid()
    b_pad4 = Gtk.Grid()
    b2 = Gtk.Grid()
    b3 = Gtk.Grid()

    # Since we're using grids, we don't need to change the packing into hbox
    hbox.pack_start(b_pad1, True, True, 0)
    hbox.pack_start(b_pad2, True, True, 0)
    hbox.pack_start(b2, True, True, 0)
    hbox.pack_start(b_pad3, True, True, 0)
    hbox.pack_start(b3, True, True, 0)
    hbox.pack_start(b_pad4, True, True, 0)
    hbox.show_all()
    mainVbox.show_all()
    mainVbox.pack_start(hbox, False, False, 0)
    
    css = b"""
    .settings-button{
        border: none;
        background-color: #FF616D ;
        color: #FFF;
        border-radius: 50px;
        font-size: 16px;
    }
    .settings-button:checked, .settings-button:active{
        background-color: #ACED9A;
        color: #000;
        }

    """
    
    style_provider = Gtk.CssProvider()
    style_provider.load_from_data(css)
    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
    
    
    for i, setting in enumerate(rp_list.settings):
        button = Gtk.ToggleButton("ON" if rp_list.settings_status[setting] else "OFF")
        button.get_style_context().add_class('settings-button')
        label = Gtk.Label()
        label.get_style_context().add_class('settings-label')
        label.set_markup('<span font="18">'+rp_list.settings[setting]+'</span>')
        button.set_margin_top(10)
        button.set_margin_bottom(10)
        label.set_margin_top(10)
        label.set_margin_bottom(10)
        button.set_size_request(70, 30)
        
        b3.attach(button, 0, i, 1, 1) 
        b2.attach(label, 0, i, 1, 1) 
        
        label.set_halign(Gtk.Align.START)
        button.show()
        label.show()
        # toggle buttons on if settings are on
        if rp_list.settings_status[setting]:
            button.set_active(True)
        button.connect('toggled', change_settings, setting)        
        
        
    ################  Advance Settings Expander ################
    # expander_label=Gtk.Label()
    # expander_label.set_markup('<span font="25">+ Advanced Settings</span>') 
    # expander_label.set_use_markup(True)
    # expander_label.show()
    
    # expander = Gtk.Expander()
    # expander.set_label_widget(expander_label)
    # expander.set_halign(Gtk.Align.CENTER)
    
    # mainVbox.pack_start(expander, False, True, 60)
    # adv_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
    # expander.add(adv_box)
    # adv_box.show()
    # expander.show()
    
    # separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    # adv_box.pack_start(separator, False, True, 0)
    # separator.show()
        
    # adv_settings_label=Gtk.Label()
    # adv_settings_label.set_markup('<span font="25">Advanced Settings</span>') 
    # adv_settings_label.set_use_markup(True)
    # adv_settings_label.set_halign(Gtk.Align.CENTER)
    # adv_box.pack_start(adv_settings_label, False, False, 100)
    # adv_settings_label.show()
    
        
    return scrolled_window



def get_settings():
    for i in rp_list.settings_status:
        try:    
            # get func.. 1=off 0=on
            rp_list.settings_status.update({i:not int((subprocess.run(\
                f'sudo raspi-config nonint get_{i}',\
                shell=True, capture_output=True, text=True).stdout.strip()))})
        except:
            print(f'Error in get_settings()\t are u in a raspberry pi? {i}')
    
    # try except to check if it's working properly
    # - pin = digitalio.DigitalInOut(board.D4)
    # - i2c = busio.I2C(board.SCL, board.SDA)
    # - spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
       
        
def change_settings(button, item):
    # 1|0 -> 1=false/off 0=true/on
    os.system('sudo raspi-config nonint do_'+ item +' '+\
        str(int(rp_list.settings_status[item])))
    rp_list.settings_status.update({item: int(\
        rp_list.settings_status[item])})
    
    
    
        
'''
################# raspi-config nonint #################
# 1|0 -> 1=false/off 0=true/on
raspi-config nonint get_can_expand
raspi-config nonint do_expand_rootfs
raspi-config nonint get_hostname
raspi-config nonint do_hostname "yourhostname"
raspi-config nonint get_boot_cli
raspi-config nonint get_autologin
raspi-config nonint do_boot_behaviour B1 #boot options
raspi-config nonint do_boot_behaviour B2
raspi-config nonint do_boot_behaviour B3
raspi-config nonint do_boot_behaviour B4 
raspi-config nonint get_boot_wait
raspi-config nonint do_boot_wait 1|0
raspi-config nonint get_boot_splash
raspi-config nonint do_boot_splash 1|0
raspi-config nonint get_overscan
raspi-config nonint do_overscan 1|0
raspi-config nonint get_pixdub
raspi-config nonint do_pixdub 1|0
raspi-config nonint get_camera
raspi-config nonint do_camera 1|0
raspi-config nonint get_ssh
raspi-config nonint do_ssh 1|0
raspi-config nonint get_vnc
raspi-config nonint do_vnc 1|0
raspi-config nonint get_spi
raspi-config nonint do_spi 1|0
raspi-config nonint get_i2c
raspi-config nonint do_i2c 1|0
raspi-config nonint get_serial
raspi-config nonint get_serial_hw
raspi-config nonint do_serial 1|0
raspi-config nonint get_onewire
raspi-config nonint do_onewire 1|0
raspi-config nonint get_rgpio
raspi-config nonint do_rgpio 1|0
raspi-config nonint get_blanking
raspi-config nonint do_blanking 1|0
raspi-config nonint get_pi_type
raspi-config nonint is_pi
raspi-config nonint is_pifour
raspi-config nonint is_fkms
raspi-config nonint get_config_var arm_freq /boot/config.txt
raspi-config nonint do_overclock None|Modest|Medium|High|Turbo
raspi-config nonint get_config_var gpu_mem /boot/config.txt
raspi-config nonint get_config_var gpu_mem_256 /boot/config.txt
raspi-config nonint get_config_var gpu_mem_512 /boot/config.txt
raspi-config nonint get_config_var gpu_mem_1024 /boot/config.txt
raspi-config nonint do_memory_split 16|32|64|128|256
raspi-config nonint get_config_var hdmi_group /boot/config.txt
raspi-config nonint get_config_var hdmi_mode /boot/config.txt
raspi-config nonint get_wifi_country
# find wifi countries here /usr/share/zoneinfo/iso3166.tab
raspi-config nonint do_wifi_country "yourcountry"
raspi-config nonint do_pi4video V1
raspi-config nonint do_pi4video V2
raspi-config nonint do_pi4video V3
raspi-config nonint get_pi4video
raspi-config nonint get_overlay_now
raspi-config nonint get_overlay_conf
raspi-config nonint get_bootro_conf
raspi-config nonint enable_overlayfs
raspi-config nonint disable_overlayfs
raspi-config nonint enable_bootro
raspi-config nonint disable_bootro
raspi-config nonint is_uname_current
raspi-config nonint list_wlan_interfaces
raspi-config nonint is_installed realvnc-vnc-server
raspi-config nonint is_installed xscreensaver
vcgencmd get_mem gpu | cut -d = -f 2 | cut -d M -f 1
echo \"$SUDO_USER:%s\" | chpasswd
'''