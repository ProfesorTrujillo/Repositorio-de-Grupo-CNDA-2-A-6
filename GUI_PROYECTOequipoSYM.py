import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
# Función guardar cita
# ==========================================
def guardar_cita():
    nombre = entrada_nombre.get()
    origen = entrada_origen.get()
    destino = entrada_destino.get()
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    transporte = tipo_transporte.get()

    if nombre == "" or origen == "" or destino == "":
        messagebox.showwarning("Error", "Completa los campos obligatorios")
    else:
        messagebox.showinfo("Registro exitoso",
                            f"Cita registrada:\n\nNombre: {nombre}\nOrigen: {origen}\nDestino: {destino}\nFecha: {fecha}\nHora: {hora}\nTransporte: {transporte}")

# ==========================================
# Ventana principal
# ==========================================
ventana = tk.Tk()
ventana.title("Sistema de Citas - Transporte Público")
ventana.geometry("900x550")
ventana.configure(bg="#EAEFF2")

# Colores
color_header = "#1DF7E8"
color_menu = "#358EED"
color_button = "#1EDD27"
color_content = "#1BF472"

# ==========================================
# Encabezado
# ==========================================
encabezado = tk.Frame(ventana, bg=color_header, height=70)
encabezado.pack(fill="x")

titulo = tk.Label(encabezado, text="Sistema de Registro de Citas de Transporte", bg=color_header, fg="white", font=("Segoe UI", 18, "bold"))
titulo.place(x=20, y=18)

# ==========================================
# Menú lateral
# ==========================================
menu = tk.Frame(ventana, bg=color_menu, width=200)
menu.pack(side="left", fill="y")

tk.Label(menu, text="MENÚ", bg=color_menu, fg="white", font=("Segoe UI", 14, "bold")).pack(pady=10)

tk.Button(menu, text="Registrar cita", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12)).pack(fill="x", pady=8)
tk.Button(menu, text="Ver citas", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12)).pack(fill="x", pady=8)
tk.Button(menu, text="Salir", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12), command=ventana.quit).pack(fill="x", pady=8)

# ==========================================
# Área de contenido
# ==========================================
contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True)

titulo_seccion = tk.Label(contenido, text="Registro de Nueva Cita", bg=color_content, fg="#333", font=("Segoe UI", 16, "bold"))
titulo_seccion.place(x=30, y=20)

# ==========================================
# Formulario
# ==========================================

# Nombre
tk.Label(contenido, text="Nombre:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=80)
entrada_nombre = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_nombre.place(x=150, y=80)

# Origen
tk.Label(contenido, text="Origen:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=120)
entrada_origen = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_origen.place(x=150, y=120)

# Destino
tk.Label(contenido, text="Destino:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=160)
entrada_destino = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_destino.place(x=150, y=160)

# Fecha
tk.Label(contenido, text="Fecha:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=200)
entrada_fecha = tk.Entry(contenido, width=20, font=("Segoe UI", 11))
entrada_fecha.place(x=150, y=200)

# Hora
tk.Label(contenido, text="Hora:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=240)
entrada_hora = tk.Entry(contenido, width=20, font=("Segoe UI", 11))
entrada_hora.place(x=150, y=240)

# Tipo de transporte
tk.Label(contenido, text="Transporte:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=280)

tipo_transporte = tk.StringVar()
combo = ttk.Combobox(contenido, textvariable=tipo_transporte, values=["Autobús", "Metro", "Taxi", "Combi"], state="readonly")
combo.place(x=150, y=280)
combo.current(0)

# Comentarios
tk.Label(contenido, text="Notas:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=320)
caja = tk.Text(contenido, width=50, height=5, font=("Segoe UI", 11))
caja.place(x=30, y=350)

# Botón guardar
btn_guardar = tk.Button(contenido, text="Guardar Cita", bg=color_button, fg="white", font=("Segoe UI", 12, "bold"), width=20, command=guardar_cita)
btn_guardar.place(x=300, y=460)

# ==========================================
ventana.mainloop()
