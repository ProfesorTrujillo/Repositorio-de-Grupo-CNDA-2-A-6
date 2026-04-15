import tkinter as tk
from tkinter import ttk, messagebox

# ================= COLORES  =================
BG = "#EEF2F7"
SIDEBAR = "#0F2A44"
CARD = "white"
TEXT = "black"

root = tk.Tk()
root.title("Dashboard UTA")
root.geometry("1200x700")
root.config(bg=BG)

usuario_actual = ""
usuarios_registrados = {}  # Diccionario para guardar usuarios

# ================= PLACEHOLDER =================
def placeholder(entry, texto):
    entry.insert(0, texto)
    entry.config(fg="gray")

    def on_focus_in(e):
        if entry.get() == texto:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(e):
        if entry.get() == "":
            entry.insert(0, texto)
            entry.config(fg="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# ================= CAMBIAR VISTA =================
def mostrar(frame):
    for f in (login_frame, registro_frame, home_frame, tramites_frame, citas_frame):
        f.pack_forget()
    frame.pack(fill="both", expand=True)

# =========================================================
#  LOGIN
# =========================================================
login_frame = tk.Frame(root, bg=BG)

tk.Label(login_frame, text="Iniciar Sesión",
         font=("Segoe UI", 24, "bold"),
         bg=BG).pack(pady=30)

entry_user = tk.Entry(login_frame, width=30)
entry_user.pack(pady=5)
placeholder(entry_user, "Usuario")

entry_id = tk.Entry(login_frame, width=30)
entry_id.pack(pady=5)
placeholder(entry_id, "CURP o ID")

entry_mail = tk.Entry(login_frame, width=30)
entry_mail.pack(pady=5)
placeholder(entry_mail, "Correo electrónico")

def login():
    global usuario_actual

    user = entry_user.get()
    user_id = entry_id.get()
    mail = entry_mail.get()

    if (user in ["", "Usuario"] or
        user_id in ["", "CURP o ID"] or
        mail in ["", "Correo electrónico"]):
        messagebox.showerror("Error", "Llena todos los campos")
        return

    # Verificar si el usuario existe
    if user in usuarios_registrados:
        datos = usuarios_registrados[user]
        if datos["curp"] == user_id and datos["correo"] == mail:
            usuario_actual = f"{datos['nombre']} | ID: {user_id}"
            label_user_home.config(text=usuario_actual)
            mostrar(home_frame)
        else:
            messagebox.showerror("Error", "CURP/ID o correo incorrectos")
    else:
        messagebox.showerror("Error", "Usuario no encontrado. ¿Ya tienes una cuenta?")

tk.Button(login_frame, text="Entrar",
          bg="#2563EB", fg="white",
          width=20,
          command=login).pack(pady=10)

tk.Button(login_frame, text="Crear cuenta",
          bg="#16A34A", fg="white",
          width=20,
          command=lambda: mostrar(registro_frame)).pack(pady=5)

# =========================================================
#  REGISTRO
# =========================================================
registro_frame = tk.Frame(root, bg=BG)

tk.Label(registro_frame, text="Crear Cuenta",
         font=("Segoe UI", 24, "bold"),
         bg=BG).pack(pady=30)

tk.Label(registro_frame, text="Completa todos los campos para registrarte",
         font=("Segoe UI", 11),
         bg=BG, fg="gray").pack(pady=5)

form_reg = tk.Frame(registro_frame, bg=BG)
form_reg.pack(pady=10)

# Nombre completo
tk.Label(form_reg, text="Nombre completo:", bg=BG,
         font=("Segoe UI", 11)).grid(row=0, column=0, sticky="e", padx=10, pady=8)
entry_reg_nombre = tk.Entry(form_reg, width=30)
entry_reg_nombre.grid(row=0, column=1, pady=8)
placeholder(entry_reg_nombre, "Ingresa tu nombre completo")

# Usuario
tk.Label(form_reg, text="Usuario:", bg=BG,
         font=("Segoe UI", 11)).grid(row=1, column=0, sticky="e", padx=10, pady=8)
entry_reg_user = tk.Entry(form_reg, width=30)
entry_reg_user.grid(row=1, column=1, pady=8)
placeholder(entry_reg_user, "Elige un nombre de usuario")

# CURP o ID
tk.Label(form_reg, text="CURP o ID:", bg=BG,
         font=("Segoe UI", 11)).grid(row=2, column=0, sticky="e", padx=10, pady=8)
entry_reg_curp = tk.Entry(form_reg, width=30)
entry_reg_curp.grid(row=2, column=1, pady=8)
placeholder(entry_reg_curp, "Ingresa tu CURP o ID")

# Correo
tk.Label(form_reg, text="Correo electrónico:", bg=BG,
         font=("Segoe UI", 11)).grid(row=3, column=0, sticky="e", padx=10, pady=8)
entry_reg_mail = tk.Entry(form_reg, width=30)
entry_reg_mail.grid(row=3, column=1, pady=8)
placeholder(entry_reg_mail, "Ingresa tu correo electrónico")

def crear_cuenta():
    nombre = entry_reg_nombre.get()
    user = entry_reg_user.get()
    curp = entry_reg_curp.get()
    mail = entry_reg_mail.get()

    placeholders = ["Ingresa tu nombre completo", "Elige un nombre de usuario",
                    "Ingresa tu CURP o ID", "Ingresa tu correo electrónico"]

    if (nombre in ["", placeholders[0]] or
        user in ["", placeholders[1]] or
        curp in ["", placeholders[2]] or
        mail in ["", placeholders[3]]):
        messagebox.showerror("Error", "Por favor llena todos los campos")
        return

    if user in usuarios_registrados:
        messagebox.showerror("Error", "Ese nombre de usuario ya existe")
        return

    # Guardar usuario
    usuarios_registrados[user] = {
        "nombre": nombre,
        "curp": curp,
        "correo": mail
    }

    # Limpiar campos
    for entry, ph in zip(
        [entry_reg_nombre, entry_reg_user, entry_reg_curp, entry_reg_mail],
        placeholders
    ):
        entry.delete(0, tk.END)
        entry.insert(0, ph)
        entry.config(fg="gray")

    messagebox.showinfo("Éxito", f"Cuenta creada correctamente.\nYa puedes iniciar sesión con el usuario: {user}")
    mostrar(login_frame)

tk.Button(form_reg, text="Crear cuenta",
          bg="#16A34A", fg="white",
          width=20,
          command=crear_cuenta).grid(row=4, column=1, pady=15)

tk.Button(form_reg, text="← Volver al inicio de sesión",
          bg=BG, fg="#2563EB",
          bd=0,
          command=lambda: mostrar(login_frame)).grid(row=5, column=1, pady=5)

# =========================================================
# SIDEBAR
# =========================================================
def crear_sidebar(parent):
    sidebar = tk.Frame(parent, bg=SIDEBAR, width=250)
    sidebar.pack(side="left", fill="y")

    tk.Label(sidebar, text="UTA\nTI", fg="white", bg=SIDEBAR,
             font=("Segoe UI", 18, "bold")).pack(pady=30)

    tk.Button(sidebar, text="Home", fg="white", bg=SIDEBAR,
              bd=0, command=lambda: mostrar(home_frame)).pack(fill="x", pady=5)

    tk.Button(sidebar, text="Trámites", fg="white", bg=SIDEBAR,
              bd=0, command=lambda: mostrar(tramites_frame)).pack(fill="x", pady=5)

    tk.Button(sidebar, text="Citas", fg="white", bg=SIDEBAR,
              bd=0, command=lambda: mostrar(citas_frame)).pack(fill="x", pady=5)

    tk.Button(sidebar, text="Cerrar sesión", fg="#FF6B6B", bg=SIDEBAR,
              bd=0, command=lambda: mostrar(login_frame)).pack(fill="x", pady=5, side="bottom")

# =========================================================
# HOME
# =========================================================
home_frame = tk.Frame(root, bg=BG)
crear_sidebar(home_frame)

main_home = tk.Frame(home_frame, bg=BG)
main_home.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(main_home, text="Pantalla de Inicio",
         bg=BG, font=("Segoe UI", 20, "bold")).pack(anchor="w")

label_user_home = tk.Label(main_home, text="", bg=BG)
label_user_home.pack(anchor="e")

bienvenida = tk.Label(main_home,
                      text="Bienvenido al sistema de trámites de la UTA",
                      bg=BG,
                      font=("Segoe UI", 14, "bold"))
bienvenida.pack(pady=10)

cards_frame = tk.Frame(main_home, bg=BG)
cards_frame.pack(pady=10)

card_values = {}

def crear_card(texto):
    frame = tk.Frame(cards_frame, bg=CARD, width=200, height=120, bd=1, relief="solid")
    frame.pack(side="left", padx=10)
    tk.Label(frame, text=texto, bg=CARD).pack()
    val = tk.Label(frame, text="0", bg=CARD, font=("Segoe UI", 20, "bold"))
    val.pack()
    card_values[texto] = val

crear_card("Citas")
crear_card("Solicitudes")
crear_card("Usuarios")

info_frame = tk.LabelFrame(main_home,
                           text="Documentos o requisitos para realizar el trámite",
                           bg=CARD,
                           font=("Segoe UI", 12, "bold"))
info_frame.pack(fill="both", expand=True, pady=15)

texto_info = tk.Text(info_frame, wrap="word", bg="white")
texto_info.pack(fill="both", expand=True, padx=10, pady=10)

scroll = tk.Scrollbar(texto_info)
scroll.pack(side="right", fill="y")
texto_info.config(yscrollcommand=scroll.set)
scroll.config(command=texto_info.yview)

contenido = """
El trámite requiere de 7 documentos:

1. Forma Migratoria (Para extranjeros)
Los extranjeros deben acreditar su residencia con credencial migratoria vigente.
(No se acepta documentación en trámite).

2. Identificación oficial
Debe ser vigente con fotografía.
Extranjeros: pasaporte vigente.
Si no coincide el domicilio, presentar comprobante.

3. Comprobante de domicilio
No mayor a 2 meses.

4. CURP
Certificado Único de Registro de Población.

5. Comprobante de pago
Debe realizarse durante el trámite.

6. Constancia de estudios
Curso de educación vial (solo primera vez).

7. Pasaporte (extranjeros)
Original y copia.

--------------------------------------------

Criterios de resolución:

- Acreditar curso de vialidad
- Presentar todos los documentos
- Realizar el pago correspondiente
"""

texto_info.insert("1.0", contenido)
texto_info.config(state="disabled")

def actualizar_cards():
    total = len(tabla.get_children())
    for k in card_values:
        card_values[k].config(text=str(total))

# =========================================================
#  TRÁMITES
# =========================================================
tramites_frame = tk.Frame(root, bg=BG)
crear_sidebar(tramites_frame)

main_tramites = tk.Frame(tramites_frame, bg=BG)
main_tramites.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(main_tramites, text="Formulario de Trámite",
         font=("Segoe UI", 20, "bold"),
         bg=BG).pack()

form = tk.Frame(main_tramites, bg=CARD)
form.pack(pady=10)

tk.Label(form, text="Nombre:", bg=CARD).grid(row=0, column=0)
entry_nombre = tk.Entry(form)
entry_nombre.grid(row=0, column=1)
placeholder(entry_nombre, "Ingresa tu nombre")

tk.Label(form, text="Tipo:", bg=CARD).grid(row=1, column=0)
combo = ttk.Combobox(form, values=["Alta", "Baja", "Cambio"])
combo.grid(row=1, column=1)

tk.Label(form, text="Fecha:", bg=CARD).grid(row=2, column=0)
entry_fecha = tk.Entry(form)
entry_fecha.grid(row=2, column=1)
placeholder(entry_fecha, "DD/MM/AAAA")

fechas_ocupadas = ["05/04/2026", "10/04/2026", "15/04/2026"]

def seleccionar_fecha(fecha):
    entry_fecha.delete(0, tk.END)
    entry_fecha.insert(0, fecha)
    entry_fecha.config(fg="black")

cal = tk.Frame(form, bg=CARD)
cal.grid(row=0, column=2, rowspan=5, padx=20)

tk.Label(cal, text="Abril 2026", bg=CARD).pack()

dias = [
    ["", "", "", "1", "2", "3", "4"],
    ["5", "6", "7", "8", "9", "10", "11"],
    ["12", "13", "14", "15", "16", "17", "18"],
    ["19", "20", "21", "22", "23", "24", "25"],
    ["26", "27", "28", "29", "30", "", ""]
]

for fila in dias:
    r = tk.Frame(cal, bg=CARD)
    r.pack()
    for d in fila:
        if d == "":
            tk.Label(r, text="   ", bg=CARD).pack(side="left")
        else:
            fecha = f"{d.zfill(2)}/04/2026"
            color = "red" if fecha in fechas_ocupadas else "black"
            tk.Button(r, text=d, fg=color, bg="white",
                      command=lambda f=fecha: seleccionar_fecha(f)
                      ).pack(side="left", padx=2, pady=2)

def guardar():
    nombre = entry_nombre.get()
    tipo = combo.get()
    fecha = entry_fecha.get()

    if (nombre in ["", "Ingresa tu nombre"] or
        tipo == "" or
        fecha in ["", "DD/MM/AAAA"]):
        messagebox.showerror("Error", "Completa todos los campos")
        return

    tabla.insert("", "end", values=(nombre, tipo, fecha))
    actualizar_cards()
    messagebox.showinfo("Éxito", "Guardado correctamente")

tk.Button(form, text="Guardar", bg="#2563EB", fg="white",
          command=guardar).grid(row=3, column=1, pady=10)

# =========================================================
#  CITAS
# =========================================================
citas_frame = tk.Frame(root, bg=BG)
crear_sidebar(citas_frame)

main_citas = tk.Frame(citas_frame, bg=BG)
main_citas.pack(fill="both", expand=True, padx=20, pady=20)

tk.Label(main_citas, text="Citas Registradas",
         font=("Segoe UI", 20, "bold"),
         bg=BG).pack()

style = ttk.Style()
style.configure("Treeview",
                font=("Segoe UI", 12),
                rowheight=30)
style.configure("Treeview.Heading",
                font=("Segoe UI", 14, "bold"))

tabla = ttk.Treeview(main_citas,
                     columns=("Nombre", "Tipo", "Fecha"),
                     show="headings")

for col in ("Nombre", "Tipo", "Fecha"):
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center", width=200)

tabla.pack(fill="both", expand=True, pady=10)

# =========================================================
# INICIO
# =========================================================
mostrar(login_frame)
root.mainloop()
