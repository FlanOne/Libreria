import tkinter as tk

class Boleta(tk.Tk):
    width = 700
    height = 500

    def __init__(self, boleta_id, items, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(f"Boleta {boleta_id}")
        self.configure(bg="white")

        self.boleta_label = tk.Label(self, text=f"Boleta {boleta_id}", font=("Arial", 16, "bold"), bg="white")
        self.boleta_label.pack(pady=20)

        item_frame = tk.Frame(self, bg="white")
        item_frame.pack()

        # Frame para el nombre del libro
        nombre_frame = tk.Frame(item_frame, bg="white")
        nombre_frame.pack(side=tk.LEFT, padx=10)

        nombre_title_label = tk.Label(nombre_frame, text="Nombre del Libro", font=("Arial", 12, "bold"), bg="white")
        nombre_title_label.pack(anchor="w")

        # Frame para la cantidad
        cantidad_frame = tk.Frame(item_frame, bg="white")
        cantidad_frame.pack(side=tk.LEFT, padx=10)

        cantidad_title_label = tk.Label(cantidad_frame, text="Cantidad", font=("Arial", 12, "bold"), bg="white")
        cantidad_title_label.pack(anchor="w")

        # Frame para el precio unitario
        precio_unitario_frame = tk.Frame(item_frame, bg="white")
        precio_unitario_frame.pack(side=tk.LEFT, padx=10)

        precio_unitario_title_label = tk.Label(precio_unitario_frame, text="Precio Unitario", font=("Arial", 12, "bold"), bg="white")
        precio_unitario_title_label.pack(anchor="w")

        # Frame para el subtotal
        subtotal_frame = tk.Frame(item_frame, bg="white")
        subtotal_frame.pack(side=tk.LEFT, padx=10)

        subtotal_title_label = tk.Label(subtotal_frame, text="Subtotal", font=("Arial", 12, "bold"), bg="white")
        subtotal_title_label.pack(anchor="w")

        total_books = 0  # Variable para almacenar la cantidad total de libros
        total_price = 0  # Variable para almacenar el precio total

        for item in items:
            libro_nombre = item["nombre"]
            cantidad = item["cantidad"]
            precio_unitario = item["precio_unitario"]

            libro_label = tk.Label(nombre_frame, text=libro_nombre, font=("Arial", 12), bg="white", anchor="w")
            libro_label.pack(fill=tk.X)

            cantidad_label = tk.Label(cantidad_frame, text=f"{cantidad}", font=("Arial", 12), bg="white")
            cantidad_label.pack()

            precio_unitario_label = tk.Label(precio_unitario_frame, text=f"${precio_unitario:.2f}", font=("Arial", 12), bg="white")
            precio_unitario_label.pack()

            subtotal = cantidad * precio_unitario
            subtotal_label = tk.Label(subtotal_frame, text=f"${subtotal:.2f}", font=("Arial", 12), bg="white")
            subtotal_label.pack()

            total_books += cantidad
            total_price += subtotal

        # Mostrar la cantidad de libros a llevar
        total_books_label = tk.Label(self, text=f"Cantidad de Libros: {total_books}", font=("Arial", 14, "bold"), bg="white")
        total_books_label.pack(pady=30)

        # Mostrar el monto total a pagar
        total_label = tk.Label(self, text=f"Total a Pagar: ${total_price:.2f}", font=("Arial", 14, "bold"), bg="white")
        total_label.pack(pady=20)

        self.aceptar_button = tk.Button(self, text="Aceptar", command=self.destroy)
        self.aceptar_button.pack(pady=20)

if __name__ == "__main__":
    items = [
        {"nombre": "Justin Bieber la bibliografía.", "cantidad": 1, "precio_unitario": 89.990},
        {"nombre": "BTS, su historia.", "cantidad": 1, "precio_unitario": 99.990},
        {"nombre": "No se tiene enemigos.", "cantidad": 3, "precio_unitario": 75.500}
    ]

    boleta = Boleta(36387272, items)
    boleta.geometry(f"{boleta.width}x{boleta.height}+500+200")  # Establecer tamaño y posición fija
    boleta.resizable(False, False)  # Deshabilitar el cambio de tamaño
    boleta.mainloop()
