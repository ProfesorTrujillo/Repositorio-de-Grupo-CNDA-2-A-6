#importar la biblioteca de tkinter para crear interfaces gráficas
import tkinter as tk
from tkinter import ttk 
# ==========================================
# Ventana principal
# ==========================================
ventana = tk.Tk()
ventana.title("Sistema de Gestión para la Movilidad en Aguascalientes")
#entre comiillas va el titulo de la ventana, el tamaño de la ventana y el color de fondo
ventana.geometry("900x550")
ventana.configure(bg="#E4E0E0")

# Colores principales
color_header = "#D34492"
color_menu = "#D34492"
color_button = "#D34492"
color_content = "#FFFFFF"

# ==========================================
# Encabezado
# ==========================================
encabezado = tk.Frame(ventana, bg=color_header, height=70)
encabezado.pack(fill="x")

titulo = tk.Label(encabezado, text="CREACION DE CITAS", bg=color_header, fg="white", font=("Segoe UI", 20, "bold"))
titulo.place(x=20, y=15)

# ==========================================
# Menú lateral viene con relieve 
# ==========================================
menu = tk.Frame(ventana, bg=color_menu, width=200)
menu.pack(side="left", fill="y")

btn_dash = tk.Button(menu, text="Cancelacion de cita", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_dash.pack(fill="x", pady=8)

btn_ajustes = tk.Button(menu, text="Correccion de cita", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_ajustes.pack(fill="x", pady=8)

btn_ayuda = tk.Button(menu, text="consulta de cita", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_ayuda.pack(fill="x", pady=8)

# ==========================================
# Área de contenido
# ==========================================
contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True)

titulo_seccion = tk.Label(contenido, text="Por favor, complete los siguientes campos:", bg=color_content, fg="#333333", font=("Segoe UI", 16, "bold"))
titulo_seccion.place(x=30, y=20)

# ==========================================
# Widgets del formulario
# ==========================================

# Etiqueta + Entry
# Etiqueta + Entry
lbl_nombre = tk.Label(contenido, text="Nombre completo:", bg=color_content, font=("Segoe UI", 12))
lbl_nombre.place(x=30, y=80)

entrada_nombre = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_nombre.place(x=170, y=80)

# Etiqueta + Entry CURP
lbl_curp = tk.Label(contenido, text="CURP:", bg=color_content, font=("Segoe UI", 12))
lbl_curp.place(x=30, y=120)

entrada_curp = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_curp.place(x=120, y=120)
#ETIQUETA + ENTRY TELEFONO
lbl_telefono = tk.Label(contenido, text="Teléfono:", bg=color_content, font=("Segoe UI", 12))
lbl_telefono.place(x=30, y=200)

entrada_telefono = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_telefono.place(x=110, y=200)
#etiqueta + entry para la fecha de la cita
lbl_fecha =tk.Label(contenido, text="Fecha de la cita:", bg=color_content, font=("Segoe UI", 12))
lbl_fecha.place(x=30, y=160)

entrada_fecha = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_fecha.place(x=140, y=160)

# RadioButtons genero

# CheckButtons documentos para el tramite
lbl_documentos = tk.Label(contenido, text="Documentos para el tramite por favor marca" 
" los que ya tienes a tu disposicion:", bg=color_content, font=("Segoe UI", 12))
lbl_documentos.place(x=20, y=240)

chk1 = tk.Checkbutton(contenido, text="Curp", bg=color_content, font=("Segoe UI", 11))
chk1.place(x=120, y=270)

chk2 = tk.Checkbutton(contenido, text="Ine", bg=color_content, font=("Segoe UI", 11))
chk2.place(x=230, y=270)

chk3 = tk.Checkbutton(contenido, text="Comprobante de domicilio", bg=color_content, font=("Segoe UI", 11))
chk3.place(x=310, y=270)

# Botón principal
btn_guardar = tk.Button(contenido, text="Guardar Datos", bg=color_button, fg="white", font=("Segoe UI", 12, "bold"), width=20)
btn_guardar.place(x=300, y=420)

# ==========================================
ventana.mainloop()