"""
1. donde se creara un menu para gestionar las concesiones, permisos e incidencias ciudadanas.
2. se podra agregar, eliminar y listar las concesiones, permisos e incidencias ciudadanas.
3. se podra actualizar el estado de las incidencias ciudadanas.
"""
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
# Funciones de interfaz
# ==========================================
def limpiar_contenido():
    for widget in frame_dinamico.winfo_children():
        widget.destroy()

def mostrar_opciones(tipo, items):
    limpiar_contenido()
    
    tk.Label(frame_dinamico, text=f"Gestión de {tipo.capitalize()}s", bg=color_content, fg=color_text, 
             font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 15))
    
    frame_botones = tk.Frame(frame_dinamico, bg=color_content)
    frame_botones.pack(fill="x", pady=10)
    
    tk.Button(frame_botones, text="✚ Agregar", bg=color_button_add, fg="white", font=("Segoe UI", 11, "bold"),
             command=lambda: mostrar_formulario_agregar(tipo, items), relief="raised", cursor="hand2").pack(side="left", padx=5)
    
    tk.Button(frame_botones, text="🗑️ Eliminar", bg=color_button_delete, fg="white", font=("Segoe UI", 11, "bold"),
             command=lambda: mostrar_formulario_eliminar(tipo, items), relief="raised", cursor="hand2").pack(side="left", padx=5)
    
    tk.Button(frame_botones, text="📋 Listar", bg=color_menu, fg="white", font=("Segoe UI", 11, "bold"),
             command=lambda: mostrar_listado(tipo, items), relief="raised", cursor="hand2").pack(side="left", padx=5)
    
    if tipo == "incidencia":
        tk.Button(frame_botones, text="🔄 Actualizar Estado", bg=color_button, fg="white", font=("Segoe UI", 11, "bold"),
                 command=lambda: mostrar_formulario_actualizar(), relief="raised", cursor="hand2").pack(side="left", padx=5)

def mostrar_formulario_agregar(tipo, items):
    limpiar_contenido()
    
    tk.Label(frame_dinamico, text=f"Agregar {tipo.capitalize()}", bg=color_content, fg=color_text, 
             font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 15))
    
    frame_form = tk.Frame(frame_dinamico, bg=color_content)
    frame_form.pack(fill="x", pady=10)
    
    tk.Label(frame_form, text="ID:", bg=color_content, fg=color_text, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(10, 5))
    entrada_id = tk.Entry(frame_form, font=("Segoe UI", 11), width=40, bd=2, relief="solid")
    entrada_id.pack(fill="x", pady=(0, 10))
    
    tk.Label(frame_form, text="Nombre:", bg=color_content, fg=color_text, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(10, 5))
    entrada_nombre = tk.Entry(frame_form, font=("Segoe UI", 11), width=40, bd=2, relief="solid")
    entrada_nombre.pack(fill="x", pady=(0, 10))
    
    tk.Label(frame_form, text="Descripción:", bg=color_content, fg=color_text, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(10, 5))
    entrada_desc = tk.Text(frame_form, font=("Segoe UI", 11), width=40, height=4, bd=2, relief="solid")
    entrada_desc.pack(fill="x", pady=(0, 10))
    
    def guardar():
        id_val = entrada_id.get().strip()
        nombre = entrada_nombre.get().strip()
        desc = entrada_desc.get("1.0", "end").strip()
        
        if not id_val or not nombre or not desc:
            messagebox.showerror("Error", "Todos los campos son requeridos")
            return
        
        msg = agregar_item(items, tipo, id_val, nombre, desc)
        messagebox.showinfo("Éxito", msg)
        mostrar_opciones(tipo, items)
    
    frame_botones = tk.Frame(frame_dinamico, bg=color_content)
    frame_botones.pack(fill="x", pady=20)
    
    tk.Button(frame_botones, text="💾 Guardar", bg=color_button_add, fg="white", font=("Segoe UI", 11, "bold"),
             command=guardar, relief="raised", cursor="hand2", padx=20).pack(side="left", padx=5)
    
    tk.Button(frame_botones, text="◀ Volver", bg="#95A5A6", fg="white", font=("Segoe UI", 11, "bold"),
             command=lambda: mostrar_opciones(tipo, items), relief="raised", cursor="hand2", padx=20).pack(side="left", padx=5)

