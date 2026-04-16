import tkinter as tk
from tkinter import messagebox
import random

# ==========================================
# Base de datos (diccionario)
# ==========================================
quejas = {}

# ==========================================
# Ventana principal
# ==========================================
ventana = tk.Tk()
ventana.title("Sistema de Quejas - Autobuses")
ventana.geometry("900x550")
ventana.configure(bg="#EAF4F4")

# Colores
color_header = "#4A90E2"
color_menu = "#A7C7E7"
color_button = "#5DADE2"
color_content = "#FFFFFF"

# ==========================================
# Funciones
# ==========================================
def generar_folio():
    return f"FOL-{random.randint(1000,9999)}"

def guardar_queja():
    nombre = entrada_nombre.get()
    correo = entrada_correo.get()
    ruta = entrada_ruta.get()
    tipo = tipo_queja.get()
    comentario = caja_comentarios.get("1.0", tk.END).strip()

    if not nombre or not correo or not ruta or not tipo or not comentario:
        messagebox.showwarning("Error", "Completa todos los campos")
        return

    folio = generar_folio()

    # Guardar datos
    quejas[folio] = {
        "nombre": nombre,
        "correo": correo,
        "ruta": ruta,
        "tipo": tipo,
        "comentario": comentario
    }

    messagebox.showinfo("Queja registrada", f"Folio generado:\n{folio}")

    # Limpiar
    entrada_nombre.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_ruta.delete(0, tk.END)
    caja_comentarios.delete("1.0", tk.END)

# ==========================================
# RECURSIVIDAD
# ==========================================
def buscar_folio_recursivo(lista, folio, indice=0):
    # Caso base: no encontrado
    if indice >= len(lista):
        return None

    # Caso base: encontrado
    if lista[indice][0] == folio:
        return lista[indice][1]

    # Llamada recursiva
    return buscar_folio_recursivo(lista, folio, indice + 1)

# ==========================================
# CONSULTAR FOLIO
# ==========================================
def consultar_folio():
    ventana_consulta = tk.Toplevel()
    ventana_consulta.title("Consultar Folio")
    ventana_consulta.geometry("400x350")

    tk.Label(ventana_consulta, text="Ingresa tu folio:").pack(pady=10)

    entrada_folio = tk.Entry(ventana_consulta)
    entrada_folio.pack(pady=5)

    resultado = tk.Text(ventana_consulta, height=12, width=40)
    resultado.pack(pady=10)

    def buscar():
        folio = entrada_folio.get()
        resultado.delete("1.0", tk.END)

        lista = list(quejas.items())
        datos = buscar_folio_recursivo(lista, folio)

        if datos:
            info = f"""
Nombre: {datos['nombre']}
Correo: {datos['correo']}
Ruta: {datos['ruta']}
Tipo: {datos['tipo']}
Comentario: {datos['comentario']}
"""
            resultado.insert(tk.END, info)
        else:
            resultado.insert(tk.END, "Folio no encontrado")

    tk.Button(ventana_consulta, text="Buscar", command=buscar).pack()

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

tk.Button(menu, text="Registrar Queja", bg=color_menu, fg="black",
          relief="flat", font=("Segoe UI", 12)).pack(fill="x", pady=10)

tk.Button(menu, text="Consultar Folio", bg=color_menu, fg="black",
          relief="flat", font=("Segoe UI", 12),
          command=consultar_folio).pack(fill="x", pady=10)

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
tk.Label(contenido, text="Nombre:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=80)
entrada_nombre = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_nombre.place(x=150, y=80)

tk.Label(contenido, text="Correo:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=120)
entrada_correo = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_correo.place(x=150, y=120)

tk.Label(contenido, text="Ruta:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=160)
entrada_ruta = tk.Entry(contenido, width=30, font=("Segoe UI", 11))
entrada_ruta.place(x=150, y=160)

tk.Label(contenido, text="Tipo de queja:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=200)

tipo_queja = tk.StringVar()
tk.Radiobutton(contenido, text="Retraso", variable=tipo_queja, value="Retraso", bg=color_content).place(x=150, y=200)
tk.Radiobutton(contenido, text="Mal servicio", variable=tipo_queja, value="Mal servicio", bg=color_content).place(x=230, y=200)
tk.Radiobutton(contenido, text="Condiciones", variable=tipo_queja, value="Condiciones", bg=color_content).place(x=350, y=200)

tk.Label(contenido, text="Descripción de la queja:", bg=color_content, font=("Segoe UI", 12)).place(x=30, y=250)

caja_comentarios = tk.Text(contenido, width=50, height=6, font=("Segoe UI", 11), bd=2)
caja_comentarios.place(x=30, y=280)

tk.Button(contenido, text="Registrar Queja", bg=color_button, fg="white",
          font=("Segoe UI", 12, "bold"), width=20,
          command=guardar_queja).place(x=300, y=430)

# ==========================================
ventana.mainloop()
