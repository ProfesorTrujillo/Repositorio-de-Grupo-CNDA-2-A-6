# Sistema YoVoy - Tkinter (versión mejorada)

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import re
import csv

reportes = []
folio = 1

rutas = {"Ruta 1": "Margaritas - Vicente Guerrero",
    "Ruta 2": "Jardin Carpio - Los Cactus",
    "Ruta 3": "La Ribera - UAA Sur",
    "Ruta 4": "Jesus Maria - Terminal sur",
    "Ruta 5": "La Ribera - Vicente Guerrero",
    "Ruta 6": "Terminal Sur - Jesus Maria",
    "Ruta 7": "Jardin de Zaragoza - Las Palmas",
    "Ruta 8": "Rivero y Gutierrez - UTMA",
    "Ruta 9": "Los Laureles - Cumbres III - Terminal Sur",
    "Ruta 10": "Paseos de Aguascalientes - UAA Sur",
    "Ruta 11": "Chichimeco - Terminal Sur",
    "Ruta 12": "Lunaria - Vicente Guerrero",
    "Ruta 14": "Vicente Guerrero - Lomas de Vista Bella",
    "Ruta 16": "Bellavista - Hacienda Nueva",
    "Ruta 18": "Lunaria - UAA",
    "Ruta 19": "Pocitos - Vistas de Oriente",
    "Ruta 20N": "Terminal Oriente",
    "Ruta 20S": "Terminal Oriente - Av. de la Convención de 1914",
    "Ruta 23": "Los Arquitos - Villa Montaña",
    "Ruta 24": "Los Negritos -Vistas de Oriente",
    "Ruta 25": "Las Palmas - Vistas de Oriente",
    "Ruta 27": "Los Cactus - Av. Fundición - Vicente Guerrero",
    "Ruta 28": "Chichimeco - Valentin Gomez Farias - Terminal Sur",
    "Ruta 29": "Lunaria - Av. Paseo de Ojocaliente - Jardin de Zaragoza",
    "Ruta 30": "Martinez Dominguez,- Villa Montaña",
    "Ruta 33": "Jesus Maria - Av. Universidad - Terminal Sur",
    "Ruta 34": "Universidad Politecnica de Aguascalientes - Villa Montaña",
    "Ruta 35": "Lunaria - Universidad Autonoma de Aguascalientes",
    "Ruta 36": "Mercado Teran - Lunaria",
    "Ruta 37": "Hacienda San Marcos - UTMA",
    "Ruta 38": "Paso Blanco - Vicente Guerrero",
    "Ruta 39": "Jardin de Zaragoza  - El Conejal",
    "Ruta 40N": "Terminal Oriente",
    "Ruta 40S": "Terminal Oriente",
    "Ruta 41 Penal": "Terminal Oriente - Universidad Tecnologica de Aguascalientes",
    "Ruta 41 Alameda": "Terminal Oriente - EATON",
    "Ruta 45": "Centro - Peñuelas",
    "Ruta 46": "Centro - Pocitos",
    "Ruta 48": "Centro - Insurgentes",
    "Ruta 50": "Universidad Tecnologica de Aguascalientes ",
    "Ruta 51": "Centro - Cañada Honda",
    "Ruta 50B": "Jesus Maria - Universidad Tecnologica de Aguascalientes)",
    "Ruta UTR": "Av. Siglo XXI - Universidad Tecnológica El Retoño",
    "Ruta 52": "Centro - Norias de Paso Hondo",
    "Ruta UP": "Centro - Universidad Politecnica de Aguaascalientes",
    "Ruta 43 Norte": "Centro - Ojocaliente Norte",
    "Ruta 43 Sur": "Villas del Puertecito - Ojocaliente Sur",
    "Ruta 10 Norte": "Centro - VNSA Norte",
    "Ruta 10 Sur": "Centro - VNSA Sur",
    "Ruta 33": "Centro - Ojocaliente",
    "Ruta 47": "Centro - Villas del Sur"
}

root = tk.Tk()
root.title("Sistema YoVoy")
root.geometry("950x560")
root.resizable(False, False)

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# =======================
# PESTAÑA REGISTRO
# =======================

registro_tab = tk.Frame(notebook)
notebook.add(registro_tab, text="Registrar reporte")

contenedor = tk.Frame(registro_tab)
contenedor.pack(fill="both", padx=10, pady=10)

# ---------- DATOS USUARIO ----------

