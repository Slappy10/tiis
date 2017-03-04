import pygtk 
import gtk
import gtk.glade
pygtk.require("2.0")
 
class Tventana : 
	def __init__(self):
		self.ventana = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.ventana.show()

if __name__ == "__main__" :
	mi_ventana = Tventana()
	gtk.main()  