import pygtk 
import gtk
import gtk.glade
pygtk.require("2.0")
 
class Tventana : 
	def __init__(self):
		self.componentes = gtk.glade.XML("ventana.glade")
		
		self.ventana = self.componentes.get_widget("window1")
		self.ventana.show_all()

if __name__ == "__main__" :
	mi_ventana = Tventana()
	gtk.main()  