def mostrar_formulario_eliminar(tipo, items):
    limpiar_contenido()
    
    tk.Label(frame_dinamico, text=f"Eliminar {tipo.capitalize()}", bg=color_content, fg=color_text, 
             font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 15))
    
    frame_form = tk.Frame(frame_dinamico, bg=color_content)
    frame_form.pack(fill="x", pady=10)
    
    tk.Label(frame_form, text="ID del {tipo} a eliminar:", bg=color_content, fg=color_text, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(10, 5))
    entrada_id = tk.Entry(frame_form, font=("Segoe UI", 11), width=40, bd=2, relief="solid")
    entrada_id.pack(fill="x", pady=(0, 10))
    
    def eliminar():
        id_val = entrada_id.get().strip()
        if not id_val:
            messagebox.showerror("Error", "Ingrese un ID")
            return
        msg = eliminar_item(items, tipo, id_val)
        messagebox.showinfo("Resultado", msg)
        mostrar_opciones(tipo, items)
    
    frame_botones = tk.Frame(frame_dinamico, bg=color_content)
    frame_botones.pack(fill="x", pady=20)
    
    tk.Button(frame_botones, text="🗑️ Eliminar", bg=color_button_delete, fg="white", font=("Segoe UI", 11, "bold"),
             command=eliminar, relief="raised", cursor="hand2", padx=20).pack(side="left", padx=5)
    
    tk.Button(frame_botones, text="◀ Volver", bg="#95A5A6", fg="white", font=("Segoe UI", 11, "bold"),
             command=lambda: mostrar_opciones(tipo, items), relief="raised", cursor="hand2", padx=20).pack(side="left", padx=5)

def mostrar_listado(tipo, items):
    limpiar_contenido()
    
    tk.Label(frame_dinamico, text=f"Listado de {tipo.capitalize()}s", bg=color_content, fg=color_text, 
             font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 15))
    
    texto_listado = scrolledtext.ScrolledText(frame_dinamico, font=("Courier", 10), width=70, height=15, 
                                              bd=2, relief="solid", bg="white", fg=color_text)
    texto_listado.pack(fill="both", expand=True, pady=10)
    
    contenido_lista = listar_items(items, tipo)
    texto_listado.insert("1.0", contenido_lista)
    texto_listado.config(state="disabled")
    
    frame_botones = tk.Frame(frame_dinamico, bg=color_content)
    frame_botones.pack(fill="x", pady=10)
    
    tk.Button(frame_botones, text="◀ Volver", bg="#95A5A6", fg="white", font=("Segoe UI", 11, "bold"),
             command=lambda: mostrar_opciones(tipo, items), relief="raised", cursor="hand2", padx=20).pack(side="left", padx=5)

def mostrar_formulario_actualizar():
    limpiar_contenido()
    
    tk.Label(frame_dinamico, text="Actualizar Estado de Incidencia", bg=color_content, fg=color_text, 
             font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=(0, 15))
    
    frame_form = tk.Frame(frame_dinamico, bg=color_content)
    frame_form.pack(fill="x", pady=10)
    
    tk.Label(frame_form, text="ID de la incidencia:", bg=color_content, fg=color_text, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(10, 5))
    entrada_id = tk.Entry(frame_form, font=("Segoe UI", 11), width=40, bd=2, relief="solid")
    entrada_id.pack(fill="x", pady=(0, 10))
    
    tk.Label(frame_form, text="Nuevo estado:", bg=color_content, fg=color_text, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(10, 5))
    estado_var = tk.StringVar(value="Pendiente")
    
    frame_estados = tk.Frame(frame_form, bg=color_content)
    frame_estados.pack(fill="x", pady=(0, 10))
    
    tk.Radiobutton(frame_estados, text="Pendiente", variable=estado_var, value="Pendiente", bg=color_content, 
                  fg=color_text, font=("Segoe UI", 10)).pack(anchor="w", pady=5)
    tk.Radiobutton(frame_estados, text="En Proceso", variable=estado_var, value="En Proceso", bg=color_content, 
                  fg=color_text, font=("Segoe UI", 10)).pack(anchor="w", pady=5)
    tk.Radiobutton(frame_estados, text="Resuelta", variable=estado_var, value="Resuelta", bg=color_content, 
                  fg=color_text, font=("Segoe UI", 10)).pack(anchor="w", pady=5)
    
    def actualizar():
        id_val = entrada_id.get().strip()
        if not id_val:
            messagebox.showerror("Error", "Ingrese un ID")
            return
        estado = estado_var.get()
        msg = actualizar_estado_incidencia(id_val, estado)
        messagebox.showinfo("Resultado", msg)
        mostrar_opciones("incidencia", incidencias)
    
    frame_botones = tk.Frame(frame_dinamico, bg=color_content)
    frame_botones.pack(fill="x", pady=20)
    
    tk.Button(frame_botones, text="🔄 Actualizar", bg=color_button, fg="white", font=("Segoe UI", 11, "bold"),
             command=actualizar, relief="raised", cursor="hand2", padx=20).pack(side="left", padx=5)
    
    tk.Button(frame_botones, text="◀ Volver", bg="#95A5A6", fg="white", font=("Segoe UI", 11, "bold"),
             command=lambda: mostrar_opciones("incidencia", incidencias), relief="raised", cursor="hand2", padx=20).pack(side="left", padx=5)

# ==========================================
ventana.mainloop()
