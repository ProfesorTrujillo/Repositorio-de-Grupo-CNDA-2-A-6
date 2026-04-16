import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import re, csv, os

# ==========================================
# Funciones
# ==========================================

folio_global = 1
archivo_citas = "citas.csv"
def obtener_ultimo_folio():
    if not os.path.exists(archivo_citas):
        return 1
    
    try:
        with open(archivo_citas, "r", encoding="utf-8") as f:
            lineas = list(csv.reader(f))
            if len(lineas) <= 1:
                return 1
            
            ultimo_folio_str = lineas[-1][0]
            numero = re.search(r"(\d+)", ultimo_folio_str)
            if numero:
                return int(numero.group(1)) + 1
    except Exception:
        return 1
    return 1

folio_global = obtener_ultimo_folio()
# Crear archivo si no existe
if not os.path.exists(archivo_citas):
    with open(archivo_citas, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Folio", "Nombre", "CURP", "Trámite", "Fecha", "Hora"])

def guardar_cita():
    global folio_global
    fecha = entrada_fecha.get()
    hora = combo_hora.get()
    tramite = combo_tramite.get()
    nombre = entrada_nombre.get()
    curp = entrada_curp.get()

    # Validaciones
    if not nombre or not tramite:
        messagebox.showwarning("Datos faltantes", "Por favor, completa el nombre y selecciona un trámite.")
        return
    if len(curp) != 18:
        messagebox.showwarning("CURP inválida", "La CURP debe tener exactamente 18 caracteres.")
        return
    if hora == "Seleccione hora" or not hora.strip():
        messagebox.showwarning("Hora faltante", "Por favor, selecciona una hora disponible.")
        return

    # Verificar duplicados (misma fecha y hora)
    with open(archivo_citas, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for fila in reader:
            if fila["Fecha"] == fecha and fila["Hora"] == hora:
                messagebox.showwarning("Horario ocupado", 
                    f"Ya existe una cita registrada en {fecha} a las {hora}.\nPor favor, seleccione otro horario.")
                return

    folio = f"FOL-{folio_global:04d}"
    folio_global += 1

    # Guardar en CSV
    with open(archivo_citas, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([folio, nombre, curp, tramite, fecha, hora])

    messagebox.showinfo("Cita Guardada",
        f"Hola {nombre},\n\nSu cita para '{tramite}' ha sido agendada.\nFecha: {fecha}\nHora: {hora}\nFolio: {folio}")

def cancelar_cita():
    folio = entrada_folio_cancelar.get()
    if not folio:
        messagebox.showwarning("Folio faltante", "Ingrese el folio de la cita a cancelar.")
        return

    citas = []
    encontrada = False
    with open(archivo_citas, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        encabezado = next(reader)
        for fila in reader:
            if fila[0] != folio:
                citas.append(fila)
            else:
                encontrada = True

    if encontrada:
        with open(archivo_citas, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(encabezado)
            writer.writerows(citas)
        messagebox.showinfo("Cancelación exitosa", f"La cita con folio {folio} ha sido cancelada.")
    else:
        messagebox.showwarning("No encontrada", f"No existe cita con folio {folio}.")

def consultar_cita():
    folio = entrada_folio_consultar.get()
    if not folio:
        messagebox.showwarning("Folio faltante", "Ingrese el folio de la cita a consultar.")
        return

    with open(archivo_citas, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for fila in reader:
         if fila["Folio"] == folio:
            mensaje = (
                f"Cita encontrada:\n\n"
                f"Nombre: {fila['Nombre']}\n"
                f"CURP: {fila['CURP']}\n"
                f"Hora: {fila['Fecha']}\n"
                f"Fecha: {fila['Trámite']}\n"
                f"Folio: {fila['Folio']}"

            )
            messagebox.showinfo("Consulta de cita", mensaje)
            return
    messagebox.showwarning("No encontrada", f"No existe cita con folio {folio}.")
def mostrar_pagina(nombre_pagina):
    for frame in paginas.values():
        frame.pack_forget()
    paginas[nombre_pagina].pack(fill="both", expand=True)

# ==========================================
# Ventana principal
# ==========================================
ventana = tk.Tk()
ventana.title("Sistema de Gestión para la Movilidad en Aguascalientes")
ventana.geometry("900x580")
ventana.configure(bg="#E4E0E0")

color_header = "#D65174"
color_menu = "#82C0D9"
color_button = "#D65174"
color_content = "#FFFFFF"

# Encabezado
encabezado = tk.Frame(ventana, bg=color_header, height=70)
encabezado.pack(fill="x")
titulo = tk.Label(encabezado, text="SISTEMA DE CITAS", bg=color_header, fg="white", font=("Segoe UI", 20, "bold"))
titulo.place(x=20, y=15)

# Menú lateral
menu = tk.Frame(ventana, bg=color_menu, width=200)
menu.pack(side="left", fill="y")

opciones_menu = ["Creación de cita", "Cancelación de cita", "Consulta de cita"]
paginas = {}

for opcion in opciones_menu:
    tk.Button(menu, text=opcion, bg=color_menu, fg="white", relief="flat",
              font=("Segoe UI", 12), activebackground="#096285",
              command=lambda o=opcion: mostrar_pagina(o)).pack(fill="x", pady=8)

# Área de contenido
contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True)

# --- Página: Creación de cita ---
pagina_creacion = tk.Frame(contenido, bg=color_content)
paginas["Creación de cita"] = pagina_creacion

tk.Label(pagina_creacion, text="Por favor, complete los campos:", bg=color_content,
         fg="#333333", font=("Segoe UI", 16, "bold")).place(x=30, y=20)

tk.Label(pagina_creacion, text="Nombre completo:", bg=color_content, font=("Segoe UI", 11)).place(x=30, y=70)
entrada_nombre = tk.Entry(pagina_creacion, width=40, font=("Segoe UI", 11))
entrada_nombre.place(x=180, y=70)

tk.Label(pagina_creacion, text="CURP:", bg=color_content, font=("Segoe UI", 11)).place(x=30, y=110)
entrada_curp = tk.Entry(pagina_creacion, width=25, font=("Segoe UI", 11))
entrada_curp.place(x=180, y=110)

lista_tramites = ["Licencia de Conducir (Nueva)", "Renovación de Licencia", "Cambio de Placas",
                  "Alta de Vehículo Nuevo", "Permiso de Transporte Público", "Permiso de Transporte Privado",
                  "Permiso de Transporte de Carga", "Baja de vehículo", "Reimpresión de Placas",
                  "Reimpresión de Licencia", "Reimpresión de Permiso", "Consulta de Multas", "Verificación Vehicular"]

tk.Label(pagina_creacion, text="Tipo de trámite:", bg=color_content, font=("Segoe UI", 11)).place(x=30, y=170)
combo_tramite = ttk.Combobox(pagina_creacion, values=lista_tramites, font=("Segoe UI", 11), width=37, state="readonly")
combo_tramite.place(x=180, y=170)
combo_tramite.set("Seleccione un trámite")

tk.Label(pagina_creacion, text="Fecha de la cita:", bg=color_content, font=("Segoe UI", 11)).place(x=30, y=210)
entrada_fecha = DateEntry(pagina_creacion, width=19, font=("Segoe UI", 11), background=color_header, 
                          foreground='white', date_pattern='dd/mm/yyyy', locale='es_ES', cursor="hand2")
entrada_fecha.place(x=180, y=210)

tk.Label(pagina_creacion, text="Hora de la cita:", bg=color_content, font=("Segoe UI", 11)).place(x=30, y=250)
horas_disponibles = ["8:00 AM", "8:30 AM", "9:00 AM", "9:30 AM", "10:00 AM", "10:30 AM", "11:00 AM", "11:30 AM", "12:00 PM", "12:30 PM"]
combo_hora = ttk.Combobox(pagina_creacion, values=horas_disponibles, font=("Segoe UI", 11), width=15, state="readonly")
combo_hora.place(x=180, y=250)
combo_hora.set("Seleccione hora")

btn_guardar = tk.Button(pagina_creacion, text="Guardar Datos", bg=color_button, fg="white",
                        font=("Segoe UI", 12, "bold"), width=20, cursor="hand2", command=guardar_cita)
btn_guardar.place(x=180, y=320)
btn_salir_crear = tk.Button(pagina_creacion, text="Salir", bg="#7E90F7", fg="white",
                        font=("Segoe UI", 12, "bold"), width=20, cursor="hand2", command=ventana.quit)
btn_salir_crear.place(x=180, y=370)

# --- Página: Cancelación de cita ---
pagina_cancelacion = tk.Frame(contenido, bg=color_content)
paginas["Cancelación de cita"] = pagina_cancelacion

tk.Label(pagina_cancelacion, text="Ingrese el folio de la cita a cancelar:", bg=color_content,
         fg="#333333", font=("Segoe UI", 16, "bold")).place(x=30, y=20)

tk.Label(pagina_cancelacion, text="Folio:", bg=color_content, font=("Segoe UI", 11)).place(x=30, y=70)
entrada_folio_cancelar = tk.Entry(pagina_cancelacion, width=40, font=("Segoe UI", 11))
entrada_folio_cancelar.place(x=180, y=70)

btn_cancelar = tk.Button(pagina_cancelacion, text="Cancelar Cita", bg=color_button, fg="white",
                         font=("Segoe UI", 12, "bold"), width=20, cursor="hand2", command=cancelar_cita)
btn_cancelar.place(x=180, y=120)
btn_salir_cancelar = tk.Button(pagina_cancelacion, text="Salir", bg="#7E90F7", fg="white",
                         font=("Segoe UI", 12, "bold"), width=20, cursor="hand2", command=ventana.quit)
btn_salir_cancelar.place(x=180, y=170)
# --- Página: Consulta de cita ---
pagina_consulta = tk.Frame(contenido, bg=color_content)
paginas["Consulta de cita"] = pagina_consulta

tk.Label(pagina_consulta, text="Ingrese el folio de la cita a consultar(Recuerde el folio se ingresa con FOL-000# siendo # tu número de cita):", bg=color_content,
         fg="#333333", font=("Segoe UI", 16, "bold")).place(x=30, y=20)

tk.Label(pagina_consulta, text="Folio:", bg=color_content, font=("Segoe UI", 11)).place(x=30, y=70)
entrada_folio_consultar = tk.Entry(pagina_consulta, width=40, font=("Segoe UI", 11))
entrada_folio_consultar.place(x=180, y=70)

btn_consultar = tk.Button(pagina_consulta, text="Consultar Cita", bg=color_button, fg="white",
                         font=("Segoe UI", 12, "bold"), width=20, cursor="hand2", command=consultar_cita)
btn_consultar.place(x=180, y=120)
btn_salir = tk.Button(pagina_consulta, text="Salir", bg="#7E90F7", fg="white",
                         font=("Segoe UI", 12, "bold"), width=20, cursor="hand2", command=ventana.quit)
btn_salir.place(x=180, y=170)

# Iniciar en la primera página
mostrar_pagina("Creación de cita")

ventana.mainloop()
