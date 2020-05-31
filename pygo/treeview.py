import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# List of Tuples (this is the model, aka the data that will be displayed
# on the tree view)
people= [("Bankole Esan", 99, "The Tech Lead"), 
         ("Jenny Blue", 21, "Shepherd"), 
         ("John Smith", 55, "Programmer"),
         ("Emma Anderson", 43, "Nurse"),
         ("Emily Wilson", 28, "Teacher")]

class MainWindow(Gtk.Window):
  def __init__(self): 
    Gtk.Window.__init__(self, title = "Window Title")
    layout = Gtk.Box()
    self.add(layout)

    # Convert data to ListStore (Lists that TreeViews can display)
    people_list_store = Gtk.ListStore(str, int, str)
    for item in people: 
      people_list_store.append(list(item))

    # for row in people_list_store:
    #   print(row[:]) # print all data as a row
    #   print(row[2]) # print data in the 3rd property

    # Treeview is the item that is displayed
    people_tree_view = Gtk.TreeView(people_list_store)

    for i, col_title in enumerate(["Name", "Age", "Profession"]):
      # Make a cell renderer - how to draw the data
      renderer = Gtk.CellRendererText()

      # create columns (title is column number)
      column = Gtk.TreeViewColumn(col_title, renderer, text=i)

      # Add column to Treeview
      people_tree_view.append_column(column)

    # Add TreeView to main layout
    layout.pack_start(people_tree_view, True, True, 0)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()