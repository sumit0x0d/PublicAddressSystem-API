import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# import RPi.GPIO as GPIO

import subprocess

class GridTop(Gtk.Grid):
    def __init__(self):
        super().__init__(column_homogeneous=True, row_homogeneous=False, column_spacing=10, row_spacing=10)
        
        label = Gtk.Label(label="PUBLIC ADDRESS SYSTEM INTERFACE")
        self.add(label)

class GridCenter(Gtk.Grid):
    def __init__(self):
        super().__init__(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=10)

        self.pin = [21, 23, 3, 29, 31, 33, 35, 37, 22, 24, 26, 5, 32, 36, 38, 40]

        button_zone1 = Gtk.ToggleButton(label="ZONE 1")
        button_zone1.connect("clicked", self.button_clicked_zone, 1)
        button_zone2 = Gtk.ToggleButton(label="ZONE 2")
        button_zone2.connect("clicked", self.button_clicked_zone, 2)
        button_zone3 = Gtk.ToggleButton(label="ZONE 3")
        button_zone3.connect("clicked", self.button_clicked_zone, 3)
        button_zone4 = Gtk.ToggleButton(label="ZONE 4")
        button_zone4.connect("clicked", self.button_clicked_zone, 4)
        button_zone5 = Gtk.ToggleButton(label="ZONE 5")
        button_zone5.connect("clicked", self.button_clicked_zone, 5)
        button_zone6 = Gtk.ToggleButton(label="ZONE 6")
        button_zone6.connect("clicked", self.button_clicked_zone, 6)
        button_zone7 = Gtk.ToggleButton(label="ZONE 7")
        button_zone7.connect("clicked", self.button_clicked_zone, 7)
        button_zone8 = Gtk.ToggleButton(label="ZONE 8")
        button_zone8.connect("clicked", self.button_clicked_zone, 8)
        button_zone9 = Gtk.ToggleButton(label="ZONE 9")
        button_zone9.connect("clicked", self.button_clicked_zone, 9)
        button_zone10 = Gtk.ToggleButton(label="ZONE 10")
        button_zone10.connect("clicked", self.button_clicked_zone, 10)
        button_zone11 = Gtk.ToggleButton(label="ZONE 11")
        button_zone11.connect("clicked", self.button_clicked_zone, 11)
        button_zone12 = Gtk.ToggleButton(label="ZONE 12")
        button_zone12.connect("clicked", self.button_clicked_zone, 12)
        button_zone13 = Gtk.ToggleButton(label="ZONE 13")
        button_zone13.connect("clicked", self.button_clicked_zone, 13)
        button_zone14 = Gtk.ToggleButton(label="ZONE 14")
        button_zone14.connect("clicked", self.button_clicked_zone, 14)
        button_zone15 = Gtk.ToggleButton(label="ZONE 15")
        button_zone15.connect("clicked", self.button_clicked_zone, 15)
        button_zone16 = Gtk.ToggleButton(label="ZONE 16")
        button_zone16.connect("clicked", self.button_clicked_zone, 16)

        self.attach(button_zone1, 0, 0, 1, 1)
        self.attach(button_zone2, 1, 0, 1, 1)
        self.attach(button_zone3, 2, 0, 1, 1)
        self.attach(button_zone4, 3, 0, 1, 1)
        self.attach(button_zone5, 0, 1, 1, 1)
        self.attach(button_zone6, 1, 1, 1, 1)
        self.attach(button_zone7, 2, 1, 1, 1)
        self.attach(button_zone8, 3, 1, 1, 1)
        self.attach(button_zone9, 0, 2, 1, 1)
        self.attach(button_zone10, 1, 2, 1, 1)
        self.attach(button_zone11, 2, 2, 1, 1)
        self.attach(button_zone12, 3, 2, 1, 1)
        self.attach(button_zone13, 0, 3, 1, 1)
        self.attach(button_zone14, 1, 3, 1, 1)
        self.attach(button_zone15, 2, 3, 1, 1)
        self.attach(button_zone16, 3, 3, 1, 1)

    def button_clicked_zone(self, button, zone):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin[zone - 1], GPIO.OUT)
        if button.get_active():
            GPIO.output(self.pin[zone - 1], GPIO.LOW)
            subprocess.Popen(["aplay", "zone_on.wav"])
        else:
            GPIO.output(self.pin[zone - 1], GPIO.HIGH)
            subprocess.Popen(["aplay", "zone_off.wav"])

class GridBottomLeft(Gtk.Grid):
    def __init__(self):
        super().__init__(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=10)

        zone_all_button = Gtk.ToggleButton(label="ALL ZONES")
        refresh_button = Gtk.ToggleButton(label="REFRESH")

        microphone_label = Gtk.Label(label = "MICROPHONE")
        microphone_switch = Gtk.Switch()
        microphone_switch.connect("notify::active", self.microphone_switch_toggled)
        microphone_switch.set_active(False)

        self.attach(zone_all_button, 0, 0, 2, 1)
        self.attach(refresh_button, 0, 1, 2, 1)
        self.attach(microphone_label, 0, 2, 1, 1)
        self.attach(microphone_switch, 1, 2, 1, 1)

    def microphone_switch_toggled(self, microphone_switch, param):
        if microphone_switch.get_active():
            state = "MICROPHONE ON"
        else:
            state = "MICROPHONE OFF"

class GridBottomRight(Gtk.Grid):
    def __init__(self):
        super().__init__(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=10)
 
        audio_test = Gtk.ToggleButton(label="Audio Test")
        powered_by_label = Gtk.Label(label="Powered By")
        tans_label = Gtk.Label(label="----")

        self.attach(audio_test, 0, 0, 1, 2)
        self.attach(powered_by_label, 0, 2, 1, 1)
        self.attach(tans_label, 0, 3, 1, 1)

class GridBottom(Gtk.Grid):
    def __init__(self):
        super().__init__(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=10)

        self.attach(GridBottomLeft(), 0, 0, 1, 1)
        self.attach(GridBottomRight(), 1, 0, 1, 1)

class GridMain(Gtk.Grid):
    def __init__(self):
        super().__init__(column_homogeneous=True, row_homogeneous=True, column_spacing=10, row_spacing=10)
        
        self.attach(GridTop(), 0, 0, 1, 1)
        self.attach(GridCenter(), 0, 1, 1, 3)
        self.attach(GridBottom(), 0, 4, 1, 2)

class WindowMain(Gtk.Window):
    def __init__(self):
        super().__init__(title="Public Address System")

        self.set_default_size(640, 480)
        self.set_resizable(False)

        grid_main = GridMain()
        grid_main.set_margin_start(20)
        grid_main.set_margin_end(20)
        grid_main.set_margin_top(20)
        grid_main.set_margin_bottom(20)

        self.add(grid_main)

window = WindowMain()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
