import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Transporte Público - Aguascalientes")
ventana.geometry("600x500")
ventana.configure(bg="#f2f2f2")

# -------- FUNCIONES --------
def guardar_demanda():
    nombre = entry_nombre.get()
    ruta = entry_ruta.get()
    pasajeros = entry_pasajeros.get()
    horario = entry_horario.get()

    if nombre and ruta and pasajeros and horario:
        messagebox.showinfo("Registro exitoso", "Demanda registrada correctamente")
        limpiar_campos()
    else:
        messagebox.showwarning("Error", "Completa todos los campos")

def enviar_queja():
    texto = txt_quejas.get("1.0", tk.END)
    if texto.strip():
        messagebox.showinfo("Enviado", "Tu comentario fue enviado")
        txt_quejas.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Error", "Escribe una queja o sugerencia")

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_ruta.delete(0, tk.END)
    entry_pasajeros.delete(0, tk.END)
    entry_horario.delete(0, tk.END)

def salir():
    ventana.quit()

# -------- TITULO --------
titulo = tk.Label(
    ventana, 
    text="Sistema de Transporte Público", 
    font=("Arial", 16, "bold"), 
    bg="#f2f2f2",
    fg="#333"
)
titulo.pack(pady=10)

# -------- FRAME REGISTRO --------
frame_registro = tk.LabelFrame(
    ventana, 
    text="Registro de Demanda", 
    bg="#f2f2f2",
    fg="#333",
    padx=10, 
    pady=10
)
frame_registro.pack(padx=20, pady=10, fill="both")

tk.Label(frame_registro, text="Nombre:", bg="#f2f2f2").grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(frame_registro)
entry_nombre.grid(row=0, column=1)

tk.Label(frame_registro, text="Ruta:", bg="#f2f2f2").grid(row=1, column=0, sticky="w")
entry_ruta = tk.Entry(frame_registro)
entry_ruta.grid(row=1, column=1)

tk.Label(frame_registro, text="Pasajeros:", bg="#f2f2f2").grid(row=2, column=0, sticky="w")
entry_pasajeros = tk.Entry(frame_registro)
entry_pasajeros.grid(row=2, column=1)

tk.Label(frame_registro, text="Horario:", bg="#f2f2f2").grid(row=3, column=0, sticky="w")
entry_horario = tk.Entry(frame_registro)
entry_horario.grid(row=3, column=1)

btn_guardar = tk.Button(
    frame_registro, 
    text="Guardar", 
    command=guardar_demanda,
    bg="#cccccc"
)
btn_guardar.grid(row=4, column=0, pady=10)

btn_limpiar = tk.Button(
    frame_registro, 
    text="Limpiar", 
    command=limpiar_campos,
    bg="#cccccc"
)
btn_limpiar.grid(row=4, column=1)

# -------- FRAME RUTAS --------
frame_rutas = tk.LabelFrame(
    ventana, 
    text="Rutas y Horarios", 
    bg="#f2f2f2",
    fg="#333",
    padx=10, 
    pady=10
)
frame_rutas.pack(padx=20, pady=10, fill="both")

info_rutas = tk.Label(
    frame_rutas,
    text="Ruta 1: Centro - Norte | 6:00 - 22:00\n"
         "Ruta 2: Sur - Centro | 5:30 - 21:30\n"
         "Ruta 3: Oriente - Poniente | 6:15 - 22:15",
    bg="#f2f2f2",
    justify="left"
)
info_rutas.pack()

# -------- FRAME QUEJAS --------
frame_quejas = tk.LabelFrame(
    ventana, 
    text="Quejas y Sugerencias", 
    bg="#f2f2f2",
    fg="#333",
    padx=10, 
    pady=10
)
frame_quejas.pack(padx=20, pady=10, fill="both")

txt_quejas = tk.Text(frame_quejas, height=4)
txt_quejas.pack()

btn_enviar = tk.Button(
    frame_quejas, 
    text="Enviar", 
    command=enviar_queja,
    bg="#cccccc"
)
btn_enviar.pack(pady=5)

# -------- BOTON SALIR --------
btn_salir = tk.Button(
    ventana, 
    text="Salir", 
    command=salir,
    bg="#999999",
    fg="white"
)
btn_salir.pack(pady=10)

# Ejecutar ventana
ventana.mainloop()
