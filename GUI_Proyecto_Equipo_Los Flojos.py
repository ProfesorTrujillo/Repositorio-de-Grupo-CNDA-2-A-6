import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# ==========================================
# Clases de datos
# ==========================================
class Item:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}"

class Incidencia(Item):
    def __init__(self, id, descripcion, estado='Pendiente'):
        super().__init__(id, descripcion, descripcion)
        self.estado = estado

    def __str__(self):
        return f"ID: {self.id}, Descripción: {self.descripcion}, Estado: {self.estado}"

# ==========================================
# Base de datos en memoria
# ==========================================
concesiones = []
permisos = []
incidencias = []

# ==========================================
# Funciones de gestión
# ==========================================
def agregar_item(items, tipo, id_val, nombre, descripcion):
    item = Item(id_val, nombre, descripcion) if tipo != "incidencia" else Incidencia(id_val, descripcion)
    items.append(item)
    return f"{tipo.capitalize()} agregado exitosamente."

def eliminar_item(items, tipo, id_val):
    for item in items:
        if item.id == id_val:
            items.remove(item)
            return f"{tipo.capitalize()} eliminado exitosamente."
    return f"{tipo.capitalize()} no encontrado."

def listar_items(items, tipo):
    if not items:
        return f"No hay {tipo}s registradas."
    else:
        return "\n".join(str(item) for item in items)

def actualizar_estado_incidencia(id_val, nuevo_estado):
    for i in incidencias:
        if i.id == id_val:
            i.estado = nuevo_estado
            return "Estado actualizado exitosamente."
    return "Incidencia no encontrada."

# ==========================================
# Ventana principal
# ==========================================
ventana = tk.Tk()
ventana.title("Gestión de Concesiones, Permisos e Incidencias")
ventana.geometry("1000x650")
ventana.configure(bg="#2C3E50")

# Colores principales - Paleta profesional y armoniosa
color_header = "#34495E"
color_menu = "#3498DB"
color_menu_hover = "#2980B9"
color_button = "#E74C3C"
color_button_add = "#27AE60"
color_button_delete = "#E67E22"
color_content = "#ECF0F1"
color_text = "#2C3E50"

# ==========================================
# Encabezado
# ==========================================
encabezado = tk.Frame(ventana, bg=color_header, height=80)
encabezado.pack(fill="x")

titulo = tk.Label(encabezado, text="Sistema de Gestión Ciudadana", bg=color_header, fg="white", font=("Segoe UI", 24, "bold"))
titulo.pack(pady=15)

subtitulo = tk.Label(encabezado, text="Concesiones • Permisos • Incidencias", bg=color_header, fg="#BDC3C7", font=("Segoe UI", 11))
subtitulo.pack()

# ==========================================
# Menú lateral
# ==========================================
menu = tk.Frame(ventana, bg=color_menu, width=220)
menu.pack(side="left", fill="y", padx=0)

tk.Label(menu, text="GESTIONAR", bg=color_menu, fg="white", font=("Segoe UI", 12, "bold")).pack(fill="x", pady=(15, 10), padx=15)

def crear_boton_menu(texto, comando):
    btn = tk.Button(menu, text=texto, bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 11),
                    command=comando, activebackground=color_menu_hover, activeforeground="white", 
                    cursor="hand2", padx=15, pady=12)
    btn.pack(fill="x", padx=5, pady=5)
    return btn

btn_concesiones = crear_boton_menu("📋 Concesiones", lambda: mostrar_opciones("concesion", concesiones))
btn_permisos = crear_boton_menu("📄 Permisos", lambda: mostrar_opciones("permiso", permisos))
btn_incidencias = crear_boton_menu("⚠️ Incidencias", lambda: mostrar_opciones("incidencia", incidencias))

tk.Label(menu, text="", bg=color_menu).pack(pady=20)

btn_salir = tk.Button(menu, text="🚪 Salir", bg="#C0392B", fg="white", relief="flat", font=("Segoe UI", 11),
                      command=ventana.quit, activebackground="#A93226", activeforeground="white",
                      cursor="hand2", padx=15, pady=12)
btn_salir.pack(fill="x", padx=5, pady=5)

# ==========================================
# Área de contenido
# ==========================================
contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True, padx=20, pady=20)

titulo_seccion = tk.Label(contenido, text="Bienvenido", bg=color_content, fg=color_text, font=("Segoe UI", 18, "bold"))
titulo_seccion.pack(anchor="w", pady=(0, 20))

mensaje_inicio = tk.Label(contenido, text="Selecciona una opción del menú para comenzar", bg=color_content, fg="#7F8C8D", font=("Segoe UI", 12))
mensaje_inicio.pack(anchor="w")

# Frame para los widgets dinámicos
frame_dinamico = tk.Frame(contenido, bg=color_content)
frame_dinamico.pack(fill="both", expand=True, pady=10)



# ==========================================
ventana.mainloop()
