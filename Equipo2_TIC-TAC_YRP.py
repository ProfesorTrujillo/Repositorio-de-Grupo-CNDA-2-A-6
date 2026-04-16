import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time # Importo la librería necesaria para gestionar los tiempos 
import os

# Se define la configuración global de las rutas disponibles en el sistema
# Se utiliza como base la información de los recorridos con origen en la Universidad Tecnológica de Aguascalientes
CONFIG_RUTAS = { 
    "Ruta 50 ": {"paradas": 10, "tiempo_base": 8}, 
    "Ruta 50-B": {"paradas": 12, "tiempo_base": 7}, 
    "Ruta 41-penal": {"paradas": 15, "tiempo_base": 10}, 
    "Ruta 25": {"paradas": 8, "tiempo_base": 9} 
} 

def salir_sistema():
    """Cierra la aplicación por completo."""
    ventana.destroy()

def cargar_historial():
    """Lee el archivo de texto y carga los comentarios previos en la lista visual."""
    if os.path.exists("sugerencias.txt"):
        with open("sugerencias.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                lista_comentarios.insert(tk.END, linea.strip())

def guardar_comentario():
    comentario = caja_comentarios.get("1.0", tk.END).strip()
    if comentario:
        registro = f"[{time.strftime('%d/%m/%Y %H:%M')}] Anónimo: {comentario}"
        
        # Se guarda físicamente en el archivo para mantener la memoria tras cerrar el programa
        with open("sugerencias.txt", "a", encoding="utf-8") as archivo:
            archivo.write(registro + "\n")
        
        # Se actualiza la lista visual inmediatamente
        lista_comentarios.insert(tk.END, registro)
        
        messagebox.showinfo("Comentario Guardado", "Gracias por ayudar a brindar un mejor servicio")
        caja_comentarios.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Atención", "Por favor, escribe un comentario antes de guardar.")

def mostrar_soporte():
    lf_monitoreo.pack_forget()
    lf_acceso.pack_forget()
    lf_soporte.pack(fill="both", expand=True, padx=10, pady=10)

def mostrar_panel_control():
    lf_soporte.pack_forget()
    lf_acceso.pack(fill="x", padx=10, pady=5)
    lf_monitoreo.pack(fill="both", expand=True, padx=10, pady=5)

# Se define esta función para la validación del identificador de sesión del usuario
def validar_id_usuario(id_ingresado): 
    # Se verifica que el dato cumpla con el formato global establecido para la activación de la sesión.
    if id_ingresado.isdigit() and len(id_ingresado) == 6: 
        return True 
    else: 
        return False 

def ejecutar_validacion():
    """Maneja la entrada del ID único del usuario."""
    id_id = entrada_id.get()
    if validar_id_usuario(id_id):
        lbl_tarjeta.config(text=f"SESIÓN ACTIVA: {id_id}", fg="#C8E6C9")
        btn_iniciar_ruta.config(state="normal")
        btn_entrar.config(state="disabled")
        entrada_id.config(state="disabled")
    else:
        messagebox.showerror("ID Inválido", "El ID de usuario debe ser de 6 dígitos numéricos.")

# Se define la lógica para el cálculo de aproximación de las paradas restantes
# Se utiliza una operación aritmética para determinar los minutos estimados de llegada a la siguiente parada
def calcular_aproximacion(parada_actual, total_paradas, minutos_base): 
    faltantes = total_paradas - parada_actual 
    tiempo_espera = faltantes * minutos_base 
      
    return faltantes, tiempo_espera 

# Se define este procedimiento para la sincronización del sistema con la plataforma de movilidad
def sincronizar_gps(segundos_pausa): 
    """ 
    Se utiliza para simular la comunicación constante con el servidor central de la CMOV.
    """ 
    # Se utiliza una pausa programada para reflejar el comportamiento del rastreo satelital en tiempo real
    time.sleep(segundos_pausa)

def iniciar_monitoreo():
    """Ejecuta el recorrido dinámico basado en la ruta elegida."""
    btn_iniciar_ruta.config(state="disabled")
    combo.config(state="disabled")
    
    ruta_seleccionada = combo.get()
    datos = CONFIG_RUTAS[ruta_seleccionada]
    total = datos["paradas"]
    base = datos["tiempo_base"]
    
    for p in range(1, total + 1):
        faltantes, tiempo = calcular_aproximacion(p, total, base)
        lbl_camion.config(text=f"UBICACIÓN ACTUAL DEL CAMIÓN: PARADA {p}")
        
        if p < total:
            lbl_paradas.config(text=f"PARADAS RESTANTES A TERMINAL: {faltantes}")
            lbl_tiempo.config(text=f"TIEMPO DE APROXIMACIÓN: {tiempo} MINUTOS")
        else:
            lbl_paradas.config(text="¡HA LLEGADO A SU DESTINO!")
            lbl_tiempo.config(text="UNIDAD EN TERMINAL")
        
        ventana.update()
        sincronizar_gps(0.4) 

    messagebox.showinfo("Viaje Finalizado", f"Has llegado al final de la {ruta_seleccionada}.")
    combo.config(state="readonly")
    btn_iniciar_ruta.config(state="normal", text="Monitorear otra ruta")


ventana = tk.Tk()
ventana.title("GUI_Proyecto_TIC-TAC_YRP")
ventana.geometry("1000x650")
ventana.configure(bg="#9BB7CC")

color_header, color_menu, color_content, color_accent = "#2F4156", "#567C8D", "#519FA1", "#FFFFFF"

# Encabezado
encabezado = tk.Frame(ventana, bg=color_header, height=80)
encabezado.pack(fill="x")
tk.Label(encabezado, text="TIC-TAC RUTA", bg=color_header, fg=color_accent, font=("Segoe UI", 22, "bold")).place(x=20, y=20)
tk.Label(encabezado, text="Coordinación General de Movilidad - Aguascalientes", bg=color_header, fg="#F5EFEB", font=("Segoe UI", 10, "italic")).place(x=25, y=55)

# Menú Lateral
menu = tk.Frame(ventana, bg=color_menu, width=200)
menu.pack(side="left", fill="y")
tk.Button(menu, text="Panel de Control", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 11), command=mostrar_panel_control).pack(fill="x", pady=20, padx=10)
tk.Button(menu, text="Soporte Técnico", bg=color_menu, fg="white", relief="flat", font=("Segoe UI", 11), command=mostrar_soporte).pack(fill="x", pady=10, padx=10)
tk.Button(menu, text="Salir del Sistema", bg="#D32F2F", fg="white", relief="flat", font=("Segoe UI", 11, "bold"), command=salir_sistema).pack(side="bottom", fill="x", pady=20, padx=10)

