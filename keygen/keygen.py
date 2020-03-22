from gi.repository import Gtk
import gi

gi.require_version("Gtk", "3.0")

win = Gtk.Window()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
