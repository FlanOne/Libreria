import tkinter as tk

class App(tk.Tk):
    width = 500
    height = 400

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(f"Boleta")
        self.configure(bg="white")

        self.boleta_label = tk.Label(self, text=f"Boleta ", font=("Arial", 16, "bold"), bg="white")
        self.boleta_label.pack(pady=20)

        item_frame = tk.Frame(self, bg="white")
        item_frame.pack()



if __name__ == "__main__":
    items = [
        {"nombre": "Harry Potter", "cantidad": 2, "precio_unitario": 10.99},
        {"nombre": "El Gran Gatsby", "cantidad": 1, "precio_unitario": 15.99},
        {"nombre": "Cien años de soledad", "cantidad": 3, "precio_unitario": 12.99}
    ]

    
    

    boleta = App()
    boleta.geometry(f"{boleta.width}x{boleta.height}+500+200")  # Establecer tamaño y posición fija
    boleta.resizable(False, False)  # Deshabilitar el cambio de tamaño
    boleta.mainloop()