# Contenido Principal
contenido = tk.Frame(ventana, bg=color_content)
contenido.pack(side="left", fill="both", expand=True, padx=30, pady=30)

# PANEL DE CONTROL
lf_acceso = tk.LabelFrame(contenido, bg=color_content, borderwidth=0)
lf_acceso.pack(fill="x", padx=10, pady=5)
tk.Label(lf_acceso, text="Ingrese su ID de Usuario (6 dígitos):", bg=color_content, font=("Segoe UI", 11), fg=color_accent).grid(row=0, column=0, padx=20, pady=20)
entrada_id = tk.Entry(lf_acceso, width=25, font=("Segoe UI", 11))
entrada_id.grid(row=0, column=1, padx=10)
btn_entrar = tk.Button(lf_acceso, text="Activar Sesión", bg=color_header, fg="white", font=("Segoe UI", 10, "bold"), command=ejecutar_validacion)
btn_entrar.grid(row=0, column=2, padx=20)
lbl_tarjeta = tk.Label(lf_acceso, text="ID REQUERIDO", bg=color_content, fg="yellow", font=("Segoe UI", 9, "bold"))
lbl_tarjeta.grid(row=0, column=3)

lf_monitoreo = tk.LabelFrame(contenido, bg=color_content, borderwidth=0)
lf_monitoreo.pack(fill="both", expand=True, padx=10, pady=5)
tk.Label(lf_monitoreo, text="Seleccionar Ruta:", bg=color_content, font=("Segoe UI", 11), fg=color_accent).place(x=30, y=10)
combo = ttk.Combobox(lf_monitoreo, values=list(CONFIG_RUTAS.keys()), state="readonly")
combo.current(0)
combo.place(x=160, y=12)
btn_iniciar_ruta = tk.Button(lf_monitoreo, text="Ver Ubicación en Tiempo Real", bg="#2F4156", fg="white", font=("Segoe UI", 10, "bold"), state="disabled", command=iniciar_monitoreo)
btn_iniciar_ruta.place(x=350, y=8)
lbl_camion = tk.Label(lf_monitoreo, text="ESPERANDO ACTIVACIÓN...", bg="#C8DDE6", fg="#1B5A5E", font=("Segoe UI", 12, "bold"), width=60, pady=10)
lbl_camion.place(x=30, y=80)
lbl_paradas = tk.Label(lf_monitoreo, text="PARADAS RESTANTES: --", bg="#C4D2FF", fg="#179CF5", font=("Segoe UI", 12, "bold"), width=60, pady=10)
lbl_paradas.place(x=30, y=140)
lbl_tiempo = tk.Label(lf_monitoreo, text="TIEMPO ESTIMADO: --", bg="#BCDBFF", fg="#0CA4BF", font=("Segoe UI", 12, "bold"), width=60, pady=10)
lbl_tiempo.place(x=30, y=200)

# PANEL DE SOPORTE (CON COMENTARIOS DE LOS USUARIOS)
lf_soporte = tk.LabelFrame(contenido, bg=color_content, borderwidth=0)
tk.Label(lf_soporte, text="ATENCIÓN CIUDADANA / BUZÓN DE QUEJAS", bg=color_header, fg="white", font=("Segoe UI", 14, "bold"), pady=10).pack(fill="x", pady=10)

tk.Label(lf_soporte, text="Escribe tu sugerencia aquí:", bg=color_content, fg="white", font=("Segoe UI", 10)).pack(anchor="w", padx=20)
caja_comentarios = tk.Text(lf_soporte, height=3, width=60, font=("Segoe UI", 10))
caja_comentarios.pack(pady=5)

tk.Button(lf_soporte, text="Enviar Sugerencia", bg="#4CAF50", fg="white", font=("Segoe UI", 10, "bold"), command=guardar_comentario).pack(pady=5)

tk.Label(lf_soporte, text="Comentarios de los Usuarios:", bg=color_content, fg="white", font=("Segoe UI", 10, "bold")).pack(anchor="w", padx=20, pady=(10, 0))
frame_lista = tk.Frame(lf_soporte, bg=color_content)
frame_lista.pack(fill="both", expand=True, padx=20, pady=5)

scroll = tk.Scrollbar(frame_lista)
scroll.pack(side="right", fill="y")

lista_comentarios = tk.Listbox(frame_lista, height=5, font=("Segoe UI", 9), yscrollcommand=scroll.set)
lista_comentarios.pack(fill="both", expand=True)
scroll.config(command=lista_comentarios.yview)

# Cargar el historial al iniciar
cargar_historial()

tk.Button(lf_soporte, text="Cerrar Aplicación", bg="#D32F2F", fg="white", font=("Segoe UI", 10, "bold"), command=salir_sistema).pack(pady=10)

ventana.mainloop()
