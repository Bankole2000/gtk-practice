import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
  def __init__(self): 
    Gtk.Window.__init__(self, title = "Window Title")

    # Box
    self.box = Gtk.Box(spacing=10)
    self.add(self.box)

    # Buttons
    self.bacon_button = Gtk.Button(label="Bacon")
    self.bacon_button.connect("clicked", self.clicked)
    self.box.pack_start(self.bacon_button, True, True, 0)

    # Tuna button 
    self.tuna_button = Gtk.Button(label="tuna")
    self.tuna_button.connect("clicked", self.clicked)
    self.box.pack_start(self.tuna_button, True, True, 0)

  def clicked(self, widget):
    label = widget.get_properties("label")
    print(label)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()