frame_usuario = tk.LabelFrame(contenedor, text="Datos del usuario")
frame_usuario.grid(row=0, column=0, padx=10, pady=5, sticky="n")

nombre_entry = tk.Entry(frame_usuario, width=25)
correo_entry = tk.Entry(frame_usuario, width=25)
folio_var = tk.StringVar(value="REP-0001")


tk.Label(frame_usuario, text="Nombre").grid(row=0, column=0, sticky="w")
nombre_entry.grid(row=0, column=1)


tk.Label(frame_usuario, text="Correo").grid(row=1, column=0, sticky="w")
correo_entry.grid(row=1, column=1)


tk.Label(frame_usuario, text="Folio").grid(row=2, column=0, sticky="w")
tk.Entry(frame_usuario, textvariable=folio_var, state="readonly", width=22).grid(row=2, column=1)

# ---------- RUTA ----------

frame_ruta = tk.LabelFrame(contenedor, text="Ruta")
frame_ruta.grid(row=0, column=1, padx=10, pady=5, sticky="n")

ruta_combo = ttk.Combobox(frame_ruta, values=list(rutas.keys()), width=30)
ruta_combo.pack(padx=10, pady=5)

recorrido_text = tk.Text(frame_ruta, height=2, width=35, state="disabled")
recorrido_text.pack(padx=10, pady=5)

def mostrar_recorrido(event=None):
    ruta = ruta_combo.get()
    recorrido = rutas.get(ruta, "")

    recorrido_text.config(state="normal")
    recorrido_text.delete("1.0", tk.END)
    recorrido_text.insert(tk.END, recorrido)
    recorrido_text.config(state="disabled")

ruta_combo.bind("<<ComboboxSelected>>", mostrar_recorrido)

# ---------- TIPO ----------

frame_tipo = tk.LabelFrame(registro_tab, text="Tipo de reporte")
frame_tipo.pack(fill="x", padx=10, pady=5)

tipo_var = tk.StringVar(value="Queja")

tk.Radiobutton(frame_tipo, text="Queja", variable=tipo_var, value="Queja").pack(side="left", padx=10)
tk.Radiobutton(frame_tipo, text="Incidencia", variable=tipo_var, value="Incidencia").pack(side="left", padx=10)
tk.Radiobutton(frame_tipo, text="Sugerencia", variable=tipo_var, value="Sugerencia").pack(side="left", padx=10)

# ---------- UNIDAD ----------

frame_unidad = tk.Frame(registro_tab)
frame_unidad.pack(fill="x", padx=10)

tk.Label(frame_unidad, text="Unidad de transporte").pack(side="left")
unidad_entry = tk.Entry(frame_unidad, width=20)
unidad_entry.pack(side="left", padx=10)

# ---------- DESCRIPCIÓN ----------

frame_desc = tk.LabelFrame(registro_tab, text="Descripción")
frame_desc.pack(fill="both", padx=10, pady=5)

texto_desc = tk.Text(frame_desc, height=5)
texto_desc.pack(fill="both", padx=5, pady=5)

# ---------- VALIDACIÓN ----------

def validar_email(correo):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, correo)

# ---------- CONFIRMAR ----------

def ir_confirmacion():

    if nombre_entry.get() == "":
        messagebox.showerror("Error", "Ingrese su nombre")
        return

    if not validar_email(correo_entry.get()):
        messagebox.showerror("Error", "Correo inválido")
        return

    if ruta_combo.get() == "":
        messagebox.showerror("Error", "Seleccione una ruta")
        return

    resumen.set(
        f"Folio: {folio_var.get()}\n"
        f"Nombre: {nombre_entry.get()}\n"
        f"Correo: {correo_entry.get()}\n"
        f"Ruta: {ruta_combo.get()}\n"
        f"Tipo: {tipo_var.get()}\n"
        f"Unidad: {unidad_entry.get()}\n\n"
        f"Descripción:\n{texto_desc.get('1.0', tk.END)}"
    )

    notebook.select(confirm_tab)

boton_confirmar = tk.Button(registro_tab, text="Confirmar reporte", bg="#2d5be3", fg="white", command=ir_confirmacion)
boton_confirmar.pack(pady=5)

# =======================
# CONFIRMAR
# =======================

confirm_tab = tk.Frame(notebook)
notebook.add(confirm_tab, text="Confirmar reporte")

resumen = tk.StringVar()

