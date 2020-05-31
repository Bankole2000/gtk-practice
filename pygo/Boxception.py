import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
  def __init__(self): 
    Gtk.Window.__init__(self, title = "Window Title")
    self.set_border_width(20)
    self.set_default_size(500, 300)

    # Boxes
    hbox = Gtk.Box(spacing=20)
    hbox.set_homogeneous(False)
    vbox_left= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
    vbox_left.set_homogeneous(False)
    vbox_right= Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
    vbox_right.set_homogeneous(False)
    
    # pack the two columns 
    hbox.pack_start(vbox_left, True, True, 0)
    hbox.pack_start(vbox_right, True, True, 0)

    # Normal
    label = Gtk.Label("This is a plan label")
    vbox_left.pack_start(label, True, True, 0)

    # Left aligned
    label = Gtk.Label()
    label.set_text("This is left aligned text.\nOh wow multiple lines")
    label.set_justify(Gtk.Justification.LEFT)
    vbox_left.pack_start(label, True, True, 0)

    # Right aligned
    label = Gtk.Label()
    label.set_text("This is right aligned text.\nOh wow multiple lines")
    label.set_justify(Gtk.Justification.RIGHT)
    vbox_left.pack_start(label, True, True, 0)

    # Line wrap
    label = Gtk.Label("Hi My name is Banky")
    # line wrap for text
    label.set_line_wrap(True)
    # justify
    label.set_justify(Gtk.Justification.FILL)
    vbox_right.pack_start(label, True, True, 0)

    # Markup
    label = Gtk.Label()
    label.set_markup("<small>Small Text</small>\n"
                     "<big>Big Text</big>\n"
                     "<b>Bold Text</b>\n"
                     "<i>Italics are cool too</i>\n"
                     "<a href=\"https://google.com\" title=\"Hover Text\">Here's a link</a>\n")
    label.set_line_wrap(True)
    vbox_right.pack_start(label, True, True, 0)                 

    self.add(hbox)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()