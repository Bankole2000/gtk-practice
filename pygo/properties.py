import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

window = Gtk.Window()

label = Gtk.Label()
label.set_label("Learning GTK is awesome")
label.set_angle(30)
label.set_halign(Gtk.Align.END)
window.add(label)

print(label.get_properties("angle"))

window.connect("delete_event", Gtk.main_quit)
window.show_all()
Gtk.main()