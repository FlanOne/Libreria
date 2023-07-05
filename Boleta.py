import tkinter as tk

class Boleta(tk.Tk):
    width = 600
    height = 700

    def __init__(self, boleta_id, items, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(f"Boleta {boleta_id}")
        self.configure(bg="white")

        self.boleta_label = tk.Label(self, text=f"Boleta {boleta_id}", font=("Arial", 16, "bold"), bg="white")
        self.boleta_label.pack(pady=20)

        for item in items:
            libro_nombre = item["nombre"]
            cantidad = item["cantidad"]
            precio_unitario = item["precio_unitario"]

            item_frame = tk.Frame(self, bg="white")
            item_frame.pack()

            # Frame para el nombre del libro
            nombre_frame = tk.Frame(item_frame, bg="white")
            nombre_frame.pack(side=tk.LEFT, padx=10)

            libro_label = tk.Label(nombre_frame, text=f"Libro: {libro_nombre}", font=("Arial", 12), bg="white", anchor="w")
            libro_label.pack()

            # Frame para la cantidad
            cantidad_frame = tk.Frame(item_frame, bg="white")
            cantidad_frame.pack(side=tk.LEFT, padx=10)

            cantidad_label = tk.Label(cantidad_frame, text=f"Cantidad: {cantidad}", font=("Arial", 12), bg="white")
            cantidad_label.pack()

            # Frame para el precio unitario
            precio_frame = tk.Frame(item_frame, bg="white")
            precio_frame.pack(side=tk.LEFT, padx=10)

            precio_label = tk.Label(precio_frame, text=f"Precio Unitario: {precio_unitario}", font=("Arial", 12), bg="white")
            precio_label.pack()

if __name__ == "__main__":
    items = [
        {"nombre": "Harry Potter", "cantidad": 2, "precio_unitario": 10.99},
        {"nombre": "El Gran Gatsby", "cantidad": 1, "precio_unitario": 15.99},
        {"nombre": "Cien años de soledad", "cantidad": 3, "precio_unitario": 12.99}
    ]

    boleta = Boleta(36387272, items)
    boleta.geometry(f"{boleta.width}x{boleta.height}+500+200")  # Establecer tamaño y posición fija
    boleta.resizable(False, False)  # Deshabilitar el cambio de tamaño
    boleta.mainloop()
