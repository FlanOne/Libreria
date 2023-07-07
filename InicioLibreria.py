import customtkinter
from PIL import Image
import os
import MenuLibreria
import Conectar as sql

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    width = 500
    height = 560

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Sistema - Libreria del Vicho.py")
        self.iconbitmap("img/libro.ico")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # FONDO DE IMAGEN DE INTERFAZ
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/img/libros.jpg"), size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # PAGINA DE INICIO DE SESION DE USUARIO
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")

        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Libreria del Vicho\nInicio de Sesion", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.login_button = customtkinter.CTkButton(self.login_frame, text="Ingresar", command=lambda: self.login_event(sql.comprobarCliente(sql.agregarBoleta(sql.traerIdCliente(self.username_entry.get())), self.password_entry.get())), width=200)
        self.login_button.grid(row=4, column=0, padx=30, pady=(5, 5))

        self.register_button = customtkinter.CTkButton(self.login_frame, text="Registrarse", command=self.register_event, width=200)
        self.register_button.grid(row=5, column=0, padx=30, pady=(5, 5))

        # PAGINA DE REGISTRO DE USUARIO
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.main_label = customtkinter.CTkLabel(self.main_frame, text="Unete a Nuestro\nClub de Lectura", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))

        self.regNombre_entry = customtkinter.CTkEntry(self.main_frame, width=200, placeholder_text="Nombre")
        self.regNombre_entry.grid(row=1, column=0, padx=30, pady=(8, 8))

        self.regApellido_entry = customtkinter.CTkEntry(self.main_frame, width=200, placeholder_text="Apellido")
        self.regApellido_entry.grid(row=2, column=0, padx=30, pady=(8, 8))

        self.regFechaNac_entry = customtkinter.CTkEntry(self.main_frame, width=200, placeholder_text="Fecha de Nacimiento")
        self.regFechaNac_entry.grid(row=3, column=0, padx=30, pady=(8, 8))

        self.regDireccion_entry = customtkinter.CTkEntry(self.main_frame, width=200, placeholder_text="Dirección")
        self.regDireccion_entry.grid(row=4, column=0, padx=30, pady=(8, 8))

        self.regFono_entry = customtkinter.CTkEntry(self.main_frame, width=200, placeholder_text="Telefono")
        self.regFono_entry.grid(row=5, column=0, padx=30, pady=(8, 8))

        self.regCorreo_entry = customtkinter.CTkEntry(self.main_frame, width=200, placeholder_text="Correo")
        self.regCorreo_entry.grid(row=6, column=0, padx=30, pady=(8, 8))

        self.regPassword_entry = customtkinter.CTkEntry(self.main_frame, width=200, placeholder_text="Contraseña")
        self.regPassword_entry.grid(row=7, column=0, padx=30, pady=(8, 8))

        self.register_button = customtkinter.CTkButton(self.main_frame, text="Registrarse", command=lambda: sql.agregarCliente(self.regNombre_entry.get(),self.regApellido_entry.get(),self.regFechaNac_entry.get(),self.regDireccion_entry.get(), self.regFono_entry.get(), self.regCorreo_entry.get(), self.regPassword_entry.get()), width=200)
        self.register_button.grid(row=8, column=0, padx=30, pady=(5, 5))

        self.back_button = customtkinter.CTkButton(self.main_frame, text="Ya tengo una cuenta", command=self.back_event, width=200)
        self.back_button.grid(row=9, column=0, padx=30, pady=(5, 5))

        #self.login_button.getvar()

    # FUNCION DEL BOTON PARA LOGEO EN EL SISTEMA
    def login_event(self,value):
        a=value
        if a == True:
            self.destroy()
            b=MenuLibreria.App()
            b.mainloop()
            
            
    
    # FUNCION DEL BOTON PARA ACCEDER A REGISTRO DE NUEVO USUARIO
    def register_event(self):
        self.login_frame.grid_forget()
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    # FUNCION DEL BOTON PARA VOLVER A LA VENTANA ANTERIOR
    def back_event(self):
        self.main_frame.grid_forget()
        self.login_frame.grid(row=0, column=0, sticky="ns")

if __name__ == "__main__":

    app = App()
    app.mainloop()