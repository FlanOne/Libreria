import tkinter
import tkinter.messagebox
import customtkinter
import os
from tkinter import*
from tkinter import ttk
from PIL import ImageTk, Image
import Conectar as sql
import InicioLibreria

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    width = 1310
    height = 900

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.libro = []
        masVendidos = sql.LibrosMasVendidos()
        masNuevos = sql.LibrosMasNuevos()
        masValorados = sql.librosMasValorados()

        print(masVendidos[0][0])

        # configure window
        self.title("Sistema - Librería VIMABE.py")
        self.iconbitmap("img/libro.ico")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        #FRAME 1 #####################################################################################################################
        self.frame_bloque1_info = customtkinter.CTkFrame(master=self)
        self.frame_bloque1_info.grid(row=0, column=0, columnspan=2, rowspan=1, pady=5, padx=10, sticky="nsew")

        self.frame_bloque1_info.rowconfigure(0, weight=0)
        self.frame_bloque1_info.columnconfigure(0, weight=1)

        self.frame_bloque1_label = customtkinter.CTkLabel(master=self.frame_bloque1_info, text="Libro más vendidos")
        self.frame_bloque1_label.grid(row=1, column=0, pady=2, padx=10, sticky="w")

        self.frame_bloque1_infoA = customtkinter.CTkFrame(master=self.frame_bloque1_info)
        self.frame_bloque1_infoA.grid(row=2, column=0, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        #######################################################
        self.frame1_bloque1_libros1 = customtkinter.CTkFrame(master=self.frame_bloque1_infoA)
        self.frame1_bloque1_libros1.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")
        self.current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masVendidos[0][2]), size=(150,200))
        
        self.btn = customtkinter.CTkButton(self.frame1_bloque1_libros1, image=self.bg_image, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masVendidos[0][0]))))
        self.btn.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)
        
        

        self.frame1_bloque1_libros2 = customtkinter.CTkFrame(master=self.frame_bloque1_infoA)
        self.frame1_bloque1_libros2.grid(row=0, column=1, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image2 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masVendidos[1][2]), size=(150,200))
        
        self.btn2 = customtkinter.CTkButton(self.frame1_bloque1_libros2, image=self.bg_image2, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masVendidos[1][0]))))
        self.btn2.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

        self.frame1_bloque1_libros3 = customtkinter.CTkFrame(master=self.frame_bloque1_infoA)
        self.frame1_bloque1_libros3.grid(row=0, column=2, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image3 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masVendidos[2][2]), size=(150,200))
        
        self.btn3 = customtkinter.CTkButton(self.frame1_bloque1_libros3, image=self.bg_image3, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masVendidos[2][0]))))
        self.btn3.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

        self.frame1_bloque1_libros4 = customtkinter.CTkFrame(master=self.frame_bloque1_infoA)
        self.frame1_bloque1_libros4.grid(row=0, column=3, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image4 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masVendidos[3][2]), size=(150,200))
        
        self.btn4 = customtkinter.CTkButton(self.frame1_bloque1_libros4, image=self.bg_image4, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masVendidos[3][0]))))
        self.btn4.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)


        #FRAME 2 #####################################################################################################################
        self.frame_bloque2_info = customtkinter.CTkFrame(master=self)
        self.frame_bloque2_info.grid(row=1, column=0, columnspan=2, rowspan=1, pady=5, padx=10, sticky="nsew")

        self.frame_bloque2_info.rowconfigure(0, weight=0)
        self.frame_bloque2_info.columnconfigure(0, weight=1)

        self.frame_bloque2_label = customtkinter.CTkLabel(master=self.frame_bloque2_info, text="Ultimos lanzamientos")
        self.frame_bloque2_label.grid(row=0, column=0, pady=2, padx=10, sticky="w")

        self.frame_bloque2_infoA = customtkinter.CTkFrame(master=self.frame_bloque2_info)
        self.frame_bloque2_infoA.grid(row=1, column=0, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        #######################################################
        self.frame2_bloque2_libros1 = customtkinter.CTkFrame(master=self.frame_bloque2_infoA)
        self.frame2_bloque2_libros1.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image5 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masNuevos[0][2]), size=(150,200))
        
        self.btn5 = customtkinter.CTkButton(self.frame2_bloque2_libros1, image=self.bg_image5, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masNuevos[0][0]))))
        self.btn5.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

        self.frame2_bloque2_libros2 = customtkinter.CTkFrame(master=self.frame_bloque2_infoA)
        self.frame2_bloque2_libros2.grid(row=0, column=1, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image6 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masNuevos[1][2]), size=(150,200))
        
        self.btn6 = customtkinter.CTkButton(self.frame2_bloque2_libros2, image=self.bg_image6, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masNuevos[1][0]))))
        self.btn6.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

        self.frame2_bloque2_libros3 = customtkinter.CTkFrame(master=self.frame_bloque2_infoA)
        self.frame2_bloque2_libros3.grid(row=0, column=2, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image7 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masNuevos[2][2]), size=(150,200))
        
        self.btn7 = customtkinter.CTkButton(self.frame2_bloque2_libros3, image=self.bg_image7, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masNuevos[2][0]))))
        self.btn7.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

        self.frame2_bloque2_libros4 = customtkinter.CTkFrame(master=self.frame_bloque2_infoA)
        self.frame2_bloque2_libros4.grid(row=0, column=3, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image8 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masNuevos[3][2]), size=(150,200))
        
        self.btn8 = customtkinter.CTkButton(self.frame2_bloque2_libros4, image=self.bg_image8, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masNuevos[3][0]))))
        self.btn8.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)


        #FRAME 3 #####################################################################################################################
        self.frame_bloque3_info = customtkinter.CTkFrame(master=self)
        self.frame_bloque3_info.grid(row=2, column=0, columnspan=2, rowspan=1, pady=5, padx=10, sticky="nsew")

        self.frame_bloque3_info.rowconfigure(0, weight=0)
        self.frame_bloque3_info.columnconfigure(0, weight=1)

        self.frame_bloque3_label = customtkinter.CTkLabel(master=self.frame_bloque3_info, text="Libro más valorados")
        self.frame_bloque3_label.grid(row=0, column=0, pady=2, padx=10, sticky="w")

        self.frame_bloque3_infoA = customtkinter.CTkFrame(master=self.frame_bloque3_info)
        self.frame_bloque3_infoA.grid(row=1, column=0, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        #######################################################
        self.frame3_bloque3_libros1 = customtkinter.CTkFrame(master=self.frame_bloque3_infoA)
        self.frame3_bloque3_libros1.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image9 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masValorados[0][2]), size=(150,200))
        
        self.btn9 = customtkinter.CTkButton(self.frame3_bloque3_libros1, image=self.bg_image9, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masValorados[0][0]))))
        self.btn9.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

        self.frame3_bloque3_libros2 = customtkinter.CTkFrame(master=self.frame_bloque3_infoA)
        self.frame3_bloque3_libros2.grid(row=0, column=1, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image10 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masValorados[1][2]), size=(150,200))
        
        self.btn10 = customtkinter.CTkButton(self.frame3_bloque3_libros2, image=self.bg_image10, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masValorados[1][0]))))
        self.btn10.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

        self.frame3_bloque3_libros3 = customtkinter.CTkFrame(master=self.frame_bloque3_infoA)
        self.frame3_bloque3_libros3.grid(row=0, column=2, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image11 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masValorados[2][2]), size=(150,200))
        
        self.btn11 = customtkinter.CTkButton(self.frame3_bloque3_libros3, image=self.bg_image11, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masValorados[2][0]))))
        self.btn11.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

        self.frame3_bloque3_libros4 = customtkinter.CTkFrame(master=self.frame_bloque3_infoA)
        self.frame3_bloque3_libros4.grid(row=0, column=3, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.bg_image12 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+masValorados[3][2]), size=(150,200))
        
        self.btn12 = customtkinter.CTkButton(self.frame3_bloque3_libros4, image=self.bg_image12, text = "datos", command=lambda : self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(masValorados[3][0]))))
        self.btn12.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

        #FRAME 4 #####################################################################################################################
        self.frame_bloque4_info = customtkinter.CTkFrame(master=self)
        self.frame_bloque4_info.grid(row=0, column=2, columnspan=2, rowspan=4, pady=5, padx=10, sticky="nsew")

        self.frame_bloque4_info.rowconfigure(0, weight=0)
        self.frame_bloque4_info.columnconfigure(0, weight=1)

        self.entry_busqueda = customtkinter.CTkEntry(master=self.frame_bloque4_info, placeholder_text="Buscar libro...")
        self.entry_busqueda.grid(row=0, column=0, columnspan=1, padx=5, pady=5, sticky="nsew")

        self.button_busqueda = customtkinter.CTkButton(master=self.frame_bloque4_info, text="Buscar", command=lambda: self.InsertarLibro(self.cambiarVariable(sql.buscadorNombreIsbn(self.entry_busqueda.get()))) )
        self.button_busqueda.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        #######################################################
        self.frame_bloque4_label = customtkinter.CTkLabel(master=self.frame_bloque4_info, text="Informacion del libro encontrado")
        self.frame_bloque4_label.grid(row=2, column=0, pady=2, padx=10, sticky="w")

        self.frame_bloque4_infoA = customtkinter.CTkFrame(master=self.frame_bloque4_info)
        self.frame_bloque4_infoA.grid(row=3, column=0, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.frame_bloque4_infoA1 = customtkinter.CTkFrame(master=self.frame_bloque4_infoA)
        self.frame_bloque4_infoA1.grid(row=1, column=0, columnspan=1, rowspan=1, pady=2, padx=2, sticky="nsew")

        self.textbox_frame_bloque4 = customtkinter.CTkTextbox(self.frame_bloque4_infoA, width=350, height=220)
        self.textbox_frame_bloque4.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")
        self.textbox_frame_bloque4.insert("0.0", "Sinopsis\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

        #self.ValoracionLibro = customtkinter.CTkOptionMenu(master=self.frame_bloque4_infoA, values=["Calificar", "1", "2", "3", "4", "5"])
        #self.ValoracionLibro.grid(row=3, column=0, pady=5, padx=5, sticky="nsew")
        #self.ValoracionLibro.set("Calificar")

        self.IdLibro_entry = customtkinter.CTkEntry(self.frame_bloque4_infoA, width=350, placeholder_text="ISBN")
        self.IdLibro_entry.grid(row=4, column=0, padx=30, pady=5)

        self.TituloLibro_entry = customtkinter.CTkEntry(self.frame_bloque4_infoA, width=350, placeholder_text="Titulo")
        self.TituloLibro_entry.grid(row=0, column=0, padx=30, pady=5)

        self.CantidadLibro_entry = customtkinter.CTkEntry(self.frame_bloque4_infoA, width=350, placeholder_text="Cantidad")
        self.CantidadLibro_entry.grid(row=5, column=0, padx=30, pady=5)

        self.AutorLibro_entry = customtkinter.CTkEntry(self.frame_bloque4_infoA, width=350, placeholder_text="Autor")
        self.AutorLibro_entry.grid(row=6, column=0, padx=30, pady=5)

        self.PrecioLibro_entry = customtkinter.CTkEntry(self.frame_bloque4_infoA, width=350, placeholder_text="Precio")
        self.PrecioLibro_entry.grid(row=7, column=0, padx=30, pady=5)

        ##Btn Añadir.
        self.button_anadirLibro = customtkinter.CTkButton(master=self.frame_bloque4_infoA, text="Añadir")
        self.button_anadirLibro.grid(row=8, column=0, padx=5, pady=7, sticky="nsew")

        ##Btn Comprar.
        self.button_comprarLibro = customtkinter.CTkButton(master=self.frame_bloque4_infoA, text="Comprar")
        self.button_comprarLibro.grid(row=9, column=0, padx=5, pady=5, sticky="nsew")

    def cambiarVariable(self, rows):
        a = rows
        return a
        

    def InsertarLibro(self, a):
        self.TituloLibro_entry.delete(0,"end")
        self.IdLibro_entry.delete(0,"end")
        self.CantidadPublLibro_entry.delete(0,"end") ##Se cambió fecha a Cantidad.
        self.AutorLibro_entry.delete(0,"end")
        self.PrecioLibro_entry.delete(0,"end")
        self.textbox_frame_bloque4.delete("0.0","end")


        self.TituloLibro_entry.insert(0, str(a[0][2]))
        self.textbox_frame_bloque4.insert("0.0", str(a[0][5]))
        self.IdLibro_entry.insert(0, str(a[0][0]))
        self.CantidadPublLibro_entry.insert(0, str(a[0][3])) ##Se cambió fecha a Cantidad.
        self.AutorLibro_entry.insert(0, str(a[0][7]))
        self.PrecioLibro_entry.insert(0, str(a[0][4]))

        self.bg_image13 = customtkinter.CTkImage(Image.open(self.current_path +"/imagenes/"+a[0][9]), size=(150,200))
        
        self.btn13 = customtkinter.CTkButton(self.frame_bloque4_infoA1, image=self.bg_image13, text = "")
        self.btn13.grid(row=0, column=0, columnspan=1, rowspan=1, pady=2, padx=2)

if __name__ == "__main__":
    app = App()
    app.mainloop()