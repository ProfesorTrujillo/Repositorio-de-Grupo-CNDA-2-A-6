import tkinter as tk
from tkinter import ttk

# ================= VENTANA =================
root = tk.Tk()
root.title("Dashboard UTA")
root.geometry("900x600")
root.config(bg="#EEF2F7")

# ================= ESTILOS =================
COLOR_BG = "#EEF2F7"
COLOR_SIDEBAR = "#0F2A44"
COLOR_CARD = "#FFFFFF"
COLOR_PRIMARY = "#2563EB"
COLOR_TEXT = "#1F2937"

# ================= SIDEBAR =================
sidebar = tk.Frame(root, bg=COLOR_SIDEBAR, width=180)
sidebar.pack(side="left", fill="y")

tk.Label(sidebar, text="UTA\nTI", fg="white", bg=COLOR_SIDEBAR,
         font=("Segoe UI", 16, "bold")).pack(pady=25)

# Botones menú (estilo moderno)
for item in ["Home", "Trámites", "Citas", "Pagos"]:
    btn = tk.Button(sidebar, text=item, fg="white", bg=COLOR_SIDEBAR,
                    activebackground="#163B5F", bd=0,
                    font=("Segoe UI", 11), anchor="w")
    btn.pack(fill="x", padx=15, pady=5)

# ================= HEADER =================
header = tk.Frame(root, bg="white", height=60)
header.pack(fill="x")

tk.Label(header, text="Pantalla de Inicio", bg="white",
         fg=COLOR_TEXT, font=("Segoe UI", 16, "bold")).pack(side="left", padx=20)

tk.Label(header, text="Alexander Misael",
         bg="white", fg="#6B7280").pack(side="right", padx=20)

# ================= CONTENIDO =================
content = tk.Frame(root, bg=COLOR_BG)
content.pack(fill="both", expand=True, padx=15, pady=15)

# ================= TARJETAS =================
cards = tk.Frame(content, bg=COLOR_BG)
cards.pack(pady=10)

def card(texto, valor):
    f = tk.Frame(cards, bg=COLOR_CARD, width=160, height=90)
    f.pack(side="left", padx=10)

    tk.Label(f, text=texto, bg=COLOR_CARD,
             fg="#6B7280", font=("Segoe UI", 10)).pack(pady=5)

    tk.Label(f, text=valor, bg=COLOR_CARD,
             fg=COLOR_TEXT, font=("Segoe UI", 16, "bold")).pack()

card("Citas", "22")
card("Solicitudes", "14")
card("Usuarios", "120")

# ================= TABLA =================
tabla_frame = tk.LabelFrame(content, text="Próximas Citas",
                            bg="white", font=("Segoe UI", 11, "bold"))
tabla_frame.pack(fill="x", pady=10)

tabla = ttk.Treeview(tabla_frame, columns=("Fecha", "Nombre"), show="headings")
tabla.heading("Fecha", text="Fecha")
tabla.heading("Nombre", text="Nombre")

tabla.insert("", "end", values=("16/07/2026", "Alexander"))
tabla.insert("", "end", values=("21/02/2026", "Misael"))

tabla.pack(fill="x", padx=10, pady=10)

# ================= FORMULARIO =================
form = tk.LabelFrame(content, text="Formulario",
                     bg="white", font=("Segoe UI", 11, "bold"))
form.pack(fill="x", pady=10)

tk.Label(form, text="Nombre:", bg="white").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(form).grid(row=0, column=1, padx=10)

tk.Label(form, text="Trámite:", bg="white").grid(row=1, column=0)
ttk.Combobox(form, values=["Alta", "Baja", "Cambio"]).grid(row=1, column=1)

tk.Checkbutton(form, text="Urgente", bg="white").grid(row=2, column=0, pady=5)

op = tk.StringVar()
tk.Radiobutton(form, text="Online", variable=op,
               value="1", bg="white").grid(row=2, column=1)

# Botón estilo moderno
tk.Button(form, text="Enviar",
          bg=COLOR_PRIMARY, fg="white",
          activebackground="#1D4ED8",
          font=("Segoe UI", 10, "bold")).grid(row=3, column=1, pady=10)

# ================= CANVAS =================
canvas = tk.Canvas(content, width=220, height=80, bg="white", highlightthickness=0)
canvas.pack(pady=10)

# Barra tipo gráfica
canvas.create_rectangle(20, 30, 180, 60, fill="#4DA3FF")

# ================= LOOP =================
root.mainloop()