import tkinter as tk
from tkinter import messagebox
import random

# ==========================================
# Ventana principal
# ==========================================
ventana = tk.Tk()
ventana.title("Sistema de Quejas - Autobuses")
ventana.geometry("900x550")
ventana.configure(bg="#EAF4F4")

# Colores suaves
color_header = "#4A90E2"
color_menu = "#A7C7E7"
color_button = "#5DADE2"
color_content = "#FFFFFF"

# ==========================================
# Función generar folio
# ==========================================
def generar_folio():
    return f"FOL-{random.randint(1000,9999)}"

def guardar_queja():
    folio = generar_folio()
    messagebox.showinfo("Queja registrada", f"Tu queja fue registrada con folio:\n{folio}")
    
    # Limpiar campos
    entrada_nombre.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_ruta.delete(0, tk.END)
    caja_comentarios.delete("1.0", tk.END)

# ==========================================
# Encabezado
# ==========================================
encabezado = tk.Frame(ventana, bg=color_header, height=70)
encabezado.pack(fill="x")

titulo = tk.Label(encabezado, text="Sistema de Quejas - Servicio de Autobuses", 
                  bg=color_header, fg="white", font=("Segoe UI", 18, "bold"))
titulo.place(x=20, y=15)

# ==========================================
# Menú lateral
# ==========================================
menu = tk.Frame(ventana, bg=color_menu, width=200)
menu.pack(side="left", fill="y")

tk.Button(menu, text="Registrar Queja", bg=color_menu, fg="black", relief="flat",
          font=("Segoe UI", 12)).pack(fill="x", pady=10)

tk.Button(menu, text="Consultar Folio", bg=color_menu, fg="black", relief="flat",
          font=("Segoe UI", 12)).pack(fill="x", pady=10)

# ==========================================
# Área de contenido
# ==========================================
contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True)

titulo_seccion = tk.Label(contenido, text="Formulario de Quejas", 
                          bg=color_content, fg="#333", font=("Segoe UI", 16, "bold"))
titulo_seccion.place(x=30, y=20)

# ==========================================
# Formulario
# ==========================================

# Nombre
tk.Label(contenido, text="Nombre:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=80)
entrada_nombre = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_nombre.place(x=150, y=80)

# Correo
tk.Label(contenido, text="Correo:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=120)
entrada_correo = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_correo.place(x=150, y=120)

# Ruta del autobús
tk.Label(contenido, text="Ruta:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=160)
entrada_ruta = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_ruta.place(x=150, y=160)

# Tipo de queja
tk.Label(contenido, text="Tipo de queja:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=200)

tipo_queja = tk.StringVar()
tk.Radiobutton(contenido, text="Retraso", variable=tipo_queja, value="Retraso", bg=color_content).place(x=150, y=200)
tk.Radiobutton(contenido, text="Mal servicio", variable=tipo_queja, value="Mal servicio", bg=color_content).place(x=230, y=200)
tk.Radiobutton(contenido, text="Condiciones", variable=tipo_queja, value="Condiciones", bg=color_content).place(x=350, y=200)

# Comentarios
tk.Label(contenido, text="Descripción de la queja:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=250)

caja_comentarios = tk.Text(contenido, width=50, height=6, font=("Segoe UI", 11), bd=2)
caja_comentarios.place(x=30, y=280)

# Botón
tk.Button(contenido, text="Registrar Queja", bg=color_button, fg="white",
          font=("Segoe UI", 12, "bold"), width=20, command=guardar_queja).place(x=300, y=430)

# ==========================================
ventana.mainloop()
