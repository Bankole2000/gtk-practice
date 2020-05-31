import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
  def __init__(self): 
    Gtk.Window.__init__(self, title = "Notebook Demo")
    self.set_border_width(10)
    self.set_default_size(500, 400)
    self.notebook = Gtk.Notebook()
    self.add(self.notebook)

    # first page
    self.page1 = Gtk.Box()
    self.page1.set_border_width(10)
    self.page1.add(Gtk.Label("Here is the stuff that is in the main area."))
    self.notebook.append_page(self.page1, Gtk.Label("First Tab"))

    # first page
    self.page2 = Gtk.Box()
    self.page2.set_border_width(10)
    self.page2.add(Gtk.Label("Page 2 main area."))
    icon = Gtk.Image.new_from_icon_name("gnome-dev-cdrom-audio", Gtk.IconSize.MENU)
    self.notebook.append_page(self.page2, icon)
    

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()