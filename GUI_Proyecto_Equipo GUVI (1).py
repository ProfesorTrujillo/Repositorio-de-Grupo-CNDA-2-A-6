import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

# -------------------------------
# Colores estilo Aguascalientes
# -------------------------------
azul = "#1D4ED8"
azul_claro = "#DBEAFE"
rojo = "#DC2626"
blanco = "#FFFFFF"
gris = "#F1F5F9"
texto = "#1F2937"

# -------------------------------
# Ventana principal
# -------------------------------
ventana = tk.Tk()
ventana.title("Rutas YoVoy - Aguascalientes")
ventana.geometry("850x600")
ventana.configure(bg=gris)

# -------------------------------
# Barra superior
# -------------------------------
barra = tk.Frame(ventana, bg=azul, height=60)
barra.pack(fill="x")

titulo = tk.Label(
    barra,
    text="Rutas YoVoy",
    font=("Arial", 18, "bold"),
    bg=azul,
    fg=blanco
)
titulo.pack(pady=10)

# -------------------------------
# Subtítulo
# -------------------------------
subtitulo = tk.Label(
    ventana,
    text="Sistema de Transporte Público 🚍",
    font=("Arial", 12),
    bg=gris,
    fg=texto
)
subtitulo.pack(pady=5)

# -------------------------------
# Frame principal
# -------------------------------
frame_principal = tk.Frame(ventana, bg=blanco)
frame_principal.pack(padx=20, pady=10, fill="both", expand=True)

# -------------------------------
# Sección Usuario
# -------------------------------
frame_usuario = tk.LabelFrame(
    frame_principal,
    text="Datos del Usuario",
    bg=blanco,
    fg=azul,
    padx=10,
    pady=10
)
frame_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

tk.Label(frame_usuario, text="Nombre:", bg=blanco, fg=texto).grid(row=0, column=0, sticky="w")

entry_nombre = tk.Entry(frame_usuario, bg=azul_claro, bd=0)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

# -------------------------------
# Sección Ruta
# -------------------------------
frame_ruta = tk.LabelFrame(
    frame_principal,
    text="Información de Ruta",
    bg=blanco,
    fg=azul,
    padx=10,
    pady=10
)
frame_ruta.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

tk.Label(frame_ruta, text="Ruta:", bg=blanco, fg=texto).grid(row=0, column=0, sticky="w")

combo_ruta = ttk.Combobox(frame_ruta, values=["Ruta 1", "Ruta 2", "Ruta 3", "Ruta 4", "Ruta 5", "Ruta 6", "Ruta 7", "Ruta 8", "Ruta 9", "Ruta 11", "Ruta 12", "Ruta 14", "Ruta 16", "Ruta 18", "Ruta 19", "Ruta 23", "Ruta 24", "Ruta 25", "Ruta 27", "Ruta 28", "Ruta 29", "Ruta 30", "Ruta 34", "Ruta 35", "Ruta 36", "Ruta 37", "Ruta 38", "Ruta 39", "Ruta 42", "Ruta 45", "Ruta 46", "Ruta 48", "Ruta 50", "Ruta 51", "Ruta 50B", "Ruta UTR", "Ruta 52", "Ruta UP", "Ruta 43 Norte", "Ruta 43 Sur", "Ruta 10 Norte", "Ruta 10 Sur", "Ruta 40 Norte", "Ruta 40 Sur", "Ruta 20 Norte", "Ruta 20 Sur", "Ruta 41 Alameda", "Ruta 41 Penal", "Ruta 33", "Ruta 47"])
combo_ruta.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_ruta, text="Frecuencia:", bg=blanco, fg=texto).grid(row=1, column=0, sticky="w")

entry_frecuencia = tk.Entry(frame_ruta, bg=azul_claro, bd=0)
entry_frecuencia.grid(row=1, column=1, padx=5, pady=5)

# -------------------------------
# Sección Reporte
# -------------------------------
frame_reporte = tk.LabelFrame(
    frame_principal,
    text="Registrar Reporte",
    bg=blanco,
    fg=azul,
    padx=10,
    pady=10
)
frame_reporte.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

tk.Label(frame_reporte, text="Tipo:", bg=blanco, fg=texto).grid(row=0, column=0)

tipo_reporte = tk.StringVar()

radio1 = tk.Radiobutton(frame_reporte, text="Queja", variable=tipo_reporte, value="Queja", bg=blanco)
radio2 = tk.Radiobutton(frame_reporte, text="Incidencia", variable=tipo_reporte, value="Incidencia", bg=blanco)
radio3 = tk.Radiobutton(frame_reporte, text="Sugerencia", variable=tipo_reporte, value="Sugerencia", bg=blanco)

radio1.grid(row=0, column=1)
radio2.grid(row=0, column=2)
radio3.grid(row=0, column=3)

tk.Label(frame_reporte, text="Descripción:", bg=blanco, fg=texto).grid(row=1, column=0, sticky="nw")

texto_descripcion = ScrolledText(frame_reporte, width=50, height=5, bg="#F0F9FF", bd=0)
texto_descripcion.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# -------------------------------
# Opciones extra
# -------------------------------
frame_opciones = tk.Frame(frame_principal, bg=blanco)
frame_opciones.grid(row=2, column=0, columnspan=2, pady=10)

check1 = tk.Checkbutton(frame_opciones, text="Notificar por correo", bg=blanco)
check1.pack(side="left", padx=10)

check2 = tk.Checkbutton(frame_opciones, text="Marcar como urgente", bg=blanco)
check2.pack(side="left", padx=10)

# -------------------------------
# Botones
# -------------------------------
frame_botones = tk.Frame(frame_principal, bg=blanco)
frame_botones.grid(row=3, column=0, columnspan=2, pady=10)

btn_guardar = tk.Button(
    frame_botones,
    text="Guardar",
    bg=azul,
    fg=blanco,
    width=15,
    bd=0,
    activebackground="#1E40AF"
)
btn_guardar.pack(side="left", padx=10)

btn_cancelar = tk.Button(
    frame_botones,
    text="Cancelar",
    bg=rojo,
    fg=blanco,
    width=15,
    bd=0
)
btn_cancelar.pack(side="left", padx=10)

# -------------------------------
# Footer
# -------------------------------
footer = tk.Frame(ventana, bg=rojo, height=40)
footer.pack(fill="x")

tk.Label(
    footer,
    text="Aguascalientes • Transporte Inteligente",
    bg=rojo,
    fg=blanco,
    font=("Arial", 10)
).pack(pady=10)

# -------------------------------
# Ejecutar
# -------------------------------
ventana.mainloop()
