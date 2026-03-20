import tkinter as tk
from tkinter import ttk

# ==========================================
# Ventana principal - Gestión de Citas 
# ==========================================
# Esta ventana simula una interfaz de escritorio para la Coordinación de Movilidad
# de Aguascalientes para gestionar citas de trámites.
ventana = tk.Tk()
ventana.title("Sistema de Gestión de Citas -  (Citas y Trámites)")
ventana.geometry("1376x768") #Configuramos directamente en pantalla completa para mayor comodidad del usuario
ventana.configure(bg="#F2F2F2") # Configuramos el fondo gris claro

# Definición de colores principales
# Colores que recuerdan al contexto institucional y de movilidad
color_header = "#E41DC3" 
color_menu = "#D423EB"   
color_button = "#A50F8C" 
color_content = "#FFFFFF" # Fondo blanco para el contenido principal
color_text_main = "#333333" # Color principal de texto

# ==========================================
# Encabezado (Header) 
# ==========================================
encabezado = tk.Frame(ventana, bg=color_header, height=75)
encabezado.pack(fill="x")

titulo = tk.Label(encabezado, text="SISTEMA DE GESTIÓN DE CITAS", bg=color_header, fg="white", font=("Segoe UI", 21, "bold"))
titulo.place(x=25, y=20)

# ==========================================
# Menú lateral (Navegación)
# ==========================================
menu = tk.Frame(ventana, bg=color_menu, width=220) # Ligeramente más ancho
menu.pack(side="left", fill="y")

# Botones de navegación con el nuevo esquema de colores
btn_dash = tk.Button(menu, text="Panel Resumen", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_dash.pack(fill="x", pady=10)

btn_citas = tk.Button(menu, text="Administrar Citas", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_citas.pack(fill="x", pady=10)

btn_servicios = tk.Button(menu, text="Configurar Servicios", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_servicios.pack(fill="x", pady=10)

btn_ayuda = tk.Button(menu, text="Ayuda", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 12))
btn_ayuda.pack(fill="x", pady=10)


# ==========================================
# Área de contenido principal
# ==========================================
contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True)

titulo_seccion = tk.Label(contenido, text="Registro de Nueva Cita", bg=color_content, fg=color_text_main, font=("Segoe UI", 18, "bold"))
titulo_seccion.place(x=35, y=25)

# ==========================================
# Widgets del formulario de cita
# ==========================================

# Etiqueta + Entry para el nombre del solicitante
lbl_nombre = tk.Label(contenido, text="Nombre Completo del Solicitante:", bg=color_content, font=("Segoe UI", 12))
lbl_nombre.place(x=35, y=85)

entrada_nombre = tk.Entry(contenido, width=40, font=("Segoe UI", 11))
entrada_nombre.place(x=290, y=85)

# Etiqueta + Entry para el teléfono o contacto
lbl_contacto = tk.Label(contenido, text="Teléfono o Correo de Contacto:", bg=color_content, font=("Segoe UI", 12))
lbl_contacto.place(x=35, y=125)

entrada_contacto = tk.Entry(contenido, width=40, font=("Segoe UI", 11))
entrada_contacto.place(x=290, y=125)

# RadioButtons para el tipo de servicio solicitado
lbl_servicio = tk.Label(contenido, text="Tipo de Servicio Solicitado:", bg=color_content, font=("Segoe UI", 12))
lbl_servicio.place(x=35, y=175)

# Variables y opciones para los RadioButtons
tipo_servicio = tk.StringVar()
rb_licencia = tk.Radiobutton(contenido, text="Licencias y Permisos", variable=tipo_servicio, value="licencia", bg=color_content, font=("Segoe UI", 11))
rb_licencia.place(x=260, y=175)

rb_verificacion = tk.Radiobutton(contenido, text="Verificación Vehicular", variable=tipo_servicio, value="verificacion", bg=color_content, font=("Segoe UI", 11))
rb_verificacion.place(x=440, y=175)

rb_multa = tk.Radiobutton(contenido, text="Multas e Impugnaciones", variable=tipo_servicio, value="multa", bg=color_content, font=("Segoe UI", 11))
rb_multa.place(x=630, y=175)

rb_placas = tk.Radiobutton(contenido, text="Alta/Baja Placas", variable=tipo_servicio, value="placas", bg=color_content, font=("Segoe UI", 11))
rb_placas.place(x=270, y=210)


# CheckButtons para la documentación presentada
lbl_documentos = tk.Label(contenido, text="Documentación Presentada (marque las que apliquen):", bg=color_content, font=("Segoe UI", 12))
lbl_documentos.place(x=35, y=255)

chk_ine = tk.Checkbutton(contenido, text="Identificación Oficial (INE)", bg=color_content, font=("Segoe UI", 11))
chk_ine.place(x=35, y=290)

chk_domicilio = tk.Checkbutton(contenido, text="Comprobante de Domicilio", bg=color_content, font=("Segoe UI", 11))
chk_domicilio.place(x=250, y=290)

chk_tarjeta = tk.Checkbutton(contenido, text="Tarjeta de Circulación (si aplica)", bg=color_content, font=("Segoe UI", 11))
chk_tarjeta.place(x=470, y=290)

chk_multa = tk.Checkbutton(contenido, text="Certificado de No Multas (si aplica)", bg=color_content, font=("Segoe UI", 11))
chk_multa.place(x=35, y=325)

# Caja de observaciones adicionales
lbl_observaciones = tk.Label(contenido, text="Detalles Adicionales y Observaciones:", bg=color_content, font=("Segoe UI", 12))
lbl_observaciones.place(x=35, y=370)

# Caja de texto para observaciones
caja_observaciones = tk.Text(contenido, width=65, height=8, font=("Segoe UI", 11), bd=2, relief="solid")
caja_observaciones.place(x=35, y=400)

# Botón principal para agendar la cita
btn_agendar = tk.Button(contenido, text="Agendar Cita ", bg=color_button, fg="white", font=("Segoe UI", 13, "bold"), width=25)
btn_agendar.place(x=600, y=520)

# ==========================================
# Fin de la estructura de la interfaz
# ==========================================
ventana.mainloop(0) # Bucle principal para mantener la ventana abierta