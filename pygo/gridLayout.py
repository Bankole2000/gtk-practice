import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
  def __init__(self): 
    Gtk.Window.__init__(self, title = "Window Title")

    grid = Gtk.Grid()
    self.add(grid)

    # Create a bunch of buttons
    button1 = Gtk.Button(label='Button 1')
    button2 = Gtk.Button(label='Button 2')
    button3 = Gtk.Button(label='Button 3')
    button4 = Gtk.Button(label='Button 4')
    button5 = Gtk.Button(label='Button 5')
    button6 = Gtk.Button(label='Button 6')

    grid.add(button1) # starts from top left
    # attact (item, colum, row, with, height)
    # rows and columns start with 0
    grid.attach(button2, 1, 0, 2, 1)

    # position with reference to button 1
    # (elemtn, elemtn to place next to, rel position, width, height)
    grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 1)
    grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
    grid.attach(button5, 3, 0, 2, 2)
    grid.attach(button6, 0, 2, 6, 2)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()