frame_resumen = tk.LabelFrame(confirm_tab, text="Verifique los datos antes de guardar")
frame_resumen.pack(fill="both", expand=True, padx=20, pady=20)

label_resumen = tk.Label(frame_resumen, textvariable=resumen, justify="left")
label_resumen.pack(padx=10, pady=10, anchor="w")

# ---------- GUARDAR ----------

def guardar_reporte():

    global folio

    datos = {
        "folio": folio_var.get(),
        "nombre": nombre_entry.get(),
        "correo": correo_entry.get(),
        "ruta": ruta_combo.get(),
        "tipo": tipo_var.get(),
        "unidad": unidad_entry.get(),
        "descripcion": texto_desc.get("1.0", tk.END)
    }

    reportes.append(datos)

    tabla.insert("", "end", values=(
        datos["folio"],
        datos["nombre"],
        datos["ruta"],
        datos["tipo"]
    ))

    folio += 1
    folio_var.set(f"REP-{folio:04}")

    messagebox.showinfo("Guardado", "Reporte registrado correctamente")

    nombre_entry.delete(0, tk.END)
    correo_entry.delete(0, tk.END)
    unidad_entry.delete(0, tk.END)
    texto_desc.delete("1.0", tk.END)

    notebook.select(registro_tab)


tk.Button(confirm_tab, text="Guardar reporte", bg="green", fg="white", command=guardar_reporte).pack(pady=10)

# =======================
# REPORTES
# =======================

reportes_tab = tk.Frame(notebook)
notebook.add(reportes_tab, text="Reportes registrados")

# BUSCADOR

buscador_frame = tk.Frame(reportes_tab)
buscador_frame.pack(fill="x", padx=10, pady=5)

tk.Label(buscador_frame, text="Buscar folio:").pack(side="left")

buscar_entry = tk.Entry(buscador_frame, width=20)
buscar_entry.pack(side="left", padx=5)


def buscar():

    folio_buscar = buscar_entry.get()

    for item in tabla.get_children():
        tabla.delete(item)

    for r in reportes:
        if folio_buscar.lower() in r["folio"].lower():
            tabla.insert("", "end", values=(
                r["folio"], r["nombre"], r["ruta"], r["tipo"]
            ))


tk.Button(buscador_frame, text="Buscar", command=buscar).pack(side="left", padx=5)

# TABLA

columnas = ("Folio", "Nombre", "Ruta", "Tipo")


tabla = ttk.Treeview(reportes_tab, columns=columnas, show="headings", height=14)

for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, width=200)


tabla.pack(fill="both", expand=True, padx=10, pady=10)

# EXPORTAR CSV

def exportar_csv():

    if not reportes:
        messagebox.showwarning("Vacío", "No hay reportes")
        return

    archivo = filedialog.asksaveasfilename(defaultextension=".csv")

    with open(archivo, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow(["Folio","Nombre","Correo","Ruta","Tipo","Unidad","Descripción"])

        for r in reportes:
            writer.writerow([
                r["folio"],
                r["nombre"],
                r["correo"],
                r["ruta"],
                r["tipo"],
                r["unidad"],
                r["descripcion"]
            ])

    messagebox.showinfo("Exportado", "Archivo CSV guardado")


tk.Button(reportes_tab, text="Exportar a CSV", command=exportar_csv).pack(pady=5)

# =======================
# CONFIG
# =======================

config_tab = tk.Frame(notebook)
notebook.add(config_tab, text="Configuración")

label_config = tk.Label(config_tab, text="Panel de configuración del sistema", font=("Arial", 14))
label_config.pack(pady=40)

# =======================
# ESTADÍSTICAS
# =======================

stats_tab = tk.Frame(notebook)
notebook.add(stats_tab, text="Estadísticas")

stats_text = tk.Text(stats_tab, height=20)
stats_text.pack(fill="both", expand=True, padx=10, pady=10)


def generar_estadisticas():

    conteo = {}

    for r in reportes:
        ruta = r["ruta"]
        conteo[ruta] = conteo.get(ruta, 0) + 1

    stats_text.delete("1.0", tk.END)

    stats_text.insert(tk.END, "Quejas por ruta:\n\n")

    for ruta, cantidad in conteo.items():
        stats_text.insert(tk.END, f"{ruta} : {cantidad} reportes\n")


tk.Button(stats_tab, text="Generar estadísticas", command=generar_estadisticas).pack(pady=5)

root.mainloop()
